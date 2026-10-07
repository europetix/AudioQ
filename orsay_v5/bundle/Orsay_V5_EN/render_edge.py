#!/usr/bin/env python3
"""edge-tts renderer — V5 edition. Called by generate_audio.command options 1 (Ava, default), 3 (Andrew), 4 (Brian),
and by voice_samples_ES_FR_DE.command.
The voice comes from EDGE_VOICE (default Ava, the chosen English voice). ONLY="015 053" renders just those track numbers (voice samples).
V4.5 rendered each track in one edge-tts call with a fixed rate. V5 performs the direction layer:
each passage gets its own rate/volume/pitch, real silences are inserted for pauses and paragraph
breaks, and the result is mastered to -16 LUFS, 64 kbps mono, 2 s tail.
Tracks without perf/<section>/<name>.perf.txt render as plain paragraphs (still paced + mastered)."""
import sys, os, glob, asyncio, subprocess, tempfile, shutil
import edge_tts
from pronunciation import apply_respelling
import v5_direction as V

VOICE = os.environ.get("EDGE_VOICE", "en-US-AvaMultilingualNeural")
BASE_RATE = -8                  # percent, as in V4.5
BITRATE = "64k"
APPLY_RESPELLING = os.environ.get("RESPELL", "1") != "0"   # RESPELL=0 for Spanish / French / German (respellings are for English voices)
SR = 24000
TIMEOUT_S = float(os.environ.get("EDGE_TIMEOUT", "60"))   # one voice request may take at most this long (it used to wait forever)
TRIES = 3                                                 # attempts per passage before the track is skipped

OUT = sys.argv[1]
ONLY = os.environ.get("ONLY", "").split()
if not shutil.which("ffmpeg"):
    sys.exit("ffmpeg is required for the V5 edge-tts render (pauses + mastering). Run: brew install ffmpeg")


def pct(n):
    return f"{n:+d}%"


async def _say_once(text, style, mp3_path):
    dr, vol, pitch = V.EDGE_STYLE.get(style, V.EDGE_STYLE[None])
    c = edge_tts.Communicate(text, VOICE, rate=pct(BASE_RATE + dr), volume=pct(vol), pitch=f"{pitch:+d}Hz")
    await asyncio.wait_for(c.save(mp3_path), timeout=TIMEOUT_S)


def say(text, style, mp3_path):
    """Voice one passage. A request that hangs or fails is retried (3 tries, short waits in between)."""
    import time
    last = None
    for attempt in range(1, TRIES + 1):
        try:
            if os.path.exists(mp3_path):
                os.remove(mp3_path)
            asyncio.run(_say_once(text, style, mp3_path))
            if os.path.exists(mp3_path) and os.path.getsize(mp3_path) > 0:
                return
            last = "no audio returned"
        except asyncio.TimeoutError:
            last = f"no answer within {TIMEOUT_S:.0f} s"
        except Exception as e:          # network hiccups, service refusals
            last = str(e) or type(e).__name__
        if attempt < TRIES:
            print(f"      (voice service: {last}; trying again, {attempt + 1} of {TRIES})", flush=True)
            time.sleep(3 * attempt)
    raise RuntimeError(f"voice service failed {TRIES} times ({last}). Check the internet connection")


def to_wav(src, dst):
    subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", src,
                    "-ar", str(SR), "-ac", "1", dst], check=True)


def silence_wav(seconds, dst):
    subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-f", "lavfi",
                    "-i", f"anullsrc=channel_layout=mono:sample_rate={SR}", "-t", f"{seconds:.2f}", dst], check=True)


# On trial (7 Oct 2026), off unless set:
#   ROOM_TONE=1  a barely audible room tone under the whole track, so pauses sound like a recording, not a dropout
#   CHIME=1      a soft two-note chime (synthesised here, no licence needed) before the voice starts
ROOM_TONE = os.environ.get("ROOM_TONE") == "1"
CHIME = os.environ.get("CHIME") == "1"
ROOM_TONE_AMP = 0.002          # about -64 dBFS after mastering: heard only in the pauses, on headphones
CHIME_EXPR = ("0.10*(1-exp(-300*t))*exp(-3.2*t)*sin(2*PI*659.25*t)+0.035*(1-exp(-300*t))*exp(-5*t)*sin(2*PI*1318.5*t)"
              "+gte(t,0.18)*(0.10*(1-exp(-300*(t-0.18)))*exp(-3.2*(t-0.18))*sin(2*PI*987.77*(t-0.18))"
              "+0.03*(1-exp(-300*(t-0.18)))*exp(-5*(t-0.18))*sin(2*PI*1975.5*(t-0.18)))")   # E5 then B5, soft bell, ~6 LU under the voice


def chime_wav(dst):
    subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-f", "lavfi", "-i",
                    f"aevalsrc='{CHIME_EXPR}':s={SR}:d=1.4", "-af", "afade=t=out:st=1.0:d=0.4", "-ac", "1", dst], check=True)


def add_room_tone(src, dst):
    noise = f"anoisesrc=color=pink:amplitude={ROOM_TONE_AMP}:sample_rate={SR}"
    subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", src, "-f", "lavfi", "-i", noise,
                    "-filter_complex", "[1:a]highpass=f=120,lowpass=f=4500[n];"
                    "[0:a][n]amix=inputs=2:duration=first:dropout_transition=0,volume=2", "-ac", "1", dst], check=True)


def perform(segs, out_mp3, tmp):
    parts = []
    if CHIME:
        c = os.path.join(tmp, "chime.wav"); chime_wav(c); parts.append(c)
        g = os.path.join(tmp, "chime_gap.wav"); silence_wav(0.45, g); parts.append(g)
    for i, (gap, text, style) in enumerate(segs):
        if gap:
            s = os.path.join(tmp, f"g{i}.wav"); silence_wav(gap, s); parts.append(s)
        m = os.path.join(tmp, f"s{i}.mp3"); w = os.path.join(tmp, f"s{i}.wav")
        say(apply_respelling(text, APPLY_RESPELLING), style, m)
        to_wav(m, w); parts.append(w)
    t = os.path.join(tmp, "tail.wav"); silence_wav(V.TAIL_S, t); parts.append(t)
    lst = os.path.join(tmp, "list.txt")
    with open(lst, "w") as fh:
        fh.writelines(f"file '{p}'\n" for p in parts)
    joined = os.path.join(tmp, "joined.wav")
    subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-f", "concat", "-safe", "0",
                    "-i", lst, "-c", "copy", joined], check=True)
    if ROOM_TONE:
        toned = os.path.join(tmp, "toned.wav"); add_room_tone(joined, toned); joined = toned
    V.master(joined, out_mp3, BITRATE)


V.check_tour(OUT)   # stop early if old and new versions are mixed
failed = []
for sec in sorted(os.listdir("scripts")):
    secdir = os.path.join("scripts", sec)
    if not os.path.isdir(secdir):
        continue
    os.makedirs(os.path.join(OUT, sec), exist_ok=True)
    for f in sorted(glob.glob(os.path.join(secdir, "*.txt"))):
        base = os.path.splitext(os.path.basename(f))[0]
        if ONLY and base[:3] not in ONLY:
            continue
        out = os.path.join(OUT, sec, base + ".mp3")
        if os.path.exists(out):
            print("  [skip]", sec + "/" + base); continue
        perf = os.path.join("perf", sec, base + ".perf.txt")
        if os.path.exists(perf):
            segs = V.segments(V.parse(perf)[1])
        else:
            paras = [p for p in open(f, encoding="utf-8").read().split("\n\n") if p.strip()]
            segs = [(V.PARAGRAPH_GAP_S if i else 0.0, p.strip(), None) for i, p in enumerate(paras)]
        with tempfile.TemporaryDirectory() as tmp:
            try:
                perform(segs, out, tmp)
            except Exception as e:      # skip this track, carry on with the rest; a re-run fills the gap
                print(f"  [FAIL] {sec}/{base}: {e}", flush=True); failed.append(base[:3]); continue
        print("  [gen] ", f"{sec}/{base}.mp3", "(directed)" if os.path.exists(perf) else "(plain)", flush=True)
if failed:
    print(f"\n{len(failed)} track(s) could not be voiced: {' '.join(failed)}")
    print("Run the same command again: finished tracks are skipped, only these are retried.")
    sys.exit(1)
print(VOICE, "render complete ->", OUT)

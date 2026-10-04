#!/usr/bin/env python3
"""edge-tts renderer — V5 edition. Called by generate_audio.command options 1 (Ava, default), 3 (Andrew), 4 (Brian),
and by voice_samples_ES_FR_DE.command.
The voice comes from EDGE_VOICE (default Ava, the chosen English voice). ONLY="015 053" renders just those track numbers (voice samples).
V4.5 rendered each track in one edge-tts call with a fixed rate. V5 performs the direction layer:
each passage gets its own rate/volume/pitch, real silences are inserted for pauses and paragraph
breaks, and the result is mastered to -16 LUFS, 96 kbps mono, 2 s tail.
Tracks without perf/<section>/<name>.perf.txt render as plain paragraphs (still paced + mastered)."""
import sys, os, glob, asyncio, subprocess, tempfile, shutil
import edge_tts
from pronunciation import apply_respelling
import v5_direction as V

VOICE = os.environ.get("EDGE_VOICE", "en-US-AvaMultilingualNeural")
BASE_RATE = -8                  # percent, as in V4.5
BITRATE = "96k"
APPLY_RESPELLING = os.environ.get("RESPELL", "1") != "0"   # RESPELL=0 for Spanish / French / German (respellings are for English voices)
SR = 24000

OUT = sys.argv[1]
ONLY = os.environ.get("ONLY", "").split()
if not shutil.which("ffmpeg"):
    sys.exit("ffmpeg is required for the V5 edge-tts render (pauses + mastering). Run: brew install ffmpeg")


def pct(n):
    return f"{n:+d}%"


async def say(text, style, mp3_path):
    dr, vol, pitch = V.EDGE_STYLE.get(style, V.EDGE_STYLE[None])
    c = edge_tts.Communicate(text, VOICE, rate=pct(BASE_RATE + dr), volume=pct(vol), pitch=f"{pitch:+d}Hz")
    await c.save(mp3_path)


def to_wav(src, dst):
    subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", src,
                    "-ar", str(SR), "-ac", "1", dst], check=True)


def silence_wav(seconds, dst):
    subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-f", "lavfi",
                    "-i", f"anullsrc=channel_layout=mono:sample_rate={SR}", "-t", f"{seconds:.2f}", dst], check=True)


def perform(segs, out_mp3, tmp):
    parts = []
    for i, (gap, text, style) in enumerate(segs):
        if gap:
            s = os.path.join(tmp, f"g{i}.wav"); silence_wav(gap, s); parts.append(s)
        m = os.path.join(tmp, f"s{i}.mp3"); w = os.path.join(tmp, f"s{i}.wav")
        asyncio.run(say(apply_respelling(text, APPLY_RESPELLING), style, m))
        if not os.path.exists(m) or os.path.getsize(m) == 0:
            raise RuntimeError("edge-tts returned no audio (check your internet connection)")
        to_wav(m, w); parts.append(w)
    t = os.path.join(tmp, "tail.wav"); silence_wav(V.TAIL_S, t); parts.append(t)
    lst = os.path.join(tmp, "list.txt")
    with open(lst, "w") as fh:
        fh.writelines(f"file '{p}'\n" for p in parts)
    joined = os.path.join(tmp, "joined.wav")
    subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-f", "concat", "-safe", "0",
                    "-i", lst, "-c", "copy", joined], check=True)
    V.master(joined, out_mp3, BITRATE)


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
            except Exception as e:
                print(f"  [FAIL] {sec}/{base}: {e}"); sys.exit(1)
        print("  [gen] ", f"{sec}/{base}.mp3", "(directed)" if os.path.exists(perf) else "(plain)")
print(VOICE, "render complete ->", OUT)

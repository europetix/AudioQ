#!/usr/bin/env python3
"""Kokoro renderer for the pipeline (invoked by the launcher via `uv run`) — V5 edition.
Same shape as the V4.5 render_kokoro.py: reads scripts/<section>/*.txt, writes <OUT>/<section>/*.mp3.
NEW in V5: if perf/<section>/<name>.perf.txt exists, the track is performed from its direction layer
(pace/volume per passage, real pauses), then mastered to -16 LUFS at 64 kbps with a 2 s tail.
Tracks without a perf file render exactly as before (plain text)."""
import sys, os, glob, shutil
import numpy as np, soundfile as sf
from kokoro import KPipeline
from pronunciation import apply_respelling
import v5_direction as V

VOICE   = "am_michael"     # try bm_lewis for the British narrator option
SPEED   = 0.85             # base pace; 0.85 ~= Brian -8%. Direction scales this per passage.
BITRATE = "64k"            # V5: 64 kbps mono (was 40k, then 96k)
APPLY_RESPELLING = True    # True = phonetic respellings from pronunciation.py; False = native
SR = 24000

OUT = sys.argv[1]
HAVE_FFMPEG = shutil.which("ffmpeg") is not None
if not HAVE_FFMPEG:
    print("WARNING: ffmpeg not found -> writing WAV (large, unmastered). Run: brew install ffmpeg")
pipe = KPipeline(lang_code="a")


def say(text, speed):
    parts = []
    for _, _, a in pipe(text, voice=VOICE, speed=speed):
        a = a.cpu().numpy() if hasattr(a, "cpu") else np.asarray(a)
        parts.append(np.asarray(a, dtype="float32"))
    return np.concatenate(parts) if parts else np.zeros(0, dtype="float32")


def silence(s):
    return np.zeros(int(s * SR), dtype="float32")


def perform(perf_path=None, plain_text=None):
    if perf_path:
        _, body = V.parse(perf_path)
        segs = V.segments(body)
    else:
        segs = [(V.PARAGRAPH_GAP_S if i else 0.0, p, None)
                for i, p in enumerate(t for t in plain_text.split("\n\n") if t.strip())]
    pieces = []
    for gap, text, style in segs:
        mult, gain_db = V.KOKORO_STYLE.get(style, V.KOKORO_STYLE[None])
        if gap:
            pieces.append(silence(gap))
        audio = say(apply_respelling(text, APPLY_RESPELLING), SPEED * mult)
        if gain_db:
            audio = audio * (10 ** (gain_db / 20))
        pieces.append(audio)
    pieces.append(silence(V.TAIL_S))
    return np.concatenate(pieces)


ONLY = os.environ.get("ONLY", "").split()   # e.g. ONLY="015 053" renders just those tracks (voice samples)
V.check_tour(OUT)   # stop early if old and new versions are mixed
for sec in sorted(os.listdir("scripts")):
    secdir = os.path.join("scripts", sec)
    if not os.path.isdir(secdir):
        continue
    os.makedirs(os.path.join(OUT, sec), exist_ok=True)
    for f in sorted(glob.glob(os.path.join(secdir, "*.txt"))):
        base = os.path.splitext(os.path.basename(f))[0]
        if ONLY and base[:3] not in ONLY:
            continue
        ext  = "mp3" if HAVE_FFMPEG else "wav"
        out  = os.path.join(OUT, sec, base + "." + ext)
        if os.path.exists(out):
            print("  [skip]", sec + "/" + base); continue
        perf = os.path.join("perf", sec, base + ".perf.txt")
        if os.path.exists(perf):
            audio = perform(perf_path=perf)
        else:
            audio = perform(plain_text=open(f, encoding="utf-8").read().strip())
        if HAVE_FFMPEG:
            wav = out + ".tmp.wav"
            sf.write(wav, audio, SR)
            V.master(wav, out, BITRATE)
            os.remove(wav)
        else:
            sf.write(out, audio, SR)
        print("  [gen] ", sec + "/" + os.path.basename(out), "%.0fKB" % (os.path.getsize(out) / 1024),
              "(directed)" if os.path.exists(perf) else "(plain)")
print("Kokoro render complete ->", OUT)

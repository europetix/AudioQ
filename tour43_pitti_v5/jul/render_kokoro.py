#!/usr/bin/env python3
"""Kokoro renderer for the V4.5 pipeline (invoked by the launcher via `uv run`).
Reads the raw scripts/ and writes audio to the output dir given as argv[1].
Tweak the settings below to change voice / speed / bitrate / pronunciation."""
import sys, os, glob, shutil, subprocess
import numpy as np, soundfile as sf
from kokoro import KPipeline
from pronunciation import apply_respelling

VOICE   = "am_michael"     # try bm_lewis for the British narrator option
SPEED   = 0.85        # lower = slower; 0.85 ~= Brian -8%
BITRATE = "40k"
PAUSE_S = 5
APPLY_RESPELLING = True     # True = phonetic Italian respellings; False = native

OUT = sys.argv[1]
HAVE_FFMPEG = shutil.which("ffmpeg") is not None
if not HAVE_FFMPEG:
    print("WARNING: ffmpeg not found -> writing WAV (large). Run: brew install ffmpeg")
pipe = KPipeline(lang_code="a")

def synth(text):
    parts = []
    for _, _, a in pipe(text, voice=VOICE, speed=SPEED):
        a = a.cpu().numpy() if hasattr(a, "cpu") else np.asarray(a)
        parts.append(np.asarray(a, dtype="float32"))
    audio = np.concatenate(parts) if len(parts) > 1 else parts[0]
    if PAUSE_S:
        audio = np.concatenate([audio, np.zeros(int(PAUSE_S * 24000), dtype="float32")])
    return audio

for sec in sorted(os.listdir("scripts")):
    secdir = os.path.join("scripts", sec)
    if not os.path.isdir(secdir):
        continue
    os.makedirs(os.path.join(OUT, sec), exist_ok=True)
    for f in sorted(glob.glob(os.path.join(secdir, "*.txt"))):
        base = os.path.splitext(os.path.basename(f))[0]
        ext  = "mp3" if HAVE_FFMPEG else "wav"
        out  = os.path.join(OUT, sec, base + "." + ext)
        if os.path.exists(out):
            print("  [skip]", sec + "/" + base); continue
        text = apply_respelling(open(f, encoding="utf-8").read().strip(), APPLY_RESPELLING)
        audio = synth(text)
        if HAVE_FFMPEG:
            wav = out + ".tmp.wav"
            sf.write(wav, audio, 24000)
            subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", wav,
                            "-ac", "1", "-b:a", BITRATE, out], check=True)
            os.remove(wav)
        else:
            sf.write(out, audio, 24000)
        print("  [gen] ", sec + "/" + os.path.basename(out), "%.0fKB" % (os.path.getsize(out) / 1024))
print("Kokoro render complete ->", OUT)

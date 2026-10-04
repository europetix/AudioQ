"""Sample render of the 3 V5 calibration tracks, am_michael, with the SAME direction logic as
render_kokoro.py (only the Kokoro backend differs: ONNX build here, KPipeline on the Mac)."""
import os, sys, numpy as np, soundfile as sf, time
from kokoro_onnx import Kokoro
import v5_direction as V
from pronunciation import apply_respelling
k = Kokoro("../models/kokoro-v1.0.onnx", "../models/voices-v1.0.bin")
VOICE, SPEED, SR = "am_michael", 0.85, 24000
def say(text, speed):
    a, sr = k.create(text, voice=VOICE, speed=speed, lang="en-us"); return np.asarray(a, dtype="float32")
names = {"016": "V5_016_Throne_Room_Sala_di_Giove", "017": "V5_017_Raphael_La_Velata", "083": "V5_083_Boboli_Amphitheatre"}
for tid, name in names.items():
    t0 = time.time()
    _, body = V.parse(f"../calibration/{tid}.perf.txt")
    pieces = []
    for gap, text, style in V.segments(body):
        mult, gain = V.KOKORO_STYLE.get(style, V.KOKORO_STYLE[None])
        if gap: pieces.append(np.zeros(int(gap * SR), dtype="float32"))
        a = say(apply_respelling(text, True), SPEED * mult)
        pieces.append(a * (10 ** (gain / 20)) if gain else a)
    pieces.append(np.zeros(int(V.TAIL_S * SR), dtype="float32"))
    sf.write(name + ".wav", np.concatenate(pieces), SR)
    V.master(name + ".wav", name + ".mp3"); os.remove(name + ".wav")
    print(f"{name}.mp3 done in {time.time()-t0:.0f}s", flush=True)
print("ALL DONE", flush=True)

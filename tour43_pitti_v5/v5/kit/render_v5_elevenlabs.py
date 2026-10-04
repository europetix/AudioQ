#!/usr/bin/env python3
"""
V5 ElevenLabs renderer — cloned from the pipeline's render_elevenlabs.py (Tour #44 Uffizi), extended
for the V5 direction layer (perf/NNN.perf.txt) and a BLIND voice bake-off.

Runs on YOUR Mac with YOUR ElevenLabs key (never stored; read from the environment):
    export ELEVENLABS_API_KEY=sk_xxx

1) See your voices (add narrator voices from the Voice Library to "My Voices" first):
    python3 render_v5_elevenlabs.py --list-voices
2) Check the cost, nothing is sent:
    python3 render_v5_elevenlabs.py --bakeoff --voices ID1,ID2,ID3 --dry-run
3) Render the blind bake-off (every voice x both models x the 3 calibration tracks):
    python3 render_v5_elevenlabs.py --bakeoff --voices ID1,ID2,ID3
   -> bakeoff/ holds shuffled files (A01_016.mp3 ...), SCORING_SHEET.csv to fill in, and
      _answer_key.csv — DON'T open the key until you've scored.
4) Later, full tour in the winning voice/model:
    python3 render_v5_elevenlabs.py --voices WINNER_ID --models eleven_v3 --out audio_v5
"""
import os, sys, json, argparse, csv, random, glob, re
from pathlib import Path
import urllib.request, urllib.error

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import v5_direction as V

API = "https://api.elevenlabs.io"
CREDIT_RATE = {"eleven_v3": 1.0, "eleven_multilingual_v2": 1.0,
               "eleven_turbo_v2_5": 0.5, "eleven_flash_v2_5": 0.5}
MODEL_CHAR_LIMIT = {"eleven_v3": 3000, "eleven_multilingual_v2": 10000,
                    "eleven_turbo_v2_5": 40000, "eleven_flash_v2_5": 40000}
# eleven_v3 accepts only 0.0 (Creative) / 0.5 (Natural) / 1.0 (Robust) stability.
DEFAULT_SETTINGS = {
    "eleven_v3": {"stability": 0.5, "similarity_boost": 0.80, "style": 0.0, "use_speaker_boost": True},
    "eleven_multilingual_v2": {"stability": 0.45, "similarity_boost": 0.80, "style": 0.15, "use_speaker_boost": True},
}


def api_key():
    k = os.environ.get("ELEVENLABS_API_KEY")
    if not k:
        sys.exit("ERROR: set ELEVENLABS_API_KEY in your environment first (export ELEVENLABS_API_KEY=sk_...).")
    return k


def list_voices():
    req = urllib.request.Request(f"{API}/v1/voices", headers={"xi-api-key": api_key()})
    data = json.load(urllib.request.urlopen(req))
    print(f'{"VOICE_ID":<24} NAME                    accent / age / use-case')
    for v in data.get("voices", []):
        lab = v.get("labels", {}) or {}
        meta = f'{lab.get("accent","-")}/{lab.get("age","-")}/{lab.get("use_case","-")}'
        print(f'{v["voice_id"]:<24} {v.get("name","")[:22]:<22}  {meta}')


def tts(text, voice_id, model_id, settings):
    body = json.dumps({"text": text, "model_id": model_id, "voice_settings": settings}).encode("utf-8")
    req = urllib.request.Request(
        f"{API}/v1/text-to-speech/{voice_id}?output_format=mp3_44100_128", data=body, method="POST",
        headers={"xi-api-key": api_key(), "Content-Type": "application/json", "Accept": "audio/mpeg"})
    try:
        return urllib.request.urlopen(req).read()
    except urllib.error.HTTPError as e:
        sys.exit(f"API error {e.code}: {e.read().decode('utf-8', 'ignore')[:300]}")


def chunks(text, limit):
    """Split at paragraph boundaries so no request exceeds the model's character limit."""
    out, cur = [], ""
    for p in text.split("\n\n"):
        if cur and len(cur) + 2 + len(p) > limit:
            out.append(cur); cur = p
        else:
            cur = f"{cur}\n\n{p}" if cur else p
    if cur:
        out.append(cur)
    too_long = [c for c in out if len(c) > limit]
    if too_long:
        sys.exit(f"A single paragraph exceeds {limit} chars — split it in the perf file.")
    return out


def render_one(path, voice, model, dry):
    meta, body = V.parse(path)
    text = V.for_model(body, model)
    parts = chunks(text, MODEL_CHAR_LIMIT[model])
    chars = sum(len(p) for p in parts)
    if dry:
        return None, chars
    audio = b"".join(tts(p, voice, model, DEFAULT_SETTINGS.get(model, DEFAULT_SETTINGS["eleven_multilingual_v2"]))
                     for p in parts)
    return audio, chars


def main():
    here = Path(os.path.dirname(os.path.abspath(__file__)))
    ap = argparse.ArgumentParser()
    ap.add_argument("--list-voices", action="store_true")
    ap.add_argument("--voices", help="comma-separated ElevenLabs voice_ids")
    ap.add_argument("--models", default="eleven_v3,eleven_multilingual_v2")
    ap.add_argument("--perf-dir", default=str(here / "perf"))
    ap.add_argument("--bakeoff", action="store_true", help="blind A/B: shuffled codes + answer key + scoring sheet")
    ap.add_argument("--out", default=str(here / "audio_v5"))
    ap.add_argument("--dry-run", action="store_true", help="validate + estimate credits; send nothing")
    a = ap.parse_args()

    if a.list_voices:
        list_voices(); return
    if not a.voices:
        sys.exit("Pass --voices ID1,ID2 (use --list-voices to find them).")
    voices = [v.strip() for v in a.voices.split(",") if v.strip()]
    models = [m.strip() for m in a.models.split(",") if m.strip()]
    for m in models:
        if m not in CREDIT_RATE:
            sys.exit(f"Unknown model {m}. Choose from {list(CREDIT_RATE)}")
    perfs = sorted(glob.glob(os.path.join(a.perf_dir, "*.perf.txt")))
    if not perfs:
        sys.exit(f"No *.perf.txt files in {a.perf_dir}")
    for p in perfs:
        V.validate(p)  # tag vocabulary + header check before any credit is spent

    jobs = [(p, v, m) for p in perfs for v in voices for m in models]
    outdir = Path(here / "bakeoff") if a.bakeoff else Path(a.out)
    if not a.dry_run:
        outdir.mkdir(parents=True, exist_ok=True)

    if a.bakeoff:  # one blind code per (voice, model) variant; same code across the 3 tracks
        variants = sorted({(v, m) for _, v, m in jobs})
        random.shuffle(variants)
        code = {vm: f"A{i:02d}" for i, vm in enumerate(variants, start=1)}

    total = 0
    for p, v, m in jobs:
        tid = os.path.basename(p).split(".")[0]
        audio, chars = render_one(p, v, m, a.dry_run)
        total += chars * CREDIT_RATE[m]
        name = f"{code[(v, m)]}_{tid}.mp3" if a.bakeoff else f"{tid}_{v[:8]}_{m}.mp3"
        if audio:
            (outdir / name).write_bytes(audio)
        print(f"  {'(dry) ' if a.dry_run else ''}{name:<34} {chars:>5} chars")

    print(f"\n{len(jobs)} render(s) | ~{total:,.0f} credits")
    if a.bakeoff and not a.dry_run:
        with open(outdir / "_answer_key.csv", "w", newline="") as f:
            w = csv.writer(f); w.writerow(["code", "voice_id", "model"])
            for (v, m), c in sorted(code.items(), key=lambda x: x[1]):
                w.writerow([c, v, m])
        with open(outdir / "SCORING_SHEET.csv", "w", newline="") as f:
            w = csv.writer(f)
            w.writerow(["code", "track", "naturalness_1to5", "pacing_1to5", "pronunciation_1to5",
                        "engagement_1to5", "sounds_like_a_real_storyteller_Y/N", "notes"])
            for c in sorted(code.values()):
                for p in perfs:
                    w.writerow([c, os.path.basename(p).split(".")[0], "", "", "", "", "", ""])
        print(f"Blind files + SCORING_SHEET.csv in {outdir}/ — score before opening _answer_key.csv")


if __name__ == "__main__":
    main()

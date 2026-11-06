#!/usr/bin/env python3
"""V5 direction layer — shared by every renderer (free + paid).
Parses NNN.perf.txt, derives the clean script, and turns direction into what each engine can perform.

FREE ENGINES (Kokoro am_michael, edge-tts Brian) cannot take emotional tags, so direction becomes:
  * per-passage PACE / VOLUME / PITCH  (the delivery tags below)
  * real SILENCE for [pause] / [long pause] and between paragraphs
  * emphasis *word* is dropped (no free engine supports stress marks reliably)
Spec: V5_AUDIO_STANDARD.md §3."""
import re, subprocess

DELIVERY = ["warmly", "quietly", "amused", "curious", "conspiratorial", "reverent", "wry", "lightly"]
TAG_RE = re.compile(r"\[(long pause|pause|" + "|".join(DELIVERY) + r")\]\s*")
ANY_BRACKET = re.compile(r"\[[^\]]*\]")
EMPH_RE = re.compile(r"\*([^*]+)\*")

PAUSE_S = {"pause": 0.55, "long pause": 1.1}
PARAGRAPH_GAP_S = 0.75
TAIL_S = 2.0

# Free-engine delivery profiles. Kokoro: speed multiplier + gain (dB). edge-tts: rate/volume/pitch offsets.
# A tag colours the rest of its paragraph (or until the next delivery tag). Neutral = no tag.
KOKORO_STYLE = {          # (speed x, gain dB)
    None:             (1.00,  0.0),
    "warmly":         (0.96,  0.0),
    "quietly":        (0.92, -3.0),
    "amused":         (1.03,  0.5),
    "curious":        (1.00,  0.0),
    "conspiratorial": (0.93, -2.5),
    "reverent":       (0.91, -2.0),
    "wry":            (1.01,  0.0),
    "lightly":        (1.04,  0.5),
}
EDGE_STYLE = {            # (rate % added to base, volume %, pitch Hz)
    None:             (0,   0,  0),
    "warmly":         (-3,  0, -1),
    "quietly":        (-7, -15, -2),
    "amused":         (+3,  0, +3),
    "curious":        (0,   0, +2),
    "conspiratorial": (-6, -10, -2),
    "reverent":       (-8, -8, -3),
    "wry":            (+1,  0, +1),
    "lightly":        (+4,  0, +3),
}


def parse(path):
    raw = open(path, encoding="utf-8").read()
    head, _, body = raw.partition("\n---\n")
    meta = {}
    for line in head.splitlines():
        if line.startswith("@") and ":" in line:
            k, v = line[1:].split(":", 1)
            meta[k.strip()] = v.strip()
    return meta, body.strip()


def _tidy(s):
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r" +([,.;:!?])", r"\1", s)
    return "\n\n".join(p.strip() for p in s.split("\n\n") if p.strip())


def clean(body):
    """Exactly what the PDF prints and the listener hears (tags removed, *emphasis* unmarked)."""
    return _tidy(EMPH_RE.sub(r"\1", TAG_RE.sub("", body)))


def validate(path, clean_text=None):
    meta, body = parse(path)
    for k in ("brief", "pace", "energy"):
        if k not in meta:
            raise ValueError(f"{path}: missing @{k}")
    unknown = ANY_BRACKET.findall(TAG_RE.sub("", body))
    if unknown:
        raise ValueError(f"{path}: unknown tag(s) {unknown}")
    c = clean(body)
    if clean_text is not None and c != _tidy(clean_text):
        raise ValueError(f"{path}: clean text differs from the approved script")
    return meta, c


def segments(body):
    """-> list of (silence_before_s, text, style). Silence comes from [pause]/[long pause] and paragraph gaps."""
    out = []
    paras = [p.strip() for p in body.split("\n\n") if p.strip()]
    for pi, para in enumerate(paras):
        style, pending = None, (PARAGRAPH_GAP_S if pi else 0.0)
        pos = 0
        for m in TAG_RE.finditer(para):
            chunk = EMPH_RE.sub(r"\1", para[pos:m.start()]).strip()
            if chunk:
                out.append((pending, chunk, style)); pending = 0.0
            tag = m.group(1)
            if tag in PAUSE_S:
                pending = max(pending, PAUSE_S[tag])
            else:
                style = tag
            pos = m.end()
        chunk = EMPH_RE.sub(r"\1", para[pos:]).strip()
        if chunk:
            out.append((pending, chunk, style))
    return out


# Voice finishing (ON by default since the user chose A/B version D, 7 Oct 2026; VOICE_FINISH=0 turns it off): rumble cut, a touch of warmth and presence, gentle de-essing,
# light compression so quiet words stay audible in a noisy gallery. Applied before the loudness normalisation.
VOICE_FINISH_AF = ("highpass=f=80,equalizer=f=200:t=q:w=1:g=1.5,equalizer=f=3200:t=q:w=1.4:g=1.5,"
                   "deesser=i=0.35:m=0.5:f=0.5,acompressor=threshold=-21dB:ratio=2.5:attack=10:release=150:makeup=1.5")


def master(wav_in, mp3_out, bitrate="64k"):
    """Two-pass loudness normalisation to -16 LUFS / -1.5 dBTP (spoken word on phones), mono MP3.
    Pass 1 measures, pass 2 applies a linear gain so pauses don't skew the result."""
    import json, os
    target = "I=-16:TP=-1.5:LRA=11"
    pre = VOICE_FINISH_AF + "," if os.environ.get("VOICE_FINISH", "1") != "0" else ""
    r = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", wav_in, "-af",
                        f"{pre}loudnorm={target}:print_format=json", "-f", "null", "-"],
                       capture_output=True, text=True)
    blob = r.stderr[r.stderr.rindex("{"):r.stderr.rindex("}") + 1]
    m = json.loads(blob)
    af = (f"{pre}loudnorm={target}:measured_I={m['input_i']}:measured_TP={m['input_tp']}:"
          f"measured_LRA={m['input_lra']}:measured_thresh={m['input_thresh']}:"
          f"offset={m['target_offset']}:linear=true")
    part = f"{mp3_out}.{os.getpid()}.part.mp3"   # write aside, then rename: an interrupted run never leaves a half file
    subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", wav_in,
                    "-af", af, "-ar", "24000", "-ac", "1", "-b:a", bitrate, part], check=True)
    import os
    os.replace(part, mp3_out)


def check_tour(out_dir):
    """Stop before voicing anything if this folder mixes tour versions.
    Scripts must match plan.json one-to-one (a new zip unzipped over an old one leaves old scripts behind),
    and the output folder must not already hold MP3s from another version (finished tracks are skipped, never replaced)."""
    import os, sys, glob, json
    plan = next((p for p in ("plan.json", "../plan.json", "../../plan.json") if os.path.exists(p)), None)
    if not plan:
        return
    expected = {t["seq"] for t in json.load(open(plan, encoding="utf-8"))["tracks"]}
    found = {}
    for f in glob.glob(os.path.join("scripts", "*", "*.txt")):
        found.setdefault(os.path.basename(f)[:3], []).append(f)
    extra = sorted(n for n in found if n not in expected)
    doubled = sorted(n for n, fs in found.items() if len(fs) > 1)
    missing = sorted(expected - set(found))
    if extra or doubled or missing:
        print("\nSTOP: this tour folder mixes two versions of the guide.")
        print(f"  The plan has {len(expected)} tracks; the scripts folder has {sum(map(len, found.values()))} files.")
        if extra:   print("  Not in this version:", " ".join(extra[:12]))
        if doubled: print("  Two scripts with the same number:", " ".join(doubled[:12]))
        if missing: print("  Missing:", " ".join(missing[:12]))
        print("  Fix: move this folder away, unzip the guide again into an empty place, and run it from there.")
        sys.exit(1)
    # one render per output folder: a second copy writing the same files makes both fail
    os.makedirs(out_dir, exist_ok=True)
    lock = os.path.join(out_dir, ".render.lock")
    if os.path.exists(lock):
        try:
            pid = int(open(lock).read().strip() or 0)
            os.kill(pid, 0)
            alive = pid != os.getpid()
        except (ValueError, ProcessLookupError, PermissionError, OSError):
            alive = False
        if alive:
            print(f"\nSTOP: another render (process {pid}) is already writing to\n    {out_dir}")
            print("  Let it finish, or stop it first:  pkill -f render_edge.py")
            sys.exit(1)
    open(lock, "w").write(str(os.getpid()))
    import atexit
    atexit.register(lambda: os.path.exists(lock) and open(lock).read().strip() == str(os.getpid()) and os.remove(lock))
    current = {os.path.splitext(os.path.basename(f))[0] for fs in found.values() for f in fs}
    stale = [f for f in glob.glob(os.path.join(out_dir, "*", "*.mp3")) + glob.glob(os.path.join(out_dir, "*", "*.wav"))
             if not f.endswith((".part.mp3", ".tmp.wav")) and os.path.splitext(os.path.basename(f))[0] not in current]
    if stale:
        print(f"\nSTOP: the output folder already holds {len(stale)} audio file(s) from another version, e.g.")
        for f in sorted(stale)[:3]:
            print("   ", os.path.relpath(f, out_dir))
        print(f"  Fix: move or rename this folder, then run again:\n    {out_dir}")
        sys.exit(1)

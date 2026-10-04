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


def master(wav_in, mp3_out, bitrate="96k"):
    """Two-pass loudness normalisation to -16 LUFS / -1.5 dBTP (spoken word on phones), mono MP3.
    Pass 1 measures, pass 2 applies a linear gain so pauses don't skew the result."""
    import json
    target = "I=-16:TP=-1.5:LRA=11"
    r = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", wav_in, "-af",
                        f"loudnorm={target}:print_format=json", "-f", "null", "-"],
                       capture_output=True, text=True)
    blob = r.stderr[r.stderr.rindex("{"):r.stderr.rindex("}") + 1]
    m = json.loads(blob)
    af = (f"loudnorm={target}:measured_I={m['input_i']}:measured_TP={m['input_tp']}:"
          f"measured_LRA={m['input_lra']}:measured_thresh={m['input_thresh']}:"
          f"offset={m['target_offset']}:linear=true")
    part = mp3_out + ".part.mp3"   # write aside, then rename: an interrupted run never leaves a half file
    subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", wav_in,
                    "-af", af, "-ar", "24000", "-ac", "1", "-b:a", bitrate, part], check=True)
    import os
    os.replace(part, mp3_out)

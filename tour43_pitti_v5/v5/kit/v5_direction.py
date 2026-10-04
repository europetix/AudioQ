#!/usr/bin/env python3
"""V5 direction layer: parse NNN.perf.txt, derive the clean script, and translate tags per engine.
Spec: V5_AUDIO_STANDARD.md §3. The clean script (tags stripped) is the single source of truth for
the PDF and the audio text; validate() guarantees the perf file reproduces it exactly."""
import re

DELIVERY = ["warmly", "quietly", "amused", "curious", "conspiratorial", "reverent", "wry", "lightly"]
TAG_RE = re.compile(r"\[(long pause|pause|" + "|".join(DELIVERY) + r")\]\s*")
ANY_BRACKET = re.compile(r"\[[^\]]*\]")
EMPH_RE = re.compile(r"\*([^*]+)\*")


def parse(path):
    """-> (meta: dict, body: str). Header lines '@key: value' until a line '---'."""
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
    """Tags removed, *emphasis* unmarked -> exactly what the PDF prints and the listener hears."""
    s = TAG_RE.sub("", body)
    s = EMPH_RE.sub(r"\1", s)
    return _tidy(s)


def for_model(body, model):
    """Engine text. v3: pauses -> ellipses, delivery tags kept, *word* -> WORD.
    v2 (and anything else): SSML breaks for pauses, delivery tags + emphasis removed."""
    if model == "eleven_v3":
        s = body.replace("[long pause]", "… …").replace("[pause]", "…")
        s = EMPH_RE.sub(lambda m: m.group(1).upper(), s)
    else:
        s = body.replace("[long pause]", '<break time="1.2s" />').replace("[pause]", '<break time="0.6s" />')
        s = re.sub(r"\[(" + "|".join(DELIVERY) + r")\]\s*", "", s)
        s = EMPH_RE.sub(r"\1", s)
    return _tidy(s)


def validate(path, clean_text=None):
    """Raise on unknown tags; if clean_text given, require exact match after stripping."""
    meta, body = parse(path)
    for k in ("brief", "pace", "energy"):
        if k not in meta:
            raise ValueError(f"{path}: missing @{k}")
    unknown = [t for t in ANY_BRACKET.findall(TAG_RE.sub("", body))]
    if unknown:
        raise ValueError(f"{path}: unknown tag(s) {unknown}")
    c = clean(body)
    if clean_text is not None and c != _tidy(clean_text):
        raise ValueError(f"{path}: clean text differs from the approved script")
    return meta, c

#!/usr/bin/env python3
"""Prado V5 lint: python3 lint.py [NNN ...]  -> one line per track, 'OK' or the problems."""
import sys, os, re, glob
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "pipeline"))
import v5_direction as V
RANGE = {"R": (180, 280), "W": (250, 360), "ANCHOR": (250, 360), "CLOSE": (250, 360)}
HEAD = ["id", "section", "room", "type", "title", "where", "what", "listen", "brief", "pace", "energy", "sources"]
files = sorted(glob.glob(os.path.join(os.path.dirname(__file__), "tracks", "*.perf.txt")))
want = set(sys.argv[1:])
bad = 0
for f in files:
    n = os.path.basename(f)[:3]
    if want and n not in want: continue
    p = []
    try:
        meta, c = V.validate(f)
    except Exception as e:
        print(n, "ERROR", e); bad += 1; continue
    for k in HEAD:
        if not meta.get(k): p.append(f"missing @{k}")
    w = len(c.split()); lo, hi = RANGE.get(meta.get("type"), (180, 360))
    if not lo <= w <= hi: p.append(f"{w} words (want {lo}-{hi})")
    if ";" in c or "(" in c or ")" in c: p.append("; or ( in speech")
    if c.count("—") > 2: p.append(f"{c.count('—')} em-dashes")
    if re.search(r"next track|track \d|play track", c, re.I): p.append("says 'next track'")
    if len(re.findall(r"the museum says", c, re.I)) > 1: p.append("'the museum says' >1")
    if re.search(r"\b(ticket|opening hours|euro|€)", c, re.I): p.append("tickets/hours/prices")
    if "!" in c: p.append("exclamation mark")
    last = c.split("\n\n")[-1]
    if meta.get("type") != "CLOSE" and not re.search(r"Room \d|Floor \d|hall|Rooms \d", last): p.append("last paragraph has no room cue")
    if re.match(r"^(Stand|Look|Walk|Turn|Go|Find|Step|Come|Move)\b", c): p.append("opens with a command")
    print(n, "OK" if not p else "; ".join(p), f"({w}w)")
    bad += bool(p)
sys.exit(1 if bad else 0)

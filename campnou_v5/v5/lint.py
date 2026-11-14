#!/usr/bin/env python3
"""Camp Nou / Barça Museum V5 lint: python3 lint.py [NNN ...]  -> one line per track, 'OK' or the problems."""
import sys, os, re, glob
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "pipeline"))
import v5_direction as V
RANGE = {"R": (180, 280), "W": (250, 360), "ANCHOR": (250, 360), "CLOSE": (250, 360), "X": (150, 230)}
HEAD = ["id", "section", "room", "type", "title", "where", "what", "listen", "brief", "pace", "energy", "sources"]
TDIR = os.environ.get("TRACKS_DIR") or os.path.join(os.path.dirname(__file__), "tracks")
files = sorted(glob.glob(os.path.join(TDIR, "*.perf.txt"))) + sorted(glob.glob(os.path.join(os.path.dirname(__file__), "extras", "*.perf.txt")))
want = set(sys.argv[1:])
bad = 0
for f in files:
    n = os.path.basename(f).split(".")[0]
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
    if re.search(r"\b(ticket prices?|buy (your )?tickets?|book (your )?tickets?|online tickets?|opening hours|(?<!billion )(?<!million )euros?\b)|€", c, re.I): p.append("tickets/hours/prices")
    if re.search(r"\b(Gamper|Sunyol|Kubala|Cruyff|Samitier|Maradona|Franco|Miró-Sans|Mitjans|Carreras|Montal|Núñez|Vázquez Montalbán|Zamora|Alcántara|Suárez Miramontes|Helenio Herrera|Tito Vilanova|Wild) (is|says|tells|thinks|wants|believes|writes|calls|adds|describes|explains|plays|scores)\b", c): p.append("present tense for a dead person")
    n=meta.get("id","")[:3]
    bans=[(r"Nou Camp",()),(r"biggest stadium in the world|largest stadium in the world",()),(r"napkin[^.]*(here|in (this|the) museum|on (show|display))|(here|on (show|display))[^.]*napkin",()),(r"eight Ballons? d.Or (at|for|with|as a player (at|of|for)) Barça|won eight[^.]*(at|for|with) Barça",()),(r"Messi statue|statue of Messi",()),(r"Un sentiment|és un sentiment|not a club, it.s a feeling",()),(r"eleven founders|Gamper[^.]*first president",()),(r"five (lost )?(European )?finals",()),(r"exhum",()),(r"two hours",()),(r"demolition",()),(r"RoboKeeper|Robokeeper|virtual reality|Virtual Dream|\bVR\b",()),(r"deepfake|hologram",()),(r"Legia",()),(r"Kubala[^.]*built (the|this)|built for Kubala|house (that )?Kubala built",()),(r"Salid y disfrutad",()),(r"free (entry|admission)",()),(r"\beastern\b|\bwestern\b|south side|north side|southern|northern",()),(r"regime.s club|Franco.s (team|club)",()),(r"Access \d|Gate \d|Accés",()),(r"(Masia|farmhouse)[^.]*(over there|behind you|to your|in front of you)",())]
    for rx,ok in bans:
        if n not in ok and re.search(rx,c,re.I): p.append("NEVER-list wording: "+rx[:30])
    if re.search(r"\b(speaker|play (it|this) (aloud|out loud))\b", c, re.I) and meta.get("type")!="ANCHOR": p.append("speaker mention outside 001")
    if re.search(r"\*[A-Za-zÀ-ÿ]", c): p.append("stress asterisk")
    if "!" in c: p.append("exclamation mark")
    last = c.split("\n\n")[-1]
    if meta.get("type") != "CLOSE" and not re.search(r"[Mm]useum|[Rr]oom|[Dd]oor|[Ww]all|[Cc]abinet|[Cc]ase|[Dd]isplay|[Ss]creen|[Tt]roph|[Cc]ups?\b|[Ss]hirts?|[Bb]alls?\b|[Bb]alcony|[Vv]iewpoint|[Mm]odel|[Bb]ench|[Ss]tadium|[Gg]ate|[Ee]ntrance|[Ee]xit|way out|[Qq]ueue|[Pp]alau|[Aa]rena|[Ss]igns?\b|[Hh]all|[Cc]orner|[Ss]pace|[Ss]tairs?|[Ll]ift|[Ss]ection|[Zz]one|[Cc]olumns?", last): p.append("last paragraph has no room cue")
    if re.match(r"^(Stand|Look|Walk|Turn|Go|Find|Step|Come|Move)\b", c): p.append("opens with a command")
    print(n, "OK" if not p else "; ".join(p), f"({w}w)")
    bad += bool(p)
sys.exit(1 if bad else 0)

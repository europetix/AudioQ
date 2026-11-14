#!/usr/bin/env python3
"""Barcelona Cathedral V5 lint: python3 lint.py [NNN ...]  -> one line per track, 'OK' or the problems."""
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
    if re.search(r"\b(Gaudí|Bermejo|Lochner|Ordóñez|Sanglada|Fabre|Gual|Carlí|Mestres|Girona|Martorell|Desplà|Oleguer|Penyafort|Lupo|Eulàlia|Almodis|Charles|Pere) (is|says|tells|thinks|wants|believes|writes|calls|adds|describes|explains)\b", c): p.append("present tense for a dead person")
    n=meta.get("id","")[:3]
    bans=[(r"alabaster(?![^.]*(Oleguer|effigy|figure))",("008","022")),(r"\b1448\b",("029",)),(r"UNESCO",()),(r"Sagrada Fam",("001",)),(r"hockey|mermaid|three queens",()),(r"Henry VIII|Francis I\b|Manuel I\b|Christian II",()),(r"Louis II",("018",)),(r"Governor of Dacia|\bscarlet\b|hung in black",()),(r"Oller[^.]*tomb|tomb[^.]*Oller",()),(r"empty (chairs|seats|stalls)",()),(r"soup kitchen|refectory for the poor|poor people's (dining|refectory)",()),(r"Diocesan Museum",()),(r"free (entry|admission)",()),(r"first victim",()),(r"\b878\b|\b1046\b",()),(r"\b1327\b",("023",)),(r"sixteenth[- ]century (Christ|crucifix|carving)",()),(r"anarchist|\bArian\b",()),(r"GVAM|Talaia|augmented|virtual",()),(r"\bBorra\b|Palou|Espartero|emptied|\brode\b",()),(r"Gaudí (built|designed) (the|this)",()),(r"(facade|front)[^.]*seventy metres|fifty-three metres",()),(r"\bcopatron|patron saint of Barcelona",()),(r"Eiffel",()),(r"Columbus brought",("010",)),(r"knife|knives|cana destra",()),(r"tombstones?",("031",)),(r"(chapel|capella) (number|no\.?) ?\d",()),(r"scaffold",()),(r"\beastern\b|\bwestern\b|south side|north side",())]
    for rx,ok in bans:
        if n not in ok and re.search(rx,c,re.I): p.append("NEVER-list wording: "+rx[:30])
    if re.search(r"\b(speaker|play (it|this) (aloud|out loud))\b", c, re.I) and meta.get("type")!="ANCHOR": p.append("speaker mention outside 001")
    if re.search(r"\*[A-Za-zÀ-ÿ]", c): p.append("stress asterisk")
    if "!" in c: p.append("exclamation mark")
    last = c.split("\n\n")[-1]
    if meta.get("type") != "CLOSE" and not re.search(r"[Ss]quare|Plaça|Pla de la Seu|[Ss]eu|[Ff]acade|[Dd]oor|[Cc]hapel|[Ss]creen|[Aa]isle|[Ll]ift|[Rr]oof|[Tt]errace|[Cc]hoir|[Cc]rypt|[Ss]tair|[Ss]teps|[Aa]ltar|[Cc]loister|[Hh]all|[Ff]ountain|[Pp]ond|[Gg]eese|[Tt]ower|[Bb]aptistery|[Aa]mbulatory|[Ss]acristy|[Nn]ave|[Ee]xit|way out|[Qq]ueue|[Gg]ate|[Ww]all|[Cc]orner|[Aa]rch|[Mm]useum|[Rr]oom", last): p.append("last paragraph has no room cue")
    if re.match(r"^(Stand|Look|Walk|Turn|Go|Find|Step|Come|Move)\b", c): p.append("opens with a command")
    print(n, "OK" if not p else "; ".join(p), f"({w}w)")
    bad += bool(p)
sys.exit(1 if bad else 0)

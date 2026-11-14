#!/usr/bin/env python3
"""Split de_src/batch*.txt (=== NNN / T: / W: / --- / body) into de/NNN.json; then copy bridges."""
import glob, json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(os.path.dirname(HERE), "de")
os.makedirs(OUT, exist_ok=True)
n_done = []
for f in sorted(glob.glob(os.path.join(HERE, "batch*.txt"))):
    txt = open(f, encoding="utf-8").read()
    for chunk in re.split(r"^=== ", txt, flags=re.M)[1:]:
        num, _, rest = chunk.partition("\n")
        head, _, body = rest.partition("\n---\n")
        t = re.search(r"^T: (.*)$", head, re.M).group(1).strip()
        w = re.search(r"^W: (.*)$", head, re.M).group(1).strip()
        body = re.sub(r"\n{3,}", "\n\n", body.strip())
        json.dump({"title": t, "where": w, "body": body},
                  open(os.path.join(OUT, f"{num.strip()}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        n_done.append(num.strip())
print("wrote", len(n_done), n_done)

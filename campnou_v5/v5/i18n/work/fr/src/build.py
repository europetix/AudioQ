import json, os, sys, glob, importlib.util, re
W = os.path.dirname(os.path.abspath(__file__))
OUT = "/tmp/claude-0/-home-claude/98e7af58-dd32-56e0-a687-5f082c01b624/scratchpad/cn_i18n/fr"
os.makedirs(OUT, exist_ok=True)
T, B = {}, {}
for f in sorted(glob.glob(os.path.join(W, "tr_*.py"))):
    spec = importlib.util.spec_from_file_location(os.path.basename(f)[:-3], f); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    T.update(getattr(m, "T", {})); B.update(getattr(m, "B", {}))
for n, d in T.items():
    body = "\n\n".join(p.strip() for p in d["body"].strip().split("\n\n"))
    json.dump({"title": d["title"].strip(), "where": d["where"].strip(), "body": body}, open(os.path.join(OUT, n + ".json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
# bridges
en = []
for f in sorted(glob.glob("/home/claude/audioq/campnou_v5/v5/bridges/*.txt")):
    for line in open(f, encoding="utf-8"):
        line = line.strip()
        if line and not line.startswith("#"):
            k, _, t = line.partition(": "); en.append((k, t))
lines = []
for k, t in en:
    if k in B:
        fr = B[k].strip(); lines.append(f"{k}: {fr}")
        ew, fw = len(t.split()), len(fr.split())
        print("bridge", k, f"{fw}/{ew}", "OK" if fw <= ew and fr.startswith("Dans cette version courte,") else "BAD")
    else:
        print("bridge", k, "MISSING")
open(os.path.join(OUT, "bridges.txt"), "w", encoding="utf-8").write("\n".join(lines) + "\n")
# title/cue consistency: every " · " cue at end of a body must match some title
titles = {n: d["title"].strip() for n, d in T.items()}
allt = set(titles.values())
for n, d in T.items():
    last = d["body"].strip().split("\n\n")[-1]
    for m in re.finditer(r": ([^:]*? · [^.]*?)\.(?:\s|$)", last):
        if m.group(1) not in allt: print("CUE?", n, m.group(1))
for k in B:
    m = re.search(r": ([^:]*? · .*?)\.$", B[k].strip())
    if not m or m.group(1) not in allt: print("BRIDGE CUE?", k, m and m.group(1))

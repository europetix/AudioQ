import sys,re
sys.path.insert(0,"/home/claude/audioq/campnou_v5/v5/pipeline"); import v5_direction as V
for n in sys.argv[1:]:
    t=open(f"/home/claude/audioq/campnou_v5/v5/tracks/{n}.perf.txt").read()
    h,_,b=t.partition("\n---\n")
    ti=re.search(r"^@title: (.*)$",h,re.M).group(1); w=re.search(r"^@where: (.*)$",h,re.M).group(1)
    print(f"=== {n} [{len(V.clean(b).split())}w]\nTITLE: {ti}\nWHERE: {w}\n{b}")

import sys,json
p=sys.argv[1]; R=json.load(open(sys.argv[2])); s=open(p).read()
for a,b in R:
    if s.count(a)!=1: print("MISS",s.count(a),a[:60]); continue
    s=s.replace(a,b)
open(p,"w").write(s)

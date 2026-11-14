import json,re,glob,sys
W="/tmp/claude-0/-home-claude/98e7af58-dd32-56e0-a687-5f082c01b624/scratchpad/gue_i18n/fr"
EN="/home/claude/audioq/guell_v5/v5/tracks"
def cue(t): return t.replace(" — "," · ")
fr={};en={}
for i in range(1,46):
    n=f"{i:03d}"; d=json.load(open(f"{W}/{n}.json")); fr[n]=d
    en[n]=open(f"{EN}/{n}.perf.txt").read()
frc={cue(d["title"]):n for n,d in fr.items()}
enc={}
for n,t in en.items():
    enc[cue(re.search(r"^@title: (.*)$",t,re.M).group(1))]=n
def find(text,table):
    return [table[c] for c in table if c in text]
bad=0
for n in fr:
    eb=en[n].partition("\n---\n")[2]
    ef=sorted(set(find(eb,enc))); ff=sorted(set(find(fr[n]["body"],frc)))
    if ef!=ff: print(n,"EN->",ef,"FR->",ff); bad+=1
print("cue mismatches",bad)
if len(sys.argv)>1:
    for line in open(sys.argv[1]):
        if re.match(r"^\d{3} [HE]>\d{3}:",line):
            k=line[:9]; dest=k[6:9]
            ok=line.rstrip().endswith(cue(fr[dest]["title"])+".")
            if not ok: print("bridge cue bad",k)

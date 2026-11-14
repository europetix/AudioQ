import json,sys
sys.path.insert(0,"/home/claude/audioq/guell_v5/v5/pipeline"); import v5_direction as V
W="/tmp/claude-0/-home-claude/98e7af58-dd32-56e0-a687-5f082c01b624/scratchpad/gue_i18n/fr"
for n in sys.argv[1:]:
    fr=V.clean(json.load(open(f"{W}/{n}.json"))["body"]).split("\n\n")
    en=V.clean(open(f"/home/claude/audioq/guell_v5/v5/tracks/{n}.perf.txt").read().partition("\n---\n")[2]).split("\n\n")
    print(n, [ (len(a.split()),len(b.split())) for a,b in zip(fr,en)])

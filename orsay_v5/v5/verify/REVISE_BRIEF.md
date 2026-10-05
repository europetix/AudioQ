# Revision brief — Orsay V5 (5 Oct 2026)
Revise ONLY your assigned tracks in /home/user/AudioQ/orsay_v5/v5/tracks/. Keep the format, tags and house style
(/home/user/AudioQ/orsay_v5/v5/WRITER_BRIEF.md rules still apply: lengths, no ; ( , ≤2 dashes, only allowed tags, facts only from
research/FACTS_R1–R5 + findings A1/A2/A3/G graded OFF/SEC2). No web research. Track 052 (Gauguin, Cheval blanc) is HELD (moved to
v5/held/): 051's closing cue must now lead to Sérusier's Talisman (053); nobody may mention the White Horse.
Inputs: /home/user/AudioQ/orsay_v5/v5/verify/V1_001-023.md, V2_024-046.md, V3_047-067.md, T_traveller_review.md, and the
"Coordinator decisions" at the end of /home/user/AudioQ/orsay_v5/v5/PLAN.md.

Apply, for your tracks:
1. EVERY CONTRA / NOTFOUND / WEAK / rule fix in the V reports (use their replacement sentence or cut; never add unsourced detail).
   Unsourced glosses ("Bastille Day", "President Giscard", "Roman poet", "novelist"…) are cut or replaced by sourced wording.
2. Coordinator decisions: 029 — remove the Renoir/station story entirely, no mention at all.
3. AUTHORITY: "the museum says / calls / notes / tells us / describes / writes" — at most ONE per track, only where attribution
   matters (an interpretation or a quote). Elsewhere state the sourced fact plainly. Never correct "older guides" or "some books".
4. NO spoken doubt about our own research ("nobody has documented…", "I can't tell you…"). If a detail isn't sourced, don't mention it.
5. LOAN FALLBACKS must work for a listener standing at the stand-in: 008 (Gleaners → L'Angélus), 044 (Starry Night → Bedroom /
   self-portrait), 051 (Arearea → Femmes de Tahiti). Structure: ONE sentence near the start ("If this wall is empty — the painting
   travels to Tokyo this winter — walk to X, which hangs nearby, and listen there"), then the main story written so that it
   still makes sense in front of X (no "look at the empty wall" instructions after that point; describe the loaned work in the
   past or in words, then give X its own look-moment). The preceding track's cue (050 → Arearea, 007 → Gleaners, 043 → Starry
   Night) gets a short "if it's away" hint.
6. 016 hedge: play it in room 18 (official); if the painting has moved, the card says so. Its cue must still work from room 18.
7. LEVEL CHANGES: 054 → level 2: say how (stairs/lift down to level 2), then what to look for on arrival (Lautrec, Jane Avril dancing,
   described), without a room number; 055's @where hedges level 2 room 68 vs level 5.
8. REPETITION — each story in ONE owner track; elsewhere at most a 3–6-word callback:
   clock passage → 024 (054 a fresh short text: the café behind the second clock, a pause, then down) · Bazille's death → 027 ·
   "wedding portrait" → 057 (cut from 048) · Gauguin at forty / "masses of colour" → 049 (053 only a callback) · scan your tracks for
   other repeats the T review lists.
9. VARIETY of closings: don't end every track with "play its track there". Vary naturally. Never "next track".
10. Traveller-review line-level rewrites for your tracks: apply those that keep facts within the sources. Weakest tracks (054, 022)
    get a tighter, warmer rewrite within the facts; ≤ 280 words.
After editing run the validator + length + authority check:
  python3 -c "import sys,glob,re;sys.path.insert(0,'/home/user/AudioQ/orsay_v5/v5/pipeline');import v5_direction as V
[print(f[-12:-9],len(V.validate(f)[1].split()),len(re.findall(r'the museum (says|calls|notes|tells|describes|writes)',V.validate(f)[1],re.I))) for f in sorted(glob.glob('/home/user/AudioQ/orsay_v5/v5/tracks/*.perf.txt'))]"
Append to /home/user/AudioQ/orsay_v5/v5/notes/REVISION_LOG.md a section for your range: per track one line per change.
Final reply ≤8 lines.

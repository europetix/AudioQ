# Revision brief — Orangerie V5 (5 Oct 2026)
Revise ONLY your assigned tracks in /home/user/AudioQ/orangerie_v5/v5/tracks/. Keep the format, tags and the house style
(/home/user/AudioQ/orangerie_v5/v5/WRITER_BRIEF.md rules still apply: lengths, no ; ( , ≤2 dashes, only allowed tags, facts only
from FACTS_A/B/C + findings G1–G5 graded OFF/SEC2). No web access.
Inputs: verification reports /home/user/AudioQ/orangerie_v5/v5/verify/V1_001-018.md, V2_019-036.md, V3_037-055.md and the traveller
review /home/user/AudioQ/orangerie_v5/v5/verify/T_traveller_review.md.

Apply, for your tracks:
1. EVERY CONTRA / NOTFOUND / WEAK / rule fix in the V reports (use their replacement sentence or cut; never add new unsourced detail).
2. AUTHORITY: "the museum says / calls / notes / tells us / describes" — at most ONE per track, and only where attribution matters
   (an interpretation or a quote). Elsewhere state the sourced fact plainly.
3. NO spoken doubt about our own research ("I can't give you…", "I don't have a reliable description…", "nobody has told me…").
   If a detail isn't sourced, simply don't mention it; keep looking prompts general and confident.
4. LOANS/ABSENCES: none in speech, except ONE short line in 040 (L'Étreinte, light-sensitive loan) if needed. Put caveats in @where.
5. REPETITION — each story is told in ONE owner track only; elsewhere at most a 3–6-word callback:
   Monet's letter / deed / death / never saw them installed → 002 and 013 (not 004, 055) · lost sky / 1960s floor / renovation → 014
   (054 only a callback) · Max Jacob & Montmartre studio → 015 (not 017) · close-up-then-step-back exercise → 004 only (vary 006, 007)
   · "tempting to read…" → 012 only · "modern primitives" passage → 015 (rewrite 033) · Père Junier callbacks → at most one later
   mention · Guillaume never Picasso's official dealer → 040 · Domenica selling Picassos → 044 · model Salvado → 050 · Pierrot =
   Paul Guillaume → 050 (not 018) · 055 must not retell 001/002 (a fresh, short goodbye: the garden, the light, the gift).
6. VARIETY of closings: don't end every track with "play its track there". Vary naturally ("…and start its track there", "the story
   continues in front of it", "listen to it there", sometimes just the place). Never "next track".
7. Traveller-review line-level rewrites for your tracks: apply those that keep facts within the sources.
8. 052 and 053 (if yours): tighten into stronger storytelling, ≤ 280 / ≤ 240 words, end the lower level with a real payoff.
After editing run the validator + length check and the house checks:
  python3 -c "import sys,glob,re;sys.path.insert(0,'/home/user/AudioQ/orangerie_v5/v5/pipeline');import v5_direction as V
[print(f[-12:-9],len(V.validate(f)[1].split()),len(re.findall(r'the museum (says|calls|notes|tells|describes)',V.validate(f)[1],re.I))) for f in sorted(glob.glob('/home/user/AudioQ/orangerie_v5/v5/tracks/*.perf.txt'))]"
Append to /home/user/AudioQ/orangerie_v5/v5/notes/REVISION_LOG.md a section for your range: per track one line per change.
Final reply ≤8 lines.

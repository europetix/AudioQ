# WRITER BRIEF — Orangerie V5 (5 Oct 2026)

You are writing part of a NEW walking audio guide to the Musée de l'Orangerie, Paris (Water Lilies + Walter-Guillaume collection):
55 tracks, about two hours. The client wants it to match or beat the museum's official audio guide on ACCURACY and to beat it on
STORYTELLING. The old V4 guide was full of errors; it is NOT a source. The voice will be a free TTS voice (Microsoft "Ava"), so
everything that makes it sound human comes from your writing and direction. DO NOT edit files outside your assigned tracks/notes.

Read, in this order:
1. /home/user/AudioQ/orangerie_v5/v5/V5_AUDIO_STANDARD.md — writing + direction standard (binding; ignore Pitti-specific examples).
2. Voice anchors (match their register exactly — spoken, warm, composed; hook → story → turn → look → payoff; short varied
   sentences; honest hedges; at most one wry aside; never a lecture):
   /home/user/AudioQ/tour43_pitti_v5/v5/tracks/015.perf.txt, 021.perf.txt, 022.perf.txt, 053.perf.txt
3. /home/user/AudioQ/orangerie_v5/v5/PLAN.md — running order, content per track, closing cue for each track.
4. FACTS: /home/user/AudioQ/orangerie_v5/research/FACTS_A_renoir_cezanne_modigliani.md, FACTS_B_matisse_picasso_rousseau_laurencin.md,
   FACTS_C_derain_soutine_utrillo_waterlilies.md and the audit /home/user/AudioQ/orangerie_v5/findings/G1–G5 (they list V4's
   errors — never repeat them — and confirmed facts).

## Accuracy rules (non-negotiable)
- Every factual statement must come from a fact-sheet or findings line graded OFF or SEC2. WEAK, NONE, "contested" or
  "do not use" items are forbidden. No web research is available (search quota exhausted) — do not invent, do not "remember".
- Visual description ("look at…") only as the fact sheet describes the work. If the sheet has no description, keep looking-
  instructions general and safe (colours/subject named in the title or official description only).
- Legends / anecdotes only if sourced, and framed honestly ("the story goes", "he later said").
- Placement: lower-level room order is unverified → name the artist's room ("in the room of Cézanne's paintings"), never left/right
  downstairs. Water Lilies: use the walls PLAN gives as OFF; otherwise describe the composition so visitors recognise it.
- Works that may be away (PLAN header): one plain hedge in @where and at most one short spoken line ("if it's away on loan…").
- No opening hours, prices, tickets, temporary exhibitions, shop/café in speech. No "next track", no production jargon.
  Closing cue = the physical next stop from PLAN, then "play its track there" (or a natural variant).
- Quotes: only those a fact sheet gives verbatim with a grade; attribute exactly as the sheet says (e.g. Roger Marx 1909).

## Writing rules
- Never open with a command. Open with a hook: a surprising fact, a person, a tension.
- Length: R 180–280 words · W 250–360 · ANCHOR/CLOSE 250–360.
- Average sentence 11–16 words, vary, max ~30. No parentheses, no semicolons, ≤2 em-dashes per track.
- Tags: only [pause] [long pause] [warmly] [quietly] [amused] [curious] [conspiratorial] [reverent] [wry] [lightly] and *word*.
  About one delivery tag per paragraph; a pause before a reveal. Vary openers: do NOT start most tracks with [curious].
- Numbers as spoken ("in nineteen fifteen" or "1915" both fine); max ~3 dates per track. Use French titles once with the English.
- Variety across the guide: different hooks, not every track ending on an aphorism, no repeated jokes or formulas.

## Output — one file per track: /home/user/AudioQ/orangerie_v5/v5/tracks/<NNN>.perf.txt
@id: <NNN> · <room label>
@section: <exactly: Opening | Water Lilies | Collectors | Renoir | Cézanne | Rousseau | Matisse | Picasso | Modigliani | Soutine | Derain | Finale | Closing>
@room: <display label from PLAN, e.g. Room 1 · Renoir room · Lower level>
@type: ANCHOR | R | W | CLOSE
@title: <e.g. Renoir — Jeunes filles au piano>
@where: <1–2 sentences for a card: where to stand, how to recognise the work>
@what: <1–2 sentences: artist, title (FR + EN), date, medium, size if sourced>
@listen: <1 sentence>
@brief: <one line: who speaks, to whom, mood>
@pace: slow | medium-slow | medium | medium-fast
@energy: e.g. 2→4
@sources: <fact-sheet refs and the URLs they cite for the load-bearing facts, e.g. "FACTS_A Renoir — Jeunes filles au piano: https://www.musee-orangerie.fr/... (OFF)">
---
<spoken body with tags, paragraphs separated by blank lines>

Also write /home/user/AudioQ/orangerie_v5/v5/notes/<range>_NOTES.md: per track, the facts used (one line each with sheet + grade) and
anything you wanted to say but could not source.
Self-check before finishing (fix every error / out-of-range length):
  python3 -c "import sys,glob;sys.path.insert(0,'/home/user/AudioQ/orangerie_v5/v5/pipeline');import v5_direction as V;[print(f[-12:],len(V.validate(f)[1].split())) for f in sorted(glob.glob('/home/user/AudioQ/orangerie_v5/v5/tracks/*.perf.txt'))]"
Final reply ≤8 lines: tracks written, word counts, anything you could not source.

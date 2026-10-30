# WRITER BRIEF — Catedral de Sevilla and the Giralda, Yo Tours (30 Oct 2026)

You are writing part of a new English walking audio guide to Seville Cathedral and the Giralda, built from scratch to the
series standard. The official guide (sold separately, €4–5) is criticised because its numbers don't match the cathedral's
and are hard to find; ticket+audio bundles are poorly rated. Popular stories are often wrong (the "think us mad" quote is
tradition; "third-largest church" is unsourced; the Puerta del Lagarto "crocodile" is later tradition). Ours must be clearly
better: right places, spoken directions by landmarks, verified, honest about legends and closures, good to listen to.
Navigation accuracy is the first priority; good storytelling is the second.

Project root: /home/claude/audioq/cathedral_seville_v5   (all paths below are relative to it)

## Read first, in this order
1. v5/V5_AUDIO_STANDARD.md — writing + direction standard (binding; §2 and §3).
2. Voice anchors (spoken, warm, composed; hook → story → turn → look → payoff):
   /home/claude/audioq/uffizi_v5/v5/tracks/017.perf.txt, 058.perf.txt and /home/claude/audioq/thyssen_v5/v5/tracks/029.perf.txt
3. v5/PLAN.md — binding for space, order, cue destination, facts in bold, what NOT to say, DATED items, NEVER list, ALT cues,
   walking-track rules for the Giralda (002, 003, 006 are heard while climbing/descending), and the bridge table (section 3).
   Read its Conventions: Spanish names first with an English gloss once per track; NO numbers; directions only as PLAN allows.
4. research/VISIT_ROUTE_AND_SPACES_OCT2026.md (entrances, Giralda first, exit, statuses, Capilla Real worship-only, works and
   closures) and research/FACTS_OCT2026.md (verified facts, safe wording, legends, popular errors).

## Accuracy rules (non-negotiable)
- Every load-bearing fact (date, artist, story, attribution, size) must be confirmed on the source PLAN gives (catedraldesevilla.es
  pages and PDFs first) via WebFetch, or on the fact file's cited source. One page at a time, never in bursts; never a browser,
  never curl; never complete any CAPTCHA. Wikipedia never alone.
- Use the fact file's safe wording. Legends as legends ("tradition says…"); superlatives attributed ("UNESCO calls it…").
- Columbus: say exactly what is established (FACTS), no more. Respectful tone: this is a working church with tombs.
- Only describe as present what is confirmed. Restorations, works and anything dated: one separate, cuttable sentence.
- Quotations only if sourced, short, attributed. No prices, opening hours, tickets, ticket types, queues or selling.

## Navigation rules
- @room and @title exactly as PLAN. @where: where to stand and how to recognise the place (size, colour, feature).
- The LAST paragraph of every track (except CLOSE) is the cue, as in PLAN: the destination's Spanish name plus one landmark to
  look for, 1–3 sentences. Extras are announced by the track before ("There's a short Extra here on…; the next main stop is…").
- Track 001 explains the three lengths in two or three plain sentences: the full tour about an hour and three-quarters, the
  essential version about an hour and a quarter, the highlights about forty-five minutes, all with the Giralda; whichever is on
  your phone, play it in order — the numbers may jump, and every stop says where to go next.
- Never "next track", "right this way", "just over there". Left/right only where PLAN marks it as confirmed.

## Bridges (shorter versions)
For every row of PLAN section 3 "Bridges" whose Track is one of yours, write ONE spoken bridge sentence (15–40 words) that
starts "On this shorter tour," and gives the route to the next stop of that version (Spanish name and one landmark). It is played after the track's normal cue, so it must make sense after it ("On this shorter tour, walk on past the Capilla de San
Antonio to the Capilla de la Antigua, …"). Put them in
v5/bridges/<first>-<last>.txt, one per line: `NNN E>MMM: text` or `NNN H>MMM: text`.

## Writing rules
- Never open with a command. Open with a hook: a surprising fact, a person, a tension.
- Length (spoken words, tags excluded): R 180–280 · W 250–360 · ANCHOR/CLOSE 250–360 · X 150–230. Aim ~290 for W, ~230 for
  R, ~190 for X (the whole guide must stay near 7,800 words: do not run long).
- Average sentence 11–16 words; vary; max ~30. No parentheses, no semicolons, ≤2 em-dashes, no exclamation marks.
- Direction tags only from the standard: [pause] [long pause] [warmly] [quietly] [amused] [curious] [conspiratorial]
  [reverent] [wry] [lightly], *word* for stress. About one delivery tag per paragraph.
- Years as digits, max ~3 dates per track. Spanish names of spaces as on the signs; English gloss once per track.

## Output — one file per track: v5/tracks/NNN.perf.txt
```
@id: NNN · <space> · 30 Oct 2026 edition
@section: <exactly the PLAN section>
@room: exactly as PLAN ("Sacristía Mayor")
@type: ANCHOR | R | W | X | CLOSE
@title: exactly as in PLAN (Extras keep "Extra · ")
@where: <1–2 sentences: where to stand and how to recognise it; no internal notes or check codes>
@what: <artist, official title, date, medium, size if useful, plus other works covered>
@listen: <1 sentence: what the track is about>
@brief: <one line: who is speaking, to whom, in what mood>
@pace: slow | medium-slow | medium | medium-fast
@energy: e.g. 2→4
@sources: <URLs read, with what each confirmed; OFF = read on an official page>
---
<spoken body, paragraphs separated by blank lines, last paragraph = cue>
```
Write v5/notes/<first>-<last>_NOTES.md: per track, the pages read and anything you could not confirm.
Check before finishing:  python3 v5/lint.py <your track numbers>   — every track must print OK.
Final reply ≤ 8 lines: tracks written, what you could not verify, what the lead must decide.

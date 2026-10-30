# WRITER BRIEF — Setas de Sevilla (Metropol Parasol) and the Antiquarium, Yo Tours (30 Oct 2026)

You are writing part of a new English walking audio guide to the Setas de Sevilla and the Antiquarium beneath it, built from
scratch to the series standard. The official free QR web guide is barely documented (not even on the official site), city
audio apps give the Setas about two minutes, and nobody offers audio in the Antiquarium. Popular claims are often wrong
("largest wooden structure in the world" is the operator's claim only; the 1840s market was approved in 1832; the fig-tree
inspiration is the city's reading, Mayer himself speaks of "big trees on a neighboring plaza"). Ours must be clearly better:
right places, spoken directions by fixed features, ONLY views that are sourced, verified facts, honest about the controversy
and the cost, good to listen to. Navigation accuracy is the first priority; good storytelling is the second.

Project root: /home/claude/audioq/setas_v5   (all paths below are relative to it)

## Read first, in this order
1. v5/V5_AUDIO_STANDARD.md — writing + direction standard (binding; §2 and §3).
2. Voice anchors (spoken, warm, composed; hook → story → turn → look → payoff):
   /home/claude/audioq/cathedral_seville_v5/v5/tracks/004.perf.txt, 014.perf.txt and /home/claude/audioq/alcazar_v5/v5/tracks/007.perf.txt
3. v5/PLAN.md — binding for place, order, cue destination, facts in bold, what NOT to say, DATED items, NEVER list, ALT cues and
   the bridge table. Read its Conventions: places by level + name; directions by fixed features; views only as sourced.
4. research/VISIT_ROUTE_AND_SPACES_OCT2026.md (entrances, level −1, lifts, Mirador by steps, Feeling Sevilla, exhibition,
   Plaza Mayor, Antiquarium contents) and research/FACTS_OCT2026.md (verified facts, safe wording, wrong claims). For the
   Cathedral and Giralda as seen from the walkway, PLAN allows rows of /home/claude/audioq/cathedral_seville_v5/research/FACTS_OCT2026.md.

## Accuracy rules (non-negotiable)
- Every load-bearing fact must be confirmed on the source PLAN gives (setasdesevilla.com, the city's pages, J. Mayer H., Arup,
  Metsä, academic papers) via WebFetch, or on the fact file's cited source. One page at a time, never in bursts; never a
  browser, never curl; never complete any CAPTCHA. Wikipedia never alone.
- Use the fact file's safe wording; attribute claims (the operator calls it…; the city told the Ombudsman…); legends as legends.
- NEVER describe a view the sources do not support. Only: Cathedral and Giralda to the south; the river and the Aljarafe to the
  west. Everything else is an ONSITE item, not speech.
- Restorations, seasons (Aurora April–October) and anything dated: one separate, cuttable sentence.
- Quotations only if sourced, short, attributed. No prices, opening hours, tickets, the shop, the bar, or selling.

## Navigation rules
- @room and @title exactly as PLAN. @where: where to stand and how to recognise the place.
- The LAST paragraph of every track (except CLOSE) is the cue, as in PLAN: the destination (level + place) plus one thing to
  look for, 1–3 sentences. Extras are announced by the track before.
- Track 001 explains the three lengths in two or three plain sentences: the full tour, with the Antiquarium, just under an
  hour; the essential version about thirty-five minutes; the highlights about twenty-five minutes, all with the lifts and
  walking; whichever is on your phone, play it in order — the numbers may jump, and every stop says where to go next. It also
  says the Antiquarium has its own entrance and ticket, and only the full tour goes there.
- Never "next track", "right this way", "just over there". Left/right only where PLAN marks it as confirmed.

## Bridges (shorter versions)
For every row of PLAN section 3 "Bridges" whose Track is one of yours, write ONE spoken bridge sentence (15–40 words) that
starts "On this shorter tour," and gives the route to the next stop of that version (Spanish name and one landmark). It is played after the track's normal cue, so it must make sense after it ("On this shorter tour, skip the Antiquarium: go
straight to the lifts beside the ticket office, …"). Put them in
v5/bridges/<first>-<last>.txt, one per line: `NNN E>MMM: text` or `NNN H>MMM: text`.

## Writing rules
- Never open with a command. Open with a hook: a surprising fact, a person, a tension.
- Length (spoken words, tags excluded): R 180–280 · W 250–360 · ANCHOR/CLOSE 250–360 · X 150–230. Aim ~290 for W, ~230 for
  R, ~190 for X (the whole guide must stay near 4,800 words: do not run long).
- Average sentence 11–16 words; vary; max ~30. No parentheses, no semicolons, ≤2 em-dashes, no exclamation marks.
- Direction tags only from the standard: [pause] [long pause] [warmly] [quietly] [amused] [curious] [conspiratorial]
  [reverent] [wry] [lightly], *word* for stress. About one delivery tag per paragraph.
- Years as digits, max ~3 dates per track. Spanish names as on the signs; English gloss once per track.

## Output — one file per track: v5/tracks/NNN.perf.txt
```
@id: NNN · <space> · 30 Oct 2026 edition
@section: <exactly the PLAN section>
@room: exactly as PLAN ("Level −1 · Antiquarium entrance")
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

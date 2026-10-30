# WRITER BRIEF — Real Alcázar de Sevilla, Yo Tours (30 Oct 2026)

You are writing part of a new English walking audio guide to the Real Alcázar de Sevilla. It replaces an old 20-track guide
that claimed every fact was verified but got about 48 wrong (the "Almohad" Lion Gate, María de Padilla in rooms finished after
her death, Almohad "cisterns" that the Alcázar itself calls Gothic vaults, swapped Game of Thrones scenes…), sent people
upstairs to the Gothic palace, put the Cuarto Real Alto in the gardens, and gave prices and ticket advice. The official free web
guide is "complicated and limited" and its numbers don't match the printed map; the paid app has poor reviews. Ours must be
clearly better: right places, spoken directions using the Alcázar's own map numbers, verified, honest, good to listen to.
Navigation accuracy is the first priority; good storytelling is the second.

Project root: /home/claude/audioq/alcazar_v5   (all paths below are relative to it)

## Read first, in this order
1. v5/V5_AUDIO_STANDARD.md — writing + direction standard (binding; §2 and §3).
2. Voice anchors (spoken, warm, composed; hook → story → turn → look → payoff):
   /home/claude/audioq/uffizi_v5/v5/tracks/017.perf.txt, 058.perf.txt and /home/claude/audioq/thyssen_v5/v5/tracks/029.perf.txt
3. v5/PLAN.md — binding for number, order, cue destination, facts in bold, what NOT to say, DATED items, NEVER list, ALT cues,
   and the bridge table (section 3). You may polish wording, never change where a cue sends people. READ its Conventions:
   how numbers are spoken, never "number 11", and NO left/right/straight-ahead until the map confirms (provisional geometry).
4. research/VISIT_ROUTE_AND_SPACES_OCT2026.md (the official leaflet numbering 1–53, statuses, object locations),
   research/AUDIT_OLD_GUIDE_FACTS_OCT2026.md (corrected facts, good stories, banned items).
5. Old scripts old/NNN.txt (OLD numbering) for stories only — their places and many facts are WRONG.

## Accuracy rules (non-negotiable)
- Every load-bearing fact (date, builder, story, attribution, size) must be confirmed on the source PLAN gives (alcazarsevilla.org
  pages and PDFs first) via WebFetch, or on the audit's cited source. One page at a time, never in bursts; never a browser,
  never curl; never complete any CAPTCHA. Wikipedia never alone.
- Use the audit's corrected wording. Contested identifications are told as tradition ("tradition sees…"); legends as legends.
- Only describe as present what is confirmed. Restorations and anything dated: one separate, cuttable sentence.
- Quotations only if sourced, short, attributed. No prices, opening hours, tickets, queues, the shop (closed), or selling.
- Be honest about uncomfortable history (the Casa de la Contratación and slavery; the Tunis campaign), briefly and plainly.

## Navigation rules
- @room and @title exactly as PLAN. @where: where to stand and how to recognise the place (size, colour, feature).
- The LAST paragraph of every track (except CLOSE) is the cue, as in PLAN: the destination's number and Spanish name ("number
  15, the Salón de los Embajadores"), plus one recognisable thing to look for. 1–3 sentences. Extras are announced by the track
  before ("Number 13 has a short Extra on…; the next main stop is number 15, the Salón de los Embajadores, …").
- How numbers are spoken: track 001 explains once that the numbers are those on the Alcázar's own map, which is also printed on
  the route map that comes with this guide. First mention of a number in Full order: "number 15 on the Alcázar map, the Salón de
  los Embajadores"; afterwards "number 15, the Salón de los Embajadores". Spanish names always with the number.
- Track 001 explains the three lengths in two or three plain sentences: the full tour about two hours, the essential version
  about an hour and a quarter, the highlights about forty-five minutes, all with walking; whichever is on your phone, play it in
  order — the numbers may jump, and every stop says where to go next. It also says the Cuarto Real Alto, the upper royal rooms,
  is a separate timed visit with two short optional tracks at the end of this guide.
- Never "next track", "right this way", "just over there". No left/right until the map confirms (PLAN).

## Bridges (shorter versions)
For every row of PLAN section 3 "Bridges" whose Track is one of yours, write ONE spoken bridge sentence (15–40 words) that
starts "On this shorter tour," and gives the route to the next stop of that version (number and Spanish name, one thing
to look for). It is played after the track's normal cue, so it must make sense after it ("On this shorter tour, skip number 4's
long look: go on to number 6, the Cuarto del Almirante, …"). Put them in
v5/bridges/<first>-<last>.txt, one per line: `NNN E>MMM: text` or `NNN H>MMM: text`.

## Writing rules
- Never open with a command. Open with a hook: a surprising fact, a person, a tension.
- Length (spoken words, tags excluded): R 180–280 · W 250–360 · ANCHOR/CLOSE 250–360 · X 150–230. Aim ~290 for W, ~230 for
  R, ~190 for X (the whole guide must stay near 8,700 words: do not run long).
- Average sentence 11–16 words; vary; max ~30. No parentheses, no semicolons, ≤2 em-dashes, no exclamation marks.
- Direction tags only from the standard: [pause] [long pause] [warmly] [quietly] [amused] [curious] [conspiratorial]
  [reverent] [wry] [lightly], *word* for stress. About one delivery tag per paragraph.
- Years as digits, max ~3 dates per track. Spanish names of spaces as on the leaflet; English gloss once where it helps.

## Output — one file per track: v5/tracks/NNN.perf.txt
```
@id: NNN · No. XX · 30 Oct 2026 edition
@section: <exactly the PLAN section>
@room: exactly as PLAN ("No. 15 · Salón de los Embajadores")
@type: ANCHOR | R | W | X | CLOSE
@title: exactly as in PLAN (Extras keep "Extra · "; CRA Extras "CRA 20 · Extra · …")
@where: <1–2 sentences: where to stand and how to recognise it>
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

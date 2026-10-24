# WRITER BRIEF — Uffizi Gallery, Florence, Yo Tours (24 Oct 2026)

You are writing part of a new English walking audio guide to the Uffizi Gallery. It replaces a guide that sent visitors into
rooms that are now closed, described the Botticellis as they hung before the June 2026 rehang, and got about 22 facts wrong
(audit). The museum's own handset guide and the free competitors are thin, dated or stop at the top floor; ours must be
clearly better: right rooms, spoken directions, honest about closures and loans, verified, and good to listen to.
Navigation accuracy is the first priority; good storytelling is the second.

Project root: /home/claude/audioq/uffizi_v5   (all paths below are relative to it)

## Read first, in this order
1. v5/V5_AUDIO_STANDARD.md — writing + direction standard (binding; §2 and §3).
2. Voice anchors (match their register: spoken, warm, composed; hook → story → turn → look → payoff):
   /home/claude/audioq/thyssen_v5/v5/tracks/029.perf.txt, 050.perf.txt and /home/claude/audioq/tour43_pitti_v5/v5/tracks/017.perf.txt
3. v5/PLAN.md — binding for room, order, cue destination, facts flagged in bold, DATED items, NEVER list, ALT cues, and the
   bridge table (section 3). You may polish wording, never change where a cue sends people.
4. The official October 2026 map: source/map.txt and research/map/p-3.png (second floor), p-2.png (first floor), p-1.png
   (overview); research/map/hi-3.png is a high-resolution second floor. Read the images: describe the walk truthfully.
5. research/FLOOR2_LOCATIONS_OCT2026.md, FLOOR1_LOCATIONS_OCT2026.md, NOTICES_OCT2026.md, AUDIT_OLD_GUIDE_FACTS_OCT2026.md.
6. Old scripts old/NNN.txt (OLD numbering; PLAN says which) for stories only — their rooms and many facts are WRONG.

## Accuracy rules (non-negotiable)
- Every load-bearing fact (date, size, medium, commission, story, attribution) must be confirmed on the work's official
  uffizi.it page (URLs in PLAN) via WebFetch, or on the audit's cited source. Read each of your works' official pages: they
  carry the curators' text and are your best material. Use WebFetch only, one page at a time, never in bursts; never a browser,
  never curl; never complete any CAPTCHA. Wikipedia never alone.
- The artwork pages' "Location" can be stale: from D19 on, page codes are one lower than the map (page "D22" = map D23), and
  the 17th-century pages use old D29–D34 codes. The MAP wins for room codes; PLAN already gives the right code.
- Use the audit's corrected wording (Family Pact 1737: nothing to leave "the capital and State of the Grand Duchy"; opened to
  the public 24 June 1769; Bernini's Saint Lawrence about a metre long; self-portraits in the Corridor 1973–2016; etc.).
- Only describe as present what is confirmed in that room. Never send people to a work that is not on display. Loans: one
  separate, cuttable sentence ("Until early February 2027, three of his paintings are on loan to Rome").
- Vasari anecdotes are "Vasari tells…", never fact. Quotations only if sourced, short, attributed.
- No ticket prices, opening hours, booking or queue advice, director names, shop/café selling. (037 may say plainly that the
  terrace café is on this floor, before the stairs, because after the way out you cannot come back — practical, not selling.)

## Navigation rules (this is what customers complained about)
- @room exactly as PLAN ("Room A4"). @where: where to stand and how to recognise the work (size, colour, subject).
- The LAST paragraph of every track (except CLOSE) is the cue, as in PLAN: the destination room code written as in the map
  ("Room A8", "Room D23"), its title from the map when it helps, plus one recognisable thing to look for. 1–3 sentences.
  Extras are announced by the track before ("Room A6 has a short Extra on …; the next main stop is Room A7 …").
- The Botticelli rooms: NEVER say A9, A10, A11 or A12 in speech. Use PLAN's position wording and "follow the museum's signs
  for Botticelli" where the entry is uncertain (ONSITE O7).
- Floor changes: say which floor and how (staircase name as on the map, lift where shown). The Lanzi staircase at the end of
  the second floor goes DOWN ONE FLOOR to the first floor: say clearly "down one floor only — not out to the street".
- Never "next track", "right this way", "just over there", "the next room along" without its code.
- Track 001 explains the three lengths in two or three plain sentences: the full tour about two and three-quarter hours, the
  essential version about two hours, the highlights about an hour and a quarter; whichever is on your phone, play it in
  order — the numbers may jump, and every stop says where to go next.

## Bridges (shorter versions)
For every row of PLAN section 3 "Bridges" whose Track is one of yours, write ONE spoken bridge sentence (15–40 words) that
starts "On this shorter tour," and gives the route to the next stop of that version (room code, staircase if any, one thing
to look for). It is played after the track's normal cue, so it must make sense after it ("On this shorter tour, skip Room A5:
go back through Room A4 to Room A7, with Gentile's golden procession."). Botticelli rule applies. Put them in
v5/bridges/<first>-<last>.txt, one per line: `NNN E>MMM: text` or `NNN H>MMM: text`.

## Writing rules
- Never open with a command. Open with a hook: a surprising fact, a person, a tension.
- Length (spoken words, tags excluded): R 180–280 · W 250–360 · ANCHOR/CLOSE 250–360 · X 150–230. Aim ~290 for W, ~230 for
  R, ~190 for X (the whole guide must stay near 17,000 words: do not run long).
- Average sentence 11–16 words; vary; max ~30. No parentheses, no semicolons, ≤2 em-dashes, no exclamation marks.
- Direction tags only from the standard: [pause] [long pause] [warmly] [quietly] [amused] [curious] [conspiratorial]
  [reverent] [wry] [lightly], *word* for stress. About one delivery tag per paragraph.
- Years as digits, max ~3 dates per track. Italian names and titles as the museum gives them in English pages, with the
  Italian where the museum uses it (Primavera, Maestà).

## Output — one file per track: v5/tracks/NNN.perf.txt
```
@id: NNN · Room XX · 24 Oct 2026 edition
@section: <exactly the PLAN section>
@room: Room XX
@type: ANCHOR | R | W | X | CLOSE
@title: exactly as in PLAN (Extras keep "Extra · ")
@where: <1–2 sentences: where to stand and how to recognise it>
@what: <artist, official title, date, medium, size if useful, plus other works covered>
@listen: <1 sentence: what the track is about>
@brief: <one line: who is speaking, to whom, in what mood>
@pace: slow | medium-slow | medium | medium-fast
@energy: e.g. 2→4
@sources: <official URLs read, with what each confirmed; OFF = read on the official page>
---
<spoken body, paragraphs separated by blank lines, last paragraph = cue>
```
Write v5/notes/<first>-<last>_NOTES.md: per track, the pages read and anything you could not confirm.
Check before finishing:  python3 v5/lint.py <your track numbers>   — every track must print OK.
Final reply ≤ 8 lines: tracks written, what you could not verify, what the lead must decide.

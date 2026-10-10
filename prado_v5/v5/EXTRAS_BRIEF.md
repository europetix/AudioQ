# WRITER BRIEF — Prado EXTRA tracks (10 Oct 2026)

The 59-track English guide is written and audited (v5/tracks/). The client asked for 22 short OPTIONAL "Extra" tracks so
travellers aren't left with silent rooms. Extras are 60–90 seconds (150–230 spoken words), in rooms the route already
walks through. Final numbering 001–081 is applied later by script — never mention track numbers in speech.

Project root: /home/claude/audioq/prado_v5. Read first:
1. v5/WRITER_BRIEF.md (the main brief: accuracy, navigation and writing rules all apply, except length).
2. v5/PLAN_EXTRAS.md — your Extras: room, works (official room + URL + facts already read on the page), "play after",
   "cue to next", notes. v5/ORDER_081.txt — the final playing order.
3. The core tracks around each Extra (v5/tracks/NNN.perf.txt), so you don't repeat them and the walk joins up.
4. research/map/floor0.png, floor1.png, floor2.png for the walk.

## Extra track format — write v5/extras/xNN.perf.txt
@id: xNN · Room 56 · Extra · 10 Oct 2026 edition
@section: <exactly the @section of the core track it is played after>
@room: Room 56
@type: X
@title: Room 56 · Extra · Anthonis Mor — Mary Tudor, Queen of England
@where / @what / @listen / @brief / @pace / @energy / @sources  (as in the core tracks)
---
body: 2–4 short paragraphs. Open with a hook (never a command). One story, one thing to look at. The LAST paragraph is
the cue to the next stop exactly as PLAN_EXTRAS "cue to next" (room number + what to look for). Facts: only what the
official page supports (re-read it with WebFetch, one fetch at a time; never browser tools or curl).
Keep the same voice as the core tracks. Lint type X = 150–230 words.

## Edit the core track played just BEFORE each of your Extras (only its LAST paragraph)
Keep the existing cue (it still guides people who skip Extras) and add one short sentence that announces the Extra, e.g.
- Extra on the way:  "On the way, in Room 56, there's a short Extra on Mary Tudor: play it there if you have time."
- Two Extras on the way: "On the way, Rooms 56 and 55 each have a short Extra: play them there if you have time."
- Extra in the same room: "Before you go, there's a short Extra on Baldung Grien's Ages of Woman and Death in this room."
- Detour (core 050 → x18 in Room 93): "If you have time, a short Extra waits in Room 93, along the row of rooms past 91 and 92.
  Otherwise, go back to Room 85 next door…"
Do not otherwise change the core track. If a core track already mentions the Extra's work in passing (e.g. 019 mentions
Titian's self-portrait in Room 41; 050 mentions the Pottery Vendor; 037 may mention Reni), shorten that mention so the two
don't repeat — keep the core track's facts correct.
Log every change in v5/notes/EXTRAS_<first>-<last>_CHANGES.md.

Check: python3 v5/lint.py <your xNN ids> <core ids you edited>   — all OK. Final reply ≤ 8 lines.

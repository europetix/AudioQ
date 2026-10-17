# WRITER BRIEF — Museo Reina Sofía, Yo Tours (17 Oct 2026)

You are writing part of a new English walking audio guide to the Museo Reina Sofía, Madrid. It replaces a guide that
sent visitors to works that are no longer on display (most of its stops) and to wrong rooms (even Guernica).
This rebuild fixes that once and for all. Navigation accuracy is the first priority; good storytelling is the second.

Project root: /home/claude/audioq/reina_v5   (all paths below are relative to it)

## Read first, in this order
1. v5/V5_AUDIO_STANDARD.md — writing + direction standard (binding; §2 and §3).
2. Voice anchors (match their register: spoken, warm, composed; hook → story → turn → look → payoff):
   /home/claude/audioq/tour43_pitti_v5/v5/tracks/017.perf.txt and 016.perf.txt and
   /home/claude/audioq/orsay_v5/v5/tracks/013.perf.txt
3. v5/PLAN.md — your tracks: room, official source URLs, the exact "cue to next", and notes. PLAN is binding for
   room, order and cue (you may polish the cue wording, not change where it sends people).
4. Official maps: research/map/floor4_official_map.png (Floor 4, Rooms 1–21, exact), research/map/plano_full.png and
   f1/f2/f3/f4.png (the museum's Oct 2026 – Feb 2027 plan; Floor 2 has no room numbers on it). Floor 2 rooms follow the
   museum's own order 201.01 → 206.03; describe the walk by room number and room title, never by left/right unless a
   map shows it. research/FLOOR2_LAYOUT.md may appear later with more detail — use it if present.
5. research/CURRENT_COLLECTION_OCT2026.md (what is on view, room by room, with official URLs) and
   research/AUDIT_OLD_GUIDE_17OCT2026.md (what was wrong).
6. Old scripts (old/NNN.txt, old numbering; contents list in source/old.txt) may help for stories, but their ROOMS,
   CUES AND MANY FACTS ARE WRONG. Check everything (below).

## Accuracy rules (non-negotiable)
- Every load-bearing fact (date, commission, story, attribution, size) must be confirmed on the work's official
  museoreinasofia.es page or the room page (URLs in PLAN) via WebFetch. Room pages carry the curators' text: use it.
  For a work PLAN names without a URL, find its page (WebSearch `site:museoreinasofia.es <artist> <title>`) and check it
  says "Exhibited in Room …" with the right room. If a room page lists only some works, describe only works you confirmed. Read each of
  your works' official pages — they also give you the best material. Use WebFetch only; never Chrome/browser
  tools, never curl (the museum firewall blocks bursts — fetch one page at a time).
- If a fact from the old script can't be confirmed, drop it or frame it honestly ("the story goes…").
- Use the museum's official title in @what (Spanish/original title plus English, as on the English page).
- Only describe as present what you confirmed in that room. Never send people to a work that isn't on display.
- Contemporary rooms (Floor 4) deal with AIDS, sexuality, drugs, dictatorship and violence: be factual, respectful and
  plain, follow the museum's own framing, no sensationalism, no explicit description beyond what the room text says.
- Quotations from artists or critics: only if on an official page, short, attributed.
- No ticket prices, opening hours, booking, or temporary exhibitions in the speech.

## Navigation rules (this is what the customers complained about)
- @room is exactly "Room 205.10" / "Room 7" style (the museum's room number). @where says where to stand in that room
  and how to recognise the work (size, colours, subject) — a card a visitor can use.
- The LAST paragraph of every track (except CLOSE) is the cue, as in PLAN's "cue to next": next room number AND its
  title (the museum's room titles, e.g. "Room 205.05, 'Speaking Walls'"), plus one recognisable thing to look for.
  1–3 short sentences. Extras: the track before announces them ("Room 6 has a short Extra on …; the next main stop is
  Room 7"), as PLAN's cues already do.
- If the next stop is in the same room, say so ("Stay in Room 58…").
- Floor changes: say which floor and how (stairs or lift), and give the signs to follow, exactly as PLAN says.
- Never "next track", never "right this way", never "just over there", never "the next room along" without its number.
- Write room numbers as digits everywhere, e.g. "Room 205.10" (the English voice gets a pronunciation for them).

## Writing rules
- Never open with a command. Open with a hook: a surprising fact, a person, a tension.
- Length (spoken words, tags excluded): R 180–280 · W 250–360 · ANCHOR/CLOSE 250–360 · Extra (X) 150–230. Aim for the
  middle-low end on Floor 4 (many short rooms).
- Average sentence 11–16 words; vary; max ~30. No parentheses, no semicolons, ≤2 em-dashes, no exclamation marks.
- Direction tags only from the standard: [pause] [long pause] [warmly] [quietly] [amused] [curious]
  [conspiratorial] [reverent] [wry] [lightly], *word* for stress. About one delivery tag per paragraph.
- Numbers as spoken ("around 1656", "almost a century later"). Max ~3 dates per track. Years as digits.
- "The museum says" at most once per track. Merged tracks (PLAN notes) cover each named work briefly but properly.
- First track of a painter/section folds in a short intro (PLAN notes say which) — 2–3 sentences, not a lecture.

## Output — one file per track: v5/tracks/NNN.perf.txt
```
@id: NNN · Room XX · 17 Oct 2026 edition
@section: <exactly the PLAN section>
@room: Room XX
@type: ANCHOR | R | W | X | CLOSE
@title: exactly as in PLAN (Extras keep "Extra · ")
@where: <1–2 sentences: where to stand and how to recognise it>
@what: <artist, official title, date, technique, plus other works covered>
@listen: <1 sentence: what the track is about>
@brief: <one line: who is speaking, to whom, in what mood>
@pace: slow | medium-slow | medium | medium-fast
@energy: e.g. 2→4
@sources: <official museoreinasofia.es URLs read, with what they confirmed; OFF = read on the official page>
---
<spoken body, paragraphs separated by blank lines, last paragraph = cue>
```
Old scripts (reference only, often wrong): old/NNN.txt by OLD number. Write v5/notes/<first>-<last>_NOTES.md: per track,
the official pages read and anything you could not confirm.

Check before finishing:  python3 v5/lint.py <your track numbers>   — every track must print OK.
Final reply ≤ 8 lines: tracks written, anything you could not verify, anything the lead must decide.

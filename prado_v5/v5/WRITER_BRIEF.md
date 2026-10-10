# WRITER BRIEF — Museo del Prado, Yo Tours V5 (10 Oct 2026)

You are writing part of a new English walking audio guide to the Museo del Prado, Madrid. It replaces a guide
customers complained about: works were sent to the wrong rooms, the order zig-zagged, cues said "right this way".
This rebuild fixes that once and for all. Navigation accuracy is the first priority; good storytelling is the second.

Project root: /home/claude/audioq/prado_v5   (all paths below are relative to it)

## Read first, in this order
1. v5/V5_AUDIO_STANDARD.md — writing + direction standard (binding; §2 and §3).
2. Voice anchors (match their register: spoken, warm, composed; hook → story → turn → look → payoff):
   /home/claude/audioq/tour43_pitti_v5/v5/tracks/017.perf.txt and 016.perf.txt and
   /home/claude/audioq/orsay_v5/v5/tracks/013.perf.txt
3. v5/PLAN.md — your tracks: room, works (official title, date, technique, ROOM, official URL), old source, the
   exact "cue to next", and notes (hedges, merges, corrections). PLAN is binding for room, order and cue.
4. The official floor plan images: research/map/floor0.png, floor1.png, floor2.png (Read them). Use them so your
   cue describes the walk truthfully (which rooms you pass through). Do not invent doors you can't see.
5. research/OFFICIAL_LOCATIONS_PRADO_10OCT2026.md — what was wrong in the old guide and the 2026 notices.
6. Old script for each track: old/NNN.txt (the "old source" in PLAN). Content is often good; its ROOMS AND CUES
   ARE NOT TRUSTED. Its facts must be checked (below).

## Accuracy rules (non-negotiable)
- Every load-bearing fact (date, commission, patron, story, attribution, size) must be confirmed on the work's
  official museodelprado.es page (URL in PLAN) via WebFetch, or on another museodelprado.es page. Read each of
  your works' official pages — they also give you the best material. Use WebFetch only; never Chrome/browser
  tools, never curl (the museum firewall blocks bursts — fetch one page at a time).
- If a fact from the old script can't be confirmed, drop it or frame it honestly ("the story goes…").
- Use the museum's current title in @what (e.g. "The Buffoon El Primo", formerly called Sebastián de Morra;
  "Vulcan's Forge"; "The Feast of Bacchus"). In speech you may use the familiar name too.
- Only describe as present what PLAN lists in that room. Never send people to a work that isn't there
  (Zurbarán's Agnus Dei is on loan; El Greco's Baptism of Christ is not on display).
- Hedges listed in PLAN notes must appear, in one plain sentence (e.g. the Goya rooms 32–38 rehang; the Leoni
  group in Room 1).
- No ticket prices, opening hours, booking, or temporary exhibitions in the speech.

## Navigation rules (this is what the customers complained about)
- @room is exactly "Room 55A" style (the number written at the doorway). @where says where to stand in that room
  and how to recognise the work (size, colours, subject) — a card a visitor can use.
- The LAST paragraph of every track (except CLOSE) is the cue, and it must name the next room number, as in PLAN's
  "cue to next", plus one recognisable thing to look for there. Keep it to 1–3 short sentences. Use "Room 9A"
  wording, and "look for 9A above the doorway" style help when a turn is not obvious.
- If the next stop is in the same room, say so ("Stay in Room 58…").
- Floor changes: say which floor and how (stairs or lift), and give the signs to follow, exactly as PLAN says.
- Never "next track", never "right this way", never "just over there", never "the next room along" without its number.

## Writing rules
- Never open with a command. Open with a hook: a surprising fact, a person, a tension.
- Length (spoken words, tags excluded): R 180–280 · W 250–360 · ANCHOR/CLOSE 250–360. Aim for the middle;
  the whole guide must fit ~2.5 hours on foot.
- Average sentence 11–16 words; vary; max ~30. No parentheses, no semicolons, ≤2 em-dashes, no exclamation marks.
- Direction tags only from the standard: [pause] [long pause] [warmly] [quietly] [amused] [curious]
  [conspiratorial] [reverent] [wry] [lightly], *word* for stress. About one delivery tag per paragraph.
- Numbers as spoken ("around 1656", "almost a century later"). Max ~3 dates per track. Years as digits.
- "The museum says" at most once per track. Merged tracks (PLAN notes) cover each named work briefly but properly.
- First track of a painter/section folds in a short intro (PLAN notes say which) — 2–3 sentences, not a lecture.

## Output — one file per track: v5/tracks/NNN.perf.txt
```
@id: NNN · Room XX · 10 Oct 2026 edition
@section: <exactly the PLAN section>
@room: Room XX
@type: ANCHOR | R | W | CLOSE
@title: Room XX · Artist — Title        (ANCHOR/CLOSE: a short title without room)
@where: <1–2 sentences: where to stand and how to recognise it>
@what: <artist, official title, date, technique, plus other works covered>
@listen: <1 sentence: what the track is about>
@brief: <one line: who is speaking, to whom, in what mood>
@pace: slow | medium-slow | medium | medium-fast
@energy: e.g. 2→4
@sources: <official URLs read, with what they confirmed; OFF = read on the official page>
---
<spoken body, paragraphs separated by blank lines, last paragraph = cue>
```
Also write v5/notes/<first>-<last>_CHANGES.md: per track, one line per material change vs the old script
(fact fixed + source, room/cue fixed, content cut/added, hedge added).

Check before finishing:  python3 v5/lint.py <your track numbers>   — every track must print OK.
Final reply ≤ 8 lines: tracks written, anything you could not verify, anything the lead must decide.

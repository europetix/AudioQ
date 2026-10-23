# WRITER BRIEF — Museo Nacional Thyssen-Bornemisza, Yo Tours (23 Oct 2026)

You are writing part of a new English walking audio guide to the Museo Nacional Thyssen-Bornemisza, Madrid. It replaces a
guide that sent visitors to the wrong room for 26 of its 47 works (12 moved, the rest on loan or not exhibited) and got
about 20 facts wrong. The museum sells its own audio guide; ours must be clearly better: right rooms, spoken directions,
honest about loans, verified, and good to listen to.
This rebuild fixes that once and for all. Navigation accuracy is the first priority; good storytelling is the second.

Project root: /home/claude/audioq/thyssen_v5   (all paths below are relative to it)

## Read first, in this order
1. v5/V5_AUDIO_STANDARD.md — writing + direction standard (binding; §2 and §3).
2. Voice anchors (match their register: spoken, warm, composed; hook → story → turn → look → payoff):
   /home/claude/audioq/tour43_pitti_v5/v5/tracks/017.perf.txt and 016.perf.txt and
   /home/claude/audioq/orsay_v5/v5/tracks/013.perf.txt
3. v5/PLAN.md — your tracks: room, official source URLs, the exact "cue to next", and notes. PLAN is binding for
   room, order and cue (you may polish the cue wording, not change where it sends people).
4. Official map (Dec 2025): source/map.txt (every room title per level) and research/map/p-2.png (Level 2), p-3.png
   (Level 1), p-4.png (Level 0). Read the images: describe the walk truthfully (which rooms you pass), never invent doors.
5. research/LEVEL2_ROOMS_OCT2026.md, LEVEL1_ROOMS_OCT2026.md, LEVEL0_CARMEN_OCT2026.md (works confirmed per room, with
   official URLs), research/CURRENT_LOCATIONS_OCT2026.md (moves, loans, not exhibited) and
   research/AUDIT_OLD_GUIDE_FACTS_OCT2026.md (what the old guide got wrong: do not repeat it).
6. Old scripts (old/NNN.txt, OLD numbering; PLAN says which) help with stories, but their ROOMS AND MANY FACTS ARE WRONG.

## Accuracy rules (non-negotiable)
- Every load-bearing fact (date, commission, story, attribution, size) must be confirmed on the work's official
  museothyssen.org page or the room page (URLs in PLAN) via WebFetch. Room pages carry the curators' text: use it.
  For a work PLAN names without a URL, find its page (WebSearch `site:museothyssen.org <artist> <title>`) and check it
  says "Exhibited in Room …" with the right room. If a room page lists only some works, describe only works you confirmed. Read each of
  your works' official pages — they also give you the best material. Use WebFetch only; never Chrome/browser
  tools, never curl (the museum firewall blocks bursts — fetch one page at a time).
- If a fact from the old script can't be confirmed, drop it or frame it honestly ("the story goes…").
- Use the museum's official title in @what (Spanish/original title plus English, as on the English page).
- Only describe as present what you confirmed in that room. Never send people to a work that isn't on display.
- Nudes, religious and violent subjects: plain and respectful, follow the museum's own framing.
- Collection history: use the audit's corrected facts (1993 purchase of 775 works; Carmen Thyssen collection leased since
  2022). Never "the last Baron", never "Spain bought the whole thing".
- Quotations from artists or critics: only if on an official page, short, attributed.
- No ticket prices, opening hours, booking, or temporary exhibitions in the speech.

## Navigation rules (this is what the customers complained about)
- @room is exactly "Room 5" / "Room A" style (the number or letter on the museum's map). @where says where to stand in that room
  and how to recognise the work (size, colours, subject) — a card a visitor can use.
- The LAST paragraph of every track (except CLOSE) is the cue, as in PLAN's "cue to next": next room number, its title
  from the map when it helps (e.g. "Room 33, the Impressionist rooms"), plus one recognisable thing to look for.
  1–3 short sentences. Extras: the track before announces them ("Room 6 has a short Extra on …; the next main stop is
  Room 7"), as PLAN's cues already do.
- If the next stop is in the same room, say so ("Stay in Room 58…").
- Level changes: say which level and how (stairs or lift), and give the signs to follow, exactly as PLAN says.
- Never "next track", never "right this way", never "just over there", never "the next room along" without its number.
- Write room numbers as digits or letters everywhere, e.g. "Room 33", "Room F".
- Track 001 must explain, in two or three plain sentences, that the guide comes in three lengths: the full tour (about
  two and a half hours), the essential version (about an hour and a quarter) and the highlights (about forty minutes);
  whichever is on your phone, play it in order — the numbers may jump, and every stop says where to go next.

## Writing rules
- Never open with a command. Open with a hook: a surprising fact, a person, a tension.
- Length (spoken words, tags excluded): R 180–280 · W 250–360 · ANCHOR/CLOSE 250–360 · Extra (X) 150–230. Aim ~290 words for W/R.
- Average sentence 11–16 words; vary; max ~30. No parentheses, no semicolons, ≤2 em-dashes, no exclamation marks.
- Direction tags only from the standard: [pause] [long pause] [warmly] [quietly] [amused] [curious]
  [conspiratorial] [reverent] [wry] [lightly], *word* for stress. About one delivery tag per paragraph.
- Numbers as spoken ("around 1656", "almost a century later"). Max ~3 dates per track. Years as digits.
- "The museum says" at most once per track. Merged tracks (PLAN notes) cover each named work briefly but properly.
- First track of a painter/section folds in a short intro (PLAN notes say which) — 2–3 sentences, not a lecture.

## Output — one file per track: v5/tracks/NNN.perf.txt
```
@id: NNN · Room XX · 23 Oct 2026 edition
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
@sources: <official museothyssen.org URLs read, with what they confirmed; OFF = read on the official page>
---
<spoken body, paragraphs separated by blank lines, last paragraph = cue>
```
Old scripts (reference only, often wrong): old/NNN.txt by OLD number. Write v5/notes/<first>-<last>_NOTES.md: per track,
the official pages read and anything you could not confirm.

Check before finishing:  python3 v5/lint.py <your track numbers>   — every track must print OK.
Final reply ≤ 8 lines: tracks written, anything you could not verify, anything the lead must decide.

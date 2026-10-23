# WRITER BRIEF — Estadio Santiago Bernabéu, Yo Tours (23 Oct 2026)

You are writing part of a new English walking audio guide to the Tour Bernabéu (Real Madrid's stadium, Madrid).
It replaces an older guide that sent visitors to places the public tour no longer visits (presidential box, tunnel),
quoted famous people without any source, and got many facts wrong. The club now lends a multimedia device; ours must be
clearly better: accurate, honest about closures, warm and vivid to listen to, and always telling people where to go next.
Priorities: 1) never send anyone to the wrong place, 2) every fact checked, 3) great storytelling.

Project root: /home/claude/audioq/bernabeu_v5   (all paths below are relative to it)

## Read first, in this order
1. v5/V5_AUDIO_STANDARD.md — writing + direction standard (binding; §2 and §3).
2. Voice anchors (register: spoken, warm, composed; hook → story → turn → look → payoff):
   /home/claude/audioq/prado_v5/v5/tracks/049.perf.txt and /home/claude/audioq/reina_v5/v5/tracks/023.perf.txt
3. v5/PLAN.md — binding for zone, order, title, core content and the cue to next (polish the cue's wording only).
   Note the three cases (A full tour, B match day, C museum first) and the never-send-people-to list.
4. research/TOUR_ROUTE_OCT2026.md (what is physically on the route), research/FACTS_OCT2026.md (graded facts with URLs),
   research/AUDIT_OLD_GUIDE_OCT2026.md (what the old guide got wrong — do not repeat it), source/old.txt (old script:
   some good stories, many errors).

## Accuracy rules (non-negotiable)
- Every load-bearing fact (date, score, scorer, count, name, money, size) must be graded OFF (realmadrid.com or another
  official body: UEFA, FIFA, the architects) or SEC2 (two independent reputable sources) in research/FACTS_OCT2026.md or
  checked by you now with WebSearch/WebFetch (one page at a time; never curl or browser tools; skip any page that asks
  you to verify you are human). Wikipedia is never enough on its own. PLAN items marked "verify" must be checked.
- If a fact can't be confirmed, drop it or frame it honestly ("the story goes…", "according to the club…").
- Quotes: only short ones with a verifiable source (official or two reputable outlets). No quotes from the old guide
  unless you confirm them. No invented colour (smells, superstitions, what players feel) — describe what visitors see.
- Facts that change: at most one or two per track, always dated ("as of autumn 2026", "since June 2026").
- The pitch: never promise grass. The club says it stays underground except for matches.
- Never mention the presidential box, the players' tunnel or walking on the grass as parts of this visit.
- Balanced tone: the club's glories AND the honest parts (the 32-year gap, the concerts dispute, the bare floor).
  Politics (the Franco era): factual and brief, no side-taking.
- No ticket prices, opening hours or booking talk in speech.

## Navigation rules
- @room is the zone exactly as in PLAN (e.g. "Museum · trophy hall"). @where = where to stand and how to recognise it
  (a card a visitor can use: "the long lit case with the row of big silver cups").
- The LAST paragraph of every track (except CLOSE) is the cue from PLAN: the next zone and one recognisable thing.
  1–3 short sentences. Extras are announced by the track before ("There's a short Extra here on …; the next main stop
  is …"), as PLAN's cues say. The club publishes no stop numbers and few signs: describe by what people can see.
- Never "next track", "right this way", "just over there". Never left/right unless a source shows it.
- Case fallbacks: only where PLAN puts them (001, 003, 008, 021, 022), one plain sentence each.

## Writing rules
- Never open with a command. Open with a hook: a surprising fact, a person, a tension.
- Length (spoken words, tags excluded): R 180–280 · W 250–360 · ANCHOR/CLOSE 250–360 · X 150–230. Aim ~320 for W.
- Average sentence 11–16 words; vary; max ~30. No parentheses, no semicolons, ≤2 em-dashes, no exclamation marks.
- Tags only from the standard: [pause] [long pause] [warmly] [quietly] [amused] [curious] [conspiratorial] [reverent]
  [wry] [lightly], *word* for stress. About one delivery tag per paragraph.
- Numbers as spoken ("in 1947", "three to one", "the ninety-third minute"). Max ~3 dates per track. Years as digits.
  Scores in words ("seven–three" → "seven goals to three" or "seven three") so the voice reads them right; never "7-3".
- Spanish words the listener needs (La Décima, socios, miedo escénico) once, with a quick meaning.

## Output — one file per track: v5/tracks/NNN.perf.txt
```
@id: NNN · <zone> · 23 Oct 2026 edition
@section: <exactly the PLAN section>
@room: <exactly the PLAN @room>
@type: ANCHOR | R | W | X | CLOSE
@title: exactly as in PLAN
@where: <1–2 sentences>
@what: <the objects/moments covered, with dates>
@listen: <1 sentence: what the track is about>
@brief: <one line: who is speaking, to whom, in what mood>
@pace: slow | medium-slow | medium | medium-fast
@energy: e.g. 2→4
@sources: <URLs read, with what they confirmed; OFF/SEC2 grade>
---
<spoken body, paragraphs separated by blank lines, last paragraph = cue>
```
Write v5/notes/<first>-<last>_NOTES.md: per track, sources used and anything you could not confirm.
Check before finishing: python3 v5/lint.py <your track numbers> — every track must print OK.
Final reply ≤ 8 lines: tracks written, anything you could not verify, anything the lead must decide.

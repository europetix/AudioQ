# WRITER BRIEF — Pitti V5 test build (4 Oct 2026)

You are rewriting part of a walking audio guide to Palazzo Pitti + Boboli for a real user test.
Visitors complained that (1) the voice is monotonous, (2) the order doesn't follow their path, and the audit
found (3) ~210 factual/currency errors. The test uses the SAME free TTS voice, so everything that makes it
sound human must come from YOUR writing and direction. Read, in this order:
1. /home/claude/pitti/v5/V5_AUDIO_STANDARD.md — the writing + direction standard (binding).
2. /home/claude/pitti/v5/calibration/016.perf.txt, 017.perf.txt, 083.perf.txt — the VOICE ANCHORS. Match
   their register exactly: spoken, warm, composed; hook → story → turn → look → payoff; short varied sentences;
   honest hedges in plain words; at most one wry aside. Not a lecture, not a stand-up act.
3. /home/claude/pitti/v5/PLAN.md — the new running order (NEW number, OLD source, room, next physical stop).
4. For each of your tracks: the OLD source /home/claude/pitti/tracks/<OLD>.txt and the audit findings in
   /home/claude/pitti/findings/ (G1 = old 001–024, G2 = 025–046, G3 = 047–069, G4 = 070–078,
   G5 = 079–092, G6_ROUTE = route for everything). Apply EVERY correction and hedge the findings give for
   your tracks. Where a finding says a claim is wrong or unverifiable, fix it or drop it.

## Accuracy rules (non-negotiable)
- Use only facts that are (a) in the old script AND not contradicted by the findings, or (b) stated in the
  findings with a source, or (c) confirmed by you on an official page via WebFetch (uffizi.it etc.).
  WebSearch is exhausted for this session — do not rely on it. Never invent a detail to make a story better.
- Unverified-but-traditional stories are fine ONLY as clearly framed tradition ("the story goes…").
- Placement: say where a work is only as precisely as the findings support.
- No ticket prices, opening hours, booking instructions or temporary exhibitions in the spoken text.
  Closures ONLY when navigation needs them, in one plain sentence (e.g. the Iliad detour line in PLAN 021).
- No production jargon ("W-track", "track 12"). Never say "play the next track". Cues are self-contained:
  name the next physical place ("The Sala di Giove is through the doorway ahead; play its track there.").

## Writing rules (from the standard, highlighted)
- Never open with a command. Open with a hook: a surprising fact, a person, a tension.
- Length: R-INTRO 180–280 words · W-FOCUS 250–360 · ANCHOR/CLOSE 250–360 · merged overview tracks
  (PLAN 047, 048, 062, 078) 220–320.
- Average sentence 11–16 words; vary; max ~30. No parentheses, no semicolons, ≤2 em-dashes per track.
- Direction tags: only the vocabulary in the standard — [pause] [long pause] [warmly] [quietly] [amused]
  [curious] [conspiratorial] [reverent] [wry] [lightly] and *word* for stress. About one delivery tag per
  paragraph, a pause before a reveal. Don't over-direct. Free voices perform tags as pace/volume/pitch
  changes and real silences, so pauses carry most of the drama.
- Numbers as spoken ("around 1512", "almost a century later"). Max ~3 dates per track.

## Output — one file per track: /home/claude/pitti/v5/tracks/<NEW>.perf.txt (NEW = 3-digit PLAN number)
```
@id: <NEW> · old <OLD or NEW> · <room label>
@section: <section name exactly as in PLAN: Opening | Palatine | Royal Apartments | Modern Art | Fashion and Costume | Russian Icons and Chapel | Boboli | Closing>
@room: <display label, e.g. Room 24 · Stop 3 · Meeting point>
@type: ANCHOR | R | W | CLOSE
@title: <e.g. Raphael — Madonna della Seggiola>
@where: <1–2 sentences: where to stand, written for a card — this is where spatial direction belongs>
@what: <1–2 sentences: what the visitor sees; artist, title, date, medium if verified>
@listen: <1 sentence: what the track is about>
@brief: <one line: who is speaking, to whom, in what mood>
@pace: slow | medium-slow | medium | medium-fast
@energy: e.g. 2→4
@sources: <URLs backing the load-bearing facts, official first; or "old script + findings G#">
---
<spoken body with direction tags, paragraphs separated by blank lines>
```
For the calibration tracks (PLAN 033, 034, 070) do NOT change the body — copy it verbatim from
/home/claude/pitti/v5/calibration/ and only add the missing header fields (@section @room @type @title
@where @what @listen @sources). You may adjust ONLY its last route sentence if PLAN requires it.

Also write /home/claude/pitti/v5/notes/<range>_CHANGES.md: per track, one line per material change vs the old
script (fact fixed + source, cue fixed, content cut/added, hedge added). This becomes the audit resolution log.

Check yourself before finishing: run
  python3 -c "import sys;sys.path.insert(0,'/home/claude/pitti/v5/pipeline');import v5_direction as V,glob;[print(f,len(V.validate(f)[1].split())) for f in sorted(glob.glob('/home/claude/pitti/v5/tracks/*.perf.txt'))]"
and fix any error or out-of-range length in your files. Final reply: ≤8 lines (tracks written, anything you
could not verify, anything the lead must decide).

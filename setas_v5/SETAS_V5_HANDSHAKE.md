# Setas de Sevilla (Metropol Parasol) + Antiquarium V5 (Yo Tours) — handshake, STATE 1 (30 Oct 2026)

## What exists
- **English:** `v5/tracks/001–018.perf.txt` — 16 main stops + 2 Extras (014 Aurora, 015 Feeling Sevilla), ~4,700 words
  (~38 min of listening). Order: welcome at street level (Calle Imagen side; north entrance mentioned) → down to level −1
  (taquilla) → Antiquarium 002–006 (Full only; own entrance and admission) → 007 by the lifts → 008 in the lift / first
  walkway → 009 Giralda view (south) → 010 river and Aljarafe (west) → 011 timber and glue → 012 Mirador 360º (steps) →
  013 the controversy → Extras 014–015 → 016 the way down past the exhibition → 017–018 Plaza Mayor (end; way out to the street).
- **User decisions (30 Oct):** build from scratch; the Antiquarium as its own section; lengths 20 / 35 / 60 min;
  EN/ES/FR/DE. Planned visit times: Full just under 1 h, Essential ~35, Highlights ~25 (the lifts and walking alone take
  ~14 min, so Highlights can't reach 20). Times exclude the Feeling Sevilla film (~15 min).
- **No official visitor map online:** no numbers spoken; directions by fixed features; only two views named (Cathedral +
  Giralda south, river + Aljarafe west); anything else after the on-site check. Route map is SCHEMATIC (dashed = unconfirmed).
- **Research:** `research/VISIT_ROUTE_AND_SPACES_OCT2026.md`, `FACTS_OCT2026.md` (Red Dot correction 30 Oct),
  `OFFICIAL_AUDIO_COMPARISON_OCT2026.md` (free QR web audio, languages unclear; official app), `AUDIT_V5_001-018.md`
  (independent audit: 1 MUST, 13 SHOULD, 17 NICE; fixes in `v5/notes/AUDIT_FIXES_001-018.md`; lead decisions at the end
  of `v5/PLAN.md`).
- **Held / provisional:** 005 is a position-free walk-along (check against the Antiquarium labels; fold into 004 if
  needed); 001 durations until the stopwatch walk; Rowan Moore quoted without naming the paper (Observer unconfirmed);
  Antiquarium 8.5 m € figure cut; steel reinforcement in the 2007 redesign left out.
- **Corrections from translators/reviewers:** 013 "Its critics said…" (Público: the critics' verdict, not a saying);
  010 "is titled" (the study has a subtitle).
- **Lengths:** `build/static/lengths.json` (Essential 11, Highlights 4); 5 hand-written bridges (`v5/bridges/*.txt`,
  `v5/i18n/<lang>/bridges.txt`); Extras-only skips silent except 013 E>016 (hand bridge, since 013 announces the Extras).
- **Translations:** `v5/i18n/{es,fr,de}/tracks/` 18 each, checks pass (N_TRACKS = 18); one translator + one independent
  reviewer per language; briefs and reviews in `v5/i18n/review_30oct/`. "Mirador 360º" is written in words in the
  spoken text of ES/FR/DE. ES quotes Público verbatim («como a un Cristo dos pistolas», «una moderna catedral urbana»,
  verified). DE: Rundweg (rooftop walkway) vs Steg (Antiquarium walkways); Kruse and one Mayer quote as reported speech.
- **Build:** `bash build/build_all.sh` → `bundle/Setas_YoTours` + `/mnt/user-data/outputs/Setas_YoTours_ALL_LANGUAGES.zip`.
  Route sheet `build/route_map.py` (5 pages: building section, Antiquarium, walkways from above, way down, stop table).
  Cover `build/cover/make_cover.py` (abstract parasols). Pronunciation +44 names (Mirador 360º → "three-sixty").
- **Tested (stand-in tones, not speech):** EN option 1 → 18/11/4 with 2+3 bridges; DE option 3 → 4 with 3 bridges.
  Real voices not heard.

## On-site (before recording) — `v5/ONSITE_CHECKLIST.txt`
The printed plan from the taquilla (photo requested from the user); the way to level −1 and the lifts; the Antiquarium
route and labels (005); where the lift lets you out; which landmarks can be named from the walkway and the Mirador; the
Feeling Sevilla room and the exhibition; the way out from the Plaza Mayor; a stopwatch walk for the times.

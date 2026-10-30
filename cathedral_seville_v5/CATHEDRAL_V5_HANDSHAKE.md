# Catedral de Sevilla + Giralda V5 (Yo Tours) — handshake, STATE 1 (30 Oct 2026)

## What exists
- **English:** `v5/tracks/001–028.perf.txt` — 23 main stops + 5 Extras, ~7,500 words (~60 min of listening; three Giralda
  tracks are heard while climbing/descending). Order: welcome at the entrance (Lagarto for online tickets, Príncipe /
  San Cristóbal for the ticket office) → the Giralda first, as the Cabildo says (002 minaret, 003 the 34 ramps, 004 the bell
  level, 005 Extra bells, 006 mosque → cathedral on the way down) → 007 at the foot of the Giralda → Capilla Mayor (Retablo,
  grilles Extra) → Coro → Capilla de San Antonio → west end → Capilla de la Antigua → Columbus ×2 → Sacristía de los Cálices →
  Sala del Pabellón (Extra) → Sacristía Mayor ×3 → Sala Capitular ×2 → Capilla Real from the grille → Puerta de la Concepción →
  Patio de los Naranjos → the Giraldillo → Nave del Lagarto → out by the Puerta del Perdón (no re-entry).
- **User decisions (30 Oct):** build from scratch (no old guide supplied); lengths 45 / 75 / 110 min with the Giralda;
  EN/ES/FR/DE. Full lands "just over an hour and a half" (001 says so) — not padded; on-site checks of the north-aisle
  chapels could add 2–3 Extras.
- **No official visitor map exists online**: directions use Spanish names + landmarks; no place numbers. Route map is a
  clearly SCHEMATIC plan (dashed outlines for unconfirmed positions).
- **Research:** `research/VISIT_ROUTE_AND_SPACES_OCT2026.md` (entrances, Giralda first, exit, Capilla Real worship-only,
  Zurbaráns in the Sala del Pabellón, Artemisia under restoration, Giralda works phase VI from Apr 2026 ~22 months, lily vases
  removed Feb 2026, Silver Altar removed Jan 2025), `FACTS_OCT2026.md` (verified facts, legends, popular errors: "think us mad"
  is tradition; "third-largest" unsourced; Lagarto crocodile later tradition; 34 ramps per the Cabildo 2025 congress;
  Columbus DNA exact wording; Campaña 1547), `OFFICIAL_AUDIO_COMPARISON_OCT2026.md` (GVAM guide €4–5, numbers don't match),
  `AUDIT_V5_001-028.md` (independent audit; fixes in `v5/notes/AUDIT_FIXES_001-028.md`).
- **Held:** the El Greco paragraph in 017 (loan unconfirmed for Oct 2026) — text in the audit-fix notes; lily-vase and
  Silver Altar sentences (only if seen on site).
- **Lengths:** `build/static/lengths.json` (Essential 18, Highlights 9); 7 hand-written bridges (`v5/bridges/*.txt`,
  `v5/i18n/<lang>/bridges.txt`); Extras-only skips silent; Highlights non-climbers sent to the Capilla Mayor (001).
- **Translations:** `v5/i18n/{es,fr,de}/tracks/` 28 each, checks pass; one translator + one independent reviewer per
  language; notes in `v5/i18n/review_30oct/`. DE: die vollständige Tour / die Kernversion / die Highlights; ES as Alcázar ES.
- **Build:** `bash build/build_all.sh` → `bundle/Cathedral_YoTours` + `/mnt/user-data/outputs/Cathedral_YoTours_ALL_LANGUAGES.zip`.
  Route sheet `build/route_map.py` (5 pages, schematic). Cover `build/cover/make_cover.py`. Pronunciation +32 names.
- **Tested (stand-in tones, not speech):** EN option 1 → 28/18/9 with 3+4 bridges; FR option 3 → 9 with 4 bridges.

## On-site (before recording) — `v5/ONSITE_CHECKLIST.txt`
Príncipe entrants and the Giralda-first rule (001); the door into the Patio; the sacristy-block order; the Ascension window
(023/024); the Perdón relief side; El Greco / Artemisia / Zurbarán labels in the Sala del Pabellón; Columbus tomb position.

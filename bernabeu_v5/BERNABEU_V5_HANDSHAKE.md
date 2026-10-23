# Estadio Santiago Bernabéu V5 (Yo Tours, Tour Bernabéu) — handshake, STATE 1 (23 Oct 2026)

## What exists
- **English:** `v5/tracks/001–028.perf.txt` — 23 main stops + 5 Extras (@type X), ~7,800 words (~62 min; main ~54 min).
  Zones in order: Outside (001–003) → Panoramic view, top tier (004–008) → Museum + trophy hall (009–022) → Dressing room
  (023) → Benches (024–025) → Press room if open (026 X) → Store (027) → Exit (028).
- **Three cases (user, 23 Oct):** A full tour 001→028; B match day / day before (dressing room + benches closed):
  after the museum play 022, then 027–028; C museum first: 001–003, 009–022, 004–008, 023 on. Spoken jumps
  ("play number twenty-two") in 001, 003, 007, 008, 019–022.
- **Three lengths (user, 23 Oct, clarified):** Full 28 tracks ~65 min; Essential 17 (001 002 003 004 007 009 010 011 013 014
  016 019 022 023 024 025 028) ~40 min; Highlights 9 (001 003 007 010 016 022 023 025 028) ~20 min. Launcher option 1 records
  once and copies the two shorter folders; option 3 = Highlights only. 001 explains the lengths. The match-day / museum-first
  handling stays in the tracks.
- **Route map (user: 'draw something from the stadium'):** 3 pages — section drawing of the bowl with zones, aerial with
  streets/entrance/store/S10, stop list with the three lengths.
- **User decisions (23 Oct):** 60–75 min of audio; facts that change are few and dated "as of autumn 2026";
  languages EN/ES/FR/DE; compare with the club's own guide (research/OFFICIAL_AUDIO_COMPARISON_OCT2026.md, Yo Tours
  column filled in).
- **Plan / brief / lint:** `v5/PLAN.md`, `v5/WRITER_BRIEF.md`, `v5/lint.py` (zone cues; "billion/million euros" allowed).
- **Research:** `research/TOUR_ROUTE_OCT2026.md`, `FACTS_OCT2026.md`, `AUDIT_OLD_GUIDE_OCT2026.md` (old guide: rebuild),
  `OFFICIAL_AUDIO_COMPARISON_OCT2026.md` (club's GVAM loan-device guide since 5 Jun 2026, 50+ items, 12 languages claimed),
  `AUDIT_V5_23OCT2026.md` (independent route + fact audit; all must-fix items applied).
- **Translations:** `v5/i18n/{es,fr,de}/tracks/` assembled, checks pass (N_TRACKS = 28); briefs, translator notes and the
  three independent reviews in `v5/i18n/review_23oct/`. ES 019 uses the verified Spanish AFP wording.
- **Build:** `bash build/build_all.sh` → `bundle/Bernabeu_YoTours` + `/mnt/user-data/outputs/Bernabeu_YoTours_ALL_LANGUAGES.zip`.
  Route sheet `build/route_map.py` (2 pages: zones flow + three cases, stop list) — schematic, the club publishes no plan.
  Cover `build/cover/make_cover.py` (original stadium drawing, no crest). Sound/labels identical to Prado/Reina.
- **Launchers:** EN option 2 samples 016 La Décima + 025 comebacks; option 3 = 23 main stops. Output
  `~/Desktop/Bernabeu_YoTours_<LANG>_<voice>`.
- **Tested:** stand-in TTS only (tones): EN full 28, ES samples, FR main stops 23; labels checked. Real voices not heard.

## Not used (and why)
Presidential box, players' tunnel, walking on grass (not on the public tour); the 1944 "temple" quote; Messi/Puyol/
Ferguson/Casillas/Roberto Carlos quotes; dressing-room colour; facade slat counts; Acerinox; hypogeum depth; Eiffel Tower.

## Dated items to revisit
- 019 Ballon d'Or: counts to 2025; ceremony 26 Oct 2026 — add one line if a Madrid player wins.
- 028 metro: L10 closed to end-2026, new station Q1 2027 — re-record 028 when it opens.
- 007 concerts "no return announced as of autumn 2026"; 015 Pérez re-elected June 2026; 024 Mourinho since June 2026;
  025 Valverde captain; 027 "no shareholders as of autumn 2026".
- On-site: `v5/ONSITE_CHECKLIST.txt`.

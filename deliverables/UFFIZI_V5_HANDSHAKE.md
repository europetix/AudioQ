# Uffizi Gallery V5 (Yo Tours) — handshake, STATE 1 (24 Oct 2026)

## What exists
- **English:** `v5/tracks/001–067.perf.txt` — 53 main stops + 14 Extras (@type X), ~17,800 words (~143 min of listening).
  One walking order on the museum's Complete line: second floor A1–A39 (13th century → Botticelli rooms → Tribune →
  High Renaissance → Raphael/Michelangelo → Niobe), down the **Lanzi staircase one floor only**, Contini Bonacossi B,
  self-portraits C1–C5, 16th century D1–D19, Venice D20–D27, the Verone D28, 17th century E4–E7, out by the Magliabechi
  staircase. Closed rooms (A9, A17–A21, A33, A36, A40–A42, C6–C12, D3, D10, D11; D9 conditional) are never stops.
- **User decisions (24 Oct):** three time-based lengths, Highlights ~75 min / Essential ~120 / Full ~165 including walking
  (not the museum's Fast/Classic/Complete); no Vasari Corridor section (D19 track only says where it starts, one way to
  Boboli); languages EN, ES, FR, DE **and IT** (first Italian guide in the series: voice it-IT-IsabellaNeural, option 4).
  The guide must beat the official €6 handset and the competitors (research/OFFICIAL_AUDIO_COMPARISON_OCT2026.md).
- **Lengths:** `build/static/lengths.json` — Essential 40, Highlights 19. Bridges are HAND-WRITTEN per skip
  (`v5/bridges/*.txt`, translated in `v5/i18n/<lang>/bridges.txt`, 23 lines each) and appended after the track's own cue;
  skips of Extras only get no bridge (the cue already names the next main stop). make_lengths.py reads `levels.txt` (JSON:
  floors, spoken floor names, Botticelli alias) and `bridges/<lang>.txt`.
- **Botticelli rooms:** the museum's map legend says A9, its plan shading, pages, notice and June 2026 news say A10–A12.
  Speech, titles, file names, scripts and the route map never give their numbers ("Botticelli rooms · …"); cues follow
  the museum's signs from A8 with a fallback via A13 (ONSITE O7, CRITICAL).
- **Held:** Tintoretto (old 059) — no work confirmed on display; old 060–068 renumbered 059–067. Madonna of the Harpies
  (PLAN 045) dropped — not confirmed on view (A41 closed; C9/C10 unclear).
- **Research:** `research/FLOOR2_LOCATIONS_OCT2026.md`, `FLOOR1_LOCATIONS_OCT2026.md`, `NOTICES_OCT2026.md` (closures
  notice 15 Sep 2026; not-on-display list 21 Oct 2026; strike 30 Oct 2026), `AUDIT_OLD_GUIDE_FACTS_OCT2026.md` (22 wrong,
  52 hedge; Family Pact 1737 wording), `OFFICIAL_AUDIO_COMPARISON_OCT2026.md` (bar to beat), `AUDIT_V5_001-034.md`,
  `AUDIT_V5_035-067.md` (independent route + fact audits; fixes in `v5/notes/AUDIT_FIXES_*.md`).
- **Plan / brief / lint:** `v5/PLAN.md` (old numbering from 059 on; see its renumbering note), `v5/WRITER_BRIEF.md`,
  `v5/lint.py` (room cue regex accepts A–E codes, staircases, corridors, Verone, Tribune, floor, "Botticelli rooms").
- **Translations:** `v5/i18n/{es,fr,de,it}/tracks/` 67 each, checks pass (N_TRACKS = 67); two translators per language and
  one independent reviewer each; briefs, notes and reviews in `v5/i18n/review_24oct/`. DE Dante = Philalethes (verified);
  IT Dante and Vasari in the original (verified), other Italian quotes reported speech; ES numbers written for feminine
  agreement; Treaty of Vienna (022) is the museum's own wording.
- **Pronunciation:** `build/static/pronunciation.py` +70 Uffizi names (Gentile, Maestà, Cimabue, Uccello, Uffizi …),
  not yet heard. Thyssen-only entries removed.
- **Build:** `bash build/build_all.sh` → `bundle/Uffizi_YoTours` + `/mnt/user-data/outputs/Uffizi_YoTours_ALL_LANGUAGES.zip`.
  Route sheet `build/route_map.py` (7 pages: overview of both floors, four route pages, stop table with F/E/H), our own
  plan drawn from the museum's October 2026 map, closed rooms hatched. Cover `build/cover/make_cover.py` (courtyard drawing).
- **Launchers:** `generate_audio.command` (EN; option 2 samples 018 Venus + 062 Medusa; option 3 Highlights only now
  records into the full folder and makes the Highlights folder WITH bridges) and `generate_audio_ES_FR_DE_IT.command`.
- **Tested (stand-in tones, not speech):** EN option 3 → 19 tracks, 12 bridges; ES option 1 → 67/40/19, 11+12 bridges;
  IT option 3 → 19, 12 bridges; all translated bridges hand-written (23 per language). Real voices not heard; the
  it-IT-IsabellaNeural voice name is unverified until the user's first Italian sample.

## Dated items to revisit
- 10 Jan 2027 Correggio back in D4 (045); 24 Jan 2027 Tintoretto Leda back in D25 (consider an Extra); 7 Feb 2027
  Pontormos and Bronzino back (048, 051, 052); 11 Apr 2027 Tetrode Venus back in A15 (021).
- Every two weeks: the not-on-display PDF and the closed-rooms notice. Botticelli numbering and signage (June 2026 news:
  "complete replacement of the museum's signage is underway").
- On-site and listening checks: `v5/ONSITE_CHECKLIST.txt` (CRITICAL: O7 Botticelli entry, O13 A33, O21 C6–C12 corridor,
  O24 D9 passage).

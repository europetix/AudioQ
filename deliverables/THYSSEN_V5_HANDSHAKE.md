# Museo Nacional Thyssen-Bornemisza V5 (Yo Tours) — handshake, STATE 1 (23 Oct 2026)

## What exists
- **English:** `v5/tracks/001–070.perf.txt` — 51 main stops + 19 Extras (@type X), ~19,600 words (~157 min of listening;
  main ~125 min). Route top down, as the museum advises: Level 2 (Rooms 1–29, old masters to Friedrich) → Level 1
  (Rooms 30–52, Impressionism to Pop; Rodin room) → Level 0 (Carmen Thyssen Rooms A–J) → exit on the Paseo del Prado.
- **Skipped on purpose (dated):** Rooms 19–21 (Mauritshuis visiting display, until 10 Jan 2027) and the Postpop
  Rooms 53–56 (Kenny Scharf exhibition, until 17 Jan 2027). The guide walks past them and says so.
- **Three lengths (user, 23 Oct), from one recording:** Full 70 tracks (~2 h 30 with walking); Essential 26
  (001 002 006 007 010 014 016 020 023 024 029 031 035 036 038 039 043 045 049 050 052 054 056 059 065 070, ~63 min listening,
  ~1 h 15 with walking); Highlights 14 (001 002 006 007 010 016 029 031 038 050 052 056 065 070, ~34 min listening, ~40 min).
  Spoken bridges (user chose) are added by `build/static/make_lengths.py` wherever a shorter version skips ahead:
  "Next stop on this shorter tour: Room 32, on Level 1. John Singer Sargent, …" — level is spoken only when it changes
  (`levels.txt` marker: 1–29 Level 2, 30–56 Level 1, A–J Level 0). Titles: brackets become a comma; a final " I" is
  spoken as One/uno/un/eins. 19 bridges in Essential, 11 in Highlights.
- **Old guide:** `source/` (old PDF, 70 tracks) — `research/CURRENT_LOCATIONS_OCT2026.md`: 26 of 47 works it names were
  in the wrong room or not on show; `AUDIT_OLD_GUIDE_FACTS_OCT2026.md` (1993 purchase 775 works for $350m; Carmen Thyssen
  lease since Feb 2022, 15 years at €6.5m a year). Rebuilt from scratch.
- **Map:** `source/FolletoThyssen_EN_map.pdf` (Dec 2025) + `map.txt` room titles; research per level
  (`LEVEL2_ROOMS`, `LEVEL1_ROOMS`, `LEVEL0_CARMEN`).
- **Official audio guide comparison:** `research/OFFICIAL_AUDIO_COMPARISON_OCT2026.md` (museum guide €5.50, 15/30/50 works,
  10 languages; Carmen Thyssen tour ES/EN only; Yo Tours column filled in).
- **Audits:** `research/AUDIT_V5_001-035.md`, `AUDIT_V5_036-070.md` (independent route + facts); fixes in
  `v5/notes/AUDIT_FIXES_*.md`. Key: 004 rebuilt on Gerard David's Crucifixion (Daret not exhibited); door routes in
  013/015/021/030; 031 "largely ended his work in oils"; 042 Hitler not named. Mondrian fallback: `v5/held/048.fallback.perf.txt`.
- **Translations:** `v5/i18n/{es,fr,de}/tracks/` 70 each, assembled, checks pass (N_TRACKS = 70); two translators per
  language, then one independent reviewer each; briefs, translator notes and reviews in `v5/i18n/review_23oct/`.
  ES uses the museum's Spanish titles (checked on museothyssen.org); 054 Rosenblum «lo sagrado» per the Spanish page.
  FR quotes first said in French are reported speech (no unconfirmed "original" wording). Room I: EN "Room Eye",
  DE "Saal I, wie Ida", FR "la salle I, comme Irène", ES "la sala de la letra i". ES 056/057 "jota, i griega, eme".
- **Build:** `bash build/build_all.sh` → `bundle/Thyssen_YoTours` + `/mnt/user-data/outputs/Thyssen_YoTours_ALL_LANGUAGES.zip`
  (includes route PDF, ONSITE_CHECKLIST, make_lengths.py, levels.txt). Route sheet `build/route_map.py`, 6 pages
  (overview of three levels + lengths, two Level 2 pages, two Level 1 pages, Level 0), geometry from the museum map.
  Cover `build/cover/make_cover.py` (palace front with garden, original drawing).
- **Launchers:** voice first, then: option 1 all three lengths (records once); option 2 samples 029 Rembrandt + 050 Hopper;
  option 3 Highlights only. Output `~/Desktop/Thyssen_YoTours_<LANG>_<voice>` (+ `_Essential`, `_Highlights`).
- **Tested:** stand-in TTS only (tones, not speech): EN option 1 → 70/26/14 with 19/11 bridges; FR option 1 → 70/26/14;
  EN (Brian) option 1 again → 70/26/14. All bridge texts printed and read in all four languages. Real voices not heard.

## Dated items to revisit
- 10 Jan 2027: 021 last sentence, 028 Mauritshuis Saenredam sentence (Rooms 19–21 reopen to the collection — re-route).
- 17 Jan 2027: 004 Van Eyck, 012 Dürer, 014 later Annunciation (back from The Hague); 040 and 059 Kenny Scharf (Rooms 53–56
  reopen — re-route).
- 24 Jan 2027: 049 Dalí exhibition line.
- On-site and listening checks: `v5/ONSITE_CHECKLIST.txt` (incl. running time of each length vs what 001 says).

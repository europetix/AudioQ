# Museo Reina Sofía V5 (Yo Tours) — handshake, STATE 1 (17 Oct 2026)

## What exists
- **English:** `v5/tracks/001–057.perf.txt` — 43 main stops + 14 Extras (@type X), 15,971 words (main ≈ 1 h 45 of listening,
  about 2 h with walking). Walking order: Sabatini entrance (Floor 1) → garden Extra → Room 102 Serra → glass lift to Floor 2:
  one loop round the cloister 201 → 202 → 204 → 205 (Guernica 205.10, mid back wing) → 206 → glass lift to Floor 4: Rooms 1–21
  (between the lifts, right side, back, left side) → glass lift down to Floor 1 → Nouvel building → lift to the Floor 3 roof
  terrace (056) → closing (057).
- **Plan:** `v5/PLAN.md` (same numbering as the tracks). Writer brief `v5/WRITER_BRIEF.md`, lint `v5/lint.py`, writers' notes
  `v5/notes/`.
- **Old guide:** `source/Museo_Reina_Sofia_EN_old.pdf`, parsed in `old/NNN.txt`. Audit `research/AUDIT_OLD_GUIDE_17OCT2026.md`:
  of 49 works only 22 still on display → full rebuild.
- **Research:** `research/CURRENT_COLLECTION_OCT2026.md` (room chains, "Exhibited in Room" strings; terrace correction at the
  top), `research/FLOOR2_LAYOUT.md` (§6 = the official Floor 2 room plan, read in Chrome 17 Oct), `research/map/` (official
  easy-read plan Oct 2026–Feb 2027, Floor 4 map), `research/FACT_AUDIT_17OCT2026.md` (independent audit: 146 claims, all
  WRONG/HEDGE items fixed in the tracks).
- **Translations:** `v5/i18n/{es,fr,de}/tracks/` (assembled, checks pass, N_TRACKS = 57). Translator notes and the three
  independent reviews: `v5/i18n/review_17oct/`. Briefs used: scratchpad copies, same content as Prado's adapted (glossary for
  Sabatini/Nouvel, room codes like 205.10 kept as digits).
- **Build:** `bash build/build_all.sh` → `bundle/ReinaSofia_YoTours` + `/mnt/user-data/outputs/ReinaSofia_YoTours_ALL_LANGUAGES.zip`.
  Route map: `build/route_map.py` (5 pages: overview cross-section of both buildings, Floor 1 + terrace, Floor 2 in two pages
  by chapter, Floor 4). Floor 2 geometry from the official room plan turned a quarter-turn; Floor 4 from the official map.
- **Sound and labels:** pipeline identical to Prado/Orangerie (voice finishing, room tone, chime; tag_tracks.py with MUSEUM
  "Museo Reina Sofía", cover `build/static/cover.jpg` made by `build/cover/make_cover.py`).
- **Pronunciation:** `build/static/pronunciation.py` reads room codes for the English voice: 205.10 → "two-oh-five point 10".
- **Launchers:** EN `generate_audio.command` (1 full, 2 samples 023 Guernica + 044 Juan Muñoz, 3 main stops only); ES/FR/DE
  `generate_audio_ES_FR_DE.command` (same options). Output `~/Desktop/ReinaSofia_YoTours_<LANG>_<voice>`.
- **Tested:** stand-in TTS only (tones, not speech): EN + ES samples, DE main stops (43 files), labels checked. Real voices not heard.

## Held / not used (and why)
- Old-guide stories with no official source: Calder fountain running with real mercury (kept only as the museum frames it),
  Dalí canvas slashed, Cap de Creus ants, Aidez l'Espagne stamp story, Falling Soldier authenticity debate.
- Judy Chicago's *Women and Smoke* — not in Room 4's artist or works list (only a photo caption).
- Room 205.08 — the Dumile Feni display ended 22 Sep 2026; content unknown, the guide walks past it.
- Rooms 203, 207, 208 (Floor 2) — on the plan but not in today's web chain; not on the route.
- Floor 3 Sabatini — closed until 2027.

## Open (on site / listening) — see `v5/ONSITE_CHECKLIST.txt`
- Room numbers at doorways (Floor 2 renumbered after 2021); Room 102 wing on Floor 1; Gargallo's Great Prophet in the garden?;
  205.03 / 205.03 bis open?; the way from 206.03 to the lifts; Nouvel terrace open?
- Listening: EN room codes; DE "Saal 205.03 bis" (bis = until); FR "MIT"; room codes in ES/FR/DE.
- ES titles still unconfirmed: room 205.07 title (Spanish page shows English), Schlemmer's "El abstracto" (014), second half of
  the Heartfield slogan (016).

# Prado V5 (Yo Tours) — handshake, STATE 1 (10 Oct 2026)

## What exists
- **English:** `v5/tracks/001–081.perf.txt` — 59 main stops + 22 Extras (@type X), 23,729 words (main ≈ 2 h 30 of listening).
  Walking order: Floor 0 north (Flemish/Italian, Raphael, medieval) → Floor 2 north (Rembrandt, Dauphin) → Floor 1
  (Room 1 → Titian 40–44 → 2–7A → El Greco → Velázquez → Central Gallery loop 27-26-25 → 14-15-15A → Murillo → Van Dyck →
  Rubens 28-29 → Goya 32-38 → 39 → Tiepolo 23) → Floor 2 south (Goya cartoons 90, 93, 85) → Floor 0 south (71, 67, 66, 64,
  63B, 75, 61B, 61, 60A) → entrance hall.
- **Numbering history:** `v5/RENUMBER_10OCT2026.md` (new → old; xNN = Extra). `v5/PLAN.md` and `v5/PLAN_EXTRAS.md` use the
  OLD numbers (59-stop plan + x01–x22). Pre-renumber copies: `v5/held/core59_before_renumber_10oct/`, `v5/held/extras_src_10oct/`.
- **Translations:** `v5/i18n/{es,fr,de}/tracks/` (assembled, `assemble.py` checks pass, N_TRACKS = 81). Work JSON, briefs,
  translator notes and the three independent reviews: `v5/i18n/review_10oct/`.
- **Research:** `research/OFFICIAL_LOCATIONS_PRADO_10OCT2026.md` + `research/*_result.tsv` (every room read on the work's own
  museodelprado.es page), `research/extras/*_result.tsv` (Extras candidates), `research/map/` (official 2026 plan PDF + crops).
- **Audits:** `v5/notes/AUDIT_ROUTE_10OCT.md`, `AUDIT_FACTS_001-030.md`, `AUDIT_FACTS_031-059.md` (old numbering),
  `AUDIT_EXTRAS_10OCT.md` (new numbering); writers' change logs in `v5/notes/`.
- **Build:** `bash build/build_all.sh` → `bundle/Prado_YoTours_EN` + zip. Route map: `build/route_map.py` (HTML/SVG → PDF via
  Playwright Chromium; room centres measured from the official plan; 7 pages). `build/route_sheet.py` is the old one-page A3
  version, no longer used. Lint: `python3 v5/lint.py`.
- **Launchers:** EN `generate_audio.command` (1 full, 2 samples 049 + 071, 3 main stops only); ES/FR/DE
  `generate_audio_ES_FR_DE.command` (same options). Output `~/Desktop/Prado_YoTours_<LANG>_<voice>`.

## Held / not used (and why)
- Zurbarán *Agnus Dei* — on loan to the Louvre until 25 Jan 2027.
- Correggio *Noli me tangere* (Room 49) — on loan to Dresden until 10 Jan 2027 (could rejoin Extra 014 after).
- Titian *Christ Carrying the Cross* (P000438) — English page "Not on display", Spanish page "Sala 043": cut from Extra 030.
- El Greco *Baptism* — not on display. Velázquez *Aesop*/*Menippus* — pages disagree (012/015): not mentioned.
- Room 74 Christina of Sweden display — temporary (to 7 Feb 2027): no Extra there.
- Leoni *Charles V and the Fury* — Room 1 per sub-record only; track 027 has a fallback to the Leoni bronze in Room 27.

## Open
- On-site: `v5/ONSITE_CHECKLIST.txt` (floor changes 19→20, 26→27, 66→67, 69→70; doorways; Goya 32–39 rehang; where room
  numbers are shown).
- User: real-voice samples, then full renders (4 languages); native-speaker spot check (`deliverables/Prado_YoTours_Scripts_*.md`).
- Research tip: museodelprado.es artwork pages read fine with WebFetch; the search page and content3.cdnprado.net are behind
  Cloudflare. In Chrome, the user must click "Verify you are human"; never send bursts (the firewall blocked the user's browser).

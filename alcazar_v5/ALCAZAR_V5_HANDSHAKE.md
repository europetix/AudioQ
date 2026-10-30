# Real Alcázar de Sevilla V5 (Yo Tours) — handshake, STATE 1 (30 Oct 2026)

## What exists
- **English:** `v5/tracks/001–035.perf.txt` — 33 tracks in the walking order (26 main + 7 Extras) plus 2 optional Cuarto Real
  Alto Extras (034–035), ~9,600 words (~73 min of listening in the walking order).
  Route on the official leaflet's numbers 1–53: Puerta del León → 1 → 2 → 3 → 4 → 5 → 6–7 (Casa de la Contratación) → Pedro's
  palace 10, 13, 15, 16, 18 → back out the palace door → 31 → 32 → 33 → Baths 34 → 37 → 36 → 35 and back (Full only) → 38 →
  39 → 40 → 41 → 44 → 45 → 46 → 51 → 53 Apeadero → Patio de Banderas (SALIDA). The Muñecas → Jardín del Príncipe passage
  (reopened Mar 2025) is mentioned but not used (its one-way rules are unknown).
- **User decisions (30 Oct):** rebuild from scratch ("the work is quite old and not great"); lengths Highlights ~45 /
  Essential ~75 / Full ~120 min with walking; Cuarto Real Alto as optional Extras (only 2 sourceable); languages EN/ES/FR/DE.
- **Old guide:** `source/old.txt`, split in `old/` (20 tracks). It claimed to be verified; the audit found ~48 wrong claims,
  ~60 unsourced, ~15 price/ticket lines (`research/AUDIT_OLD_GUIDE_FACTS_OCT2026.md`).
- **Official leaflet:** `source/triptico_alcazar_sevilla.pdf` (from the user, 30 Oct; the site blocks the cloud shell),
  renders `research/map/t-2.png`, `hi-2.png`. It dates from 2016 (re-uploaded Nov 2024) and does not show the 2025 passage.
- **Research:** `research/VISIT_ROUTE_AND_SPACES_OCT2026.md` (numbering, statuses: shop closed 19 Oct 2026, Pabellón de
  Carlos V restoration, Mercury bronze replica, Doncellas restoration in phases), `OFFICIAL_AUDIO_COMPARISON_OCT2026.md`
  (free MuseumMate QR guide "complicated and limited", numbers don't match the map; paid Artymax app poorly reviewed),
  `AUDIT_V5_001-035.md` (independent route + fact audit; fixes in `v5/notes/AUDIT_FIXES_001-035.md`).
- **Map pass:** `v5/notes/MAP_PASS_30OCT.md` — directions from the drawing; stair 19 is in the Montería corner by the
  Cuarto del Almirante; 53 does not open off the Montería.
- **Lengths:** `build/static/lengths.json` (Essential 20, Highlights 10; 034–035 outside the lengths). Hand-written bridges
  `v5/bridges/*.txt` (10 lines) and `v5/i18n/<lang>/bridges.txt`; Extras-only skips are silent. `levels.txt` gives the spoken
  "number N" for generic bridges.
- **Translations:** `v5/i18n/{es,fr,de}/tracks/` 35 each, checks pass (N_TRACKS = 35); one translator + one independent
  reviewer per language; briefs, notes and reviews in `v5/i18n/review_30oct/`. ES quotes three original Spanish texts verbatim
  (verified). Version names: ES recorrido completo / versión esencial / imprescindibles; FR as reviewed; DE die vollständige
  Tour / die Kernversion / die Highlights.
- **Build:** `bash build/build_all.sh` → `bundle/Alcazar_YoTours` + `/mnt/user-data/outputs/Alcazar_YoTours_ALL_LANGUAGES.zip`.
  Route sheet `build/route_map.py` (5 pages: site overview, palaces, gardens, Cuarto Real Alto, stop table; our own drawing,
  numbers as on the leaflet; garden route line approximate). Cover `build/cover/make_cover.py`. Pronunciation +50 names.
- **Tested (stand-in tones, not speech):** EN option 1 → 35/20/10 with 4+6 bridges; DE option 3 → 10 with 6 bridges.
  Real voices not heard.

## Dated / on-site
- Pabellón de Carlos V: recorded as "may still be behind screens" (version b); swap in (a) when reopening is confirmed (O24).
- Doncellas restoration phases; Mercury original's whereabouts; 2026 = 500th anniversary of the 1526 wedding (dated line).
- `v5/ONSITE_CHECKLIST.txt` (CRITICAL: O12 Muñecas → Crucero way, O18 Baths entrance, O28 last garden stretch to the exit;
  per-track DIRECTIONS tick list).

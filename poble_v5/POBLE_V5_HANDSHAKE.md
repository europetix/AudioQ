# Poble Espanyol (Barcelona, Montjuïc) V5 (Yo Tours) — handshake, STATE 1 (31 Oct 2026)

## What exists
- **User decisions (31 Oct, `USER_DECISIONS.md`):** start fresh (the user's old guide is "not so great", not used; no
  user map); lengths 45 / 75 / 120; EN/ES/FR/DE. Honest Full ≈ 1 h 30 ("nearer two hours with the art museum"): the
  sourced, placeable content runs out; do not pad. Held items that could lengthen it (with a source or on-site photo):
  two Fran Daurel Extras, the Guinovart Space Extra, the Maestrazgo R (`v5/PLAN.md` section 2 end, section 3 "Gap").
- **English:** `v5/tracks/001–025.perf.txt` — 21 main stops + 4 Extras (003 Sun and Moon, 010 FIESTA, 016 Sculpture
  Garden, 019 the flamenco house), ~7,700 words (~60 min listening). Sections: The gate / Calle Caballeros / The brick
  tower / Catalonia / The top of the hill / Andalusia / Back to the Plaza Mayor. Loop: Plaza Castellana → C. Caballeros →
  C. Príncipe de Viana → Pl. Aragonesa (Utebo tower) → Pl. de la Iglesia (church, Fran Daurel) → C. Davallada (house 83)
  → C. Mercaders (glass, 81) → Pl. de la Font → Barcelona Panorama (dictatorship track) → Sculpture Garden → Monastery of
  Sant Miquel → Andalusia (Pl. de la Hermandad, C. Arcos/Tablao) → Pl. del Carmen (war, prisoners, folk museum) → Gradas
  de Santiago (the North, thin and says so) → Plaza Mayor (Riaza, town hall/Valderrobres, the 1961 critics, close).
- **Research:** `research/FACTS_OCT2026.md` (~210 graded rows; §9 popular errors and official-page slips; §13
  corrections), `VISIT_ROUTE_AND_SPACES_OCT2026.md` (116 numbered buildings with originals), `OFFICIAL_AUDIO_COMPARISON_
  OCT2026.md`, `research/map/` (official Feb 2026 plan, read in the user's Chrome; OFFICIAL_PLAN_NOTES_31OCT2026.md),
  `AUDIT_V5_FACTS.md`, `AUDIT_V5_ROUTE_LISTENING.md`; fixes in `v5/notes/AUDIT_FIXES_001-025.md`; lead decisions at the
  end of `v5/PLAN.md`. Lead read every track.
- **Corrections worth remembering:** the Tudela clutch letter is the SECOND trip (15 Nov 1927), not "from Borja", car not
  named; the monastery is NOT Puig i Cadafalch (official-page slip); the 1929 opening was May 1929; the notebooks were in
  J. M. Reventós's desk (no "ninety years"); the war camp is the Poble's own claim, not in the published camp list;
  014 now "mainly through Catalonia and Aragon" (translator caught the Tudela tension).
- **Lengths:** `build/static/lengths.json` — Essential 21, Highlights 10; 8 hand bridges (`v5/bridges/`, `v5/i18n/<lang>/
  bridges.txt`; 7 used per language); Extras-only skips silent. Visit: Full ≈ 1 h 30, Essential ≈ 1 h 15, Highlights
  ≈ 45 min.
- **Translations:** `v5/i18n/{es,fr,de}/tracks/` 25 each, checks pass; one translator + one independent reviewer per
  language (`v5/i18n/review_31oct/`). ES uses the Poble's Spanish names "Monasterio de Sant Miquel", "Jardín Escultórico";
  FR/DE titles "Monestir de Sant Miquel" (DE speech "Kloster Sant Miquel"); FR rulers « Alphonse treize »,
  « Victoire-Eugénie ». Spanish-original quotes in ES verified at source; the rest translated or reported. "1600" in
  digits in 004 in all three (listen once).
- **Build:** `bash build/build_all.sh` → `bundle/PobleEspanyol_YoTours` + `/mnt/user-data/outputs/PobleEspanyol_
  YoTours_ALL_LANGUAGES.zip`. Route sheet `build/route_map.py` (5 pages, schematic, numbers from the tracks). Cover (gate
  drawing). Pronunciation +~70 names. Samples 008 + 012.
- **Tested (stand-in tones, not speech):** EN option 1 → 25/21/10 with 2+5 bridges; ES option 3 → 10 with 5 bridges;
  bridge check 28 hand lines across 4 languages, none missing. Real voices not heard. On-site markers stripped from
  visible header lines (kept in ONSITE_CHECKLIST.txt and PLAN.md).

## On-site (before recording) — `v5/ONSITE_CHECKLIST.txt`
CRITICAL: house numbers posted on the fronts (O2), Plaza Castellana and the gate (O1), the 102/103 junction (O4), the
squares by the tower (O5), house 83's stair, 7 steps (O6), the steps to the monastery (O8), viewpoint landmarks (O9), the
monastery (O11), Andalusia (O12), Gradas/Rincón (O14), Plaza Mayor + town hall photos (O15), a stopwatch walk per length
(O17). Also O10: if the Sculpture Garden is entered by house 89, move 016 after 012. Listening: "1600" in ES/FR/DE 004.

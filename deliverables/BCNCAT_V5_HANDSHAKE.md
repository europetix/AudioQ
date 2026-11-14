# Barcelona Cathedral (Catedral de la Santa Creu i Santa Eulàlia) V5 (Yo Tours) — handshake, STATE 1 (14 Nov 2026)

## What exists
- **User decisions (`USER_DECISIONS.md`):** everything on the cultural-visit ticket + the facade and square; lengths 30 /
  60 / 90; start fresh (no old guide, no plan from the user); EN/ES/FR/DE; ≈ 32–36 tracks for 90 min (the user's
  Park Güell expectation of many tracks). Context checked 14 Nov: the ticket includes a phone web audioguide (GVAM,
  2019, six languages) per ticket sellers; the official ticket page is JS-only.
- **English:** `v5/tracks/001–036.perf.txt` — 33 main + 3 Extras (008 the bishop under the crucifix, 017 under the
  canons' seats, 033 Jewish memory — conditional on O6), ≈ 9,800 words. Sections: The square and the facade · Inside
  the main door · Up the left aisle · The roof · The choir · The crypt · Behind the high altar · The cloister · The
  Chapter Hall · The way out. Plan: `v5/PLAN.md` (+ lead's decisions at the end); skeleton `v5/SKELETON.md`.
- **Route (Variant A, ALT-B/C/D held for O1):** the Pla de la Seu and facade → main door, lantern tower → Lepanto
  chapel from its doorway (Mass-proof) → choir screen → baptistery → up the left aisle to the Sant Iu door and organ →
  lift (queue tracks 012–013, work with no queue) → roof (014–015; unverified sights cuttable) → choir (016–020; closed
  fallback) → crypt (021–023; closed fallback) → ambulatory (024–025) → founders' coffins by the sacristy (026) →
  cloister door (027) → cloister (028–033) → Chapter Hall (034–035) → out by the Santa Eulàlia door (036). All
  left/right "as you face the high altar": lift left, cloister door right.
- **Research:** `research/FACTS_NOV2026.md` (348 rows), `FACTS_GAPS_NOV2026.md` (128 + corrections table),
  `VISIT_ROUTE_AND_SPACES_NOV2026.md`, `OFFICIAL_AUDIO_COMPARISON_NOV2026.md`. The official plan
  (`catedralbcn.org/wp-content/uploads/2021/11/planta-catedral-barcelona.jpg`; magazine PDF p. 39) is NOT read: the
  user's Chrome would not open catedralbcn.org (extension site permission?). Cues are landmark-only.
- **Audits:** `research/AUDIT_V5_FACTS.md` (2 MUST, 13 SHOULD, 21 NICE; 40 quotes checked) and
  `AUDIT_V5_ROUTE_LISTENING.md` (4 MUST, 22 SHOULD, 20 NICE); fixes in `v5/notes/AUDIT_FIXES.md`. Lead read every track.
- **Corrections worth remembering:** Eulàlia's tomb is marble (the alabaster is Sant Oleguer's effigy, 1406); the
  cathedral now says the Lepanto Christ is "not from the 16th century"; the cannonball story first written 1762;
  1448 = the cloister; facade 1887–1890 from Carlí's 1408 design, cimbori 1913 over the entrance; Gaudí only drew for
  Martorell's losing entry; relics found 877; the shields painted by Joan de Borgonya, paid by the order's treasurers;
  no Henry VIII / Francis I; "King Martin's throne" is a folding bishop's chair; the 1058 consecration was not by the
  count and countess; the Pietat door is late 1300s, Lochner's relief about a century later; Hebrew gravestones are
  outside the cathedral; the goose-girl tale is betevé's, not a canon's.
- **Lengths:** `build/static/lengths.json` — Essential 18, Highlights 9 (no roof); 15 hand bridges. Visit: Full about an
  hour and a half, a little more with a lift wait (≈ 94–97 min), Essential ≈ 1 h, Highlights ≈ 30 min.
- **Translations:** `v5/i18n/{es,fr,de}/tracks/` 36 each, checks pass; one translator + one independent reviewer per
  language (`v5/i18n/review_14nov/`; work files `v5/i18n/work/`; briefs `v5/i18n/briefs/`). ES uses the cathedral's
  Spanish names (Capilla del Santo Cristo de Lepanto, puerta de la Piedad) and "Eulalia"; 019's 1519 Spanish account
  verified and kept in the original. FR: salle du chapitre (old, 1407) vs salle capitulaire (museum). DE: Kapitelhaus
  vs Kapitelsaal; "Hanß".
- **Build:** `bash build/build_all.sh` → `bundle/BarcelonaCathedral_YoTours` + `/mnt/user-data/outputs/
  BarcelonaCathedral_YoTours_ALL_LANGUAGES.zip`. Route sheet `build/route_map.py` (5 pages, schematic, our own drawing;
  025 and 033 positions approximate). Pronunciation +147. Samples 018 + 030. Cover: arch, spires, goose.
- **Tested (stand-in tones, not speech):** EN option 1 → 36/18/9 with 8+7 bridges; DE option 3 → 9 with 7 bridges;
  bridge files ES/FR/DE complete (15 each, cues match titles). Real voices not heard. On-site notes stripped from
  visible header lines (kept in ONSITE_CHECKLIST.txt and PLAN.md).

## On-site (before recording) — `v5/ONSITE_CHECKLIST.txt`
CRITICAL: read the official plan (O5); doors and flow (O1); the transept-vault works, Oct–Dec 2026 (O2); the lift and
queue (O3); the Lepanto chapel from its door and Mass (O4); the choir (O8); the cloister layout (O9); the crypt (O10);
the founders' coffins (O16); the ambulatory and Penyafort's tomb (O17); a stopwatch walk (O22). Also: roof sights
(O7: the neighbours, the Sagrada Família on the horizon, the gargoyle beasts — each cuttable), where Jewish memory is
(O6), the Golden Fleece shields (O8: Louis II only if found), Bermejo's signature spelling on the panel (O21), the
Pont del Bisbe in view (O23).

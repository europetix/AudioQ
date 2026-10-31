# Guggenheim Museum Bilbao V5 (Yo Tours) — handshake, STATE 1 (31 Oct 2026)

## What exists
- **Scope (user, 30–31 Oct):** the building + permanent works only (no temporary exhibitions, not the floor-3 Collection
  display). Lengths: the user chose 45 / 90 / 150, then accepted that core-only Full lands ≈ 1 h 40. EN/ES/FR/DE.
  The user said the Setas guide had degraded: depth was the priority (research 165+ graded facts; lead read every track;
  two independent audits). The user sent the NY Guggenheim visitor guide by mistake (set aside: source/_new_york_not_used/).
- **English:** `v5/tracks/001–029.perf.txt` — 25 main stops + 4 Extras, ~8,640 words (~69 min listening).
  Route: plaza (001 welcome, 002 Puppy, 003 Txema Agirre, 004 the deal) → 005 stairway → 006 ZERO → 007 Atrium →
  008 Holzer (101) → 104: 009–013 Serra (014 X the Serra that vanished) → 015 terrace/Chillida → 016 balcony opposite 204 →
  017 lifts/walkways (every piece different) → 018 balcony opposite 304 (metal flower) → 019 Bilbao effect (020 X opening
  day) → 021 out to the river walk → 022 Kapoor → 023 fog (024 X fire) → 025 Maman → 026 titanium → 027 La Salve/Buren
  (028 X the ones who lost) → 029 close.
- **Research:** `research/FACTS_BUILDING_AND_PERMANENT_OCT2026.md` (+ corrections after the audit), `VISIT_ROUTE_AND_SPACES_
  OCT2026.md`, `OFFICIAL_AUDIO_COMPARISON_OCT2026.md`, `research/map/` (official interactive map read in the user's Chrome:
  key works, placements, official texts; OFFICIAL_MAP_NOTES_30OCT2026.md), `AUDIT_V5_FACTS.md` (3 MUST, 12 SHOULD, 20
  NICE), `AUDIT_V5_ROUTE_LISTENING.md` (6 MUST, 22 SHOULD, 20 NICE); fixes in `v5/notes/AUDIT_FIXES_001-029.md`; lead
  decisions at the end of `v5/PLAN.md`.
- **Corrections worth remembering:** Snake shared 104 with two Lichtensteins and a Warhol at the opening (Irish Times);
  Pérez's "costly" was about reaching the frame; "It isn't so" = a museum spokeswoman (Lucía Agirre, not named in speech);
  Carmen Giménez; Hal Foster's line in context; Serra's "It is narrative" dropped (museum's Spanish says "no es narrativo").
- **Lengths:** `build/static/lengths.json` — Essential 19, Highlights 9; 10 hand bridges (`v5/bridges/`, `v5/i18n/<lang>/
  bridges.txt`); Extras-only skips silent. Visit: Full ≈ 1 h 40, Essential ≈ 1 h 15, Highlights ≈ 45 min.
- **Translations:** `v5/i18n/{es,fr,de}/tracks/` 29 each, checks pass; one translator + one independent reviewer per
  language (`v5/i18n/review_31oct/`). Floors: ES segunda/tercera planta (museum's usage), FR niveau deux/trois, DE Ebene 2/3.
  Museum titles: ES La materia del tiempo, Serpiente…; FR La matière du temps, Grand arbre et l'œil…; DE English titles.
  ES quotes Serra's Spanish verbatim from the museum's teachers' guide; FR quotes the museum's French Klein text.
- **Build:** `bash build/build_all.sh` → `bundle/Guggenheim_YoTours` + `/mnt/user-data/outputs/Guggenheim_YoTours_ALL_
  LANGUAGES.zip`. Route sheet `build/route_map.py` (5 pages, schematic, numbers from the tracks). Cover (abstract metal
  curves). Pronunciation +40 names (Gehry, Txema Agirre, Ertzaintza, ETA, Bourgeois, Chillida…). Samples 009 + 025.
- **Tested (stand-in tones, not speech):** EN option 1 → 29/19/9 with 4+6 bridges; ES option 3 → 9 with 6 bridges.
  Real voices not heard. On-site markers stripped from visible header lines.

## On-site (before recording) — `v5/ONSITE_CHECKLIST.txt`
CRITICAL: the way out and down to the river walk (ALT-X), whether the terrace leads outside (ALT-T), which end of 104 the
Serra order starts (ALT-S), the balcony opposite 204 open (ALT-B), the plaque's spot (ALT-P), pond vs Maman order (ALT-M),
a stopwatch walk; listening: DE 015 Chillida titles.

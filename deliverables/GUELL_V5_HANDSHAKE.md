# Park Güell (Barcelona) V5 (Yo Tours) — handshake, STATE 1: edition 2 (7 Nov 2026)

## What exists
- **User decisions (`USER_DECISIONS.md`):** scope = the monumental core + the nearest viaducts + the Portico of the
  Washerwoman, the Gaudí House Museum outside only; start fresh (no old guide, no user map); EN/ES/FR/DE. On 7 Nov the
  user asked for ≈ 45 tracks / 120 min ("cover more stories and better quality audio, including views and only part of
  the tickets"): edition 2. The Casa del Guarda interior is in (normal ticket); the Gaudí House interior is not.
- **Edition 1** (25 tracks, 6 Nov) is held in `v5/held/ed1/` with its plan `v5/PLAN.md` and audits
  (`research/AUDIT_V5_FACTS.md`, `AUDIT_V5_ROUTE_LISTENING.md`).
- **English, edition 2:** `v5/tracks/001–045.perf.txt` — 39 main + 6 Extras (007–009 the Casa del Guarda floors, 013
  the carob bridge, 025 the Font Sarva, 035 words in the bench tiles), ≈ 11,500 words. Sections: The gate · Inside the
  Casa del Guarda · The viaducts · The Dragon Stairway · The Hypostyle Room · The Austria Gardens · The Nature Square ·
  The Portico · Casa Larrard · The way out. Plan: `v5/PLAN_V2.md` (+ lead's decisions at the end).
- **Route:** the official recommended order A–I (read in the user's Chrome on 7 Nov: `research/map/OFFICIAL_ROUTE_MAP_
  NOTES_7NOV2026.md` + images): everything outside the inner section first (gate, Casa del Guarda, the viaducts out and
  back by the Marianao steps-ramp), then the second ticket check at the foot of the stairway (queue tracks 014–015 with
  the one-way warning, played before the check queue or not) → stairway → hall front → inside → up the right to the
  Austria Gardens → the square → out by its left-hand corner, the path above Casa Larrard → Portico → ramp → back along
  the wall to the Carrer d'Olot gate (exit only). No re-entry; headphones only (the park bans speakers).
- **Research:** `research/FACTS_NOV2026.md` (249 rows), `FACTS_GAPS_NOV2026.md` (86), `FACTS_EXPANSION_NOV2026.md`
  (132 + corrections), `VISIT_ROUTE_AND_SPACES_NOV2026.md`, `OFFICIAL_AUDIO_COMPARISON_NOV2026.md`.
- **Audits of edition 2:** `research/AUDIT_V5_ED2_FACTS.md` (2 MUST, 8 SHOULD, 22 NICE; all 142 quotes checked) and
  `AUDIT_V5_ED2_ROUTE_LISTENING.md` (3 MUST, 21 SHOULD, 18 NICE); fixes in `v5/notes/AUDIT_FIXES_ED2.md`. Lead read
  every track of both editions.
- **Corrections worth remembering:** public park from 26 Apr 1926 (not 1922/1923); hilltop bought 9 Jul 1899 (not
  1895); bench "about a hundred metres", never "longest"; 86 columns; Gaudí didn't design his house (Berenguer; Gaudí
  signed) nor invent trencadís; the cross is a 1996 copy; the gates came from Casa Vicens; Gràcia joined Barcelona in
  1897; the 2023 Ar@cne author is **Manuel-Blas** García Ávila (not "María-Belén": caught by the ES reviewer, fixed in
  all languages); the "mushroom" roof is disputed between the two pavilions (no cue uses it); the 1903 caves quote is
  Bassegoda's paraphrase; the garden party was part of the Oct 1906 Catalan language congress.
- **Lengths:** `build/static/lengths.json` — Essential 21, Highlights 11; 21 hand bridges. Visit: Full "a little over
  two hours" (≈ 125–131 min), Essential ≈ 1 h 15, Highlights ≈ 45 min.
- **Translations:** `v5/i18n/{es,fr,de}/tracks/` 45 each, checks pass; one translator + one independent reviewer per
  language (`v5/i18n/review_7nov/`; work files `v5/i18n/work/`; briefs `v5/i18n/briefs/`). ES uses verified Spanish
  originals for nine quotes; 014's Güell quote is reported speech in ES. Version names: ES recorrido completo / versión
  esencial / imprescindibles; FR visite complète / version essentielle / incontournables; DE vollständige Tour /
  Kernversion / Highlights. ES/FR drop the "Laundry Room Portico" alternative name.
- **Build:** `bash build/build_all.sh` → `bundle/ParkGuell_YoTours` + `/mnt/user-data/outputs/ParkGuell_YoTours_ALL_
  LANGUAGES.zip`. Route sheet `build/route_map.py` (5 pages, schematic, our own drawing; viaduct and Font Sarva
  positions are estimates). Pronunciation ≈ 95 new names. Samples 018 + 034. Cover: abstract bench wave + tower.
- **Tested (stand-in tones, not speech):** EN option 1 → 45/21/11 with 13+8 bridges; FR option 3 → 11 with 8 bridges;
  bridge files ES/FR/DE complete (21 each, cues match titles). Real voices not heard. On-site notes stripped from
  visible header lines (kept in ONSITE_CHECKLIST.txt and PLAN_V2.md).

## On-site (before recording) — `v5/ONSITE_CHECKLIST.txt`
CRITICAL: the official drawing on the ground (O-map), the second check and one-way flow (O1), the iron door / Portico /
ramp (O3), the Marianao steps-ramp and the viaducts (O5), the other gates (O9; ALT-G2 for Carmel), the queue (O10),
Casa Larrard and the way out (O11), the Austria Gardens' middle (O12), the Casa del Guarda floors (O23), a stopwatch
walk (O18). Also: which pavilion has the mushroom cap (O2); the view landmarks (O7: sea, Olympic Village towers);
re-check before recording: the year the Suns were restored, whether the April 2026 dinner took place, the manifesto
date, Duch's study (Jujol's son's words stay reported).

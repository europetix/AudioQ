# FC Barcelona Museum at Spotify Camp Nou V5 (Yo Tours) — handshake, STATE 1 (14 Nov 2026)

## What exists
- **User decisions (`USER_DECISIONS.md`):** the Museum ticket only (the temporary museum "Barça Immersive Tour" in the
  old ice rink beside the Palau Blaugrana + the Espai Barça models + the Construction Viewpoint; no stadium interior);
  30 / 60 / 90; EN/ES/FR/DE; "good facts, fun stories and their legacy … like Santiago"; the 90-min extra = "More
  stories inside" (Extras that need no view until their last paragraph). The user's old guide (source/) was audited
  (`research/AUDIT_OLD_GUIDE_NOV2026.md`, 475 claims: ~50 wrong) and used as a topic list only.
- **English:** `v5/tracks/001–034.perf.txt` — 24 main + 10 Extras (004, 005 by the door; 017–020 in a quiet corner;
  030–033 on the old benches), ≈ 8,730 words. Sections: Outside the museum · The entrance hall · The trophies · The
  club's history · More stories inside · Messi's space · The round room · The models · The viewpoint · The way out.
  Plan `v5/PLAN.md` (+ lead's decisions at the end, three sections); skeleton `v5/SKELETON.md`.
- **Design:** honesty in 001 (no stadium on this ticket); topic-keyed bodies with a swappable route layer for the
  imminent new museum inside the stadium (O2); cues by displays, not rooms (O3 order); the 360° warning in 001 and 024;
  even-handed politics (1925, Sunyol, 1943 with Real Madrid's own wording and Barça's Franco medals withdrawn in 2019,
  "Més que un club"); no sums of money; no anthem lyrics; no 1 October 2017; no gate numbers spoken.
- **Research:** `research/FACTS_NOV2026.md` (276 rows + §18 errors), `FACTS_GAPS_NOV2026.md` (G1–G111 + changes
  table), `VISIT_ROUTE_AND_SPACES_NOV2026.md`, `OFFICIAL_AUDIO_COMPARISON_NOV2026.md`, `map/` (official access maps Oct
  2026 and the campus map Mar 2026, read in Chrome: the museum = the long ridged building at Av. de Joan XXIII /
  Arístides Maillol, Access 9 at it).
- **Audits:** `research/AUDIT_V5_FACTS.md` (2 MUST, 5 SHOULD, 16 NICE) and `AUDIT_V5_ROUTE_LISTENING.md` (2 MUST, 19
  SHOULD, 19 NICE); fixes in `v5/notes/AUDIT_FIXES.md`. Lead read every track.
- **Corrections worth remembering:** Walter Wild first president (Gamper declined to keep playing); the colours' origin
  unknown (club favours Merchant Taylors' School); "culers" story doubted; the stadium not built for Kubala; official
  name Estadi del FC Barcelona until 2000–01; the napkin was never in the museum (auctioned 2024); six Ballons d'Or won
  at Barça, eight shown; Lamine Yamal wears the 10; Wembley 1992: Koeman's goal, THEN Alexanko on to lift the cup; Xavi
  seventeen seasons played (not scored in); Spain's Olympic gold 1992 and again 2024; Luis Suárez the first
  Spanish-born winner (not "only Spaniard"); Cruyff's delay was the Dutch window; Kubala statue 2009; Alexia's 2026
  Ballon d'Or after leaving the club.
- **Lengths:** `build/static/lengths.json` — Essential 18, Highlights 6; 10 hand bridges (E 5, H 5). Visit: Full "a
  little over an hour and a half" (≈ 95.5 min + ≈ 4 min of pauses), Essential "about an hour" (≈ 62), Highlights
  "about thirty-five minutes" (≈ 34), the 360° show counted at ≈ 10 min (O11).
- **Translations:** `v5/i18n/{es,fr,de}/tracks/` 34 each + `bridges.txt`, checks pass; one translator + one independent
  reviewer per language, all "ready" (`v5/i18n/review/`; work `v5/i18n/work/`; briefs `v5/i18n/briefs/`). ES uses
  Real Madrid's own 1943 wording and the club's own Spanish Messi statement; "Salid y disfrutad" in Spanish in all
  languages; 011 title "91648" (ES, no separator).
- **Build:** `bash build/build_all.sh` → `bundle/SpotifyCampNou_YoTours` + `/mnt/user-data/outputs/SpotifyCampNou_
  YoTours_ALL_LANGUAGES.zip`. Route sheet (5 pages, schematic, our own drawing; room order "may change"; no gates).
  Pronunciation +187. Samples 013 + 029. Cover: abstract blue/claret stripes + stadium curve (no crest, no logos).
- **Tested (stand-in tones, not speech):** EN option 1 → 34/18/6 with 5+5 bridges; ES option 3 → Highlights 6 with 5
  bridges; bridge files ES/FR/DE complete (10 each, end on the destination titles). Real voices not heard. On-site
  markers stripped from visible header lines in all languages (kept in ONSITE_CHECKLIST.txt and PLAN.md).

## On-site (before recording) — `v5/ONSITE_CHECKLIST.txt`
CRITICAL: O2 — has the new museum inside the stadium opened? (then rewrite the route layer: 001, 003, 006, 024–029, 034
and the cues); O1 the gate and the museum door (Access 9 per the official maps; 001 may then name it once); O3 the room
order; O4 the viewpoint and the old benches; O5 the models; O7 the exit; O11 the 360° show length; O15 a quiet corner
for 017–020; O16–O19 the displays (the European Cups, the women's trophies, the shirts, Messi's space). Also: statues
(O9), the stopwatch walk (O21). Listen in each voice to: Barça, Camp Nou, Messi, Ronaldinho, "foot-vall", 91,648
(ES "91648", FR "91 648", DE "91.648"), U14/U19 (DE), Jean-Paul deux (FR).

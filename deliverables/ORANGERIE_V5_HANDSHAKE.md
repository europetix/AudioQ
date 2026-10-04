# MUSÉE DE L'ORANGERIE — V5 HANDSHAKE (state 1)
**Date:** 5 Oct 2026 · **User:** Puneet Sharma · **Status:** V5 English guide written, fact-checked, revised and built
(55 tracks, ~2 h 8 min, 15,943 words). Not yet rendered or heard. Next: render with Ava on the Mac, listening test vs V4, on-site check.
**Repo:** europetix/AudioQ, branch claude/tour43-pitti-v5-test-ddbz7z, folder `orangerie_v5/` (Pitti V5.1 is in `tour43_pitti_v5/`).
Restore: unzip the snapshot to /home/claude/orangerie (or symlink) → `bash build/build_all.sh` → must print OK.

## What happened (5 Oct)
1. **Inputs:** V4 full-tour PDF + shipped V4 EN/ES bundles (`source/`). V4 = 30 tracks, ~107 min, Brian -8%, one edge-tts call per
   track, no direction or mastering. EN scripts = PDF text (29/30 identical).
2. **Audit (findings/G1–G5):** ~60 HIGH errors in V4: Rousseau jungles / Matisse Three Sisters triptych (Barnes) / Derain bagpiper
   (Minneapolis) not at the Orangerie; L'Étreinte misdescribed; Morning on the wrong wall (it is Room 1 SOUTH, official); invented
   Monet quote; Pollock "visits"; wrong dates/ages (Domenica, Walter, Durand-Ruel, Modigliani burial, Soutine/Barnes); 146 not 148
   paintings; hours/exhibitions in speech; every track over length. G5: layout, 2025 north exit by footbridge, lower-level rooms by
   artist (order unverified), traveller complaints (robotic voice, thin Monet, broken app, outdated).
3. **User decision:** new guide, 50–60 tracks, ~2 h, every work verified, Pitti storytelling, match/beat the official guide.
4. **Research (research/FACTS_A/B/C):** per-work fact sheets with source grades. WebSearch quota (200) ran out; museum sites are
   egress-blocked (search snippets only). Gaps: Laurencin, Utrillo, Monet Argenteuil/Sisley/Gauguin, 3 Modiglianis → HELD.
5. **Plan (v5/PLAN.md):** 55 tracks — Arrival 2 · Water Lilies 12 · Collectors 4 · Renoir 6 · Cézanne 6 · Rousseau 5 · Matisse 4 ·
   Picasso 5 · Modigliani 1 · Soutine 4 · Derain 4 · Finale 1 · Closing 1.
6. **Writing:** 6 parallel writers (v5/WRITER_BRIEF.md: facts only from OFF/SEC2 lines; Pitti voice anchors).
7. **Verification (v5/verify/):** V1–V3 = 988 claims, 940 OK, 0 V4 errors, 2 CONTRA, 46 weak/unsourced → all fixed in the revision
   pass (REVISE_BRIEF.md, notes/REVISION_LOG.md). Traveller review (T_traveller_review.md): avg engagement 3.7 / clarity 3.8 before
   revision; fixes applied: "the museum says" 98 → 15, no spoken doubt, loan talk only on cards (one line in 040), one owner track per
   anecdote, varied closings, stronger 052/053 and closing.
8. **Build:** cloned Pitti V5 pipeline (build/, v5/pipeline). Bundle `Orangerie_V5_EN`: launcher (1 Ava default, 2 am_michael,
   3 Andrew, 4 Brian; full or 2 samples 005 + 046) → ~/Desktop/Orangerie_V5_EN_<voice>/; one-page pictorial route map
   `Orangerie_Audio_Guide_Route.pdf` (ground-floor ovals with each composition on its wall + lower-level artist rooms);
   USER_TEST (ONSITE_CHECKLIST, TEST_PLAN, make_listening_test: V4 Brian vs V5 Ava, feedback form). pronunciation.py starts empty
   (Ava reads French natively; ~140 candidate respellings in T_traveller_review.md for listen-QA). Tested with a stand-in TTS only.

## Honest status
- Verified: every spoken fact traces to an OFF/SEC2 line in the fact sheets (snippet-level; no live page read this session).
- Not verified: lower-level room order, which works are on the wall in 2026 (loans), some Water Lilies wall positions (Matin south,
  Room 2 north/south/east are sourced; others by size/inference — tracks describe by size), Ava's French names.
- Not covered yet: the HELD artists above; Water Lilies colour/detail descriptions (no official descriptions found).
- Official museum audio guide: not accessible to Claude; the comparison is the user's listening test.

## Next steps
1. Mac: render `printf '1\n1\n\n' | bash generate_audio.command` (Ava) and listen to 5 tracks; keep V4 (Brian) renders for Test 1.
2. Allow musee-orangerie.fr / musee-orsay.fr in the environment network → new session: read the official artwork pages, fill the
   HELD artists (Laurencin, Utrillo, Monet/Sisley/Gauguin, Modiglianis) and add official visual details to the Water Lilies tracks.
3. On site: ONSITE_CHECKLIST (room order, loans, exit), then fix and rebuild.
4. Then ES (Dalia) / FR (Vivienne) / DE (Katja) using the Pitti method (tour43_pitti_v5/v5/i18n/assemble.py + translation brief).

## Update: official plans added (May 2024 + Oct 2021)
- source/Plan_Guide_Mai_2024.pdf (+ map2024.txt) and source/Museum_Map.pdf (+ map.txt) added.
- Confirmed by both plans: all eight Water Lilies wall placements in 003–013 and the route map.
- The May 2024 plan shows the exit beside the entrance. The 2025 works notice describes a garden-side footbridge exit. The two disagree, so 053–055 no longer name a door. 055 now works anywhere outside with the Tuileries in view. The route-map badge now reads "Exit · Tuileries garden".
- 054: no start year voiced. The 2024 plan says 1916–1926, the artwork pages say 1914–1926.
- Lower-level cards now read "Level −2" (as signed). 014 says "marked minus two on the signs".
- 2024 plan: level −2 is one "Les Arts à Paris" collection area with a Focus room. There are no per-artist room labels, so no room numbers are voiced. 2021 numbering (Renoir 9, Cézanne 10, Laurencin+Matisse 11, Derain 12, Utrillo+Rousseau 13) is kept for the on-site check only.
- musee-orangerie.fr is still blocked from the cloud session (egress policy). Laurencin, Utrillo and the 3 extra Modiglianis stay held until the site is reachable or the pages are supplied as PDFs.
- Route map checked against both official plans: the exit/FINISH badge now sits beside the entrance (as on the May 2024 plan), and the small rotunda between the hall and Room 1 is marked. The ground floor matches the plan. The order on level −2 is not confirmed by either plan (see ONSITE_CHECKLIST).

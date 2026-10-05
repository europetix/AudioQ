# Orsay V5: handshake (5 Oct 2026)

**Status:** V5 English guide written, verified, revised and built: 66 tracks, 17,624 words, about 2 h 21 of audio (about 3 h 30 on
foot). Route level 0 → 5 → 2 → exit. Bundle outputs/Orsay_V5_EN.zip (launcher: Ava default, 64 kbps, launcher safeguards). Route at a
Glance PDF (three levels). Not yet rendered with a real voice or tested on site. ES/FR/DE not started.

## What was done
1. Source: the previous EN guide (31 tracks, 28k words), source/Orsay_EN_previous.pdf, split into source/v4_tracks/.
2. Audit (findings/A1, A2, A3, G): 62 HIGH errors in V4: Van Gogh, Gauguin, Post-Impressionists and Manet's Déjeuner on the wrong
   floor; MNR room moved to level 0 room 10b (opened 5 May 2026); invented or misquoted quotes; wrong ages and names; practical info;
   every track 600–1,200 words. Verdict: rewrite, not repair.
3. User decisions (5 Oct): route 0 → 5 → 2 → exit; Tokyo loans (Gleaners 008, Starry Night 044, Arearea 051; 14 Nov 2026 – 28 Mar 2027)
   kept, each with a spoken fallback to a nearby stand-in; Courbet's L'Origine du monde as an OPTIONAL track (012); plan approved.
4. Research (research/FACTS_R1–R5): official musee-orsay.fr text via WebSearch extracts (the site itself is blocked from the
   cloud session), vangoghletters.org for quotes. The search budget (200) ran out near the end.
5. Writing (6 writers), verification (3 fact-checkers: 1,106 claims, 1,052 OK at first pass, 0 V4 errors repeated) + traveller review,
   revision (3 revisers): all CONTRA/NOTFOUND/WEAK fixed or cut, "the museum says" 92 → 13, loan fallbacks rebuilt, repeats removed.
6. HELD (v5/held/ or never written; tell the user, add when verifiable): Gauguin Le Cheval blanc (only a single-source anecdote;
   held after writing, old 053–067 renumbered 052–066), Gauguin Oviri, Redon Les Yeux clos, Rousseau La Charmeuse de serpents (search
   budget ran out), Whistler's Mother (Amsterdam until 10 Jan 2027), Puvis Le Pauvre Pêcheur and Monet London Parliament (off
   display), Roty La Semeuse (not on display), photography (prints rotate).

## Open / to verify (build/static/USER_TEST/ONSITE_CHECKLIST.md)
- Manet's Déjeuner + Monet's Femmes au jardin (+ Bazille?): ground floor room 18 per official pages, vs level 5 room 29 per older sources.
- Lautrec: level 2 room 68 (official page) vs level 5 (older plans). Room numbers on level 5 for about 12 works. Talisman's room.
- The Opéra models during "Vertige. Richard Peduzzi à Orsay" (6 Oct 2026 – 17 Jan 2027). Les Muses (056): not on the Tokyo list?
- The official English guide map (spring 2026) would settle most of these: ask the user for it.
- Allow musee-orsay.fr in the environment's Network access, then research the held works directly and re-check room numbers.

## Next steps
1. User: render 2 samples (013 Olympia, 042 Van Gogh), then the full tour; walk the on-site checklist.
2. Fill held tracks when verifiable; fix rooms from the map or site visit; rebuild with build/build_all.sh.
3. ES/FR/DE: same method as Pitti/Orangerie (translate for listening, independent review per language, assemble.py checks).

## FROZEN STATE (5 Oct 2026, end of session, at the user's request)
The delivered bundle deliverables/Orsay_V5_EN.zip is the last COMPLETE build (66 tracks, before the 2026-plan changes). The working
tree has work IN PROGRESS on top of it. Do not ship the working tree until steps 1–4 below are done.
- Official plan-guide summer 2026 received: source/Planguide_Orsay_ete_2026.pdf; read-out in findings/M_planguide_ete_2026.md (OFF).
- Done: Bazille moved to level 0 room 18 as track 018 (old 018–026 → 019–027); level-2 files renamed for a first order.
- IN PROGRESS when frozen (an editing pass applying the plan; it may have stopped part-way, see v5/notes/PLAN2026_LOG.md):
  room numbers and closing cues for the new order. Requested level-2 order WEST → EAST (visitors arrive from the Café Campana at the
  west end): 054 Moreau Orphée (room 59) · 055 Claudel (55) · 056 Jardins publics (72) · 057 Le Ballon (71) · 058 Les Muses (70) ·
  059 Jane Avril (68) · 060 Cha-U-Kao/La Goulue (68) · 061 Balzac (Terrasse Rodin) · 062 Guimard/Majorelle (64) · 063 Gallé/Carabin
  (63, 65) · 064 Pompon · 065 Maillol/Bourdelle · 066 close. Check the files' @id/@title against this list first.
  Other plan fixes: Van Gogh = room 36 (Gachet 36); Pont-Aven 43; Tahiti 44; Talisman 45; Café Campana by rooms 38–39; clock salon 28;
  L'Angélus in room 5 or the Chauchard gallery (Galerie Seine 1); Lautrec level 2 room 68 (settled).
- APPROVED by the user, NOT yet started (research was launched and may not have finished; files would be research/FACTS_R6_*.md
  and FACTS_R7_*.md): 9 new tracks → about 75 tracks, about 2 h 40:
  level 0: Cézanne's beginnings (room 11), Degas (room 13), after the MNR room · level 5: Gauguin Le Cheval blanc and Oviri (room 44),
  Redon (room 45), Rousseau's Snake Charmer (room to find), Chat Noir (46), Cinema (47), before the Café Campana · level 2: Salle
  des fêtes (room 51) first on arrival. Search works again (budget reset).
- ALSO REQUESTED by the user: redesign the Route at a Glance: more schematic and presentable for customers, impactful and useful
  (draw the three levels as simplified floor plans with the real room numbers from the 2026 plan, the red route, track badges on
  their rooms, START/FINISH, escalator/lift icons). Not started.

## To resume (new session): steps
1. Finish/verify the plan-2026 pass (all cues in order 001→066; validator; lengths).
2. Research (R6/R7) → write the 9 tracks → verify → insert and renumber (make_bundle sections: rename the level-2 sections).
3. Redesign build/route_sheet.py as above; rebuild with build/build_all.sh; stand-in TTS test; update this handshake.
4. Refresh deliverables (zip, route PDF, scripts) and the snapshot; then ES/FR/DE if wanted.

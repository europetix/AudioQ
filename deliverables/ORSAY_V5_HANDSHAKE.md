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

## STATE 2 (5 Oct 2026, end of session): COMPLETE, 75 tracks
- 75 tracks, 20,312 words, about 2 h 42 of listening. Route level 0 → 5 → 2 → exit, rooms from the museum's summer 2026 plan-guide
  (source/Planguide_Orsay_ete_2026.pdf; findings/M_planguide_ete_2026.md). Renumbering history: v5/notes/RENUMBER_75.md (v5/PLAN.md
  keeps the earlier numbering; the tracks and the bundle's plan.json are authoritative).
- Added (user-approved): Cézanne room 11 (020), Degas Bellelli room 13 (021, Tokyo fallback), Gauguin Le Cheval blanc (054, the
  'too green' story as the museum's own account), Oviri (055), Rousseau La Charmeuse de serpents (056, back from loans July 2026,
  hedged), Redon (058), Chat Noir room 46 (059), Cinema room 47 (060), Salle des fêtes room 51 (062, first stop on level 2).
  Facts: research/FACTS_R6_additions.md, FACTS_R7_held_works.md.
- Applied from the plan: Bazille to room 18 (018); Van Gogh room 36; Pont-Aven 43; Tahiti / Galerie Cachin 44; Redon and Nabis 45;
  Café Campana by rooms 38–39; level 2 west → east (51, 59, 55, 72, 71, 70, 68, Terrasse Rodin, 64, 63/65, terraces, exit).
- Final pass (v5/notes/FINAL_PASS_LOG.md): 17 fact fixes in the new tracks, 8 cue fixes, all closings checked in order, loan
  fallbacks for 008, 021, 046, 053 work. Three quotes (Christopher Gray, "black Eve", Redon's "refined, savage") are reported speech
  until checked against the live museum pages.
- Route at a Glance redesigned: A3 schematic floor plans of levels 0/5/2 with the 2026 room numbers, track badges in their rooms,
  route line, escalator moves, START/FINISH, track index (build/route_sheet.py, plan-driven).
- Tested with a stand-in TTS only: full run 75 files in 11 section folders + route PDF. Real voice not heard; not tested on site.
- Still held: Whistler's Mother (Amsterdam until 10 Jan 2027); Puvis, Monet's London Parliament, Roty (off display); photography.
- Next: user renders samples (013 Olympia, 044 Van Gogh) then the full tour; on-site checklist; ES/FR/DE if wanted (same method as
  the Orangerie).

## STATE 3 (5 Oct 2026): ES / FR / DE done, 75 tracks each
- Method as for the Orangerie: brief + glossary (v5/i18n/review/BRIEF.md), 3 translators per language (001–025, 026–050,
  051–075), one independent reviewer per language (REVIEW_BRIEF.md), then v5/i18n/assemble.py checks. Translator notes and the
  three review logs are in v5/i18n/review/. Reviewers changed ES 31, FR 42, DE 60 tracks; each judged its language ready for a
  native-speaker spot check. Scripts for that check: deliverables/Orsay_V5_Scripts_ES.md / _FR.md / _DE.md.
- Words: ES 19,971 · FR 19,820 · DE 19,385 (EN 20,312), about 2 h 35–2 h 40 each.
- assemble.py (Orsay copy) also reads years written in words in the English ("eighteen sixty-five") and requires them as digits.
- Quotations: ES/DE translate the English quotes. FR uses the original French wording only where it was verified (museum pages,
  vangoghletters.org; 37 passages, URLs in the FR translator notes, all re-checked by the FR reviewer); the rest is reported speech
  (Champfleury 011, "point de départ de l'art moderne" 016, Monet's nightmare letter 039, Artaud 044, Fénéon, Jane Avril 068).
- Bundle: generate_audio_ES_FR_DE.command (1 ES Dalia, 2 FR Vivienne, 3 DE Katja; full or samples 013 + 044), copied by
  make_bundle.py; README has a languages section. Stand-in test: 75 files + route PDF for each of ES, FR, DE and EN; samples 2 each.
- FACT FIX in the English: 018 Bazille was killed at twenty-eight, not twenty-six (museum FR page for Un atelier aux Batignolles
  says "vingt-huit ans"; dates 1841–1870 from the museum's exhibition). Fixed in EN and all three languages; @sources updated.
- Open:
  - 048 @what calls the painting "Portrait du Docteur Gachet"; the FR translator found that title on the etching's copper plate
    page, while the painting (RF 1949 16) is "Le Docteur Paul Gachet". Header only, not spoken; settle before the image kit.
  - 055 Oviri: the museum's page said "not currently exhibited" on 5 Oct 2026 (added to ONSITE_CHECKLIST).
  - FR unconfirmed names: room 36 "Vincent van Gogh en France" (043), "Tout change, quoique pierre" (039).
  - Loan tracks say "this winter" in every language: right only for Nov 2026 – Mar 2027; revise after the loans return.
  - Native-speaker spot check for each language (ES reviewer suggests listening to 027, 030 and 051–075 first).

## STATE 4 (7 Oct 2026): audio polish, user-approved items 1–2 done, 3–5 on A/B trial
- (1) No more stuck renders: render_edge.py gives each voice request 60 s (EDGE_TIMEOUT), 3 tries, then skips the track and
  lists it at the end (exit 1); a re-run fills the gaps. Tested with a stand-in that hangs (retry works; skip + report works).
- (2) Phone labels: build/static/tag_tracks.py, run by both launchers after every render (also on a failed run, and on MP3s
  made earlier): title "NNN · <@title>", album "Musée d'Orsay Audio Guide · English" (Audioguía · Español, Audioguide ·
  Français / Deutsch), track n/75, artist + album artist "Yo Tours" (brand chosen by the user), genre, year, language, cover.
  Cover: build/static/cover.jpg, made by build/cover/make_cover.py (original clock-face artwork, no museum logo).
  Audio stream untouched (checked by md5); one cover stream per file.
- (3–5) On trial, OFF by default: VOICE_FINISH=1 (v5_direction.VOICE_FINISH_AF: highpass 80, +1.5 dB 200 Hz, +1.5 dB 3.2 kHz,
  de-esser, compressor 2.5:1, before loudnorm), ROOM_TONE=1 (pink noise ~ -64 dBFS under the whole track), CHIME=1 (synthesised
  E5→B5 bell, 1.4 s + 0.45 s gap before the voice). make_ab_test_013.command renders 013 Olympia four ways on the Mac into
  ~/Desktop/Orsay_V5_AB_Test_013/ (A current, B finish, C +room tone, D +chime). After the user picks, set the chosen
  switches as defaults (render_edge.py / v5_direction.py), rebuild, and tell the user to re-render (delete nothing: render
  into a new output folder or move the old one away, since finished tracks are skipped).
- Levels checked with stand-in tones only (loudness −16 LUFS kept; room tone −63.4 dBFS in pauses). Real voice not heard.
- Only Orsay changed. Pitti and Orangerie still have the old renderer (no timeout, no labels); port when the user asks.

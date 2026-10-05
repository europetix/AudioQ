MUSEE D'ORSAY - V5 AUDIO GUIDE (English)  (75 tracks, ~2 h 45)
Built 5 Oct 2026. Replaces the V4 walking script (31 tracks).

WHAT'S NEW IN V5
================
1. A new guide, not a repair. The audit of V4 found 62 serious errors: Van Gogh,
   Gauguin and Manet's Dejeuner on the wrong floor, invented quotes, wrong dates
   and names, practical information in the audio, tracks 2-3 times too long.
   V5 is written only from verified fact sheets (the museum's own pages first).
2. Route: level 0 -> level 5 -> level 2 -> exit, no backtracking.
   Level 0: academic art, Realism (Millet, Courbet), Manet and the 1860s, the
   MNR room, young Cezanne, Degas, Carpeaux's La Danse, the Opera models,
   the Paris rooms, Rodin's Gates of Hell.
   Level 5: the clock salon, the Impressionists, Van Gogh, Seurat and Signac,
   Pont-Aven, Gauguin (Arearea, The White Horse, Oviri), Rousseau's Snake
   Charmer, Redon and the Nabis, the Chat Noir, early cinema, Cafe Campana.
   Level 2: the hotel ballroom (Salle des fetes), Symbolism, Claudel, the Nabis,
   Toulouse-Lautrec, Rodin's Balzac, Art Nouveau, the sculpture terraces.
   Room numbers follow the museum's summer 2026 plan.
3. Narration: story-first scripts with a direction layer (pauses, pace, warmth),
   performed by the chosen voice, Ava, at 64 kbps.

WORKS THAT MAY BE AWAY
======================
Millet's Gleaners (008), Van Gogh's Starry Night over the Rhone (046) and
Gauguin's Arearea (053) are lent to Tokyo, 14 Nov 2026 - 28 Mar 2027; Degas's
Bellelli Family (021) may be too. Each of these tracks tells the listener where
to go if the wall is empty.
Track 012 (Courbet, L'Origine du monde) is optional and says so.

WHAT YOU GET
============
One folder per section (00_Welcome ... 10_Closing), tracks numbered in walking order,
plus Orsay_Audio_Guide_Route.pdf: a one-page picture of the route.

HOW TO RUN (macOS)
==================
  1. Open Terminal. Type  bash  and a space, drag "generate_audio.command" in, Return.
  2. Choose a voice: 1) Ava. Then 1) full tour or 2) two samples (013 + 044).
  3. The tour appears in  ~/Desktop/Orsay_V5_EN_Ava/
If a render stops, run it again: finished tracks are skipped.

START CLEAN
===========
Unzip this guide into an empty place, never on top of an older copy. The launcher
stops with a message if it finds old files mixed in, or if a second copy is
already running.

REQUIREMENTS
============
- ffmpeg (pauses + loudness):  brew install ffmpeg
- Python 3.9+ (edge-tts installs itself on first run); internet while rendering.

NOT YET IN THIS EDITION
=======================
Whistler's Mother (on loan to Amsterdam until Jan 2027). Several room numbers
are to be confirmed on site (USER_TEST/ONSITE_CHECKLIST.md).

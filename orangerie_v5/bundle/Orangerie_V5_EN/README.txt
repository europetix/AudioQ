MUSEE DE L'ORANGERIE - V5 AUDIO GUIDE (English)  (55 tracks, ~2 h)
Built 5 Oct 2026. Replaces the V4 guide (30 tracks, Brian voice, May 2026).

WHAT'S NEW IN V5
================
1. A new guide, not a repair. The V4 audit found ~60 serious errors (works that
   are not in the museum, wrong walls in the Water Lilies rooms, invented quotes,
   hours and exhibitions in the audio). V5 was written from verified fact sheets:
   every fact traces to an official museum source or two independent sources.
2. Coverage. All eight Water Lilies compositions on their own, Monet's story,
   the collectors Paul Guillaume and Domenica Walter, and the Walter-Guillaume
   collection work by work: Renoir, Cezanne, Henri Rousseau, Matisse, Picasso,
   Modigliani, Soutine, Derain. Then a second look at the lilies and the exit.
3. Narration. Story-first scripts with a direction layer (pauses, pace, warmth),
   performed by the chosen voice, Ava, and levelled to the same loudness.

WHAT YOU GET
============
One folder per section (00_Arrival ... 12_Closing), tracks numbered in walking order,
plus Orangerie_Audio_Guide_Route.pdf: a one-page picture of the route with the
track numbers at every room and wall. Share it with the MP3s.

HOW TO RUN (macOS)
==================
  1. Open Terminal. Type  bash  and a space, drag "generate_audio.command" in, Return.
  2. Choose a voice: 1) Ava (the chosen voice). Then 1) full tour or 2) two samples.
  3. The tour appears in  ~/Desktop/Orangerie_V5_EN_Ava/
     (a different folder from the V4 guide, so nothing is overwritten).
If a render stops, run it again: finished tracks are skipped.

REQUIREMENTS
============
- ffmpeg (pauses + loudness):  brew install ffmpeg
- Python 3.9+ (edge-tts installs itself on first run); internet while rendering.

NOT YET IN THIS EDITION
=======================
Monet's Argenteuil, Sisley, Gauguin, Marie Laurencin, Maurice Utrillo and three
Modigliani portraits are held until they can be verified. Rooms downstairs are
arranged by artist; their order is to be confirmed on site (USER_TEST/).

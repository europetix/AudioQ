YO TOURS - MUSEE DE L'ORANGERIE AUDIO GUIDE  (55 tracks, ~2 h)
English, Spanish, French, German. Edition of 17 Oct 2026 (scripts of 5 Oct 2026).
Replaces the V4 guide (30 tracks, Brian voice, May 2026).

WHAT'S NEW ON 17 OCT 2026
=========================
- The Yo Tours sound, as in the Pitti and Orsay guides: voice finishing, a barely audible
  room tone under the voice, and a soft two-note chime before each track.
- MP3s are labelled for phones: title, album ("Musee de l'Orangerie Audio Guide" + language),
  track n/55, artist Yo Tours, and a Yo Tours cover picture.
- Renders no longer hang: a voice request that gets no answer is retried automatically, and a
  track that still fails is skipped and filled in when you run the command again.
- New output folders (Orangerie_YoTours_...), so earlier renders are never mixed in.
- The scripts, facts and route are unchanged.

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

(The sections below describe the V5 rewrite of 5 Oct 2026.)

WHAT YOU GET
============
One folder per section (00_Arrival ... 12_Closing), tracks numbered in walking order,
plus Orangerie_Audio_Guide_Route.pdf: a one-page picture of the route with the
track numbers at every room and wall. Share it with the MP3s.

HOW TO RUN (macOS)
==================
  1. Open Terminal. Type  bash  and a space, drag "generate_audio.command" in, Return.
  2. Choose a voice: 1) Ava (the chosen voice). Then 1) full tour or 2) two samples.
  3. The tour appears in  ~/Desktop/Orangerie_YoTours_EN_Ava/
     (a new folder, so older renders are never overwritten or mixed in).
If a render stops, run it again: finished tracks are skipped.

SPANISH, FRENCH, GERMAN
=======================
  bash generate_audio_ES_FR_DE.command  ->  1) Espanol (Dalia)  2) Francais (Vivienne)
  3) Deutsch (Katja). Then 1) full guide or 2) two samples (005 + 046).
  Output: ~/Desktop/Orangerie_YoTours_<ES|FR|DE>_<voice>/, same folders and numbers as English.

START CLEAN
===========
Unzip this guide into an empty place, never on top of an older copy, and move old
output folders off the Desktop first. The launcher now stops with a message if it
finds old scripts or old MP3s mixed in.

REQUIREMENTS
============
- ffmpeg (pauses + loudness):  brew install ffmpeg
- Python 3.9+ (edge-tts installs itself on first run); internet while rendering.

NOT YET IN THIS EDITION
=======================
Monet's Argenteuil, Sisley, Gauguin, Marie Laurencin, Maurice Utrillo and three
Modigliani portraits are held until they can be verified. Rooms downstairs are
arranged by artist; their order is to be confirmed on site (USER_TEST/).

V5.1 - TOUR #43
Palazzo Pitti + Boboli Gardens - Yo Tours edition of 7 Oct 2026 (61 tracks, ~2 h 20)
English, Spanish, French, German
Built 5 Oct 2026 for user testing. The released guide (90 tracks, June 2026) is unchanged.

WHAT'S NEW IN V5
================
1. Walking order. Tracks now follow the museum's own one-way route through the
   Palatine Gallery (Rooms 1 -> 28, out through the Sala delle Nicchie), then the
   second floor, the Royal Apartments on the way back down, the ground floor and Boboli in the order
   you actually walk it. Every track ends by naming the next place to go.
2. Accuracy. Placements and facts were checked against uffizi.it and
   independent sources (4-5 Oct 2026). V5.1 cuts 18 tracks whose room or content
   could not be confirmed (Volterrano Wing, closed for restoration; several room
   introductions; works probably moved or of unconfirmed location). Galileo removed (his portrait is at the
   Uffizi). Added: Raphael's Doni portraits (Saturn), Titian's La Bella (Venus),
   Ussi's Expulsion of the Duke of Athens (Modern Art, Room 3).
3. Narration. Scripts were rewritten as stories (hook, story, turn, look, payoff)
   in short spoken sentences. Each track has a direction file (perf/) that
   the renderer performs: pace and volume change by passage, real pauses before
   reveals, and every track is levelled to the same loudness.

WHAT'S NEW ON 7 OCT 2026
========================
- Palatine Gallery rebuilt around the room names written above the doors (Sala di Saturno,
  Sala di Giove ...). Every Palatine track title starts with its room's name, and every
  track ends by naming the next door sign. Lost? Look up at the door and play the tracks
  with that name.
- Every painting's room was checked on the museum's own artwork pages (uffizi.it, 7 Oct
  2026) or the Ministry of Culture catalogue. Fixed: Raphael's La Gravida is now in the
  Sala di Prometeo (track 006, with a fallback to the Sala dell'Iliade); Leo X, no longer
  at Pitti, is replaced by Raphael's Ezekiel's Vision in the Sala di Saturno (017).
- The Yo Tours sound: voice finishing, a soft room tone and a short chime before each track.
- MP3s are labelled for phones (title, album, track n/61, Yo Tours, cover picture).
- Renders no longer hang: a voice request that gets no answer is retried automatically.
- New output folders (Pitti_YoTours_...), so earlier renders are never mixed in.

WHAT YOU GET
============
After you run the launcher, the tour is organised into one folder per section:
  00_Welcome/                              1 track
  01_Palatine_Gallery/                    31 tracks
  02_Gallery_of_Modern_Art/                8 tracks
  03_Museum_of_Fashion_and_Costume/        3 tracks
  04_Imperial_and_Royal_Apartments/        2 tracks  (separate ticket; on the way back down,
                                                      before + after the guided visit)
  05_Russian_Icons_and_Palatine_Chapel/    3 tracks
  06_Boboli_Gardens/                      12 tracks
  07_Closing/                              1 track
plus Palazzo_Pitti_Audio_Guide_Route.pdf (one-page picture of the route:
palace floors + garden, the path in red, track numbers at every room and stop;
share it with the MP3s) and
USER_TEST/ (test plan, feedback form, on-site checklist).

Track files are named  <play-order>_<room>_<title>.mp3
  e.g.  016_Sala-di-Saturno_Raphael_Madonna_della_Seggiola.mp3
        053_Stop-5_The_Amphitheatre.mp3
The old section maps are not included: their numbering belongs to the June guide.
The route PDF replaces them.

HOW TO RUN (macOS)
==================
macOS blocks double-clicking files downloaded from the internet ("could not
verify..."). The reliable way:
  1. Open Terminal (Applications > Utilities > Terminal).
  2. Type  bash   and a space, drag "generate_audio.command" into the window,
     and press Return.
     (Or: System Settings > Privacy & Security > "Open Anyway" after the first
      blocked double-click.)
3. Choose a voice:
     1) Ava        - Microsoft edge-tts, the chosen voice. Needs internet while rendering.
     2) am_michael - Kokoro. First run sets itself up via "uv" (~2GB).
     3) Andrew     - Microsoft edge-tts, en-US-AndrewMultilingualNeural (trial).
     4) Brian      - Microsoft edge-tts, en-US-BrianMultilingualNeural (earlier test voice).
   Then choose what to render: 1) the full tour, or 2) two voice samples only
   (016 Madonna della Seggiola + 053 The Amphitheatre), saved in
   ~/Desktop/Pitti_YoTours_Voice_Samples/Sample_<voice>/ for a quick comparison.
4. The tour appears in  ~/Desktop/Pitti_YoTours_EN_<voice>/
   (a different folder from the June guide and from any V5.0 test render,
   so nothing is mixed or overwritten).
Run it twice (1, then 2) if you want both voices for the test.
If a render stops (network, sleep), just run it again: finished tracks are skipped.

START CLEAN: unzip this guide into an empty place, never on top of an older copy, and
move old output folders off the Desktop first. The launcher stops with a message if it
finds old scripts or old MP3s mixed in (this caused a 233 MB English folder on 5 Oct).

SPANISH, FRENCH AND GERMAN GUIDES
=================================
Run  generate_audio_ES_FR_DE.command  the same way (bash + drag), then choose:
  1) Espanol - Dalia   2) Francais - Vivienne   3) Deutsch - Katja
and 1) the full guide (61 tracks) or 2) two samples. The guide appears in
~/Desktop/Pitti_YoTours_<ES|FR|DE>_<voice>/, same folders and numbers as the
English, so the same route map works. Scripts are in languages/<es|fr|de>/.
Translations adapted for listening, formal address; please have a native speaker
check them before release.

VOICE SAMPLES IN SPANISH, FRENCH AND GERMAN (female voices)
===========================================================
Run  voice_samples_ES_FR_DE.command  the same way (bash + drag). It renders the
two sample tracks (016 Madonna della Seggiola, 053 The Amphitheatre), translated
with formal address, in six voices:
  Spanish: Ximena (Spain), Dalia (Latin America)   French: Vivienne, Denise
  German: Seraphina, Katja.  Spanish only:  bash voice_samples_ES_FR_DE.command es
into ~/Desktop/Palazzo_Pitti_V5_1_Voice_Samples/<LANG>_<Voice>/. A voice the free
service doesn't offer is skipped and listed at the end. Needs ffmpeg + internet.

REQUIREMENTS
============
- ffmpeg (needed for the pauses and loudness levelling):  brew install ffmpeg
- Ava / Andrew / Brian: Python 3.9+ (edge-tts installs itself on first run).
- am_michael: internet on first run; "uv" installs itself and manages Python 3.11.

SETTINGS (for whoever maintains the pipeline)
=============================================
- render_kokoro.py: VOICE am_michael, SPEED 0.85, 64k MP3.  render_edge.py: Ava by default (EDGE_VOICE), base rate -8%.
- v5_direction.py: how each direction tag is performed (pace / volume / pitch, pause
  lengths, 2 s tail, -16 LUFS mastering). Shared by both voices.
- pronunciation.py: phonetic respellings for Italian names.
  Set APPLY_RESPELLING = False in the renderers to hear native pronunciation.
- scripts/ = exactly the words spoken; perf/ = the same words plus direction.
  Stripping the tags from a perf file must give the script exactly (checked at build).

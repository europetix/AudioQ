V5 TEST BUILD - TOUR #43
Palazzo Pitti + Boboli Gardens - English Edition  (79 tracks, ~177 min)
Built 4 Oct 2026 for user testing. The released guide (90 tracks, June 2026) is unchanged.

WHAT'S NEW IN V5
================
1. Walking order. Tracks now follow the museum's own one-way route through the
   Palatine Gallery (Rooms 1 -> 28, out through the Sala delle Nicchie), then the
   Royal Apartments, the second floor, the ground floor and Boboli in the order
   you actually walk it. Every track ends by naming the next place to go.
2. Accuracy. Every placement and fact was re-checked against uffizi.it and
   independent sources (October 2026). Galileo removed (his portrait is at the
   Uffizi). Added: Raphael's Doni portraits (Saturn), Titian's La Bella (Venus),
   Ussi's Expulsion of the Duke of Athens (Modern Art, Room 3).
3. Narration. Scripts were rewritten as stories (hook, story, turn, look, payoff)
   in short spoken sentences. Each track has a direction file (perf/) that
   the renderer performs: pace and volume change by passage, real pauses before
   reveals, and every track is levelled to the same loudness.

WHAT YOU GET
============
After you run the launcher, the tour is organised into one folder per section:
  00_Welcome/                              1 track
  01_Palatine_Gallery/                    45 tracks
  02_Imperial_and_Royal_Apartments/        2 tracks  (before + after the guided visit)
  03_Gallery_of_Modern_Art/               11 tracks
  04_Museum_of_Fashion_and_Costume/        3 tracks
  05_Russian_Icons_and_Palatine_Chapel/    3 tracks
  06_Boboli_Gardens/                      13 tracks
  07_Closing/                              1 track
plus Palazzo_Pitti_V5_Route_Sheet.pdf (where to stand for every track) and
USER_TEST/ (test plan, feedback form, on-site checklist).

Track files are named  <play-order>_<room>_<title>.mp3
  e.g.  027_Room-24_Raphael_Madonna_della_Seggiola.mp3
        070_Stop-5_The_Amphitheatre.mp3
The old section maps are not included: their numbering belongs to the June guide.
The Route Sheet replaces them for the test.

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
     1) Brian      - Microsoft edge-tts. Needs internet while rendering.
     2) am_michael - Kokoro. First run sets itself up via "uv" (~2GB).
4. The tour appears in  ~/Desktop/Palazzo_Pitti_V5_Test_EN_<voice>/
   (a different folder from the June guide, so nothing is overwritten).
Run it twice (1, then 2) if you want both voices for the test.
If a render stops (network, sleep), just run it again: finished tracks are skipped.

REQUIREMENTS
============
- ffmpeg (needed for the pauses and loudness levelling):  brew install ffmpeg
- Brian: Python 3.9+ (edge-tts installs itself on first run).
- am_michael: internet on first run; "uv" installs itself and manages Python 3.11.

SETTINGS (for whoever maintains the pipeline)
=============================================
- render_kokoro.py: VOICE am_michael, SPEED 0.85, 96k MP3.  render_edge.py: Brian, base rate -8%.
- v5_direction.py: how each direction tag is performed (pace / volume / pitch, pause
  lengths, 2 s tail, -16 LUFS mastering). Shared by both voices.
- pronunciation.py: phonetic respellings for Italian names (75 entries).
  Set APPLY_RESPELLING = False in the renderers to hear native pronunciation.
- scripts/ = exactly the words spoken; perf/ = the same words plus direction.
  Stripping the tags from a perf file must give the script exactly (checked at build).

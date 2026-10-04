V4.5 HUMANIZED AUDIO GUIDE - TOUR #43
Palazzo Pitti - English Edition

WHAT YOU GET
============
After you run the launcher, your tour is organised into one folder per
museum section. Each section folder holds, together:
  - that section's audio tracks (MP3), in play order
  - the section MAP (.html - opens in any browser, full poster layout)
  - a flat MAP IMAGE (.jpg - view or print without a browser)

SECTIONS
========
  00_Welcome/   1 track(s)
  01_Palatine_Gallery/   45 track(s)  + map + image
  02_Gallery_of_Modern_Art/   10 track(s)  + map + image
  03_Museum_of_Costume_and_Fashion/   13 track(s)  + map + image
  04_Imperial_and_Royal_Apartments/   6 track(s)  + map + image
  05_Russian_Icons_and_Palatine_Chapel/   3 track(s)  + map + image
  06_Boboli_Gardens/   13 track(s)  + map + image
  07_Closing/   1 track(s)

Track files are named:  <play-order>_<room>_<title>.mp3
  e.g.  018_Room-24_Sala_di_Saturno.mp3   (play order 18, official Room 24)
        030_Room-21_Sleeping_Cupid.mp3
        077_Stop-1_Boboli_Gardens.mp3
The number is the listening order; the room/stop label matches the section map
and the museum's own signs. Welcome and Closing tracks carry no room label.

HOW TO USE (macOS)
==================
1. Double-click "generate_audio.command".  (If blocked: right-click -> Open -> Open.)
2. Choose a voice when prompted:
     1) Brian      - Microsoft edge-tts. Fast, nothing extra to install.
     2) am_michael - Kokoro (warmer, open-source). On first run it sets up
                     automatically via "uv" (its own Python 3.11 + model, ~2GB)
                     - you do NOT install Python yourself.
3. Your tour appears in:  ~/Desktop/Palazzo_Pitti_Audio_EN_<voice>/
4. Open a section folder, glance at the map, and play its MP3s in number order.

VOICES
======
- Brian:      en-US-BrianMultilingualNeural at rate -8%. Re-encoded MP3 with a 5s silent tail.
- am_michael: Kokoro am_michael at speed 0.85, 40k MP3, 5s silent tail.
Both apply phonetic respellings for Italian names (toggle APPLY_RESPELLING in
render_kokoro.py for native Kokoro pronunciation). Navigation is by spoken cues.

REQUIREMENTS
============
- ffmpeg (both voices):  macOS: brew install ffmpeg | Linux: sudo apt install ffmpeg
- Brian:  Python 3.9+ (edge-tts auto-installs on first run).
- am_michael:  internet on first run; "uv" auto-installs and manages Python 3.11.

92 tracks, ~201 minutes. Built with the V4.5 pipeline.

MUSÉE DE L'ORANGERIE — V4 HUMANIZED AUDIO TOUR (English)
=========================================================

What's in this bundle
---------------------
  Orangerie_V4_Full_Tour.pdf
    The companion PDF — cover, table of contents, Stop & Look navigation
    box for every track, and the full word-for-word script.

  GENERATE_AUDIO_EN.command
    Double-click this to generate 30 MP3 tracks on your Mac Desktop.
    The first run will install edge-tts (Microsoft's free TTS engine).
    Re-running is safe — already-generated files are skipped.

  scripts/
    The 30 ASCII-safe script files that drive the audio generation.
    Each file is a single track of word-for-word narration.

  plan.json
    Manifest of all 30 tracks with titles, register, minutes, and
    word counts. Not required to use the bundle; useful for reference.


How to use it
-------------
  1. Open this folder in Finder.
  2. Double-click GENERATE_AUDIO_EN.command
     (If macOS warns about an unidentified developer:
      right-click → Open → Open. You only have to do this once.)
  3. Wait while edge-tts installs (first run only — about 30 seconds)
     and renders 30 MP3 files. Total time: usually 10–20 minutes,
     depending on your internet connection.
  4. The MP3s land in ~/Desktop/Orangerie_Audio_EN/
  5. The script will offer to open that folder for you.


Voice settings
--------------
  Voice: en-US-BrianMultilingualNeural (Microsoft Azure TTS)
  Rate:  -8% (slightly slowed for warmth and clarity)
  Total: about 1 hour 40 minutes of audio across 30 tracks.


Requirements
------------
  - macOS 10.15 or newer
  - Python 3.9+ (preinstalled on macOS 12+)
  - An internet connection (edge-tts queries Microsoft's API)


Troubleshooting
---------------
  "command not found: edge-tts"
    This bundle's launcher avoids that by calling
    `python -m edge_tts` directly. If you see it anyway, run:
        python3 -m pip install --user --upgrade edge-tts
    in Terminal, then re-run the launcher.

  "permission denied"
    Open Terminal, cd into this folder, and run:
        chmod +x GENERATE_AUDIO_EN.command
    Then double-click the launcher again.

  A track fails to generate
    The launcher skips already-generated MP3s. Just run it again
    and it will pick up where it left off.


About this tour
---------------
  Thirty tracks. Roughly one hour and forty minutes. Designed to walk
  alongside you through the Musée de l'Orangerie:

    Part I    — Arrival & the building (3 tracks)
    Part II   — The Water Lilies, first pass (8 tracks)
    Part III  — Monet, the man behind the gift (1 track)
    Part IV   — The Walter-Guillaume Collection (13 tracks)
    Part V    — Return to the Water Lilies (3 tracks)
    Part VI   — Closing (2 tracks)

  Walk in order, take your time, and don't skip the return visit
  to the Water Lilies.


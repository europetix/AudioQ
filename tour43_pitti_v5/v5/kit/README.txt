PITTI V5 VOICE BAKE-OFF — pilot for the new narration standard (4 Oct 2026)
==========================================================================

WHAT THIS IS
Three Pitti tracks rewritten as told stories (see scripts_clean/ to read them), with a performance
"direction layer" (perf/). You render them in 2-3 ElevenLabs narrator voices x 2 models and pick the
series voice by BLIND listening:
  - eleven_v3              + direction (pauses, delivery colour, stressed words)  -> most expressive
  - eleven_multilingual_v2 + pauses only                                         -> steadier
Tracks:  016 Throne Room (room intro) · 017 Raphael's Veiled Lady (masterpiece) · 083 Boboli Amphitheatre
Facts in all three were re-verified against uffizi.it today (several corrections vs the current audio).

STEP 1 — Pick 2-3 candidate voices (10 min)
  elevenlabs.io > Voices > Voice Library. Filter for narration / storytelling / educational.
  Look for: warm, mature, unhurried, NOT announcer-like. Add 2-3 to "My Voices".
  (Tip: include one American and one British accent if you're unsure which your guests prefer.)

STEP 2 — Get your API key
  elevenlabs.io > Developers > API Keys > create one (text-to-speech + voices read access).

STEP 3 — Run in Terminal (not by double-clicking; macOS doesn't block it this way)
  cd ~/Downloads/Pitti_V5_Voice_Bakeoff
  export ELEVENLABS_API_KEY=sk_your_key_here
  python3 render_v5_elevenlabs.py --list-voices                      # copy the IDs you added
  python3 render_v5_elevenlabs.py --bakeoff --voices ID1,ID2,ID3 --dry-run   # shows the credit cost
  python3 render_v5_elevenlabs.py --bakeoff --voices ID1,ID2,ID3            # renders
  Cost: ~29,000 credits for 3 voices, ~19,000 for 2. Needs only Python 3 (already on your Mac).

STEP 4 — Listen blind (20-30 min)
  Open bakeoff/. Files are named A01_016.mp3, A02_016.mp3 ... — the same code is the same
  voice+model on every track. Listen on PHONE EARBUDS (that's how guests hear it), ideally
  standing up and walking, not at a desk.
  Fill in bakeoff/SCORING_SHEET.csv (1-5 each): naturalness, pacing, pronunciation, engagement,
  and the real test — "sounds like a real storyteller?" Y/N.
  Only then open bakeoff/_answer_key.csv to see which voice/model each code was.
  Optional before/after: compare with your current am_michael files on the Desktop
  (Palazzo_Pitti_Audio_EN_am_michael: 015 Throne Room, 016 La Velata, 081 Stop-5 Amphitheatre —
  older text, so compare the FEEL, not the words).

STEP 5 — Send back
  The filled SCORING_SHEET.csv (or just "A03 wins, and the Velata felt too slow"), plus any word
  or name that sounded wrong. That locks the series voice; then the full tour is rendered the same way.

FILES
  perf/NNN.perf.txt        script + direction (tags are stripped for the printed guide)
  scripts_clean/NNN.txt    the exact words a listener hears (for reading along)
  render_v5_elevenlabs.py  renderer (cloned from the pipeline's render_elevenlabs.py + direction layer)
  v5_direction.py          direction-layer parser/translator (shared with the full-tour render)
  V5_AUDIO_STANDARD.md     the new standard: writing, direction, voice, mastering, QA gates

Note: Claude cannot hear audio. Your ears are the quality gate — that's by design (V5 gate 7).

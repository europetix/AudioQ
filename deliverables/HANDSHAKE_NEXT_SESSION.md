# AudioQ: handshake for the next session (written 5 Oct 2026; updated 5 Oct, second session: Orsay ES/FR/DE done)

Paste this into the new session to start:

> Read `HANDSHAKE_NEXT_SESSION.md` at the root of the AudioQ repo (branch `claude/tour43-pitti-v5-test-ddbz7z`) and run its
> "Session setup" commands. Then continue from "What to do next". Follow the "Rules" section exactly.

---

## 1. Where everything is

- **Repo:** `europetix/AudioQ`. **Branch:** `claude/tour43-pitti-v5-test-ddbz7z`. Everything is committed and pushed. Last commit:
  "Orsay V5 complete: 75 tracks…".
- **Clone path in the cloud session:** `/home/user/AudioQ`. If the repo is not there, attach it (add_repo), clone the branch to
  `/home/claude/audioq` and link it: `mkdir -p /home/user && ln -sfn /home/claude/audioq /home/user/AudioQ` (done this way on 5 Oct).

| Folder | What it is |
|---|---|
| `tour43_pitti_v5/` | Palazzo Pitti + Boboli, V5.1: 61 tracks, EN + ES/FR/DE. Handshake: `TOUR43_V5_HANDSHAKE.md` |
| `orangerie_v5/` | Musée de l'Orangerie, V5: 55 tracks, EN + ES/FR/DE. Handshake: `ORANGERIE_V5_HANDSHAKE.md` |
| `orsay_v5/` | Musée d'Orsay, V5: 75 tracks, EN only so far. Handshake: `ORSAY_V5_HANDSHAKE.md` |
| `deliverables/` | Everything sent to the user: zips, route PDFs, scripts (.md), snapshots, image kit |

The same structure is used inside each guide folder:

- `v5/tracks/NNN.perf.txt`: the **source of truth**. Each file has a header (`@id @section @room @type @title @where @what @listen
  @brief @pace @energy @sources`), then `---`, then the spoken body. The body carries tags: `[pause] [long pause] [warmly] [quietly]
  [amused] [curious] [conspiratorial] [reverent] [wry] [lightly]` and `*emphasis*`.
- `v5/pipeline/`: `v5_direction.py`, `render_edge.py` and `render_kokoro.py`.
  - `v5_direction.py` handles parse, validate, clean, segments, master (mastering at **64 kbps** mono, −16 LUFS) and
    `check_tour` (a launcher safeguard plus a lock file).
  - `render_edge.py` renders with edge-tts. The voice comes from `EDGE_VOICE` (default **Ava**). `ONLY="NNN NNN"` renders a subset;
    `RESPELL=0` turns respelling off.
- `v5/i18n/<lang>/tracks/` holds the translations (Pitti and Orangerie). `v5/i18n/assemble.py` builds them, with checks.
- `build/`:
  - `make_bundle.py`: its `SECTIONS` list sets the section folders.
  - `route_sheet.py`: the "Route at a Glance" PDF, driven by `plan.json`.
  - `feedback_form.py`.
  - `build_all.sh`: rebuilds the bundle and the zip.
  - `static/`: the launchers, `README.txt`, `pronunciation.py` and `USER_TEST/` (`ONSITE_CHECKLIST.md`, `TEST_PLAN.md`).
- `findings/`: audits of the old guides. `research/`: fact sheets, graded OFF / SEC2 / WEAK / NONE. `v5/verify/`: verification
  reports. `v5/notes/`: logs.

## 2. Session setup (run first in a new cloud session)

```bash
# the build scripts use these absolute paths
ln -sfn /home/user/AudioQ/tour43_pitti_v5 /home/claude/pitti
ln -sfn /home/user/AudioQ/orangerie_v5    /home/claude/orangerie
ln -sfn /home/user/AudioQ/orsay_v5        /home/claude/orsay
mkdir -p /mnt/user-data/outputs          # Pitti's build_all.sh writes its zip here
cd /home/user/AudioQ && git checkout claude/tour43-pitti-v5-test-ddbz7z && git pull origin claude/tour43-pitti-v5-test-ddbz7z
pip list 2>/dev/null | grep -i reportlab || pip install reportlab   # route maps and forms
which ffmpeg pdftotext                    # needed for the checks below

# rebuild ONLY the guide you are working on (each prints "OK -> …zip"); the other two lines are for reference
bash tour43_pitti_v5/build/build_all.sh
bash orangerie_v5/build/build_all.sh
bash orsay_v5/build/build_all.sh

# validate all tracks (each line: track, word count)
for g in tour43_pitti_v5 orangerie_v5 orsay_v5; do python3 -c "
import sys,glob;sys.path.insert(0,'$g/v5/pipeline');import v5_direction as V
fs=sorted(glob.glob('$g/v5/tracks/*.perf.txt'));t=sum(len(V.validate(f)[1].split()) for f in fs)
print('$g',len(fs),'tracks',t,'words ~',round(t/125),'min')"; done
```

**Stand-in TTS** (for launcher tests only; it writes tones, never real speech). Create it once:

```bash
mkdir -p /tmp/shim && cat > /tmp/shim/edge_tts.py <<'EOF'
import subprocess
class Communicate:
    def __init__(self, text, voice, **kw): self.n = len(text.split())
    async def save(self, path):
        subprocess.run(["ffmpeg","-loglevel","error","-y","-f","lavfi","-i",f"sine=f=330:d={max(0.3,self.n/40):.2f}",
                        "-ar","24000","-ac","1",path],check=True)
EOF
# example: a full Orsay run into a fake home folder
T=/tmp/orsay_test; rm -rf $T; mkdir -p $T/home/Desktop $T/u && cd $T/u && unzip -q /home/user/AudioQ/orsay_v5/outputs/Orsay_V5_EN.zip \
 && cd Orsay_V5_EN && HOME=$T/home PYTHONPATH=/tmp/shim bash -c "printf '1\n1\n\n' | bash generate_audio.command" >/dev/null; \
 find $T/home/Desktop/Orsay_V5_EN_Ava -name '*.mp3' | wc -l    # expect 75
```

After any change: run `build_all.sh` → validate → stand-in test → copy the outputs to `deliverables/` → update that guide's
handshake → refresh its snapshot zip in `deliverables/` → commit and push (see Rules).

## 3. Rules (from the user; still binding)

- Edit only `v5/tracks/*.perf.txt` and `build/static/`, then rebuild with `build/build_all.sh`. Never reinvent the pipeline.
- **Work only on the guide the user names** (5 Oct). Rebuild only that guide; in the setup below, run only its `build_all.sh`.
  Reading another guide's files as a reference is fine; say so plainly if you do.
- **Real audio is made only on the user's Mac**, with the bundle's launcher. Never fake or substitute audio. A stand-in voice is for
  launcher tests only, and must be called that.
- **Facts:** the official museum site comes first. Wikipedia is never the only source. If a fact can't be verified, hold it and tell
  the user. Grades: OFF (official), SEC2 (two reputable independent sources), WEAK / NONE (do not use).
- **Ask before deleting anything.** Moving a file into a `held/` folder is the accepted alternative to deleting it.
- **Don't touch the June release folders** on the user's Desktop.
- **ElevenLabs is on hold.** If it is ever used, the API key comes only from the environment and is never written to a file.
- **Give a verdict with pros and cons before acting on any question.** The user asked for this explicitly; don't act on a question
  before answering it.
- Keep updates short and plain: say what is verified, what isn't, and what couldn't be tested.
- Before the session ends: update the guide's handshake, refresh its snapshot zip in `deliverables/`, and commit and push.
  - Commit trailer:
    `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` and `Claude-Session: <the session URL>`.
  - No model names anywhere else in commits.
- **Writing standard:**
  - Lengths: R 180–280 words; W, ANCHOR and CLOSE 250–360.
  - No `;` or `(` in speech, and at most 2 em-dashes.
  - No opening hours, prices or tickets. Never say "next track".
  - "The museum says" at most once per track.
  - Each track ends with a closing cue that sends the listener to the next stop.
- **Network:** the egress policy blocks museum sites (uffizi.it, musee-orangerie.fr, musee-orsay.fr, wikipedia). Research goes
  through WebSearch with `allowed_domains=["musee-orsay.fr"]` etc.; those extracts count as OFF. The search budget is about 200 per
  session. To lift the block, the user adds the domains under Network access in the environment settings
  (https://code.claude.com/docs/en/cloud-environments#network-access).

## 4. Decisions the user has made (don't re-ask)

- **Voices:**
  - English: **Ava** (`en-US-AvaMultilingualNeural`), launcher option 1 and the default.
  - Spanish: **Dalia** (`es-MX-DaliaNeural`). French: **Vivienne** (`fr-FR-VivienneMultilingualNeural`). German: **Katja**
    (`de-DE-KatjaNeural`). All female.
- **Bitrate:** **64 kbps**, for every guide and every language.
- **Translations:** rewritten for listening, not word for word. Formal address (usted / vous / Sie). Facts unchanged. Each language
  gets an independent native-level review, then `assemble.py` checks.
- **Launcher safeguards:** stop if old and new versions are mixed; one render per output folder (lock file).
- **Pitti:** Royal Apartments come after Fashion & Costume.
- **Orsay:**
  - Route level 0 → 5 → 2 → exit.
  - Tokyo loans (14 Nov 2026 – 28 Mar 2027) are handled with spoken fallbacks: 008 Gleaners, 046 Starry Night, 053 Arearea, and 021
    Bellelli if it travels.
  - 012 *L'Origine du monde* is optional.
  - The 9 extra tracks were approved and are done.
  - The Route at a Glance must be schematic and customer-ready. It now uses the A3 floor-plan design.
- **Images for the apps:** public-domain scans from Wikimedia Commons. Picasso is protected until 2043, so it needs a licence.
  Building photos come from Pexels/Unsplash. Kit: `deliverables/Orangerie_App_Images_Kit.zip` (`download_images.py` runs on the Mac).

## 5. Status per guide

| Guide | EN | ES/FR/DE | Route map | Tested | Open |
|---|---|---|---|---|---|
| Pitti V5.1 | 61 tracks, ~142 min | done; reviewed by assemble.py checks only (no second native review yet) | pictorial, one page | stand-in only; the user has rendered EN at least once (first run mixed old files; re-render with the current zip) | the user may want the same second review as the Orangerie; native-speaker check |
| Orangerie V5 | 55 tracks, ~128 min | done + independent review per language | pictorial, exit by the entrance | stand-in only; the user was rendering all 4 languages at session end | level −2 room order and exit door on site; native-speaker check |
| Orsay V5 | 75 tracks, 20,312 words, ~2 h 42 | done 5 Oct (session 2) + independent review per language; FR quotes are verified originals or reported speech | A3 schematic floor plans (2026 rooms) | stand-in: 75 files in each of EN/ES/FR/DE | on-site checklist; 3 quotes kept as reported speech until checked against the live museum pages; native-speaker check; 048 @what title; Oviri on display? |

Orsay detail: see `orsay_v5/ORSAY_V5_HANDSHAKE.md`.
- **Official plan:** `orsay_v5/source/Planguide_Orsay_ete_2026.pdf`, read out in `orsay_v5/findings/M_planguide_ete_2026.md`.
- **Numbering:** history in `orsay_v5/v5/notes/RENUMBER_75.md`. `v5/PLAN.md` still has the OLD numbering, so use the tracks or
  `plan.json`.
- **Held** (in `v5/held/` or never written): Whistler's *Mother* (in Amsterdam until 10 Jan 2027); Puvis's *Pauvre Pêcheur*,
  Monet's *London Parliament* and Roty's *La Semeuse* (not on display); photography (the prints rotate).

## 6. What to do next (the order the user is likely to ask for)

1. **Orsay ES/FR/DE: DONE (5 Oct, second session).** 75 tracks per language, reviewed, assembled, in the bundle with
   `generate_audio_ES_FR_DE.command`. Details, word counts and open points: `orsay_v5/ORSAY_V5_HANDSHAKE.md` STATE 3. Brief,
   notes and review logs: `orsay_v5/v5/i18n/review/`. Next for it: the user's real-voice samples (013 + 044 per language) and a
   native-speaker spot check (`deliverables/Orsay_V5_Scripts_ES/FR/DE.md`). If an English track changes, edit the same passage in
   `v5/i18n/<lang>/tracks/NNN.perf.txt` in all three languages and re-run the check (`assemble.py --check` works on a JSON work
   folder; for perf files, rebuild and validate).
   - Fact fixed in the English this session: 018 Bazille killed at twenty-eight (was twenty-six), from the museum's own pages.
   - 7 Oct: Orsay renderer now times out and retries (no more stuck renders); every MP3 gets phone labels and a Yo Tours
     cover; an A/B test of voice finish / room tone / chime is waiting for the user's ear (`make_ab_test_013.command`).
     See `orsay_v5/ORSAY_V5_HANDSHAKE.md` STATE 4. Pitti/Orangerie not yet ported.
2. **Orsay quotes:** if `musee-orsay.fr` becomes reachable, check the Christopher Gray, "black Eve" and Redon "refined, savage" quotes
   verbatim (tracks 055 to 058, see `v5/notes/FINAL_PASS_LOG.md`), and the rooms listed in `ONSITE_CHECKLIST.md`.
3. **Orsay app images:** build an image kit like the Orangerie one. Copy `orangerie_v5/app_images/` and generate the CSV from
   `orsay_v5/v5/tracks` @what lines. Mind the Picasso rule (no Picasso works in Orsay V5 so far).
4. **Pitti:** the user may ask for the independent second-review pass on ES/FR/DE, as done for the Orangerie.
5. **After on-site tests:** apply the checklist results to `@room`, `@where` and the closing cues → rebuild → resend.

## 7. Commands the user runs on the Mac (for reference when helping them)

```bash
# one-time
brew install ffmpeg && python3 -m pip install --user edge-tts
# start clean: move old output folders off the Desktop, unzip each new zip into an empty place
mkdir -p ~/AudioGuides && cd ~/AudioGuides && unzip -oq "$(ls -t ~/Downloads/Orsay_V5_EN*.zip | head -1)"
# render (first number = voice/language, second = 1 full / 2 samples; the last empty line closes the window)
cd ~/AudioGuides/Orsay_V5_EN && printf '1\n2\n\n' | bash generate_audio.command          # samples 013 + 044, Ava
cd ~/AudioGuides/Orsay_V5_EN && printf '1\n1\n\n' | bash generate_audio.command          # full EN, 75 MP3s
cd ~/AudioGuides/Orangerie_V5_EN && printf '1\n1\n\n' | bash generate_audio_ES_FR_DE.command   # 1 ES Dalia, 2 FR, 3 DE
cd ~/AudioGuides/Orsay_V5_EN && printf '1\n2\n\n' | bash generate_audio_ES_FR_DE.command       # Orsay ES samples 013 + 044 (2 FR, 3 DE)
# check
find ~/Desktop/Orsay_V5_EN_Ava -name '*.mp3' | wc -l && du -sh ~/Desktop/Orsay_V5_EN_Ava
```

Lessons from this session:
- The user's first runs failed because the unzip step was skipped. Always chain commands with `&&`.
- Never let two renders run at once. The lock file now prevents it.
- A 233 MB folder was old and new scripts mixed together. The safeguard now stops that.

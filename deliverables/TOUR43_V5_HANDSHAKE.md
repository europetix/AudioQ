# TOUR #43 — PALAZZO PITTI + BOBOLI — V5 HANDSHAKE (state 3)

**Date:** 5 Oct 2026 (state 2 was 4 Oct 2026; its sections 1–8 follow below, with V5.0 numbering)  
**Status:** **V5.1 build: 61 tracks (~142 min), Royal Apartments after Fashion & Costume, one-page "Route at a glance" PDF.** Not yet rendered or heard. Waiting on the user to render both voices on his Mac, then the listening test and on-site test.  
**User:** Puneet Sharma (puneet@yotours.in).  
**Series rules:** `V4_MASTER_HANDSHAKE_5.md` + `ADDENDUM` + `AUDIO_TOURS_MASTER_STATE_JUL2026.md`, in `~/Downloads/audio_tours_handoff_bundle/`. (Not available in the 5 Oct cloud session; not read there.)

---

## STATE 3 — WHAT CHANGED ON 5 OCT 2026 (read this first)

**Where the work lives now:** git repo `europetix/AudioQ`, branch `claude/tour43-pitti-v5-test-ddbz7z`, folder `tour43_pitti_v5/` (= the snapshot layout). Commits: baseline snapshot → hedge/cue fixes → fact-check fixes → V5.1 cut + route PDF → handshake. Restore as before: copy/unzip to `/home/claude/pitti` (scripts use absolute paths; a symlink works) and run `build/build_all.sh` → must print OK.

**1. 18 tracks cut, 79 → 61, renumbered.** Held unchanged in `v5/held/cut_5oct2026/` (V5.0 numbers). Mapping + reason per track: `v5/RENUMBER_5OCT2026.md`. V5.1 running order: top of `v5/PLAN.md`. User asked to remove tracks whose location/content could not be verified, and the room intros 012/015/017/018 (V5.0), to shorten the tour.
- Volterrano Wing 005–011: newest official notice says the wing is closed (no end date); its exit, the Sala della Musica, is closed 30 Jun–25 Oct 2026 (uffizi.it notice "chiusa-sala-della-musica-a-palazzo-pitti").
- 037 Four Philosophers: several secondary sources say it moved to the Uffizi (Self-Portraits, room 1) on 10 Jul 2023.
- 039 Titian Young Englishman: MiC catalogue 0900295133 gives Sala di Apollo since 1956, not Mars.
- 017 Napoleon's Bathroom: framing contradicted (built by Elisa *for Napoleon*, uffizi.it Napoleon online exhibition).
- 012, 014, 015, 018 room intros (mostly secondary sources); 054 Fattori Self-Portrait, 056 Lo Staffato, 059 De Chirico, 073 Knight's Garden (room / opening unconfirmed, optional).
- Hand-over cues rewritten so every track still names the next stop (checked: all 60 hand-overs match the next track's @where; no dangling references).

**2. Second full fact-check (5 parallel checkers + 1 independent "traveller" reviewer), all 61 tracks.** Network: this cloud environment blocks uffizi.it, cultura.gov.it, wikipedia, getyourguide (proxy 403) — evidence came from **search-result snippets** of official pages plus the 4 Oct fetch records (V1/V2/G1–G6). So nothing was re-read on an official page on 5 Oct. Fixes applied (79 automated before/after checks pass):
- Errors: Bartolini Charity marble finished c.1835 (not 1824); Baldacchino is oil on **canvas**; Velata — Vasari doesn't name Margherita Luti (later tradition), beads not pearl; Rubens letter: *woman* with broken lute, architect with instruments; La Bella — Duke wrote to his agent in Venice, not Titian; Canova *met* Napoleon five times (not "sittings"); Rotonda awning ochre, not striped; Eleonora malaria from period reports, TB from bones; Abundance set up 1637 (catalogo.beniculturali.it 0900289222); Oceanus finished by 1576 for the Medici, moved 1911 (0900286790); Boboli developed over three centuries (uffizi history); Neptune pose (on a rock, trident swung down); Grotta Grande satyrs; Annalena Malatesta (of Rimini, living in Florence).
- Unsourced details cut or hedged: Impannata restoration claim ("some scholars believe"), Child clings to robe, white veil, Christ in a cloud (icon), painted "tapestries" (chapel), Andromeda, Roman marbles on the Viottolone, cypress replanting date, green-and-cream Kaffeehaus, Morgante original kept in the Kaffeehaus, "first project" of Boboli 2030, etc.
- Clarity (traveller review): Iliad detour line simplified (009), Venus intro shortened (028), duplicate Vasari "painter without errors" removed (023), garbled sentences fixed.
- 038/V5.1-025 card duplicate hedge fixed; 020 (V5.1 008) room now cites culturaitalia (ministry portal).

**3. Traveller navigation PDF** `Palazzo_Pitti_Audio_Guide_Route.pdf` (replaces the V5 Route Sheet; built by `build/route_sheet.py`, same house pattern). **Final form (user, 5 Oct): ONE page, "Route at a glance" only**: the 8 stops in walking order, each with floor, track range, minutes and short directions; Iliad-closure line in the Palatine stop; Royal Apartments stop flagged "Separate ticket … No ticket? carry on to step 6". The longer per-track version described next was superseded. Addresses GetYourGuide review complaints for the current product (t842382, search snippets only): "hard to match audio to rooms", "rooms labelled differently from the app", "audio not in room order", "want offline/clearer mapping". It has: how-to (MP3s, offline, play in number order), October notices (Iliad closure with track ranges computed from plan.json; Royal Apartments; Boboli fences), route-at-a-glance diagram, then per track: room number + the Italian name on the museum's signs, title, where to stand, minutes. The launcher copies it into the output folder.

**3b. Royal Apartments moved (user, 5 Oct): they need a separate ticket**, so they now come after Fashion & Costume, on the way back down (the meeting point is the Palatine entrance atrium, one floor below). Order: Palatine 002–032 → Modern Art 033–040 → Fashion 041–043 → Royal Apartments 044–045 → Icons & Chapel 046–048 → Boboli 049–060 → Closing 061. Section folders renumbered (02 Modern Art, 03 Fashion, 04 Royal). Cues rewritten in 001, 032, 043, 045; all hand-overs re-checked. Second mapping step in `v5/RENUMBER_5OCT2026.md`. "Separate ticket" is the user's product information; not re-verified on uffizi.it (the official page says reservation is compulsory). No ticketing in the spoken text.

**4. Other build changes:** launcher output → `~/Desktop/Palazzo_Pitti_V5_1_EN_<voice>` (so V5.0 renders never mix); listening test uses V5.1 033→021 Throne Room, 027→015 Seggiola, 070→053 Amphitheatre; TEST_PLAN + ONSITE_CHECKLIST rewritten for V5.1; README counts; `pronunciation.py` +69 names (144 total) — **not listen-checked**; Boboli stop labels renumbered (Stop 8–11).

**Verified vs not (honest state, 5 Oct):**
- Verified in-session: build OK; 61 contiguous tracks; all hand-overs connect; validator + length/style rules pass; PDF renders correctly (checked visually).
- Facts: every remaining claim has an official or two-source basis per the checkers, *at snippet level*. Still needs on site: see `USER_TEST/ONSITE_CHECKLIST.md` (~20 items: Rubens room, Sleeping Cupid room, Doni backs, corridor left/right, Bacchino left, Neptune pose, fences…).
- Voice / "sounds human / engaging": **untested**. No V5 audio has been heard. Traveller review (text only): strong stories; risks = repeated "Planet Rooms backwards" explanation (still in 002, 010, 014, 024, 026), several "who was she?" portraits in a row, many [curious] openers; free voices will flatten jokes. Only the listening test can answer this.

**Next steps (state 3):**
1. On the Mac: render V5.1 with both voices (`printf '1\n\n' | bash generate_audio.command`, then `2`), into the new V5_1 folders.
2. Listen-QA 3–5 tracks (pronunciation respellings especially), then Test 1 (listening) and Test 2 (on site with the checklist).
3. If allowed, add `uffizi.it`, `www.uffizi.it`, `pdf.uffizi.it`, `catalogo.beniculturali.it`, `catalogo.cultura.gov.it`, `cultura.gov.it` to the cloud environment's network allow-list and re-read the official pages for the snippet-level claims.
4. Optional text pass from the traveller review (reduce the repeated Planet-Rooms explanation, vary openers).
5. After 25 Oct: confirm the Iliad Room reopened; remove the detour line from V5.1 009 and the Iliad notice in `build/route_sheet.py`; rebuild.
6. Then §7 items 5–8 below (full PDF rebuild, audit report, Spanish, series updates).

---

## 0. START HERE (new Claude cloud session)

1. Ask the user to attach two files from `~/Downloads/audio_tours_handoff_bundle/`:
   - this file;
   - `tour43_V5_source_snapshot.zip`.
   If the session is linked to his Mac, stage them yourself instead (connected folders: `~/Downloads`, `~/Desktop`).
2. Restore the snapshot:
   ```bash
   mkdir -p /home/claude/pitti && cd /home/claude/pitti && unzip -o <path>/tour43_V5_source_snapshot.zip
   pip install reportlab --break-system-packages   # if missing
   bash build/build_all.sh    # rebuilds bundle + route sheet + feedback form + zip; must print "OK"
   ```
   All paths in the scripts are absolute (`/home/claude/pitti/...`), so restore exactly there.
   A rebuild reproduces the shipped bundle byte for byte, except the timestamps inside the PDFs.
3. **Do NOT rebuild anything from notes or PDFs. Do NOT re-invent the pipeline.** Everything is in the snapshot.
4. Ask the user what stage he is at: renders done? listening test done? on-site test done? Then continue from §7.

---

## 1. WHAT HAPPENED IN THE 4 OCT SESSION (short)

**User's three complaints about the released Pitti guide:**
- **Accuracy and placement:** works described in the wrong rooms.
- **Route:** the audio order didn't match the visitor's path. "Lots of complaints."
- **Voice:** "monotonous AI voice". He wants it to sound like a real person telling stories, with a process that can be repeated for other tours.

**What I did:**
1. **Confirmed the latest version.** The customer-facing release is the **90-track June build**: `~/Desktop/Palazzo_Pitti_Audio_EN_am_michael` plus `Palazzo_Pitti_EN.pdf` (1 Jun 2026, ~195 min). The 92-track July zip, `Palazzo_Pitti_Audio_EN.zip` in the handoff bundle, was never rendered. It added Bentivoglio, a wrong Galileo track and a stale Saturn closure note.
2. **Full audit**, via 6 parallel reviewers plus a route study. Findings are in `findings/G1–G6`, which use the OLD 92-track numbering. About 210 issues were found. The root causes:
   - The Palatine ran BACKWARDS. The official one-way route runs from Room 1 to Room 28 and exits through the Sala delle Nicchie, so the Planet Rooms go Saturn → Jupiter → Mars → Apollo → Venus.
   - Several works were in the wrong rooms.
   - The Costume museum was reorganised in 2025.
   - The Royal Apartments are staff-led group visits only.
   - The Boboli order was wrong: the Bacchino is to the LEFT, and the Grotta Grande comes before the Grotta di Madama.
3. **Designed the V5 Audio Standard**, the repeatable process (`v5/V5_AUDIO_STANDARD.md`). It covers story-first scripts, a direction layer, mastering and 8 quality gates.
4. **Voice-quality plan.** I first proposed paid expressive TTS, and the user picked ElevenLabs (his only paid account). I built a bake-off kit (`v5/kit/`). Then he decided: **"stick to the available free voices with the expert changes suggested by you, we will do a user testing with the new Audio."** The paid step is ON HOLD until the test results are in.
5. **Rewrote all 79 tracks**, with parallel writers working from `v5/WRITER_BRIEF.md`. Two independent fact-checkers then reviewed them (`v5/verify/V1`, `V2`). All 21 of their fixes are applied, and the resolution log is in `v5/notes/*_CHANGES.md`.
6. **Built and shipped the test bundle**, in the same launcher shape as before. I tested both voice paths with stand-in voices. It went to `~/Downloads/Palazzo_Pitti_V5_Test_EN/` (unzipped) plus `.zip`.

**User decisions (locked):**
- Free voices first. ElevenLabs only if the test shows the voice is the bottleneck.
- Pitti is the pilot for V5. If it works, the process rolls out to other tours.
- Rewrite plus a direction layer (not just re-voicing the old scripts).
- Coverage, "Fix + top 3 additions":
  - CUT the Galileo track. His portrait is at the Uffizi (room E7).
  - ADD Raphael's Doni portraits (Saturn), Titian's *La Bella* (Venus), and Ussi's *Expulsion of the Duke of Athens* (Modern Art, Room 3).
- Royal Apartments: 2 tracks, one before and one after the guided visit.
- Costume: a durable 3-track version (rotating displays, so no room-by-room claims).

---

## 2. WHERE EVERYTHING IS

**User's Mac:**

| Path | What |
|---|---|
| `~/Downloads/Palazzo_Pitti_V5_Test_EN/` (+ `.zip`) | THE V5 TEST BUNDLE (79 tracks). No MP3s inside; the user renders them. |
| `~/Desktop/Palazzo_Pitti_V5_Test_EN_Brian/` and `_am_michael/` | Where the launcher writes the MP3s. These did NOT exist yet on 4 Oct. |
| `~/Desktop/Palazzo_Pitti_Audio_EN_am_michael/` | June release, 90 tracks, OLD numbering (live product, don't touch). |
| `~/Downloads/audio_tours_handoff_bundle/tour43_V5_source_snapshot.zip` | Full V5 source (see the table below). |
| `~/Downloads/Pitti_V5_Voice_Bakeoff/` | ElevenLabs bake-off kit (paid step, on hold). |
| `~/Downloads/Pitti_V5_Samples/` | 3 early calibration samples (rendered with the ONNX Kokoro, voice reference only). |

**Snapshot layout (restore to `/home/claude/pitti`):**

| Path | What |
|---|---|
| `v5/tracks/001–079.perf.txt` | **SOURCE OF TRUTH.** Header fields (`@id @section @room @type @title @where @what @listen @brief @pace @energy @sources`), then `---`, then the spoken body with direction tags. |
| `v5/PLAN.md` | Master running order: NEW number, OLD number, type, section, room, next physical stop. |
| `v5/V5_AUDIO_STANDARD.md` | The repeatable writing, direction, voice and QA standard. |
| `v5/WRITER_BRIEF.md` | Brief used for the parallel writers (reuse for other tours). |
| `v5/calibration/` | Voice anchors: old 016 / 017 / 083, which are now V5 033 / 034 / 070. |
| `v5/notes/*_CHANGES.md` | Per-track change log against the old script (the audit resolution log). The verification pass is at the end of `063-079_CHANGES.md`. |
| `v5/verify/V1_001-040.md`, `V2_041-079.md` | Independent fact-check reports (all applied). |
| `v5/pipeline/` | `v5_direction.py` (shared), `render_kokoro.py` (V5), `render_edge.py` (Brian, V5). |
| `v5/kit/` | `render_v5_elevenlabs.py` bake-off renderer (paid, on hold). |
| `v5/backup_preverify/` | The 79 tracks before the verification fixes. |
| `build/build_all.sh` | One-command rebuild. |
| `build/make_bundle.py` | Turns perf files into `scripts/` + `perf/` + `plan.json`, plus the static files. |
| `build/route_sheet.py` | Route Sheet PDF, cloned from the Tour #49 route-map pattern and house palette. |
| `build/feedback_form.py` | Printable tester form, 2 pages. |
| `build/static/` | Hand-maintained bundle files: `generate_audio.command` (V5), `README.txt`, `pronunciation.py` (75 entries), and `USER_TEST/` (`TEST_PLAN.md`, `ONSITE_CHECKLIST.md`, `make_listening_test.command`). |
| `bundle/Palazzo_Pitti_V5_Test_EN/` | Built bundle, the same as shipped. |
| `findings/G1–G6`, `BRIEF.md` | The audit, in OLD 92-track numbering. G6_ROUTE has the full route evidence and sources. |
| `tracks/NNN.txt`, `pdf.txt` | Old 92-track scripts plus their PDF cards, one per track, used as review sources. |
| `jul/` | Unpacked 92-track July zip: the ORIGINAL V4.5 launcher, `render_kokoro.py`, `pronunciation.py` and maps. This is the reference for "don't reinvent". |

---

## 3. THE V5 BUNDLE (what the user runs)

```
Palazzo_Pitti_V5_Test_EN/
  generate_audio.command   same shape as V4.5. 1 = Brian (calls render_edge.py), 2 = am_michael (uv run … render_kokoro.py)
  render_kokoro.py  render_edge.py  v5_direction.py  pronunciation.py  plan.json
  scripts/<section>/NNN_<Room-label>_<Title>.txt   exactly the spoken words
  perf/<section>/NNN_<…>.perf.txt                  same words + direction (stripping the tags = the script, checked at build)
  Palazzo_Pitti_V5_Route_Sheet.pdf                 replaces the old maps (old maps carry wrong numbering)
  README.txt
  USER_TEST/  TEST_PLAN.md  ONSITE_CHECKLIST.md  Pitti_V5_Feedback_Form.pdf  make_listening_test.command
```

**Section folders:**

| Folder | Tracks |
|---|---|
| `00_Welcome` | 1 |
| `01_Palatine_Gallery` | 45 |
| `02_Imperial_and_Royal_Apartments` | 2 |
| `03_Gallery_of_Modern_Art` | 11 |
| `04_Museum_of_Fashion_and_Costume` | 3 |
| `05_Russian_Icons_and_Palatine_Chapel` | 3 |
| `06_Boboli_Gardens` | 13 |
| `07_Closing` | 1 |

Total: **79 tracks, 22,144 words, ~177 min.**

**Output:** `~/Desktop/Palazzo_Pitti_V5_Test_EN_<Brian|am_michael>/`, a different folder from the June release.

**How the user runs it:** in Terminal, `bash ` then drag in `generate_audio.command`, then Return. macOS Gatekeeper blocks double-clicking downloaded `.command` files; "Open Anyway" in Privacy & Security also works.

**Requirements:**
- ffmpeg (`brew install ffmpeg`), required for Brian. Without it, Kokoro writes WAV files.
- Brian needs internet throughout.
- Kokoro needs internet only on first run (uv installs Python 3.11 + model, ~2 GB).
- Re-running skips finished tracks. Mastering writes to `.part.mp3` and then renames, so no half files are left behind.

**How direction is performed by the free engines (`v5_direction.py`):**
- **Tags:** `[pause]` = 0.55 s; `[long pause]` = 1.1 s; 0.75 s between paragraphs; 2 s tail.
- **Delivery tags:** `[warmly] [quietly] [amused] [curious] [conspiratorial] [reverent] [wry] [lightly]`. Each colours the rest of its paragraph:
  - Kokoro: speed multiplier and gain (`KOKORO_STYLE`). Base speed is 0.85.
  - Brian: rate %, volume % and pitch Hz per segment (`EDGE_STYLE`). Base rate is -8%. One edge-tts call per segment.
- `*word*` emphasis is dropped by the free engines (kept for ElevenLabs v3 as CAPS).
- **Mastering:** two-pass loudnorm to -16 LUFS / -1.5 dBTP, 96k mono MP3. Tests measured -16.8 LUFS, which is acceptable.
- **Changed from V4.5 on purpose:** 96k instead of 40k, a 2 s tail instead of 5 s, and per-passage synthesis instead of one call per track.

**Tested on 4 Oct** with stand-in shims (a Kokoro ONNX wrapper and a fake edge_tts), on 4 tracks through the real launcher, both options:
- folders, names, skip-on-rerun, copy steps, tag→prosody mapping and loudness all OK;
- `make_listening_test.command` was tested against fake folders.

The real Brian and am_michael voices have **not** been heard on V5 yet.

---

## 4. RUNNING ORDER (full table in `v5/PLAN.md`)

**A. Opening.** 001 Piazza Pitti.

**B. Palatine** (first floor, official one-way route):

| Tracks | Room |
|---|---|
| 002 | Rooms 1–2 |
| 003–004 | Castagnoli 3 + Table of the Muses |
| 005–011 | Volterrano Wing: Allegorie 4, Belle Arti 5, Ercole 6, Aurora 7, Berenice 8, Psiche 9, Arca 11 |
| 012–013 | Prometeo 14 + Lippi tondo |
| 014 | Flora 17 |
| 015–016 | Ulisse 19 + Impannata |
| 017 | Napoleon's Bathroom 20 |
| 018–020 | Educazione di Giove 21: Allori Judith, Caravaggio Sleeping Cupid |
| 021 | Stufa 22. Carries the temporary Iliad detour line. |
| 022–025 | Iliade 23: Passerini Assumption, Bartolini Charity, Artemisia Judith |
| 026–032 | **Saturn 24:** Seggiola, La Gravida (moved here), Leo X, Granduca, Baldacchino, **Doni (NEW)** |
| 033–035 | **Jupiter 25:** Throne Room, La Velata, del Sarto St John |
| 036–039 | **Mars 26:** Four Philosophers, Consequences of War, English Gentleman |
| 040–041 | **Apollo 27:** Magdalene |
| 042–046 | **Venus 28:** Canova Venus Italica, Concert, Aretino (moved here), **La Bella (NEW)** |

Exit through the Sala delle Nicchie.

**C. Royal Apartments.** 047 before the staff-led ~30-minute visit (meeting point: Palatine entrance atrium); 048 after.

**D. Modern Art** (second floor, corridor LEFT), 049–059:
- 052 is the **Ussi (NEW)**.
- 059 is De Chirico's *Metaphysical Composition* (his late replica of *Song of Love*; the original is at MoMA).

**E. Fashion & Costume** (corridor RIGHT, staircase of two short flights, stair-lift; a dead end), 060–062.

**F. Ground floor.** 063–065: Russian Icons + Palatine Chapel.

**G. Boboli,** 066–078:

| Track | Stop |
|---|---|
| 066 | Courtyard |
| 067 | Bacchino (LEFT) |
| 068 | Grotta Grande |
| 069 | Grotta di Madama |
| 070 | Amphitheatre |
| 071 | Neptune |
| 072 | Kaffeehaus |
| 073 | Knight's Garden |
| 074 | Abundance |
| 075 | Viottolone |
| 076 | Isolotto |
| 077 | Limonaia |
| 078 | Ways out |

**Closing.** 079, location-neutral.

**HELD (not in the build):**
- Van Dyck, *Cardinal Bentivoglio*: room not officially confirmed (the uffizi.it slug 404s).
- Caravaggio, *Knight of Malta*: the reviewers disagree on whether it's in Iliad or Venus.
- Verified gaps for a later release: Ezekiel, Inghirami, Perugino, Fra Bartolomeo, Lega, Magenta, and the Chapel altar detail.

**Old ↔ new numbering:**
- `v5/PLAN.md` maps NEW to OLD (OLD = 92-track July numbering).
- June 90-track equivalents used in the listening test:
  - June 015 Throne Room = V5 033
  - June 019 Seggiola = V5 027
  - June 081 Amphitheatre = V5 070

---

## 5. VERIFIED FACTS THAT DRIVE THE ROUTE (re-check before release)

- **Official one-way Palatine route,** Rooms 1 → 28, exit via the Sala delle Nicchie. Source: G6_ROUTE §1, uffizi.it.
- **Iliad Room closed 30 Jun – 25 Oct 2026.** Source: uffizi.it notice "palazzo-pitti-tempranea-chiusura-della-sala-delliliade", modified 29 Jun.
  - The official detour runs Stufa → Educazione → Ulisse → Prometeo → Giove → Saturno → Marte → Apollo → Venere → Nicchie.
  - Track 021 handles it; so does the Route Sheet box ("play 033–035 in Jupiter, then 026–032 in Saturn, carry on from 036").
  - **After 25 Oct:** confirm the room has reopened, then remove the line from 021 (`v5/tracks/021.perf.txt`) and the box in `build/route_sheet.py`, and rebuild.
- **Saturn** was closed only until 16 Jun 2026; it's open now. During that closure the Doni portraits were temporarily in Apollo. The official page now says "Palatine Gallery, Saturn Room".
  - **The series-level rule that the Doni portraits are at the Uffizi is OUTDATED.** Update `AUDIO_TOURS_MASTER_STATE` / the handshake addendum.
- **Official artwork pages used:**
  - Mars Room ceiling (`uffizi.it/en/artworks/mars-room`): Cortona 1643–44 and 1647. A naval battle; Mars lights the prince with his star; Hercules' trophy; prisoners led toward Victory, Plenty and Peace; the arms crowned with Ferdinando II's name.
  - Apollo ceiling: Cortona 1647, Ferri 1659–61.
  - Jupiter ceiling: the figures are "probably" the Medicean stars.
  - Velata: canvas, 1512–15.
  - Amphitheatre: Tribolo from 1550 in the stone quarry; Giulio Parigi 1630–34; obelisk 1790; basin 1840.
  - Artemisia's Judith is in the Iliad Room, per the official Allori page.
  - Grotta di Madama: "small door with jambs and cornice in white marble"; the name comes "presumably" from Maria Maddalena of Austria.
- **Boboli:** restoration programme "Boboli 2030", with fences at the Amphitheatre tiers, the Neptune basin and the Limonaia gates. The Porcelain Museum is closed.
  - Since 3 Mar 2026 there has been a combined Boboli+Bardini ticket. Ticketing is kept out of the spoken text (Add-on #25).

The items no web source could confirm are in `USER_TEST/ONSITE_CHECKLIST.md`, about 20 of them. Examples: the Volterrano order, the Rubens and Fattori rooms, the Bacchino turning left, the Knight's Garden being open, and whether the backs of the Doni panels are visible.

---

## 6. THE USER TEST (as designed and shipped)

- **Test 1, desk and blind (voice only).**
  - 6–10 listeners; 3 tracks × 3 versions: A = June am_michael, B = V5 am_michael, C = V5 Brian.
  - Two statements, scored 1–5: "sounds like a real person telling me a story" and "would listen to 30 more".
  - `make_listening_test.command` builds the shuffled clips plus `ANSWER_KEY.txt` in `~/Desktop/Pitti_Listening_Test/`. It needs all 3 Desktop folders to exist.
- **Test 2, on site (route + content).**
  - 6–12 testers: half on the June guide, half on V5, both in am_michael.
  - Testers mark per-track flags: L = lost, W = wrong, R = robotic, B = bored. Then 9 end questions on a 1–5 scale, plus open questions. Observers shadow 2–3 testers.
- **Decision table** (in TEST_PLAN):
  - R flags spread across tracks AND voice score ≤ 3 → run the ElevenLabs bake-off (kit ready) and re-render the same perf files.
  - L or W flags clustered on certain tracks → fix those cues or placements.
  - B flags → tighten those tracks.
  - V5 beats June → full PDF rebuild and release.

---

## 7. NEXT STEPS (in order)

1. **User renders both voices** with the launcher. Help him with Gatekeeper, ffmpeg or uv if needed. Never render the customer audio in the container.
2. If he wants it, **listen-QA together**: stage 3–5 rendered MP3s from his Desktop. Check timing with ffprobe and loudness with ebur128. Look for odd pauses or mispronunciations and fix them in `perf/` tags or `pronunciation.py` (`build/static/pronunciation.py`). Rebuild with `build_all.sh`.
3. **Test 1, then Test 2.** Collect the results and analyse them with the decision table.
4. **If the voice is the bottleneck:** run the ElevenLabs bake-off (`v5/kit/render_v5_elevenlabs.py`). It covers 2–3 voices × eleven_v3 / multilingual_v2. Estimated ~19k credits for 2 voices, ~29k for 3. The user runs it on the Mac with his API key from the environment; never store the key.
   - Notes for that path: v3 needs stability of 0.0, 0.5 or 1.0; pauses become ellipses; the limit is 3000 characters.
   - Neither the container nor the Mac VM can reach the TTS APIs. It has to run in the user's own Terminal.
5. **After the test:**
   - Apply the fixes.
   - **Full V5 PDF rebuild** in house style. The `@where` / `@what` / `@listen` card fields are already in every perf file. Clone the PDF renderer from `tour43_source_snapshot.zip` (`render_pdf.py`); don't write a new one.
   - Get the user's approval (Rule 11 / Rule 13: PDF first).
6. **Consolidated audit and resolution report** in the Prado format (`Prado_PLACEMENT_AUDIT_JUL2026.md`). Sources: `findings/`, `v5/notes/`, `v5/verify/`.
7. **Spanish:** the ES guide (78 tracks) is stale and was deliberately not touched. It would need V5 in Castilian (formal *usted*), after the EN version is approved.
8. **Series follow-ups:**
   - Update the series master state (Doni rule; V5 standard available).
   - Offer the V5 standard to other tours only after the Pitti test proves it.

---

## 8. GOTCHAS LEARNED (don't repeat)

**Pipeline and audio:**
- **"Why are you trying to reinvent the pipeline"** (user, during the GEM tour). Clone the existing scripts (`jul/` and the earlier snapshots) and render on the Mac via the launcher. Never fake audio, and never ship in-container renders as the product.
- **Audio is rendered on the Mac only.** The container can't reach edge-tts (403) or ElevenLabs. The Mac VM (device_bash) is also blocked from the TTS APIs.

**Network and research:**
- curl to www.uffizi.it is blocked, but WebFetch works. The WebSearch budget ran out on 4 Oct, so rely on WebFetch of official pages.
- **Wikipedia is never a sole source** (Rule 6). uffizi.it artwork slugs often 404 when guessed: confirm via site pages, and if you can't, HOLD the claim.

**Working on the user's Mac:**
- **Deleting is off** in his connected folders. A `__pycache__` remains in `~/Downloads/Pitti_V5_Voice_Bakeoff/` because deletion wasn't granted. Ask before requesting delete permission.
- `~/Desktop` can't be reached as `mnt/Desktop` in device_bash; use device_list_dir. `~/Downloads` works in device_bash.

**Shell:**
- `pkill -f` / `pgrep -f` with the pattern in the same command matches its own bash. Use a separate call.
- Background `setsid` jobs don't survive; run in the foreground with a timeout.

**Writing rules (V5):**
- No commander-voice openers (Rule 12).
- Avoid parentheses and semicolons; no more than two em-dashes per track.
- Track lengths, in words: R 180–280, W 250–360, ANCHOR / CLOSE 250–360, merged tracks (047, 048, 062, 078) 220–320.
- **Exception:** the calibration tracks 034 (330 words) and 070 (314 words) are deliberately kept over length.
- The QA snippet is in `v5/WRITER_BRIEF.md`.

**Working with Puneet:**
- He wants shipping, not narration. Give a short final summary.
- He wants to be told honestly what is unverified or untested.

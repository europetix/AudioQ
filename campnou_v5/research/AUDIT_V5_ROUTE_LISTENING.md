# AUDIT V5: ROUTE and LISTENING, FC Barcelona Museum at Spotify Camp Nou EN (34 tracks + 10 bridges), 14 Nov 2026

I'm an independent auditor. I did not write this guide, and I edited no track, bridge or plan. Navigation comes first, then how the guide sounds through a synthetic voice, then lengths. Facts belong to the facts audit; where I noticed a fact as it is *heard*, I pass it on (N14).

**What I read:**
- all 34 `v5/tracks/*.perf.txt` and the 4 bridge files (`v5/bridges/A–D.txt`, 10 bridges);
- `v5/PLAN.md` in full: §1 (user and lead decisions, Conventions, sections, route, ALT cues, lint), §2 (every row's @room, @title, content, Ending and cue), §3 (aims, walking, counts, playing orders, bridges, version-neutral sentences, safe callbacks, one home per story), §4 NEVER, §5–§8, and **both lead's-decision sections at the end, which I treated as overriding** (Highlights 6 and "about thirty-five minutes"; Essential 18 with 027; "Salid y disfrutad" allowed once in 008; Maradona's Bernabéu ovation in; no anthem lyrics; no Sunyol box; Les Corts "tens of thousands");
- `v5/SKELETON.md` decisions 1–15; `v5/V5_AUDIO_STANDARD.md`; `v5/WRITER_BRIEF.md`; `v5/ONSITE_CHECKLIST.txt` (O-items and per-track ticks);
- `research/VISIT_ROUTE_AND_SPACES_NOV2026.md` (§0–§8: spaces S0–S10, O1–O13, the works state) and `research/map/OFFICIAL_ACCESS_MAP_NOTES_14NOV2026.md` with the campus-map zoom (`official_campus_map_1C_mar2026_museum_corner.png`: the trophy icon on the ridged building at Av. Joan XXIII / Arístides Maillol, Access 9 at it, 11/12 along it, the Palau Blaugrana beside it, the store and Sala París towards the main stand, Access 15 far along);
- `v5/lint.py` and `pipeline/v5_direction.py` (clean text, tags, silences);
- spot checks in `research/FACTS_NOV2026.md` and `FACTS_GAPS_NOV2026.md` where a line's status changed how it is heard (G38 Cruyff's Dutch-TV line, G36 the 26 games, G87–G88 the 1971 rink and arena, G96, G98, F8.11, F10.17, F16.5);
- the Barcelona Cathedral route-and-listening audit, as the model for format and depth.

**Method.**
- A script checked every cue's destination against the next track's @title in each version, and every bridge's key, opening, word count and closing title.
- I walked Full (34), Essential (18) and Highlights (6) in PLAN's default order, with each bridge played after its track's cue, on the building as MAP draws it. Then I re-walked each version under ALT-O3 (history before trophies; Messi before history), ALT-O2 (new museum open), ALT-O15 (no quiet corner) and ALT-O7.
- I counted words, sentence lengths, numbers, years, tags and repeated phrases on the clean text (tags stripped as `lint.py` does). **`lint.py` passes all 34 tracks.**

**Counts.** **MUST: 2** · **SHOULD: 19** (8 route, 11 listening) · **NICE: 19**.

**Verdict in one paragraph.** The route layer is careful and mostly right:
- Every cue's title matches the next track in all three versions. All 10 bridges open "On this shorter tour,", name the right next stop and end on its exact title (E 5: 001, 006, 009, 012, 024; H 5: 001, 008, 022, 024, 028).
- The Extras are offered to shorter versions only in 016 and 029, as "If you're on the full tour, … Otherwise, the next main stop is …"; the Full-only tracks announce the next Extra plainly. Every "needs no view" Extra keeps its look for the last paragraph.
- The 360° warning is in 001 and 024. There is no compass word, gate or access number, room number, directional distance, "next room", "upstairs" or "the Masia over there". No track sends anyone to the Masia, a statue, the store or into the stadium.
- 001 is honest in its first paragraph, warmly, and speaks exactly the lengths the lead decided.
- No E or H track recalls a track that version lacks.

Two things must change before recording:
- **M1.** The guide is 1,242 words over PLAN (9,562 against 8,320). Full now runs **≈ 102 minutes (≈ 106 with rendered silences)** against the "about an hour and a half" that 001 speaks. Twenty-one tracks are more than 10% over their aims.
- **M2.** At the show, the guide breaks PLAN's own rule that "stop the guide now" is the last instruction before the title. The body and the cue give two different stop moments. In E and H the bridge "now that the show is over" plays straight after the title, so anyone who lets the cue run to its end hears it *before* the show.

For listening, the voice is warm, the politics are even, and the hard moments (Gamper, Sunyol, Cruyff's death, the Pope) are well judged. The guide's tics are:
- "the club's own …" as the attribution in 11 tracks, with the club cited in about 20;
- tracks that open "On the [date]" (six, two pairs back to back);
- payoffs said twice inside one track (010, 028, 031, 034);
- six-digit numbers read out in full (45,157; 91,553 and 91,648; 672 in 778 against 643).

Several stories reach E listeners twice in near-identical words: the ice-rink move (001 → 006), and the kept bowl and the 105,000 (026 → 028). Four groups of tracks end on the same idea. E runs ≈ 65 against "about an hour"; H (≈ 34) is honest.

---

## 1. Track table

Words are clean words (as `lint.py` counts them) against the PLAN §3 aim. In = versions.

| # | In | Words / aim | Verdict | One line |
|---|---|---|---|---|
| 001 | H E F | 340 / 300 | SHOULD | Honest first paragraph ✓, the warning ✓, the lengths exactly as the lead decided ✓ (true for E and H; Full fails, M1). Its route line fixes an order O3 hasn't confirmed (R4). "the women's team that filled the stadium" is a fourth telling for E (L1c). |
| 002 | F | 291 / 260 | NICE | Strong hook and payoff ✓, look ✓, Gol Nord without a compass word ✓. "Forty-five thousand, one hundred and fifty-seven" (L7). "sixty-two thousand" comes again in 028 (L2c). |
| 003 | F | 245 / 190 | SHOULD | +29% (M1). "[wry] Temporary is a flexible word." ✓. A third square-metre figure within two tracks (L2f). |
| 004 | F | 333 / 260 | SHOULD | The opener is PLAN's word for word ✓, but it repeats 003's cue (L6). +28%. It adds a motto with a "you" that 032 ends on too (L4, L5). |
| 005 | F | 215 / 160 | SHOULD | +34%, the largest overrun with 017. "A writer who goes by the name Roger Vinton" is said again, word for word, in 017, and Conventions give Vinton to 017 only (L2e). |
| 006 | E F | 231 / 200 | SHOULD | E hears 001's ice-rink sentence again almost word for word (L1a). Its route line fixes the O3 order (R4). Its ending, "waiting to move house", is 001's and 034's idea (L4). |
| 007 | F | 214 / 180 | NICE | Eight numbers in the first two paragraphs (L7). "See if you can spot the pair" is soft enough for O16 ✓. The ending is PLAN's ✓. |
| 008 | H E F | 270 / 290 | NICE | Strong ✓. "Salid y disfrutad" is attributed to the club's history, as the revised decision 4 allows ✓; add it to the lexicon (§6). "Find the oldest of the five big cups" needs a condition (R7). |
| 009 | E F | 305 / 270 | NICE | Clear, with a good wry beat (Numancia). The look line restates the body's "a coach from the reserves", which is PLAN's Ending, so acceptable. |
| 010 | F | 268 / 250 | SHOULD | Its payoff "Four European Cups in ten years" is said two paragraphs earlier (L3). The black cat is a good touch ✓. |
| 011 | E F | 347 / 290 | SHOULD | +20%. 39 number words and 11 years. Two six-digit crowds back to back (L7). "Alexia added a third" is unclear by ear (L10). Q7 ending ✓. |
| 012 | E F | 257 / 250 | PASS | The look is conditional ✓, no sum ✓, "Spotify Camp Nou" once ✓. "And here's the turn" (N3). |
| 013 | F | 319 / 260 | SHOULD | +23%. Cruyff's "people were saying thank you" has no context for the ear (L10). The Bernabéu applause anticipates 033's payoff (L2g). "has said it plainly" (L9). |
| 014 | E F | 298 / 290 | NICE | The fourteenth minute is applause, not silence ✓, and the statue is DATED ✓. Its look needs a condition (R7). Its hook is a summary (N4). |
| 015 | E F | 320 / 270 | SHOULD | +19%. "And remember where most of them really lived. Most of the boys…" (N5). Its look needs a condition (R7). No direction to the Masia ✓. |
| 016 | E F | 352 / 270 | SHOULD | +30%, the largest overrun heard by E. The Extra announcement is right ✓. "the crest on any shirt here" may find no shirt (R7). Even-handed ✓. |
| 017 | F | 228 / 170 | SHOULD | +34%. Its opener repeats 016's cue (L6). It ends on "look at the people around you", and so does 018 (L4). |
| 018 | F | 353 / 260 | SHOULD | +36%, the largest overrun. Gamper's death is told gently ✓. Its ending repeats 017's (L4). Four club attributions (L9). It opens on a date, as 019 does (L8). |
| 019 | F | 290 / 260 | SHOULD | Tone right ✓, box cut ✓. Nine different years (L7). No "you" moment (L11). |
| 020 | F | 306 / 280 | NICE | Even-handed, with Madrid's own history and Franco's medals ✓. A quip after the motto (L5). "Ya" (N9). |
| 021 | E F | 269 / 250 | PASS | The napkin lines are exactly as lint requires ✓, Rexach is attributed ✓, and "What you will find is what came after it" is a good turn. |
| 022 | H E F | 279 / 280 | SHOULD | The version-neutral lines are present ✓. Three three-digit numbers in two sentences (L7). Two mottos in a row (L3). |
| 023 | E F | 267 / 260 | PASS | The debut correction is right ✓, the No 10 is DATED and separate ✓, and the look is conditional ✓. |
| 024 | H E F | 197 / 180 | **MUST** | The warning is correct ✓. It has two different stop instructions, and the E/H bridge can play before the show (M2). "where the exhibition ends" is said for the third time in E (L1d). |
| 025 | F | 234 / 190 | SHOULD | +23%. Even about the anthem ✓. "first of thousands" without a number ✓. |
| 026 | E F | 288 / 260 | SHOULD | 028 repeats its kept-bowl and 105,000 sentences almost word for word for E (L1b). It names 030's architects (L2b). It ends on the 1957 bowl, as 028 and 030 do (L4). |
| 027 | E F | 251 / 210 | SHOULD | +20%. Five big numbers (L7). "socis" once ✓. No bridge is needed after it in E (R6). |
| 028 | H E F | 293 / 280 | SHOULD | The hook and the payoff are the same sentence (L3). "Now look right at the top" (L10). L1b. The version-neutral lines are present ✓. |
| 029 | E F | 343 / 260 | SHOULD | +32%, heard by E. Its cue's "need nothing to look at" is repeated by 030's opener (L6). "something stranger happened" (N11). |
| 030 | F | 299 / 250 | SHOULD | +20%. The opener is PLAN's word for word ✓. "tens of thousands, and still not enough" comes again in 031 (L2a). Ends on the 1957 concrete (L4). |
| 031 | F | 330 / 250 | SHOULD | +32%. The correction is said three times (L3). Les Corts is repeated from 030 (L2a). The Five Cups as G64 gives them ✓. |
| 032 | F | 185 / 170 | NICE | No lyrics ✓ and no Montal ✓. "doesn't matter where you come from" is 004's added ending (fix in 004, L4). |
| 033 | F | 286 / 260 | SHOULD | The Maradona ovation is in, per the lead ✓. No "you" moment (L11). It opens on a date, as 032 does (L8). |
| 034 | H E F | 259 / 260 | SHOULD | The recap is self-contained for H ✓. It says "follow the signs for the way out" to people already at the way out (R3). The payoff is said twice (L3). |

**Bridges (10).**
- All open "On this shorter tour,".
- The keys are right after the lead's decision 11: E 001>006, 006>008, 009>011, 012>014, 024>026; H 001>008, 008>022, 022>024, 024>028, 028>034.
- There is no 026 E bridge, correctly, because 027 now follows it. There is also no 027 E bridge, and none is needed: 027's own cue already goes to 028 in the same words (R6).
- All end on the target's exact title. They run 18–32 words before the title (PLAN: 15–45).
- Both 024 bridges open "now that the show is over" ✓. None says "for now", "come back" or "later" ✓. None names skipped content ✓.
- Problems:
  - 024 E/H timing (M2);
  - 024 H uses "the way out", which is the exit's fixed name (R2);
  - no [O#] tags anywhere in the bridge files (R6);
  - 008 H, 022 H and 024 E/H follow cues that promise more at the same spot, without "instead" (R6).

---

## 2. Findings

### MUST

**M1. Full runs ≈ 102 minutes (≈ 106 with rendered silences) against the "about an hour and a half" spoken in 001.**
*Exact words (001):* *"The full tour takes about an hour and a half, the essential about an hour, and the highlights about thirty-five minutes, walking and the show in the round room included."*

*Problem:*
- Full is **9,562 words against PLAN's 8,320** (+1,242, +9.9 min of listening). With PLAN §3's 25.6 min of walking, show and looking, that makes **≈ 102 min**. The pipeline's own silences (0.75 s per paragraph, 0.55 s per [pause], 2 s tail) add 4.3 min, for **≈ 106**. A 20-minute wait for the show makes it ≈ 122.
- That is 13–18% over the spoken length. The user's binding instruction is "honest length stated", and SKELETON decision 15 says "If Full can't be 90 honestly, say so". PLAN §3: "Over by more than 10% → the lead cuts."
- **21 tracks are more than 10% over their aim**:

  | Track | Words / aim | Over | | Track | Words / aim | Over |
  |---|---|---|---|---|---|---|
  | 018 | 353 / 260 | +36% | | 007 | 214 / 180 | +19% |
  | 005 | 215 / 160 | +34% | | 015 | 320 / 270 | +19% |
  | 017 | 228 / 170 | +34% | | 006 | 231 / 200 | +16% |
  | 029 | 343 / 260 | +32% | | 001 | 340 / 300 | +13% |
  | 031 | 330 / 250 | +32% | | 009 | 305 / 270 | +13% |
  | 016 | 352 / 270 | +30% | | 002 | 291 / 260 | +12% |
  | 003 | 245 / 190 | +29% | | 019 | 290 / 260 | +12% |
  | 004 | 333 / 260 | +28% | | 026 | 288 / 260 | +11% |
  | 013 | 319 / 260 | +23% | | 011 | 347 / 290 | +20% |
  | 025 | 234 / 190 | +23% | | 027 | 251 / 210 | +20% |
  | 030 | 299 / 250 | +20% | | | | |

- The ten Extras alone come to 2,825 words (22.6 min), against PLAN's 2,320 (18.6).
- E (≈ 65) is also over; see R5. H (≈ 34) is honest.

*Fix, in three steps (all figures by script):*
1. **Take the listening cuts in this report** (L1–L11, R3, N-items). They are all repeats, tics, optional or DATED lines: **≈ −370 words**. Full ≈ 99, E ≈ 64, H ≈ 34.

   | Track | Cut (exact words) | Words |
   |---|---|---|
   | 004 | *"Wild lent his flat on Carrer Princesa for the board's meetings, and played in ten matches, the very first among them."* · *"If you've come from somewhere else to stand here today, you're in good company."* (L4) | −35 |
   | 029 | *"Spain won it again in Paris, thirty-two years later, with three more Barça players: Fermín López, Eric Garcia and Pau Cubarsí."* (DATED-light, cuttable per the lead) · *"He was also given a Barça membership card, and he said so himself, years later."* | −36 |
   | 016 | *"Barcelona is more than a place of leisure where we go to watch the team play every Sunday."* (end the quote at "football club.") · *"Those are her words, and her reading of it."* | −26 |
   | 003 | *"A few of their greats have had their shirts retired there."* · *"A new arena is planned on another part of the campus."* (optional, DATED) | −22 |
   | 013 | *"Later, on Dutch television, Cruyff said: 'I was surprised that instead of congratulating us on the win, people were saying thank you.'"* (L10) | −22 |
   | 031 | *"It wasn't built for him."* (L3) · *", the work of the sculptor Montserrat Garcia Rius"* · the Les Corts rewrite (L2a) | −20 |
   | 005 | *"And a writer who goes by the name Roger Vinton points out that Basel plays in blue and red."* (L2e) | −19 |
   | 018 | last paragraph rewritten (L4) | −18 |
   | 034 | *"From here, follow the signs for the way out."* (R3) · *"And every time, it has found its way back."* (L3) | −18 |
   | 011 | *"A year later they lost the final to Arsenal, in Lisbon, by a single goal."* and the crowd rewrite (L7) | −21 |
   | 027 | *"Around the world there are also about twelve hundred and seventy official supporters' clubs, on all five continents."* | −17 |
   | 025 | *"Three years later he became the first player to score five in one game there."* | −15 |
   | 022 | *"in seven hundred and seventy-eight matches"* · *"Two great clubs, level on gold."* | −12 |
   | 019 | the absent-president years (L7) | −12 |
   | 017 | *"One of them stood where the Hospital de Sant Pau stands today."* (optional) | −12 |
   | 024 | *"And this is where the exhibition itself comes to an end."* (L1d) | −11 |
   | 006, 010, 015, 026, 030, 007, 001, 002 | L1a, L3, N5, L2b, *"The members had even endorsed it in a referendum."*, *"And there are sixteen Spanish Super Cups."*, L1c, L7 | ≈ −55 |

2. **Bring every track to within 10% of its aim** (≈ −290 more words, mostly 018 −49, 031 −33, 017 −29, 016 −28, 029 −21, 005 −20). Then **apply PLAN §3's own "if it comes in longer" rule: drop the Extras 005 and 017**, with 004's cue taking 005's cue text and 016's Extra sentence naming 018 as "the next three stories". **Full ≈ 93.5 (≈ 97 with silences)**, which "about an hour and a half" can honestly carry until O21.
3. **If the lead keeps every Extra**, 001 must say *"The full tour takes about an hour and three quarters, …"* (word-neutral), until O21's stopwatch says otherwise.

**M2. 024: two different moments to stop the guide, and in E and H the "now that the show is over" bridge can play before the show.**
*Exact words:*
- 024 body: *"The show has its own sound, so this guide will step aside while it plays. Stop it when the show begins, and start it again when the show ends."*
- 024 cue: *"Go in when the staff let you, and stop the guide now. When the show ends, press play again before you leave the room: The round room · After the show: the first full house."*
- Bridge 024 E: *"On this shorter tour, now that the show is over, follow the way out of the room to the models of the finished stadium: …"*
- Bridge 024 H: *"On this shorter tour, now that the show is over, follow the way out to the viewpoint over the works, …"*

*Problem:*
- PLAN §1 Conventions are binding: *"'stop the guide now' is the last instruction before the title; the next audio heard (025 in F, a bridge in E/H) is heard after the show."* The track puts a second instruction after it ("press play again"). This is PLAN §2's own cue text, so PLAN contradicts itself, but the convention is the one that protects the listener.
- The body says to stop "when the show begins". The cue says to stop "now", at the door. The listener gets two different stop moments within twenty seconds.
- A listener who stops at "now" is fine. A listener who lets the sentence finish (the natural thing, since it is still giving an instruction) hears the title and then, in E and H, the bridge, *before* going in. They hear "now that the show is over" before it starts, and the route to the next stop ten or more minutes early. After the show, pressing play starts 026 (E) or 028 (H) with no direction.
- This is the one stop every version must get right: 024 is never-skip and carries the safety warning. In H the next stop is the viewpoint, a different place.

*Replacements (word-neutral):*
- 024 body: *"The show has its own sound, so this guide will step aside while it plays. Stop it before you go in, and start it again when the show ends."*
- 024 cue: *"When the show ends, press play again before you leave the room. Now go in when the staff let you, and stop the guide here: The round room · After the show: the first full house."*
- Rendering: play each 024 bridge as its own clip, or with at least 3 s of silence after the title, and never auto-continue it.
- ONSITE O11: add *"Play 024 E/H through without stopping: does the bridge start before the doors open? Time the gap."*
- Update PLAN §2's 024 cue to the same order, so ES, FR and DE follow it.

### SHOULD (route and placement)

**R1. ALT-O15 option 1 (the default if there's no quiet corner) leaves three recorded cues pointing the wrong way.**
*Exact words:*
- PLAN ALT-O15: *"Option 1 (default): 017–020 play at the old benches, before 030 … 016's Extra sentence then goes; 029's announcement becomes 'the next eight stories'."*
- 029 cue: *"…: The old benches · Extra · The stadium the nickname named."*
- 020 cue: *"Now walk on to Messi's space, the room with his golden balls, and stop at its way in: Messi's space · A promise on a paper napkin."*
- 018: *"Look around you at the people in this museum."*

*Problem:*
- Under option 1, the bench cluster becomes 029 → 017–020 → 030–033, but:
  - 029's Extra title must change to 017, whose fixed place name is "A quiet corner", heard while sitting on "the old benches";
  - 020's cue would send Full listeners from the viewpoint *back* to Messi's space, the one double-back the route can't afford, instead of on to 030;
  - 018's "the people in this museum" is wrong outdoors (L4's rewrite fixes it).
- O15 is CRITICAL in ONSITE, so the fallback is likely to be used. The cue chain in the default order is sound: every display cue is a "find …" or "When you reach …", and "the big silver European Cups, the tall trophies with the big handles" is the best recognition line in the guide.

*Fix:* add to ALT-O15 option 1:
- 029's Extra clause → *"…: A quiet corner · Extra · Backsides on a wall"*. Better, retitle 017–020's place to "The old benches" in that case.
- 020's cue → 030's title, with *"Stay on the benches for the stadium's own name: The old benches · Extra · The stadium the nickname named."*
- 016's E/F cue keeps only its "Otherwise" sentence.

**R2. Bridge 024 H: "follow the way out" is the exit's fixed name.**
*Exact words:* *"On this shorter tour, now that the show is over, follow the way out to the viewpoint over the works, and find a place at the rail: The viewpoint · What you're looking at."*

*Problem:*
- "The way out" is the fixed place name of 034 (PLAN Conventions). H listeners hear it again two stops later, in the 028 H bridge (*"follow the signs for the exit: The way out · …"*).
- Straight after the show, "follow the way out" can be heard as "follow the exit signs". That is the one move that skips the viewpoint (028, never-skip) for the version that has the fewest landmarks.
- The E bridge and 025's cue say "the way out **of the room**", which is safe.

*Replacement:* *"On this shorter tour, now that the show is over, leave the room and follow the way on to the viewpoint over the works, and find a place at the rail [O4, ALT-O4]: The viewpoint · What you're looking at."* (+3) The same wording goes into PLAN §3's table.

**R3. 034 tells people who are already at the way out to follow the signs for the way out.**
*Exact words:*
- 029 and 033 cues: *"follow the signs for the exit: The way out · A club that keeps coming home."*
- 034 @where: *"At the exit of the visit, or just outside it"*.
- 034 body: *"[lightly] It has packed up and moved, again and again. And every time, it has found its way back. / From here, follow the signs for the way out. / A club that keeps leaving home, and keeps coming back."*

*Problem:*
- The listener is told to go to the exit, then told at the exit to follow the signs to it. It reads as "you're in the wrong place".
- The direction also sits between the build-up and the payoff, which breaks the close (see L3).
- O7 is open: the exit may run through the store, onto the campus, or back past the viewpoint. ALT-O7 already holds the neutral line for each case.

*Fix:* cut *"From here, follow the signs for the way out."* (−9). Add the ALT-O7 line only after O7, before the recap, never between the last two sentences.

**R4. ALT-O3: 001's and 006's route lines state a fixed room order, and ALT-O3 gives them no replacement.**
*Exact words:*
- 001: *"Then in, to the trophies, the history, Messi's space, the round room and its show, the models, the viewpoint, and out."*
- 006: *"From this hall, the trophies come first, then the club's history, then Messi's space, and finally the round room, where the exhibition ends."*

*Problem:*
- ALT-O3 (a) and (c) re-route the cues (006 → 013, 012 → 021, 023 → 013 …) but say nothing about these two body lines. ONSITE ticks them, but there is no replacement text. Under (a), every E and F listener hears "the trophies come first" and is then sent to Cruyff.
- Both lines can be made order-neutral now, so they survive O3 without re-recording, which is the point of decision 3.

*Replacements:*
- 001: *"Then in, through the trophies, the club's history and Messi's space, to the round room and its show, then the models, the viewpoint, and out."* (+1)
- 006: *"From this hall, the exhibition takes you through the trophies, the club's history and Messi's space, and ends in the round room."* (−4)
- Add both to ALT-O3 as "no change needed".

**R5. Essential runs ≈ 65 (≈ 68 with silences) against "about an hour".**
- E is 5,166 track words + 174 bridge words = 5,340. PLAN's aims with 027 give ≈ 4,845. E listening is 42.7 min, plus PLAN's 22.7 min of walking, show and looking, for **≈ 65.4**.
- The lead accepted ≈ 62 as "about an hour" (decision 11). The excess is in four E tracks: 016 (+82), 029 (+83), 011 (+57) and 015 (+50).
- M1 step 1 gives E ≈ 64. Bringing 016 and 029 within 10% gives ≈ 63, which is acceptable. If O21 is longer, PLAN's own next E cut is 012 (−2.0).

**R6. Bridge hygiene.**
- **No [O#] tags in any bridge file.** PLAN §3: "Every bridge inherits its cue's [O#] tags", and ONSITE re-checks bridges by them. Add a `#` comment line above each bridge with its tags, for example `# 024 H>028 [O4, O11, ALT-O4]`, so that the renderer never sees a bracket.
- **"instead" is used only in the two 001 bridges.** The cues before 008 H, 022 H and 024 E/H promise more at the same spot (*"Stay at the European Cups, and find the next two, from Paris and from Rome"*; *"Stay in Messi's space for how his time here ended, and who wears his number now"*). The bridge then says "walk on" with no word that cancels the promise. Add "instead":
  - 008 H: *"On this shorter tour, walk on instead, through the museum to Messi's space, …"*
  - 022 H: *"On this shorter tour, walk on instead to the round room with the screens, …"*
  - 028 H already says "stay at the rail", which works.
- **Decision 11's "027 E → 028 takes 026's old E bridge text"** was correctly not written: 027's own cue goes to 028 in the same words, and a bridge would repeat it. Strike the line from PLAN §3 and the lead's decision 11 so the translators don't add one.

**R7. Looks that are not yet conditional on O12, O16 and O16's labels.**
*Exact words:*
- 008: *"Find the oldest of the five big cups. That's the one from Wembley, and every one beside it came after it."*
- 014: *"Look at the Dream Team's photographs or shirts here, then think of that ground"*
- 015: *"Find the farmhouse in the photographs here"*
- 016: *"Now look at the crest on any shirt here."*

*Problem:*
- 008's @where says "if they stand in order", but the spoken line doesn't. Without year labels nobody can find "the oldest", and H has nothing else to look at in 008.
- O12 has not confirmed a Dream Team display or a farmhouse photograph.
- 016 is often heard at "any quiet spot in the history space" (its own @where), where there may be no shirt at all.

*Replacements:*
- 008: *"If the cups are labelled, find the one from 1992. That's Wembley, and every one beside it came after it."*
- 014: *"If the Dream Team's photographs or shirts are here, look at them, then think of that ground: …"*
- 015: *"If the farmhouse is in the photographs here, find it: a farmer's house that ended up as a football school."*
- 016: *"Now look at the crest on any shirt you can see, even one a visitor is wearing."*

**R8. 033 and 019 have no "you" moment, and 033's first line could give them one.** (Listening and placement together.)
- The standard asks for one clear "you" moment per track. Extras put it in the last paragraph. PLAN says 019 and 033 need no last look, but a "you" needs no view.
- 033: *"Nine days later, the World Cup opened in this stadium."* → *"Nine days later, the World Cup opened in the stadium in front of you."* (+3)
- 019: *"He was president for about a year, and the club has no grave to visit."* → *"He was president for about a year, and there is no grave you can visit."*

### SHOULD (listening)

**L1. The same fact twice, heard in E (and H where marked).**

| | Exact words | Heard by | Fix |
|---|---|---|---|
| a | **The move into the ice rink.** 001 *"was the club's old ice rink. The museum moved in while the stadium is being rebuilt."*; 006 *"In 2023 the museum moved into the club's old ice rink, while the stadium is rebuilt."* | E (three minutes apart); F a third time in 003 | 006's sentence was planned as version-neutral because E skips 003, but 001 already gives it to every version. 006: *"Since June 2023 it has been here, and over a million visitors came in 2025."* (−9; DATED clause kept) |
| b | **The kept bowl and 105,000.** 026 *"Its bottom two tiers, the ones poured in the 1950s, were kept and renovated… Only the third tier, the top ring, was taken down and built again."* + *"When it's finished, the club expects about a hundred and five thousand seats."*; 028 *"The two lower tiers in front of you are the bowl that opened in 1957, kept and renovated. Above them, the third tier is the part that was taken down and built again."* + *"When everything is finished, the club expects about a hundred and five thousand seats."* | E, F (four minutes apart, one track between) | 028 must stay self-contained for H, so change its shape rather than its facts. 028: *"Start low. [pause] The two lower tiers in front of you are the 1957 bowl, kept. Above them is the rebuilt third tier: built, but not yet open to fans."* and fold 105,000 into the Montjuïc paragraph: *"…for Montjuïc, the Olympic stadium on the hill. When they come back for good, it should hold about a hundred and five thousand."* |
| c | **The women's crowds, four times.** 001 *"the women's team that filled the stadium"*; 011 (home); 029 *"Barça's women filled it twice in a month, with world-record crowds"*; 034 *"its women's team filled the stadium with the biggest crowds women's football had ever seen"* | E four times; H twice (001, 034) | 001: *"…from a classified ad in a newspaper to the women's team."* (PLAN's own wording, −4). 029 and 034 are PLAN's one clause each. |
| d | **"Where the exhibition ends", three times.** 006 *"finally the round room, where the exhibition ends"*; 023 cue *"the round room with the screens, where the exhibition ends"*; 024 *"And this is where the exhibition itself comes to an end."* | E (H twice: bridge 022 H, 024) | Cut 024's sentence (−11). The cue and 006 do the job. |

**L2. The same fact twice, Full only.**

| | Exact words | Fix |
|---|---|---|
| a | **Les Corts, back to back.** 030 *"It held twenty-two thousand at first, then tens of thousands, and still not enough."*; 031 *"What he did do was fill Les Corts, the old ground. It held tens of thousands, and it still wasn't enough."* | 031: *"What he did do was fill Les Corts, the old ground, to bursting."* (−8; the lead's "tens of thousands" wording stays in 030, its home). |
| b | **The architects, twice.** 026 *"…the canopy that the original architects, Francesc Mitjans, Josep Soteras and Lorenzo García, designed for the stadium of 1957"*; 030 *"The architects were Francesc Mitjans and Josep Soteras, with Lorenzo García-Barbón."* (and the surname differs: "García" against "García-Barbón") | 026, as PLAN's row has it: *"…inspired by the canopy the original architects designed for the stadium of 1957."* (−8). 030 is the home. |
| c | **Sixty-two thousand, twice.** 002 *"Since March 2026, it has held about sixty-two thousand."*; 028 *"Today the stadium holds about sixty-two thousand people."* | PLAN gives both. Optional: cut 002's sentence and keep the Gol Nord line as *"In March 2026 the Gol Nord, the stand behind one goal, opened again."* |
| d | **Gamper introduced three times.** 004 *"Hans Gamper, from Winterthur in Switzerland, living in Barcelona since the late 1890s"*; 006 *"a young Swiss called Joan Gamper"*; 018 *"Joan Gamper had come to Barcelona from Switzerland in the late 1890s, and he had been the club's president five times."* | 018: *"Gamper had been the club's president five times."* (−11; the Extra still makes sense alone). |
| e | **Roger Vinton, word for word.** 005 *"And a writer who goes by the name Roger Vinton points out that Basel plays in blue and red."*; 017 *"A writer who goes by the name Roger Vinton searched the archives…"* | Conventions: *"'a writer, Roger Vinton' ([S6], 017 only)"*. Cut 005's sentence (−19). In 017, *"A writer, Roger Vinton, searched the archives…"* ("goes by the name" suggests a pseudonym the sources don't state). |
| f | **Three floor areas in two tracks.** 003 *"about two thousand four hundred square metres"*; 006 *"nine hundred and fifty square metres"*, *"three thousand six hundred square metres"* | 006: *"…in a space under the main stand."* and *"It kept growing, to almost four times that size by 2010."* (our arithmetic: 3,600 / 950 ≈ 3.8). |
| g | **Madrid's applause, before its payoff.** 013 *"The image I remember most is the Bernabéu fans applauding us as we went into the dressing room."*; 033's payoff *"Two players in Barça's shirt, twenty-two years apart, and two Madrid crowds on their feet."* | The lead keeps Asensi in 013 (one home). It is the team, not a player, so 033's "two" stays true. Keep, but drop Cruyff's line after it (L10) so that 013 doesn't end its Madrid paragraph on a second compliment. |

**L3. Payoffs said twice inside one track.**
*Exact words:*
- 010: *"Catalan News counted it as the club's fifth European Cup, and its fourth in ten years."* … *"[warmly] Four European Cups in ten years."*
- 028: hook *"You are looking at a stadium that keeps playing matches while it's being finished."* … payoff *"A stadium being finished while it's being played in."*
- 031: *"The club's own historians say no: the plans were in place before he signed."* … *"It wasn't built for him. It was built for crowds like the ones he drew."* … *"He didn't build it. He filled the one before."*
- 034: *"It has packed up and moved, again and again. And every time, it has found its way back."* … *"A club that keeps leaving home, and keeps coming back."*
- 022: *"Two great clubs, level on gold."* followed by *"Six won in these colours. Eight on the shelf."*
- 029: *"But the stadium in front of you was never only the club's."* … *"It has always been the city's stage, as much as the club's."* (NICE: it frames the track)

*Problem:* a payoff lands only if the listener hasn't just heard it. In 028 and 034, the two tracks every version hears, the motto is said twice within a minute.

*Fixes:*
- 010: *"Catalan News counted it as the club's fifth European Cup."* (−6)
- 028: open *"The team has been playing here again since November 2025, and the builders never left."* (version-neutral clause kept). Drop the second sentence.
- 031: cut *"It wasn't built for him."*. The look becomes *"Look at the stadium in front of you. It was built for crowds like the ones he drew."*
- 034: cut *"And every time, it has found its way back."* (−9). The payoff then answers *"It has packed up and moved, again and again."*
- 022: cut *"Two great clubs, level on gold."* (−6). The respectful line is already *"exactly the same number as Real Madrid"*.

**L4. No two tracks may end on the same idea (decision 7). Four pairs do.**

| Idea | Tracks (last story lines) | Heard by | Fix |
|---|---|---|---|
| "Look at the people around you" | 017 *"look at the people around you in the club's shirts. Culers, every one of them."*; 018 *"Look around you at the people in this museum. The club didn't die."* | F, back to back | 018's last paragraph: *"[pause] The dictatorship that closed it is long gone, and so is the founder. You're standing in the museum of the club he said could not die."* (−18; keeps a "you" and "cannot die"). Cut *"A hundred years on, in 2025, the club marked the day…"* (optional in PLAN). |
| The 1957 bowl inside the new one | 026 *"That curve is the same bowl that opened in 1957, inside the new one."*; 028 *"the old bowl low down, the new ring above it, and open sky where the roof will be"*; 030 *"Now look at the lower tiers in front of you. That concrete is the new ground of 1957."* | E 026 + 028; F all three | 028 is the home of what you see, so it keeps the bowl. 026 ends on the model instead: cut *"Then look past the new shell, at the curve of the lower tiers. That curve is the same bowl that opened in 1957, inside the new one."* and end *"…and the skin wrapped round the outside. All of it has to go up around a stadium that never stops playing."* (no pointer to 028, so it stays safe for ALT-O5). 030 ends on the name: *"Now look at the stadium in front of you, and say its name. The nickname won."* |
| Moving house | 001 *"This is a club that has moved house more than once."*; 006 *"So the museum you're standing in is itself waiting to move house."*; 034 payoff | E all three | 001 → 034 is PLAN's set-up and answer. 006 ends on its fact without the motto: *"[wry] For now, even the museum is a visitor here."* Or end on the route line. |
| "It doesn't matter where you come from" | 004 *"If you've come from somewhere else to stand here today, you're in good company."*; 032 *"The song itself, in Catalan, says that it doesn't matter where you come from."* | F | 004's added line is not in PLAN, and it is also a motto outside the payoff list (L5). Cut it (−14). 004 then ends on PLAN's Ending: *"So it was a club named for its city, by men from somewhere else."* |

**L5. Mottos outside PLAN's eleven payoff tracks.** The eleven listed payoffs are all present (002, 008, 010, 012, 015, 022, 028, 030, 031, 033, 034) ✓. Three tracks add a motto anyway:
- 004 (see L4);
- 006 (see L4);
- 020: after PLAN's last line, *"[lightly] Both cities still tell this match differently."*, it adds *"So if you ever hear someone say eleven–one, it's worth asking which city they're from."*. This is light after Franco's medals, and it is a second ending. NICE if kept: it is the track's only "you" moment.

**L6. The Extras' openers repeat the cue the listener has just heard.**
*Exact words:*
- 003 cue *"Stay by the door for two short stories. You can hear them here, or in the queue if there is one"* → 004 *"You can listen to this one in the queue, or standing anywhere by the door."*
- 016 cue *"find a bench or a quiet corner away from the screens. The next four stories need nothing to look at until their last lines"* → 017 *"This one needs nothing to look at, so find somewhere to lean or sit."*
- 029 cue *"stay on the benches. The next four stories need nothing to look at until their last lines"* → 030 *"Sit, if there's room: you won't need to look at anything until the end."*
- Also "if there's room" three times in about four minutes: 028 cue, 029 body, 030.

*Problem:* the opener exists so that an Extra works when played anywhere. Played in order, Full listeners hear the same instruction twice within ten seconds. PLAN made both (cue and opener), so fix it in the cue, which E also hears and doesn't need at that length.

*Fixes:*
- 003 cue: *"Stay by the door for two short stories, here or in the queue if there is one: …"*
- 016 cue: *"If you're on the full tour, find a bench or a quiet corner away from the screens, for four short stories: A quiet corner · Extra · Backsides on a wall. Otherwise, …"*
- 029 cue: *"If you're on the full tour, stay on the benches for four more stories: The old benches · Extra · …. Otherwise, …"*
- The openers stay as written. 030: drop "if there's room" (*"Sit back: you won't need to look at anything until the end."*).

**L7. Numbers too dense to take in by ear.**
- 002: *"Forty-five thousand, one hundred and fifty-seven people were let in…"* → *"More than forty-five thousand people were let in…"*
- 011 (39 number words, 11 years):
  - five finals in one paragraph (2021 Gothenburg, 2023, 2024 Bilbao, Lisbon "a year later", 2026 Oslo);
  - then *"ninety-one thousand, five hundred and fifty-three"* and *"ninety-one thousand, six hundred and forty-eight"* in consecutive sentences.
  - Fix: cut the Lisbon sentence (−15). Then: *"On the thirtieth of March, 2022, more than ninety-one thousand people watched them play Real Madrid at the Camp Nou. Twenty-three days later, against Wolfsburg, even more came: ninety-one thousand, six hundred and forty-eight."* The title's number is said once, in full, as the climax.
- 022: *"Six hundred and seventy-two goals in seven hundred and seventy-eight matches for this club. That's more than Pelé's six hundred and forty-three for Santos…"* has three three-digit numbers in two sentences, right after six years in a row. Fix: *"Six hundred and seventy-two goals for this club: more than Pelé scored for Santos, and the most anyone has scored for one club."* (−9; F10.9's comparison kept without a third number).
- 027: 150,000 members; 1,270 supporters' clubs; 625 to 49; 114,000; 50,000. Fix: cut the supporters' clubs sentence (−17). Keep the rest.
- 019: nine different years (1898, 1935, 1936, 1937, 1939, 1996, 2010, 2022, 2026). Fix: *"From late 1937, its board named him the absent president, and it went on calling him that until the start of 1939."* → *"For the rest of the war, the board called him the absent president."* (−12)
- 007: eight numbers in two paragraphs (100, 25, 50, 29, 32, 1910, 5, 16). Cut the Super Cups sentence (optional in PLAN, −7).

**L8. Six tracks open on "On the [date]", two pairs back to back.**
*Exact words:*
- 002 *"On Saturday the twenty-second of November, 2025, Barça came home."*
- 016 *"On the 17th of January 1968, a new president took office…"*
- 018 *"On Sunday the 14th of June, 1925, Barça played a friendly at Les Corts…"*
- 019 *"[quietly] On the 6th of August, 1936, three weeks into the Spanish Civil War…"*
- 032 *"[warmly] On the twenty-seventh of November 1974, the club turned seventy-five."*
- 033 *"On the 4th of June 1982, Barça signed Diego Maradona…"*
- (and 004's second paragraph)

*Fixes (the pairs first):*
- 019: *"[quietly] Three weeks into the Spanish Civil War, on the 6th of August 1936, the president of FC Barcelona drove…"*
- 033: *"Barça signed Diego Maradona, then the most expensive footballer in the world, nine days before the World Cup opened in the stadium in front of you. That was June 1982. His Argentina…"* (adds R8's "you").
- 016 (optional): *"Barcelona is more than a football club. A new president said so, in Catalan, on the 17th of January 1968…"*

**L9. Attribution tics.**

| Tic | Count | Where |
|---|---|---|
| "the club's own …" as a source (account, history, story, explanation, centenary history, words, count, report, description, historians) | 11 tracks, 14 times | 004, 008 ×2, 014, 015, 017, 018 ×2, 022, 023, 024, 031 |
| the club as the source in any form | ≈ 20 tracks (PLAN: "The club says" at most in 10) | 018 has four in one track: *"the club's own centenary history reads"*, *"In the club's own words"*, *"The club's history pages give his words"*, *"The club's history says it was probably…"* |
| "said it plainly / puts it simply / put it simply / put it this way" | 4 | 013, 004, 028, 016 |
| signposts | 2 | 012 *"[wry] And here's the turn."*, 028 *"[amused] Here's the part nobody planned for."* |

*Replacements:*
- 008: *"The club's own account adds that the goalposts were square in those days."* → *"The goalposts, the club's archive adds, were square in those days."*
- 008: *"The club's own history keeps one detail from the dressing room."* → *"One detail survives from the dressing room."* (the next sentence says *"it says"*: make it *"the club's history says"*).
- 018: *"…and the club's own centenary history reads the whistles as a protest against that regime."* → *"…and the club's centenary history reads the whistles as a protest against it."* (also removes "regime" from a 1925 track; see lint). *"The club's history says it was probably because of those business problems…"* → *"Probably, the same history says, because of those business problems…"*
- 015: *"The club's own story says they could see…"* → *"They could see the pitch from their bedroom windows, the club's archive says."* (also matches PLAN's "pitch" and the payoff's).
- 013: *"Jordi Cruyff has said it plainly:"* → *"Jordi Cruyff tells it himself:"*.
- 004: *"A Catalan encyclopedia puts it simply:"* → *"A Catalan encyclopedia gives the reason:"*.
- 012: cut *"And here's the turn."* and start *"[wry] It was Barça that paid UNICEF…"*.

**L10. Lines that are hard to follow by ear.**
- **013, Cruyff:** *"Later, on Dutch television, Cruyff said: 'I was surprised that instead of congratulating us on the win, people were saying thank you.'"*
  - Problem: who were "people", and why thank you? The sentence before is about Madrid fans, so the ear takes "people" as them. The real meaning (Catalans thanking the team after the 0–5, in 1974) is never said. G38 allows the quote, but heard cold it is a puzzle.
  - Fix: cut it (−22). If kept: *"Back in Barcelona, Cruyff later said on Dutch television, people didn't congratulate them. They said thank you."* (paraphrase, no quotation marks unless RC).
- **011:** *"Alexia and Aitana have won the Ballon d'Or five times between them as Barça players, and in 2026 Alexia added a third."*
  - Problem: "a third" what, after "five"? The listener can't do the split.
  - Fix: *"Between them, Alexia and Aitana won the Ballon d'Or five times as Barça players. In 2026, Alexia won her third."* (F12.9's safe wording kept; DATED).
- **028:** *"Now look right at the top, at the ring that runs all the way round."*
  - Problem: heard as "look right", a direction without an [O#] tag.
  - Fix: *"Now look up to the very top, at the ring that runs all the way round."*
- **028:** *"Its last piece went in in October 2026."*
  - Problem: "in in".
  - Fix: *"Its last piece was fitted in October 2026."*

**L11. Opening and tone notes the lead should hear before render** (one item; each is small):
- 029 *"That November, something stranger happened. [quietly] Pope John Paul the Second said Mass here…"*: "stranger" sits oddly before a papal Mass heard [quietly]. → *"That November, the stadium held something else entirely."*
- 024 opens on PLAN's mandated *"The club gives one warning for the room ahead."* ✓, but the warning paragraph and the sound paragraph give two stop moments (M2).
- 014 opens on a summary (*"Johan Cruyff had already been a star here as a player, in the 1970s."*). PLAN's hook is the return: *"[warmly] In 1988, Johan Cruyff came back. He had been a star here as a player in the 1970s. This time he came as coach."*

### NICE

- **N1. Bridges vs cue teasers.** H hears 008's *"find the next two, from Paris and from Rome"* and 022's *"for how his time here ended, and who wears his number now"*, then a bridge that moves them on. E hears 024's title *"After the show: the first full house"*. This is the pattern PLAN accepts (cue, then bridge), but the teasers hint that longer versions hold more. R6's "instead" softens it. Optional: drop the teaser half of the 008 and 022 cues (*"Stay at the European Cups for Paris and Rome: …"*).
- **N2. Date style.** Dates mix digits and words: "the 22nd of October", "the 20th of May", "the 14th of June" against "the twenty-second of November", "the twenty-eighth of May", "the twenty-seventh of November". TTS reads both, but translators and the PDF should get one style. Use words throughout (V5: "as people say them").
- **N3. 020:** *"Barça finished the game with ten men."* floats after Barau's reading and before *"Real Madrid's own history…"*. Move it into the first paragraph, after the score: *"…eight–nil at half time, and Barça finished with ten men."*
- **N4. 022's version-neutral line stands alone** between the hook and the definition: *"He came from Rosario as a boy and played here until 2021."* For E it is the third telling (021, 022, 023). Join it to the hook paragraph (*"…The last two came after he had left, in 2021. He had come from Rosario as a boy."*). That keeps H's line in fewer words.
- **N5. 015:** *"And remember where most of them really lived. Most of the boys slept under a stand…"*. "Most" twice, and the payoff is announced before it is said. Cut the first sentence (−8).
- **N6. [quietly] in 029** (the Pope). PLAN lists [quietly] for Gamper, Sunyol and Cruyff's death only. The tone is right, so update PLAN's tag melody instead of the track. [curious] openers: 7 of 34 ✓ (cap 11). [warmly] appears in 19 tracks and before six of the eleven payoffs. Listen for over-acting on v3.
- **N7. 030's opener is tagged [wry]** on an instruction (*"[wry] Sit, if there's room…"*). Move the tag to the second sentence (*"This is the story of a stadium whose real name nobody used."*).
- **N8. 016's letters.** *"The letters on the crest changed from FCB to CFB."* will be spelt out. That's fine, but render-test it: a fast read blurs it. Optional: *"…from FCB, Futbol Club Barcelona, to CFB."*
- **N9. 020:** *"a Madrid paper, Ya, accused…"*: "Ya" sounds like "yeah". → *"a Madrid paper called Ya accused…"*.
- **N10. 004:** *"Mr Kans Kamper, of the foot-vall section."* The joke depends on hearing "foot-vall". Put it on the render test (PLAN §7 has FOOT-vahl). Also "Carrer Princesa" (cut in M1).
- **N11. 010:** *"…a club record he shares with Charly Rexach and, later, Messi."* "Later" is ambiguous by ear (later than what?). → *"…a club record he shares with Charly Rexach, and that Messi later matched."*
- **N12. "the room with his golden balls"** (016, 020 cues) is PLAN's wording and fine. Messi's space is never "the round room" ✓.
- **N13. 033:** *"Twenty-two years later, it happened again."* and the payoff *"…twenty-two years apart…"* use the same number in consecutive paragraphs. → *"In November 2005, it happened again."* (the date is already in the next sentence: merge them).
- **N14. For the facts audit, as heard:**
  - 007 *"the first time the club had ever clinched one against them"* (AU-S66/67, G-wait item);
  - 024 *"two storeys high"* (not in PLAN's row or FACTS 16.12–16.14; FACTS 16.3's "two floors" is the 1984 museum);
  - 020 *"According to a Guardian writer, Madrid's fans were given free whistles at the gate"* (PLAN: "reportedly handed whistles"; the Guardian writer is for the doubt about the visit);
  - 013 *"twenty-six games"* (G36 OK OFF; the lead's GAPS note allows it);
  - 015 *"they could see the stadium through their bedroom windows"* against the payoff's "pitch" (F9.5 says pitch);
  - 006 *"In its record year, 2016, nearly two million people came"* (F16.5 OK) ✓;
  - 003 "1971" for both rink and arena (G87–G88 OK) ✓;
  - 022 *"This museum shows all eight of his"* is F10.17's safe wording ✓.
- **N15. The quote in 016 is long** (two sentences of de Carreras plus a reported third). M1 trims it to the first.
- **N16. Rendered silence.** The pipeline adds ≈ 4.3 min in Full, 2.6 in E and 1.0 in H. PLAN §3's 125 wpm doesn't include them. Add a "with silences" column to §3 (as in §5 below).
- **N17. 001's route line names the models and the viewpoint to H**, which walks past the models. *"On the shorter tours, some of these stops are skipped."* covers it ✓.
- **N18. Lexicon gaps**: see §6.
- **N19. Gol Nord gloss twice** (002, 015: "the stand behind one goal / one of the goals"). Fine per track. Keep the wording identical for translators.

---

## 3. PLAN binding items: status

| Item | Status | Where / note |
|---|---|---|
| Decision 1: honesty first (001) | **Applied** | First paragraph, warm, once: no pitch, stands or dressing room; seen from outside and the viewpoint; a temporary museum in the old ice rink. |
| Decision 2: topic-keyed bodies (O2) | **Applied** | Building talk only in 001, 003, 006, 024–029, 034. Other bodies survive a move: 018's and 021's "this museum" and 022's "This museum shows" stay true anywhere. |
| Decision 3: displays, not rooms; order-free 007–016; callbacks only to 001/006 | **Applied, except R4** | No "next room". No callback between 007 and 016. No callback to 006 at all. 001's and 006's route lines fix an order (R4). |
| Decision 4: Extras | **Applied** | "If you're on the full tour" only in 016 and 029. The Full-only tracks (003, 004, 017–019, 030–032) announce plainly. The openers are in 004, 017 and 030 only, none alike, but each repeats the cue before it (L6). None needs a view before its last paragraph. |
| Decision 5: the 360° room | **Applied, except M2** | The club's warning, attributed. The show's sound. No content beyond the official description. 025 is short and on another subject. |
| Decision 6: the stadium as it is | **Applied** | Back since Nov 2025; ≈ 62,000; third tier built and not open; ring closed Oct 2026; roof from summer 2027 with Montjuïc again and no return date; ≈ 105,000. Each is a separate sentence. No "demolition", "biggest" or "Nou Camp". |
| Decision 7: legacy, endings, payoffs | **Payoffs applied** (all 11 present). **Endings: four pairs share an idea (L4)**, and three tracks add a motto (L5). | |
| Decision 8: even-handed politics | **Applied** | 1925 is attributed. Sunyol: "shot by Franco's troops" once, no box. 1943 has both readings plus Franco's medals. "Més que un club" is attributed. Real Madrid is named with respect in 007, 009, 011, 013, 020, 022 and 033. No 2017. |
| Decision 9: legends as legends | **Applied** | Colours (005), culers (017), napkin (021, two sentences), "Salid y disfrutad" (008, the club's history, per the revised decision), the 1943 visit (020). |
| Decision 11: statues | **Applied** | 014 and 031 "stood … from 2019 / 2009". No cue. No Messi statue. |
| Decision 12: directions | **Applied, except R2 and L10 ("look right")** | Landmarks only. No compass, gate, distance or "Masia over there". |
| Decision 13: practical lines once | **Applied** | Headphones, the club's hour, the warning repeated at the door, offline. Nothing else anywhere. |
| Lead's §8 decision 1: lengths in 001 | **Wording applied; Full not honest (M1); E borderline (R5)** | |
| Lead's §8 decision 11: E = 18 with 027 | **Applied** | 026 E bridge dropped. No 027 E bridge needed (R6). |
| Lead's §8 decision 17: no lyrics | **Applied** | 032 paraphrases. |
| Lead's GAPS decisions | **Applied** | Walter Wild first president (004). Les Corts "tens of thousands" (030, 031; L2a). Five Cups listed (031). Maradona's ovation (033). Luis Suárez "first Spanish-born winner" (022). No Sunyol box (019). Olympics "first", Paris 2024 (029, cut in M1 as DATED-light). |
| Version-neutral sentences (§3) | **All present** | 001 (frame, ice rink), 006 (Gamper, the move; L1a makes the move redundant), 008 (Cruyff coach, Dream Team), 022 (Rosario to 2021; Luis Suárez 1960), 028 (Nov 2025; 1957 bowl; 105,000), 029 (1982 opening; women's crowds), 034 (every clause self-contained). |
| Safe callbacks (§3) | **All safe** | None to 006. 034 answers 001 without "as you heard". |
| Watch the doubles | **Applied** | Two Luis Suárez (010 "the Uruguayan", 022 "in 1960"); two Wembleys each with their year; no bare "Ronaldo"; no Montal; the Gol Nord never "north"; "the round room" is only the 360° room. New: the architects' surname (L2b). |
| Lint | **All 34 OK** | The suggestions here are lint-neutral. |

---

## 4. The three play-throughs (default order, with the bridges)

**Full (34).**
- 001 on Av. de Joan XXIII by the ridged building → onto the campus, the stadium in view (002) → back to the door (003, 004, 005; L6 on the openers) → in, through the ticket check, the entrance hall (006).
- The trophies: the wall (007) → the European Cups (008–010; R7 on "the oldest") → the women's trophies (011) → the wall of shirts (012).
- The history: Cruyff (013, 014) → La Masia (015) → "Més que un club" (016) → a quiet corner (017–020; L4 on 017/018).
- Messi's space: the way in (021) → the golden balls (022, 023) → the round room's way in (024; **M2**) → the show → just outside (025).
- The models (026, 027) → the rail (028) → the benches (029–033; L2a and L4 on 030/031) → the way out (034; R3).
- No doubling back except the planned out-and-back from the museum to the stadium view (001 → 002 → 003).
- Nothing sends anyone into the stadium, to the Masia, a statue or the store.

**Essential (18, 5 bridges).**
- 001 → bridge to 006 ✓ (the "go straight to the museum's door instead" cancels the campus cue) → 006 → bridge to 008 ✓ → 008 → 009 → bridge to 011 ✓ → 011 → 012 → bridge to 014 ✓ (same display as 012's cue) → 014 → 015 → 016 ("Otherwise" → 021 ✓) → 021 → 022 → 023 → 024 → **bridge to 026 (M2 timing)** → 026 → 027 → 028 → 029 ("Otherwise" → 034 ✓) → 034.
- Nothing refers to a track E lacks. 014's "already a star here as a player" and 029's "the European Cup at Wembley" are self-contained or point to 008, which E has.
- Repeats that E hears: L1a (001/006), L1b (026/028), L1c (women ×4), L1d (exhibition ends ×3), the "move house" endings (001/006/034).

**Highlights (6, 5 bridges).**
- 001 → bridge to 008 ✓ → 008 → bridge to 022 ✓ (R6 "instead") → 022 → bridge to 024 ✓ → 024 → **bridge to 028 (M2 timing; R2 "the way out")** → 028 → bridge to 034 ✓ ("stay at the rail as long as you like" is a good addition) → 034.
- Every version-neutral line is present. H never hears a callback to 006, 009–016, 021, 023, 026 or 029. 034's recap explains the advert, the closure, Cruyff, the boys under the stand, the napkin and the women's crowds from scratch ✓.
- H's two risks are both at the round room: the bridge before the show (M2), and "the way out" read as the exit (R2).

**Under the ALTs.**
- **ALT-O3 (a) history first and (c) Messi first:** the cue rewrites in PLAN work, but 001's and 006's route lines become false (R4).
- **ALT-O2 (new museum):** the bodies outside 001, 003, 006 and 024–029 survive. 006's *"A new museum is being finished inside the stadium."* and 026's *"The museum's next home…"* are DATED and in the rewrite list ✓.
- **ALT-O15 option 1:** three cue gaps, one of them a double-back to Messi's space (R1).
- **ALT-O7:** 034's direction line should go (R3).
- **ALT-O4** (viewpoint closed): 029–033's last lines all say "in front of you". PLAN accepts that they lose their look; no text change needed.

---

## 5. Lengths and visit times

**Per track** (clean words / PLAN aim), 001–034:
340/300, 291/260, 245/190, 333/260, 215/160, 231/200, 214/180, 270/290, 305/270, 268/250, 347/290, 257/250, 319/260, 298/290, 320/270, 352/270, 228/170, 353/260, 290/260, 306/280, 269/250, 279/280, 267/260, 197/180, 234/190, 288/260, 251/210, 293/280, 343/260, 299/250, 330/250, 185/170, 286/260, 259/260.
- All are inside the lint ranges.
- 21 are more than 10% over their aim (M1). Only 008 (−7%) is under.
- Extras: 2,825 words (PLAN 2,320).

**Bridges.** E: 5 bridges, 174 words with titles. H: 5 bridges, 169 words. PLAN's figures (≈ 210 and ≈ 175) assumed 6 E bridges.

**Versions.** Words at 125 wpm, plus PLAN §3's walking, show (10 min) and viewpoint looking. Silences are the pipeline's: 0.75 s per paragraph gap, 0.55 s per [pause], 2 s tail per track and bridge.

| Version | Words (tracks + bridges) | PLAN | Listening | Walk + show + look | **Visit** | + silences | With a 20-min wait for the show | 001 says | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| Full | 9,562 | 8,320 | 76.5 | 25.6 | **≈ 102** | ≈ 106 | ≈ 122 | "about an hour and a half" | **Over by 13–18% (M1).** After M1 step 1 ≈ 99; after steps 1–2 (005 and 017 dropped) **≈ 93.5** (≈ 97 with silences). |
| Essential | 5,166 + 174 = 5,340 | ≈ 4,845 (with 027) | 42.7 | 22.7 | **≈ 65** | ≈ 68 | ≈ 85 | "about an hour" | **Borderline (R5).** After M1's cuts ≈ 64; with 016 and 029 at aim ≈ 63. |
| Highlights | 1,638 + 169 = 1,807 | ≈ 1,765 | 14.5 | 19.8 | **≈ 34** | ≈ 35 | ≈ 54 | "about thirty-five minutes" | **OK.** |

- None of these includes a queue at the ticket check, a wait for the show, photographs, the store or toilets. That matches PLAN, and nothing about waits is spoken.
- If O11 finds a show shorter than 10 min, every version gains the difference. H at an 8-min show is ≈ 32.
- Every walking figure still waits on O21.

---

## 6. Pronunciation: additions to PLAN §7 (names the tracks now speak that the lexicon lacks)

Catalan for Catalan names, Castilian for Spanish ones. Stress in CAPS. All go on ONSITE's listening check.

| Name | Say | Tracks |
|---|---|---|
| **Salid y disfrutad** | sah-LEED ee dees-froo-TAHD | 008 (allowed by the revised decision 4; not in §7 because it was banned when §7 was written) |
| Bern · Olympiastadion | BERN (English) · oh-LIM-pee-ah-SHTAH-dee-on | 008 · 010 |
| Juan Manuel Asensi · Granada | HWAN mah-NWEL ah-SEN-see · grah-NAH-dah | 013 |
| Numancia · Racing Santander | noo-MAN-thyah · RAH-theeng san-tan-DEHR | 009 |
| Bilbao · Gothenburg · Lisbon · Oslo | (English) | 011 |
| Cant de la Senyera | KANT duh luh suh-NYEH-ruh | 032 |
| Copa Eva Duarte · Copa Martini Rossi · Latin Cup | KOH-pah EH-bah DWAR-teh · mar-TEE-nee ROS-see · (English) | 031 |
| Montserrat Garcia Rius | mun-suh-RAT gur-SEE-uh REE-oos | 031 (cut in M1) |
| Agustín · Juan José | ah-goos-TEEN · HWAN hoh-SEH | 033 |
| Fermín López · Eric Garcia · Pau Cubarsí | fer-MEEN LOH-peth · EH-reek gur-SEE-uh · POW koo-bar-SEE | 029 (cut in M1) |
| Carrer Princesa | kuh-RAY preen-SEH-zuh | 004 (cut in M1) |
| Estadi del FC Barcelona | uss-TAH-dee del EFF-SEE bur-suh-LOH-nuh | 030 |
| Ya (the Madrid paper) | YAH (and write "a Madrid paper called Ya", N9) | 020 |
| FCB · CFB | letters (render test) | 016 |
| Elena Fort · Guadarrama · Hospital de Sant Pau | already in §7 ✓ | 016 · 019 · 017 |

- Also render-test the misprints in 004 ("Kans Kamper", "foot-vall"). The joke only works if the voice says them as written.
- **PLAN §7 names no track now speaks:** Avinguda de Joan XXIII and Arístides Maillol (ALT-O1 only), Futbol Club Barcelona in full, Gol 1957's "Gol" (spoken in 002 ✓, keep), Oriol Tort, Can Planes, Benito García, Alfredo Di Stéfano, Ferran Olivé, Vandenbergh, Teddy (Sheringham is spoken without it), Estudiantes, Guadarrama's "Alto del León" (spoken ✓, keep), Jorge (spoken in 013 ✓). Keep them for ES, FR and DE, marked "unused in EN".

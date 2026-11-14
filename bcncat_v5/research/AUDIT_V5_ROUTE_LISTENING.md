# AUDIT V5: ROUTE and LISTENING, Barcelona Cathedral EN (36 tracks + 15 bridges), 14 Nov 2026

I'm an independent auditor. I did not write this guide, and I edited no track, bridge or plan. Navigation comes first, then how the guide sounds through a synthetic voice, then lengths. Facts belong to the facts audit. Where I noticed a fact as it is *heard*, I pass it on (N6).

**What I read:**
- all 36 `v5/tracks/*.perf.txt` and the 3 bridge files (15 bridges);
- `v5/PLAN.md` in full: §1 (user and lead decisions, conventions, sections, route, ALT cues, lint), §2 (every row's @room, @title, content and cue), §3 (aims, walking, counts, playing orders, bridges, version-neutral sentences, safe callbacks, one home per story), §4 NEVER, §5–§7, §8 and the lead's decisions;
- `v5/ONSITE_CHECKLIST.txt`;
- the writers' notes (`v5/notes/*`);
- `v5/lint.py` and `pipeline/v5_direction.py` (the clean-text rule, tags and silences);
- `research/VISIT_ROUTE_AND_SPACES_NOV2026.md` (doors, the transept bays, the crypt stair, the choir);
- `research/OFFICIAL_AUDIO_COMPARISON_NOV2026.md` (§1.4, §2.2, §5: the on-site confusions);
- the Park Güell edition-2 audit, used as the model for format and depth.

`research/map/` is empty, so the official plan is still unread. Every cue is judged against the landmark rules and [O#] tags.

**Method.**
- A script checked every cue's destination against the next track's @title, and every bridge's opening, key, word count and closing title.
- I walked Full, Essential and Highlights on the route as the research describes it: the lift in the left transept bay, the cloister door in the right one, the choir and the crypt stair between them, and the crypt stair going down from the crossing towards the altar (ROUTE S11, §5 design rule). I tested each cue in the direction the listener is actually facing at that moment.
- I counted words, sentence lengths, tags and repeated phrases on the clean text (tags stripped as `lint.py` does). `lint.py` passes all 36 tracks.

**Counts.** **MUST: 4** · **SHOULD: 22** (9 route, 13 listening) · **NICE: 20**.

**Verdict in one paragraph.** The route is well designed and mostly well cued:
- Every title matches.
- Every skip that changes the walk has a bridge. All 15 bridges open "On this shorter tour," with the right keys (E 8, H 7).
- The Mass line, the choir-closed line and the crypt-closed line are all in place as fixed text.
- Extras are offered only with "If you're on the full tour", and the next main stop is named.
- There is no compass word, distance or chapel number.
- No shorter version is told to play a track it lacks.

Four things must change before recording:
- **M1.** Coming up out of the crypt, the listener faces *away* from the altar. There, the H/E bridge says "the bay on the right" and 023 says "the left side of the high altar", both without "as you face the high altar". The natural reading sends Highlights and Essential to the lift side of the church.
- **M2.** 013's cue tells people already on the roof to "ride up".
- **M3.** The roof tracks point at things O7 hasn't ticked: seven named buildings, the Sagrada Família on the horizon, and gargoyle "beasts".
- **M4.** 032 sends Full listeners to "look for" a room nobody has located. G102 puts it over the church's left-side chapels, not off the cloister.

For listening, the voice is clear, and the tone at 1391, 1936 and the martyrdom is right, with one exception ("naked", L7). The guide's tics are different from Park Güell's:
- "says it plainly" and "in one line";
- a run of "Then the turn" and "You'll often read" signposts;
- "older than" ten times;
- full Catalan and Spanish sentences for an English voice to read.

Several facts reach H and E listeners twice (the thirteen, "the bishops never moved", "five centuries", the bell towers). Full now runs about 97 minutes (about 101 with rendered silences) against "about an hour and a half". E (≈ 61) and H (≈ 32) are honest.

---

## 1. Track table

Words are clean words (as `lint.py` counts them) against the PLAN §3 aim. In = versions.

| # | In | Words / aim | Verdict | One line |
|---|---|---|---|---|
| 001 | H E F | 341 / 320 | SHOULD | The hat line PLAN and the lead kept is missing (R9). "About an hour and a half" is now ≈ 97 (R5). There is a 32-word sentence on the times (N18). The route line names the Lepanto chapel and the roof to H, which PLAN accepts (N10). |
| 002 | E F | 283 / 280 | NICE | Good hook ("When Barcelona began, it was tiny."). Three looks (N19). Its cue has two colons in a row (N3). "Then came the fire" (N6). |
| 003 | F | 228 / 200 | SHOULD | +14% (R5). [quietly] at 1938 is right, and it never says "the cathedral was hit" ✓. |
| 004 | H E F | 303 / 310 | SHOULD | "put it plainly" (L3). "almost five centuries" ×2, then 006 ×2 (L1). The version-neutral Gaudí line is exact ✓. "Carlí's visit" (N6). |
| 005 | F | 240 / 220 | SHOULD | "says it plainly" straight after 004's "put it plainly" (L3). "Then the turn", which 011 repeats (L4). |
| 006 | H E F | 317 / 300 | SHOULD | The Mass line is fixed text ✓, and the right side is tagged [O4] ✓. "A century and a half… more than a hundred and fifty years" in back-to-back sentences (L1). The payoff restates the stopgap (L1). |
| 007 | E F | 335 / 310 | SHOULD | Looks are conditional ✓, and the version-neutral lines are exact ✓. "older than" ×3 plus the payoff (L4). "Then the bigger surprise" (L4). "Hanß" (L6). The cue reads "marble screen… the wooden enclosure" (R2). |
| 008 | F | 228 / 220 | SHOULD | It tells the marble correction before 022, its home (L2). "If you can see in…, his tomb is Baroque" (L12). Same cue problem as 007 (R2). The Sança cut rule is only in the notes (R8). |
| 009 | E F | 214 / 220 | NICE | Clear, with one look ✓. Its @where lacks the cue's [O11] (R7). The cue echoes "the baptistery: The baptistery" (N3). It never shows the X-shaped cross that 021 recalls (L7). |
| 010 | E F | 266 / 290 | NICE | The plaque is gated by O14 in ONSITE ✓. The cue's "left-hand aisle" has no "as you face the high altar" and no [O18] (R7). Three looks and a floating font line (N19). |
| 011 | E F | 319 / 290 | SHOULD | The Saracen head is handled evenly and in the past tense ✓. Seven attributions (L3). "Then the turn" (L4). A [warmly] payoff straight after "xenophobia and racism" (L8). "carasses" (L6). |
| 012 | E F | 340 / 310 | SHOULD | Queue-safe: no look before the cue ✓. The tower sentence comes back in 014 (L1). "The oldest bell up there is older than the crypt" (L4, N4, N6). |
| 013 | F | 217 / 200 | **MUST** | The cue says "ride up" to people already at the top (M2). The gargoyle animals conflict with NEVER (M3). "for the cloister below", said in a ground-floor queue (N4). The title differs from PLAN (N1). |
| 014 | E F | 298 / 290 | **MUST** | "Look for the beasts among them" has no O7 gate (M3). Six looks (L9). The towers are re-told from 012, and the cloister is told before 015 (L1). |
| 015 | E F | 232 / 230 | **MUST** | It names seven buildings and asks for the Sagrada Família on the horizon, none ticked by O7. PLAN: "only what O7 ticks is named" (M3). "where the bishops never moved" (L1). |
| 016 | F | 285 / 280 | SHOULD | It opens on an attribution (L10). "cadirat" (L6). It re-tells 008's alabaster bishop (L2). The cue never says "don't lift a seat" (R9). "wooden enclosure" in @where (R2). |
| 017 | F | 156 / 170 | PASS | Good; it asks for a comparison. It can't work when the choir is closed (N5). |
| 018 | H E F | 344 / 330 | PASS | Strong hook. Its version-neutral line is exact ✓. "the arms of distant kings" ✓. No Carbonell ✓. |
| 019 | F | 308 / 280 | NICE | +10% (R5). [quietly] at Maximilian's funeral is right. |
| 020 | F | 231 / 210 | PASS | The cue keeps the crypt fallback and adds "Either way, start here" ✓. "never left" echoes 009 (N20). |
| 021 | E F | 332 / 310 | SHOULD | "Barcelona's own historians doubted her too" against "Barcelona has never had any doubt" (L7). "crucified, naked" (L7). "You saw that cross on the choir screen", which 009 never showed (L7). "say it plainly" (L3). "St" inside a quote (L6). |
| 022 | H E F | 340 / 320 | SHOULD | "girl of thirteen" one minute after 021 (L1). "Who was she?" for E and F (L11). The kings' party is listed twice (L11). "You'll often read" (L4). Five looks (L9). |
| 023 | F | 251 / 230 | **MUST** | The cue says "Walk round the left side of the high altar" to someone facing away from it (M1). |
| 024 | F | 344 / 270 | SHOULD | +27%, the largest overrun (R5). It re-tells 006's "started at the far end" and 022's Fabre (L2). It opens on "Nobody can say for sure" (L10). The cue depends on chapel signs (R3). |
| 025 | F | 268 / 240 | SHOULD | +12%. An internal note in @where (N2). The cue's "right side" has no "as you face it" (R7). |
| 026 | F | 343 / 310 | SHOULD | The cue's "turn round, and look back at the choir" faces the altar (R1). A full Spanish sentence (L5). "in one line" (L3). |
| 027 | F | 312 / 280 | SHOULD | The 1936 tone is right ✓, and there is no "anarchist" or "bombed" ✓. "look back" (R1). A full Catalan sentence (L5). "Mossos d'Esquadra" is not in the lexicon (§6). |
| 028 | F | 258 / 220 | SHOULD | +17% (R5). It opens on "older than", which 032 repeats (L4). |
| 029 | H E F | 333 / 300 | SHOULD | The 1448 correction is in place ✓. An old Catalan sentence with "Barchinona" (L5). "Here's the date everyone gets wrong… You'll often read" (L4). |
| 030 | H E F | 266 / 290 | SHOULD | The cue sends people to "the cloister's door to the street" without "don't go out" (R4). Three cathedral attributions (L3). "Barcelona's own saint" (L1). |
| 031 | F | 272 / 240 | SHOULD | "The original… is in the cathedral's museum" sets up a second Pietà just before 034 (L2). +13%. |
| 032 | F | 279 / 240 | **MUST** | The Extra cue sends people to an unlocated room (M4). +16%. "older than" and "It's often called" (L4). |
| 033 | F | 223 / 180 | **MUST** | Unreachable under what we know (M4). Internal notes in @room and @where (N2). "the Call" (L6). +24%. The tone at 1391 is right ✓. |
| 034 | H E F | 343 / 330 | SHOULD | The signature is written in capitals and may be spelt out letter by letter (L6). Otherwise one of the best tracks. |
| 035 | F | 251 / 220 | NICE | +14%. The monstrance stands on a "silver base" in the cue but a "silver seat" in @where (N12). |
| 036 | H E F | 262 / 300 | SHOULD | It opens and closes on "seventeen centuries" (L13). "a girl of thirteen" and "the city's own saint" again (L1). "Thank you for walking it with me" (L13). The Pont del Bisbe cut rule is only in the notes (R8). |

**Bridges (15).**
- All open "On this shorter tour,".
- The keys are right: E 8 (002, 004, 012, 015, 018, 022, 030, 034) and H 7 (001, 004, 006, 018, 022, 030, 034), as in PLAN §3.
- All end on the target's exact title.
- All run 27–45 words before the title.
- The fixed fallbacks are present: the choir in 006 H and 015 E, the crypt in 018 E/H.
- None says "for now", "come back" or "later". "Skip the next story" (002 E, 012 E) is PLAN's own text (N15).
- Problems: 022 H/E (M1); 006 H and 015 E "wooden" (R2); [O#] tags are spoken in five bridges (R6).

---

## 2. Findings

### MUST

**M1. Out of the crypt: "right" and "left" given to a listener who faces away from the altar.**
*Exact words:*
- Bridges 022 H>029 and 022 E>029: *"On this shorter tour, climb back up, and cross in front of the high altar to the white marble doorway into the cloister, in the bay on the right."*
- 023 cue: *"Climb back up. Walk round the left side of the high altar into the walkway behind it."*

*Problem:*
- The crypt stair "goes down from the crossing in front of the high altar" (ROUTE S11). People go down facing the altar, so they come back up facing the nave and the main door.
- At that moment their own right is the *left* as you face the high altar: the Sant Iu door and lift side.
- PLAN §1 is binding: "Left/right is always as you face the high altar… used only with its [O#] tag". The convention lives only in the bridge file's comment line (*"'On the right' in 022 H/E is as you face the high altar (O2)"*), which is never spoken.
- Every H and E listener hears this bridge. H has never been to the left transept, so they have no lift or organ to tell them they're on the wrong side.
- 023 has the same fault for Full ("the left side of the high altar" can mean the altar's own left or the listener's). Starting the ambulatory from the wrong end also reverses 024 → 025 → 026 and doubles back at the sacristy.
- This is exactly the "sent to the wrong place" complaint.

*Replacements:*
- Bridges 022 H and E (44 words before the title; tags in the header [O2, O9, O10]): *"On this shorter tour, at the top of the crypt stair, turn to face the high altar. The white marble doorway into the cloister is in the bay on your right. Go through to the small vaulted pavilion over a fountain, by the door: The cloister · The egg the accountant wrote down."* ("At the top of the crypt stair" also works when the crypt was closed.)
- 023 cue: *"Climb back up to the top of the stair, and face the high altar. Walk round its left-hand side into the walkway behind it. Stop where you can look up at its tall windows: Behind the high altar · They started at this end."* Add [O17] to 023's @where.
- ONSITE O10: add *"Coming up the crypt stair, which way do you face? Check that 'turn to face the high altar' then 'on your right' finds the white marble door."*

**M2. The no-queue case: 013's cue tells people already on the roof to ride up.**
*Exact words (013 cue):* *"When it's your turn, ride up. On the roof, follow the walkway until the lantern tower over the main door is in front of you."*

*Problem:*
- 011's cue sends no-queue listeners straight up: *"If there's no queue, ride up and play the next stop at the top"*.
- PLAN §1 is binding that both queue tracks "work in a queue, standing beside the lift chapel, or at the top beside the lift (ALT-NQ)".
- ALT-NQ says 013's cue "drops 'When it's your turn, ride up'". But whether there's a queue changes from hour to hour, so one recording must serve both cases. The E bridge already does this ("If you're still waiting, ride up when it's your turn") ✓.
- With no queue, Full listeners standing on the terrace are told to "ride up".
- Smaller slips: the queue tracks place the listener as if in the queue ("The roof you're about to walk", "Up there you'll also be…", "made gargoyles for the cloister below") or at the top ("The oldest bell up there"). See N4.

*Replacement (013 cue, +5 words):* *"If you're still in the queue, ride up when it's your turn. On the roof, follow the walkway until the lantern tower over the main door is in front of you: The roof · Saint Helena on the lantern."* [O3, O7, ALT-NQ]

**M3. The roof points at what O7 hasn't ticked.**
*Exact words:*
- 015: *"Within a few streets of this roof, the cathedral counts its neighbours. The Bishop's Palace. The Palau de la Generalitat, the seat of the Catalan government. Barcelona's City Hall. The Casa de l'Ardiaca, the archdeacon's house. The Palau Reial Major, the old royal palace. The Frederic Marès museum. And the Archive of the Crown of Aragon. From where you stand, some of them may hide behind their neighbours' roofs. So pick out the towers and the roof lines the view gives you, and let the rest be a list of who lives next door."*
- 015: *"[lightly] And if the day is clear, look far off on the horizon for the spires of the other great church in this city, the one people so often mistake this one for."*
- 014: *"Look for the beasts among them."*
- 013: *"And among the monsters, it says, there's a bull, a unicorn and an elephant."*

*Problem:*
- PLAN §2 015 is binding: "Only what O7 ticks is named, each with a way to find it", with NOT "any landmark not ticked". The Sagrada Família line is "only if O7 ticks it" (G64 is one guidebook).
- NEVER bans "gargoyle animals (F4.16)… until the matching ONSITE item finds them". The 014 row: "point only at those O7 finds".
- The writer's note admits the list is "a few metres away" (O6), not "from the roof". Asking 18 E and F listeners to "pick out" seven buildings, and to look for spires that may be hidden by haze or by the lantern tower, is the "wrong place" failure in visual form: people will pick the wrong tower.
- None of the three tracks has a cut rule in @where. ONSITE O7 has tick boxes, but it doesn't say what happens when a box stays empty.
- 013's list is attributed, and PLAN's row allows it. But it conflicts with NEVER, and Full hears it a minute before 014's "Look for the beasts". The lead must choose.

*Replacements (until O7):*
- 015 P2: *"Within a few streets of this roof stand the seats of the city, of the Catalan government and of the old kings. From up here, most of them hide behind their neighbours' roofs. Look instead at how tightly the old town packs round the cathedral."* (−52 words). After O7, add one sentence per ticked building, with a way to find it ("the square tower with…").
- 015 @where: add *"Cut 'And if the day is clear…' unless O7 ticks the Sagrada Família on the horizon."*
- 014: cut *"Look for the beasts among them."* Add to @where: *"Add 'Look for the [animal], [how to find it]' only for an animal O7 photographs."*
- 013: keep the animal sentence only if O7 ticks at least one of the three; otherwise cut it (−13).
- ONSITE O7: add after the ticks: *"Unticked = cut: 015's list names only ticked buildings; 015's horizon line goes without the Sagrada Família tick; 014/013's animals go without a photo."*

**M4. 032 sends Full listeners to "look for" a room that nobody has located.**
*Exact words:*
- 032 cue: *"If you're on the full tour, look for the room called Jewish memory, in the old archive: The cloister · Extra · Jewish memory."*
- 033 @where: *"PLACEMENT PENDING, how visitors reach it is unknown."*

*Problem:*
- The task's test is that every cue must be reachable under what we know. What we know (PLAN §8.13, G102) is that the Old Archive is "built over the left-side gallery of the church". That is the far side of the church from the cloister, by a stair nobody has found.
- Going there from Santa Llúcia means going back into the church. That is doubling back beyond what the plan accepts, and it may not even be allowed: O1 asks whether you "can go from the cloister back into the church".
- The cue gives no landmark, sign or direction. It is the Font Sarva problem (Güell R5), but worse: the room may not be off the cloister at all.

*Replacements:*
- Default until O6: record 032's cue in its ALT-J form: *"Now go into the Chapter Hall museum, next to this chapel. Find the painting of the dead Christ across his mother's lap: The Chapter Hall · The saint in spectacles."* Hold 033 out of the default Full playing order. PLAN §3 Full: −1.8 listening, −0.3 walking.
- After O6, if the room is reached from the cloister: *"If you're on the full tour, there's a short Extra in the room called Jewish memory, [sign or landmark from O6]: The cloister · Extra · Jewish memory. Otherwise, the next main stop is the Chapter Hall museum, next to this chapel…"*
- After O6, if it is reached from the church: use ALT-J2 (between 010 and 011).
- ONSITE O6: add *"From the Santa Llúcia doorway, can a visitor reach the room without going back into the church? Name the sign or door."*

### SHOULD (route and placement)

**R1. 026 → 027: "turn round, and look back at the choir" faces the altar.**
*Exact words:*
- 026 cue: *"Walk on towards the main door, to the white marble doorway into the cloister, in the bay beside the altar. Stop there, turn round, and look back at the choir."*
- 027 @room: *"looking back at the choir"*.
- 027 body: *"Look back at the choir once more"*.

*Problem:*
- Coming from the sacristy door on the right of the altar and walking "towards the main door", the choir is *ahead* of the listener, between the transept and the main door.
- "Turn round" turns them towards the altar and the ambulatory they've just left. 027 then opens *"The choir in front of you…"*.
- People who stop facing the doorway will find the choir to one side. People who stop as they walked will turn away from it.

*Replacements:*
- 026 cue: *"Walk on towards the main door, to the white marble doorway into the cloister, in the bay beside the altar. Stop beside it, out of the way, and look across at the choir, the enclosure in the middle of the nave: The cloister door · The summer of 1936."* [O2, O19]
- 027 @room: *"beside the white marble doorway, inside the church, the choir in view"*.
- 027 last look: *"Look across at the choir once more, and at the church around it."*
- ONSITE O19: *"Arriving from the sacristy door, where is the choir as seen from the doorway: ahead, across, behind?"*

**R2. "The wooden enclosure", and "the marble screen… the wooden enclosure" in one breath.**
*Exact words:*
- 007 and 008 cues: *"…the marble screen at the end of the choir, the wooden enclosure in the middle of the nave."*
- 015 cue: *"Then go to the choir, the wooden enclosure in the middle of the nave, and in at its entrance."*
- Bridge 006 H: *"…walk up the nave to the choir, the wooden enclosure in the middle…"*
- Bridge 015 E: *"…go to the choir, the wooden enclosure in the middle of the nave."*
- 016 @where: *"the wooden enclosure"*.

*Problem:*
- The stalls are wood, but from the nave the choir shows its outer walls, and the research calls them a "marble enclosure" (ROUTE, GEC). The screen that faces the main door is white marble (009).
- In 007/008, "the marble screen…, the wooden enclosure" sounds like one object described two contradictory ways.
- People told to find "the wooden enclosure" look for wood and see stone.
- 015's "and in at its entrance" is missing its verb.

*Replacements:*
- 007/008: *"…the next main stop is the white marble screen at the end of the choir, the enclosure in the middle of the nave."*
- 015: *"Then go to the choir, the enclosure in the middle of the nave, and go in at its entrance."*
- Bridge 006 H: *"…walk up the nave to the choir, the enclosure in the middle behind the white marble screen, and go in at its entrance."*
- Bridge 015 E: *"…go to the choir, the enclosure in the middle of the nave."*
- 016 @where: drop "wooden".
- ONSITE O8: *"What is the choir's outer wall made of, seen from the nave? Three words for the cues."*

**R3. 024 → 025: the cue only works if the ambulatory chapels carry readable signs.**
*Exact words:*
- 024 cue: *"Walk slowly on round the walkway, past its chapels, reading the names beside them, to the tomb of Sant Ramon de Penyafort."*
- 025 @where: *"PLACEMENT PENDING, no source names the chapel."*

*Problem:* O17 asks whether the chapels are signed at all, and G49 says no source names Penyafort's chapel. If there is no sign, Full listeners walk the whole ambulatory looking for a name. ALT-P (drop 025) exists, but only after O17. Meanwhile the recorded cue has no fallback.

*Replacement (two sentences, each ≤ 30):* *"Walk slowly on round the walkway, past its chapels, and look for a sign naming Sant Ramon de Penyafort. If you can't find one, stop anywhere along the walkway: Behind the high altar · The saint who sailed on his cloak."* [O17, O5, ALT-P]. Move "PLACEMENT PENDING" out of @where into the tags or notes (N2).

**R4. 030: sent to "the cloister's door to the street", with no "don't go out".**
*Exact words:* *"Walk on to the cloister's door to the street with a Pietà carved above it, the Pietat door. Stand near it…"*

*Problem:*
- The Pietat door is an outer door (ROUTE §1: "Outer cloister door… Visitor use unknown (O1)").
- PLAN treats re-entry as none. A Full listener who takes "walk on to the… door to the street" literally ends the visit before Santa Llúcia, the Chapter Hall and 036.
- H and E hear this cue too, before their bridge.

*Replacement:* *"Walk on to the cloister's street door with a Pietà carved above it, the Pietat door. Don't go out. Stand inside, near it, where you can also see a pillar's carved capital: The cloister · A Bible on the capitals."* (+4 words)

**R5. Full runs about 97 minutes (about 101 with rendered silences) against "about an hour and a half". Thirteen tracks are more than 10% over their aim.**
*Exact words (001):* *"The full tour takes about an hour and a half…"*

*Problem:*
- Full is 10,162 words against PLAN's 9,540 (+622, +5.0 min). See §5.
- PLAN §3: "Over by more than 10% → the lead cuts." The tracks more than 10% over are:

  | Track | Words / aim | Over |
  |---|---|---|
  | 024 | 344 / 270 | +27% |
  | 033 | 223 / 180 | +24% |
  | 028 | 258 / 220 | +17% |
  | 032 | 279 / 240 | +16% |
  | 003 | 228 / 200 | +14% |
  | 035 | 251 / 220 | +14% |
  | 031 | 272 / 240 | +13% |
  | 025 | 268 / 240 | +12% |
  | 027 | 312 / 280 | +11% |
  | 029 | 333 / 300 | +11% |
  | 026 | 343 / 310 | +11% |
  | 019 | 308 / 280 | +10% |
  | 020 | 231 / 210 | +10% |

- Most of the overrun is in Full-only tracks. E (+138 words) and H (+49) are fine.

*Fix (≈ −330 words, −2.6 min, all repeats, dated lines or tics):*

| Track | Cut | Words |
|---|---|---|
| 024 | *"Who drew the first plan of this cathedral? Nobody can say for sure."* and the L2 rewrite | ≈ −40 |
| 024 | *"Twelve of the cathedral's old windows were restored in a project finished in 2024."* | −14 |
| 028 | *"Then turn to the garden, with its palms, its magnolias and an orange tree."* (DATED garden works) | −14 |
| 028 | *"And above this door rises the cathedral's second bell tower, the one with eleven bells for the services."* | −18 |
| 032 | *"And every December since 1786, a Christmas fair named after her has filled the square outside."* | −16 |
| 033 | *"The Call's edge ran along streets beside the bishop's own houses, a few steps from here."* | −16 |
| 033 | *"All this, from an archive left with only about a hundred documents after Almanzor's army burned the city."* | −18 |
| 035 | *"While it was still being made, a bishop ordered a sapphire and a ruby to be added."* | −17 |
| 025 | *"He is the patron saint of Catalan lawyers, and his feast falls on the seventh of January."* | −17 |
| 031 | *"A picture Bible, perhaps, for people who couldn't read."* | −9 |
| 026, 027, 029 | the foreign-language sentences (L5) | ≈ −35 |
| 011 | *"His workshop calls it 'the largest and most important historical organ in Catalonia'."* | −12 |
| 011 | the [warmly] payoff (L8) | −16 |
| 012 | *"And the clock that drives the hours was a marvel in its day, regulated by electric pulses."* | −17 |
| 015 | the list (M3) | −52 |
| 014 | the repeated towers and cloister (L1) | ≈ −30 |

- With M4's default (033 held), Full ≈ 92 (≈ 96 with silences).
- If the first render or O22 still gives more than ≈ 95, change 001 to *"The full tour takes a little over an hour and a half…"* (word-neutral).

**R6. Bridges: [O#] tags inside five spoken lines, and none recorded for four others.**
*Exact words:* `bridges/001-011.txt`, e.g. *"…from the door up to the spires [O13]: The facade · Drawn in 1408, built in 1887."* The same applies to 002 E, 004 H, 004 E ([O1]) and 006 H ([O8, ALT-K]).

*Problem:*
- `v5_direction.validate()` rejects any bracket that isn't a delivery tag. A renderer that reads the line as it stands will either fail or send "[O13]" to the voice.
- `bridges/012-023.txt` does it correctly, with a `#` header. `bridges/024-036.txt` has no tags at all (030 → [O20, O21, ALT-K9]; 034 → [O1, O23], per the notes).
- PLAN §3 says every bridge inherits its cue's tags, and ONSITE re-checks bridges by them.

*Fix:* in 001-011, move the tags to a `#` header as in 012-023. Add the header to 024-036.

**R7. Left/right and tag hygiene in four places.**
- 009 cue *"the first chapel on the left as you face the high altar"*: 009's @where carries [O24, O2] but not the [O11] the plan's cue has. Add [O11, O14].
- 010 cue *"Walk up the left-hand aisle…"*: no "as you face the high altar" and no [O18]. Use *"Walk up this left-hand aisle, as you face the high altar, past its side chapels…"* and add [O18] to 010's @where.
- 025 cue *"Carry on round to the right side of the high altar."*: use *"…to the right side of the high altar, as you face it."*
- 027 @where *"in the bay on the right of the high altar"*: add *"as you face it"*.
- Every other left/right in a cue or @where is correctly phrased and tagged: 006, 007, 009 (phrase), 011, 026.

**R8. ONSITE_CHECKLIST: cut rules that live only in the writers' notes, and missing tests.**
*Cut rules now only in `notes/*`:*
- 008 Sança paragraph: *"only if O4/O5 find the neighbouring chapel and its tomb in view; otherwise cut it"*.
- 036 Pont del Bisbe sentence: *"cut it if O23 finds the bridge isn't in view"*.
- 015 horizon line (M3).

Put each into the item (O4, O23, O7) and the per-track tick list as *"[ ] … → keep, else cut"*.

*Missing tests:*
- M1: which way you face coming up the crypt stair.
- M2: none needed.
- M3: unticked = cut.
- M4: reaching the archive from the cloister.
- R1: where the choir is from the cloister door.
- R2: the choir's outer wall.
- R3: a fallback stop in the ambulatory.
- R4: is the Pietat door an exit visitors can use by mistake?
- N13: does the cloister loop pass the Santa Eulàlia door before Santa Llúcia?

**R9. Working-church lines that dropped out.**
*Exact words:*
- 001: *"Inside, keep your voice low."*
- 016 cue: *"find a seat whose folding ledge is raised, and look at the carving underneath"*.

*Problem:*
- PLAN 001 and the lead's §8.3 decision ("hats off and voices low (keep)") keep the hat line. The track dropped it.
- 017's @where says *"never lift a seat yourself"*, but nothing spoken says it. The Extra cue invites a hunt for raised seats in the canons' stalls.

*Replacements:*
- 001: *"Inside, keep your voice low, and take your hat off."* (+5)
- 016: *"…find a seat whose folding ledge is already raised, and look at the carving underneath. Please don't lift one yourself."* (+6)

### SHOULD (listening)

**L1. The same fact twice, heard in H and/or E.**

| | Exact words | Heard by | Fix |
|---|---|---|---|
| a | **The thirteen.** 021 *"a girl of thirteen"* + *"Thirteen tortures… one for each year of her life"*; 022 *"Who was she? Eulàlia, by tradition a girl of thirteen martyred in 304, is Barcelona's own saint."*; 030 *"That's the girl of thirteen in the legend, Barcelona's own saint"* + the city's *"for each of the agonies… years of her life"*; 036 *"by tradition a girl of thirteen, martyred for her faith"* | E: 5 times in 4 tracks. H: 022, 030, 036 | 022 (still version-neutral; H gets "thirteen" in 030): *"She was Eulàlia: by tradition a young girl martyred in 304, and Barcelona's own saint."* 036: *"She is the city's martyr saint. Her feast is still kept every twelfth of February."* 030: *"That's the girl of thirteen in the legend."* (drop "Barcelona's own saint", which H has just heard in 022). |
| b | **"The bishops never moved."** 001 cue title, 002 body and title, 015 *"on the same corner of the Roman town where the bishops never moved"*, 036 *"And the bishops never moved."* | E F | 015: *"…on the corner of the Roman town where you began."* Keep 002 (home) and 036 (H needs it). |
| c | **Five centuries, four times in two tracks.** 004 *"The plans came first, by almost five centuries."* + *"Barcelona waited almost five centuries for its front door."*; 006 *"The stopgap lasted almost five hundred years"* + *"A stopgap roof that lasted five centuries, right over the door."* | H E F (back to back) | 004: *"The plans are far older than the stone."* 006: cut the payoff and end on *"Pick one out above you, and look for the colour."* (−11) |
| d | **006 says one fact twice in a row.** *"For a century and a half they built around the Mass. The city says the work took more than a hundred and fifty years, and never interrupted the services."* | H E F | Cut the first sentence (−10). |
| e | **The bell towers.** 012 *"One stands over the Sant Iu door and carries the clock. The other stands over the door from the church into the cloister."*; 014 *"One stands over the Sant Iu door and carries the clock, the other over the door into the cloister."* | E F | 014: *"There are the two eight-sided bell towers you heard about while you waited."* (safe: 012 is in E and F) |
| f | **The cloister below, twice in two minutes.** 014 *"And down below lies the cloister, its garden open to the sky."*; 015 *"Now look down into the cloister."* | E F | 014: cut (015 is the home). |
| g | **"own saint" / "the city's own".** 001 *"the city's own saint"*; 022 *"Barcelona's own saint"*; 030 *"Barcelona's own saint"*; 036 *"the city's own saint"* + *"It is still a working church, and the city's own."* | H E F | See (a). Keep 001, 022 and 036's last line. |
| h | **"Seventeen centuries … one corner"**: 001; 036 opening *"Seventeen centuries of history, on one corner of the Roman town."*; 036 closing *"One corner of a Roman town, and seventeen centuries of people coming back to it."* | H E F | See L13. |

**L2. The same fact twice, Full only.**

| | Exact words | Fix |
|---|---|---|
| a | **The alabaster correction told before its home.** 008 *"[lightly] This is the alabaster people confuse with Santa Eulàlia's tomb. Hers, in the crypt, is marble."* / 022 *"You'll often read that this tomb is alabaster. It's marble, not alabaster…"* (decision 6: the correction lives in 022) | 008: *"[lightly] Remember this alabaster when you reach Santa Eulàlia's tomb in the crypt."* (PLAN's safe forward pointer 008 → 022 is kept, and the reveal stays in 022.) |
| b | **"They started at the far end", twice.** 006 *"They started at the far end, behind the altar, and worked their way towards this door."* / 024 *"The first builders started here, at the far end, and worked their way towards the main door."* | 024: *"This is the end you heard about at the main door, where the building began."* (safe: 006 is in every version) |
| c | **Fabre twice.** 022 *"The crypt is thought the finest work of Jaume Fabre, a master builder from Mallorca."* / 024 *"His name was Jaume Fabre. In 1317 the cathedral hired him from Mallorca… The crypt you've just left was his finest work."* (now stated as fact, N6) | 024 P1: *"The crypt you've just left was the work of Jaume Fabre. In 1317 the cathedral hired him from Mallorca, where he had been running the works of a Dominican convent in Palma, and made him master of the works for life. Historians still ask whether he kept an earlier design or reworked it."* |
| d | **016 re-tells 008.** *"Sanglada's hand turns up elsewhere in this church. He carved the alabaster figure of Sant Oleguer, the bishop who lies under the Lepanto crucifix near the main door."* | *"You've met his work already: the alabaster bishop by the main door."* (−15) |
| e | **Two Pietàs in the museum.** 031 *"The original, the Catalan encyclopedia says, is in the cathedral's museum, so this may be a copy."* Five minutes later, 032/033 send people into that museum to *"find the painting of the dead Christ across his mother's lap"*. | 031: *"The original wooden relief, the Catalan encyclopedia says, is kept by the cathedral, so the one above the door may be a copy."* (Add to "Watch the doubles": the Pietat relief and Bermejo's Pietà.) |

**L3. Attribution tics.** Counted on the clean text:

| Tic | Count | Where |
|---|---|---|
| "the cathedral" as the source (says, describes, calls, dates, answers, "in the cathedral's words") | 13 tracks against PLAN's cap of 12 | 007, 010, 014, 015, 018, 022, 023, 024, 025, 027, 028, 030 (×3), 033 |
| "the city" as the source | 011 ×3, 021 ×3 (plus 006, 012, 013, 017, 030) | 021 has the popular-culture pages twice in five sentences |
| "put/says/say it plainly" | 3 | 004, 005 (back to back, both the University of Barcelona), 021 |
| "in one line" | 3 | 016, 026, 027, each before a foreign quote |
| "…'s own" + source | 4 | "the city's own guide" (012), "the city's own popular-culture pages" (021), "the cathedral's own record" (027), "the cathedral's own words" (030) |
| 011 alone | 7 attributions | "The city dates", "A newspaper tells", "the same paper says", "says the city's popular-culture service", "the newspaper puts", "the city explains", "His workshop calls it" |

*Replacements:*
- 004: *"A University of Barcelona exhibition put it plainly:"* → *"A University of Barcelona exhibition gave the reason:"*.
- 005: *"The University of Barcelona says it plainly: it was a project 'drafted by Antoni Gaudí'."* → *"The same university calls it a project 'drafted by Antoni Gaudí'."*.
- 021: *"The city's own popular-culture pages say it plainly."* → *"The same pages answer it:"*. *"Experts, the city says, see…"* → *"Experts, they add, see…"*.
- 030: *"In the cathedral's own words: 'The presence…'"* → *"It adds: 'The presence…'"*. *"The cathedral describes daily cleaning, a pond whose water is constantly renewed, a diet prescribed by a vet, and regular check-ups."* → *"They get daily cleaning, a pond whose water is constantly renewed, a diet prescribed by a vet, and regular check-ups."*
- 011: *"And in 1892, the same paper says, its beard was remade from three donkey tails."* → *"And in 1892 its beard was remade from three donkey tails."* Cut the workshop line (R5).
- 016, 026, 027: see L5 and L10.
- With M3's 015 rewrite, the "cathedral" count is 12.

**L4. Signposts, "corrections" and "older than".**
*Exact words:*
- Signposts:
  - *"[pause] Then the turn."* in both 005 and 011.
  - 007: *"[curious] Now the evidence."* and *"[pause] Then the bigger surprise."*
  - 021: *"Now the harder question."*
  - 029: *"Here's the date everyone gets wrong."*
- Correction formulas, three of them heard by H:
  - 022: *"You'll often read that this tomb is alabaster."*
  - 029: *"You'll often read that the cathedral was finished in 1448."*
  - 020: *"So when you read that Lochner carved this choir…"*
  - 032: *"It's often called the last surviving piece of the Romanesque cathedral. It isn't."*
- "older than" ten times in eight tracks:
  - 006 and 010 ("older than the chapel's vault");
  - 007 three times plus a payoff on the same idea ("older than the battle it's famous for", "older than the legend", "It was old long before the battle");
  - 012 ("older than the crypt");
  - 018 ("older than the paint");
  - 028 ("This doorway may be older than the cathedral around it");
  - 031 and 032 ("older than the cathedral it now belongs to").

*Fix:*
- 011: cut *"Then the turn."* and start the paragraph *"[pause] By the middle of the 20th century…"*.
- 007: cut *"Then the bigger surprise."* and *"The room itself is older than the legend."*. Start P6 *"Arnau Bargués built this room in 1407…"*.
- 022: *"[lightly] Many books call this tomb alabaster. It's marble: white marble, partly painted and gilded."*
- 029: *"[pause] Here's the date everyone gets wrong: 1448. It's often given for the cathedral, but it belongs to the cloister."*
- 012: *"The oldest bell in the towers was cast in 1321: a small bell, an esquella in Catalan, called l'Esquella de Prima."* (also N4, N6).
- 028: *"This doorway may have come from the church before this one."* (032 keeps "older than": it's its title.)

**L5. Whole sentences in Spanish and Catalan for an English voice.**
*Exact words:*
- 026: *"…in Spanish: 'las obras de la catedral gótica implicaron la destrucción de la románica'. The works on the Gothic cathedral involved the destruction of the Romanesque one."*
- 027: *"…in Catalan: 'La primavera de l'any 1939, l'arxiu retorna a la Seu.' In the spring of 1939, the archive came back to the cathedral."*
- 029: *"…in old Catalan: 'Aquest die fonch feta crida pública per la ciutat de Barchinona.' On this day a public proclamation was made through the city of Barcelona."*

*Problem:*
- PLAN §7's lexicon covers names, not sentences. The free engines in `render_edge.py` (edge-tts Brian, Kokoro) will read these with English phonology ("Barchinona", "fonch", "implicaron").
- Each one is then translated, so the listener hears the fact twice and the voice stumbles first.
- 016 and 032 handle this better: 016 gives the quote in English only, and 032 keeps a two-word *"molt mediocre"*.

*Replacements:*
- 026: *"In the words of the city's history museum, the building of the Gothic cathedral meant the destruction of the Romanesque one."* (−15)
- 027: *"The cathedral's record ends the story simply: in the spring of 1939, the archive came back to the cathedral."* (−12)
- 029: *"In April 1456 the Generalitat's diary noted that a public proclamation had been made through the city: Saint George's day was to be a holiday."* (merges the next sentence; −16)

The @sources keep the original wording.

**L6. Words the voice will misread.**
- 007 *"Stefan Hanß"*: write *"Stefan Hanss"* in the spoken text; the @sources keep "ß". The ß is outside most English lexica.
- 021 *"'St Eulàlia of Barcelona's existence…'"*: "St" can be read "Street". Spell it out in speech, *"Saint Eulàlia"* (rendering an abbreviation, not changing the quote), or add a lexicon rule.
- 034 *"in Latin capitals: 'OPUS BARTOLOMEI VERMEJO CORDUBENSIS'"*: all-caps words are often spelt out letter by letter. Write *"Opus Bartolomei Vermejo Cordubensis"*; the sentence already says "in Latin capitals".
- 033 *"the Call, the Jewish quarter"*: the voice will say the English verb. Add "Call → KAHL" to the lexicon and the render test (§6).
- 016 *"with its cadirat, its choir stalls"*: a one-off Catalan technical term. Use *"with its choir stalls"*.
- 011 *"carasses"*: the plural is new to the lexicon. *"That's told of the city's carasses in general"* → *"That's told of these carved heads in general"*. *"the carasses had been taken down"* → *"the heads had been taken down"*.

**L7. 021: a contradiction, one word too many for a martyred child, and a callback to something nobody showed.**
*Exact words:*
- *"A century and more ago, Barcelona's own historians doubted her too… Historians argue whether Barcelona's Eulàlia and Mérida's were two girls or one story. Barcelona has never had any doubt."*
- *"She was crucified, naked, on an X-shaped cross."*
- *"You saw that cross on the choir screen by the main door, and you'll find it in images of her all over this cathedral."*

*Problem:*
- "Barcelona has never had any doubt" contradicts the sentence three lines earlier. It also says for a third time what the track has already said twice ("a single legend claimed by two different places"). PLAN's row has it in quotes, but writers may smooth.
- NEVER bars "the tortures' sexual details". "Naked", said of a thirteen-year-old in a working church, adds nothing the listener needs.
- 009, which E and F heard, says "Find the flames". It never mentions an X-shaped cross, and O24 hasn't confirmed one, so "You saw that cross" can be false.

*Replacements:*
- *"Whether Barcelona's Eulàlia and Mérida's were two girls or one story, the argument goes on. The city's devotion to her has never wavered."*
- *"She was crucified on an X-shaped cross."*
- *"You'll find that cross in images of her all over this cathedral."* After O24, add *"…the choir screen among them"* if it's there.

**L8. 011: [warmly] on the head criticised for racism.**
*Exact words:* *"…a severed head, which came to be seen 'as an apology for xenophobia and racism'. … [warmly] A face that rolled its eyes at the feast days, and that the city now explains."*

*Problem:*
- Decision 5 asks for "today's criticism, evenly". The track does that.
- Then a warm motto lands two paragraphs after "racism". It also re-uses "rolled its eyes" from the look line just before it ("where the face once rolled its eyes").

*Fix:* cut the payoff (−16; it also helps 011's +29). The track ends on its look, then the cue.

**L9. One clear look per track.**
*Exact words:*
- 014 asks for six things:
  - the statue;
  - *"turn slowly and take in the roof around you"*;
  - the two towers;
  - the two pinnacles;
  - the cloister;
  - *"Look along the roof for that cross"* and the gargoyles.
- 022 asks for five:
  - the inscription round the edge;
  - the lid;
  - *"eight columns of different shapes"*;
  - the keystone;
  - the ninth-century stone.
- 002 asks for three: the towers, *"Find the big letters"*, *"Now look back at the cathedral"*.
- 021, at the top of the crypt stair, has none.

*Fix:*
- 014: after L1e/f and M3, the looks are Helena, the apse cross and the gargoyles in general.
- 022: cut *"The box stands on eight columns of different shapes."* (−9). Make the inscription conditional like the plaque (*"if you're close enough to read it"*; G73 and O10 are open).
- 021 (NICE): add before the cue *"Look down the stair: the tomb you're about to see is hers."*

**L10. Two weak openers.**
*Exact words:*
- 016: *"The chapter's old book of the choir sums it up in one line, in old Catalan."*
- 024: *"Who drew the first plan of this cathedral? Nobody can say for sure."*

*Problem:*
- PLAN: "Open on the thing, the person or the question". 016 opens on a source. 024 opens on a non-answer, under a title, "They started at this end", that it doesn't deliver until P2.
- "Nobody can say for sure" joins "nobody knows" (013, 030 ×2, 034) and "nobody can show it" (002).

*Replacements:*
- 016: *"These seats began with a journey to Flanders. The chapter's old choir book records it, in old Catalan: 'Anglada was sent … to Bruges to buy oak for the said choir.'"* Then *"He travelled all the way to Flanders to choose the wood himself."* → *"He went to choose the wood himself."*
- 024: open with L2c's paragraph (*"The crypt you've just left was the work of Jaume Fabre…"*).

**L11. 022: "Who was she?" for listeners who have just heard who she was, and the kings' party listed twice.**
*Exact words:*
- *"In July 1339 two kings came down these steps. With them came their queens, a cardinal and bishops, and they came for a saint. King Peter the Ceremonious wrote in his own chronicle that he, the king of Mallorca, the cardinal, the archbishop and several bishops carried her body…"*
- *"Who was she?"*

*Problem:* E and F heard 021 a minute ago. The list of the party comes twice in three sentences.

*Replacements:*
- *"In July 1339 two kings came down these steps, and they came for a saint."*
- For "Who was she?", see L1a. *"She was Eulàlia: …"* works for H and needs no question.

**L12. 008: a conditional that reads as a cause.**
*Exact words:* *"If you can see in from the doorway, his tomb is Baroque."*

*Replacement:* *"If you can see in from the doorway, look for his tomb. It's Baroque, and on it lies something older:"*

**L13. 036: two payoffs that close on the opening, and a vague "it".**
*Exact words:*
- First line: *"Seventeen centuries of history, on one corner of the Roman town."*
- Last lines: *"…It is still a working church, and the city's own. [quietly] One corner of a Roman town, and seventeen centuries of people coming back to it."*
- *"[warmly] Thank you for walking it with me:"*

*Problem:*
- 036 (with 001) says "seventeen centuries" four times, counting the title.
- The quiet last line works best if the opening hasn't already said it.
- "Walking it": the "it" has no referent.

*Fix:*
- Cut the first sentence (−11). 036 still opens self-contained for H: *"The first Christians of Barcelona built their church in this corner of the walled town. And the bishops never moved."*
- *"[warmly] Thank you for walking this corner with me:"*

### NICE

- **N1. 013's title.**
  - PLAN §2 says *"Lightning and fireworks"*. The track and 012's cue say *"Lightning and firecrackers"*, which matches the source ("petards", note 012-023 l.51).
  - The pair is consistent. Update PLAN §2 (row 013 and 012's cue) so the translators follow it.
- **N2. Internal notes in listener-facing fields.**
  - 025 @where: *"PLACEMENT PENDING, no source names the chapel."*
  - 033 @where: *"PLACEMENT PENDING, how visitors reach it is unknown."*
  - 033 @room: *"(G102: built over the left-side gallery of the church: see ALT-J2)"*.
  - Move these to the tags or the notes.
- **N3. Cue echoes.**
  - 009: *"…beside the main door: the baptistery: The baptistery · Baptised here."* The voice says "the baptistery. The baptistery." Use *"…beside the main door, the baptistery: The baptistery · Baptised here."* by dropping the colon after "door".
  - 002: *"…the Casa de l'Ardiaca, the archdeacon's house: The Pla de la Seu · …"* (two colons, 34 words). Use *"Turn now to the old stone house built into the Roman wall beside the cathedral, the Casa de l'Ardiaca: The Pla de la Seu · A square from after the war."*
- **N4. Where the queue tracks think you are.**
  - 012 *"The oldest bell up there"* (see L4).
  - 013 *"The roof you're about to walk reopened in 2024"* → *"The roof walk reopened in 2024"*.
  - 013 *"Up there you'll also be in the company of the gargoyles."* → *"On the roof you'll also be in the company of the gargoyles."*
  - 013 *"made gargoyles for the cloister below"* → *"made gargoyles for the cloister"*.
  - 012 *"If you're here at noon, that's la Tomasa."* is the only clock time in speech. It's harmless but DATED (§6); consider cutting it with the clock line (R5).
- **N5. Closed-space leftovers.** PLAN accepts these under ALT-M.
  - 023's cue *"Climb back up"* comes after a closed crypt (M1's wording fixes it).
  - 016's Extra cue (raised seats) comes when the choir is closed. Prefix *"If you're inside the choir, …"* if the lead wants.
  - 019's cue *"Walk back to the choir's entrance"* is said to people already standing there.
- **N6. For the facts audit (as heard).**
  - 004 *"Nine years after Carlí's visit"*: no source here says he visited; use *"Nine years after Carlí's drawing"*.
  - 012 *"older than the crypt you're going to see"*: 1321 against a crypt whose works began under Fabre from 1317 and ended in 1339.
  - 024 *"The crypt you've just left was his finest work"*: stated as fact; 022 says "is thought".
  - 027 *"Sant Oleguer's tomb was moved too, from the Lepanto chapel down into the crypt"*: the listener saw it back in the chapel; add *"for safety, and later brought back"* if F10.22 says so.
  - 033 *"Those who survived converted to Christianity or fled."*: check against G104's wording.
  - 002 *"Then came the fire"*: the archive source says "destrucció".
- **N7. "Later" is the commonest link word.** 16 uses, including "X years later" seven times (004, 013, 016, 019, 020, 022, 025). Vary two or three.
- **N8. "At the end of the tour" three times** (003, 007, 010). E hears it in 007 and again in 010.
- **N9. [quietly] in more places than PLAN lists.** PLAN lists [quietly] "once each" in 021, 022, 027, 036. The tracks also use it in 003 (1938), 019 (the funeral), 026 (the countess killed) and 033 (1391), and 022 uses none. The tone is right in every case. Update PLAN's tag melody instead of the tracks.
- **N10. 001's route line names the Lepanto chapel and the roof**, which H never visits. PLAN sanctions it with *"On the shorter tours, some of these stops are skipped."* Optional: *"…pause at the chapel of the Christ of Lepanto, and on some tours take the lift up onto the roof."*
- **N11. DATED lines.** 013 *"reopened in 2024"* (cut after 2028) and 024's windows line (R5).
- **N12. 035.** The cue and 034's cue say *"on its silver base"*. 035's @where says *"silver seat"*, and the body says *"a silver seat called King Martin's throne"*. Use "silver seat" everywhere.
- **N13. The cloister loop (O9).** If the Santa Eulàlia door lies on the walk between the Pietat door and Santa Llúcia, all three versions pass the exit and come back to it. That is a short double-back the plan doesn't list. Add it to O9's drawing.
- **N14. 036.**
  - *"Behind you, in the cloister"* assumes the listener faces the street door, but @where says "to one side". Use *"Here in the cloister, the thirteen geese keep their pond…"*.
  - *"the cathedral's step-free way in"* is a practical line outside 001. It is harmless; the lead decides.
- **N15. "Skip the next story"** (bridges 002 E, 012 E). This is PLAN's text and it undoes the cue's "one more story". It implies content exists, which brushes the "never name skipped content" rule. Optional: *"On this shorter tour, go straight on: …"*.
- **N16. Rendered silence.**
  - The pipeline adds 0.75 s per paragraph gap, 0.55 s per [pause] and a 2 s tail: ≈ 4.1 min in Full, 2.2 in E, 1.1 in H.
  - If 125 wpm is speech only, add these to §3 (they are in §5's "with silences" column).
  - Mid-track [pause] count: 26 of 36 tracks have exactly one, and 9 have none. That mix is fine.
- **N17. Callbacks that restate a number.** 033 repeats 002's *"about a hundred documents"*, and 036 repeats 030's *"at least four hundred years"*. Both are allowed callbacks; shorten if cutting.
- **N18. Long sentences.**
  - 001: *"The full tour takes about an hour and a half, the essential about an hour, the highlights about half an hour, walking included, plus any wait for the lift to the roof."* (32 words). Split it after "half an hour": *"…about half an hour. That's walking included, plus any wait for the lift to the roof."*
  - 015's horizon sentence (32) goes with M3.
  - Counting the title, the cue sentences of 001 (31), 002 (34), 024 (34), 028 (35) and 031 (32) pass 30. Without it they are all ≤ 30.
- **N19. Three looks and a floating line.**
  - 010 asks for three things: the window, the cupboard and "Find the girl". *"The font itself is from the 15th century."* floats on its own. Join it to the window paragraph or cut it.
  - 002 also has three looks; on the square that's acceptable.
- **N20. 020's hook echoes 009.** *"A German woodcarver came to Barcelona and never left"* echoes 009's *"came to Barcelona in 1517… He never came back"*. Full hears both. Optional: *"A German woodcarver settled in Barcelona for the rest of his life."*

---

## 3. PLAN binding items: status

| Item | Status | Where / note |
|---|---|---|
| Decision 1: not the Sagrada Família | **Applied** | 001 opens warmly. 015's bookend is unnamed (M3 gates it). |
| Decision 2: Variant A | **Applied** | Main door in, Santa Eulàlia door out (001, 035, 036). ALT-B/C are held in PLAN. |
| Decision 3: Mass-proof | **Applied** | 006 cue: *"If Mass is on, don't go in. You can hear this from the door"* (the semicolon is spoken as a full stop, as lint requires). 007/008 looks are conditional. Choir fallback in 015 and bridges 006 H, 015 E. Crypt fallback in 020 and bridges 018 E/H. Nothing says "come back" or "after Mass". |
| Decision 4: the roof block | **Applied, except M2 and M3** | 012 and 013 need no view. Nothing mentions the AR viewer (lint). H has no roof. |
| Decision 5: legends as legends | **Applied** | The geese (030), the cannonball (007), the finger (023), the Saracen head (011, evenly; L8), Honorata (012). |
| Decision 6: corrections spoken once | **Mostly applied** | 1448 (029), the facade dates (004), Gaudí (004 line, 005 home) ✓. The marble correction is told twice in Full (L2a). |
| Decision 7: one home and payoff lines | **Applied for payoffs** (10 tracks end on a motto, the listed ones; 016 and 024 come close) | The repeats are in L1 and L2. |
| Decision 8: directions | **Applied, except M1, R1, R7** | No compass word, distance or chapel number. No scaffolding. Transept cues work with or without works. |
| Decision 9: practical lines once | **Applied, except the hat line (R9)** | Headphones, voice, photos, the lift wait, offline. No prices or hours. |
| Decision 10: lengths | **E and H honest; Full drifted** | R5. |
| Version-neutral sentences (§3) | **All present** | 004, 007 (both), 018, 022, 030, 034 and 036 are word for word or close. L1a changes 022's wording without breaking its H role. |
| Safe callbacks (§3) | **All safe by version** | One is factually unsafe: 021 → 009 "You saw that cross" (L7). |
| Watch the doubles | **Applied** | The two chapter houses (007 *"It's not the Chapter Hall museum at the end of the tour"*), Bernat Martorell named in full, "the bell called Eulàlia", "the Santa Eulàlia door", August Font only in 005. Two Pietàs are a new double (L2e). |

---

## 4. The three play-throughs (default order, with the bridges)

**Full (36).**
- 001 beside the steps → along the square to the Roman towers (002) → the Casa de l'Ardiaca (003) → back to face the front (004, 005) → in by the main door (006).
- The Lepanto chapel's doorway, right, [O4] (007, 008) → the choir screen (009) → the baptistery, left, [O11] (010).
- Up the left aisle (R7) to the Sant Iu door (011) → the lift queue (012, 013; M2 if there's no queue) → the terraces (014, 015; M3) → down.
- The choir (016–020; R2 for the description) → the crypt stair (021) → the tomb (022, 023).
- **M1**: back up, facing the nave, "the left side of the high altar" is ambiguous → the ambulatory (024; R3 to 025) → the sacristy door, right (026).
- **R1**: "turn round, and look back at the choir" → the cloister door (027) → through (028) → the fountain (029) → the pond (030).
- **R4**: the Pietat door, a street door with no "don't go out" (031) → Santa Llúcia (032).
- **M4**: the Jewish-memory room, unlocated (033) → the Chapter Hall (034, 035) → just inside the Santa Eulàlia door (036).
- No doubling back beyond what PLAN accepts: the square and the lift. N13 is a possible exception at the Santa Eulàlia door.
- Nothing sends anyone to Sant Sever, the Pia Almoina, the Pont del Bisbe or out and back in. 027 names Sant Sever only as a church that survived, and 036's bridge sentence gives no direction.

**Essential (18, 8 bridges).**
- 001 → 002 → bridge to 004 ✓ → 004 → bridge to 006 ✓ → 006 → 007 → "Otherwise" to 009 ✓ → 010 → 011 → 012 → bridge to 014 ("If you're still waiting…" handles the no-queue case) ✓ → 014 → 015 → bridge to 018 ✓ → 018 → bridge to 021 ✓ → 021 → 022 → **bridge to 029 (M1)** → 029 → 030 → bridge to 034 ✓ → 034 → bridge to 036 ✓.
- Callbacks are all safe by version: 009 → the crypt; 010 → the Pietà; 011 → Carbonell in the choir; 012 → the crypt; 014 → the lantern and the banker; 015 → 001 and 002; 034 → the fountain; 036 → the front and the geese.
- One callback is unsafe in fact: 021's "You saw that cross" (L7).
- Nothing tells E to play or recall a track it lacks.

**Highlights (9, 7 bridges).**
- 001 → bridge to 004 ✓ → 004 → bridge to 006 ✓ → 006 → bridge to 018 (R2) ✓ → 018 → bridge to 022 ✓ → 022 → **bridge to 029 (M1)** → 029 → 030 → bridge to 034 ✓ → 034 → bridge to 036 ✓.
- Version-neutral lines all present: 004 (Gaudí), 006 (the lantern, no Lepanto recall), 018 (the canons' choir and the 1300s seats), 022 (Eulàlia), 030 (the girl of thirteen), 034 (Desplà from scratch), 036 (the Roman corner, 1936 and the co-patroness).
- No H track recalls the choir screen, the roof, 021 or the baptistery.
- The only route gap is M1, but it is the one H can least recover from: H has never seen the lift side, so nothing tells them they've turned the wrong way.

**Mass and closures.**
- **Lepanto Mass:** heard from the door (006 fixed text) ✓.
- **Choir closed:** listen at the entrance (015, 006 H, 015 E) ✓. The looks in 016, 017 and 020 become meaningless, which ALT-M accepts.
- **Crypt closed:** stay at the top (020, 018 E/H, 021) ✓.
- **Roof closed:** ALT-R (no text in the tracks; correct).
- **Transept works:** no cue names scaffolding ✓.
- **No lift queue:** M2.

---

## 5. Lengths and visit times

**Per track** (clean words / PLAN aim), 001–036:
341/320, 283/280, 228/200, 303/310, 240/220, 317/300, 335/310, 228/220, 214/220, 266/290, 319/290, 340/310, 217/200, 298/290, 232/230, 285/280, 156/170, 344/330, 308/280, 231/210, 332/310, 340/320, 251/230, 344/270, 268/240, 343/310, 312/280, 258/220, 333/300, 266/290, 272/240, 279/240, 223/180, 343/330, 251/220, 262/300.
- All are inside the lint ranges.
- More than 10% over: 003, 019, 020, 024, 025, 026, 027, 028, 029, 031, 032, 033, 035 (R5).
- Under: 036 (−38), 010 (−24), 030 (−24), 017 (−14).

**Bridges.** E: 8 bridges, 363 words with titles (PLAN 280). H: 7 bridges, 307 words (PLAN 245).

**Versions.** 125 wpm; PLAN §3's walking; a 5-min lift wait, with the queue tracks heard inside it.

| Version | Words (tracks + bridges) | PLAN | Listening | Walking | Lift wait | Overlap | **Visit** | No queue → 20-min queue | + rendered silences | 001 says | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Full | 10,162 | 9,540 | 81.3 | 14.9 | 5 | −4.5 (012 + 013 = 557 words) | **≈ 97** | 96 → 112 | ≈ 101 | "about an hour and a half" | **Over by ≈ 7–12%** (R5). With M4 (033 held) ≈ 95; with R5's cuts ≈ 92. |
| Essential | 5,468 + 363 = 5,831 | 5,610 | 46.6 | 12.3 | 5 | −3.0 (012 + its bridge) | **≈ 61** | 59 → 76 | ≈ 63 | "about an hour" | OK |
| Highlights | 2,849 + 307 = 3,156 | 3,045 | 25.2 | 6.3 | – | – | **≈ 31.5** | 31.5 (no lift) | ≈ 32.6 | "about half an hour" | OK |

- 012 + 013 come to 4.5 minutes, so they still fit inside a 5-minute wait. A 20-minute queue is what the only 2026 reviewer reports (COMP §2.2): Full ≈ 112, E ≈ 76. 001's *"plus any wait for the lift to the roof"* covers this honestly.
- If the conditional tracks drop on site, Full falls: without 017 by ≈ 1.3; without 025 by ≈ 2.1 (+0.3 walking); without 033 by ≈ 1.8 (+0.3 walking).
- None of the times includes an entry or ticket queue (PLAN §1, correct). Every walking figure still waits on O22.

---

## 6. Pronunciation list (TTS lexicon; additions and changes to PLAN §7 marked **new**)

Catalan for Catalan names, Castilian for Spanish ones. Stress in CAPS.

| Name | Say | Tracks |
|---|---|---|
| Santa Eulàlia · Eulàlia | SAN-tuh uh-oo-LAH-lee-uh | 001 004 008 009 011 012 021–023 030 035 036 |
| la Seu | luh SEH-oo | 001 027 |
| Barcino · Joan Brossa · **decumanus** · Augustus | bar-SEE-noh · zhoo-AN BROSS-uh · **dek-oo-MAH-nus** · aw-GUS-tus | 002 **new (decumanus)** |
| Almanzor | al-man-ZOR | 002 033 |
| **Sant Felip Neri** | **san fuh-LEEP NEH-ree** | 003 **new** |
| Casa de l'Ardiaca · Lluís Desplà · Carl Nesjar | KAH-zuh duh lur-dee-AH-kuh · lyoo-EES dus-PLAH · karl NESS-yar | 002 003 015 034 |
| Carlí · Rouen · Manuel Girona | kar-LEE · roo-AHN · muh-noo-EL zhee-ROH-nuh | 004 031 · 004 |
| Joan Martorell · Lluís Domènech i Montaner · Josep Oriol Mestres · August Font | zhoo-AN mur-too-RELL · doo-MEN-ek ee moon-tuh-NAY · zhoo-ZEP oo-ree-OL MESS-truss · ow-GOOST FON | 005 |
| Gaudí | gow-DEE | 004 005 |
| cimbori · Bartomeu Gual | seem-boo-REE · bur-too-MEH-oo GWAL | 006 |
| Lepanto · Don John of Austria | luh-PAN-toh · (English) | 006 007 |
| **Stefan Hanß → write "Hanss"** | SHTEH-fun HAHNSS | 007 **changed (L6)** |
| Arnau Bargués · Sant Oleguer · Tarragona | ur-NOW bur-GESS · san oo-luh-GEH · tuh-ruh-GOH-nuh | 007 008 016 027 |
| Pere Sanglada · **Anglada** | PEH-ruh san-GLAH-duh · **an-GLAH-duh** | 008 016 020 **new (Anglada)** |
| Sança Ximenis de Cabrera | SAN-suh shee-MEH-nees duh kuh-BRAY-ruh | 008 |
| trascor · Bartolomé Ordóñez · Carrara · **quondam** · Pedro Villar | truss-KOR · bar-toh-loh-MEH or-DOH-nyeth · kuh-RAH-ruh · **KWON-dam** · PEH-droh vee-LYAR | 009 **new (quondam)** |
| Noli me tangere · Gil de Fontanet · Bartolomé Bermejo · Antoni Canet | NOH-lee may TAN-geh-reh · ZHEEL duh foon-tuh-NET · ber-MEH-ho · un-TOH-nee kuh-NET | 010 034 |
| Sant Iu | san EE-oo | 010–012 014 019 |
| carassa · **carasses** | kuh-RAH-suh · **kuh-RAH-suss** (or rewrite, L6) | 011 **new (plural)** |
| Pere Flamenc · Antoni Carbonell · Gabriel Blancafort · **King Jaume** | PEH-ruh fluh-MENK · kur-boo-NELL · guh-bree-EL blun-kuh-FORT · **ZHOW-muh** | 011 (Jaume also 025) **new (Jaume alone)** |
| Holy Innocents | (English; the plan's "Sants Innocents" is not spoken) | 011 012 |
| Honorata · Francesc Calbetó · **esquella** · l'Esquella de Prima · la Tomasa · **Angelus** | oo-noo-RAH-tuh · frun-SESK kahl-buh-TOH · **uss-KEH-lyuh** · luss-KEH-lyuh duh PREE-muh · luh too-MAH-zuh · **AN-juh-lus** | 012 **new (esquella, Angelus)** |
| Joan Claperós | zhoo-AN kluh-puh-ROS | 013 016 |
| Eduard Alentorn · Constantine · Benedicció del Terme | uh-doo-ARD uh-lun-TORN · (English) · buh-nuh-deek-see-OH del TER-muh | 014 |
| Palau de la Generalitat · **Generalitat** · Palau Reial Major · Frederic Marès | puh-LOW duh luh zhuh-nuh-ruh-lee-TAT · **zhuh-nuh-ruh-lee-TAT** · puh-LOW ray-AL muh-ZHOR · fruh-duh-REEK muh-RESS | 015 (cut by M3) · 029 **new (alone)** |
| **cadirat** · Bruges · Ramon d'Escales · Macià Bonafè | **kuh-dee-RAT** (or cut, L6) · BROOZH · ruh-MON duss-KAH-luss · muh-see-AH boo-nuh-FEH | 016 020 **new (cadirat)** |
| **misericords** | **miz-ER-ih-kordz** | 017 **new** |
| Toisó d'Or · Philip the Good · Gideon · Joan de Borgonya · Burgundy | toy-ZOH DOR · (English) · GID-ee-un · zhoo-AN duh bur-GOH-nyuh · BUR-gun-dee | 018 019 |
| **clarions · sackbuts · shawms · compline · catafalque** · Maximilian | **KLAR-ee-unz · SAK-buts · SHAWMZ · KOMP-lin · KAT-uh-falk** · (English) | 019 **new (clarions, compline, catafalque)** |
| Michael Lochner · Joan Frederic · Carrer de Mercaders · Lluís Borrassà | MIH-kha-el LOKH-ner · zhoo-AN fruh-duh-REEK · kuh-RAY duh mur-kuh-DAYS · lyoo-EES boo-ruh-SAH | 020 031 |
| Sarrià · Dacian · Mérida · Santa Maria del Mar | suh-ree-AH · DAY-shun · MEH-ree-dah · SAN-tuh muh-REE-uh del MAR | 021–023 |
| **"St" in a quote → say "Saint"** | — | 021 **new (render test)** |
| Peter the Ceremonious · **Mallorca** · Frodoí · Santa Maria de les Arenes | (English) · **muh-YOR-kuh** · froo-doo-EE · duh luss uh-REH-nuss | 022–025 **new (Mallorca)** |
| Jaume Fabre · Lupo di Francesco · **Golden Legend** | ZHOW-muh FAH-bruh · LOO-poh dee fran-CHES-koh · (English) | 022–024 |
| Ponç de Gualba · Patrocini · **Palma** | PONS duh GWAL-buh · puh-troo-SEE-nee · **PAHL-muh** | 024 **new (Palma)** |
| Ramon de Penyafort · Sóller · Santa Caterina · Pere Nolasc | ruh-MON duh puh-nyuh-FORT · SOH-lyer · SAN-tuh kuh-tuh-REE-nuh · PEH-ruh noo-LASK | 024 025 |
| Almodis · Ramon Berenguer the First · al-Bakri · Tortosa · Ermessenda · Victor the Second | ahl-MOH-dees · ruh-MON buh-ren-GAY · al-BAK-ree · toor-TOH-zuh · ur-muh-SEN-duh · (English) | 026 |
| **Mossos d'Esquadra** · Sant Sever · Agustí Duran i Sanpere | **MOSS-ooss duss-KWAH-druh** · san suh-VEH · uh-goos-TEE doo-RAN ee sun-PEH-ruh | 027 **new (Mossos)** |
| l'ou com balla · Corpus Christi · **Te Deum** | LOH-oo kom BAH-yuh · (English) · **tay DAY-oom** | 029 035 **new (Te Deum)** |
| Sapera · Dello Delli · Berenguer Vila · Bernat Martorell · Pietat | suh-PEH-ruh · DEL-loh DEL-lee · buh-ren-GAY VEE-luh · bur-NAT mur-too-RELL · pee-uh-TAT | 030 031 036 |
| Santa Llúcia · Arnau de Gurb · **molt mediocre** | SAN-tuh LYOO-see-uh · ur-NOW duh GOORP · **MOL muh-dee-OH-kruh** | 028 031–035 **new (molt mediocre)** |
| **the Call** (the Jewish quarter) · **papyri** · Seville | **KAHL** · **puh-PY-ree** · (English) | 033 **new (render test)** |
| **Opus Bartolomei Vermejo Cordubensis (write in lower case)** · Bartolomé de Cárdenas · Córdoba · **converso** | OH-poos bar-toh-loh-MAY-ee ver-MEH-yoh kor-doo-BEN-sis · bar-toh-loh-MEH deh KAR-deh-nahs · KOR-doh-bah · **kon-VER-soh** | 034 **changed (L6), new (converso)** |
| King Martin the Humane · Jaume Huguet · **Saint Bernardino** · Giuliano di Nofri | (English) · ZHOW-muh oo-GET · **ber-nar-DEE-noh** · joo-LYAH-noh dee NOH-free | 035 **new (Bernardino)** |
| Carrer del Bisbe | kuh-RAY del BEEZ-buh | 001 035 036 |
| Spanish and Catalan sentences (026, 027, 029) | (cut, L5; if kept, render and score them) | 026 027 029 **new (render test)** |

- **PLAN §7 names no track now speaks:** Santa Creu, Plaça Nova, Praetextatus, Agapit Vallmitjana, Pere Joan, Antoni Claperós, Sants Innocents (spoken as "Holy Innocents"), Elisenda de Montcada, Andreu Escuder, Font de Sant Jordi (spoken as "Saint George"), Timbor de Prades, Usatges, Guislabert, Pere Ramon, Pons of Toulouse, Hugh of Lusignan, Narbonne, Nicolau de Maraia, Berenguer de Palou, Hic requiescit, Apòstols, Carrer dels Comtes, Pont del Bisbe (spoken as "the little stone bridge"). Keep them for ES, FR and DE, marked "unused in EN".
- **ONSITE's listening checks (l.253–281):** add the **new** rows, with "Hanss", "St", the lower-case signature, "the Call" and any surviving foreign sentence as render tests.

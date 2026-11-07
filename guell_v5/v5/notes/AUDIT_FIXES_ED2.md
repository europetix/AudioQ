# Audit fixes, edition 2 (7 Nov 2026)

These are the fixes for the two edition-2 audits:
- `research/AUDIT_V5_ED2_FACTS.md` (**FA2**: 2 MUST, 8 SHOULD, 22 NICE);
- `research/AUDIT_V5_ED2_ROUTE_LISTENING.md` (**RA2**: 3 MUST, 21 SHOULD, 18 NICE).

They also apply the lead's decisions of 7 Nov.

**Files changed**
- `v5/tracks/001–045.perf.txt`: 44 of the 45 tracks.
- The four files in `v5/bridges/`.
- `v5/ONSITE_CHECKLIST.txt`.
- `v5/PLAN_V2.md`: only the lines that carried the mushroom, the old queue cue and the "about two hours" wording.
- `build/static/README.txt`, both `build/static/*.command` launchers, and `build/route_map.py`.

A copy of every file as it was before these fixes is in the scratchpad: `fix/tracks_before`, `fix/bridges_before`, `fix/build_before`, `fix/PLAN_V2.md` and `fix/ONSITE_CHECKLIST.txt`.

**Checks**
- `python3 v5/lint.py`: all 45 tracks OK, all inside their word ranges. 001 is exactly at its 360-word cap.
- `bash build/build_all.sh`: succeeded (45 tracks, route PDF and zip).
- Nothing was committed.
- No source page was re-read. Every change uses the wording the audits relayed, or the lead's wording. The changes either attribute less, or say less than the source.

**Totals.** Fixed in full or in part: 2/2 FA2 MUST, 8/8 FA2 SHOULD, 22/22 FA2 NICE, 3/3 RA2 MUST, 19/21 RA2 SHOULD (R5 only in part) and 13/18 RA2 NICE.
- Held for the on-site check, with the text ready: RA2 R1, plus the landmark half of R5.
- Declined on the lead's instruction: RA2 R6.
- Declined NICE items: RA2 N7, N11/L4i, N13, N15 and N16.

**Lengths after the fixes** (words of the tracks, plus the bridges for E and H):

| Version | Words before | Words after | Visit time, RA2 §3 method | Shorter tour, as spoken in 001 |
|---|---|---|---|---|
| Full | 12,210 | 11,549 | ≈ 125, or ≈ 130 with the rendered silences (N16) | — |
| Essential | 6,905 | 6,666 | ≈ 76 | "about an hour and a quarter", kept |
| Highlights | 3,747 | 3,650 | ≈ 46–47 | "about three quarters of an hour", kept |

Full is still above the ≈ 125 threshold, so 001 now says "a little over two hours" (lead's decision; RA2 R2).

---

## Lead's decisions (7 Nov)

| Decision | What was done |
|---|---|
| **025, the Font Sarva water** | Before: "It was also piped to the well of the old Larrard farmhouse, which Güell later made his home." After: "It was also piped down to the old Larrard farmhouse, which Güell later made his home." @what now quotes the source ("fins a la deu de l'antiga masia Larrard") and notes that the receiving point is called neither a well nor a spring. |
| **The mushroom** | Removed from every placement field and every bridge.<br>• 004 @where: "…the mushroom on the right" → "…the other gatehouse on the right".<br>• 006 @room: "outside its door, the mushroom roof in view" → "outside its door, the gatehouse without the tower".<br>• 006 @where: "the gatehouse on the right as you face the stairway, with the cap on its roof in view" → "the other gatehouse, the one without the tower, on the right as you face the stairway".<br>• 006 @what: the La Pedrera line is marked "in the body only and attributed… never used to find the house".<br>• 001 @sources: "past the mushroom pavilion" → "past the Casa del Guarda, the gatehouse without the tower".<br>• 045 @what: "no 'mushroom' identifier" → "no roof identifier".<br>• Kept, as instructed: 006's body line "the La Pedrera foundation sees a 'mushroom-shaped dome'" (attributed), and 004's plural "mushroom-shaped ventilators" with its @listen and @what.<br>• Bridges: none uses the mushroom. Their tag comments now read [O-map, O2] and so on.<br>• PLAN_V2 and ONSITE: see RA2 M1. |
| **The no-queue case (M2)** | Every line that sends people to the second check now says to stop before it, queue or not: the 012 cue, the 013 cue, bridge 004 H>015 and bridge 010 E>014. The audit's wording is used: "Play the next stop before the check: in the queue if there is one, or standing to one side just before it". 014's own cue already said "Stay in the queue, or where you are, for one more story before the check". So 015's one-way warning is now always heard before the check. |
| **036, the view** | The sea sentence and the towers sentence are now each separate and can be cut whole.<br>• Sea: "On a clear day, the same board says, 'you can even see as far as the sea': find its flat line on the horizon."<br>• Towers, now its own paragraph: "The Catalan Tourist Board says the view is 'framed by the towers of the Olympic Village and the blue Mediterranean': two tall towers by the sea."<br>• The look that always stays: "Look out over the roofs, as far as the day allows."<br>• @where already carried [O7]. It now also carries the cut rule: keep the sea sentence only if the sea is ticked, and the towers only if the sea and the two towers are ticked. Nothing else in the track depends on either. |
| **Full length** | 001: "about two hours" → "a little over two hours". The Essential and Highlights wordings are unchanged.<br>• README.txt: "about 2 hours" → "a little over 2 hours".<br>• Both launchers: "about 2 hours" → "a little over 2 hours".<br>• route_map.py: "about 2 hours" → "about 2 h 10".<br>• The route map prints "45 tracks" from the data. PLAN_V2 §1 and §3 now say the same; the lead's decision 1 text was left as the lead wrote it. |
| **Closing mottos** | Cut in 20 of the ≈ 40 tracks that had one: 002, 004, 005, 006, 007, 008, 009, 011, 013, 015, 016, 017, 021, 022, 028, 029, 031, 033, 034 and 040. Two more were trimmed: 032 keeps only "A theatre on the roof of a market.", and 026's "Two houses, from all those plots." went too. Kept where they are strong and not a near-repeat: 003, 010, 012, 014, 018, 019 (reworded), 020, 024, 030, 036, 037, 038 (untagged), 039 (needed for the W minimum), 041, 042 (reworded), 043 and 044. No more than two kept mottos in a row use the "A [noun] that…" shape. |
| **Attribution tics** | Counted on the clean text ("the park says, calls, describes, admits or lists"; "in the park's words"; "the park's own"; "the park's history, historians, page or guide"). Every track now has two at most. Before, 015 had 3, 016 had 4, 021 had 4, 039 had 3 and 042 had 3. Each one removed was a plain description: the quotation marks were kept, or the line paraphrased, and @sources still holds the attribution. Every opinion or reading keeps its attribution. The "restoration study" run in 004–010 is down to 004 (which introduces the study), 006's "the restorers found" and 007's "the restorers' study". No two consecutive tracks open with the same words or tag: 007 and 013 were untagged to avoid back-to-back [curious] openers. |

---

## FA2: the facts audit

### MUST

| ID | Track | Before → after |
|---|---|---|
| M1 | 002 | Before: "Next to this gate, outside the park, is an old spring, the Font del Carbó. Around it, in 1875, the first modest building on this hillside began, a quarter of a century before Güell."<br>After: "Next to this gate, outside the park, are gardens named after an old spring, the Font del Carbó. Around that spring, below the old farmhouse you'll pass at the end, a modest start was made at building in 1875, a quarter of a century before Güell."<br>@what: "una tímida urbanització"; never "the first building". All three versions pass Casa Larrard. |
| M2 | 011 | Before: "She measured about fifty metres of stone columns, up to six metres high."<br>After: "…made this viaduct the subject of her master's thesis: a bridge about fifty metres long, on stone columns up to six metres high."<br>@what: she modelled it from the Ajuntament's drawings and did not measure it. "An engineering student" kept (FA2 calls it acceptable). |

### SHOULD

| ID | Track | Before → after |
|---|---|---|
| S1 | 011 | "…and the thrust stays inside the stone, all the way to the ground. Her analysis found the vault stable." → "So each column is tilted along the path the load wants to take. In her analysis, the thrust stays inside the vault, and the vault is stable." |
| S2 | 035 | "Josep Maria Jujol engraved prayers to the Virgin Mary into its tiles. One study calls their meaning an open question." → "What the prayers in its tiles mean is still argued over." This also covers RA2 L4e. |
| S3 | 040 | "argued that the whole park hides a picture" → "argued that the park hides a picture". @what now notes the central area. |
| S4 | 044 | "Neighbourhood associations also signed a manifesto…" → "At one point, neighbourhood associations even signed a manifesto against closing the park off." It is no longer tied to 2013. |
| S5 | 024 | "Then, in 2016, each of the four Suns…" → "Later, each of the four Suns…". @what notes RC before any year is spoken again. |
| S6 | 025 | "well" → "piped down to the old Larrard farmhouse" (the lead's wording, above). |
| S7 | 037 | "It was never begun: the plots didn't sell." → "It was never built: the plots didn't sell." @what now quotes s3. |
| S8 | 007 | "…two parabolic arches, the shape of a hanging chain turned upside down." → "The restorers' study describes them as two parabolic arches." The sentence now ends there, with no catenary gloss. |

### NICE (all 22 applied)

| ID | Track | Before → after |
|---|---|---|
| N1 | 007 | "found each room's original colour under the later paint" → "studied the layers of plaster and paint, found each room's original colour, and brought it back". |
| N2 | 007 | "The cleverest house on the hill…" cut with the motto. The hook now uses aj4's own words, "great richness and compositional complexity". |
| N3 | 008 | "As the press reported her words" → "As an English press note reported her words". |
| N4 | 009 | "At the attic windows, look for two crosses made of porcelain." → "Look at the two attic windows: each forms a cross, worked in porcelain." |
| N5 | 012 | "Bassegoda added the plain truth: they were artificial" → "Bassegoda added that they were artificial". |
| N6 | 013 | "a road that was bent round a tree" → "a road that made room for a tree". "the bridge makes room for it" → "the builders let it keep growing" (op12: "natural growth… respected"). |
| N7 | 018 | "some scholars see in this creature the Python of Delphi" → "some writers, among them the Gaudí scholar Joan Bassegoda, see in this creature the Python of Delphi". The full form is used because H and E meet him here first; 022's full form stays. |
| N8 | 019 | "some four hundred dragons on its buildings" → "nearly four hundred dragons, on its buildings, fountains and parks". |
| N9 | 023, 035 | 023: "by the historian Joan Duch" → "by Joan Duch". 035: "A study of his life" → "A study of Jujol's work". |
| N10 | 025 | "mines deep in the hill" → "mines in the hill". |
| N11 | 026 | "what one of them looks like with no house on it" → "what that part of the estate looks like with no houses on it". |
| N12 | 028 | "No other buyer ever came." → "No buyer came for it." |
| N13 | 031 | "A botanist once gave…" → "A botanist's talk once gave…". |
| N14 | 033 | "In April 2026 … the neighbours were invited to a community dinner in the park" → "For April 2026 … the neighbours were invited to a community dinner here". Only the invitation, which is documented, is now spoken. The motto "and still throwing them" that depended on it is cut. Still RC: did the dinner take place? |
| N15 | 036 | "calls this one of the best views" → "calls the park one of the best views". |
| N16 | 036 | "houses in Sant Gervasi and on the new estate at Tibidabo" → "houses in Sant Gervasi, or the new estate at Tibidabo". |
| N17 | 038 | "too narrow to open to visitors" → "very narrow, and not fit to open to visitors". |
| N18 | 038 | "It was the way down to Güell's own home." → "It leads on toward Güell's own home." |
| N19 | 039 | "the park's signs may call it" → "the park's pages call it". "Nothing here was carved smooth" → "Little here was carved smooth". |
| N20 | 041 | "Of the three homes on the estate in Güell's time" → "Of the estate's homes in Güell's time" (also RA2 N18). |
| N21 | 042 | "parish priest and teacher" → "parish priest and educator". |
| N22 | 044 | "People from the neighbourhoods around it still come in free." → "People who live in the city, and the neighbours above all, can still come in free." No card names. |

---

## RA2: the route and listening audit

### MUST

| ID | What was done |
|---|---|
| M1 | **Tracks:** see the lead's mushroom decision above.<br>**PLAN_V2** (so the translators don't bring the mushroom back):<br>• §1 route: "the mushroom pavilion (B)" → "the other gatehouse, the one without the tower (B)".<br>• ALT-W is marked as applied by default.<br>• ALT-Q2's 043 cue: "the house with the mushroom on its roof" → "the gatehouse without the tower".<br>• §2: 001 P6, the 003 cue, the 005 cue and 006 @room/look are replaced by their as-written texts.<br>• §3 bridges: 002 H/E>004 and 004 E>006 (as written), 004 H>015 and 010 E>014 (M2 text).<br>• §5: "tower left / mushroom right" → "tower left / the other gatehouse right".<br>• The audit-resolution row for RA M2 is updated.<br>**ONSITE:**<br>• l.41: "(the other gatehouse, without the tower)", with the cue list corrected.<br>• l.163–164: "along the inside of the wall to the two gatehouses".<br>• The 006 tick: "the gatehouse without the tower".<br>• The bridge ticks 002 and 004 E>006.<br>• O2/E103 is kept as a question only. |
| M2 | See the lead's no-queue decision above. Also: ONSITE O10 gains a no-queue spot test, the 014 tick gains a "no queue" spot, and the PLAN §2 cues for 012/013 and the §3 bridges are changed. Bridge 010 E>014 is 45 words before its title: "to the esplanade," was dropped to stay within the 45-word limit. |
| M3 | See the lead's decision on 036 above. ONSITE O7 and the 036 tick now carry the sea and towers keep-or-cut ticks. |

### SHOULD: route and placement

| ID | What was done |
|---|---|
| R1 | **Held for O9.** It depends on a site fact that is still unknown. The whole ALT-G2 text (the 001 Carmel line, the 012/013 cue, 006's main-stop sentence) and the O9 question "do you pass the Low Viaduct or the Marianao steps-ramp? Time it" are written into ONSITE O9. 001 is unchanged and stays at its 360-word cap. |
| R2 | 001 now says "a little over two hours" (see the lead's length decision). Cuts:<br>• 003: "The park's page on this entrance says it plainly." became an inline attribution, and "That iron was shaped for another house…" was cut.<br>• 011: "From here you can see it for yourself.", "Her verdict was dry and clear." and "Her analysis found the vault stable." (replaced by S1).<br>• 013: the MUHBA vegetation line.<br>• 019: "On that reading, the creature carries its patron's beliefs."<br>• 020: "She named none of them." and "Nobody has found it in Gaudí's own words."<br>• 026: the "completely different look" sentences (−27).<br>• 027: the closure sentence.<br>• 029: "There he lived in a small study, surrounded by plans and models, with a simple bed…" → "for a small study at the Sagrada Família".<br>• 031: "Not a lawn and a flower bed…"<br>• 032: the La Pedrera sentence.<br>• 035: the 1986 sentence.<br>• 038: the iron-door sentence and "the patient part of the story".<br>• 040: "Its pages don't say who carved her either." and "Look along the row… decide for yourself."<br>• 044: "Two years later, neighbours told a local broadcaster that the park had improved." was folded into the iguana sentence ("Two years later, the head of one residents' association told a local broadcaster, in Catalan:").<br>Full: −661 words. |
| R3 | 034: "And the square behind you is the roof of the hall of columns." → "And this whole square is the roof of the hall of columns." Added to ONSITE O16: "sitting on the bench, do you face the square?" |
| R4 | 036 cue: "Stay at the bench, and look up at the hill…" → "Stay at the bench, but turn away from the city, and look up at the hill above the park, with three crosses on its top". This is provisional. O7 now asks "which way do you turn… note the real turn in words", and the 036 tick has "the turn to the hill". ALT-T1 is listed in @where. |
| R5 | **Partly done.** 024 cue: "a short Extra beside this hall, if its little room is open" → "a short Extra at a little room set in the hall's enclosing wall, if it's open". This is G65's fact, and the cue sentence stays at 30 words or fewer. The real landmark waits for O13, which now asks "where exactly is its door, as seen from inside the hall?" The 024 tick asks for a landmark for the cue. |
| R6 | **Declined, on the lead's instruction:** keep the attributed La Pedrera line in 006's body. No placement field uses it. |
| R7 | ONSITE:<br>• The stale mushroom lines are fixed (M1).<br>• New tests: M2 (O10 and the 014 tick), M3 (O7 and the 036 tick), R1 (O9), R3 (O16), R4 (O7) and R5 (O13 and the 024 tick).<br>• O17 notes that the 040 "decide for yourself" line is gone. |
| R8 | `[O-map, O4]` (028 E>032) and `[O16]` (032 E>034) are removed from the spoken lines. All 21 bridges now have their tags in a comment block at the top of each bridge file (`#   NNN X>MMM: [tags]`), copied from PLAN §3 and updated for ALT-K. `make_lengths.py` reads only lines that start with a track number, so the comments are never spoken. The build was checked. |

### SHOULD: listening

| ID | What was done |
|---|---|
| L1 | See the lead's attribution decision above. Wording changes:<br>• 002: "In the park's own words, it's…" → "The park describes it as…". "In the park's own history, he wanted to recreate the British residential parks:" → cut; the sentence now reads "Güell spelt it in English on purpose: an English word for an English idea…".<br>• 003: "The park's own history says" → "The park's history says".<br>• 005: "A study written for its restoration found" → "Its restorers found". "The restoration study describes it as a hyperbolic paraboloid" → "It's a hyperbolic paraboloid".<br>• 006: "Its ground-floor walls are half a metre thick, the restorers found, of stone from the park's old quarries."<br>• 007: "As built, this floor held…"<br>• 008: "This level held four bedrooms, with an attic space above them."<br>• 010: "A study of the gatehouses says, in Spanish, that…" and "Their names 'already appeared…'".<br>• 011: "Its official description reads like a diagram: it…"<br>• 012: "The park lists the bones" → "Among them were the bones".<br>• 015: "The estate was laid out in 'some 60 triangular-shaped plots'. Each was to have 'sewerage…'", with the two attributions dropped.<br>• 016: the op7 stair description paraphrased, and "The park's works pages call it the Monumental Staircase." cut.<br>• 018: "The park names the dragon's mouth as the tank's overflow." → "Its mouth was the tank's overflow."<br>• 019: "…and a salamander in the park's own careful wording" → "A dragon to most visitors, a lizard to a zoologist, and a dragon or salamander to the park."<br>• 021: "The official count is exact:…" and "The outer ones, the park says, 'slope…', which is 'clearly contrary…'"; "and the park has counted" cut.<br>• 026: "Many of them died."<br>• 031: "The park lists twenty-five kinds of bird here".<br>• 032: "The rest is 'held up…'".<br>• 039: "The same description calls it…"<br>• 042: "In 1931 it 'became a municipal public school'".<br>• 044: "One of its aims is…" |
| L2 | See the lead's motto decision above. |
| L3 | a: 043 now opens "[warmly] In the early 1920s the city bought…".<br>b: 041 "So why would a rich industrialist leave a palace for a farmhouse?".<br>c: 002 opens "This wall was built to close an estate off from the city.", and the British-parks line is dropped.<br>d: 006 "…and since 2010 the city's history museum has run it."<br>e: 032's La Pedrera sentence is cut.<br>f: 034 "[amused] There's a favourite story about this bench, and even local television has told it." |
| L4 | a: 007's hook is rewritten, and "built for the man who kept the gate, right beside it" is cut.<br>b: 013 "For now, the path higher up, on to the top bridge, is closed for works."; 027's sentence is cut.<br>c: 013's MUHBA line is cut.<br>d: 031 "In the same museum's story for schoolchildren, Güell has the hill replanted…".<br>e: 035's opener is rewritten (see FA2 S2).<br>f: 038's iron-door sentence is cut; the paragraph now starts "This path runs above Casa Larrard, through a pine grove."<br>g: 030 "[curious] How did Gaudí spend his days, in the years he lived up here? The Sagrada Família's own blog has pieced it together."<br>h: 022 "their white skirts of broken tile"; 023 "Trencadís is broken-tile mosaic." cut.<br>i: **declined** (marked NICE in the audit). 029 keeps the verified G79 quote, because without it 029 would fall to about 183 words, close to the R minimum. 029 already lost its bed sentence and its motto. |
| L5 | • 021: "A market under a temple's roof, built ahead of its customers."<br>• 026: the sentence ends at "with its own garden round it."<br>• 036: "Most of them went elsewhere." The payoff is kept.<br>• 045: "A square on its roof, for crowds that came only later."<br>"never came" is now spoken only in 015 and 036's payoff. |
| L6 | • 018: "Nobody can say for sure." cut; "puts it plainly" → "says".<br>• 020: "Nobody has found it…" cut.<br>• 040: "It's a theory, not a fact." → "It's one reader's theory."<br>• 010: "puts it plainly" → "says".<br>• 028: "As Bassegoda wrote, in Catalan:".<br>• 012: FA2 N5.<br>• 003: rephrased.<br>• "in one line": 014 "That is the pitch."; 045 "sums it up:".<br>• 004, 034 and 032 are kept, as the audit advised. |
| L7 | • 021: "The tilt is real, and it carries weight."<br>• 032: ends on "A theatre on the roof of a market."<br>• 039: "Shelter for walkers, and a prop for the hillside…" cut. |
| L8 | 041: "Joan Bassegoda described the Larrard family…" |
| L9 | 045: "Francesc Berenguer, Gaudí's right hand, drew the house where Gaudí lived. The builders were an uncle and his nephew." "Theatre" is handled under L5. |
| L10 | 038: "On a hill that a war once stripped…" cut, and "A war took almost every tree on this hill. The pines came back." is now untagged. |
| L11 | 007's hook: "Small as it is, this house was built with great care. The city's history museum describes it as 'a small space, designed to be used by a humble family', and says it shows 'great richness and compositional complexity'." The audit's own replacement opened with a command ("Step inside"), which the lint and the brief forbid. "A caretaker's family lived here" was avoided because NEVER bans the caretaker's family. aj4's full sentence is in @sources. |
| L12 | • 022: "The bench sits on top of the colonnade along the front. There, the park describes a conduit that…"<br>• 023: "…puts it in Catalan. Jujol 'designs…'"<br>• 020: "He was reported as saying:"<br>• 036: the towers sentence is now 21 words. |
| L13 | 023: "'decorated with original tile-shard mosaics' made by Jujol." |

### NICE

| ID | What was done |
|---|---|
| N1 | 044: "When charging began, in October 2013,". A look was added, position-safe: "Look across at the two gatehouses, and the crowd between them." |
| N2 | 020: "As reported in English" → "He was reported as saying". One language tag ("in Spanish") remains. |
| N3 | 034: "Barcelona's water museum adds…". Every "city history museum" became "the city's history museum": 013, 031, 036 and 041 were changed. |
| N4 | 027: "The magazine Time Out describes it". |
| N5 | 007, 008, 009 and 030: the internal notes are moved inside the bracket tags. 009 keeps the visitor line "Do not climb the stair unless it is open to visitors." "[O7]" was removed from 037 @room and "[O27]" from 038 @room. The "(official D/E/H/I)" labels in @room are kept because they name the operator's map letters, which visitors can use. route_map's `tidy()` already hides bracketed tags. |
| N6 | 029's bed line is cut (R2). 042: "This estate was once offered to a king.", and the motto became "Not a king's palace, but a school…". 013: "hard to work" is cut. 030's "commissioned … in 1883" is kept: it is in 030's @what and the facts audit did not flag it. |
| N7 | Not changed. 043's Gaudí Year line is already its own sentence, and it is on the DATED list (cut after 31 Dec 2026). |
| N8 | 033: "finished at the top of the hill above the park". |
| N9 | 015: "A telephone, on a bare hill, at the start of the twentieth century." cut. |
| N10 | Bridge 018 H>022: "walk in among the columns of the hall." |
| N11 | = L4i, declined. |
| N12 | 024 and 025 cues: "up its right-hand side, as you came in from the stairway," (O-map and O4 are already in their tags). 025 had to drop its DATED "Visitors have been able to see it since September 2020." to stay under the X cap of 230. op23's "until now had not been accessible" still implies the opening. |
| N13 | **Declined.** PLAN P3 sanctions the line. "Some tours also climb…" would be heard as other companies' tours, and 001 is at its cap. |
| N14 | 008: "Why the estate failed is told at the foot of the great stairway." This works in both orders, so it is safe under ALT-Q2. |
| N15 | **Declined.** The [pause] pattern costs no words to leave alone. Thinning it is a direction pass for the render. |
| N16 | **Not changed.** This is a calibration of the rendered silences for the first render. "A little over two hours" now covers the ≈ 125–130 range. |
| N17 | 035: the 1986 sentence is cut. |
| N18 | = FA2 N20. |
| §6 | **Not done, for the lead.** The pronunciation additions are not part of this pass: Kopsida, phylloxera, troglodyte, Eusebio, Gamarra and García, Eurocatalana, La Veu de Catalunya, hoopoe, "molt tensa", Ara, Vicky Cristina Barcelona and Juan Antonio. "Josep M." is no longer spoken. "Museu de les Aigües" (034) and "Berdié" and "Pardo" (045) are now gone from the spoken text, so they can drop out of the lexicon list for 034 and 045. |

---

## For the lead
- **036 cue (R4):** "turn away from the city" is provisional until O7. **024 cue (R5):** it needs O13's landmark. **R1/ALT-G2:** the full text is in ONSITE O9.
- **Still RC before recording:**
  - the Suns' restoration year (024 says "Later");
  - whether the April 2026 dinner happened (033 now says only that the neighbours were invited);
  - the manifesto's date (044: "At one point").
- **PLAN_V2 changes:** only the lines listed under RA2 M1 and M2, and the two "Spoken in 001" lines. The text of the lead's decision 1 ("about two hours") was left as written. The lead may want to restate it as "a little over two hours".
- **018 and Bassegoda:** 018 now names "the Gaudí scholar Joan Bassegoda" (FA2 N7). For H and E this is now his first appearance, before 022's full form, which stays.

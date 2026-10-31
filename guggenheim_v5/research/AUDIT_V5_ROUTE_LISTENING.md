# Guggenheim Bilbao V5: ROUTE and LISTENING audit (independent), 31 Oct 2026

Scope: route, shorter versions, listening, standard, tone. Facts are left to the other auditor; where a fact problem also hurts the route or the ear, it is noted and passed on.
Inputs: 29 tracks (v5/tracks), v5/PLAN.md §1–§6, v5/ONSITE_CHECKLIST.txt, research/VISIT_ROUTE_AND_SPACES_OCT2026.md, research/map/OFFICIAL_MAP_NOTES_30OCT2026.md plus the 5 map screenshots, v5/bridges/*.txt, and the writers' notes. `python3 v5/lint.py`: 29/29 OK. No track was edited.

**Counts: 6 MUST · 22 SHOULD · 20 NICE.**

The route itself is sound. The cue chain in Full is unbroken: every cue names the next stop's @title, with "·" for "—" and the quotation marks dropped. The order matches the building and the map: plaza at floor-2 level, down the stairway, ZERO, Atrium, 101 seen from the Atrium, 104 as a dead end, terrace, 204 balcony, 304 balcony, out, river walk, pond, Maman, La Salve. Kapoor is drawn west of 101, Maman north of the west end of 104, and La Salve over 104 further east, so pond → Maman → bridge is right. No track uses left/right or a compass word. Only 101, 104, 204 and 304 are named. There are no prices, hours or tickets. Every length is in range.

The problems are in five areas:
- the welcome's Full time;
- the 021 walk to the river, which lost its directions;
- the bridges;
- the Extras announced to shorter-version listeners;
- a handful of things a TTS voice will misread.

---

## 1. Verdict per track

| Track | Words* | Verdict | One line |
|---|---|---|---|
| 001 | 358 | **MUST** | Says Full is "about an hour and forty minutes"; PLAN §3 says "about an hour and a half" (M1). |
| 002 | 353 | SHOULD | The cue dropped "on the city side": "in front of Puppy" is ambiguous to someone facing Puppy (S10). |
| 003 | 224 | SHOULD | Tone right. But the memorial's last words are the title "Our town is dying", and the cue is a 39-word sentence (S3, S20). |
| 004 | 355 | OK | Repeats 001's "former wharf" quote and "all costs" (S11, N5). |
| 005 | 260 | OK | |
| 006 | 215 | OK | Never actually invites the listener into ZERO (N10). |
| 007 | 325 | **MUST** | "55m" will be misread (M5). Holzer's gallery is described with the same words later used for 104 (S16). |
| 008 | 316 | SHOULD | "L.E.D." breaks into three sentences on TTS (S21). |
| 009 | 327 | SHOULD | "toruses" unexplained for H and E; the Snake-opening fact is later repeated (S15, S12). |
| 010 | 284 | OK | Commas needed in "Closed Open Closed Open Closed" (N3). |
| 011 | 244 | NICE | "on either side of it" is geometry [O6] (N16). |
| 012 | 299 | NICE | Repeats "Torqued means twisted" (N15). |
| 013 | 341 | SHOULD | Announces an Extra that E doesn't have (S1). Repeats Snake/2005 two tracks after 009 in E (S12). |
| 014 | 175 | OK | |
| 015 | 356 | **MUST** | "Advice to Space V" / "Embrace XI": Roman numerals (M4). |
| 016 | 273 | SHOULD | Four recycled lines from 009, 010 and 012 (S14). |
| 017 | 347 | OK | SOM and CATIA need respellings (pronunciation list). |
| 018 | 312 | OK | |
| 019 | 353 | **MUST** | Number pile-up (M3). Garden-path "Guggenheim's spread" (S18). Vidarte "for more than thirty years" (S22). Announces an Extra E lacks (S1). |
| 020 | 202 | OK | Full only, so its callback to the plaque is safe. |
| 021 | 269 | **MUST** | No usable way from the exit to the river walk. PLAN's tagged stairs line and "toward the bridge" were removed, and the only directions come at the end of a track played while walking (M2). |
| 022 | 342 | SHOULD | Repeats 015's pond-tribute quote word for word, and no version needs it (S13). |
| 023 | 276 | **MUST** | "F.O.G." (the punchline) and "Expo '70" (M6). "the titanium wall behind it" is geometry [O13] (S9). "Soon after the opening" is ambiguous (S19). Announces an Extra E lacks (S1). |
| 024 | 224 | SHOULD | The cue gives no direction along the river walk (S8). |
| 025 | 348 | SHOULD | "She" switches from Bourgeois to Maman (S17). The cue has no direction (S8). |
| 026 | 358 | NICE | "it reported" is ambiguous (N8). |
| 027 | 353 | SHOULD | Announces an Extra H and E lack (S1). "LEDs" (S21). "This spot" (N8). |
| 028 | 200 | OK | |
| 029 | 320 | NICE | Repeats 001 and 019 (N6). "You've walked the whole of it" overclaims for H (N9). |
| Bridges | – | SHOULD | Four bridges lack the next stop's title (002 H>004 is the exception). Problems in 002 H>004 (tone), 009 H>018, 015 E>017 (order) and 018 H>025 (direction, exit) (S2, S4–S7). |

\*Words: the lint count without the "·" token. Ranges: R 180–280, W 250–360, X 150–230, ANCHOR/CLOSE 250–360. All pass. 001 and 026 sit 2 words under the cap, so any fix that adds words there must also cut.

---

## 2. Findings

### MUST

**M1. 001: the Full duration contradicts PLAN §3.**
- Exact words: "The full tour takes about an hour and forty minutes, the essential about an hour and a quarter, and the highlights about three quarters of an hour, walking included." (29 words)
- Problem: PLAN §3 (Counts note, option (a), recommended) and the 001 row both say "about an hour and a half". No file records a decision for "forty minutes". The writer's notes say the times "are PLAN's". The sentence is also over the ear limit.
- Replacement: "The full tour takes about an hour and a half. The essential takes about an hour and a quarter, and the highlights about three quarters of an hour, walking included."
- If the lead prefers ≈ 98 min as "an hour and forty", change PLAN §3 instead. Either way, the two must agree before O20.

**M2. 021 (E and Full): the walk to the river walk has no directions.**
- Exact words:
  - 019 and 020 cues: "leave the museum and make your way round to the river side, and play it as you walk."
  - 021 paragraph 2: "You're heading for the river walk … It's possible to walk all the way round the museum."
  - 021 last paragraph: "If you came out onto the plaza, make your way down to the river walk. If you came out on the river side, you're nearly there. At the water, find the pond beside the building…"
- Problem:
  - The listener starts a two-minute walking track with no way to go. The only instruction, "make your way down", names no stairs and no side, and comes at the end.
  - PLAN's cue carries the allowed, tagged line "the stairs that lead down from the plaza toward the park and the river walk, on the side away from the bridge [O12]" and "walk along the river toward the bridge [O13]". Both were removed (notes 021–029).
  - The Highlights bridge 018 H>025 still has the stairs. So the shorter version is better guided than Full and Essential.
  - The writer's hedge for ALT-X is good. Keep it, but add the route.
- Replacement:
  - 021 paragraph 2: "Keep walking while you listen. If you've come out onto the plaza, take the stairs that lead down from the plaza toward the park and the river walk, on the side away from the big road bridge [O12]. If you've come out on the river side, you're nearly there."
  - 021 last paragraph: "At the water, walk along the river toward the bridge until you reach the pond beside the building, where a tall tree of silver balls stands in the water [O13]: The pond · Tall Tree and the Eye."
  - Optional, in the 019 and 020 cues: "…leave the museum and play the next stop as you go. It tells you the way to the river walk."
  - Net change is about +10 words; 021 stays under 280.

**M3. 019: number pile-up.**
- Exact words: "In its first full year, 1998, about 1.3 million came. In its first three years, almost four million. / In 2025 about 1.3 million came, almost seven in ten from abroad, after a record year in 2023 of just over 1.32 million."
- Problem:
  - That is seven numbers in about 40 words, after the 400,000 opening.
  - "1.3 million" is said twice, and "1.32 million" is indistinguishable by ear.
  - The years run 1998 → 2025 → 2023.
  - Then come "four billion", "twenty years" and "fourteen thousand", which makes 13 figures in 110 words.
- Replacement for paragraphs 2–3 (the second sentence stays the cuttable DATED one): "In its first full year, 1998, about 1.3 million people came. In its first three years, almost four million. / Its best year so far was 2023. In 2025, almost seven in ten visitors came from abroad."
- Optionally also: "…more than four billion euros added to the Basque economy in its first twenty years, and some fourteen thousand jobs in 2025."

**M4. 015: Roman numerals.**
- Exact words: "Advice to Space V" and "Embrace XI".
- Problem: TTS will read "Advice to Space vee" and "Embrace ex-eye".
- Replacement: write "Advice to Space Five" and "Embrace Eleven" in speech, or add both to the pronunciation file (below).

**M5. 007: "55m".**
- Exact words: "The museum gives a different figure: "With a height of 55m"."
- Problem: edge-tts and Kokoro can read "55m" as "fifty-five million" or "fifty-five em". The figure is the whole point of the hook.
- Replacement: "The museum gives a different figure: a height of fifty-five metres."

**M6. 023: "F.O.G." and "Expo '70".**
- Exact words:
  - "followed by three letters, F.O.G. And those letters stand for Frank O. Gehry."
  - "the Pepsi-Cola Pavilion for Expo '70".
- Problem:
  - The reveal depends on hearing three letters. "F.O.G." may be read as the word "fog", or as "F. O. G." with sentence breaks.
  - "'70" may be read "apostrophe seventy".
  - "Frank O. Gehry" can also pause after "O." as if at a full stop.
- Replacement:
  - "followed by three letters: F, O, G. And those letters stand for Frank O Gehry."
  - "for Expo 1970".
  - Also add "F.O.G." to the pronunciation file as "F, O, G" so the track title is safe.

### SHOULD

**S1. 013, 019, 023, 027: Extras announced to listeners who don't have them.**
- Exact words:
  - 013: "There's a short Extra you can play here or on the walk back: the Serra that vanished."
  - 019: "There's a short Extra you can play here in the Hall before you leave: opening day, 1997."
  - 023: "There's a short Extra here, about the fire in this same pond…"
  - 027: "There's a short Extra here, about the two architects who lost."
- Problem: E has none of the four Extras, and H doesn't have 028. Those listeners are told to play something that isn't in their list, and no bridge corrects it ("Extras-only skips are silent").
- Replacement: open each with "On the full tour, there's a short Extra here…". For example, 013: "On the full tour, there's a short Extra you can play here or on the walk back: the Serra that vanished. The next main stop is outside: …". The cost is +4 words each. 019 and 027 have room; 013 is at 341.

**S2. Bridge 002 H>004: tone, and an unexplained street name.**
- Exact words: "On this shorter tour, skip the plaque: stay on the plaza and find the view of the whole front of the museum, with Calle Iparragirre at your back."
- Problem:
  - The listener has just heard "Before you go in, one stop that matters … stand quietly beside it." Then "skip the plaque" is jarring next to a memorial.
  - H never hears what Calle Iparragirre is (003's cue explains it, and H skips 003).
- Replacement (41 words): "On this shorter tour there's no stop at the plaque. Pause there as you pass, if you wish. Then find the whole front of the museum, with the long straight street, Calle Iparragirre, at your back: Museum plaza · Our town is dying."

**S3. 003: the memorial ends on "Our town is dying".**
- Exact words: "[long pause] When you're ready, find a place … at your back: Museum plaza · Our town is dying."
- Problem: The last words after a beat of silence for a man who was killed are "is dying". It is a quote about the city, but on one hearing it lands as a clash.
- Replacement (also splits the 39-word sentence): "[long pause] When you're ready, find a place on the plaza where you can see the whole front of the museum. The long straight street into the city, Calle Iparragirre, should be at your back. The next stop is about how the museum began: Museum plaza · Our town is dying."

**S4. Bridge 009 H>018.**
- Exact words: "On this shorter tour, go back to the Atrium and take a glass lift up. Stop first on the second floor, at the balcony opposite gallery 204, for all eight sculptures from above. Then play the next stop at the third-floor balcony opposite gallery 304."
- Problem:
  - (a) 009 has just promised "In a minute, that will be you", and the bridge sends the listener away without setting foot inside.
  - (b) The 204 balcony is given as a firm stop, but it is O9 CRITICAL; floor 2 is between exhibitions on 2–10 Nov.
  - (c) The next stop's title is not named.
- Replacement (≈ 44 words): "On this shorter tour, step into the nearest sculpture if you like, then go back to the Atrium and take a glass lift up. If you can, glance down from the second-floor balcony opposite gallery 204. Then play Third floor · The metal flower opposite gallery 304."

**S5. Bridge 015 E>017: wrong order.**
- Exact words: "…take a glass lift up toward the third floor, and start the next stop in the lift. If you like, stop first at the second-floor balcony…"
- Problem: The listener hears "start the next stop in the lift" before "stop first". Anyone who acts on the first sentence is already in 017 when the optional stop is offered.
- Replacement (44 words): "On this shorter tour, skip the second-floor stop. If you like, glance down at the Serra from the second-floor balcony opposite gallery 204 on the way. Then take a glass lift on toward the third floor, and start Lifts and walkways · Every piece different in the lift."

**S6. Bridge 018 H>025.**
- Exact words: "On this shorter tour, leave the museum. Take the stairs down from the plaza toward the park and the river walk, on the side away from the bridge. Follow the water past the pond's tree of silver balls, to the giant spider by the footbridge."
- Problem:
  - (a) It doesn't say to skip the stop the 018 cue just announced ("Going down · The Bilbao effect").
  - (b) "Follow the water" has no direction. PLAN's "toward the bridge" was cut for length, but it is the one thing a listener at the bottom of the stairs needs.
  - (c) "the bridge": H has only heard of "the bridge" over 104, so "the big road bridge" is clearer.
  - (d) The next stop's title is not named.
  - (e) It assumes a plaza exit [O11]; 021 now hedges this, and the two should match after O11.
- Replacement (≈ 45 words): "On this shorter tour, skip the stop on the way down and leave the museum. From the plaza, take the stairs down toward the river walk, away from the big road bridge. At the water, walk toward that bridge, past the pond, to River walk · Maman."

**S7. Bridge 004 E/H>007 (and 010 E>013's style).**
- Exact words: "…Play the next stop near its middle, where you can look straight up."
- Problem: This is the only route bridge that doesn't name the stop. The listener has to find "the next stop" in a list where the numbers jump.
- Replacement (≈ 44 words): "…walk on into the Atrium, the tall heart of the building. Near its middle, where you can look straight up, play Atrium · The heart of the building."

**S8. 024 and 025 cues: no direction along the river walk.**
- Exact words:
  - 024: "Now follow the river walk to the giant spider by the footbridge".
  - 025: "Now walk on along the river walk to where you can get close to the museum's titanium skin".
- Problem: At the pond the walk runs two ways. PLAN's cue for 024 says "walk on along the river walk toward the bridge". 023's map hint helps in Full, but 024 is heard after it.
- Replacement:
  - 024: "Now walk on along the river walk toward the big road bridge, to the giant spider by the footbridge [O14]: River walk · Maman."
  - 025: "…walk on along the river walk toward the bridge, to where you can get close to…" [O15].

**S9. 023: geometry not yet confirmed.**
- Exact words: "watch the titanium wall behind it soften and vanish".
- Problem: This presumes the pond lies between the walk and the building, which is O13 (only ABC-BLOG, a low-grade source, says so).
- Replacement: "watch the building soften and vanish" (PLAN's wording).

**S10. 002 cue: an ambiguous "in front of Puppy".**
- Exact words: "In the small square just in front of Puppy, there's a plaque."
- Problem: To a listener facing Puppy, "in front of" can mean between them and the dog. PLAN's cue says "on the city side" [O2], the checklist still tests that phrase, and the writer's notes list it, but the track dropped it.
- Replacement: "In the small square just in front of Puppy, on the city side, there's a plaque [O2]."

**S11. "A former wharf with port and industrial use" is quoted three times.**
- Exact words: 001 ("a former wharf with port and industrial use", on a curve of the river Nervión), 004 ("the site was 'a former wharf with port and industrial use on a curve of the Nervión'") and 021 ("on a former wharf with port and industrial use on a curve of the Nervión").
- Problem: H hears it twice in about five minutes; E and Full hear it three times. 013 and 029 also say "wharf".
- Replacement:
  - 004: "Beyond it is the river, and the working riverbank this museum replaced."
  - 021 opening: "Before there was a museum here, this riverbank worked for a living." Drop the quote and go straight on.

**S12. Snake "here for the opening, the other seven in 2005" is said four times.**
- Exact words:
  - 009: "The oldest, Snake, was here for the opening. The other seven came in 2005."
  - 011: the whole hook.
  - 013: "Snake, the oldest of the eight, was here for the opening. The rest arrived in 2005."
  - 014: "the oldest of the eight pieces".
- Problem: E hears 009 and 013 about six minutes apart. PLAN put the clause in 013 because "E skips 011", but E also hears 009, which already carries it.
- Replacement: in 013, cut the two Snake sentences, keeping "This is where that progression arrives."

**S13. The pond-tribute quote in both 015 and 022.**
- Exact words: "The pond pays tribute to the Nervión estuary and its fundamental role in the development of the city of Bilbao."
- Problem: PLAN gave it to 022 "for H/E who missed 015". But no version has 022 without 015 (E has both; H has neither), so the second use helps nobody.
- Replacement for 022: "[pause] The pond is part of the picture. From the terrace you heard that it's a tribute to the river. The river that shaped the city is echoed here in water, and then mirrored again in steel."

**S14. 016 (Full only) recycles four earlier lines.**
- Exact words:
  - "the viewer loses all reference and does not know what lies ahead" (012);
  - "When you move they move too…" (010);
  - "an enormous, column-free space" (009);
  - "Watch them vanish, then turn up again where you didn't expect" (009: "disappear into a curve, and come out somewhere you didn't expect").
- Problem: The Full listener heard all four within the last 15 minutes. The track reads as a recap.
- Replacement: make them callbacks.
  - "Down on the floor, as you found among the spirals, you lose all reference."
  - "Remember Serra's line, that when you move, they move too? From up here, at last, you can get them. Or nearly."
  - "Notice, too, what isn't there: a single column."
  - Cut the "vanish" sentence or the 009 one.

**S15. 009: "toruses" is unexplained.**
- Exact words: "They end in pieces made from 'sections of toruses and spheres'."
- Problem: 009 is H's only Serra track, and E reaches 013's "a torus is a ring, like a doughnut" ten minutes later.
- Replacement: "They end in pieces made from 'sections of toruses and spheres': rings and balls, cut in steel."

**S16. 007: Holzer's gallery described like 104.**
- Exact words: "Those columns of moving red and blue words, in the gallery that opens off the Atrium, are a work by Jenny Holzer".
- Problem:
  - Two minutes later, E and H hear the bridge describe gallery 104 as "the long gallery that opens off the Atrium", and Full hears 008's cue say the same.
  - Several galleries open off the Atrium, so "the gallery" points nowhere.
- Replacement: "Those columns of moving red and blue words, in gallery 101, which you can see from the Atrium, are a work by Jenny Holzer, made for this building." (PLAN's allowed phrase.)

**S17. 025: "she" switches referent.**
- Exact words: "Bourgeois was a French-American artist, and she made Maman in 1999. She is bronze, marble and stainless steel. She is one of a whole series…"
- Problem: The first "she" is Bourgeois and the next two are Maman.
- Replacement: "…and she made Maman in 1999. The spider is bronze, marble and stainless steel, one of a whole series of spiders…"

**S18. 019: a garden-path sentence.**
- Exact words: "Critics of the Guggenheim's spread around the world had a word for it: McGuggenheim."
- Problem: The ear parses "critics … spread around the world".
- Replacement: "Critics of the Guggenheim's expansion around the world had a word for it: McGuggenheim."

**S19. 023: "the opening" is ambiguous.**
- Exact words: "Robert Rauschenberg invited her to make it for his retrospective here. Soon after the opening, he bought it…"
- Problem: In this guide "the opening" has meant the museum's opening (002, 003, 009, 011, 013). Here it means the 1998 show's.
- Replacement: "Soon after his show opened, he bought it…" (The facts auditor should confirm the purchase.)

**S20. Long sentences.**
- **003 cue: 39 words.** Fixed in S3.
- 007: "The museum describes it as 'an ample space…', with 'curved volumes…'" is 32 words of quotation in one breath. Split it: "The museum describes 'an ample space flooded with light and covered by a great skylight'. It has 'curved volumes and large glass curtain walls that connect the inside and the outside'."
- 009: "What fills it is The Matter of Time … just over a thousand tonnes of it in all." is 30 words. Split after "Richard Serra".
- Over 25 but acceptable because they end in a cue or a clean list: 001 cue (31), 026 cue (31), 007 cue (31), 013 (30).

**S21. "L.E.D." and "LEDs" (008, 027).**
- Problem: The full stops in "L.E.D." become sentence breaks on edge-tts ("L. E. D. signboards").
- Replacement: speak "LED" (pronunciation file: "L.E.D." and "LED" → "L-E-D"; "LEDs" → "L-E-Ds").

**S22. 019 and 011: Vidarte's tenure.**
- Exact words:
  - 019: "The museum's director for more than thirty years, Juan Ignacio Vidarte".
  - 011: "The museum's director then".
- Problem:
  - 019 implies he is still director, which is a present-tense, dated claim; PLAN NOT says "the director's name today".
  - 011's "then" implies he no longer is.
  - The listener can't reconcile the two.
- Replacement for 019: "The museum's long-time director, Juan Ignacio Vidarte, put it more carefully." Passed to the facts auditor.

### NICE

- **N1.** The " · " in every cue: the pipeline has no rule for it. Listen-QA one cue per renderer (Ava, Andrew, Brian, Kokoro) to check that it gives a short pause and is not read aloud. The cue punctuation is also inconsistent: 011–020 use ". Title" and the rest ": Title". Pick one.
- **N2.** 021 cue "Tall Tree & the Eye": write "and" in speech.
- **N3.** 010 "Closed Open Closed Open Closed" and 012 "Open Left Closed Right" / "Right Left" need commas, or TTS runs them into one word string.
- **N4.** 008 "LIKE BEAUTY IN FLAMES": all capitals can trigger letter-spelling. Write it in title case.
- **N5.** 001 "the Basque side agreed to bear all the costs" and 004's "'All costs, operating and capital' would be borne by the Basque side" sit five minutes apart in every version. Cut the 001 sentence. The hook still works.
- **N6.** 029 repeats things listeners already heard:
  - from 019: "400,000 … about 1.3 million" (E and Full);
  - from 019: the "Bilbao effect" opener;
  - from 001: "Gehry died in December 2025, at ninety-six", word for word.
  The 029 lines are needed for H. To soften them for E and Full: "Gehry died in December 2025." (no age), and "Remember the target…" can't be used because H didn't hear it. Leave the visitor numbers as they are.
- **N7.** 026 "remember: no two joints in the building are the same" is a fair callback; every version with 026 has 017. You could make it explicit: "the builder's line from the walkways".
- **N8.** Ambiguous references:
  - 016 "Its guide for teachers" (its = the route?) → "The museum's guide for teachers".
  - 027 "This spot, the museum notes, is 'the immediate entrance…'" → "This bridge, the museum notes, marks…".
  - 026 "it reported" (after "a titanium executive said") → "BusinessWeek reported".
- **N9.** 029 "You've walked the whole of it" and "Steel you could walk through": H never walks the Serra. Use "You've walked it, inside and out."
- **N10.** 006 never says to go in, although Full budgets a two-minute look. Add: "Go in and take a look. Afterwards, walk on into the Atrium…" Don't say how long it lasts.
- **N11.** 022 "Kapoor talks about working in what he calls 'form languages'" is jargon with no payoff. Cut it (−12 words).
- **N12.** Bridge 025 H>027 "its red frame" (the tower's?) → "the red frame on the bridge".
- **N13.** 002: put a [pause] before the plaque cue, so the "half-dressed" joke doesn't run into "one stop that matters".
- **N14.** 003 "This small square carries the name…" and "Here, he is Txema Agirre" assume the plaza sign (O2). Keep O2's photo of the sign as a gate for these two lines.
- **N15.** 012 repeats 010's "Torqued means twisted". Cut it or make it "Torqued, remember, means twisted".
- **N16.** 011 "the twisted pieces on either side of it" is placement [O6]. If ALT-S applies, or Snake is not between them, use "the twisted pieces you've just been in".
- **N17.** 001 promises Chillida, Kapoor, fog, fire and Holzer's columns. H never stops for most of them. Consider "The full tour covers…" or "Along the way you'll meet…" (lead's call).
- **N18.** Gallery numbers: edge-tts reads "104" as "one hundred four" or "one hundred and four". Most English speakers say "one-oh-four". Add respellings for 101, 104, 204 and 304 (the Setas pronunciation.py already has a room-code helper).
- **N19.** 019's own "400,000" appears three times (opening, figure, close). That's acceptable as framing, but the closing "Four hundred thousand was the target" could go.
- **N20.** 015 "two cranes swung two steel sculptures": the doubled "two" is fine on paper but clumsy aloud. Use "a pair of cranes swung two steel sculptures".

---

## 3. Route check (item 1) in brief

- **Cue → @title chain (Full):** all 28 joints are correct. Extras are announced, and each Extra repeats the next main stop.
- **Order versus the building:** correct. The map puts Puppy on the floor-2 plan (south of 207), ZERO beside 105, 101 off the Atrium, and 104 running east from the Atrium with a lift at its Atrium end and no far door. 204 is opposite the west end of 104 on floor 2, and 304 is on floor 3. Kapoor is west of 101, Maman north of the west end of 104, and La Salve over 104.
- **[O#] presented as certain:**
  - the 021 river route (M2, under-specified rather than over-certain);
  - 023 "behind it" (S9);
  - 009 H>018 "Stop first … 204" (S4);
  - 011 "on either side" (N16);
  - 003 sign (N14).
  These are acceptable as long as the tags stay: 104 as a dead end ([O6], PLAN-sourced), 023's map-attributed Maman placement, and 015's view, which is limited to the pond, Kapoor and the fire and hedges Maman ("If you can see…").
- **Gallery numbers:** only 101, 104, 204 and 304. No "first floor" in speech.
- **Left/right, compass, "straight ahead":** none. ("at your back" in 003 and 004 is allowed.)

## 4. Standard (item 4)

- Ranges: all pass (table above).
- No prices, tickets or opening hours. "On the hour" appears in 001, 022, 023 and 029. "After dark" appears in 001, 015, 023, 024 and 029. The 019 "euros" is economic impact, not a price, and the lint allows it.
- The welcome's durations: Essential and Highlights match PLAN; **Full does not (M1).**
- Bridges: 15–45 words each, within the brief.

## 5. Tone around 003 (item 5)

003 is restrained and factual:
- short sentences;
- no weapon, wound, date of death or attackers;
- "hero" only in Ardanza's mouth;
- [quietly]/[reverent] only, and a held silence before the cue.

Nothing flippant is inside it. The issues are at its edges:
- the title "Our town is dying" as its last words (S3);
- the H bridge's "skip the plaque" straight after "one stop that matters" (S2);
- 002's "half-dressed" joke right before the plaque cue (N13).

020's one quiet line for him (Full only) is right.

---

## 6. Play-throughs (item 2): what the listener hears at each joint

### Full (001 → 029)

- **Plaza.** 001 sends the listener to Puppy, 002 to the plaque, 003 to the Iparragirre view, and 004 to the stairway. Clean, except that 003 ends on "Our town is dying" (S3).
- **Going in.** 005 is heard on the stairs and points to ZERO's door. 006 never quite says "go in" (N10), then sends the listener to the middle of the Atrium. 007 sends them to the 101 viewpoint, and 008 to "just inside" 104.
- **Serra.** 009 → 010 → 011 → 012 → 013 walk the gallery in ZWIR order. 013 announces Extra 014 and the terrace, and 014 repeats the terrace. Snake's "opening/2005" fact has now been heard four times (S12).
- **Up and down.** 015 sends the listener up to the 204 balcony. 016 is the Serra seen from above, but half of it is recap (S14). 016 → 017 in the lift → 018 at the 304 balcony → 019 going down. 019 offers Extra 020 in the Hall, and both 019 and 020 say "leave the museum and make your way round to the river side".
- **Outside.** 021 plays while the listener walks, but the way there arrives only at its end, with no stairs or side named (M2). The pond comes next: 022 → 023 → 024. 023's map hint points toward the bridge; 024 gives no direction (S8).
- **River walk.** 025 Maman → 026 titanium (no direction, S8) → 027 La Salve → 028 → 029. The close works.

### Essential (001 002 003 004 007 009 010 013 015 017 018 019 021 022 023 025 026 027 029)

- **004 → bridge → 007.** The 004 cue says "Play the next stop as you walk down: The stairway · Going down to go in". The bridge says "skip the stairway stop … Atrium … play the next stop near its middle". It works, but it doesn't name the stop (S7).
- **007 → bridge → 009.** The 007 cue sends the listener to the 101 viewpoint, then the bridge says "skip the columns … 104 … play The gallery under the bridge". Fine, but 007 has just called Holzer's room "the gallery that opens off the Atrium" (S16).
- **009 → 010** is a normal cue. **010 → bridge → 013:** "walk on … past Snake and the spirals … play Torus and sphere". Good.
- **013 → 015.** The listener is offered "a short Extra … the Serra that vanished", which isn't in E (S1), then sent to the terrace. They also hear Snake/2005 again after 009 (S12).
- **015 → bridge → 017.** The cue says "Second floor · Serra from above". The bridge says skip it, start 017 in the lift, then "stop first" at 204: back to front (S5).
- **017 → 018 → 019** are normal cues. **019 → 021:** an Extra is offered that E doesn't have (S1), then the walk to the river has no directions (M2).
- **021 → 022 → 023.** 022 repeats 015's tribute quote word for word (S13). 023 offers an Extra E doesn't have (S1), then points to Maman via the map hint. Good.
- **025 → 026 → 027 → 029.** No direction from Maman (S8). 026's "no two joints" callback is valid, since 017 is in E. 027 offers Extra 028, which E doesn't have (S1).
- **No back-reference problem.** E hears nothing that depends on a skipped track:
  - "the twisted ellipses", "the officer whose name is on the plaza" and "Chillida's steel" are all in Full-only tracks (012/016, 020, 024);
  - "the guide for teachers" is introduced in full in 013 ("The museum's guide for teachers").

### Highlights (001 002 004 007 009 018 025 027 029)

- **002 → bridge → 004.** "One stop that matters … stand quietly beside it" is followed straight away by "skip the plaque" (S2). The bridge also says "Calle Iparragirre" without explaining it.
- **004 → bridge → 007, and 007 → bridge → 009.** As in E.
- **009 → bridge → 018.** 009 ends "In a minute, that will be you. Walk in to the first sculptures…", and the bridge says "go back to the Atrium". The listener never walks the Serra (S4). The 204 stop is given as certain [O9], and the stop is not named.
- **018 → bridge → 025.** The 018 cue says "Play the next stop on the way down", and the bridge says only "leave the museum" (it never says skip). Then: stairs from the plaza, "Follow the water" with no direction, "the bridge" unexplained, and no title (S6). This is the longest unguided walk in any version. It is better than E's 021 because the stairs are named.
- **025 → bridge → 027.** "Skip the titanium … toward the big road bridge, La Salve … La Salve Bridge · The bridge, the tower and the red arches". Good ("its red frame", N12).
- **027 → 029.** Extra 028 is offered but H doesn't have it (S1). 027's Kapoor callback is correctly hedged for H ("If you looked into…").
- **029.** "Think back to the plaza" works (004 is in H). "Steel you could walk through" and "You've walked the whole of it" overclaim for H (N9).
- **No missing bridge.** Every non-Extra skip in E and H has one: 002H, 004E/H, 007E/H, 009H, 010E, 015E, 018H, 025H. The only gaps are the four silent Extra skips, which still announce the Extras (S1).

---

## 7. Pronunciation file: names a TTS voice may mispronounce

Castilian values are used for Spanish (Bilbao usage); Basque *tx* = "ch", *tz* = "ts", *rr* trilled.

| Text | Respelling | Track(s) |
|---|---|---|
| Guggenheim Bilbao Museoa | GOOG-en-hime bil-BAH-oh moo-SAY-oh-ah | 001, 029 |
| Bilbao | bil-BAH-oh | many |
| Nervión | nair-VYOHN | 001, 004, 015, 021, 022 |
| Txema Agirre | CHEH-mah ah-GEE-rreh | 002, 003, 020 |
| José María Aguirre Larraona | ho-SEH mah-REE-ah ah-GEE-rreh lah-rrah-OH-nah | 003 |
| Ertzaintza | air-TSINE-tsah | 003 |
| ETA | EH-tah (not "E-T-A", which a voice can hear as "estimated time of arrival") | 003 |
| José Antonio Ardanza | ho-SEH an-TOH-nyoh ar-DAN-thah | 003 |
| Juan Carlos / Queen Sofía | hwan KAR-los / soh-FEE-ah | 003, 020 |
| Calle Iparragirre | KAH-yeh ee-pah-rrah-GEE-rreh | 003, 004, bridge 002H |
| Coop Himmelblau | kohp HIM-mel-blow | 004, 028 |
| Arata Isozaki | ah-RAH-tah ee-soh-ZAH-kee | 004, 028 |
| Thomas Krens | krens | 004, 015, 028 |
| IDOM | EE-dom | 005, 026 |
| Juan Ignacio Vidarte | hwan eeg-NAH-thyoh vee-DAR-teh | 005, 011, 019 |
| Ferrovial | feh-rroh-VYAHL | 005 |
| Juan Ramón Pérez | hwan rah-MOHN PEH-reth | 005 |
| txalaparta | chah-lah-PAR-tah | 006 |
| Biscay | BIS-kay | 006 |
| Local Projects | (fine) | 006 |
| 55m | fifty-five metres | 007 |
| L.E.D. / LED / LEDs | L-E-D / L-E-Ds | 008, 027 |
| LIKE BEAUTY IN FLAMES | Like Beauty in Flames | 008 |
| Arno | AR-noh | 008 |
| 101 / 104 / 204 / 304 | one-oh-one / one-oh-four / two-oh-four / three-oh-four | 007–018, bridges |
| Torqued | torkt | 010, 012, 016 |
| Museo Reina Sofía | moo-SAY-oh RAY-nah soh-FEE-ah | 014 |
| Guernica-Bengasi | gair-NEE-kah ben-GAH-see | 014 |
| Ara (the paper) | AH-rah | 014 |
| Carmen Jiménez | KAR-men hee-MEH-neth | 013 |
| Eduardo Chillida | ed-WAR-doh chee-YEE-dah | 001, 015 |
| San Sebastián | san seh-bas-TYAHN | 015 |
| Advice to Space V | Advice to Space Five | 015, 024 (title only) |
| Embrace XI / Besarkada | Embrace Eleven / beh-sar-KAH-dah | 015 |
| Artxanda | ar-CHAN-dah | 015 |
| CATIA | KAH-tee-ah | 017 |
| SOM | S-O-M | 017 |
| John Zils | jon ZILZ | 017 |
| BIM | bim | 017 |
| gefilte | geh-FIL-tuh | 018 |
| Frank Owen Goldberg | (fine) | 018 |
| Pritzker | PRITS-ker | 018 |
| Beatriz Plaza | beh-ah-TREETH PLAH-thah | 019 |
| McGuggenheim | mik-GOOG-en-hime | 019 |
| Abandoibarra | ah-ban-doy-BAH-rrah | 021 |
| Euskalduna | ews-kal-DOO-nah | 021 |
| Bilbao Ría 2000 | bil-BAH-oh REE-ah two thousand | 021 |
| Tall Tree & the Eye | Tall Tree and the Eye | 021 |
| Anish Kapoor | ah-NEESH kah-POOR | 001, 015, 022, 027 |
| Fujiko Nakaya / Ukichiro | foo-jee-koh nah-kah-yah / oo-kee-chee-roh | 023 |
| F.O.G. | F, O, G | 023 (and its title in cues) |
| Frank O. Gehry | frank oh GAIR-ee | 006, 022 cue, 023 |
| Expo '70 | Expo nineteen seventy | 023 |
| Rauschenberg | ROW-shen-burg | 023 |
| Praemium Imperiale | PRY-mee-um im-peh-ree-AH-leh | 023 |
| Yves Klein | eev KLINE | 001, 015, 024 |
| Sorbonne | sor-BON | 024 |
| Krefeld | KRAY-felt | 024 |
| Mies van der Rohe | mees van der ROH-uh | 024 |
| Louise Bourgeois | loo-EEZ boor-ZHWAH | 001, 015, 025 |
| Maman | mah-MAHN | 001, 015, 023–025 |
| Ottawa | (fine) | 025 |
| Príncipes de España | PREEN-thee-pes deh es-PAH-nyah | 027 |
| La Salve | lah SAHL-veh | 026, 027, bridges |
| Juan Batanero | hwan bah-tah-NEH-roh | 027 |
| Daniel Buren / Arcos rojos / Arku gorriak | dan-YEL bu-REN / AR-kos ROH-hos / AR-koo goh-RREE-ak | 001, 022, 027 |
| Santiago Calatrava / Rafael Moneo / Álvaro Siza | san-TYAH-goh kah-lah-TRAH-vah / rah-fah-EL moh-NEH-oh / AL-vah-roh SEE-zah | 028 |
| Arolsen | AH-rol-zen | 002 |
| Jeff Koons | (fine) | 002, 015 |

# Setas de Sevilla V5.1 (EN): route and listening audit

Independent audit, 31 Oct 2026. Scope: route, shorter versions, listening, standard. Facts are checked by a separate auditor and are not judged here.

Read for this audit: `v5/tracks_v51/001–021.perf.txt`, `bridges_001-011.txt`, `bridges_012-021.txt`, `v5/PLAN_V5_1.md`, `v5/PLAN.md` (route rules, §3 bridges, §4 NEVER), `v5/ONSITE_CHECKLIST.txt`, `research/VISIT_ROUTE_AND_SPACES_OCT2026.md`, the V5.1 writer notes, and `lint.py` (all 21 tracks pass with `TRACKS_DIR=v5/tracks_v51`). No track was edited.

Verdicts: **OK** means no change needed (NICE items may still apply). **SHOULD** means fix before recording. **MUST** means it breaks the TTS, a shorter version, or one-hearing sense.

## 1. Summary table

| Track | Verdict | One line |
|---|---|---|
| 001 Welcome | MUST | Cues are correct: "Found under a car park", plus the closed-Antiquarium skip to "A plaza with many lives". But "Mirador 360º" is a TTS hazard, and the date is in digits. |
| 002 Found under a car park | SHOULD | Cue correct. "some 1,200 years … to the 1200s" puts two numbers that sound alike in one sentence. The cue promises a spot that "shows how deep it goes", which is unconfirmed (O4). |
| 003 Seville stacked up | OK | Cue correct ("Medusa, the guardian"). "That first test dig" points back to 002, which is safe because both are Full only. |
| 004 Medusa, the guardian | OK | Cue correct. "The scholar" is introduced here, and 005–006 rely on it (Full only, consecutive). |
| 005 Bacchus and the dinner party | OK | Walk-along with no position claims. Cue correct, with a fallback ("or as you walk on"). |
| 006 Two birds and a wine bowl | OK | Cue correct, with the fallback "If you passed it earlier…" in case the order differs (ALT-A). |
| 007 The Almohad house | OK | Cue correct (exit signs, then the lifts, then "A plaza with many lives"). It repeats 003's depths (NICE). |
| 008 A plaza with many lives | OK | Works as the Essential entry point. Cue correct ("Mushrooms of wood"). |
| 009 Mushrooms of wood | SHOULD | Cue correct. 216 words run before "As you step out", so listeners are off the lift long before. "Singular trees" won't mean anything to an English ear. This is the first of the vault and fig-tree repeats. |
| 010 The Cathedral and the Giralda | MUST | Cue correct (Giralda on your left = west ✓). "The same Moorish Seville as a house found under this square" refers back to an Antiquarium track that Essential skips. The vault story comes three times across 009 and 010. |
| 011 The river, Triana and the Aljarafe | SHOULD | Cue correct. "AD" appears twice (TTS). "Toward the river lie the rooftops of Triana, on its far bank" has the geography muddled. |
| 012 The glue that had to be baked | MUST | "Mirador 360º" is in the cue. "60 degrees" gives no unit, and US listeners will hear Fahrenheit. |
| 013 The highest point | SHOULD | All three directions are correct and derived from the compass. For Essential and Full it re-tells 010 and 011 almost word for word. |
| 014 Love it or hate it | SHOULD | Names the Extras by descriptions rather than their titles. "Play that one before you go in" is ambiguous. The 51/102 million sentence runs to 27 words. |
| 015 Aurora (Extra) | SHOULD | Doesn't say how to find the film room ("follow the signs"). Has two 28-word sentences. |
| 016 The room at 21 metres (Extra) | SHOULD | "200 square metres … ninety-six people" puts two numbers in one sentence. Has two 27-word sentences. Cue correct. |
| 017 From building site to city symbol | SHOULD | "At the bottom you come out on the Plaza Mayor" clashes with 001's "bottom". It repeats 014's opening, mayor and quarrel. |
| 018 Under the timber | MUST | Says "This is the Plaza Mayor, the raised square", and 020 repeats the sentence word for word. Makes the same payoff three times. "Follow the timber down… to the trunks" is unconfirmed (O14). |
| 019 The market that waited 37 years | SHOULD | Re-tells 008's 1830s, 1973 and "fenced, dusty car park", although 008 is always heard first. Has a 29-word sentence. |
| 020 The plaza on stilts (CLOSE) | MUST | Repeats 018's identification sentence. Highlights listeners hear "when Aurora is running" without ever being told what Aurora is. |
| 021 The fig trees and the Roman columns (Extra) | MUST | The fig-tree paragraph repeats 009 almost word for word. It gives no help in finding either place. |
| Bridge 001 E>008 | OK | Correct destination and title. NICE: punctuation and "once you're down". |
| Bridge 001 H>009 | OK | Correct destination and title. NICE: as above. |
| Bridge 009 H>013 | MUST | "360º" (TTS). "Carry on past that view" comes before the view. "The highest point" is said twice. |
| Bridge 013 H>020 | SHOULD | "Carry on down" skips "the way down". Title correct. |
| Bridge 014 E>017 | SHOULD | Repeats 014's own cue, and leaves unclear whether Essential listeners may still see the film. |

Counts: **4 MUST**, **22 SHOULD**, **17 NICE** findings (below). No missing bridges. No left/right other than "Giralda on your left", and no view other than south, west or north. No prices, hours or ticket talk. All word counts are in range.

## 2. Findings

Word-count note. 001 (358/360), 009 (359/360), 005 (357/360) and 015 (229/230) are at their caps. Every replacement for those four is word-neutral or shorter. Counts are lint counts.

### MUST

**M1. "º" in spoken text (001, 012, bridge 009 H>013).**
- Exact words:
  - 001: "the walkways and the Mirador 360º, the viewing platform on top"
  - 012: "Go up the steps to the highest point, the Mirador 360º, the viewing platform."
  - Bridge: "the steps up to the Mirador 360º, the highest point"
- Problem: "º" is the masculine ordinal indicator, not a degree sign. Engines read it as "three hundred sixty o", "three hundred and sixtieth", or drop it. It sits in route cues in all three versions.
- Replacement: write **"Mirador three-sixty"** everywhere in speech. This is one token, so the lint count is unchanged. Keep "360º" only in @title, @where and on-screen text. If the app ever voices titles, the 013 title "Mirador 360º — The highest point" needs the same treatment (N17).

**M2. 010 refers back to the Antiquarium in Essential (and in Full when the Antiquarium is closed).**
- Exact words: "Work on it started in 1184, for the Great Mosque of the Almohads, the same Moorish Seville as a house found under this square."
- Problem:
  - In Essential, and in Full with the Antiquarium closed, the listener has never heard of a Moorish house (007 is skipped). "The same … as a house found" sounds like a reminder of something already heard.
  - The phrase is ungrammatical to the ear: Seville "as a house".
  - "The Almohads" is never glossed outside 007.
- Replacement (+4 words, 010 goes to 352): "Work on it started in 1184, for the Great Mosque of the Almohads, the Moorish rulers of the city. A house from their Seville lies under this square." It works for every version.

**M3. The vaults and fig trees are told four times (009 → 010 → 021).**
- Exact words:
  - 009: "Mayer has said he took cues from the cathedral's vaulting and from the great shade trees of a neighbouring square. The city names them as the giant fig trees of the Plaza del Cristo de Burgos. The operator calls them centennial, and the city cares for them as singular trees. Trees and vaults, then, not mushrooms."
  - 010 hook, the very next track in Essential and Full: "The architect of the Setas has said that one of his starting points was not a mushroom at all. It was the cathedral…"
  - 010 again: "Now, the link. Mayer has spoken of the cathedral's stone vaulting as one of his references."
  - 021: "Jürgen Mayer H. spoke of the cathedral's vaulting, and of big trees on a neighbouring square. The city names those trees: the fig trees of the Plaza del Cristo de Burgos. The operator calls them centennial… A local report calls them singular trees, and the city has been giving them specialist care…"
- Problem:
  - Essential and Full hear "not mushrooms, the cathedral's vaults" three times within about three minutes.
  - Full then hears 009's fig-tree passage again in 021: the same four facts, in the same order, mostly in the same words.
  - 009 is in every version that contains 010 or 021, so both later tracks can lean on it.
- Replacements:
  - 010 hook: "[curious] One of the ideas behind the Setas is in view from here. It's the cathedral, less than a kilometre from where you stand."
  - 010, "Now, the link" paragraph: cut "Mayer has spoken of the cathedral's stone vaulting as one of his references." Then write "Now, the link. The Museum of Modern Art in New York keeps a model of the Setas. The museum describes the design as a democratic 'cathedral without walls'." This also fixes N7, where "it" could mean the museum or the model.
  - 021, first three paragraphs (about −30 words, 021 goes to about 190, X minimum 150): "[curious] On the way up, you heard about the old fig trees that the city links to the parasols. You can stand under them today. / They grow in the Plaza del Cristo de Burgos, nearby. Look up into the branches, and see whether the parasols look familiar. / They need looking after now, and the city has been giving them specialist care to keep them stable and safe."

**M4. The Plaza Mayor is introduced three times (018 → 019 → 020).**
- Exact words:
  - 018: "This is the Plaza Mayor, the raised square. It covers almost four thousand square metres … on the roof of the market."
  - 019: "…this raised square on top of it, like a roof you can walk on."
  - 020: "This is the Plaza Mayor, the raised square. It sits on the roof of the market, under the parasols, open to the sky and used for events."
  - 017's cue and the H bridge also both say "the big raised square under the parasols".
- Problem:
  - In Essential and Full, 018, 019 and 020 play back to back on the same spot. 020's opening sentence is word for word 018's, about five minutes later.
  - Highlights listeners have already been told the place by the 013 H bridge ("the Plaza Mayor, the big raised square under the parasols"), so 020 doesn't need it either.
- Replacements:
  - 020 paragraph 2 opening: change "This is the Plaza Mayor, the raised square. It sits on the roof of the market, under the parasols, open to the sky and used for events. It's one of the four layers of the design." to "The Plaza Mayor is one of the four layers of the design: open to the sky, and made for events." "Below you, the market carries on" stays later in 020, so Highlights still learns that the market is underneath.
  - 019: "…and this raised square on top of it…" becomes "…with this square on top of it…" (see S11).

### SHOULD (route)

**S1. 009: "As you step out" arrives about 95 seconds in.**
- Exact words: "[pause] As you step out, the timber is all around you."
- Problem: 216 spoken words come first, about 95 seconds plus pauses. The lift ride is probably well under a minute (O5 not timed yet). Listeners hear "as you step out" after they have been walking, possibly in the flow.
- Replacement (word-neutral; 009 is at 359): "[pause] By now you're out of the lift, among the timber." Also consider O5's fallback of moving the trees paragraph after this line.

**S2. 017: "At the bottom".**
- Exact words: "At the bottom you come out on the Plaza Mayor, the big raised square under the parasols."
- Problem: 001 defines "the bottom" as level minus one ("You'll start at the bottom, go to the very top, and finish in the middle"). A listener taking a lift down (ALT-D, O12) may stay in it to the real bottom.
- Replacement: "At the end of the way down, you come out on the Plaza Mayor, the big raised square under the parasols."

**S3. 014 cue: the Extras are named by description, not title, and "that one" is ambiguous.**
- Exact words: "There are two short Extras here: Aurora, the light in the timber after dark, and Feeling Sevilla, about the film room. Play that one before you go in."
- Problem:
  - The titles on the phone are "Aurora, the Setas after dark" and "The room at 21 metres".
  - "That one … before you go in" does not say into what.
- Replacement: "There are two short Extras next: Aurora, the Setas after dark, and The room at 21 metres, for anyone going into the Feeling Sevilla film. Play that one at the film room's door."

**S4. 015 and 014 never say how to find the film room.**
- Exact words (015): "If you're going into the Feeling Sevilla film, play the next Extra before you go in: The room at 21 metres."
- Problem:
  - The room's position is unknown (O11), and no line tells the listener how to find it. 016's @where says "follow the signs", but that is not spoken.
  - PLAN allows "follow the signs for…" [O19].
- Replacement (+3 words): "If you're going into the Feeling Sevilla film, follow its signs, and play the next Extra at the door: The room at 21 metres." 015 is at 229, so combine this with S16's 015 fix, which saves 2 words. 015 then lands at 230, exactly the cap.

**S5. Bridge 014 E>017 repeats the cue and leaves the film unclear.**
- Exact words: "On this shorter tour, skip the Extras: walk on toward the way down, and play the next stop, From building site to city symbol, as you go down past the exhibition."
- Problem:
  - It is needed: 014 has just told Essential listeners to "play that one", and their list doesn't have it.
  - But it then repeats 014's own next-main-stop sentence almost word for word.
  - "Skip the Extras: walk on" can be heard as "skip the film". 001 implies the film is optional for everyone, not excluded.
- Replacement: "On this shorter tour, the Extras aren't on your list. If you're seeing the Feeling Sevilla film, see it first. Then follow the way down, and play From building site to city symbol as you pass the exhibition."

**S6. Bridge 009 H>013 is muddled (and contains M1).**
- Exact words: "On this shorter tour, carry on past that view: walk on along the walkway to the steps up to the Mirador 360º, the highest point, and play the next stop, The highest point, at the top."
- Problem:
  - "Carry on past that view" comes before the listener has reached the view.
  - "The highest point" is said twice.
  - Highlights listeners may worry that they are missing the Giralda.
- Replacement: "On this shorter tour, don't stop for that view: you'll see the Giralda from the top. Walk on along the walkway to the steps up to the Mirador three-sixty, and play the next stop at the top: The highest point."

**S7. Bridge 013 H>020 skips "the way down".**
- Exact words: "On this shorter tour, don't stop on the walkway: carry on down, past the exhibition, to the Plaza Mayor, the big raised square under the parasols, and play the last stop there, The plaza on stilts."
- Problem:
  - "Carry on down" right after "go back down the steps" can be heard as more steps.
  - The listener still has to walk the walkway to the way down.
  - The title is tacked on after a comma.
- Replacement: "On this shorter tour, skip the walkway stops: follow the way down, past the exhibition, to the Plaza Mayor, the big raised square under the parasols. Play the last stop there: The plaza on stilts."

**S8. 018: the trunks are presented as visible (O14).**
- Exact words: "Follow the timber down, and you come to the trunks that hold it all up. Two of them are concrete, not wood, and the lifts run up inside them."
- Problem:
  - Whether a trunk is in view from every part of the square is unconfirmed, and the writer flagged it.
  - It is also the third telling of "lifts inside concrete trunks", after 001 and 009.
- Replacement: "If you can see one of the trunks, follow the timber down to it. Two of the trunks are concrete, and the lift you rode runs inside one." This works in all versions, since everyone took the lift.

**S9. 002 cue promises a viewpoint that is unconfirmed (O4).**
- Exact words: "Walk on along the walkway to the first place where you can look down into the excavation and see how deep it goes."
- Problem: O4 asks whether any such place exists. 003 does not need it, because it says "Wherever you stand in here…".
- Replacement: "Walk on along the walkway, and play the next stop at the first good view down into the remains: Seville stacked up."

**S10. 021 gives no way to find either place.**
- Exact words: "Both are nearby: the Plaza del Cristo de Burgos for the fig trees, and the Alameda de Hércules for the columns."
- Problem: "Nearby" is correct and sourced-safe, but a visitor cannot act on it. No direction or distance is sourced (PLAN_V5_1).
- Replacement: keep the sentence, then add: "Any map on your phone will show you the way."

### SHOULD (repetition between consecutive tracks)

**S11. 019 re-tells 008's market history.**
- Exact words:
  - 019: "A market hall had stood here since the 1830s. In 1973 it was demolished, largely because of structural problems…" and "The square they left behind became a fenced, dusty car park."
  - 008 has already said the 1830s, 1973 with three reasons, and "a fenced, dusty car park". It also promised: "Their own story waits for you at the end, above the market."
- Problem: 008 is always heard before 019 (Essential, Full, and Full with the Antiquarium closed), so the re-telling is pure repetition.
- Replacement:
  - Hook: "[curious] By the lifts, you heard how the old market hall came down in 1973. Its traders were promised a temporary home. Three years, at most. They waited thirty-seven."
  - Paragraph 2: "Right below you, at street level, is the Mercado de la Encarnación, the Incarnation Market. When the old hall came down, the stallholders moved into makeshift stalls nearby."
  - Paragraph 3: "The square they left behind became a car park. Then the archaeologists came…"
  - About −9 words, so 019 goes to about 204.
  - Also split the 29-word sentence: "The architect had kept its place in the plan. The market went at street level, with this square on top of it, like a roof you can walk on."

**S12. 017 repeats 014's opening, mayor and quarrel.**
- Exact words:
  - 014: "When the Setas opened, in March 2011, some Sevillanos came out to protest… The mayor who opened it, Alfredo Sánchez Monteseirín…"
  - 017, next in Essential: "On a Sunday in the spring of 2011, Seville's mayor opened a building the city had been arguing about for seven years… On the twenty-seventh of March 2011, Mayor Alfredo Sánchez Monteseirín opened it…"
- Problem: Essential hears 014 then 017 back to back, so the mayor's full name and the opening date come twice in a row.
- Replacement (paragraph 3): "On the twenty-seventh of March 2011, the mayor opened it, and the museum of Roman remains below opened the same evening." The hook can stay.

**S13. 013 re-tells 010 and 011 for Essential and Full.**
- Exact words:
  - 013: "That way is south, less than a kilometre off." (010: "less than a kilometre from where you stand")
  - 013: "Beyond them rises the Aljarafe, the high ground west of the city." (011, the same words: "the Aljarafe, the high ground west of the city")
- Problem: the recap is needed for Highlights, but Essential and Full hear it as a rerun.
- Replacement:
  - "Three directions are worth fixing first." becomes "Three directions are worth fixing, even if you found some of them on the walkway."
  - In 013, "the high ground west of the city" becomes "the higher ground beyond the river".

**S14. 018 makes its payoff three times.**
- Exact words: "One of the first big crowds here didn't come for a concert." / "Built for fairs and concerts, the square held a protest camp in its very first season." / "So a square designed for crowds found one almost at once. Just not the kind anyone had put on the calendar."
- Replacement: cut the middle sentence, "Built for fairs and concerts, the square held a protest camp in its very first season." (−16 words, 018 goes to 278.)

### SHOULD (listening)

**S15. 002: "some 1,200 years … to the 1200s".**
- Exact words: "The remains cover some 1,200 years of the city's life, from about the time of the emperor Tiberius, in the first century, to the 1200s."
- Problem: "one thousand two hundred years" and "the twelve hundreds" collide in one 25-word sentence.
- Replacement: "The remains span some twelve centuries. The oldest go back to the emperor Tiberius, in the first century. The latest are from the 1200s."

**S16. Two numbers fighting in one sentence.**
- 014: "…the cost had roughly doubled, from a budget of about 51 million euros to a final bill of about 102 million." (27 words) becomes "…the cost had roughly doubled. The budget was about 51 million euros. The final bill came to about 102 million."
- 016: "The operator, Sacyr, gives it more than 200 square metres, and one trade report says its stands hold ninety-six people." becomes "The operator, Sacyr, gives it more than two hundred square metres. One trade report says its stands hold ninety-six people."
- 018: "It covers almost four thousand square metres, and it stands about five metres above the street, on the roof of the market." becomes "It covers almost four thousand square metres. And it stands about five metres above the street, on the roof of the market."
- 015, two 28-word sentences:
  - "The operator says it responds to how many people are up here and how they move, to the weather and the wind, and to the time of year." becomes "The operator says it responds to how many people are up here and how they move. It also follows the weather, the wind and the season." (−2)
  - "The same report says usually under thirty percent of the lights are on at any moment, for a sense of movement, with less light spilling into the sky." becomes "The same report says usually under thirty percent of the lights are on at once. That gives a sense of movement, with less light spilling into the sky." (±0)

**S17. Other sentences over 25 words.**
- 016: "Add sound from every side, images projected onto the floor, moving air and even scents, and you have a room built to work on all your senses." (27) becomes "Add sound from every side, images on the floor, moving air and even scents. It's a room built to work on all your senses."
- 016: "It arrived in 2021, ten years after the opening, together with Aurora, the light show, as part of what Sacyr calls a complete renewal of the building." (27) becomes "It arrived in 2021, ten years after the opening, together with Aurora, the light show. Sacyr calls it part of a complete renewal of the building."
- 017: "He pointed to the Eiffel Tower, which Paris had once argued about too, and said Seville could be proud of a new symbol of modernity and technology." (27) becomes "He pointed to the Eiffel Tower, which Paris had once argued about too. Seville, he said, could be proud of a new symbol of modernity and technology."
- 019: the 29-word sentence, fixed in S11.

**S18. 020: "Aurora" is never introduced in Highlights.**
- Exact words: "And when Aurora is running, the timber above you lights up after sunset."
- Problem: Highlights never hears 014, 015 or 017, so "Aurora" is a bare name.
- Replacement (+3 words): "And after sunset, when the Aurora light show is running, the timber above you lights up."

**S19. 011: "AD", twice.**
- Exact words: "a fish-salting works from the first century AD" and "somewhere between 70 and 120 AD"
- Problem: engines read "AD" as "ad" or as the letters "A D".
- Replacement: "a fish-salting works from the first century" and "somewhere between the years 70 and 120".

**S20. 012: "60 degrees" with no unit.**
- Exact words: "'the temperatures in the adhesive could potentially reach almost 60 degrees.' That was right at the limit the glue was rated for."
- Problem: US listeners will hear 60 °F, which is cool, and the scare lands on nothing.
- Replacement (−1 word): keep the quote, then: "Sixty Celsius: right at the limit the glue was rated for."

**S21. 009: "singular trees" (Spanish *árboles singulares*).**
- Exact words: "and the city cares for them as singular trees"
- Problem: in English "singular" means odd or single.
- Replacement (word-neutral): "and the city cares for them as remarkable trees". If M3's 021 rewrite is not used, apply the same change in 021.

**S22. 018: "indignados" is not glossed.**
- Exact words: "Seville's indignados made it their meeting place."
- Replacement: "Seville's indignados, 'the outraged', made it their meeting place."

### NICE

- **N1. 001 and 009 both explain the nickname.**
  - 001: "Sevillanos took one look and called it las Setas, the mushrooms."
  - 009: "But Sevillanos called it las Setas anyway."
  - Highlights hears both within about two minutes. In 009, "The nickname stuck, and even the architect came round to it" could stand alone after "He didn't set out to build mushrooms."
- **N2. 007 and 010, Full only:** the Great Mosque, the minaret begun in 1184 and the Giralda are told twice. This is acceptable as reinforcement. M2's wording softens it.
- **N3. 003 and 007, Full only:** "About three metres down, Moorish houses" is followed by "about three metres below the street. The Roman floors lay about twice as deep." This is acceptable.
- **N4. 004–006 say "the scholar" eight times.**
  - 005 says "One scholar of these floors" after 004's "the scholar who studied these mosaics", which suggests a second person.
  - Use "the same scholar" in 005 and vary one or two instances ("the review", "her book's reviewer").
- **N5. 007 says "by the lifts" twice in a row:** "The story of the square above you comes by the lifts." then "The next stop plays by the lifts". Cut the first sentence.
- **N6. 008.**
  - "Their own story waits for you at the end" should be "near the end", since 019 is not the last stop.
  - "Joseph Bonaparte's government" should be "Joseph Bonaparte, Napoleon's brother, then ruling Spain", so the hook links to the name.
- **N7. 010.**
  - "…keeps a model of the Setas, and it describes the design" is ambiguous: "it" could be the museum or the model. Fixed by M3.
  - "The cathedral chapter voted" should be "the cathedral's clergy voted".
- **N8. 011:** "Toward the river lie the rooftops of Triana, on its far bank" should be "Across the river, on its far bank, lie the rooftops of Triana."
- **N9. 019 and 020 both say the market can be visited:** "You can visit it afterwards, from the street." and "From there you can visit the market, too." Keep 020's line, which Highlights needs, and cut 019's.
- **N10. 001.**
  - "From the north entrance, the way down leads to the same underground level" uses "the way down", which the rest of the guide reserves for the exit route. Say "From the north entrance, you go down to the same underground level."
  - "The taquilla, the box office, and the Antiquarium, the museum of the remains" is an appositive chain that can sound like four places. Consider "First comes level minus one. There you'll find the taquilla, the box office, and the Antiquarium, the museum of the remains."
- **N11. 012:** "The polyurethane is only the skin" follows 009's "waterproof skin of polyurethane". Fine. Optionally "The polyurethane you heard about in the lift is only the skin." 012 is in Essential and Full only, and 009 always comes before it.
- **N12. The cathedral metaphor appears three times in Essential:** 010 "cathedral without walls", 014 "a modern urban cathedral", 020 "open cathedral". It is a deliberate motif and acceptable. Don't add a fourth.
- **N13. 005:** "Hospitium" is glossed three sentences after it is first said twice. Move "Hospitium is a Latin word for hospitality…" up, right after "the Hospitium of the Dolphins".
- **N14. Bridges 001 E>008 and 001 H>009.**
  - The title after a comma ("…before you go up, A plaza with many lives") is hard to hear as a title. Use the colon style of the tracks.
  - They also omit that the listener is still at street level.
  - Suggested E: "On this shorter tour, skip the Antiquarium. Once you're down on level minus one, go to the lifts beside its entrance, the Mirador access, and play the next stop there, before you go up: A plaza with many lives."
  - Suggested H: "On this shorter tour, skip the Antiquarium. Once you're down on level minus one, go to the lifts beside its entrance, the Mirador access. Take the lift up, and start the next stop as the doors close: Mushrooms of wood."
- **N15. 001 date digits:** "it opened on 27 March 2011" is often read "twenty-seven March". 017 already spells it out. Write "and opened on the twenty-seventh of March, 2011" and drop the "it", for 359 words.
- **N16. 013's derived "Giralda at your back = north" is consistent with PLAN_V5_1.**
  - ONSITE_CHECKLIST still says the only compass words allowed are south and west. Update O9 to check the north cue.
  - "The great bulk of the cathedral beside it" depends on O7. The writer has a fallback.
- **N17. Titles with symbols or digits:** "Mirador 360º — The highest point", "The room at 21 metres", "The market that waited 37 years". The spoken body is fine ("thirty-seven" and "twenty-one" are read correctly), but if the app or an intro voices titles, spell them out. Also, "21 metres" comes four times in 016's first paragraph. That is the intended joke, so keep it.

## 3. Route check (criterion 1)

**Order.** The order matches the research and the official stop list:
- Calle Imagen or the north entrance → level −1, past the taquilla → Antiquarium, with its entrance beside the lifts → lift up inside a concrete trunk → walkways → Mirador steps → Aurora and Feeling Sevilla (Extras) → exhibition on the way down → Plaza Mayor → stairs or escalators to the street.
- This follows "Mirador 360º → Aurora → Sala Feeling → Tienda → Exposición → Plaza Mayor" (OFF). The shop is never named.

**Next-stop titles.** All 20 cues name the next title correctly:
- 001 → Found under a car park
- 002 → Seville stacked up
- 003 → Medusa, the guardian
- 004 → Bacchus and the dinner party
- 005 → Two birds and a wine bowl
- 006 → The Almohad house
- 007 → A plaza with many lives
- 008 → Mushrooms of wood
- 009 → The Cathedral and the Giralda
- 010 → The river, Triana and the Aljarafe
- 011 → The glue that had to be baked
- 012 → The highest point
- 013 → Love it or hate it
- 014 → From building site to city symbol (the Extras are described, not titled: S3)
- 015 → The room at 21 metres / From building site to city symbol
- 016 → From building site to city symbol
- 017 → Under the timber
- 018 → The market that waited 37 years
- 019 → The plaza on stilts
- 020 → The fig trees and the Roman columns

**Compass.**
- "Giralda on your left = facing west" appears in 010, 011 and 013, and is geometrically correct.
- "Giralda at your back = north" appears in 013 and is derived the same way.
- "Right angles" in 018 and "right here" or "right below you" in 018 and 019 are not directions.
- "Go straight to" in the H bridge means "directly", not "straight ahead". It is fine, but N14's rewording drops it anyway.

**Views.**
- South: the Giralda and the cathedral.
- West: river, Triana's rooftops, Aljarafe. The river is correctly hedged with "Whether or not the water shows".
- North: toward the Macarena district, direction only.
- No other landmark is claimed as visible. The Torre del Oro (007) and the Atlantic (011) are mentioned as geography, not as views.

**Unconfirmed points spoken as certain.** All the rest are either sourced OFF/SEC with their [O] tag, or hedged ("may glimpse", "look for", "if you find her", "or the escalators"):
- S1: step-out timing (O5)
- S8: trunks in view (O14)
- S9: the depth viewpoint (O4)
- S2: "at the bottom" (O12, ALT-D)

## 4. Standard check (criterion 4)

- **Word ranges.** All tracks are in range (lint). R: 003 250, 006 262, 007 262, 012 280, 017 240, 019 213. W: 250–359. X: 015 229, 016 206, 021 221. ANCHOR 001 358, CLOSE 020 264. Several are at their caps (see the note in §2).
- **Prices, hours and tickets.** None.
  - 014's "51 / 102 million euros" is the construction cost, in PLAN's prescribed wording.
  - 001's "its own admission" and "the taquilla, the box office" are the allowed exception and a navigation feature.
  - Aurora is "after sunset", with no times or months. The Antiquarium is only "if it's closed".
- **Dates.** 002 has four year markers (1990s, 1991, 1998, 2003–2009), and 010 has four (1184, 1248, 1560s, early 1400s), against the standard's three per track. Both are listenable as spaced, short sentences. The writer flagged 002, and the lead decides.
- **Em-dashes, semicolons, parentheses, exclamation marks.** None in speech.

## 5. Names a TTS voice may mispronounce (add to the per-engine override list after the first listen)

- **Spanish places and terms:**
  - Calle Imagen ("KAH-yeh ee-MAH-hen"; risk: "Cally Image-en")
  - taquilla ("ta-KEE-ya")
  - Setas, Sevillanos
  - Plaza de la Encarnación, Mercado de la Encarnación
  - Mirador, casa almohade, Casa de la Columna, Casa de Baco, Casa del Sigma, Casa de la Ninfa, Casa de las Basas, Casa de la Noria, Patio del Océano, Hospitium de los Delfines
  - Giralda, Giraldillo
  - Guadalquivir ("gwah-dal-kee-VEER"), Aljarafe ("al-ha-RAH-feh"), Triana, Macarena
  - Tamarguillo ("ta-mar-GHEE-yo"), Mercasa
  - Plaza Mayor, Feeling Sevilla, Sala Feeling, Semana Santa, Feria, indignados
  - Plaza del Cristo de Burgos, Alameda de Hércules
- **People:**
  - Jürgen Mayer H. (the "H." can trigger a sentence-end pause)
  - Felipe Palomino, Fernando Amores, Melchor Cano, Joseph Bonaparte
  - King Fernando the Third, Abu Ya'qub Yusuf
  - Alfredo Sánchez Monteseirín, José de la Peña
  - Rowan Moore, Dirk Kruse, Mika Kallio
  - Count of Barajas, Tiberius, Trajan, Hadrian, Perseus, Ariadne
- **Latin, Greek and technical terms:**
  - Hispalis, Baetica ("BEE-ti-ka"), garum, triclinium, stibadium, hospitium, sigma, crater (the wine bowl)
  - Almohad, Medusa, Bacchus, Gorgon
  - Kerto-Q, epoxy, polyurethane
  - Fraunhofer, Finnforest, Skandal Technologien, Bavaria
  - Sacyr ("sa-THEER" or "sa-SEER"), Arup ("AIR-up")
  - Mies van der Rohe, Red Dot, UNESCO, LED
- **Symbols and abbreviations:** "360º" (M1), "AD" (S19), "27 March 2011" in digits (N15), "1,200" against "1200s" (S15).

## 6. Play-throughs

### Full (001–021, in order)

- **001 → 002.** The listener goes down the ramp beside the escalators to level minus one. "Found under a car park" plays at the Antiquarium door. If the Antiquarium is closed, 001 sends them to the lifts and "A plaza with many lives", and they continue at 008. In that case 010's "a house found under this square" points to something they never heard (M2).
- **002 → 007, inside the Antiquarium.**
  - 002 ends with "the first place where you can look down" (S9).
  - 003 opens on "That first test dig", which 002 just named. That works.
  - 003 → 004 at the House of the Column label. 004 → 005 as they walk. 005 → 006 at the wall mosaic. 006 → 007 at the casa almohade label, with a fallback for the opposite order.
  - "The scholar" is introduced in 004 and carried through 006 (N4).
  - 007 sends them out by the exit signs to the lifts.
- **007 → 008.** 008 plays at the lifts.
  - 008's "What they found is in the Antiquarium, beside these lifts" rings true.
  - Its promise "Their own story waits for you at the end" is kept by 019 (N6).
- **008 → 009.** 009 starts as the doors close. "As you step out" comes about a minute after they are out (S1).
- **009 → 010.** The Giralda is in view.
  - 009 ended "Trees and vaults, then, not mushrooms". 010 opens with "not a mushroom at all. It was the cathedral", and later says it a third time (M3).
  - 010 also re-tells 007's minaret (N2).
- **010 → 011.** "Stand with the Giralda on your left" works, and 011 repeats it as confirmation.
- **011 → 012, walking toward the Mirador steps.** 011 keeps 002's promise ("Their story comes later, when you can look toward the river").
- **012 → 013, up the steps.** "Mirador 360º" trips the TTS (M1). At the top, 013 runs south, west and north again, a rerun of 010 and 011 for this listener (S13).
- **013 → 014.** Down the steps, walking toward the way down.
- **014 → 015 → 016 → 017.** 014 announces the Extras by description (S3). 015 plays anywhere. 015's cue splits film-goers from the rest but never says how to find the film (S4). 016 at the door, then the way down. 017 plays past the exhibition.
- **017 → 018.** 017 retells 014's opening and mayor (S12). "At the bottom" (S2) leads to the Plaza Mayor, where 018 introduces the square.
- **018 → 019.** "Stay on the Plaza Mayor". 019 then retells 008's 1973 and "fenced, dusty car park" (S11).
- **019 → 020.** 020 repeats "This is the Plaza Mayor, the raised square" (M4). It then gives the way out and announces 021.
- **020 → 021.** After leaving, 021 repeats 009's fig-tree passage (M3) and ends "nearby" with no way to find either place (S10).

### Essential (001 008 009 010 011 012 013 014 017 018 019 020)

- **001 + bridge E → 008.** 001 has just said "Found under a car park plays at the door of the Antiquarium". The bridge overrides it cleanly: "skip the Antiquarium: go to the lifts beside its entrance, the Mirador access". They still have to get down to level minus one first, as 001's previous sentence says (N14).
- **008.** Fully self-contained. "What they found is in the Antiquarium, beside these lifts" is new information, not a back-reference.
- **008 → 009 → 010.**
  - Clean joints. 010's "the same Moorish Seville as a house found under this square" is the one back-reference to a skipped track (M2).
  - "The Almohads" is not glossed for this listener, which M2 fixes.
  - The vault story comes three times (M3).
- **010 → 011 → 012 → 013.** Clean joints. 013 repeats the directions just heard (S13).
- **013 → 014 + bridge E → 017.**
  - 014 tells them "There are two short Extras here… Play that one before you go in". These are tracks they don't have.
  - The bridge corrects that, but repeats 014's next-main-stop sentence, and "skip the Extras: walk on" can be heard as "don't go to the film" (S5).
  - No Essential track refers back to 015 or 016. 017's "adding the Aurora lights and the Feeling Sevilla room" is self-explanatory.
- **017 → 018 → 019 → 020.**
  - The joints are right, but this is where the repetition is densest: the opening and the mayor again (S12), "the raised square" three times (M4), and the market history again (S11).
  - 020's "If you're on the full tour, there's one last short Extra" is correctly conditional.

### Highlights (001 009 013 020)

- **001 + bridge H → 009.** Clean. "Go straight to the lifts beside its entrance… take the lift up, and start the next stop… as the doors close" fits 009's @where exactly.
- **009.** Self-contained for this listener: "a car park, then a dig" and "the ruins were in the brief" need no earlier track.
  - It repeats 001's nickname line within about two minutes (N1).
  - The cue sends them to "The Cathedral and the Giralda", which they don't have.
- **009 + bridge H → 013.**
  - The bridge corrects the cue, but "carry on past that view" comes before the view.
  - "Mirador 360º" trips the TTS, and "the highest point… The highest point" is doubled (S6, M1).
  - At the top, 013 is the right orientation for this listener: it introduces the Giralda, the cathedral, west, Triana and north from scratch.
- **013 + bridge H → 020.**
  - The bridge sends them to the Plaza Mayor via the exhibition. "Carry on down" should name the way down (S7).
  - 020 works standalone ("You've been below the street…" is true of level −1), except for "when Aurora is running" (S18). The light show has never been named to this listener.
  - The goodbye and the way out are correct.

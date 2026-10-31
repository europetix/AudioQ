# V5.1 audit fixes (EN), 31 Oct 2026

Applied to `v5/tracks_v51/001–021.perf.txt` and both `bridges_*.txt` from
`research/AUDIT_V51_FACTS.md` (F) and `research/AUDIT_V51_ROUTE_LISTENING.md` (R), with the lead's six decisions
overriding the reports where they conflict. Pre-fix copies were kept outside the project (scratchpad), not in this folder.

`cd /home/claude/audioq/setas_v5 && TRACKS_DIR=v5/tracks_v51 python3 v5/lint.py` → **OK for all 21**.
Every track's last paragraph still names the next stop's title exactly (020 names 021 in its way-out paragraph, before
the goodbye, as before). Every bridge was re-read against its track's new ending.

## Totals
| Report | Severity | Findings | Fixed | Not done |
|---|---|---|---|---|
| F | SHOULD | 11 | 11 | 0 |
| F | NICE | 15 items (13 IDs; 009.1 and 018.3 have two parts each) | 13 | 2 (009.1b, 018.3b) |
| R | MUST | 4 | 3 | 1 (M1, lead decision 1) |
| R | SHOULD | 22 | 22 | 0 |
| R | NICE | 17 | 11 | 6 (N2, N3 and N12 the auditor called acceptable as they stand; N11, N16 and N17 not done) |

Words (lint): 6,076 → 6,000. Every track is in range. Tracks now at their cap: 004 (360/360), 012 (280/280), 015 (230/230).
Under 200: 019 (198, R min 180), 021 (195, X min 150).

| Track | 001 | 002 | 003 | 004 | 005 | 006 | 007 | 008 | 009 | 010 | 011 | 012 | 013 | 014 | 015 | 016 | 017 | 018 | 019 | 020 | 021 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Before | 358 | 348 | 250 | 350 | 357 | 262 | 262 | 333 | 359 | 348 | 326 | 280 | 285 | 291 | 229 | 206 | 240 | 294 | 213 | 264 | 221 |
| After | 358 | 337 | 250 | 360 | 356 | 258 | 260 | 337 | 353 | 331 | 326 | 280 | 296 | 294 | 230 | 202 | 242 | 283 | 198 | 254 | 195 |

## Lead decisions applied
1. "Mirador 360º" stays in the English everywhere (001, 012, the 009 H>013 bridge, the 013 title). The English
   pronunciation file respells it. → R-M1 and R-N17 not done.
2. 006 is neither held nor dropped. It is rewritten so that only ACOM and ACOM-B facts are stated as fact. Kramer's panel is
   presented as one that "may be the same mosaic", and its details only as "If the label matches, look for more". The new
   title is **"Antiquarium — The two birds"**. 005's cue was updated. No other cue or bridge named 006.
3. 010 now reads "the Moorish rulers of the city. This was the same Moorish Seville whose remains lie under this square."
4. Repeats removed. The vaults and fig trees are told in full only in 009, with callbacks in 010 and 021. The Plaza Mayor
   is identified only in 018, and 020 no longer repeats the sentence.
5. 018: the trunk wording follows F-018.1, and "camped right here" is gone (F-018.2).
6. 005: the Bacchus scene follows F-005.1, and the corner vessels follow F-005.2.

---

## Fact audit (F)

**002.1 NICE: fixed.**
- Before: "Some of it is clear, some frosted, and some every shade in between."
- After: "The glass can be clear, or frosted, or anything in between."

**004.1 SHOULD: fixed.**
- Before: "Only about a dozen are on show."
- After: "Guadalupe López Monteagudo wrote the specialist study of them. When it came out, only about a dozen were on show."
- The @what now says the count is the one at publication.

**004.2 SHOULD: fixed.** The attribution is set up once in 004 and kept the same in 005 and 006.
- 004:
  - "One scholarly review puts it plainly" → "A review of her study puts it plainly". The "unmatched" line is Kramer's, and Kramer is the reviewer.
  - "The scholar who studied these mosaics calls this one…" → "The specialist study calls this one a warning and protective Medusa." I did not use "Her study", because the sentences around it use "her" for Medusa.
  - "The same scholar notes…" → "The same study notes…".
- 005: "One scholar of these floors" / "the scholar describes" / "The scholar admits" / "The scholar lists" → "The study of these floors says" / "the study describes" / "The study says" / "the study counts".
- 006: "The scholar who reviewed these mosaics" → "The study of these mosaics", and "the scholar admits" → "the study admits".

**005.1 SHOULD: fixed** (lead decision 6).
- Before: "One scholar of these floors says it was the favourite Bacchus scene in Roman southern Spain for a long time."
- After: "The study of these floors says one version, with Ariadne riding in his chariot, was long the most common in Roman southern Spain."
- The auditor's opener, "It was a popular theme", was left out because the track is at its cap. The attribution was kept, per 004.2. The @what says the version is not claimed to be this floor.

**005.2 SHOULD: fixed** (lead decision 6).
- Before: "When you find the Bacchus floor, look at its corners for the drinking vessels."
- After: "When you find the mosaic floor of the Casa de Baco, look at its corners for the drinking vessels."

**005.3 SHOULD: fixed.**
- Before: "Their dinner party is still on the floor."
- After: "Their dinner party was set down in stone."

**005.4 NICE: fixed.**
- Before: "Here, the main mosaic of that dining room showed the triumph of Bacchus, with Ariadne, the princess he married in the myth, beside him."
- After: "In this house, the main mosaic of the dining room showed the triumph of Bacchus. With him was Ariadne, the princess he married in the myth."
- The sentence was also split, because it was 26 words. "Beside" was dropped as a position-sounding word.

**005.5 NICE: fixed.** "in late Roman times" → "in Roman times".

**005.6 NICE: fixed.**
- Before: "The sea runs all through these floors. The scholar lists dolphins, fish and water birds."
- After: "Among the mosaics found here, the study counts many sea creatures: dolphins, fish and water birds."

**006.1 SHOULD: fixed** (lead decision 2; this replaces the HOLD).
- Title: "Antiquarium — Two birds and a wine bowl" → "Antiquarium — The two birds".
- 005 cue:
  - "…a mosaic hung upright on a wall, with two birds and a wine bowl. … : Two birds and a wine bowl."
  - → "…a mosaic hung upright on a wall, with two birds at its centre. … : The two birds."
- 006 paragraph 2:
  - "look for a mosaic hung upright on a wall: two birds facing each other over a wine bowl."
  - → "look for a mosaic hung upright on a wall, with two birds at its centre. It was pieced back together and set on the wall, so you see it standing up."
- 006 nickname line: "Kissing, or just sharing a drink?" → "Kissing, or just keeping each other company?" The old line presupposed the bowl.
- 006 Kramer paragraph:
  - Before: "…describes a panel very like it. Two birds on a crater… It sits as a small square… [pause] It may well be this one. Either way, look past the birds to the borders…"
  - After: "The study of these mosaics describes a panel with two birds on a crater, the big bowl Romans mixed their wine in. It may be the same mosaic. That panel comes from the Hospitium de los Triclinia, the Hospitium of the Dining Rooms. [pause] If the label matches, look for more. On that panel, the birds sit in a small square at the centre of a geometric design. Around it, two borders are laid to look like moving water, and smaller zigzag panels add to the ripple. See if the water seems to move."
- Also dropped: "two **small** birds" in the hook (no source sizes the emblem), and "Why birds **on a floor** at all?" → "Why birds at all?".
- @where, @what and @listen were rewritten to match.

**006.2 NICE: fixed** by deletion rather than the auditor's replacement.
- Before: "It began as part of a floor. … so you see it standing up instead of underfoot."
- After: removed. The track keeps only "pieced back together and set on the wall" (ACOM, ACOM-B).
- The lead asked that nothing inferred be stated as fact, and "Like the others, it was made for a floor" is still an inference.

**007.1 SHOULD: fixed.**
- "This is the Almohad house. It comes from…" → "At the label for the casa almohade, you reach Moorish Seville. The house comes from…". I wrote "The house" rather than the auditor's "It" so the reference is clear.
- "found a Moorish house here" → "found a Moorish house on this site".
- Also changed: "So this house stood…" → "So the house stood…", and "This house had a different fate." → "The house had a different fate."

**008.1 NICE: fixed.**
- Before: "There was damage from a flood of the Tamarguillo, a stream on the edge of the city."
- After: "There was the Tamarguillo flood, when a stream on the edge of the city burst its banks."

**009.1a NICE: fixed** (with R-S21 and F-021.2).
- Before: "…and the city cares for them as singular trees."
- After: "…and the city lists them among its remarkable trees."
- The City's guide *Árboles singulares de Sevilla* was added to @sources as SEV-AS, via the audit and not re-read. "Remarkable" renders *singulares* for the English ear.

**009.1b NICE: not done.**
- S-HIST's "centennial" refers to the ficus "in the Plaza de San Pedro", and the track applies it to the Cristo de Burgos trees.
- The line is left as it is, with the merge noted in @what. The fix is to confirm the age in the City guide, p. 114 [O20], or else drop "centennial".

**010.1 NICE: fixed.** "It was made to stand for the triumph…" → "It stands for the triumph…".

**011.1 SHOULD: fixed.**
- Before: "Traditionally it was a quarter of craftsmen and sailors, and above all of potters."
- After: "Its trade for centuries was pottery: the regional tourism office calls it the district's most important activity."
- Payoff: "Sailors and potters across the water…" → "Potters across the water…".
- UPO-TRI was regraded to SNIP in @sources, and JA-TRI (OFF, via the audit) was added. @what and @listen were updated.

**011.2 NICE: fixed.** "A long corridor" → "A corridor".

**014.1 SHOULD: fixed.**
- Before: "…it took four more years, and those were the years of Spain's financial crisis."
- After: "…it took four more years, years that ran straight into Spain's financial crisis."

**015.1 NICE: fixed** in a word-neutral variant, because 015 is at its cap.
- Before: "It was added in 2021…"
- After: "Aurora was added in 2021…"
- This says the show is new, not the wiring. The hook "The timber around you is wired for light" is true on both sources' accounts.

**018.1 SHOULD: fixed** (lead decision 5, merged with R-S8).
- Before: "Follow the timber down, and you come to the trunks that hold it all up. Two of them are concrete, not wood, and the lifts run up inside them."
- After: "If you can see one of the trunks that hold the parasols up, follow the timber down to it. Two of the trunks hold the lifts, inside concrete. You rode up through one of them."
- @what records the wording that VS-SET, JA-SET and PUBSP agree on.

**018.2 SHOULD: fixed** (lead decision 5).
- Before: "…made it their meeting place… and some of them camped right here, under the timber."
- After: "…made the Setas their meeting place… and some of them set up camp here."
- "Here" now follows "the Setas". There is no claim that the camp was on the raised square.

**018.3a NICE: fixed.** "about five metres above the street" → "about five metres up". This was done together with the R-S16 split.

**018.3b NICE: not done.** The ZARCH line ("argues that the architecture changed how people could use a public space") is a fair simplification, as the auditor says. Adding the "convex/concave structure" point would not work by ear.

**021.1 NICE: fixed.** "and probably from a temple" → "and possibly from a temple".

**021.2 NICE: fixed** by R-M3. 021's "A local report calls them singular trees" is gone, so the "singular" status is now told once, in 009, and credited to the city. 021 keeps the specialist care (VIVIR).

---

## Route and listening audit (R)

### MUST
**M1: not done** (lead decision 1). "Mirador 360º" stays in 001, 012 and the 009 H>013 bridge. The pronunciation file respells it "three-sixty".

**M2: fixed** (lead decision 3).
- Before: "…for the Great Mosque of the Almohads, the same Moorish Seville as a house found under this square."
- After: "…for the Great Mosque of the Almohads, the Moorish rulers of the city. This was the same Moorish Seville whose remains lie under this square."

**M3: fixed** (lead decision 4). The full telling stays in 009, the only one of the three tracks Highlights hears.
- 010 hook:
  - Before: "The architect of the Setas has said that one of his starting points was not a mushroom at all. It was the cathedral, less than a kilometre from where you stand."
  - After: "One of the ideas behind the Setas is in view from here. It's the cathedral, less than a kilometre from where you stand."
- 010 link paragraph:
  - Before: "Now, the link. Mayer has spoken of the cathedral's stone vaulting as one of his references. The Museum of Modern Art in New York keeps a model of the Setas, and it describes the design…"
  - After: "Now, the link. The Museum of Modern Art in New York keeps a model of the Setas. The museum describes the design…" This also fixes N7's "it". The timber-vaults line stays as the callback.
- 021, first three paragraphs. The auditor's text was used, minus a second "nearby":
  - Before: Mayer's vaulting and trees, the city naming them, centennial, "Stand under them…", and "A local report calls them singular trees…"
  - After: "On the way up, you heard about the old fig trees that the city links to the parasols. You can stand under them today. / They grow in the Plaza del Cristo de Burgos. Look up into the branches, and see whether the parasols look familiar. / They need looking after now, and the city has been giving them specialist care to keep them stable and safe."

**M4: fixed** (lead decision 4).
- 020 before: "This is the Plaza Mayor, the raised square. It sits on the roof of the market, under the parasols, open to the sky and used for events. It's one of the four layers of the design."
- 020 after: "The Plaza Mayor is one of the four layers of the design: under the parasols, open to the sky, and made for events."
- I kept "under the parasols" from the old text so that 020 stays above the CLOSE minimum (254).
- 019: "…and this raised square on top of it…" → "…with this square on top of it…" (see S11).

### SHOULD
**S1: fixed** (009). "[pause] As you step out, the timber is all around you." → "[pause] By now you're out of the lift, among the timber." The O5 fallback of moving the trees paragraph was not used.

**S2: fixed** (017). "At the bottom you come out on the Plaza Mayor" → "At the end of the way down, you come out on the Plaza Mayor".

**S3: fixed** (014).
- Before: "There are two short Extras here: Aurora, the light in the timber after dark, and Feeling Sevilla, about the film room. Play that one before you go in."
- After: "There are two short Extras next: Aurora, the Setas after dark, and The room at 21 metres, for anyone going into the Feeling Sevilla film. Play that one at the film room's door."

**S4: fixed** (015).
- Before: "…film, play the next Extra before you go in: The room at 21 metres."
- After: "…film, follow its signs, and play the next Extra at the door: The room at 21 metres."
- Combined with S16, 015 is exactly 230.

**S5: fixed** (bridge 014 E>017).
- Before: "On this shorter tour, skip the Extras: walk on toward the way down, and play the next stop, From building site to city symbol, as you go down past the exhibition."
- After: "On this shorter tour, the Extras aren't on your list. If you're seeing the Feeling Sevilla film, see it first. Then follow the way down, and play From building site to city symbol as you pass the exhibition."

**S6: fixed** (bridge 009 H>013). This is the auditor's text, but "Mirador 360º" is kept (lead decision 1).
- Before: "On this shorter tour, carry on past that view: walk on along the walkway to the steps up to the Mirador 360º, the highest point, and play the next stop, The highest point, at the top."
- After: "On this shorter tour, don't stop for that view: you'll see the Giralda from the top. Walk on along the walkway to the steps up to the Mirador 360º, and play the next stop at the top: The highest point."

**S7: fixed** (bridge 013 H>020).
- Before: "On this shorter tour, don't stop on the walkway: carry on down, past the exhibition, to the Plaza Mayor, the big raised square under the parasols, and play the last stop there, The plaza on stilts."
- After: "On this shorter tour, skip the walkway stops: follow the way down, past the exhibition, to the Plaza Mayor, the big raised square under the parasols. Play the last stop there: The plaza on stilts."

**S8: fixed** (018), merged with F-018.1 (see above). The "if you can see one" condition is from S8, the concrete wording from F, and "You rode up through one of them" is S8's callback.

**S9: fixed** (002).
- Before: "Walk on along the walkway to the first place where you can look down into the excavation and see how deep it goes. The next stop in the Antiquarium is Seville stacked up."
- After: "Walk on along the walkway in the Antiquarium, and play the next stop at the first good view down into the remains: Seville stacked up."
- 003's @where was aligned to "the first good view down into the remains".

**S10: fixed** (021). Added "Any map on your phone will show you the way." after "Both are nearby: …".

**S11: fixed** (019).
- Hook: "In 1973 the traders of this square were promised…" → "By the lifts, you heard how the old market hall came down in 1973. Its traders were promised…"
- "A market hall had stood here since the 1830s. In 1973 it was demolished, largely because of structural problems, and the stallholders moved…" → "When the old hall came down, the stallholders moved…"
- "became a fenced, dusty car park" → "became a car park".
- The 29-word sentence was split: "The architect had kept its place in the plan. The market went at street level, with this square on top of it, like a roof you can walk on."

**S12: fixed** (017). "On the twenty-seventh of March 2011, Mayor Alfredo Sánchez Monteseirín opened it" → "…, the mayor opened it". The hook is unchanged.

**S13: fixed** (013).
- "Three directions are worth fixing first." → "Three directions are worth fixing, even if you found some of them on the walkway."
- "Beyond them rises the Aljarafe, the high ground west of the city." → "Beyond them rises the Aljarafe, the higher ground on that side of the river." The auditor's "the higher ground beyond the river" was reworded to avoid "beyond… beyond".

**S14: fixed** (018). Cut "Built for fairs and concerts, the square held a protest camp in its very first season."

**S15: fixed** (002).
- Before: "The remains cover some 1,200 years of the city's life, from about the time of the emperor Tiberius, in the first century, to the 1200s."
- After: "The remains span some twelve centuries. The oldest go back to the emperor Tiberius, in the first century. The latest are from the 1200s."

**S16: fixed.** The auditor's text was used in each case.
- 014: "…roughly doubled. The budget was about 51 million euros. The final bill came to about 102 million."
- 016: "…more than two hundred square metres. One trade report says its stands hold ninety-six people."
- 018: "…almost four thousand square metres. And it stands about five metres up, on the roof of the market." This is combined with F-018.3a.
- 015:
  - "…and how they move. It also follows the weather, the wind and the season."
  - "…under thirty percent of the lights are on at once. That gives a sense of movement, with less light spilling into the sky."

**S17: fixed.** The auditor's text was used in each case.
- 016: "Add sound from every side, images on the floor, moving air and even scents. It's a room built to work on all your senses."
- 016: "…together with Aurora, the light show. Sacyr calls it part of a complete renewal of the building."
- 017: "He pointed to the Eiffel Tower, which Paris had once argued about too. Seville, he said, could be proud of a new symbol of modernity and technology."
- 019: see S11.

**S18: fixed** (020).
- Before: "And when Aurora is running, the timber above you lights up after sunset."
- After: "And after sunset, when the Aurora light show is running, the timber above you lights up."

**S19: fixed** (011). "from the first century AD" → "from the first century", and "between 70 and 120 AD" → "between the years 70 and 120".

**S20: fixed** (012). "That was right at the limit the glue was rated for." → "Sixty Celsius: right at the limit the glue was rated for."

**S21: fixed** (009). "singular trees" → "remarkable trees", with the F-009.1 source upgrade. 021 no longer has the phrase (M3).

**S22: fixed** (018). "Seville's indignados made it…" → "Seville's indignados, "the outraged", made the Setas…".

### NICE
- **N1: fixed** (009). "He didn't set out to build mushrooms. But Sevillanos called it las Setas anyway. The nickname stuck…" → "He didn't set out to build mushrooms. But the nickname stuck…". Every version hears 001's nickname first.
- **N2, N3: no change.** The auditor judged both acceptable. M2's wording also softens N2.
- **N4: fixed** through F-004.2. There is now one attribution chain ("her study" / "the specialist study" / "the study"), and no "scholar" remains in 004–006.
- **N5: fixed** (007). Cut "The story of the square above you comes by the lifts."
- **N6: fixed** (008).
  - "at the end" → "near the end".
  - "Joseph Bonaparte's government ordered…" → "the government of Napoleon's brother, Joseph Bonaparte, ordered…". The hook's phrase is reused, and the unsourced "then ruling Spain" was not added.
- **N7: fixed** (010). "the cathedral chapter voted" → "the cathedral's clergy voted". The "it" ambiguity was fixed by M3.
- **N8: fixed** (011). "Toward the river lie the rooftops of Triana, on its far bank." → "Across the river, on its far bank, lie the rooftops of Triana."
- **N9: fixed** (019). Cut "You can visit it afterwards, from the street." 020 keeps its line.
- **N10: fixed** (001).
  - "From the north entrance, the way down leads to the same underground level." → "From the north entrance, you go down to the same underground level."
  - "First comes level minus one, with the taquilla…" → "First comes level minus one. There you'll find the taquilla, the box office, and the Antiquarium, the museum of the remains."
  - To stay at 358, "some of the ruins" became "some ruins".
- **N11: not done** (012). "The polyurethane you heard about in the lift…" adds 5 words, and 012 is at the R cap of 280.
- **N12: no change.** The auditor judged the three cathedral metaphors acceptable, and no fourth was added.
- **N13: fixed** (005). The gloss now comes before the name: "Hospitium is Latin for hospitality, or for taking in guests. In the Hospitium de los Delfines…" The old version gave the gloss three sentences after it.
- **N14: fixed** (bridges). These use the auditor's texts. In E, the last clause is split off to keep the sentences under 25 words.
  - 001 E>008: "On this shorter tour, skip the Antiquarium. Once you're down on level minus one, go to the lifts beside its entrance, the Mirador access. Play the next stop there, before you go up: A plaza with many lives."
  - 001 H>009: "On this shorter tour, skip the Antiquarium. Once you're down on level minus one, go to the lifts beside its entrance, the Mirador access. Take the lift up, and start the next stop as the doors close: Mushrooms of wood."
- **N15: fixed** (001). "and it opened on 27 March 2011" → "and opened on the twenty-seventh of March, 2011".
- **N16: not done.**
  - `v5/ONSITE_CHECKLIST.txt` still uses the old V5 track numbers. Its O9 line ("Track 12: the Mirador 360") does not ask for a check of 013's derived north cue ("Giralda at your back").
  - Renumbering one line out of a whole V5-numbered checklist would leave it inconsistent, so the checklist needs a full V5.1 renumbering pass (lead).
- **N17: not done** (lead decision 1). The titles keep "360º", "21 metres" and "37 years", because the app does not voice titles.

## Still open (for the lead or on site)
- **O4 (006, 005):**
  - Whether the emblem's label names the Hospitium de los Triclinia. The track works whatever the label says.
  - Whether the Casa de Baco floor and its corner vessels are on show.
- **O20 / 009.1b:** "centennial" for the Cristo de Burgos ficus (City guide, p. 114).
- **N16:** a V5.1 renumbering of ONSITE_CHECKLIST, including the north cue for 013.
- **Caps:** 004, 012 and 015 are at their caps, so any later addition there must cut something.

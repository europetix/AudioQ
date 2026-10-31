# AUDIT FIXES 001–025: Poble Espanyol EN, 31 Oct 2026

This note applies `research/AUDIT_V5_FACTS.md` (IDs **F-**) and `research/AUDIT_V5_ROUTE_LISTENING.md` (IDs **R-**), with the lead's seven decisions (**L1–L7**) overriding where they conflict. Every MUST and SHOULD is fixed (R-S4 only partly, pending O10). NICE items are fixed where worthwhile, and the ones not done are given with reasons.

**Checks after editing:**
- `python3 v5/lint.py` prints OK for all 25.
- Every last paragraph ends with the next main stop's @title (`—` spoken as `·`), checked by script: 24/24.
- Every bridge was retraced on `research/map/` (NE and NW zooms): 8 bridges, 35–45 words including the closing title.
- No `*`, `XIII`, `FIESTA` or abbreviations remain in speech.
- Each track keeps its voice, tags and paragraph structure; the only change of structure is 009's second paragraph (R-S19).

**Not touched:** PLAN.md, whose §2 cue column and §3 bridge table now differ from the tracks for 008, 011, 018, 019 and 020, and from the bridges. The lead should sync PLAN, or treat these tracks as the source.

**Also edited:**
- `v5/ONSITE_CHECKLIST.txt`: the auditors' new questions for O3, O5, O8, O10, O13 and O16, and the tick-list rows for the changed cues and bridges.
- `research/FACTS_OCT2026.md` §13: a dated correction note covering rows 1.4/8.10, 1.21, 2.6, 2.11, 2.14, 2.19, 2.22, 2.24 (writer-reported), 4.8, 5.2, 5.9, 5.15, 6.41, 7.4 and ROUTE §3.4 (69 = Son Berga).

**Lead to decide:**
1. **025, Sangüesa (F-N16, HOLD):** keep the hedge ("If this arcade is the one they mean…") or cut it until O16.
2. **ALT-G2 (R-S4):** after O10, if the Sculpture Garden's way in is by the steps at 89, move 016 to after 012.
3. **PLAN sync:** update the §2 cues, §3 bridges and House key (69 → INF), or let the tracks stand as the source.
4. **023 has four dates.** "May 1929" (L3) makes the fourth.

## 1. Status by finding

| ID | Status | Tracks | What was done / why not |
|---|---|---|---|
| F-M1 | FIXED | 023 | "the following May" → "in May 1929" (lead decision 3). |
| F-M2 | FIXED | 004, 007 | Clutch letter re-dated to the second trip (November 1927); no Borja, no Hispano-Suiza; the ACE19 breakdown near Zaragoza kept as a separate, undated event (lead decision 4). |
| F-M3 | FIXED | 004 | "Reventós's desk for about ninety years" → "a desk in a Reventós family office, until the researchers found them". J. M. Reventós is named in @what/@sources, not in speech (lead decisions 4 and 6: initials a voice could misread). 023's "notebooks that lay hidden in a drawer" stands (the audit says so). |
| F-S1 | FIXED | 011 | Grey is "on the plan, outside the four region colours", not "no region at all". |
| F-S2 | FIXED | 015 | Catalanists and the earlier idea are now attributed to the study ("it points out", "it argues"). |
| F-S3 | FIXED | 012 | Eight Rupit houses on five fronts, attributed to Rupit's journal; the 79–82 number pile-up dropped (with R-S15). |
| F-S4 | FIXED | 012 | "Rupit once agreed to put a little sign on each of its houses here." |
| F-S5 | FIXED | 005 | The purple and the green are now plan colour + "the Poble's list places…", not certain matches (with R-S2, lead decision 5). |
| F-S6 | FIXED | 014 | House 69 is described by the Poble as a "Balearic Island-style stately home"; the list "has" the Casa Son Berga. No match claimed (lead decision 5). |
| F-S7 | FIXED | 019 | The Amaya story is attributed to the city's film office ("passes on the house's story… it says"; "that listing is the only place we have found it"). |
| F-S8 | FIXED | 022 | Capacity, not attendance; 1968 "decided to hold". |
| F-S9 | FIXED | 003 | No timing at all: "He created the mascot for Barcelona's 1992 Games: Cobi…". The auditor's "had already created" was not used, because Cobi's year is itself unverified (audit §3.3). |
| F-S10 | FIXED | 006 | "laid out S'Agaró" → "took charge of planning the resort of S'Agaró". |
| F-S11 | FIXED | 020 | "A count of the Francoist camps in Catalonia, sixteen of them, published by the newspaper Ara, does not mention the Poble." The auditor's word "concentration" was left out: "concentration camp" is on the PLAN NEVER list, and the route auditor's tone check relied on its absence. |
| F-S12 | FIXED | 008 | "On a journey in 1928…"; the reading is attributed to the researchers ("If they're right…"). |
| F-N1 | FIXED | 001 | "Almost every house"; "Life-size, not miniatures." |
| F-N2 | FIXED | 002 | "official visitors". |
| F-N3 | FIXED | 003 | "By 1990 the village had a weak spot." |
| F-N4 | FIXED | 004 | "stood ready with the camera". |
| F-N5 | FIXED (hedged) | 008 | No claim that the cast has glazed ceramic: "The real tower's ceramics flash in the sun… does this one catch the light too?" Restore "find the glazed ceramic" only if O5 confirms (added to ONSITE O5). |
| F-N6 | FIXED | 010 | "Among the festivals it takes in are…". |
| F-N7 | FIXED | 010 | "the one they said they liked better". |
| F-N8 | FIXED | 011 | "small" dropped. |
| F-N9 | FIXED | 013 | The unconfirmed Catalan clause is no longer quoted: it is a paraphrase without quote marks, naming the three confirmed houses. |
| F-N10 | FIXED | 014 | "lists a fountain from Prades… among the village's models, without saying where it stands". |
| F-N11 | FIXED | 014 | "The islands were left out of the first plans." (018 already said "The islands"). |
| F-N12 | FIXED | 017 | "Lombard-style" cut; "Every source on the village's authorship credits the same four men instead". |
| F-N13 | FIXED | 018, 025 | "The historians credit a king who asked where it was" / "A quarter the historians credit to a king who asked…". |
| F-N14 | FIXED | 023 | "a message from the trip reads". |
| F-N15 | FIXED | 024 | "three Barcelona critics". |
| F-N16 | FIXED + HOLD | 025 | Montjuïc: "being remodelled, with work timed toward it". Sangüesa porticoes are HOLD per the audit: hedged to "on this side of the square… If this arcade is the one they mean". **Lead to decide:** keep the hedge or cut the paragraph until O16 (sign at 26; added to ONSITE O16). |
| F-§3.12 | FIXED | 013 | "blacksmithing with Japanese techniques" → "blacksmithing" (unverified qualifier; list shortened with R-S14). |
| R-M1 | FIXED | 002, 015, 018 | Extras are offered with "If you're on the full tour" (002) or "On the Essential and full tours" (015, 018) (lead decision 1). 009 is heard only in Full, so its offer needs no qualifier. |
| R-M2 | FIXED | 008, 009, 011, 020 + bridges | Checked on the NE plan zoom. The tower stands between Plaza Aragonesa and Plaza del Carmen; the church is 57–59; the Plaza de la Iglesia is reached along the church front (the blue route) and marked by the top of the wide steps. The museum is the grey block behind the church, reaching the Plaza de la Iglesia by the Guinovart Space (56). 008 now says "Walk on along the front of the church to the Plaza de la Iglesia, the small square where a wide flight of steps goes down". 009 @where, 011 @where and cue ("go back along the church"), 020's opening and cue, and bridges 008 E>011, 018 H>022, 018 E>019 and 019 E>021 all match. "Long grey front" is gone from speech. O5 questions added (lead decision 2). |
| R-M3 | FIXED | 023 | As F-M1. The workers clause kept, attributed (the facts audit's version); the budget sentence cut instead (R-S15). 023 now has four dates (1927, 1599, 1928, 1929): one over the standard's three, which the lead's "May 1929" requires. |
| R-S1 | FIXED | 001 | "…so pick one up at the entrance." (trimmed "if you can" for length). |
| R-S2 | FIXED | 005 | "Just off the start of the street, one row back, the plan shows a little purple…"; O3 question added. |
| R-S3 | FIXED | 011, bridge 008 H>012 | "house 83, a few doors up, before Carrer Mercaders comes in. It's the house with an outside stair up its front". |
| R-S4 | PARTLY | 016 (+015 kept) | 015's line kept ("below the viewpoint" is a PLAN-allowed feature). 016's cue made entrance-neutral: "Leave the garden the way you came in, and take the steps from the Baluard up to the monastery." 016 @where flags the unknown way in. O10 question added. **ALT-G2 (held, lead to approve after O10):** if the way in is by the steps at 89, play 016 from the 012 stop. 012's E cue would get "On the Essential and full tours, there's a short Extra in the Sculpture Garden, down the steps by house 89…", and 016's cue would become "Come back up the steps and walk up Carrer Mercaders to house 81". Not written into the tracks: it reorders E/Full and depends on O10. |
| R-S5 | FIXED | 019 | "Walk on down Calle Arcos, which has steps. At its foot you come out by the brick tower, where the little Plaza del Carmen opens". |
| R-S6 | FIXED | 014 | "Morella and Catí elsewhere in the village, and La Jana, which the list places round this square". |
| R-S7 | FIXED | 025 | "An outside stair with seven steps, where Rupit's has fourteen." pays off 012's "Keep that number" (025 is in every version). |
| R-S8 | FIXED | bridges 012 H>015, 018 H>022 | Both now end with the closing title. 012 H>015 glosses the Baluard. 018 H>022 routes past the tower and the church, and the "Gradas de Santiago steps" both glosses gradas and warns of steps. |
| R-S9 | FIXED | new bridge 018 E>019 | "On this shorter tour, the next main stop is the top of the Gradas de Santiago. Without the Extra, take Calle Bulas to the Plaza del Carmen and pass the tower and the church to the Plaza de la Iglesia: Gradas de Santiago · The North." 019 E>021 kept and rewritten. |
| R-S10 | FIXED | 018, 019 | "house 61" and "number 9" removed from speech (kept in @where/@room with [O13]); O13 asks whether 9 is posted. |
| R-S11 | FIXED | 018, 019 | "down Calle Arcos, which has steps"; O13 question added. |
| R-S12 | FIXED | 014 | "above this square" (with F-S6). |
| R-S13 | FIXED | 011 (+009 @where) | "Now look at the museum's front… This block is grey on the plan"; 009/011 @where no longer call it a long grey building. |
| R-S14 | FIXED | 001, 004, 006, 024, 013 | The long sentences in 001, 004, 006 and 024 are split as the auditor proposed (004's quote kept verbatim in two parts). 013's crafts list is cut to six. Cues 008, 015, 017, 019 and 020 are all under 30 words a sentence now. |
| R-S15 | FIXED | 004, 012, 015, 023 | 004: "A month on the road." 012: the 79–82 numbers are dropped. 015: "almost six million visitors", and the deficit line is cut (the debt stays in the encyclopedia sentence). 023: the budget is cut. |
| R-S16 | FIXED | 002, 005, 007, 014, 021 | Name lists cut to the auditor's shorter forms. 021 drops Caldas de Reyes and Maluenda; its honest line on unplaced towns stays in the next paragraph. |
| R-S17 | FIXED | 008, 023 | "Mudéjar ones, in brick and glazed ceramic, like Utebo's tower" (not "like this tower", which N5 leaves unconfirmed); "a late-Renaissance, Mannerist building". |
| R-S18 | FIXED | 002, 008, 009, 010, 018, 019, 025 | "Alfonso the Thirteenth"; "Fiesta" in speech (the @title of 010 and @room keep PLAN's FIESTA). The asterisk markers are removed from speech everywhere (lead decision 6). |
| R-S19 | FIXED | 009 | The second paragraph is now "You heard the recipe at the tower. Here you can see it." The freed words give the Extra's location (N5). |
| R-S20 | FIXED | 022 | "The makers wanted a square with changes of level, and that, the historians write, …"; "On the opposite side, they note, the plan for that row grew…". |
| R-S21 | FIXED | 025 | "Without the journey, the Poble Espanyol would not just be very different: 'it would probably no longer exist. It would have disappeared long ago.'" |
| R-S22 | FIXED | 018 | "with Arcos, five Andalusian provinces". |
| R-N1 | NOT DONE | – | Global attribution thinning would touch every track and every quote's language tag (a PLAN rule). Only local repeats were fixed (012, 022, 025). Left for the lead's read-through. |
| R-N2 | FIXED (part) | 008, 021, 023 | "A campanile is a bell tower."; Fefiñáns dropped with R-S16; "Valencia's old court building, the Audiencia". Pre-Romanesque left as the auditor advised. |
| R-N3 | FIXED | 014 | "Next, the view." |
| R-N4 | NOT DONE (pending O9) | 015 | The three landmarks are attributed ("says the Poble's own page… See how many you can find"); cut any that O9 does not tick. |
| R-N5 | FIXED | 009 | "Play it at the show's door, before you go in." |
| R-N6 | FIXED | 022, 023, 025 | "The Poble shows its photographs… inside"; "the Poble says you'll find inside"; "Fiesta… is in the brick tower…, the Poble says". The glassblower line in 025 is left as is: it is a DATED, cuttable sentence. |
| R-N7 | FIXED | 017 | "the Vidre art gallery, a former glassblowing workshop". |
| R-N8 | FIXED | 015 | "A step-free path climbs to it round the houses at the top of Plaça de la Font." (the ALT-S route; [O8, O18]). |
| R-N9 | FIXED | 021 | "the Gradas de Santiago, the Santiago Steps"; the H bridge says "Gradas de Santiago steps". |
| R-N10 | FIXED | 001 | "the Fran Daurel art museum". |
| R-N11 | NOT DONE (render check) | all cues | The "·" cue separator is a series convention and is required by the cue format and by PLAN. Confirm it renders as a short pause at the TTS listening QA. |
| R-N12 | NOT DONE | 023 | "on the square's steps toward Plaza Castellana" would place the steps by geometry (the plan's inner steps are not clearly on that side). Wait for O15. |
| R-N13 | NOTED | all | Every addition was offset in the same track. Final counts (spoken words): 001 359, 002 352, 003 213, 004 356, 005 253, 006 360, 007 260, 008 359, 009 249, 010 222, 011 352, 012 256, 013 258, 014 347, 015 359, 016 218, 017 345, 018 359, 019 229, 020 354, 021 252, 022 355, 023 349, 024 360, 025 345. That is 7,721 in Full (was 7,822; E 6,683, H 3,445), so 001's times still hold. |
| L1 | DONE | 002, 015, 018 | See R-M1. |
| L2 | DONE | 008, 009, 011, 020, bridges | See R-M2. |
| L3 | DONE | 023 | See F-M1. |
| L4 | DONE | 004, 007 | See F-M2, F-M3. |
| L5 | DONE | 002, 005, 009, 012, 013, 014, 022, 025 | Unconfirmed matches and numbers are now "the Poble's list places…" or "Rupit's own local journal places… here, at number 83/81" (DOC numbers by source, attributed until O2/O6/O7), or a landmark. 017's "house at number 69" and 024's "arcade at house 26" are plan landmarks in cues, not matches, so they are kept. |
| L6 | DONE | 003, 006, 007, 009, 011, 014, 016, 017, 019, 021, 025 | All *…* markers are removed from spoken text, so no asterisk is left in any body. No initials, "C/", "No.", "%" or Roman numerals are left in speech. "1.3 million" (024) is left: it reads as "one point three million". |
| L7 | DONE | bridges | Rewritten: 008 E>011, 008 H>012, 012 H>015, 018 H>022, 019 E>021. New: 018 E>019. Unchanged, because their track endings still fit: 004 H>008, 022 H>025. |

## 2. Bridges, before → after

- **004 H>008** (unchanged; still fits): On this shorter tour, skip the next stops: walk on up Calle Caballeros as it curves into Calle Príncipe de Viana, to Plaza Aragonesa and its tall brick tower. Stop where you see the whole tower: Plaza Aragonesa · The tower they liked better.
- **008 E>011**
  - before: On this shorter tour, skip the church: walk round to the Plaza de la Iglesia and stop by the door of the Fran Daurel Museum: Plaza de la Iglesia · A bottler's art collection.
  - after: On this shorter tour, skip the church's story: walk on along its front to the Plaza de la Iglesia and stop by the door of the Fran Daurel Museum: Plaza de la Iglesia · A bottler's art collection.
- **008 H>012**
  - before: On this shorter tour, head instead up Carrer de la Davallada, which climbs from Plaza Aragonesa into the Catalan quarter, to house 83, just below where Carrer Mercaders comes in, with an outside stair: Carrer de la Davallada · Seven steps, not fourteen.
  - after: On this shorter tour, head instead up Carrer de la Davallada, which climbs from this square into the Catalan quarter. Stop at house 83, a few doors up, the house with an outside stair: Carrer de la Davallada · Seven steps, not fourteen.
- **012 H>015**
  - before: On this shorter tour, don't stop at house 81. Carry on up Carrer Mercaders, past the glassblower's, to Plaça de la Font, then walk on past the Baluard to the viewpoint the plan calls Barcelona Panorama.
  - after: On this shorter tour, don't stop at house 81. Carry on up Carrer Mercaders to Plaça de la Font, then walk on past the Baluard, the terrace beside the square, to the viewpoint the plan calls Barcelona Panorama: Barcelona Panorama · Born under a dictatorship.
- **018 E>019**
  - before: (none)
  - after: On this shorter tour, the next main stop is the top of the Gradas de Santiago. Without the Extra, take Calle Bulas to the Plaza del Carmen and pass the tower and the church to the Plaza de la Iglesia: Gradas de Santiago · The North.
- **018 H>022**
  - before: On this shorter tour, skip Calle Arcos. Take Calle Bulas from Plaza Peñaflor down to the Plaza del Carmen, at the tower's foot. Cross the Plaza de la Iglesia, go down the Gradas de Santiago, past Rincón del Triste, to the Plaza Mayor's steps.
  - after: On this shorter tour, take Calle Bulas to the Plaza del Carmen, pass the tower and the church to the Plaza de la Iglesia, then go down the Gradas de Santiago steps into the Plaza Mayor: Plaza Mayor · A square from Riaza.
- **019 E>021**
  - before: On this shorter tour, skip the story at the Plaza del Carmen. Carry on across the Plaza de la Iglesia to the top of the Gradas de Santiago, the wide steps down toward the Plaza Mayor: Gradas de Santiago · The North.
  - after: On this shorter tour, skip the story at the Plaza del Carmen. Pass the tower and the church to the Plaza de la Iglesia and the top of the Gradas de Santiago, the wide steps down toward the Plaza Mayor: Gradas de Santiago · The North.
- **022 H>025** (unchanged; still fits): On this shorter tour, skip the town hall. Walk to the corner of the square by the arcade at house 26, with Plaza Castellana and the gate just beyond: Plaza Mayor · The village that stayed.

## 3. Every edit, before → after (by track; spoken text unless marked meta)

### 001
- **F-N1**
  - before: [warmly] Every house in this village comes from somewhere else.
  - after: [warmly] Almost every house in this village comes from somewhere else.
- **F-N1**
  - before: Full size, not miniatures.
  - after: Life-size, not miniatures.
- **R-S1**
  - before: Many stops name a house by its number on that plan.
  - after: Many stops name a house by its number on that plan, so pick one up at the entrance if you can.
- **R-S14**
  - before: Up Calle Caballeros to Aragon's brick tower, through Catalonia to the monastery at the top and its view of Barcelona, then down through the white streets of Andalusia and the Santiago Steps to the Plaza Mayor, and out through this gate.
  - after: Up Calle Caballeros to Aragon's brick tower, then through Catalonia to the monastery at the top, with its view of Barcelona. Then down through the white streets of Andalusia and the Santiago Steps to the Plaza Mayor, and out through this gate.
- **R-N10**
  - before: nearer two hours if you also go round the art museum.
  - after: nearer two hours if you also go round the Fran Daurel art museum.
- **R-N13 (length)**
  - before: In the shorter versions the track numbers on your phone may jump.
  - after: In the shorter versions the numbers may jump.
- **R-N13 (length)**
  - before: Start with the way you came in. Stay in Plaza Castellana and face the gate, its two round towers
  - after: Stay in Plaza Castellana and face the gate you came in by, its two round towers
- **R-S1 (trim)**
  - before: so pick one up at the entrance if you can.
  - after: so pick one up at the entrance.
### 002
- **F-N2**
  - before: In 1929, the Exhibition's most important visitors were photographed right here.
  - after: In 1929, the Exhibition's official visitors were photographed right here.
- **R-S18**
  - before: The King and Queen, Alfonso XIII and Victoria Eugenia, came
  - after: The King and Queen, Alfonso the Thirteenth and Victoria Eugenia, came
- **R-S16, L5**
  - before: By the Poble's own list, the Casa del Sol, from Cáceres, is house 3. Round this square the list also places the Golfines, Carvajal, Mayoralgo and Ovando houses of Cáceres, the Almaraz house of Plasencia and the bishop's palace of Miajadas.
  - after: The Poble's own list places the Casa del Sol, from Cáceres, at house 3. Round this square it also places more noble houses from Cáceres, one from Plasencia and a bishop's palace from Miajadas.
- **R-M1, L1**
  - before: There's a short Extra you can play here, on what these towers became about sixty years later.
  - after: If you're on the full tour, there's a short Extra here, on what these towers became in 1990.
### 003
- **F-N3, L6**
  - before: [conspiratorial] For about sixty years the village had a weak spot. In 1990 the Catalan magazine *El Temps* described it
  - after: [conspiratorial] By 1990 the village had a weak spot. That year the Catalan magazine El Temps described it
- **F-S9**
  - before: Two years later Barcelona's Games had a mascot he created: Cobi,
  - after: He created the mascot for Barcelona's 1992 Games: Cobi,
- **F-S9 (meta)** (meta)
  - before: Mariscal's Cobi, the Barcelona 1992 mascot.
  - after: Mariscal's Cobi, the Barcelona 1992 mascot (no creation year spoken: unverified, AUDIT_V5_FACTS S9).
### 004
- **R-S14**
  - before: He wrote, in Spanish, that the journey was "so indispensable that a good part of the work done this month will, logically, be changed by the living things that the architects and our friend Nogués will see" as they travelled round Spain.
  - after: He wrote, in Spanish, that the journey was "so indispensable that a good part of the work done this month will, logically, be changed". Changed, he went on, "by the living things that the architects and our friend Nogués will see" as they travelled round Spain.
- **R-S15**
  - before: Thirty-one days, at a planned two hundred kilometres a day.
  - after: A month on the road.
- **F-N4**
  - before: while the two architects waited with the camera for a good photograph.
  - after: while the two architects stood ready with the camera.
- **F-M2, L4**
  - before: On the road to Zaragoza the car broke down, and Utrillo recorded the moment in a caricature. A letter from Borja says, in Catalan, "we have the car in Tudela being repaired, because the clutch burned out".
  - after: Near Zaragoza the car broke down, and Utrillo recorded the moment in a caricature. On the second trip, that November, a letter was written while they waited for the Zaragoza express. It says, in Catalan, "we have the car in Tudela being repaired, because the clutch burned out".
- **F-M3, L4**
  - before: stayed in Reventós's desk for about ninety years. The researchers who found them wrote:
  - after: lay hidden in a desk drawer in a Reventós family office until the researchers found them. They wrote:
- **F-M3 (meta)** (meta)
  - before: the five travel notebooks in Reventós's drawer;
  - after: the five travel notebooks, hidden in a desk drawer in the office of J. M. Reventós (ACE19 p. 239 n. 11; "Private archive of the Reventós family", EGA24), no duration sourced;
- **F-M3 (meta)** (meta)
  - before: and how their notebooks resurfaced ninety years later.
  - after: and how their notebooks stayed hidden in a drawer until researchers found them.
- **F-M2 (meta)** (meta)
  - before: letter of 15/11/27 "tenim l'auto a Tudela
  - after: letter of 15/11/27 (second trip; writer not named; "l'auto", car not named), waiting for "l'Expres de Zaragoza", "tenim l'auto a Tudela
- **F-M3 (meta)** (meta)
  - before: desk drawer via FACTS 2.14)
  - after: p. 239 n. 11, re-read by the fact audit: notebooks "ocultas en el cajón del escritorio del despacho de J.M Reventós", "hasta hoy", no duration)
- **R-S14 (trim)**
  - before: Changed, he went on, "by the living things that the architects and our friend Nogués will see" as they travelled round Spain.
  - after: Changed "by the living things that the architects and our friend Nogués will see".
- **F-M2 (trim)**
  - before: a letter was written while they waited for the Zaragoza express. It says, in Catalan,
  - after: a letter written while they waited for the Zaragoza express says, in Catalan,
- **R-N13 (length)**
  - before: and only three of them unchanged.
  - after: and only three unchanged.
- **F-M2 (sentence length)**
  - before: a letter written while they waited for the Zaragoza express says, in Catalan,
  - after: a letter was written while they waited for the Zaragoza express. It says, in Catalan,
- **R-N13 (length)**
  - before: Look up the street in front of you: this is what all that voting produced.
  - after: Look up the street: this is what all that voting produced.
- **F-M3 (wording)**
  - before: lay hidden in a desk drawer in a Reventós family office until the researchers found them.
  - after: lay hidden there, in a desk in a Reventós family office, until the researchers found them.
### 005
- **R-S16**
  - before: There's the Casa del Doncel from Sigüenza. From Ayllón, in Segovia, the Casa de la Torre and the Contreras palace. The bishop's palace of El Burgo de Osma. A fifteenth-century house from Segovia, and houses from Toro. From Soria, the Casa del Francés of Molinos de Duero and the Casa Ramos of Vinuesa.
  - after: There's the Casa del Doncel from Sigüenza, palaces from Ayllón and El Burgo de Osma, and houses from Segovia, Toro and Soria.
- **F-S5, R-S2, L5**
  - before: Near the start of the street the plan shows two purple houses, and the list says they come from the Mediterranean: from Jérica, in Castellón, and the Desclergue house of Montblanc, in Catalonia. And the run of green belongs to the north, to Cantabria: the house of the Marqués de Santillana.
  - after: Just off the start of the street, one row back, the plan shows a little purple, the Mediterranean colour. The Poble's list places two Mediterranean houses here, from Jérica, in Castellón, and the Desclergue house of Montblanc, in Catalonia. It also lists a northern one, green on the plan, from Cantabria: the house of the Marqués de Santillana.
- **R-S2 (meta)** (meta)
  - before: the purple Jérica (Castellón) and Casa Desclergue (Montblanc, Tarragona);
  - after: the purple Jérica (Castellón) and Casa Desclergue (Montblanc, Tarragona), pins on 23/24, which sit one row back from the street frontage on the plan [O2, O3];
### 006
- **L6**
  - before: He called it *Iberiona*.
  - after: He called it Iberiona.
- **R-N13 (length)**
  - before: A few years later Utrillo brought his idea back.
  - after: Later, Utrillo brought his idea back.
- **F-S10**
  - before: Francesc Folguera, who later laid out S'Agaró.
  - after: Francesc Folguera, who later took charge of planning the resort of S'Agaró.
- **R-N13 (length)**
  - before: The village was the last of the Exhibition's projects to be awarded, and it got a leftover plot.
  - after: The village was the Exhibition's last project to be awarded, and it got a leftover plot.
- **R-S14, L6**
  - before: [wry] In December 1929 a gossip column in the Catalan magazine *Mirador* began: "Now it turns out that the author of the Poble Espanyol was also, if not the first, one of the first excavators of Montjuïc." It meant Utrillo.
  - after: [wry] In December 1929 a gossip column in the Catalan magazine Mirador took a swipe at Utrillo. "Now it turns out," it began, "that the author of the Poble Espanyol was also, if not the first, one of the first excavators of Montjuïc."
- **F-S10 (meta)** (meta)
  - before: ENC-FOLG https://www.enciclopedia.cat/EC-GEC-0027326 (SEC: S'Agaró)
  - after: ENC-FOLG https://www.enciclopedia.cat/EC-GEC-0027326 (SEC, re-read by the fact audit: "Es feu càrrec de la urbanització de s'Agaró el 1935", took charge of planning S'Agaró)
### 007
- **F-M2, L4**
  - before: Tudela, where the Hispano-Suiza sat in the repair shop, is a Navarrese town.
  - after: On the second trip, in November 1927, the car ended up in a repair shop in Tudela, a Navarrese town.
- **R-S16**
  - before: include the palace of San Cristóbal, from Estella, and the Casa de las Cadenas, from Corella. There are carved pre-Romanesque reliefs from Villatuerta, a coat of arms from Olazagutía, and a house from the Roncal valley.
  - after: include the palace of San Cristóbal, from Estella, the Casa de las Cadenas, from Corella, and a house from the Roncal valley. There are carved pre-Romanesque reliefs too.
- **R-S16, L6**
  - before: Then the Basque Country. A farmhouse, a *caserío*, the Casa Arteche from Erandio in Bizkaia. A house from Vergara, in Gipuzkoa. The list also has the palace of the Álava-Esquivel family.
  - after: Then the Basque Country: a farmhouse, a caserío, from Bizkaia, and a house from Gipuzkoa.
- **F-M2 (meta)** (meta)
  - before: (SEC-acad, re-read 31 Oct 2026: the car repaired in Tudela)
  - after: (SEC-acad, re-read 31 Oct 2026 and by the fact audit: the car repaired in Tudela, letter dated 15/11/27, i.e. the second trip; the car is "l'auto", not named)
- **R-S16 (sentence length)**
  - before: the palace of San Cristóbal, from Estella, the Casa de las Cadenas, from Corella, and a house from the Roncal valley. There are carved pre-Romanesque reliefs too.
  - after: the palace of San Cristóbal, from Estella, and the Casa de las Cadenas, from Corella. There's a house from the Roncal valley, and carved pre-Romanesque reliefs too.
### 008
- **F-S12, R-N2**
  - before: [wry] On a later journey, the travellers passed the real tower at Utebo again, and wrote a note. It says, in Catalan, "We like the Exhibition's campanile better than Utebo's." They meant their own design, the one in front of you. They liked their version more than the original.
  - after: [wry] On a journey in 1928, passing the real tower at Utebo again, one of them wrote a note, in Catalan: "We like the Exhibition's campanile better than Utebo's." A campanile is a bell tower. The researchers read it as meaning their own design, the one in front of you. If they're right, the travellers liked their version more than the original.
- **R-S17**
  - before: So they swapped the Baroque models they had planned for Mudéjar ones.
  - after: So they swapped the Baroque models they had planned for Mudéjar ones, in brick and glazed ceramic, like Utebo's tower.
- **F-N5**
  - before: Now look up at it. Find the glazed ceramic set into the brick. If the sun is out, wait a moment and watch it flash. That's the effect that gave the real tower its nickname.
  - after: Now look up at it. The real tower's ceramics flash in the sun. If the sun is out, wait a moment: does this one catch the light too? That's the effect that gave the original its nickname.
- **R-S18**
  - before: The Poble's ten-minute show of Spain's festivals, FIESTA, is,
  - after: The Poble's ten-minute show of Spain's festivals, Fiesta, is,
- **R-M2, L2**
  - before: Walk round to the Plaza de la Iglesia, the small square on the other side of the tower and the church, below the long grey front of the Fran Daurel Museum: Plaza de la Iglesia · A church from three towns.
  - after: Walk on along the front of the church to the Plaza de la Iglesia, the small square where a wide flight of steps goes down: Plaza de la Iglesia · A church from three towns.
- **R-M2 (meta)** (meta)
  - before: it rises between Plaza Aragonesa and Plaza del Carmen, beside the church and the long grey front of the Fran Daurel Museum. [O5]
  - after: it rises between Plaza Aragonesa and Plaza del Carmen, at the end of the church (57–59 on the plan). The Plaza de la Iglesia is reached along the church front; the Fran Daurel Museum is the grey block on the plan behind the church. [O5, O14]
### 009
- **R-M2 (meta), L2** (meta)
  - before: @where: In the Plaza de la Iglesia, the small square below the long grey front of the Fran Daurel Museum, facing the front of the church with the brick tower beside it. [O5]
  - after: @where: In the Plaza de la Iglesia, reached from Plaza Aragonesa along the church front (57–59 on the plan), the small square where the wide steps of the Gradas de Santiago go down; face the church front, with the brick tower at its far end. [O5, O14]
- **R-S19**
  - before: The preliminary design, drawn before the great journey of 1927, fused two churches into one, from Amorebieta in the Basque Country and Caldes de Montbui in Catalonia. You heard at the tower how Aragon won the travellers over. The church paid the price. Out went the Baroque, and in came Aragon's Mudéjar.
  - after: You heard the recipe at the tower. Here you can see it.
- **L6**
  - before: *una simbiosis*
  - after: una simbiosis
- **L5**
  - before: On this square, the Poble's own list of buildings includes the Carmelite church of Alcañiz.
  - after: The Poble's own list places the Carmelite church of Alcañiz on this square.
- **R-N5, R-S18**
  - before: There's a short Extra here about FIESTA, the ten-minute show of light and sound inside the tower.
  - after: There's a short Extra about Fiesta, the ten-minute show of light and sound that the Poble places inside the tower. Play it at the show's door, before you go in.
### 010
- **R-S18**
  - before: The Poble places its show, called FIESTA,
  - after: The Poble places its show, called Fiesta,
- **F-N6**
  - before: [lightly] It takes in four festivals. The human towers of the Castellers. La Patum of Berga. The Sanfermines of Pamplona. And Holy Week in Andalusia.
  - after: [lightly] Among the festivals it takes in are the human towers of the Castellers, La Patum of Berga, the Sanfermines of Pamplona, and Holy Week in Andalusia.
- **F-N7**
  - before: the one they joked they liked better than the original.
  - after: the one they said they liked better than the original.
### 011
- **R-M2 (meta), R-S13** (meta)
  - before: @where: By the door of the Fran Daurel Museum on the Plaza de la Iglesia, the long grey building beside the brick tower; stand to one side of the door. [O5, O24]
  - after: @where: By the door of the Fran Daurel Museum on the Plaza de la Iglesia; on the plan the museum is the grey block behind the church, between the brick tower and the Guinovart Space (56). Stand to one side of the door. [O5, O24]
- **F-S1 (meta)** (meta)
  - before: Grey on the official plan (no region).
  - after: Grey on the official plan, outside the four region colours (82 and 89 are grey too; the plan has no grey legend).
- **L6**
  - before: *Alice au pays des merveilles*
  - after: Alice au pays des merveilles
- **L6**
  - before: *Cavalier avec son aurige*
  - after: Cavalier avec son aurige
- **F-N8**
  - before: From Miró, a small selection of lithographs
  - after: From Miró, a selection of lithographs
- **F-S1, R-S13**
  - before: Now look at the long grey front of the museum. On the official plan the houses are coloured by region: green, pink, yellow or purple. This block is grey. Unlike the houses round it, it stands for no region at all.
  - after: Now look at the museum's front. On the official plan the houses are coloured by region: green, pink, yellow or purple. This block is grey on the plan, outside the four region colours.
- **R-S3, L2**
  - before: From here, go back to Plaza Aragonesa and start up Carrer de la Davallada, the street that climbs into the Catalan quarter. Stop at house 83, just below where Carrer Mercaders comes in, where an outside stair climbs the front of the house:
  - after: From here, go back along the church to Plaza Aragonesa and start up Carrer de la Davallada, the street that climbs into the Catalan quarter. Stop at house 83, a few doors up, before Carrer Mercaders comes in. It's the house with an outside stair up its front:
### 012
- **F-S3, R-S15, L5**
  - before: This is house 83, Can Banús, the Poble's version of a house in Rupit, a village in the province of Barcelona. Rupit gave the Poble eight houses in all. Four more, Can Betes, Can Vázquez, a house put together from several, and Can Lo, are numbers 79, 80, 81 and 82 on Carrer Mercaders, just above.
  - after: Rupit's own local journal places Can Banús here, at number 83: the Poble's version of a house in Rupit, a village in the province of Barcelona. It counts eight Rupit houses in the village, on five fronts: this one, and four more just above, on Carrer Mercaders.
- **F-S3 (follow-on)**
  - before: The writer, in Rupit's own local journal, put it like this, in Catalan:
  - after: The writer put it like this, in Catalan:
- **F-S4**
  - before: Little signs once named the houses and their towns.
  - after: Rupit once agreed to put a little sign on each of its houses here.
- **F-S3 (meta)** (meta)
  - before: One of eight Rupit houses in the Poble; Can Betes, Can Vázquez, a composite and Can Lo are 79, 80, 81 and 82 on Carrer Mercaders (DOC [O7]).
  - after: Banús counts eight Rupit houses on five fronts (83 here; 79–82 on Carrer Mercaders, with Can Serra above Can Vázquez at 80 and 81 combining Can Rovira, Can Sallent and Ca l'Estragués) (DOC [O7]).
### 013
- **F-N9, L5**
  - before: This is house 81 on Carrer Mercaders, one of the Rupit fronts. Rupit's own local journal calls it the composite. In Catalan, it says the house "took architectural elements from different houses of Rupit": pieces of Can Rovira and Can Sallent, and the doorway of a third, Ca l'Estragués.
  - after: Rupit's own local journal places a composite Rupit house here, at number 81 on Carrer Mercaders. It was put together from pieces of several houses in Rupit: Can Rovira and Can Sallent, and the doorway of a third, Ca l'Estragués.
- **R-S14 (list), F §3.12**
  - before: The crafts on the Poble's current list include pottery on the wheel, leaded stained glass, glass painting, engraving and printmaking, classical guitar making, blacksmithing with Japanese techniques, hand embroidery and wooden toys.
  - after: The crafts on the Poble's current list include pottery on the wheel, stained glass, guitar making, blacksmithing, embroidery and wooden toys.
### 014
- **L6**
  - before: of great benefit to the *poble*,
  - after: of great benefit to the poble,
- **F-N10, R-S16**
  - before: Its name, Plaça de la Font, means Fountain Square, and the Catalan encyclopedia records that the fountain is modelled on one at Prades, in the Baix Camp. The same entry lists the Catalan towns imitated in the village: Santa Pau and Besalú, Rupit, Camprodon, Isona, Montblanc, Premià de Dalt, La Garriga, Cornudella, Tàrrega, "and others".
  - after: Its name, Plaça de la Font, means Fountain Square. The Catalan encyclopedia lists a fountain from Prades, in the Baix Camp, among the village's models, without saying where it stands. The same entry lists the Catalan towns imitated here, from Besalú and Rupit to Montblanc and Tàrrega, "and others".
- **F-N11, F-S6, R-S12, L5**
  - before: The Balearic Islands were left out of the first plans, along with the Canaries. Yet the big house at number 69, just up from this square, is the Casa Son Berga, from Palma de Mallorca.
  - after: The islands were left out of the first plans. Yet the Poble's list has a house from Palma de Mallorca, the Casa Son Berga. And the Poble describes the big house at number 69, above this square, as a "Balearic Island-style stately home".
- **R-S6**
  - before: Morella, Catí, and La Jana, which the Poble's list also places round this square.
  - after: Morella and Catí elsewhere in the village, and La Jana, which the list places round this square.
- **R-N3**
  - before: Next, the top of the hill. Walk on past the Baluard
  - after: Next, the view. Walk on past the Baluard
- **F-S6 (meta)** (meta)
  - before: house 69, Casa Son Berga, Palma de Mallorca (DOC; visibility [O8]).
  - after: house 69 described by the operator as a "Balearic Island-style stately home" (EST); its identification as Casa Son Berga, Palma de Mallorca, is a pin inference (ROUTE §3.4 INF), not spoken as certain [O2, O8]; the Prades fountain's position is not sourced [O8].
- **F-N11 (meta)** (meta)
  - before: Balearic and Canary Islands excluded at first;
  - after: "Inicialmente se excluyeron las islas" (the islands, unnamed, per the fact audit);
### 015
- **R-S15**
  - before: The International Exhibition's theme was "Industry, Art and Sport". It covered more than a hundred hectares, twenty-nine nations took part, and almost five point eight million visitors came.
  - after: The International Exhibition's theme was "Industry, Art and Sport", and almost six million visitors came.
- **R-S15**
  - before:  By January 1929, Sirés counts a deficit of 140 million pesetas.
  - after: (cut)
- **F-S2**
  - before: The village's four makers were Catalanists. And Utrillo's idea for it came before the dictatorship. That, it says,
  - after: The village's four makers, it points out, were Catalanists, and Utrillo's idea, it argues, came before the dictatorship. That, it says,
- **R-M1, L1, R-N8**
  - before: There's a short Extra in the Sculpture Garden, below the viewpoint, where the giant slides are. The next main stop is the monastery at the top of the hill. Go up the steps from the Baluard to the Romanesque church with the square bell tower:
  - after: On the Essential and full tours, there's a short Extra in the Sculpture Garden, below the viewpoint, where the giant slides are. The next main stop is the monastery at the top of the hill. Go up the steps from the Baluard, or take the step-free path round the houses at the top of Plaça de la Font, to the Romanesque church with the square bell tower:
- **R-N8 (sentence length)**
  - before: The next main stop is the monastery at the top of the hill. Go up the steps from the Baluard, or take the step-free path round the houses at the top of Plaça de la Font, to the Romanesque church with the square bell tower:
  - after: The next main stop is the monastery at the top. A step-free path climbs to it round the houses at the top of Plaça de la Font. Otherwise, go up the steps from the Baluard to the Romanesque church with the square bell tower:
- **R-N8 (wording)**
  - before: The next main stop is the monastery at the top. A step-free path climbs to it round the houses at the top of Plaça de la Font. Otherwise, go up the steps from the Baluard to the Romanesque church with the square bell tower:
  - after: The next main stop is the monastery. A step-free path climbs to it round the houses at the top of Plaça de la Font. Otherwise, go up the steps from the Baluard to the Romanesque church with the square bell tower, at the top of the hill:
- **R-M1, R-N8 (meta)** (meta)
  - before: Speak only the landmarks ticked on site. [O8, O9]
  - after: Speak only the landmarks ticked on site. The cue offers the Sculpture Garden Extra to Essential and Full only, and names the step-free path round the houses at the top of Plaça de la Font (ALT-S route). [O8, O9, O10, O18, ALT-S]
### 016
- **L6**
  - before: *leves pendientes*
  - after: leves pendientes
- **R-S4**
  - before: Come back up to the Baluard and take the steps up to the monastery.
  - after: Leave the garden the way you came in, and take the steps from the Baluard up to the monastery.
- **R-S4 (meta)** (meta)
  - before: the garden is a dead end, so you come back the same way. [O10, ALT-G]
  - after: the garden is a dead end, so you come back the same way. The way in is unconfirmed: from the viewpoint and the Baluard, or by the steps beside house 89 at the foot of Carrer Mercaders, where the plan draws the garden path (if so, ALT-G2 in AUDIT_FIXES). [O10, ALT-G]
### 017
- **L6**
  - before: the *Monestir* de Sant Miquel
  - after: the Monestir de Sant Miquel
- **F-N12**
  - before: Then find the square bell tower, the Lombard-style tower modelled on Taradell's.
  - after: Then find the square bell tower, modelled on Taradell's.
- **F-N12**
  - before: Every source on the village's authorship says otherwise: it was the same four men who made the rest of the village, among them the architects Folguera and Reventós.
  - after: Every source on the village's authorship credits the same four men instead, among them the architects Folguera and Reventós.
- **R-N7**
  - before: and on between 69 and the Vidre art gallery into the Andalusian quarter.
  - after: and on between 69 and the Vidre art gallery, a former glassblowing workshop, into the Andalusian quarter.
- **R-N7 (sentence length)**
  - before: toward the big house at number 69, and on between 69 and the Vidre art gallery, a former glassblowing workshop, into the Andalusian quarter.
  - after: toward the big house at number 69. Go on between 69 and the Vidre art gallery, a former glassblowing workshop, into the Andalusian quarter.
### 018
- **R-S18**
  - before: Alfonso XIII, write the researchers
  - after: Alfonso the Thirteenth, write the researchers
- **R-S22**
  - before: Écija and Ronda: five Andalusian provinces in all.
  - after: Écija and Ronda: with Arcos, five Andalusian provinces.
- **F-N13**
  - before: It came because a king asked where it was.
  - after: The historians credit a king who asked where it was.
- **R-M1, L1, R-S10, R-S11**
  - before: There's a short Extra on Calle Arcos, at the flamenco house, the Tablao de Carmen, house 61, number 9 on the street: go through Plaza Peñaflor and down Calle Arcos.
  - after: On the Essential and full tours, there's a short Extra at the flamenco house on Calle Arcos, the Tablao de Carmen: go through Plaza Peñaflor and down Calle Arcos, which has steps.
### 019
- **F-S7, R-S18**
  - before: When the Exhibition opened in 1929, the house says, "a very young Carmen Amaya danced" for King Alfonso XIII, in its courtyard.
  - after: The house's story, as the city's film office tells it, is that when the Exhibition opened in 1929, "a very young Carmen Amaya danced" for King Alfonso the Thirteenth, in its courtyard.
- **F-S7**
  - before: we have found it only in the house's own telling.
  - after: we have found it only in the venue's own story.
- **L6**
  - before: a Catalan *bailaora*
  - after: a Catalan bailaora
- **R-S10**
  - before: [warmly] Look at the house: number 61 on the official plan, number 9 on this street.
  - after: [warmly] Look at the house: the Tablao de Carmen.
- **R-S5, R-S11**
  - before: Walk on down Calle Arcos to Carrer de la Davallada, then cross Plaza Aragonesa to the Plaza del Carmen, at the foot of the brick tower:
  - after: Walk on down Calle Arcos, which has steps. At its foot you come out by the brick tower, where the little Plaza del Carmen opens:
- **R-S10 (meta)** (meta)
  - before: house 61 on the plan and number 9 on the street; stand to one side of the door. [O13, ALT-T]
  - after: house 61 on the plan (one of several 61s along the street) and "C/ Arcos, 9" by its address (FILM-T), neither spoken until O13; stand to one side of the door. Calle Arcos has steps. [O13, O18, ALT-T]
- **F-S7 (sentence length)**
  - before: The house's story, as the city's film office tells it, is that when the Exhibition opened in 1929, "a very young
  - after: The city's film office passes on the house's story. When the Exhibition opened in 1929, it says, "a very young
- **F-S7 (wording)**
  - before: It's a lovely story, and we have found it only in the venue's own story.
  - after: It's a lovely story, and that listing is the only place we have found it.
### 020
- **L2**
  - before: You can keep walking while you listen, across toward the Plaza de la Iglesia.
  - after: You can keep walking while you listen, past the tower toward the Plaza de la Iglesia.
- **R-N13 (length)**
  - before: That is the Poble's account, in its own words.
  - after: That is the Poble's account.
- **F-S11**
  - before: A list of the Francoist camps in Catalonia, published by the newspaper Ara, counts sixteen. The Poble is not among them.
  - after: A count of the Francoist camps in Catalonia, sixteen of them, published by the newspaper Ara, does not mention the Poble.
- **L2**
  - before: Cross the Plaza de la Iglesia to the top of the Gradas de Santiago, the wide flight of steps that goes down toward the Plaza Mayor:
  - after: Walk past the tower and along the church to the Plaza de la Iglesia, and on to the top of the Gradas de Santiago, the wide steps down toward the Plaza Mayor:
- **R-N13 (length)**
  - before: When the war was over, it came back to its rooms here.
  - after: After the war, it came back.
- **L2 (sentence length)**
  - before: Walk past the tower and along the church to the Plaza de la Iglesia, and on to the top of the Gradas de Santiago,
  - after: Walk past the tower and along the church to the Plaza de la Iglesia. Stop at the top of the Gradas de Santiago,
- **R-M2 (meta), L2** (meta)
  - before: or walking on across the Plaza de la Iglesia toward the top of the Gradas de Santiago
  - after: or walking on past the tower and along the church to the Plaza de la Iglesia and the top of the Gradas de Santiago
- **F-S11 (meta)** (meta)
  - before: not on the ARA list of sixteen Francoist camps in Catalonia)
  - after: not mentioned in ARA's count of sixteen Francoist camps in Catalonia, which names 14 municipalities and covers Francoist camps only)
### 021
- **R-N9, L6**
  - before: the Gradas de Santiago, *gradas* meaning steps, and its family trail
  - after: the Gradas de Santiago, the Santiago Steps, and its family trail
- **R-S16, R-N2**
  - before: Round these steps, the Poble's own list includes houses from Galicia: Cambados and its Pazo de Fefiñáns, Betanzos, and Villanueva de Lourenzá. From Asturias, Cangas de Onís. And from Aragon, arches from Sos del Rey Católico and a house from Maluenda. A fourth Galician town on the list, Caldas de Reyes, we can't place at all.
  - after: Round these steps, the Poble's own list includes houses from Galicia, from Cambados and Betanzos among others. From Asturias, Cangas de Onís. And from Aragon, arches from Sos del Rey Católico.
### 022
- **R-S20**
  - before: The square they had in mind, with its changes of level, "they would find in the main square of Riaza", they write.
  - after: The makers wanted a square with changes of level, and that, the historians write, "they would find in the main square of Riaza".
- **R-N13 (length)**
  - before:  So the layout and the levels came from Riaza. The fronts came from all over.
  - after: (cut)
- **R-S20**
  - before: On the opposite side, they say, the row grew from five models to seven,
  - after: On the opposite side, the historians say, the plan for that row grew from five models to seven,
- **L5**
  - before: Alquézar, in Huesca, is on this square too.
  - after: Alquézar, in Huesca, is on the Poble's list for this square too.
- **F-S8**
  - before: and on concert nights more than five thousand people fill it. From 1968, a local history journal records, the village held a festival each year dedicated to one town.
  - after: and it can hold more than five thousand people for a concert. In 1968, a local history journal records, the village decided to hold a festival each year dedicated to one town.
- **R-N6**
  - before: If its door is open, the photographs of the building site are inside:
  - after: The Poble shows its photographs of the building site inside, if the door is open:
- **F-S8 (meta)** (meta)
  - before: About 2,000 m²; over 5,000 on concert nights.
  - after: About 2,000 m²; concert capacity 5,200 (SQUARE); 1968: the village agreed to hold a yearly festival (BANUS).
- **R-S20 (wording)**
  - before: On the opposite side, the historians say, the plan for that row
  - after: On the opposite side, they note, the plan for that row
### 023
- **F-N14**
  - before: the team's diary reads, in Catalan:
  - after: a message from the road reads, in Catalan:
- **R-S17**
  - before: Its town hall is a Mannerist building, finished in 1599.
  - after: Its town hall is a late-Renaissance, Mannerist building, finished in 1599.
- **R-N2**
  - before: the same interlaced pattern as the Audiencia of Valencia.
  - after: the same interlaced pattern as Valencia's old court building, the Audiencia.
- **R-N6**
  - before: If the door is open, inside is "A photographic journey. The construction of Poble Espanyol": photographs, letters and drawings from the trips, the Poble says.
  - after: If the door is open, the Poble says you'll find inside "A photographic journey. The construction of Poble Espanyol": photographs, letters and drawings from the trips.
- **R-S15**
  - before:  The budget was about two and a half million pesetas.
  - after: (cut)
- **F-M1, R-M3, L3**
  - before: and it opened the following May, about sixteen months later.
  - after: and it opened in May 1929, about sixteen months later.
- **F-N14 (wording)**
  - before: near the end of a month on the road, a message from the road reads, in Catalan:
  - after: near the end of a month on the road, a message from the trip reads, in Catalan:
- **F-N14 (meta)** (meta)
  - before: Tortosa...", diary of 1 Oct 1927)
  - after: Tortosa...", 1 Oct 1927, tagged "(FP) LP26-15b", the same LP26 series as the Nov 1927 letter, so possibly a letter rather than a diary: spoken as "a message from the trip")
- **R-S15 (meta)** (meta)
  - before: about 2.5 million pesetas, work from
  - after: about 2.5 million pesetas (not spoken), work from
### 024
- **F-N15**
  - before: how Barcelona's sharpest critics, Just Cabot,
  - after: how three Barcelona critics, Just Cabot,
- **R-S14**
  - before: the village could only be seen as "a merry-go-round for tourism": "as nicely decorated as you like by four sensitive artists, but only, and simply, a merry-go-round."
  - after: the village could only be seen as "a merry-go-round for tourism". "As nicely decorated as you like by four sensitive artists," it went on, "but only, and simply, a merry-go-round."
### 025
- **L6**
  - before: *Bé Cultural d'Interès Local*
  - after: Bé Cultural d'Interès Local
- **R-S21**
  - before: Then they go further: "Perhaps it is no longer that without the journey the Poble Espanyol would be very different. It is that it would probably no longer exist. It would have disappeared long ago."
  - after: Then they go further. Without the journey, they write, the Poble Espanyol would not just be very different: "it would probably no longer exist. It would have disappeared long ago."
- **R-S7**
  - before: An outside stair with half the steps of the one in Rupit.
  - after: An outside stair with seven steps, where Rupit's has fourteen.
- **F-N13**
  - before: A quarter added because a king asked where Andalusia was.
  - after: A quarter the historians credit to a king who asked where Andalusia was.
- **F-N16**
  - before: The Exhibition's centenary is coming, and Montjuïc is being remodelled for it.
  - after: The Exhibition's centenary is coming too, and Montjuïc is being remodelled, with work timed toward it.
- **R-N6**
  - before: The photographs of the building site are in the town hall.
  - after: The Poble shows photographs of the building site in the town hall.
- **R-N6, R-S18**
  - before: FIESTA, the ten-minute show, is in the brick tower on Plaza Aragonesa.
  - after: Fiesta, the ten-minute show, is in the brick tower on Plaza Aragonesa, the Poble says.
- **F-N16 (HOLD), L5**
  - before: The historians write that you come into this square through the porticoes of Sangüesa's town hall, from Navarre. Even the way in was borrowed.
  - after: The historians write that, on this side of the square, you come in through the porticoes of Sangüesa's town hall, from Navarre. If this arcade is the one they mean, even the way in was borrowed.
- **R-S21 (wording)**
  - before: Then they go further. Without the journey, they write, the Poble Espanyol
  - after: Then they go further. Without the journey, the Poble Espanyol

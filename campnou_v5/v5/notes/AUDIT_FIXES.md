# AUDIT FIXES: FC Barcelona Museum at Spotify Camp Nou EN, 14 Nov 2026

The fixer's log for `research/AUDIT_V5_FACTS.md` (**FA**: 2 MUST, 5 SHOULD, 16 NICE) and `research/AUDIT_V5_ROUTE_LISTENING.md` (**RL**: 2 MUST, 19 SHOULD, 19 NICE), with the lead's ten decisions applied.

**Scope**
- **Edited:**
  - `v5/tracks/001–034.perf.txt` (bodies, and @what where a fact changed: 004, 007, 008, 010, 011, 012, 020);
  - `v5/bridges/A–D.txt` (wording, and a `#` tag line above each bridge);
  - `v5/PLAN.md`: Conventions (the show line, the tag melody), §2 row 024's cue, §3's bridge text and table rows 008 H, 022 H, 024 E/H, ALT-O15 option 1, and §7 (lexicon rows);
  - `v5/ONSITE_CHECKLIST.txt`: an O11 play-through test, an O15 re-cue note, and the bridge tags line.
- **Not edited:** research files (see the FACTS 8.11 note below), `lint.py`, the lead's decision sections.
- **New facts: none.** Every change is a cut, a re-attribution, a re-ordering, or wording taken from the audits or from the lead's decisions.
- **One page re-read:** the club's Xavi/Rexach/Messi article, https://www.fcbarcelona.com/en/football/first-team/news/1846462/what-do-charly-rexach-xavi-and-messi-have-in-common, as relayed:
  - Messi "has featured in 17 consecutive seasons for the blaugranes", which "equals the run of Xavi Hernández between 1998 and 2015 and that of Charly Rexach from 1965 to 1981";
  - "Neither Xavi nor Rexach can boast of scoring in each of their seasons as a blaugrana";
  - the page does **not** say "club record", so the track doesn't either (FA M2).

**Result**
- `python3 v5/lint.py`: **all 34 tracks OK**, every one inside its type's range.
- **Bridge and cue check (script):**
  - all 10 bridges open "On this shorter tour,", and each ends on its destination's exact @title;
  - every cue in F, E and H ends on the next track's @title.
- **"the club's own"** as an attribution: 11 tracks before, **0 now**. The club is still credited, as "the club says", "the club's history pages" and so on.
- **Digit dates:** "the 22nd of October" and the like are now written in words everywhere (RL N2).
- **Lengths** (clean words at 125 wpm, plus PLAN §3's walking, the show at 10 min and the time looking; the method RL M1 uses):

  | Version | Words before | Words now | Cut | Visit before | **Visit now** | With rendered silences | Target (lead) |
  |---|---|---|---|---|---|---|---|
  | Full (34) | 9,562 | **8,732** | −830 | ≈ 102.1 | **≈ 95.5** | ≈ 99.7 | ≈ 95 |
  | Essential (18 + 5 bridges) | 5,340 (bridges 174) | **4,916** (bridges 173) | −424 | ≈ 65.4 | **≈ 62.0** | ≈ 64.4 | ≈ 61–62 |
  | Highlights (6 + 5 bridges) | 1,807 (bridges 169) | **1,763** (bridges 181) | −44 | ≈ 34.3 | **≈ 33.9** | ≈ 34.8 | ≈ 34–35 |

  - The silences column adds the pipeline's 0.75 s per paragraph gap, 0.55 s per [pause] and 2 s tail per track and bridge (RL N16).
  - Full is under 97, so **001's lengths line is unchanged**: "about an hour and a half, … about an hour, … about thirty-five minutes".
  - **Short of the lead's ≈ 900 / 450.** Full is cut by 830 words, not 900. E tracks are cut by 423 (5,166 → 4,743), plus 1 in the bridges, not 450. Going further meant losing whole stories (the 1999 final in 029, Iniesta in 015, the Porto friendly in 023). Several tracks are now at their type's floor (002 250, 012 250, 026 253, 023 254, 034 254 against 250; 024 183 against 180), so they can't lose more.
  - Highlights is ≈ 34 because its tracks lost only 56 words. The H bridges gained 12 words of navigation: "instead" twice, the European Cups' recognition line in 001 H, and "leave the room and follow the way on" in 024 H.
- **Over 10% of PLAN's aim** (all inside the lint range): 004 +11%, 005 +14%, 007 +12%, 013 +12%, 017 +17%, 020 +13%, 031 +18%. These are Full-only Extras or stories. The rest of each is a correction, an attribution, a quote or a "you" moment, none of which the lead lets me cut.

### Per track (clean words)

| # | In | Before | After | Δ | Aim |
|---|---|---|---|---|---|
| 001 | H E F | 340 | 329 | −11 | 300 |
| 002 | F | 291 | 250 | −41 | 260 |
| 003 | F | 245 | 198 | −47 | 190 |
| 004 | F | 333 | 289 | −44 | 260 |
| 005 | F | 215 | 182 | −33 | 160 |
| 006 | E F | 231 | 208 | −23 | 200 |
| 007 | F | 214 | 201 | −13 | 180 |
| 008 | H E F | 270 | 279 | +9 | 290 |
| 009 | E F | 305 | 271 | −34 | 270 |
| 010 | F | 268 | 257 | −11 | 250 |
| 011 | E F | 347 | 300 | −47 | 290 |
| 012 | E F | 257 | 250 | −7 | 250 |
| 013 | F | 319 | 292 | −27 | 260 |
| 014 | E F | 298 | 285 | −13 | 290 |
| 015 | E F | 320 | 282 | −38 | 270 |
| 016 | E F | 352 | 295 | −57 | 270 |
| 017 | F | 228 | 199 | −29 | 170 |
| 018 | F | 353 | 285 | −68 | 260 |
| 019 | F | 290 | 275 | −15 | 260 |
| 020 | F | 306 | 315 | +9 | 280 |
| 021 | E F | 269 | 264 | −5 | 250 |
| 022 | H E F | 279 | 262 | −17 | 280 |
| 023 | E F | 267 | 254 | −13 | 260 |
| 024 | H E F | 197 | 183 | −14 | 180 |
| 025 | F | 234 | 209 | −25 | 190 |
| 026 | E F | 288 | 253 | −35 | 260 |
| 027 | E F | 251 | 222 | −29 | 210 |
| 028 | H E F | 293 | 275 | −18 | 280 |
| 029 | E F | 343 | 277 | −66 | 260 |
| 030 | F | 299 | 275 | −24 | 250 |
| 031 | F | 330 | 296 | −34 | 250 |
| 032 | F | 185 | 185 | 0 | 170 |
| 033 | F | 286 | 281 | −5 | 260 |
| 034 | H E F | 259 | 254 | −5 | 260 |

---

## 1. Lead's decisions

| # | Decision | Before | After |
|---|---|---|---|
| 1 | Length (RL M1): keep all ten Extras, trim wording | 9,562 words, ≈ 102 min | 8,732 words, ≈ 95.5 min (table above). The audit's cut list was used first, then PLAN's optional items: Gol 1957 (002), the new rink (003), Wild's flat and his departure (004), Vinton (005), the 16 Super Cups (007), the 14 of 19 (009), Lisbon 2025 (011), Catalonia's coach (014), the farmhouse's future (015), the 1973 advert (016), Sant Pau (017), the 2025 centenary (018), Paris 2024 and the membership card (029), the spending rules (023), the September assembly (027), the penyes (027), Garcia Rius (031). No "you" moment, cue, safety line, attribution or correction of a popular error was cut. RL M1 step 2 (drop 005 and 017) was **not** done, by the lead's decision. Step 3 (001 says "an hour and three quarters") was not needed. |
| 2 | 024 reorder (RL M2) | Body: "Stop it when the show begins…". Cue: "Go in when the staff let you, and stop the guide now. When the show ends, press play again before you leave the room: …". Bridges: "now that the show is over" | Body: "Stop it before you go in, and start it again when the show ends." Cue: "When the show ends, press play again before you leave the room. Now go in when the staff let you, and stop the guide here: The round room · After the show: the first full house." **Build check:** `bcncat_v5/build/static/make_lengths.py` appends a bridge to the end of the track's own mp3 (track, 0.6 s silence, bridge, 1.5 s). It can't play a bridge as its own clip. So both bridges now open **"On this shorter tour, when the show is over, …"**, which is true whether they're heard at the door or after resuming. PLAN Conventions, §2 row 024 and §3 are updated to match. ONSITE O11 gets the play-through test. |
| 3 | 008 Koeman, then Alexanko (FA M1) | "Ninety minutes went by without a goal. Pep Guardiola was in midfield. The captain, Alexanko, came on for extra time, and still nothing. Then … Koeman hit it past the goalkeeper, Pagliuca, and the club had its first European Cup…" | "Ninety minutes went by without a goal, and most of extra time too. Pep Guardiola was in midfield that night. Then, with penalties not far off, Barça won a free kick. Ronald Koeman hit it past the goalkeeper, Pagliuca. Soon after, the captain, Alexanko, came on for Guardiola, and at the end it was Alexanko who lifted the cup. The club had its first European Cup, in its ninety-third year." No minute is spoken (G44; lint bans "112th"). |
| 4 | 010 Xavi (FA M2) | "By then he had scored in seventeen seasons in a row, a club record he shares with Charly Rexach and, later, Messi." | "By then he had played seventeen seasons in a row for the first team, the same run as Charly Rexach's. Messi later matched them both." The page re-read today has no "club record" wording, so none is spoken. "Later" is no longer ambiguous (RL N11). Also cut: "It was his last match for the club.", which the next line repeats. |
| 5 | 012 shirt (FA S4) | "For more than a century, nobody's name went across the front of Barça's shirt. No company, no logo, nothing." | "For more than a century, no sponsor's name went across the front of Barça's shirt." The UN's attributed "first time … that a logo had been featured" stays. Payoff: "A shirt kept clean for a century…" becomes "A shirt kept free of sponsors for a century, then lent to a charity, at the club's expense." |
| 6 | 004 founders (FA S1) | "They were Swiss, English, German and Catalan." | "They came from Switzerland, England, Germany, Catalonia and elsewhere in Spain." (No count of nations, AU §3.7.) |
| 7 | 011 (FA S2) | "fifty-one years after that Christmas match" | "fifty years after that Christmas match" |
| 8 | 020 Barau (FA S3) | "But he also says that the dressing-room story is one nobody has ever been able to prove." | "But another part of the story, a threat at half time, is one he says nobody has ever been able to prove." The Guardian writer's pre-kick-off visit stays as the players' account. |
| 9 | 007 counts (FA S5) | "…more than a hundred football trophies on display. Twenty-five of them came from the women's game. And about fifty more came from the club's other sports." | "…more than a hundred football trophies on display, twenty-five from the women's game, and about fifty from the club's other sports." |
| 10 | O3 route lines (RL R4) | 001: "Then in, to the trophies, the history, Messi's space, the round room and its show, the models, the viewpoint, and out." · 006: "From this hall, the trophies come first, then the club's history, then Messi's space, and finally the round room, where the exhibition ends." | 001: "First, a short stop outside. Then in, through the trophies, the club's history and Messi's space, to the round room and its show, then the models, the viewpoint, and out." · 006: "From this hall, the exhibition takes you through the trophies, the club's history and Messi's space, and ends in the round room." The club's official space list runs Trophies → Barça History → Messi Zone → 360° room (PLAN §1 route, OFF), so the list order is the club's. "Through …" fixes no sequence among the three. |
| — | No-quiet-corner fallback (RL R1) | ALT-O15 option 1 left 020's cue sending Full listeners from the benches back to Messi's space. 029's title and 018's "people in this museum" were wrong outdoors. | PLAN ALT-O15 option 1 now gives the replacements: (i) 016 keeps only its "Otherwise" sentence; (ii) 017–020 retitled "The old benches · Extra · …"; (iii) 029 "stay on the benches for eight more stories: The old benches · Extra · Backsides on a wall"; (iv) 020 → "Stay on the benches for the stadium's own name: The old benches · Extra · The stadium the nickname named." 018's last line is now place-neutral ("the club he said could not die is all around you"). ONSITE O15 says to apply (i)–(iv). |
| — | Repeated endings and double payoffs (028, 034; RL L3, L4) | See L3 and L4 below. | Done. |
| — | 91,553 and 91,648 (RL L7) | Both said in full, back to back | "more than ninety-one thousand people … Twenty-three days later, against Wolfsburg, even more came: ninety-one thousand, six hundred and forty-eight." The title's number is said once, in full. |

**Correction note for the lead: FACTS 8.11 (do not edit research files).**
- FACTS 8.11 says Xavi "played and scored in 17 consecutive seasons". **"Scored" is wrong.**
- The club's page (above) says: "Neither Xavi nor Rexach can boast of scoring in each of their seasons as a blaugrana." Only Messi did.
- Correct row: Xavi **featured in 17 consecutive seasons (1998–2015)**, equalling Charly Rexach's run (1965–1981), later matched by Messi. The club's page does not call it a club record.
- Translators and later writers should follow 010, not FACTS 8.11.

## 2. Facts audit (FA)

| ID | Track | What changed, or why not |
|---|---|---|
| M1 | 008 | Lead's decision 3 (above). |
| M2 | 010 | Lead's decision 4 (above). |
| S1 | 004 | Lead's decision 6. @what updated. |
| S2 | 011 | Lead's decision 7. |
| S3 | 020 | Lead's decision 8. @what notes where Barau's line belongs. |
| S4 | 012 | Lead's decision 5. @what updated. |
| S5 | 007 | Lead's decision 9. |
| N1 | 013 | "It was the first of twenty-six games without defeat, and that season they won the league…" |
| N2 | 015 | "The club's history says the boys in the farmhouse could see the stadium through their bedroom windows." Ending: "Most of the boys slept under a stand, a few steps from the pitch they wanted to play on." |
| N3 | 021 | "Rexach met the boy's agent, Horacio Gaggioli, and Josep Maria Minguella, who had helped bring him over…" and "The two men were his witnesses." |
| N4 | 029 | "He spoke some words in Catalan, to a stadium that was, the club's history pages say, exceptionally silent." |
| N5 | 032 | "In November 1974, the club turned seventy-five. On the twenty-seventh, to mark it, a new anthem…" |
| N6 | 020 | "…and only in 2019 did its board and its members' delegates vote to withdraw them." |
| N7 | 027 | "More than forty-eight thousand did, and Joan Laporta was re-elected." |
| N8 | 007 | "…the first league, the club says, that it had ever clinched against them." |
| N9 | 017 | "It began as a jibe, and the club admits it was meant as an insult." |
| N10 | 016 | No change (confirmed). |
| N11 | 028 | "for some months" |
| N12 | 004 | "He had placed the ad with a fellow Swiss, Walter Wild." |
| N13 | 030 | "And Mitjans, the club points out, was the president's cousin." (Not "the club's history pages", which the same track has just used.) |
| N14 | 002 | "…almost every place the licence then allowed." |
| N15 | 015 | Not done: +4 words for a claim that is already right. |
| N16 | 018 | No change (the track says only "That afternoon"). |

## 3. Route and listening audit (RL)

### MUST
| ID | Track | What changed |
|---|---|---|
| M1 | all | Lead's decision 1 (above). |
| M2 | 024, bridges | Lead's decision 2 (above). |

### SHOULD (route)
| ID | Track | What changed, or why not |
|---|---|---|
| R1 | PLAN ALT-O15, ONSITE O15, 018 | See §1. |
| R2 | bridge 024 H | "…when the show is over, leave the room and follow the way on to the viewpoint over the works, and find a place at the rail: The viewpoint · What you're looking at." |
| R3 | 034 | Cut "From here, follow the signs for the way out." The ALT-O7 line, if needed after O7, goes before the recap. |
| R4 | 001, 006 | Lead's decision 10 (above). |
| R5 | E | E ≈ 62.0 (from 65.4). 016 and 029 are now within 10% of their aims (+9%, +6%). |
| R6 | bridges | A `#` tag line above every bridge, e.g. `# 024 H>028 [O11, O4, ALT-O4]`. `make_lengths.py` reads only lines matching `NNN X>MMM:`, so `#` lines are never voiced. "instead" added to 008 H and 022 H (001 E/H had it already). No 027 E bridge, correctly (027's cue goes to 028). Decision 11's "027 E → 028 takes 026's old E bridge text" is left for the lead to strike: it is a lead's-decision section, which I don't edit. |
| R7 | 008, 014, 015, 016 | 008 "If the cups are labelled, find the one from 1992. That's Wembley, and every one beside it came after it." · 014 "If the Dream Team's photographs or shirts are here, look at them, then think of that ground…" · 015 "If the farmhouse is in the photographs here, find it…" · 016 "Now look at the crest on any shirt you can see, even one a visitor is wearing." |
| R8 | 019, 033 | 019 "…and there is no grave you can visit." · 033 "…nine days before the World Cup opened in the stadium in front of you. That was June 1982." |

### SHOULD (listening)
| ID | Track | What changed, or why not |
|---|---|---|
| L1a | 006 | "Since June 2023 it has been here. Over a million visitors came in 2025." (DATED kept as its own sentence.) |
| L1b | 028 | "The two lower tiers in front of you are the 1957 bowl, kept and renovated. Above them is the rebuilt third tier: built, but not yet open to fans." The 105,000 is folded into the Montjuïc paragraph: "When they come back for good, the club expects it to hold about a hundred and five thousand." 026's sentences stay as the home. |
| L1c | 001 | "…from a classified ad in a newspaper to the women's team." |
| L1d | 024 | Cut "And this is where the exhibition itself comes to an end." |
| L2a | 031 | "What he did do was fill Les Corts, the old ground, to bursting." |
| L2b | 026 | "…inspired by the canopy the original architects designed for the stadium of 1957." 030 is the architects' home. |
| L2c | 002 | Cut the 62,000 sentence (028 keeps it). "In March 2026 the Gol Nord, the stand behind one goal, opened again." |
| L2d | 018 | "Gamper had been the club's president five times." |
| L2e | 005, 017 | 005's Vinton sentence cut. 017: "A writer, Roger Vinton, searched…" |
| L2f | 006 | "…in a space under the main stand." · "It kept growing, to almost four times its first size by 2010." |
| L2g | 013 | Kept Asensi. Cut Cruyff's Dutch-TV line (L10). |
| L3 | 010, 028, 031, 034, 022, 029 | 010: "…the club's fifth European Cup." · 028 opens "The team has been playing here again since November 2025, and the builders never left." (the hook sentence is gone; the payoff stays) · 031: cut "It wasn't built for him." · 034: cut "And every time, it has found its way back." · 022: cut "Two great clubs, level on gold." · 029 (NICE): cut its closing "It has always been the city's stage…" |
| L4 | 017/018, 026/028/030, 006, 004 | 018 ends "[pause] The dictatorship that closed it is long gone, and so is the founder. But the club he said could not die is all around you." (place-neutral, for ALT-O15). 026 ends on the model's three things. 030 ends "Now look at the stadium in front of you, and say its name. The nickname won." 006 ends "[wry] For now, the museum you're standing in is a visitor here too." **004, partly:** its "you" moment is kept (the lead bars cutting one) but folded into PLAN's Ending, so it is no longer a second motto and no longer says "where you come from" (032's idea): "So it was a club named for its city, by men from somewhere else, like a good many of the visitors around you today." |
| L5 | 004, 006, 020 | 004 and 006 as L4. **020's "eleven–one … which city they're from" is kept**: it is the track's only "you" moment (the audit marks it NICE if kept). |
| L6 | 003, 016, 029 cues; 030 | 003 "Stay by the door for two short stories, here or in the queue if there is one: …" · 016 "…away from the screens, for four short stories: …" · 029 "…stay on the benches for four more stories: …" · 030: the hook comes first, then "You won't need to look at anything until the end." This drops "if there's room" and doesn't open with a command (it also covers N7). |
| L7 | 002, 011, 022, 027, 019, 007 | 002 "More than forty-five thousand people…" · 011: Lisbon cut, crowds as §1 · 022 "Six hundred and seventy-two goals for this club: more than Pelé scored for Santos, and the most anyone has scored for one club." · 027: penyes sentence cut · 019 "For more than a year, its board called him the absent president." (The audit's "for the rest of the war" would overstate: late 1937 to early 1939 ends before the war did.) · 007: Super Cups cut. |
| L8 | 019, 033 | 019 "[quietly] Three weeks into the Spanish Civil War, on the sixth of August 1936, the president…" · 033 opens "Barça signed Diego Maradona…" (R8). 016 is optional and was not done. |
| L9 | 004, 008, 012, 013, 015, 018, 028 | 004 "gives the reason:" · 008 "The goalposts, the club adds, were square…" and "One detail survives from the dressing room. Moments before the players went out, the club's history says, …" · 012: cut "And here's the turn." · 013 "Jordi Cruyff has told it himself:" ("tells" trips the dead-person lint on "Cruyff") · 015 as FA N2 · 018: four club attributions down to three, "the club's own" gone · 028 "The club's treasurer said, in Catalan, that…". **Kept:** 028's "[amused] Here's the part nobody planned for." (the audit lists it but gives no fix; it is the track's light beat). |
| L10 | 013, 011, 028 | 013: Cruyff's "people were saying thank you" cut · 011 "Between them, Alexia and Aitana won the Ballon d'Or five times as Barça players. In 2026, Alexia won her third." · 028 "Now look up to the very top…" and "Its last piece was fitted in October 2026." |
| L11 | 029, 014 | 029 "That November, the stadium held something else entirely." · 014 opens "[warmly] In 1988, Johan Cruyff came back, this time as coach. He had been a star here as a player in the 1970s." |

### NICE
| ID | What changed, or why not |
|---|---|
| N1 | 008's cue: "Stay at the European Cups for the next two, from Paris and from Rome." 022's cue was kept, because Full needs its pointer to 023. |
| N2 | Every "the 22nd of …" style date is now in words (004, 008, 013, 016, 018–021, 023, 025, 031; 033's date is gone). Zero words. |
| N3 | 020 "…It was eight–nil at half time, and Barcelona finished with ten men." |
| N4 | 022: the Rosario line is joined to the hook paragraph. |
| N5 | 015: cut "And remember where most of them really lived." |
| N6 | PLAN Conventions' tag melody now lists [quietly] for the Pope (029). |
| N7 | 030, as L6. |
| N8 | Not done (+5 words). FCB/CFB is on the render test (PLAN §7). |
| N9 | 020 "a Madrid paper called Ya". |
| N10 | Render test noted in PLAN §7. "Carrer Princesa" is cut. |
| N11 | 010, as lead's decision 4. |
| N12 | No change needed. |
| N13 | 033 "The Bernabéu would do it again, in November 2005, when Barça won three–nil there." (Clearer than "it happened again".) |
| N14 | 024: cut "two storeys high", which is not in PLAN's row or in FACTS. 007: as FA N8. 015: as FA N2. The rest were confirmed by FA. |
| N15 | 016: the quote now ends at "football club." The paraphrase after it is cut too. |
| N16 | Reported here (Result). PLAN §3 itself is not changed. |
| N17 | No change. |
| N18 | Audit §6's names added to PLAN §7, except the names whose lines were cut (Garcia Rius, Fermín López/Eric Garcia/Cubarsí, Carrer Princesa). |
| N19 | 015 now says "the stand behind one goal", as 002 does. |

## 4. Other changes made while cutting
- 016: "That is her reading." replaces "Those are her words, and her reading of it." The attribution to Elena Fort stays.
- 018: "[quietly] In 1930, Gamper took his own life. It was probably, the same history says, because of his business problems, and the forced closure of the club he loved." This is the club's own reason, nearer its wording ("the forced closure").
- 025: opens "[warmly] The first time the Camp Nou filled up was on its opening day…". This drops the repeat of 024's "puts you at the centre of the stadium", and Eulogio's five-goal sentence is cut.
- 034: "Now the team is back home, in a stadium still being finished." and "[lightly] As you heard at the start, it has packed up and moved house, again and again." These keep the close at 254 (CLOSE floor 250) after R3 and L3. "As you heard at the start" is PLAN's one allowed callback to 001.
- 006: "[pause] The club itself was founded in 1899, by a young Swiss called Joan Gamper." This is PLAN's version-neutral sentence.
- 029: "[warmly] These benches came out of the old stadium, and the club put them here for visitors. So, if there's room, you're sitting where its legendary players sat."
- PLAN §2 rows other than 024 still carry their old cue texts. **The tracks are the reference for ES, FR and DE.**

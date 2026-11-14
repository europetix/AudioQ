# AUDIT FIXES: Barcelona Cathedral EN, 14 Nov 2026

The fixer's log for `research/AUDIT_V5_FACTS.md` (**FA**: 2 MUST, 13 SHOULD, 21 NICE) and `research/AUDIT_V5_ROUTE_LISTENING.md` (**RL**: 4 MUST, 22 SHOULD, 20 NICE), with the lead's decisions applied.

**Scope**
- **Edited:** `v5/tracks/001–036.perf.txt`, `v5/bridges/*.txt`, `v5/ONSITE_CHECKLIST.txt` (cut rules and new tests, RL R8), PLAN §2 row 013's title (RL N1), `build/static/pronunciation.py` (two lexicon entries), `build/static/README.txt`, both launchers, and `build/route_map.py` (lengths and the Jewish-memory note).
- **Not committed.**
- **No new facts were added.** Every change is a cut, a re-attribution, a re-ordering or a wording taken from the audits. Where a wording is my own, it was checked against the audit's quoted source.
- **No pages were re-fetched.** The audits' quotes, as relayed, were enough for every change.

**Result**
- `python3 v5/lint.py`: all 36 tracks OK and inside their word ranges.
- `bash bcncat_v5/build/build_all.sh`: OK. The route map has 5 pages and every stop is placed; the bridges in the bundle carry no brackets.
- **Lengths** (clean words at 125 wpm, PLAN §3 walking, a 5-minute lift wait):

  | Version | Words | Visit | Before | With rendered silences |
  |---|---|---|---|---|
  | Full | 9,833 | ≈ 94 min | 10,162 words, ≈ 97 min | ≈ 98 min |
  | Essential | 5,633 | ≈ 60 min | | |
  | Highlights | 3,094 | ≈ 31 min | | |

  - Essential and Highlights include their bridges.
  - 001 now says: "With walking, the full tour takes about an hour and a half, a little more with a wait for the lift. The essential takes about an hour, and the highlights about half an hour."
  - The README, both launchers and the route map say "about 1 h 35", with "a short wait for the roof lift; a long queue adds more".

---

## 1. Lead's decisions

| Decision | Before | After |
|---|---|---|
| 021 (FA M1, RL L7) | "…were two girls or one story. Barcelona has never had any doubt." | The sentence is **cut**. The paragraph ends on "two girls or one story", and the next one opens "What the record does show is devotion." |
| 026 (FA M2) | "…the count and countess consecrated their new cathedral, here, on this site." | "Soon after, in November 1058, their new cathedral was consecrated, here, on this site." |
| Facing, bridges 022 H/E (RL M1) | "climb back up, and cross in front of the high altar to the white marble doorway into the cloister, in the bay on the right. Go through, and turn to the small vaulted pavilion over a fountain, close to the door" | "On this shorter tour, at the top of the crypt stair, face the high altar. Cross to the white marble cloister doorway, in the bay on the right as you face it. Go through to the small vaulted pavilion over a fountain, by the door: …" [O2, O9, O10] (45 words) |
| Facing, 023's cue (RL M1, N5) | "Climb back up. Walk round the left side of the high altar into the walkway behind it." | "If you went down, climb back up to the top of the stair. Turn to face the high altar, and walk round its left side, as you face it, into the walkway behind it." @where gains [O17]. |
| Facing, the other cues after the crypt | 025: "Carry on round to the right side of the high altar." · 026: "…in the bay beside the altar." · 027 @where: "in the bay on the right of the high altar" | 025: "…to the right side of the high altar, as you face it." · 026: "…in the bay on the right as you face the high altar." · 027 @where: "…as you face it". |
| Facing, consistency | — | Every left/right after the crypt now has the lift on the left and the cloister door on the right as you face the high altar. 012-023's header comment states the rule. |
| 013 (RL M2) | "When it's your turn, ride up. On the roof, follow the walkway…" | "If you're still in the queue, ride up when it's your turn. If you're already on the roof, or once you get there, follow the walkway until the lantern tower over the main door is in front of you: …" |
| Roof, 015 neighbours (RL M3) | The seven names, then "From where you stand, some of them may hide behind their neighbours' roofs. So pick out the towers and the roof lines the view gives you, and let the rest be a list of who lives next door." | The list stays, framed as the cathedral's neighbours "within a few streets". One summary sentence is added: "Bishops, kings, the city and the government, all packed round one corner." The unverified look becomes **one cuttable sentence**: "From where you stand, you may pick out a tower or a roof line of one or two of them." "The Palau Reial Major" is now "the old royal palace". |
| Roof, 015 horizon (RL M3, N18) | "And if the day is clear, look far off on the horizon for the spires of the other great church in this city, the one people so often mistake this one for." (32 words) | **One cuttable sentence:** "On a clear day, look far off on the horizon for the spires of the other great church in this city, the one people so often take this cathedral for." (30 words) |
| Roof, 014 and 013 gargoyles (RL M3, FA S13) | 014: "Look for the beasts among them." · 013: "And among the monsters, it says, there's a bull, a unicorn and an elephant." | **Kept**, each as one separate cuttable sentence that nothing else depends on. 014, 015 and 013 each name their cuttable sentence(s) in the [O7] bracket of @where. ONSITE O7 gains "UNTICKED = CUT". |
| Jewish memory (RL M4) | 032 cue: "If you're on the full tour, look for the room called Jewish memory, in the old archive: …" · 033 @where: "PLACEMENT PENDING, how visitors reach it is unknown." · 033 @room: "(G102: …)" | 032 cue: "If you're on the full tour, and the room called Jewish memory is open and signposted, look for it: The cloister · Extra · Jewish memory. Otherwise, the next main stop is the Chapter Hall museum…". 032 @where: [O6: …open and signposted…]. 033 @where: "its location must be confirmed on site, and it is not assumed to open off the cloister" [O6: G102 …]. 033 @room: "its place to be confirmed on site". Route map note: "An Extra, only if the room is open and signposted; where it is reached from is still to be confirmed." ONSITE O6 gains the cloister-reach test. 033 stays a Full-only Extra. |
| Length (RL R5) | 001: "The full tour takes about an hour and a half, the essential about an hour, the highlights about half an hour, walking included, plus any wait for the lift to the roof." | See Result above. Static files: "about 1 h 30" becomes "about 1 h 35" in README.txt, generate_audio.command, generate_audio_ES_FR_DE.command and route_map.py. The wait line becomes "Times include walking and a short lift wait; a long queue adds more." The map's "The times on page 1 don't include the wait." becomes "…allow for a short wait; a long queue adds more." |
| Bridge tags (RL R6) | [O#] inside the spoken line (001 H, 002 E, 004 H/E, 006 H); 012-023 tags only in a header; 024-036 untagged | Every bridge line ends `…: <place> · <title>. [O#…]`. The build strips the tags; `bundle/…/bridges/en.txt` contains no brackets. 024-036 gains its tags: 030 → [O20, O21, ALT-K9]; 034 → [O1, O23]. |
| Thin attributions and payoffs | See L3, L8, L1c below. | "The cathedral" as a source is now used in 12 tracks: 007, 010, 014, 015, 018, 024, 025, 027, 028, 029, 030, 033 (cap 12). "plainly" and "in one line" are gone from the speech. |

## 2. Facts audit (FA)

| ID | Before | After / why not |
|---|---|---|
| M1 | 021 "Barcelona has never had any doubt." | Cut (lead). |
| M2 | 026 "the count and countess consecrated" | Passive (lead). |
| S1 | 018 "…treasurers: the knights paid for their own coats of arms." | "…treasurers. The order paid for its own coats of arms." |
| S2 | 034 "This is his last known work." | "This is his last known painting." (The 1495 window in 010 was his design, not his painting.) |
| S3 | 009 "Then he went to Carrara, in Italy, for more marble." | "Then he left for Carrara, in Italy, the marble town." @listen updated to match. |
| S4 | 011 "Carbonell also worked for the knights of the Golden Fleece, in the choir." | "A joiner of the same name, Antoni Carbonell, had worked on the choir for the knights of the Golden Fleece." |
| S5 | 024 "beside the arms of Barcelona" | "beside the royal arms" |
| S6 | 025 "…pulled down… By then the convent was all but abandoned, and so his tomb was moved here that year." | "…a great fire damaged the convent, and it was left all but abandoned. His tomb was brought here. Soon afterwards the convent was pulled down, and explosives were used to bring down its church's vault." |
| S7 | 029 "This cathedral was the first place in Barcelona to present the dancing egg" | "The cathedral says it was the first place in Barcelona…" |
| S8 | 033 "Until 1969 this was the chapter's archive. It holds about forty thousand parchments" | "Until 1969 this room held the chapter's archive. The archive itself, now kept elsewhere, holds about forty thousand parchments…". The audit's "kept elsewhere in the cathedral" was not used: no source here says where. |
| S9 | 023 "The best story, the cathedral says, is carved on the back." | "The best story is carved on the back." The judgement is ours, and the legend keeps "the story goes". |
| S10 | 004 "A University of Barcelona exhibition put it plainly:" | "A University of Barcelona report gives the reason:" (also RL L3) |
| S11 | 026 "…shown an old tomb here." | "…shown an old tomb in this cathedral." |
| S12 | 026 "al-Bakri, says" | "al-Bakri, wrote that" |
| S13 | 013 gargoyle animals | Kept, attributed and cuttable on O7 (lead's M3); the rule is in @where and ONSITE O7. |
| N1 | 001 "worshipped… for seventeen centuries" | Not changed: the audit grades it OK. |
| N2 | 003 "built from the 12th century" | "built around the 12th century" (speech and @what) |
| N3 | 004 "Carlí's visit" | "Carlí's drawing" (also RL N6) |
| N4 | 004 title "built in 1887" | Not changed. The title is fixed in PLAN, in two cues and in the bridges, and the speech already gives 1887–1890. |
| N5 | 005 "had a hand in the drawing too" | Not changed. The audit grades it OK, PLAN F5.8 is HEDGE, and a further COAC attribution would add to the attribution count. |
| N6 | 010 "six men Columbus brought back" | "six people Columbus brought back from the Caribbean". The plaque paragraph's O14 cut rule is now in @where. |
| N7 | 011 "Gabriel Blancafort restored it" | "The organ above was first built around 1540… Gabriel Blancafort rebuilt it inside its old case in the 1980s and 1990s" (GEC: built "a partir de la façana i la caixa originals"). |
| N8 | 013 betevé, 1606 | No change: attributed, as PLAN requires. |
| N9 | 014 "two tall Gothic pinnacles" | "two tall pinnacles" |
| N10 | 016 "to choose the wood himself" | "sent to buy the wood himself" |
| N11 | 018 "those of distant kings" | Kept (lead's decision 5). |
| N12 | 020 "carried on alone" | "carried on" |
| N13 | 021 "he attacks her" | "he threatens her" |
| N14 | 021 "You saw that cross on the choir screen" | Cut. The sentence is now "You'll find that cross in images of her all over this cathedral." @where and O24 say "…the choir screen among them" may go back only if O24 finds the cross on a panel. |
| N15 | 024 the crypt in the first-phase list, under Ponç de Gualba | The list now ends at "the sanctuary of the high altar". 024's opener hedges the crypt: "is thought to be the work of Jaume Fabre". |
| N16 | 027 | OK; one clause added for RL N6 (see below). |
| N17 | 031 "calls them a great Bible of the poor in stone" | "A study of the cloister reports that they have been read as a great Bible of the poor in stone, a picture Bible promoted by Bishop Sapera." (merged with the RL R5 cut of "A picture Bible, perhaps…") |
| N18 | 033 "after Almanzor's army burned the city" | The sentence is cut (RL R5). |
| N19 | 034 signature spelling | Still O21. The speech is now in lower case (RL L6), and the lexicon says "Vermejo" in both spellings. |
| N20 | 035 Corpus 1320 in our voice | "Barcelona was, the same encyclopedia adds, one of the first cities…". "A ruby" is not affected: that line was cut (RL R5). |
| N21 | 036 Pont del Bisbe | Kept. The O23 cut rule is now in 036's @where and in ONSITE O23. |

## 3. Route and listening audit (RL)

### MUST

M1–M4: see §1.
- ONSITE O10 gains the facing test for the crypt stair.
- ONSITE O7 gains "unticked = cut".
- ONSITE O6 gains the reach-from-the-cloister test.

### SHOULD: route

| ID | Before | After |
|---|---|---|
| R1 | 026 cue "Stop there, turn round, and look back at the choir." · 027 @room "looking back at the choir" · 027 "The choir in front of you" · "Look back at the choir once more" | 026: "Stop beside it, out of the way, and look across at the choir, the enclosure in the middle of the nave". 027 @room: "…the choir in view". 027 @where: "…with the choir in view across the church". 027: "The choir you can see from here…" and "Look across at the choir once more…". ONSITE O19 gains the test. |
| R2 | 007 and 008 "the marble screen… the wooden enclosure"; 015 "the wooden enclosure… and in at its entrance"; bridges 006 H and 015 E "wooden enclosure"; 016 @where "wooden" | 007 and 008: "the white marble screen at the end of the choir, the enclosure in the middle of the nave". 015: "the enclosure in the middle of the nave, and go in at its entrance". Bridge 006 H: "the enclosure in the middle behind the white marble screen". Bridge 015 E: "the enclosure in the middle of the nave". 016 @where: "wooden" dropped. ONSITE O8 gains the outer-wall question. |
| R3 | 024 cue "…reading the names beside them, to the tomb of Sant Ramon de Penyafort" | "…and look for a sign naming Sant Ramon de Penyafort. If you can't find one, stop anywhere along the walkway: …". 025's look: "If a sign beside a chapel names him, find his tomb there." 025 @where gains the fallback. ONSITE O17 gains the test. |
| R4 | 030 "Walk on to the cloister's door to the street… Stand near it" | "Walk on to the cloister's street door with a Pietà carved above it, the Pietat door. Don't go out. Stand inside, near it, …". ONSITE O9 gains the test. |
| R5 | Full ≈ 97 | Cut: 024's opener and its 2024 windows line; 028's garden and bell-tower lines; 032's fair; 033's Call's edge and the Almanzor sentence; 035's sapphire and ruby; 025's lawyers and feast day; 031's "A picture Bible, perhaps…" (merged); the three foreign sentences (L5); 011's workshop line and payoff; 012's clock; 014's towers and cloister. Full is now ≈ 94 (−329 words). 015's list was **not** cut (lead's decision): the look on it is cuttable instead. |
| R6 | Tags in spoken bridge text | See §1. |
| R7 | 009 @where without [O11]; 010 "Walk up the left-hand aisle"; 025 and 027 "right" without "as you face it" | 009 @where: [O24, O2, O11, O14]. 010: "Walk up this left-hand aisle, as you face the high altar, …", with @where [O18]. 025 and 027: see §1. |
| R8 | Cut rules only in the writers' notes | Each rule is now in its track's @where bracket and in ONSITE: 008 Sança (O4), 010 plaque (O14), 015 horizon and neighbours (O7), 014 and 013 beasts (O7), 036 bridge (O23). The missing tests are added to O6, O7, O8, O9, O10, O17, O19, O23 and O24. |
| R9 | 001 hat line missing; 016 never says "don't lift" | 001: "Inside, keep your voice low, and take your hat off." 016: "…find a seat whose folding ledge is already raised, and look at the carving underneath. Please don't lift one yourself: …" |

### SHOULD: listening

| ID | Before | After |
|---|---|---|
| L1a | "thirteen" ×5 in E | 022: "She was Eulàlia: by tradition a young girl martyred in 304, and Barcelona's own saint." H keeps "the girl of thirteen in the legend" in 030. 030 drops "Barcelona's own saint". 036: "…on the feast of Santa Eulàlia, the city's martyr saint." |
| L1b | 015 "where the bishops never moved" | "on the corner of the Roman town where you began" |
| L1c | 004 "The plans came first, by almost five centuries." · 006 payoff "A stopgap roof that lasted five centuries…" | 004: "The plans are far older than the stone." 006: the payoff is cut, and the track ends on "Pick one out above you, and look for the colour." |
| L1d | 006 "For a century and a half they built around the Mass." | Cut. |
| L1e | 014 re-tells the towers | "There are the two eight-sided bell towers you heard about at the lift." (012 is in E and F.) |
| L1f | 014 "And down below lies the cloister…" | Cut (015 is its home). |
| L1g | "own saint" ×4 | 030 and 036 drop it; 001 and 022 keep it. |
| L1h | 036 opens and closes on seventeen centuries | See L13. |
| L2a | 008 "This is the alabaster people confuse… Hers… is marble." | "Remember this alabaster when you reach Santa Eulàlia's tomb in the crypt." |
| L2b | 024 "The first builders started here, at the far end…" | "It's the end you heard about at the main door, where the building began." |
| L2c | Fabre twice; "his finest work" as fact | 024's opener: "The crypt you've just left is thought to be the work of Jaume Fabre. In 1317 the cathedral hired him from Mallorca… He was made master of the works for the rest of his life. Historians still ask whether he kept an earlier design, or reworked it." |
| L2d | 016 re-tells 008 | "You've met his work already: the alabaster figure of the bishop under the Lepanto crucifix." ("figure" keeps the lint's alabaster rule.) |
| L2e | 031 "The original… is in the cathedral's museum" | "The original relief, the Catalan encyclopedia says, is kept indoors by the cathedral, so the one above the door may be a copy." "Wooden" is not used: the source doesn't say it. |
| L3 | Attribution tics | 004 and 005: "plainly" gone (005: "The University of Barcelona calls it a project 'drafted by Antoni Gaudí'."). 021: "The same pages answer it:" and "Experts, they add, see…". 030: "…there is a fact, and the cathedral gives it too:" and "They get daily cleaning…". 011: "the same paper says" cut, and the workshop line cut. 022: "as the cathedral describes the scene" cut. 023: see FA S9. 016, 026 and 027: "in one line" gone. |
| L4 | Signposts and "older than" | 011: "Then the turn." cut (005 keeps the only one). 007: "Then the bigger surprise." and "The room itself is older than the legend." cut; "Arnau Bargués built this room in 1407…". 021: "Now the harder question." cut. 022: "Many books call this tomb alabaster. It's marble: …". 029: "Here's the date everyone gets wrong: 1448. It's often given for the cathedral, but it belongs to the cloister." 012: "The oldest bell in the towers was cast in 1321: …". 028: "This doorway may have outlived the church it was made for." "Older than" is down from 10 to 7 in the speech. |
| L5 | Spanish and Catalan sentences | 026: "In the words of the city's history museum, the building of the Gothic cathedral meant the destruction of the Romanesque one." 027: "The cathedral's record ends the story simply: in the spring of 1939, the archive came back to the cathedral." 029: "In April 1456 the Generalitat's diary noted that a public proclamation had been made through the city: Saint George's day was to be a holiday." The originals stay in @sources. |
| L6 | Misreadings | 007: "Hanss" (with a lexicon entry). 021: "Saint Eulàlia" inside the quote (an abbreviation spelt out; the words are unchanged). 034: "Opus Bartolomei Vermejo Cordubensis" (with a lexicon entry). 016: "cadirat" dropped. 011: "carasses" becomes "these carved heads" and "the heads". "Call" was already in the lexicon ("Kahl"). The listening checks in ONSITE are updated. |
| L7 | 021 | See FA M1 and N14. "crucified, naked," becomes "crucified". |
| L8 | 011 [warmly] payoff after "racism" | Cut. |
| L9 | Too many looks | 014: towers and cloister cut (L1e, L1f). 022: the eight columns cut, and the inscription is now "if you're near enough to read it". 021 (NICE): "Look down the stair: the tomb below is hers." |
| L10 | 016 and 024 openers | 016: "These seats began with a journey to Flanders. The chapter's old choir book records it, in old Catalan: …". 024: see L2c. |
| L11 | 022 the party twice; "Who was she?" | "In July 1339 two kings came down these steps, and they came for a saint." "Who was she?" is gone (L1a). |
| L12 | 008 "If you can see in from the doorway, his tomb is Baroque." | "If you can see in from the doorway, look for his tomb. It's Baroque, and on it lies something older: …" |
| L13 | 036 | The first sentence is cut. "Thank you for walking it with me" becomes "Thank you for taking this walk with me" ("walking this corner" would have repeated "the Roman corner" in the same breath). The cut took 036 below 250 words, so one recap sentence from 001 was added: "The cathedral still carries both its names: the Holy Cross, and Santa Eulàlia." 036 is now 253 words. **If O23 cuts the bridge sentence (−15), 036 needs about 10 words back** (this is noted in ONSITE O23). |

### NICE

| ID | Action |
|---|---|
| N1 | PLAN §2 rows 012 and 013 now say "Lightning and firecrackers". |
| N2 | 025 and 033: the placement notes moved into the tag brackets or out; 033 @room is cleaned. |
| N3 | 009: "…beside the main door, the baptistery: The baptistery · Baptised here." 002: "Turn now to the old stone house built into the Roman wall beside the cathedral, the Casa de l'Ardiaca: …" |
| N4 | 012: "If you're here at noon" is cut ("At noon the Angelus is rung on one of the big bells, la Tomasa."). 013: "The roof walk reopened in 2024", "On the roof you'll also be…", "for the cloister". |
| N5 | 023: fixed (M1). 019: "At the choir's entrance stands a wooden pulpit. Stand beside it, and look up at the spires…". 016's Extra cue is not prefixed: ALT-M accepts it. |
| N6 | 004 ("drawing"); 012 (no "older than the crypt"); 024 (hedged); 002: "Then came Almanzor." 027: "It is back in its chapel today." (O11, 2026, places the tomb under the crucifix.) 033: "converted… or fled" matches G104, so there is no change. |
| N7 | 019: "twenty years on". 025: "more than three centuries after his death". |
| N8 | 003: "in the Chapter Hall museum". 010: "the Pietà you'll see in the Chapter Hall museum". 007 keeps its "at the end of the tour" (the doubles rule). |
| N9 | Not changed. PLAN's tag melody undercounts [quietly], but the audit finds the tone right everywhere, so the tracks stay. |
| N10 | Not changed: PLAN sanctions the route line. |
| N11 | 024's 2024 windows line is cut. 013's "reopened in 2024" stays (DATED list). |
| N12 | 034's cue: "on its silver seat". |
| N13 | Added to ONSITE O9. |
| N14 | 036: "Here in the cloister, the thirteen geese…". The step-free line is kept (lead's call). |
| N15 | Bridge 002 E: "On this shorter tour, turn instead to the front of the cathedral…". Bridge 012 E: "On this shorter tour, the next stop is on the roof. If you're still waiting, ride up when it's your turn. Once up there, follow the walkway…". |
| N16 | No action (the pipeline adds the silences; the lengths above give the "with silences" figure). |
| N17 | 033's "about a hundred documents" is cut. 036's "four hundred years" is kept (an allowed callback). |
| N18 | 001's 32-word sentence is split. 015's horizon sentence is 30 words. |
| N19 | 010: the font joined to the window paragraph ("This chapel is the baptistery, and its font is from the 15th century."). |
| N20 | 020: "A German woodcarver made Barcelona his home for the rest of his life." |

## 4. Metadata

- Each track with a cut or a re-wording now ends its `@what` with an "Audit fixes, 14 Nov 2026: …" note, so translators don't script a cut line from @what.
- The research rows in @what and @sources are otherwise unchanged. The removed foreign-language originals stay in @sources.

## 5. For the lead

- **036 and O23.** 036 is at 253 words. If O23 cuts the Pont del Bisbe sentences, the track needs about 10 words back.
- **015 and O7.** 015 keeps the seven neighbours as a list (lead's decision). After O7, rewrite the cuttable look sentence to name only the ticked neighbours, each with a way to find it.
- **Route map.** It still draws 033's dot in the cloister, as a schematic position. Its note now says the room is visited only if it is open and signposted, and that its access is still to be confirmed.
- **024's opener.** It now hedges the crypt as "thought to be the work of Jaume Fabre", to match 022's "thought the finest work".

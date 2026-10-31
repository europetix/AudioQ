# AUDIT FIXES: tracks 001–029 and bridges, 31 Oct 2026

Inputs: research/AUDIT_V5_FACTS.md ("F-") and research/AUDIT_V5_ROUTE_LISTENING.md ("R-"), plus the lead's seven decisions.
Lint: `python3 v5/lint.py` prints OK for all 29 after the edits. Cue chain: every last paragraph ends with the next main stop's @title (with "·" for "—" and the quotation marks dropped), and every bridge names its target's title. Checked by script.
Words after the edits: 001 358 · 002 358 · 003 239 · 004 349 · 005 268 · 006 221 · 007 336 · 008 317 · 009 335 · 010 285 · 011 265 · 012 306 · 013 335 · 014 176 · 015 359 · 016 249 · 017 354 · 018 311 · 019 345 · 020 201 · 021 250 · 022 317 · 023 276 · 024 227 · 025 359 · 026 360 · 027 359 · 028 201 · 029 323. **026 is at its 360 cap; 015, 025 and 027 are 1 word under it.**
Bridges: 30–45 words each, not counting "·".
No new facts were added beyond what the auditors verified (Irish Times "two Lichtensteins and a Warhol"; Pollack film; Giménez; Arzak; the fire's evening hour and short bursts) or what FACTS holds (A37: fish lamps 1984). @sources lines were updated where an attribution changed (002, 003, 005, 007, 011, 013, 017, 024).

Counts (83 findings: facts 3 MUST / 12 SHOULD / 20 NICE; route 6 / 22 / 20): **fixed 72 · partly fixed 3 (F-S9, R-M1, R-N6) · overridden by the lead 2 (F-S2, F-S12) · not done 6 (F-N4, F-N16, R-N2, R-N7, R-N18, R-N19)**, plus the R §7 pronunciation table (pipeline). Every MUST and SHOULD is fixed, partly fixed or overridden by a lead decision.

## Lead's decisions
1. **001 times.** Kept "about an hour and forty minutes" (it overrides F-S2 and R-M1). The 29-word sentence is split in two. **PLAN §3 and the Targets table still say "about an hour and a half": update PLAN to match.**
2. **TTS.** Done:
   - "fifty-five metres" (007);
   - "F, O, G" (023);
   - "the 1970 world's fair in Osaka" (023);
   - "Advice to Space Five" and "Embrace Eleven" (015; the numerals stay in @what only);
   - "LED" (008, 027);
   - no "#" anywhere in speech (grep clean).
3. **Extras.** 013, 019, 023 and 027 now say "If you're on the full tour, there's a short Extra…".
4. **021.** Directions now come in paragraph 2, version-neutral. A plaza exit takes the stairs (the PLAN line, tagged [O12]); a river-side exit is "nearly there". The last paragraph says: walk along the river toward the big road bridge to the pond [O13]. 019 and 020 cues now say "play it as you go. It tells you the way to the river walk".
5. **011.** Rewritten (F-M1).
6. **Quotes.** Fixed: 002 Agirre and AGNSW; 005 Pérez; 007 Foster; 013 Giménez; 017 Arzak and the joints line; 025 Bourgeois splice; 023 Nakaya; 019 Gehry order.
7. **Bridges.** All rewritten except 007 E/H>009 and 010 E>013, which still fit their track endings.

## Fact audit (F-)
| ID | Track | Status | Before → after |
|---|---|---|---|
| M1 | 011 | fixed | "For eight years, this long gallery held just one work… it stood here alone… For eight years it was the only one." → "For eight years, Snake was the only part of The Matter of Time in this room. The rest was still to come." / "…for the museum's opening. It didn't have the gallery to itself, though. At the opening it shared the room with other works, among them two Lichtensteins and a Warhol, as an Irish critic noted. The other seven Serras came later…" / "It was the first. Everything else in this installation came after it." @listen and @sources (IRISH97-OPEN) updated. **Title kept** ("Snake waited eight years" is still true: it waited for its seven companions). Retitling would change PLAN's @title and 010's cue. Lead's call. |
| M2 | 005 | fixed | "He also called the project 'financially incredibly costly'. Both things, it seems, were true." → "He also admitted that just reaching the building's twisted frame to work on it was 'indeed difficult, and financially incredibly costly'." |
| M3 | 002 | fixed | "'The Sydney version now stands outside the Guggenheim Museum in Bilbao.'" → "the Puppy that 'now stands outside the Guggenheim museum in Bilbao' is 'the one designed and created' in Sydney." @sources corrected. **FACTS G5 itself not edited** (research file outside this pass). |
| S1 | 002 | fixed | "…by popular acclaim,' the same paper wrote." → "…by popular acclaim,' the museum's Lucía Agirre told the same paper." Note: she shares the surname of Txema Agirre, the next stop. No relation is implied, but the lead may want her role added ("deputy director for curatorial affairs"). |
| S2 | 001 | overridden | Lead decision 1: "about an hour and forty minutes" kept. |
| S3 | 003 | fixed | "This small square carries the name of a police officer… Here, he is Txema Agirre." → "This small square is named after a police officer… He is remembered by the Basque form of his name, Txema Agirre." / "Every October, flowers are laid for him." → "On anniversaries, flowers are laid here for him." Note (NICE): "Two Ertzaintza officers" → "Ertzaintza officers". Also (§3, Aznar): "the inauguration, attended by King Juan Carlos, the Spanish prime minister…" → "the inauguration, which King Juan Carlos, the Spanish prime minister and the Basque president were to attend." |
| S4 | 007 | fixed | "The critic Hal Foster attacked the Guggenheim as spectacle, and called it… you may feel both halves of that sentence at once." → "In Sydney Pollack's film about Gehry, the critic Hal Foster argued that the building upstages the art it's meant to serve. Gehry, he said, had given his clients 'a sublime space that overwhelms the viewer'. Stand here a minute, and decide whether you agree." "2006" was left out (not read on the page). |
| S5 | 013 | fixed | "The curator Carmen Jiménez" → "The curator of this installation, Carmen Giménez". |
| S6 | 017 | fixed | "The builder says that at the time, CATIA…" → "One of the museum's own educators put it more sharply: at the time, CATIA…". **FACTS A24 not edited.** |
| S7 | 017 | fixed | "As the builder puts it, 'no two joints in the building are the same'." → the same words, unquoted. |
| S8 | 023 | fixed | "on the museum's map she stands between this pond and the big road bridge. Follow the river walk to her" → "The next main stop is Maman, the giant spider by the footbridge. Follow the river walk toward the big road bridge to find her" (route direction per R-S8, PLAN-allowed [O13, O14], in @where). |
| S9 | 024, 029 | fixed (partly) | 024: "It only wakes up after dark." → "…in the evening."; "Unless it's already dark… come back to the river walk after dark, and watch fire dance on water" → "By day you won't see them lit. If you're in Bilbao tonight, come back in the early evening. For about an hour, in short bursts, fire dances on the water, as Klein imagined." ("after the museum has closed" omitted, as the auditor allows.) 029: "The fire burns after dark" → "The fire comes for a short time in the evening". 023's Extra line dropped "which burns only after dark". **Not changed: 001 "The fire fountains burn only after dark" and 015 "which burn only after dark"** (user-approved timing words, not flagged by the auditor). **Lead: decide whether these also become "in the evening".** This also departs from PLAN/WRITER_BRIEF's "only the words 'after dark'"; PLAN 024 NOT on "posthumous" should be updated as the auditor notes. |
| S10 | 025 | fixed | "'Spiders are friendly presences that eat mosquitoes. So, spiders are helpful…'" → "'…eat mosquitoes,' she said. Then: 'So, spiders are helpful and protective, just like my mother.'" "said" (not the auditor's "wrote") matches the track's other Bourgeois attributions. |
| S11 | 027 | fixed | "It was the first bridge in Spain built with stays, the cables that hold up its deck." → "It's a cable-stayed bridge: cables from its masts hold up the deck." The superlative is cut (the hedged version did not fit 360 words). |
| S12 | bridge 018 H>025 | overridden by lead decision 4 | The stairs line is kept, because the lead restored it in 021 and the two must match. It is PLAN's allowed tagged phrase [O12]. It is now conditional: "If you're on the plaza, take the stairs down toward the river walk, away from the big road bridge." It becomes position-free if O12 fails. |
| N1 | 004 | fixed | "the first conversation lasted" → "the conversation that set it all going lasted". |
| N2 | 011 | fixed | "summed up the room in one line:" → "described the room as". |
| N3 | 012, 016 | fixed | 012: "There are two of them" → "Here are two more Torqued Spirals". 016: "Find the twisted ellipses, then Snake, then the spirals" → "Find the first spiral and the twisted ellipses, then Snake, then the other spirals". |
| N4 | 013 | not done | "At the far end of the gallery, away from the Atrium" is kept as tagged [O6]; it rests on PLAN's 104 dead end. Revisit after O6. |
| N5 | 017 | fixed | "at a turning point" → at "the turning point between analog and digital practice". |
| N6 | 018 | fixed | "He was born there as Frank Owen Goldberg." → "He was born there, into the Goldberg family." |
| N7 | 018 | fixed | "long before Bilbao: fish lamps, and…" → "before this building: fish lamps in 1984, and…" (1984 from FACTS A37, OFF). |
| N8 | 018 | fixed | "Why a flower, and why all these curves?" → "Why all these curves?" |
| N9 | 019 | fixed | "Then he added:" → "He also said:". |
| N10 | 019 | fixed | "Critics of the Guggenheim's spread around the world had a word for it" → "Local critics had a word for it". |
| N11 | 020 | fixed | Order now: choir → "The King declared…" → "Then he threw the master switch that lit up the Atrium." |
| N12 | 021 | fixed | "a deep crisis in the steel sector" → "a deep industrial crisis". |
| N13 | 023 | fixed | "the work is 'both a phenomenon and an artifact'" → "fog sculpture is…". |
| N14 | 023 | fixed | "She later won that same prize for sculpture, the one Gehry had won in 1992." → "She later won that same prize herself, for sculpture. Gehry had won it, for architecture, in 1992." |
| N15 | 025 | fixed | "one of six casts" → "one of an edition of six, plus an artist's proof". |
| N16 | 026 | not done | "0.38 of a millimetre" does not fit the 360 cap (026 is at 360). FACTS' safe wording is "about a third of a millimetre", and it is attributed to the builder. |
| N17 | 026 | fixed | "The price drop, it reported, let Gehry choose" → "The price drop, Gehry's office said, let him choose". |
| N18 | 027 | fixed | "This spot, the museum notes, is 'the immediate entrance…'" → "This bridge, the museum notes, stands at 'the immediate entrance…'". |
| N19 | 002 | fixed | "his own watering system, run remotely" → "a new remote-controlled watering system". |
| N20 | 020 | fixed | "The Spanish prime minister and the Basque president were there too, under tight security…" → "The Basque president was there too. Security was tight, with marksmen watching from the rooftops." |
| §3 items | 006, 027, 003/020 | – | 006's "December 2018" is kept (SEC, EUSK). 027's superlative is cut (S11). Aznar is fixed in 003 and 020. |

## Route and listening audit (R-)
| ID | Track | Status | Before → after |
|---|---|---|---|
| M1 | 001 | partly fixed | Time overridden (lead decision 1). The sentence is split: "The full tour takes about an hour and forty minutes. The essential takes about an hour and a quarter, and the highlights about three quarters of an hour, walking included." |
| M2 | 021, 019, 020 | fixed | See lead decision 4. 021 paragraph 2: "…You're heading for the river walk, the promenade along the water. If you've come out onto the plaza, take the stairs that lead down from the plaza toward the park and the river walk, on the side away from the big road bridge. If you've come out on the river side, you're nearly there." Last paragraph: "At the water, walk along the river toward the big road bridge until you reach the pond beside the building, where a tall tree of silver balls stands in the water: The pond · Tall Tree & the Eye." 019 and 020 cues: "Leave the museum, and play it [the next stop] as you go. It tells you the way to the river walk". |
| M3 | 019 | fixed | "In 2025 about 1.3 million came, almost seven in ten from abroad, after a record year in 2023 of just over 1.32 million." → "Its record year so far was 2023. In 2025, almost seven in ten visitors came from abroad." Also "about 1.3 million people came". The jobs sentence stays separate, as it is DATED. |
| M4 | 015 | fixed | "Advice to Space V" / "Embrace XI" → "Advice to Space Five" / "Embrace Eleven". |
| M5 | 007 | fixed | "'With a height of 55m'" → "a height of fifty-five metres". |
| M6 | 023 | fixed | "three letters, F.O.G." → "three letters: F, O, G."; "Expo '70" → "the 1970 world's fair in Osaka" (also in @listen). "Frank O. Gehry" keeps its full stop, to match 023's @title and 022's cue: listen-QA it. |
| S1 | 013, 019, 023, 027 | fixed | "There's a short Extra…" → "If you're on the full tour, there's a short Extra…". |
| S2 | bridge 002 H>004 | fixed | → "On this shorter tour, there's no stop at the plaque. Pause there as you pass, if you wish. Then find the whole front of the museum, with the long straight street, Calle Iparragirre, at your back: Museum plaza · Our town is dying." |
| S3 | 003 | fixed | → "…where you can see the whole front of the museum. The long straight street into the city, Calle Iparragirre, should be at your back. The next stop is about how the museum began: Museum plaza · Our town is dying." |
| S4 | bridge 009 H>018 | fixed | → "On this shorter tour, step into the nearest sculpture if you like. Then take a glass lift up from the Atrium. If you can, glance down from the second-floor balcony opposite gallery 204. At the balcony opposite gallery 304, play Third floor · The metal flower." |
| S5 | bridge 015 E>017 | fixed | → "On this shorter tour, skip the second-floor stop. If you like, glance down at the Serra from the balcony opposite gallery 204 on the way. Then take a glass lift toward the third floor, and start Lifts and walkways · Every piece different in the lift." |
| S6 | bridge 018 H>025 | fixed | → "On this shorter tour, skip that stop and leave the museum. If you're on the plaza, take the stairs down toward the river walk, away from the big road bridge. At the water, walk toward that bridge, past the pond, to River walk · Maman." |
| S7 | bridges 004 E/H>007 | fixed | "…Play the next stop near its middle, where you can look straight up." → "…Near its middle, where you can look straight up, play Atrium · The heart of the building." |
| S8 | 024, 025 (023) | fixed | 024: "Now follow the river walk toward the big road bridge, to the giant spider by the footbridge". 025: "Now walk on along the river walk toward the big road bridge, to where you can get close…". 023: see F-S8. |
| S9 | 023 | fixed | "watch the titanium wall behind it soften and vanish" → "watch the building soften and vanish". |
| S10 | 002 | fixed | "In the small square just in front of Puppy, there's a plaque." → "…in front of Puppy, on the city side, there's a plaque." |
| S11 | 004, 021 | fixed | 004: "and the site was 'a former wharf with port and industrial use on a curve of the Nervión'" → "and the working riverbank this museum replaced". 021: the wharf quote is cut; the track opens "Before there was a museum here, this riverbank worked for a living." 001 keeps the quote. |
| S12 | 013 | fixed | "Snake, the oldest of the eight, was here for the opening. The rest arrived in 2005." is cut; 009 carries it for E and H. @what clause removed. |
| S13 | 022 | fixed | "The museum's architecture route puts it this way: 'The pond pays tribute…'" → "From the terrace you heard that it's a tribute to the river." Safe: E and Full both contain 015. |
| S14 | 016 | fixed | "Down on the floor, the same guide says, 'the viewer loses all reference…'" → "Down on the floor, as you found among the spirals, you lose all reference." / "Serra said of these pieces: 'When you move…'" → "Remember Serra's line, that when you move, they move too, and you're always trying to get them?" / "Watch them vanish, then turn up again…" → "Wait for someone to walk into a spiral, and see how long it takes them to come out." / The column sentence is cut to "Notice, too, what isn't there: a single column." |
| S15 | 009 | fixed | adds ": rings and balls, cut in steel." |
| S16 | 007 | fixed | "in the gallery that opens off the Atrium" → "in gallery 101, which you can see from the Atrium". |
| S17 | 025 | fixed | "She is bronze… She is one of a whole series" → "The spider is bronze, marble and stainless steel, one of a whole series". |
| S18 | 019 | fixed | via F-N10 ("Local critics had a word for it"). |
| S19 | 023 | fixed | "Soon after the opening" → "Soon after his show opened". |
| S20 | 003, 007, 009 | fixed | 003, see S3. 007: "…great skylight". It has "curved volumes…" 009: "…by Richard Serra. It's eight sculptures…". |
| S21 | 008, 027 | fixed | 008 "L.E.D." → "LED". 027 "At night, LEDs light the frame." → "At night, the frame is lit with LED lights." |
| S22 | 019, 011 | fixed | 019 "director for more than thirty years" → "long-time director". 011 "The museum's director then" → "The museum's long-time director". |
| N1 | 011–018 | fixed | Cues ". Title" → ": Title" (011, 012, 013, 014, 015, 016, 017, 018). 013's first colon became a full stop. The "·" pause still needs listen-QA per renderer. |
| N2 | 021 | not done | "Tall Tree & the Eye" is kept so the cue matches 022's @title exactly (the lead's check). Handle "&" → "and" in the pronunciation layer, or change PLAN's @title. |
| N3 | 010, 012 | fixed | "Closed, Open, Closed, Open, Closed"; "Torqued Spiral, Right, Left" / "Torqued Spiral, Open, Left, Closed, Right". |
| N4 | 008 | fixed | "LIKE BEAUTY IN FLAMES" → "Like Beauty in Flames" (speech; @what keeps the official caps). |
| N5 | 001 | fixed | "And the Basque side agreed to bear all the costs." cut. |
| N6 | 029 | partly fixed | "Gehry died in December 2025, at ninety-six." → "Gehry died in December 2025." The visitor numbers are left, as the auditor advises. |
| N7 | 026 | not done | The explicit "the builder's line from the walkways" does not fit the 360 cap. The implicit callback stays. |
| N8 | 016, 026, 027 | fixed | 016 "Its guide for teachers" → "The museum's guide for teachers". 026, see F-N17. 027, see F-N18. |
| N9 | 029 | fixed | "You've walked the whole of it." → "You've walked it, inside and out." "Steel you could walk through" is kept (the H bridge now invites a step inside). |
| N10 | 006 | fixed | "After ZERO, walk on…" → "Go in and take a look. Afterwards, walk on into the Atrium…". |
| N11 | 022 | fixed | "Kapoor talks about working in what he calls 'form languages'." cut. |
| N12 | bridge 025 H>027 | fixed | "its red frame" → "the red frame". |
| N13 | 002 | fixed | "[pause]" before "Before you go in, one stop that matters." |
| N14 | 003 | fixed | via F-S3. Neither line now depends on the sign's wording. "the square that bears his name" is kept (the naming is sourced). |
| N15 | 012 | fixed | "Torqued means twisted." → "Torqued, remember, means twisted." (Full-only, after 010). |
| N16 | 011 | fixed | "on either side of it" → "you've just walked through". |
| N17 | 001 | fixed | Added "On the full tour, you'll meet them all." before the list. |
| N18 | 101/104/204/304 | not done | Pronunciation file. There is no pronunciation layer in this folder, and it is pipeline work. |
| N19 | 019 | not done | The closing "Four hundred thousand was the target" is kept as framing (the auditor: "acceptable"). |
| N20 | 015 | fixed | "two cranes swung" → "a pair of cranes swung". |
| §7 list | all | not done | Pronunciation respellings (SOM, CATIA, IDOM, Txema, Iparragirre, etc.) belong to the render pipeline's override list (V5_AUDIO_STANDARD §4). The table is in R §7, ready to copy. |

## Bridges rewritten
- 002 H>004 (S2), 004 E>007 and 004 H>007 (S7), 009 H>018 (S4), 015 E>017 (S5), 018 H>025 (S6, F-S12), 025 H>027 (N12).
- Unchanged and checked against their track endings: 007 E/H>009 (007 no longer uses "opens off the Atrium" for Holzer) and 010 E>013.
- The 019, 023 and 027 endings changed only in their Extra phrasing. Extras skip silently, and the next-main-stop cues are unchanged, so no new bridge is needed.

## For the lead
1. PLAN §3 and the Targets table still say "about an hour and a half" for Full. 001 now says "an hour and forty minutes".
2. Fire timing: 024 and 029 now say "early evening… for about an hour, in short bursts" and "a short time in the evening" (F-S9). 001 and 015 still say "only after dark". Either align them, or confirm that the user's "after dark" wording stands. Either way, the WRITER_BRIEF/PLAN timing rule needs updating.
3. 011 title "Snake waited eight years": keep, or retitle (that changes PLAN's @title and 010's cue).
4. 002: Lucía Agirre right before Txema Agirre. Consider adding her role.
5. FACTS G5 (AGNSW quote) and A24 (CATIA attribution) are still wrong in the research file. PLAN rows 002, 011 and 017 carry the same errors.
6. 021 and 018 H>025 rest on [O12]/[O13] (the stairs and the walk toward the bridge). If O12 fails, both lose the stairs clause. If ALT-X applies, the river-side branch needs its own direction to the pond.

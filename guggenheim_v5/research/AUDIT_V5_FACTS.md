# AUDIT V5: independent fact audit of the 29 tracks (Guggenheim Museum Bilbao, EN)

Auditor: an independent agent that did not write the tracks. Date: 31 Oct 2026. Scope: the spoken bodies of `v5/tracks/001–029.perf.txt` (and the bridge lines in `v5/bridges/`), checked against the cited @sources, against FACTS / ROUTE / MAP / PLAN §2–§4, and against about 45 web pages that I re-read myself.
Method: WebSearch and WebFetch only. Official and academic sources first. One page at a time per site, fetched sequentially. No curl, no browser, no CAPTCHA, and no reliance on Wikipedia. I edited no tracks and did not touch git.

Severity: **MUST** = factually wrong, or a quotation that does not match its source; fix before recording. **SHOULD** = misattributed, overstated, or stated as certain against PLAN/[O#]; fix unless the lead decides otherwise. **NICE** = precision or style.

## 1. Track table

| Track | Verdict | One line |
|---|---|---|
| 001 | FIX | "about an hour and forty minutes" contradicts PLAN §3 (≈98 min, "about an hour and a half"). |
| 002 | FIX | The AGNSW "quote" is not on the page (**MUST**). "It isn't so" was said by the museum's Lucía Agirre, not written by "the paper". |
| 003 | FIX | The plaza's name and signage are stated as certain [O2, F-L]. "Every October" is only weakly sourced. |
| 004 | OK | Verified. NICE: "first conversation" vs TAN's "the conversation that set the course". |
| 005 | FIX | Pérez's "financially incredibly costly" is quoted out of context (**MUST**). |
| 006 | OK | Verified (Local Projects, /en/zero). The Dec 2018 date was not re-verified (see §3). |
| 007 | FIX | Hal Foster: the source and the referent are wrong. He said it in Pollack's film, about the building, not about this Atrium. |
| 008 | OK | Verified on the work page and PR-HAR. |
| 009 | OK | Verified. |
| 010 | OK | Verified (teachers' guide strings exact). |
| 011 | FIX | "held just one work… stood here alone… the only one" is false: Lichtensteins and a Warhol hung beside Snake in 1997 (**MUST**). |
| 012 | OK | Quotes verified. NICE: "There are two of them": the first piece in the gallery is also a Torqued Spiral. |
| 013 | FIX | The curator is **Carmen Giménez** (AP misspelt her "Jimenez"). "away from the Atrium" is a position [O6]. |
| 014 | OK | Verified on Ara. |
| 015 | OK | Verified on WP-ADV (305 cm, quotes; "To construct…" also on this page). |
| 016 | OK | Teachers'-guide strings exact. NICE: the listed order skips the first spiral. |
| 017 | FIX | The CATIA quote is the museum's Marta Arzak, not "the builder". "no two joints…" is not verbatim. |
| 018 | OK | Verified. NICE: birth name conflict; "long before Bilbao" for 1992; "Why a flower" is never answered. |
| 019 | OK | Figures verified. NICE: quote order ("Then he added"); "McGuggenheim" came from local critics (TAN). |
| 020 | OK | AP details verified. NICE: the switch and the words are in the wrong order. Aznar's presence rests on EI17's "would attend" (§3). |
| 021 | OK | UPM verified. NICE: "steel sector" (UPM's words; it was a shipbuilding crisis). |
| 022 | OK | Verified on the Kapoor page. |
| 023 | FIX | "on the museum's map she stands between this pond and the big road bridge" is an inference stated as map fact [O14]. NICE: Nakaya's 1990 remark was about fog sculpture in general. |
| 024 | FIX | "come back… after dark, and watch fire" overstates: the fountains run one hour in the evening, one minute every fifteen. "Posthumous realization" is now verified on the page (PLAN NOT outdated). |
| 025 | FIX | Bourgeois quote spliced: a sentence is silently omitted between "…eat mosquitoes." and "So, spiders…". |
| 026 | OK | Verified (CONSTR, FERRO "quilted", BW, APM). NICE attributions. |
| 027 | FIX | "the first bridge in Spain built with stays" rests on one tourism site, and I could not confirm it. Hedge it or cut it. |
| 028 | OK | R-ARCH list verified verbatim. |
| 029 | FIX | "The fire burns after dark, so … worth a second look tonight": same overstatement as 024 (SHOULD). Otherwise verified. |
| Bridge 018 H>025 | FIX | "Take the stairs down from the plaza … on the side away from the bridge" is the ABC-BLOG hint stated as fact [O12]. 021 itself was made position-free. |

Counts: **OK 16 · FIX 13 (+1 bridge) · HOLD 0**. Findings: **MUST 3 · SHOULD 12 · NICE 20**.

## 2. Findings

### MUST

**M1 — 011: "Snake stood alone for eight years" is false**
- Words: "For eight years, this long gallery held just one work. The rest of the room was waiting." / "When the doors first opened, it stood here alone." / "For eight years it was the only one."
- Problem: The Irish Times's opening-week review describes the "fish room" as "an appropriate home for Richard Serra's specially commissioned Snake", and adds: "On the other hand, two Lichtensteins and a Warhol seemed less at home in this rather warehousey ambience." So Snake shared the gallery from day one. The claim is also in PLAN 011 and FACTS E8's note, which are inferences that no source supports. UPI (2005) says only that "the artist's existing work 'Snake'" would be joined by seven new pieces.
- Checked: https://www.irishtimes.com/news/wow-bilbao-1.119611 (25 Oct 1997); https://www.upi.com/Entertainment_News/2005/05/06/Bilbao-museum-to-install-Serra-sculptures/UPI-12131115411044/
- Replace: "Snake is the oldest work in this room. Serra made it between 1994 and 1997 for the museum's opening, and for eight years it was the only piece of this installation here. The other seven came later, and the complete Matter of Time opened in June 2005." Change the hook to: "For eight years, Snake was the only part of this work in the room." End with: "It was the first. Everything else in this installation came after it." Consider retitling the track (for example "Snake came first").

**M2 — 005: Pérez's "costly" quote is out of context**
- Words: "He also called the project 'financially incredibly costly'. Both things, it seems, were true."
- Problem: The Ferrovial interview question was "Was it particularly difficult to work on such a seemingly twisted frame?" Pérez answered: "It was indeed difficult, and financially incredibly costly." He was describing access: lifting platforms, cranes, rope access, and bespoke scaffolding close to 50 m high. He was not passing judgement on the project as a whole. Placed straight after "on time and on budget", the track turns his words into a verdict on the overall cost.
- Checked: https://www.ferrovial.com/blog/en/2017/10/guggenheim-museum-construction/
- Replace: "He also admitted that just reaching the building's twisted frame to work on it was 'indeed difficult, and financially incredibly costly'." Or cut the sentence, and with it "Both things, it seems, were true."

**M3 — 002: the AGNSW quotation is not on the page**
- Words: "As the Art Gallery of New South Wales records it, 'The Sydney version now stands outside the Guggenheim Museum in Bilbao.'"
- Problem: That string does not appear on the page. The page reads: "The version that now stands outside the Guggenheim museum in Bilbao, Spain, is the one designed and created … on Sydney Harbour at the Museum of Contemporary Art in Sydney in 1995 as a Kaldor project." FACTS G5 and PLAN 002 carry the same false quote.
- Checked: https://archive.artgallery.nsw.gov.au/exhibitions/archived/2010/kaldor_projects/projects/1995_jeff_koons/index.html
- Replace: "As the Art Gallery of New South Wales records it, the Puppy that 'now stands outside the Guggenheim museum in Bilbao' is 'the one designed and created' in Sydney." Or paraphrase without quotation marks. Also correct FACTS G5.

### SHOULD

**S1 — 002: "It isn't so" is misattributed**
- Words: "'There is an idea that Puppy stayed in Bilbao by popular acclaim,' the same paper wrote. 'It isn't so.'"
- Problem: El Independiente does not say this in its own voice. It quotes the museum's own deputy director for curatorial affairs and archive: "asegura Lucía Agirre". The story is stronger, and correct, with her name. Separately, "just arrived from Australia" is the journalist's narration, in a sentence about the attack. That part is fine as "one Spanish paper".
- Checked: https://www.elindependiente.com/?p=144701
- Replace: "'There is an idea that Puppy stayed in Bilbao by popular acclaim,' the museum's Lucía Agirre told a Spanish paper. 'It isn't so.'"

**S2 — 001: the Full time conflicts with PLAN**
- Words: "The full tour takes about an hour and forty minutes".
- Problem: PLAN §3 estimates ≈98 min (92–105) and recommends option (a): "about an hour and a half". Nothing in the notes records a lead decision to change it.
- Replace: "about an hour and a half", or have the lead confirm the change.

**S3 — 003: the plaza's name and signage are stated as certain, and "every October" is weakly sourced**
- Words: "This small square carries the name of a police officer… Here, he is Txema Agirre." / "in the square that bears his name" / "Every October, flowers are laid for him."
- Problem, part 1: The sources do agree that a plaza by the museum is named after him (Orain 2022: "bautizada con el nombre del ertzaina"; ABE17). But EI17 says only that the plaque "da nombre a la plaza", and FACTS L lists "the plaza's exact signage" as unverified. "Here, he is Txema Agirre" asserts what the sign says [O2].
- Problem, part 2: The October offering is not in EI17. Orain 2022 says only that the floral offering was made "como en anteriores ocasiones".
- Checked: https://www.elindependiente.com/politica/2017/10/13/gobierno-vasco-ignora-recuerdo-agente-atentar-rey-inauguracion-guggenheim/amp/ ; https://orain.eus/es/politica/2022/10/13/recuerdan-a-txema-agirre-en-bilbao-asesinado-por-eta-hace-25-anos/
- Replace: Keep "This small square is named after a police officer" (sourced), but cut "Here, he is Txema Agirre" until O2 reads the sign. Change the October line to: "On anniversaries, flowers are laid here for him."
- Note (NICE): EI17 speaks of a single agent asking for papers, while the 2016 prosecution account has two ertzainas. "Two Ertzaintza officers went to check the van" is fine as sourced, but "officers went to check the van" avoids the conflict.

**S4 — 007: Hal Foster's source and referent are wrong**
- Words: "The critic Hal Foster attacked the Guggenheim as spectacle, and called it 'a sublime space that overwhelms the viewer'. Stand here a minute, and you may feel both halves of that sentence at once."
- Problem: The Guardian (Rowan Moore) says Foster spoke "in Sydney Pollack's film Sketches of Frank Gehry". His point was that "the building trumps the art it is supposed to serve": Gehry has "given his clients too much of what they want, a sublime space that overwhelms the viewer, a spectacular image that can circulate … as brand". He was talking about the building, not specifically the Atrium. The quote itself is verbatim.
- Checked: https://www.inkl.com/news/the-bilbao-effect-how-frank-gehry-s-guggenheim-started-a-global-craze
- Replace: "Not everyone was won over. In a 2006 film about Gehry, the critic Hal Foster argued that the building upstages the art it's meant to serve, that Gehry had given his clients 'a sublime space that overwhelms the viewer'. Stand here a minute, and decide whether you agree." The film's year is general knowledge and was not read on the page. Drop "2006" if you want page-only facts.

**S5 — 013: the curator's name is misspelt**
- Words: "The curator Carmen Jiménez called him…"
- Problem: She is **Carmen Giménez**, curator of *Richard Serra: The Matter of Time* (Guggenheim library record, 2005). The AP obituary spells her "Jimenez" and calls her "the exhibition organizer". The spoken audio is identical, but the script, transcripts and PDF should read Giménez. "Curator" is accurate.
- Checked: https://library.guggenheim.org/bib/23116 ; https://www.kqed.org/arts/13954850/sculptor-richard-serra-the-poet-of-iron-dies-at-85
- Replace: "The curator of this installation, Carmen Giménez, called him, as AP reported her words in English, 'beyond doubt the most important living sculptor'." This also explains who she is.

**S6 — 017: the CATIA quote is the museum's, not the builder's**
- Words: "The builder says that at the time, CATIA 'had only been used in the French aeronautical industry'."
- Problem: The Ferrovial blog attributes this to Marta Arzak, Assistant Director for Education and Interpretation at the Guggenheim Bilbao. FACTS A24 also has it as Ferrovial's own statement.
- Checked: https://www.ferrovial.com/blog/en/2017/10/guggenheim-museum-construction/
- Replace: "One of the museum's own educators put it more sharply: at the time, CATIA 'had only been used in the French aeronautical industry'."

**S7 — 017: the "joints" quote is not verbatim**
- Words: "As the builder puts it, 'no two joints in the building are the same'."
- Problem: Ferrovial's wording is "with no two joints being the same in the whole building". FACTS A23 tidied it. 026 already uses the line unquoted, which is correct.
- Replace: "As the builder puts it, there are 'no two joints being the same in the whole building'." Or drop the quotation marks: "As the builder puts it, no two joints in the building are the same."

**S8 — 023: a map inference is stated as map fact [O14]**
- Words: "on the museum's map she stands between this pond and the big road bridge."
- Problem: The map shows Kapoor's marker "west of 101 (pond)" and Maman's "north of the west end of 104". "Between the pond and the bridge" is PLAN's inference, which PLAN tags [O14] (ALT-M exists because it may be wrong). Attributing an inference to the map makes it sound verified.
- Checked: research/map/OFFICIAL_MAP_NOTES_30OCT2026.md.
- Replace: "The next main stop is Maman, the giant spider by the footbridge. Follow the river walk to her [O14]". Restore a placement only after O14.

**S9 — 024 and 029: "after dark" overstates when the fire runs**
- Words: 024 "Unless it's already dark, you won't see them lit. So if you're in Bilbao tonight, come back to the river walk after dark, and watch fire dance on water". 029 "The fire burns after dark, so the river walk is worth a second look tonight."
- Problem: The work page says the fountains are active "every fifteen minutes for one minute", within a one-hour evening window (October 7:30–8:30 pm; May–July 9–10 pm, which is not "after dark" in midsummer). Someone who comes back at 11 pm sees nothing. PLAN bans clock times, but a duration word is not a clock time.
- Checked: https://pro.guggenheim-bilbao.eus/en/the-collection/works/fire-fountain
- Replace: 024: "…come back to the river walk in the early evening, after the museum has closed. For about an hour, the fountains flare up in short bursts." 029: "The fire comes for a short time in the evening, so the river walk is worth a second look tonight." If "after the museum has closed" is wrong in Nov–Feb, as the writer notes, keep only "in the early evening".
- Also: PLAN 024's NOT bans "posthumous" as "unsourced on a page". It is now on the page: "In the posthumous realization of Fire Fountain in Bilbao…". The writer's use is accurate; update PLAN.

**S10 — 025: a Bourgeois quote is spliced without an ellipsis**
- Words: "'Spiders are friendly presences that eat mosquitoes. So, spiders are helpful and protective, just like my mother.'"
- Problem: The teachers' guide prints a sentence in between: "We know that mosquitoes spread diseases and are therefore unwanted." Presenting the two as one continuous quote breaks the verbatim rule.
- Checked: https://guggenheim-bilbao.eus/en/learn/schools/teachers-guides/maman
- Replace: "'Spiders are friendly presences that eat mosquitoes,' she wrote. And: 'So, spiders are helpful and protective, just like my mother.'" Or restore the missing sentence.

**S11 — 027: "first in Spain" rests on one tourism site**
- Words: "It was the first bridge in Spain built with stays, the cables that hold up its deck."
- Problem: The only source is Bilbao Visita Virtual, a tourism site made with the Basque tourism department. Structurae confirms that the bridge is cable-stayed (1968–1972) but not that it was the first. My searches found no engineering source for "first in Spain". This is a superlative with a single, non-specialist source.
- Checked: https://www.bilbaovisitavirtual.eus/en/bilbao-through-its-bridges/ ; https://structurae.net/en/structures/puente-de-los-principes-de-espana
- Replace: "It's a cable-stayed bridge: cables from its masts hold up the deck. A Bilbao guide to the city's bridges calls it the first of its kind in Spain." Or cut the superlative.

**S12 — Bridge 018 H>025: a low-grade hint is spoken as fact [O12]**
- Words: "Take the stairs down from the plaza toward the park and the river walk, on the side away from the bridge."
- Problem: This rests on ABC-BLOG, which PLAN grades "ONSITE hints only, never facts" [O12, and O11 for the exit]. The writer of 021 deliberately replaced the same wording with a position-free cue. Highlights listeners still hear the unverified version.
- Replace: "On this shorter tour, leave the museum and make your way down to the river walk. At the water, follow the river walk past the pond's tree of silver balls to the giant spider by the footbridge." Tag it [O11–O14].

### NICE

1. **004** "Krens recalled that the first conversation lasted 'no more than half an hour'". TAN's words are "the conversation that set the course for the museum". Say "the conversation that set it all going".
2. **011** "Robert Hughes summed up the room in one line: 'one old and seven new rolled steel sculptures'". It is a clause inside Hughes's praise of Serra, read in an ArtsJournal digest (https://www.artsjournal.org/?p=24278). Say "Robert Hughes described the room as…".
3. **012 and 016** "There are two of them" (the spirals), and "Find the twisted ellipses, then Snake, then the spirals". The first piece at the Atrium end is also a Torqued Spiral (ZWIR order). Say "two more Torqued Spirals" (012), and in 016 "the first spiral and the twisted ellipses, then Snake…".
4. **013** "At the far end of the gallery, away from the Atrium" is a position [O6]. R-COLL says only "at the far end". This is acceptable if O6 confirms that 104 is a dead end.
5. **017** "at a turning point between analog and digital practice": the source has "**the** turning point" (https://www.archdaily.com/881663/…). Also, ArchDaily's only rope-access evidence is a photo caption ("Mountain climber installing titanium facade panels"). Ferrovial says climbers gave rope access "in some areas". "Climbers on ropes fitted titanium panels" is acceptable.
6. **018** "He was born there as Frank Owen Goldberg." The museum says Frank Owen Goldberg, but CBS (5 Dec 2025) says "Ephraim Owen Goldberg". Safe wording: "He was born there, Frank Goldberg" or "born into the Goldberg family". Checked: https://www.cbsnews.com/news/frank-gehry-dies-age-96-architect
7. **018** "Fish swam through his work long before Bilbao: fish lamps, and a … fish sculpture … in Barcelona in 1992." 1992 is the year after he won Bilbao. Say "before this building: fish lamps in 1984, and…".
8. **018** "Why a flower, and why all these curves? Gehry's answer went back to his childhood." The carp story answers the curves, not the flower. Say "Why all these curves?".
9. **019** "dismissed… in a word we won't repeat here, and blamed journalists for it. Then he added: 'I apologise…'". In the Guardian the apology comes first, and the coarse line comes later. Say "He also said:".
10. **019** "Critics of the Guggenheim's spread around the world had a word for it: McGuggenheim." TAN credits **local** critics, who attacked the €20m fee as cultural imperialism. Say "Local critics had a word for it".
11. **020** "threw the master switch … and declared". AP: the King said the line, then "flipped the master switch". Reverse the order.
12. **021** "a deep crisis in the steel sector". These are UPM's words; Euskalduna was a shipyard. Say "a deep industrial crisis".
13. **023** "In Nakaya's words, the work is 'both a phenomenon and an artifact'". The page cites a 1990 statement about fog sculpture in general, made before this 1998 work. Say "In Nakaya's words, fog sculpture is…".
14. **023** "She later won that same prize for sculpture, the one Gehry had won in 1992". This could suggest that Gehry won it for sculpture. Say "the same prize Gehry had won, for architecture, in 1992".
15. **025** "Bilbao's is one of six casts". The edition is 2/6 + A.P. Say "one of an edition of six, plus an artist's proof".
16. **026** "The builder gives their thickness as about a third of a millimetre". The builder gives 0.38 mm. Say "The builder gives it as 0.38 of a millimetre, about a third of a millimetre".
17. **026** "The price drop, it reported, let Gehry choose titanium…". In BusinessWeek this is Randy Jefferson of Gehry Partners speaking. Say "his own office said".
18. **027** "This spot, the museum notes, is 'the immediate entrance to the city center'". The page means the bridge site, not the listener's spot. Say "This bridge, the museum notes, stands at…".
19. **002** "Since 2022 he has had his own watering system, run remotely". The press release says "un nuevo sistema de riego en remoto" (Puppy always had internal irrigation, per jeffkoons.com). Say "a new remote-controlled watering system".
20. **020** "The Spanish prime minister and the Basque president were there too". AP mentions only Ardanza. EI17 says "Todos acudirían" ("would attend"). See §3.

### Verified as written (the risky items the brief listed)
- **Vidarte, UPI 2005.** "This huge gallery was envisioned to hold art of the 21st century" (UPI: "Museum director Juan Ignacio Vidarte said"). Also "pilgrimage site". 430-ft gallery; opening 8 June.
- **Hughes.** "one old and seven new rolled steel sculptures": verbatim, in a digest.
- **AP / KQED (Serra).** Shipyard pipefitter father; steel foundries "to help finance his education"; died 26 Mar 2024 on Long Island, aged 85.
- **Teachers' guide (Serra).** "loses all reference…", "partially hidden" (Serra, quoted by the guide), "the two final works of this evolution", "transform in unexpected ways", "continuous movement", and every Serra line: all exact. Note that the guide gives Serra's birth year as 1939 and *Snake* as 1995–97; neither is spoken.
- **Simpsons.** The Real Deal: "it has haunted me" (CNN, Fareed Zakaria GPS, Sept 2011).
- **SOM / Zils.** The quote is exact. SOM was the structural engineer, with IDOM as local engineer.
- **Ferrovial.** BIM claim, attributed to Pérez; 665/664 piles averaging 14 m; 0.38 mm; "quilted rather than flat".
- **Chillida.** 305 × 143 × 207 cm; both museum quotes; "To construct is to build in space."
- **Puppy.**
  - Edition 1 + AP; Bilbao has the AP; Rockefeller Center 2000; Brant Foundation 2002 to date.
  - Arolsen 20,000 plants; Sydney 60,000.
  - 40,000 plants, May and October, nine days, twenty specialists, remote irrigation since 2022 with six zones.
  - "No es así".
- **Txema Agirre.**
  - Age 35 and newborn son (EI17); 13 Oct 1997.
  - The false gardeners and false pots.
  - The plaque in "la pequeña plaza que precede al Puppy" took 14 years.
  - The monolith; tribute 13 Oct 2022; Ardanza calling him a hero (AP).
  - "Died of his wounds" is consistent with the Irish Times's "died 26 hours later".
- **AP, opening day.**
  - "The Guggenheim Museum is inaugurated!"; the master switch.
  - The choir in Basque greeting the King and Queen Sofía; rooftop sharpshooters.
  - About 2,000 marchers; Ardanza "remembered slain policeman Jose Maria Aguirre"; $100 m.
  - The painter's quote.
- **Public opening.** Sunday 19 Oct 1997 (Irish Times).
- **Philip Johnson.** Dezeen reports the line "after visiting shortly following its opening", with no source. The track's "is reported to" is correct.
- **Harvard case.** $20 m "rental fee"; $50 m; $100 m building budget; three weeks and $10,000; Frankfurt; "most unusual project"; "strength of his vision"; "two arduous days"; jogging; Artxanda; Alhóndiga; three re-estimates; plywood replaced by galvanised sheet; "does not have a single straight line…".
- **Dezeen.** "on time and on budget" (Dezeen: as Gehry "often recounts"); APM agrees. The fish quote is from Charlie Rose, 1997.
- **ZERO.** "We transformed a small, underused lounge…" (Local Projects); 300º and 14 times; the txalaparta.
- **Atrium.** "With a height of 55m and an approximate surface of 900m2".
- **Visitor numbers.**
  - 1998 ≈ 1,307,200 (2017 PDF: "superado en 15.411 visitantes la cifra de 1998").
  - Almost 4 m in the "first three years of operation" (ArchDaily).
  - 2023: 1,324,221, a record. 2025: 1,305,003, 69 % foreign, 14,319 jobs.
  - 24,710,000 at 25 years, "más del doble".
  - €4.3 bn by end-2016 "commissioned by the museum".
- **Quotes on the Bilbao effect.**
  - Beatriz Plaza (MPRA abstract): verbatim.
  - Vidarte: "ingredients" / "cannot be isolated" / "family name": verbatim.
- **NPR (Gehry).** The carp story (NPR's narration); "The curves were from the fish — were a sense of movement with inert materials"; "We all need love. And it's nice to get it for doing things like that."
- **Gehry biography.** Pritzker 1989; Barcelona fish 1992; Praemium Imperiale 1992 (for architecture); died 5 Dec 2025 in Santa Monica, aged 96.
- **Titanium.**
  - The sample pinned outside his office; "approximately 33,000".
  - BusinessWeek reprint lines.
  - APM: "We'll probably never know", told as speculation.
  - IDOM's galvanised backing (Harvard).
- **Kapoor.** Bombay 1954; 73 spheres; 1297 cm; "form languages" (Kapoor's own term); all quotes.
- **Nakaya.**
  - F.O.G. = "Frank O. Gehry"; 1,000 nozzles.
  - Commissioned at Rauschenberg's invitation for his 1998 Bilbao retrospective; "Soon after the opening, Rauschenberg purchased it and donated it to the museum."
  - E.A.T. and the Pepsi pavilion at Expo '70 (the page wrongly says Tokyo; no city is spoken).
  - "every hour on the hour … eight minutes"; her father's snow crystal (PRAEM).
- **Klein.** 1959 Sorbonne; Krefeld, about fifty Bunsen burners on the lawn in front of the Mies van der Rohe villa (Haus Lange retrospective); five fountains; "posthumous realization"; the quote; 1928–1962.
- **Maman.** All the work-page wording; Tate "inaugural commission … May 2000"; "Edition 2/6 + A.P."; Ottawa.
- **La Salve.** Príncipes de España; Batanero; 1968–1972; cable-stayed (Structurae).
- **Buren.** 2007, Tenth Anniversary; "less brutal, but more visible"; three circles; black-and-white stripes; red vs green; LEDs; "immediate entrance to the city center".
- **Euskalduna and Bilbao Ría 2000.** Founded 1900, closed 1988; Bilbao Ría 2000 set up in 1992 (UPM).
- **Isozaki and the architects.** The Isozaki Towers line, and the R-ARCH architects list verbatim (no extra words between "Frank Gehry" and "but also").
- **Past tense.** Correct throughout for Gehry, Serra, Bourgeois, Chillida and Klein. No "Gehry is/says" or "Serra is/says" was found. Kapoor, Nakaya and Koons are living and correctly in the present tense.
- **Numbers across tracks.** Consistent (55 m; 130 × 30 m; about 1.3 m in 1998; more than 600 piles; about 40,000 plants; 1,034 t spoken as "just over a thousand tonnes"; 38 t). The only clash between tracks is the 001 time versus PLAN (S2).

## 3. Claims I could not verify either way

1. **ZERO "opened in December 2018"** (006). /en/zero and Local Projects give no date. The source is turismo.euskadi.eus (EUSK, SEC, via ROUTE), which I did not re-read. Keep it as SEC, or cut the date.
2. **"First bridge in Spain built with stays"** (027). One tourism-site source; no confirmation or refutation found (S11).
3. **Aznar's presence at the inauguration** (003 "attended by…", 020 "were there too"). EI17 says the three were the target and "Todos acudirían", which is future tense. AP 1997 and the Irish Times do not mention him. It is very likely true, but no contemporaneous page read confirms it. Safe wording for 020: "The Basque president was there too…".
4. **Gehry's birth forename**: Frank (museum biography) or Ephraim (CBS) (NICE 6).
5. **Where and when Philip Johnson said "the greatest building of our time"**. Dezeen gives no source; the track's hedge is correct.
6. **The 1,034 t total** (009) and the Tate "white marble eggs" were not re-fetched; I relied on FACTS E3 / G13.
7. **Whether "every October" there is an offering for Txema Agirre** (S3). Orain implies repeated offerings ("como en anteriores ocasiones") but not a fixed month.
8. **What the "/2017" in Holzer's date means**. Still unexplained on the work page; the track correctly avoids it.
9. **Carmen Giménez's "most important living sculptor"**: the date and occasion are not given by AP. The track correctly does not tie it to his death.

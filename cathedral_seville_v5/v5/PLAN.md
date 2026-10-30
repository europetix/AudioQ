# CATEDRAL DE SEVILLA + GIRALDA V5 (Yo Tours, English) — PLAN, 30 Oct 2026. Built from the lead's SKELETON.md (30 Oct 2026).

**Binding for writers.** Navigation and placement come first: customers complained that earlier guides described things in the wrong place. Facts come second, and only in the wording of `research/FACTS_OCT2026.md` (verdicts OK / HEDGE / LEGEND; UNVERIFIED is never scripted). Placements and statuses come from `research/VISIT_ROUTE_AND_SPACES_OCT2026.md`, plus five pages read for this plan on 30 Oct 2026 (marked "read 30 Oct, plan" in the source key). Competitor gaps come from `research/OFFICIAL_AUDIO_COMPARISON_OCT2026.md`.

**There is no official visitor map** (none online; the user has been asked for a photo of the paper plan). So the destinations and the order below are binding, but every left/right, "straight ahead", compass word and "next to" is **PROVISIONAL**. Every cue names the destination by its **Spanish name** plus **one big landmark** to look for. Wherever geometry matters there is an ONSITE or MAP item (section 5 and `v5/ONSITE_CHECKLIST.txt`), tagged [Oxx] in the table. Writers must not add directions of their own.

## 1. Header

### User decisions (30 Oct 2026, from the skeleton)
- Build from scratch to the series standard (no old guide supplied; the old work is "quite old and not great").
- **Three lengths along ONE walking order**: Highlights ≈ 45 min, Essential ≈ 75 min, Full ≈ 110 min, as visit times **including walking and the Giralda climb**. One recording. The shorter versions get hand-written spoken "next stop" bridges; section 3 lists where.
- Languages EN, ES, FR, DE. Spanish names in cues work in all four.
- Must beat the official GVAM guide (€4 app / €5 device, 50+ points, numbers that don't match the cathedral's, wayfinding complaints) and the poorly rated ticket + audio bundles. Our answers: name-and-landmark cues instead of numbers; one linear route with a cue at the end of every track; both entrances handled in 001; the sacristies, chapter house and Patio told in depth (no competitor confirms them); the Giralda's 2025–26 news (builders' sketches, Phase VI works, the fallen lily vase), dated.

### Targets
- Skeleton: Full ≈ 9,000 spoken words (≈ 72 min listening + ≈ 38 min climbing/walking), Essential ≈ 5,600, Highlights ≈ 3,000.
- **This plan:** Full **28 tracks ≈ 7,470 words**, Essential **18 tracks ≈ 5,300 words**, Highlights **9 tracks ≈ 2,670 words**. Visit times (section 3): **H ≈ 44 min, E ≈ 76 min, Full ≈ 96 min (96–102)**.
- Why Full is short of 110: the tower alone takes ≈ 24 min, and three tracks are designed to be heard while climbing or descending (they cost no extra time); the sourced, correctly placeable content runs out at ≈ 7,500 words. Five held items can come back after ONSITE (+≈ 7 min). **Do not pad.** Open question for the lead (section 3).
- Type lengths (V5 standard): R 180–280 (aim 230) · W 250–360 (aim 300) · X 150–230 (aim 190) · ANCHOR/CLOSE 250–360 (aim 320). Listening at 125 words/min.

### Conventions
- **@room** = the space's Spanish name as visitors see it, with an English position note only where one space has several listening points: `Giralda · ramps`, `Capilla Mayor`, `Sacristía Mayor`, `Patio de los Naranjos`. 001 is `Entrada · Puerta del Lagarto or Puerta del Príncipe`.
- **@title** = `<Spanish name> — <title>`, e.g. `Sacristía Mayor — Campaña's Descent`. Extras: `<Spanish name> · Extra · <title>`. 001 takes a plain title (`Welcome to the Catedral de Sevilla`). CLOSE follows the room pattern (`Puerta del Perdón — The way out`).
- **Spoken names.** Always the Spanish name first, as on the signs, with an English gloss once per track ("the Sacristía Mayor, the great sacristy"). **No numbers anywhere**: there is no official map, and reviewers say the official guide's numbers don't match the cathedral's.
- **Cue pattern.** The last paragraph of every track except CLOSE gives the destination's Spanish name and one landmark to look for. A track before an Extra announces it: "There's a short Extra here on…; the next main stop is the Coro…". Never say "next track" (lint). Tracks heard while walking the tower say "the next stop plays on the way down" etc.
- **Directions.** Allowed without ONSITE: the landmark; "the middle of the church, where the transept crosses the nave"; "between the gilded altarpiece and the choir" (BLDG: the coro is "directly in front of the Main Chapel"); "turn round" at the crossing (same source); "the side aisle on the side where you came down from the tower" (= north: the Giralda is at the NE corner, research; San Antonio is on the Evangelio = north aisle, GLASS); "the far side of the church from the tower" (= south); "the far end, with the great central doors" (= west: Asunción centre of the west façade, BLDG); "the far side of the courtyard, opposite the cathedral" (= north side of the Patio: Perdón, research/BLDG); "follow the Salida / Giralda signs". **Not allowed until ONSITE/MAP:** left/right, "straight ahead", "north/south/east/west" spoken to listeners, distances, and any "next to" not listed above. Each provisional element carries its [Oxx] tag.
- **Lint.** The Uffizi room-cue regex does not fit. The cathedral lint must accept as a cue token any of: `Giralda|Capilla|Coro|Catedral|Sacristía|Sala|Sepulcro|Puerta|Patio|Nave|Antecabildo|Salida`. Lead: copy and adapt `lint.py` before writing starts.
- **Walking tracks.** 002 and 003 are heard while climbing, 006 while descending. They contain **no "look at…" instructions** except the ramps and walls around you, and they must work if the listener keeps walking.
- **Dated items** are a separate sentence that can be cut ("DATED" in the table; section 6).
- **Writing rules** as in the series standard. Tradition is voiced as tradition ("tradition says…"), never as fact; the cathedral's own superlatives are attributed ("UNESCO calls it…", "the Cathedral calls it…"). **No prices, hours, tickets, ticket types, booking, time slots, queues, security, bags, free Sunday visits, the official audioguide, shop or toilets.** "The Cathedral says" at most once per track.

### Sections (one folder each, in walking order)
| Folder | Section | Tracks | Spaces |
|---|---|---|---|
| `01_Opening` | Opening | 001 | Puerta del Lagarto or Puerta del Príncipe |
| `02_La_Giralda` | La Giralda | 002–006 | foot, ramps, bell level, descent |
| `03_Capilla_Mayor_and_Coro` | The heart of the cathedral | 007–010 | foot of the Giralda (inside), crossing: Capilla Mayor, Coro |
| `04_Around_the_naves` | Around the naves | 011–013 | Capilla de San Antonio, west end, Capilla de la Antigua |
| `05_Columbus` | Columbus | 014–015 | Sepulcro de Colón, south transept |
| `06_Sacristies_and_Chapter_House` | Sacristies and chapter house | 016–022 | Cálices, Pabellón, Sacristía Mayor, Antecabildo, Sala Capitular |
| `07_Capilla_Real_and_north_transept` | Royal chapel and the way to the courtyard | 023–024 | Capilla Real (outside the grille), Puerta de la Concepción |
| `08_Patio_de_los_Naranjos` | Patio de los Naranjos | 025–027 | Patio, view of the Giraldillo, Nave del Lagarto |
| `09_Closing` | Closing | 028 | Puerta del Perdón |

### The route (reasoning; binding order, provisional geometry)
**Fixed points (sourced).**
- **Entrances.** Puerta del Lagarto (street side C/ Cardenal Amigo Vallejo, east gallery of the Patio de los Naranjos, by the Giralda) for online tickets; **Puerta del Príncipe**, also called **Puerta de San Cristóbal**, in the south arm of the transept, for ticket-office buyers (SCHED, re-read 30 Oct, plan: "Online access through Lagarto Gate", "Ticket office access through Prince's Gate"; HIGH: "Lagarto or San Cristóbal, depending on the type of ticket"; BLDG: the Prince's Gate is "in the south arm of the transept" and is where "the cultural and artistic visit … is currently accessed individually"). Ticket types are ops only: in speech the doors are identified by name and landmark (the Lagarto by the crocodile overhead [O1]; the Príncipe by Columbus's tomb nearby [O2, O12]).
- **Order.** "The visit begins at the Giralda tower, which has its own access control" (SCHED, re-read 30 Oct, plan). **The page does not say whether this applies to Príncipe entrants, and gives no route inside.** → O2 CRITICAL, ALT-A. Inside, the order is free and self-guided (research).
- **The Giralda** is entered from inside the cathedral at its **north-east corner** (research). Ramps, one way at a time, "siempre por su derecha"; no wheelchairs or strollers (NORMAS). About 10 min up (TRV).
- **Exit.** The **Puerta del Perdón**, out of the Patio de los Naranjos (BLDG: "this door marks the exit for cultural and artistic visitors"; TRV). The church opens onto the Patio through the north arm of the transept, the **Puerta de la Concepción** (BLDG). EN Wikipedia says the Concepción is "kept closed except on festival days", so **which door visitors actually use into the Patio is unknown** → O15 CRITICAL, ALT-D. **No re-entry** once the ticket is validated (NORMAS).

**Interior plan facts used (and their sources).** Capilla Mayor in the central nave; the coro "directly in front of the Main Chapel", walled except for the Renaissance grille on its front (BLDG) — so both are seen from the crossing, facing each other. Capilla Real "occupies the head of the temple" (REN), i.e. the east end behind the Capilla Mayor. The sacristies and chapter house form the SE block (research). The Sala Capitular is reached from the Antecabildo "through a curved corridor" (REN). San Antonio is the baptistery chapel on the **Evangelio (north) aisle** (GLASS: "Nave lateral del Evangelio, sobre la capilla de San Antonio"; "Capilla del Bautismo"); how far west is unsourced [O9]. **WIKI-ES only (placement lead, paired with ONSITE):** along the south wall, from the east: Capilla del Mariscal, Antesacristía, Capilla de los Dolores, Capilla de San Andrés, then the Puerta de San Cristóbal; then Capilla de la Antigua ("larger than the others"), San Hermenegildo, Santa Ana, San Laureano toward the west front. The Sacristía de los Cálices is reached through the Capilla de los Dolores. Columbus's monument is near the Puerta de San Cristóbal; a replica of the Giraldillo stands outside that door. (GLASS confirms San Andrés on the Epístola/south aisle.)

**Chosen order: one loop, no backtracking.**
Entrance → **Giralda** (NE corner; up, bell level, down) → just inside at the foot of the tower (orientation) → **crossing**: Capilla Mayor, then turn round to the Coro → along the **north aisle** (the side you came down the tower) to the **Capilla de San Antonio** → across the **west end** (the inside of the Puerta de la Asunción) → along the **south aisle** to the **Capilla de la Antigua** → **south transept**: Columbus's tomb by the Puerta del Príncipe → east along the south side into the **SE block**: Sacristía de los Cálices (via the Capilla de los Dolores, WIKI-ES) → Sala del Pabellón [O13] → Sacristía Mayor → Antecabildo and curved corridor → Sala Capitular → back into the church to the **Capilla Real** at the east end (outside the grille) → **north transept**, Puerta de la Concepción → **Patio de los Naranjos** → view of the Giraldillo → **Nave del Lagarto** → **Puerta del Perdón**.
- Why: it is a single circuit (NE → centre → NW → W → SW → S → SE → E → N) that follows the official "begins at the Giralda" and the official exit, puts the altarpiece straight after the tower, keeps the SE rooms in the west-to-east order of their doors (WIKI-ES), and leaves the Capilla Real and the transept door for last, beside the way out.
- Rejected: the skeleton's order (crossing → Columbus → Antigua → back east to the sacristies → Capilla Real → all the way west to San Antonio → back east to the Concepción). It back-steps at the Antigua and crosses the church twice at the end (≈ 4 extra min).
- **Príncipe entrants** walk from the south transept through the crossing to the Giralda first (001 tells them), and meet Columbus's tomb again at 014. If O2 finds they must do the interior first and the Giralda last: ALT-A.
- **If you are not climbing** (wheelchairs, strollers, vertigo, or by choice: NORMAS), 001 sends you to the foot of the Giralda inside, to start at 007.

**What the map (or the site) must confirm:** MAP-1/MAP-2 and the CRITICAL ONSITE items O1, O2, O3, O5, O8, O13, O15, O18 (section 5).

### ALT cues (held: swap in after the map or the on-site check)
- **ALT-A (O2: Príncipe entrants must do the interior first, Giralda last):** a re-plan, not a swap. Lead's choice: (i) if staff let them go to the Giralda first, nothing changes; (ii) otherwise a "Príncipe order" playlist (014–015 → 016–022 → 023 → 007–013 → 002–006 → 024–028) needs re-recorded cues for ≈ 10 tracks. Decide before recording 001.
- **ALT-B (O13: the SE block runs the other way, in at the Sala Capitular end, out by the Cálices):** reverse 016–022 and re-record the cues of 015–023 (cues only; content unchanged).
- **ALT-C (O5/O16: the Giraldillo cannot be seen from the Patio, e.g. hidden by the Phase VI works):** 026 records version (b), with no "look up" ("high above on the tower, above the works…"). If it can be seen only from the bell level, the lead may move 026 to follow 005 (renumber).
- **ALT-D (O15: visitors enter the Patio by a door other than the Concepción):** 024 is still played facing the Concepción from inside; its cue and the E/H bridges say "follow the Salida signs into the Patio de los Naranjos".
- **ALT-F (O14: the Capilla Real grille is closed or curtained):** 023 records its "behind the grille, which is often closed" sentence instead of the "look through the grille" sentence (both written).
- **ALT-G (O13: the Sala del Pabellón is not between the Cálices and the Sacristía Mayor):** 017 moves within section 06; the cue lines of 016, 017 and 018 swap.
- **ALT-H (O17: the Nave del Lagarto cannot be reached at the end):** 027 records its "look across the courtyard at the covered gallery" variant, and 026's cue changes to match.

### Changes from the skeleton
1. **Interior order re-sequenced into one loop** (above). San Antonio moves up to straight after the coro; the Antigua comes before Columbus; the Capilla Real comes last before the transept door.
2. **New 006 W "From mosque to cathedral", heard on the way down the tower.** The mosque, 1248 and the 1401 decision move here from 001, which needs its words for the two entrances. The descent costs time anyway, so this track adds none.
3. **The Giraldillo moves from the bell level to the Patio (026, X→R).** It cannot be seen from inside the bell chamber; from the Patio you can look up at it [O16]. The bell level gets **new 005 X "Twenty-four bells"** (24 bells, OFF; la Gorda 1588; the Phase VI bell frames).
4. **Dropped (cannot be sourced or visited):** S022 Artemisia ("en restauración", PAINT); S026 Biblioteca Colombina (not on the cultural visit; one line on the library goes into 015 and 027); S011 Puerta del Príncipe X (thin: its two names go into 001 and 014, the Giraldillo replica outside it into 026).
5. **S017 Antecabildo R is not a stop** (no works confirmed; FACTS 11.6): it is walked through, named in 020's cue. The Sala Capitular gets **021 X "An oval for the chapter"** (architecture, OFF-rich) plus **022 W** (Murillo).
6. **S021 "Chapels of the north aisle" is held**: the OFF painting list names works in the Capilla de Santiago, Belén, Evangelistas, Ángel de la Guarda etc., but no source places those chapels. It comes back if MAP-1 places them. Its slot goes to **012 R "The west end"** (Puerta de la Asunción from inside, the oldest windows: BLDG, GLASS; Hernando Colón's gravestone only if O10 finds it).
7. **Columbus becomes two W:** 014 the monument; **new 015 "Whose bones?"** (journey, Santo Domingo claim, DNA 2003/2006/2024, safe line). The most-asked question deserves its own track.
8. **New 019 X** in the Sacristía Mayor: the Last Judgment dome and Murillo's San Isidoro and San Leandro (OFF).
9. **Type changes** where the verified material is rich: S009 Coro R→W; S012 Antigua R→W; S019 Capilla Real X→W; S025 Lagarto X→R; S005 Giraldillo X→R.
10. **Membership for time** (section 3): the tower takes ≈ 24 min, so **Highlights loses S015 Sacristía Mayor and S020 San Antonio** (≈ 9 min with walking) and gains 003 and 006 (heard while climbing and descending: no added time). **Essential loses S023 Concepción** (024, Full only) and gains 006, 013 Antigua and 015 Columbus's bones.
11. **Renumbering** (skeleton → plan): S001–S004 → 001–004; **005 new** (bells); **006 new** (descent); S006 → 007; S007 → 008; S008 → 009; S009 → 010; **S020 → 011**; **012 new** (west end; replaces S021, held); S012 → 013; S010 → 014; **015 new**; S011 dropped; S013 → 016; S014 → 017; S015 → 018; **019 new**; S016 → 020; S017 → walk-through, **021 new X**; S018 → 022; S019 → 023; S023 → 024; S024 → 025; **S005 → 026**; S025 → 027; S022, S026 dropped; S027 → 028.

## 2. Track table

**Source key** (URLs as logged in the research files, or read for this plan on 30 Oct 2026).

| Code | Grade | Source |
|---|---|---|
| SCHED | OFF | https://www.catedraldesevilla.es/en/cultural-visit/schedules-and-rates/ (re-read 30 Oct, plan: Lagarto = online, Prince's Gate = ticket office; "The visit begins at the Giralda tower, which has its own access control"; no route, no exit, no rule for Príncipe entrants; ≈ 75 min visit) |
| HIGH | OFF | https://www.catedraldesevilla.es/en/plan-your-visit-to-seville-cathedral-during-high-season-ticket-types-discounts-and-free-admission/ (17 Apr 2026: Lagarto or San Cristóbal by ticket type) |
| NORMAS | OFF | https://catedraldesevilla.es/wp-content/uploads/2025/03/Normas-generales-catedral-descargable-actualizado.pdf (no re-entry; Capilla Real worship only; ramps one way "siempre por su derecha"; no wheelchairs/strollers; health warnings) |
| BLDG | OFF | [O11] https://www.catedraldesevilla.es/en/the-cathedral/building/the-gothic-cathedral-main-altarpiece-choir-side-chapels-and-doorways (re-read 30 Oct, plan: Capilla Mayor in the central nave; coro "directly in front of the Main Chapel", grille on its front; double organ in the choir; Asunción centre of the west façade; Perdón aligned with the mosque's central nave and mihrab, Expulsion relief "just above the arch", exit; Concepción "on the north front of the transept … onto the Orange Tree Courtyard"; Príncipe "south arm of the transept", visit access; Campanillas at the head, left of the Royal Chapel) |
| REN | OFF | [O13] https://catedraldesevilla.es/en/the-cathedral/building/renaissance-additions-royal-chapel-chapter-house-and-main-sacristy (re-read 30 Oct, plan: Royal Chapel "occupies the head of the temple", entrance closed by a grille; Chapter Hall entered "from the antecabildo … through a curved corridor"; Campaña "in front of the central chapel" of the Sacristía Mayor) |
| GLASS | OFF | https://www.catedraldesevilla.es/en/?p=53385 (stained glass; read 30 Oct, plan: "Nave lateral del Evangelio, sobre la capilla de San Antonio"; San Antonio = "Capilla del Bautismo"; "Nave lateral de la Epístola sobre la capilla de San Andrés"; Ascension window, "Hastial del crucero norte sobre la puerta de la Concepción"; San Fernando window in the Antigua chapel; the openings in the western half and central nave are the oldest; three west-façade windows by Vicente Menardo; 13 saints windows in the transept by Arnao de Flandes) |
| HIST | OFF | [O1] https://www.catedraldesevilla.es/en/the-cathedral/its-history/ (timeline) |
| OVR | OFF | [O2] https://www.catedraldesevilla.es/en/?p=53300 |
| UNESCO | OFF | [O3] https://whc.unesco.org/en/list/383/ |
| LECT | OFF | [O4] https://www.catedraldesevilla.es/en/?p=51926 |
| TF | OFF | [O6][O7] Turris Fortissima congress page and abstracts PDF (Nov 2025) |
| GIR | OFF | [O8] https://www.catedraldesevilla.es/en/the-cathedral/building/the-giralda |
| AHPS | OFF | [O9] Junta, Archivo Histórico Provincial, "El símbolo que Morel regaló a Sevilla" (Dec 2022) |
| PATIO | OFF | [O10] Patio de los Naranjos and Colombian Library page |
| BIB | OFF | [O12] https://www.catedraldesevilla.es/en/?p=53313 |
| PAINT | OFF | [O14] https://catedraldesevilla.es/en/?p=53309 (paintings list) |
| GOLD | OFF | [O15] https://catedraldesevilla.es/en/?p=53366 (goldsmithing) |
| PH6 | OFF | https://www.catedraldesevilla.es/en/phase-vi-of-the-giralda-intervention-begins/ (14 Apr 2026) |
| VISITS | OFF | https://www.catedraldesevilla.es/en/the-cathedral-maintains-its-cultural-visits-during-regular-hours/ (9 Feb 2026) |
| GRECO | OFF | https://www.catedraldesevilla.es/en/the-cathedral-temporarily-hosts-el-grecos-work-santa-maria-magdalena/ |
| PLATA | OFF | https://www.catedraldesevilla.es/en/?p=71940 (Altar de Plata restoration) |
| ROOF | OFF | https://www.catedraldesevilla.es/en/cultural-visit/guided-tours/visit-to-the-roofs/ |
| ARCH | SEC | [S1] Archnet, Mezquita de Sevilla |
| ARAMCO | SEC | [S2] AramcoWorld, "The Giralda" (1994) |
| GUIN | SEC | [S4] Guinness World Records, largest cathedral (area) |
| IAPH | SEC | [S5]–[S8] IAPH Giraldillo bulletins and project pages |
| CAMP | SEC | [S10] campaners.com, Santa María la Mayor |
| FACTUM | SEC | [S11] Factum Foundation, Puerta del Perdón (Nov 2025) |
| RECIO | SEC | [S12] Recio Mir, *Laboratorio de Arte* 9 (1996) |
| UPO24 | SEC | [S13] *El Patio Colorao* (UPO), 30 Apr 2024 (crocodile) |
| RUIZ | SEC | [S14] Ruiz Jiménez, *Paisajes sonoros históricos* (2016) (the Sultan's embassy) |
| WILL | SEC | [S15] Williams, *Arts and Crafts of Older Spain* (1907) |
| OHC | SEC | [S16] Oficina del Historiador de La Habana PDF (Columbus tomb) |
| AP06 | SEC | [S18] NBC/AP, 19 May 2006 |
| EFE24 | SEC | [S19] Última Hora (EFE) and Público, 10 Oct 2024 |
| ALJ | SEC | Al Jazeera, 27 Oct 2024 (caution on origin claims) |
| AHPS-G | SEC | [S20] Google Arts & Culture / AHPS, Hernando Colón gravestone drawing (1539) |
| GEIIC | SEC | [S21] GE-IIC paper on Campaña's *Descendimiento* |
| MUR | SEC | [S22] visitasevilla.es "Ruta de Murillo" PDF |
| TERAMO | SEC | [S23] Univ. Teramo, the Corpus monstrance |
| GOYA | SEC | [S24] Fundación Goya en Aragón, *Santas Justa y Rufina* |
| CT | SEC | [S25] *Church Times*, 24 Jan 2020 |
| GLOBE | SEC | [S26] *The Globe* (NZ), 17 Apr 1875 |
| FERRER | SEC | [S27] Ferrer Garrofé, *Laboratorio de Arte* 6 (1993) |
| BBVA | SEC | [S28] Colección BBVA, *Our Lady of La Antigua* |
| BRIT | SEC | [S29] Britannica, History of Antigua and Barbuda |
| 3CAT | SEC | 3cat, 8 Jun 2024 (Murillo theft: New York, Cádiz, dates) |
| ELESP | SEC | El Español, 21 Feb 2026 (lily vases removed to the Patio) |
| TRV | SEC | trvlogue.com, updated 1 Oct 2026 (≈ 10 min up; exit Perdón) |
| WIKI-ES | WIKI | es.wikipedia.org/wiki/Catedral_de_Sevilla (read 30 Oct, plan) — **placement lead only, never alone**: south-wall chapel order; Cálices through the Capilla de los Dolores; Columbus near the Puerta de San Cristóbal; Giraldillo replica in front of that door. Every use carries an [Oxx]. |

Key: H = Highlights, E = Essential (E includes every H), "–" = Full only. [Oxx] = provisional wording that depends on ONSITE item Oxx. **NOT** = must not be said. FACTS § numbers refer to `research/FACTS_OCT2026.md`.

| # | Type | Section | @room | @title | Core content (corrected wording; **NOT** = do not say) | Sources | Cue to next (Spanish name + one thing to look for) | H/E |
|---|---|---|---|---|---|---|---|---|
| 001 | ANCHOR | Opening | Entrada · Puerta del Lagarto or Puerta del Príncipe | Welcome to the Catedral de Sevilla | Play once through the entrance check, standing aside [O1, O2]. One-paragraph arc: an Almohad mosque of the 1170s and its minaret; the cathedral of Seville from 1248; the Gothic church built after the chapter's decision of 1401 (story on the way down the tower, 006). "A World Heritage Site since 1987, with the Alcázar and the Archive of the Indies" (UNESCO). How this guide works: one route, three lengths (minutes from section 3, after O19); every stop named in Spanish, as on the signs, plus something to look for. **The cathedral's own visit begins at the Giralda** (SCHED), so this guide does too. A working cathedral: the Capilla Real is for prayer only and is seen from outside; chapels may close for Mass (NORMAS; the Aug 2026 Mass list, research §6). **One way through:** the way out is at the end, through the courtyard of orange trees; once out, you can't come back in (NORMAS) — say it as route advice, not as a rule about tickets. **Two entrance paragraphs:** (a) "If you came in by the Puerta del Lagarto, you walked under a crocodile hanging from the ceiling [O1]: its story comes at the end." (b) "If you came in by the Puerta del Príncipe, also called the Puerta de San Cristóbal, the monument near you, four heralds carrying a coffin, is the tomb of Columbus [O2, O12]. You'll come back to it." **One sentence for non-climbers** (NORMAS: ramps, no wheelchairs or strollers): "If you're not going up the tower, go to its door anyway and start at the stop called 'at the foot of the Giralda'." **NOT:** ticket types ("online", "ticket office"), prices, hours, time slots, the tower closing earlier, queues; "largest church in the world"; "they'll think us mad" (it is in 006, as tradition); the official audioguide. | UNESCO OFF · SCHED OFF · NORMAS OFF · HIGH OFF · BLDG OFF | Lagarto: "Head for the door into the Giralda, the tower, signed 'Giralda' [O1, O3]." Príncipe: "Cross the church to the Giralda: through the crossing, between the great gilded altarpiece behind its grille and the choir, into the opposite arm of the transept, and on by the Giralda signs to the tower door in the corner [O2, O3]." Both: "Start the next stop as you begin the climb: Giralda · ramps." | H E |
| 002 | W | La Giralda | Giralda · first ramps | Giralda — The minaret of 1184 | Heard at the foot or on the first ramps [O3, O4]. Ordered **1184** under the Almohad caliph **Abu Ya'qub Yusuf**, carried on under his son al-Mansur (§2.1); designed by **Ahmad ibn Baso** (§2.2); "a second master, Ali al-Ghumari, finished it in brick" (§2.3 HEDGE). **March 1198**: four huge gilded balls (the *yamur*) raised to the top (§2.4 HEDGE wording); the chronicler Ibn Sahib al-Salat: travellers saw it "as if suspended among the stars" (§2.6). The **1356 earthquake** brought the balls down (§1.6). After 1248 it became the cathedral's bell tower (§2.10); the Renaissance belfry you're climbing toward was added in the 1560s (§2.12). "A sister of the great Almohad minarets of Marrakesh and Rabat" (§2.27 HEDGE, stylistic only). "Close to a hundred metres to the tip of the weathervane" (§2.13 HEDGE). Copied across Spain and the Americas (§2.26, generic). Visual references only to the walls and ramps around you. **NOT:** "35 ramps", "stairs"; "built 1172–98 by al-Mansur"; a rider or king on horseback reaching the top; "tafaforas"; "same architect as the Koutoubia"; "first public clock in Spain"; city names for the copies. | ARAMCO SEC · TF OFF · ARCH SEC · HIST OFF · AHPS OFF · OVR OFF · UNESCO OFF | "Keep climbing, keeping to the right. The next stop is on the ramps themselves, a few turns up: Giralda · ramps." | H E |
| 003 | R | La Giralda | Giralda · ramps | Giralda — Thirty-four ramps | Heard while climbing [O4]. **34 ramps and 7 vaulted chambers** (§2.7, TF). The ramps were made **wide enough for a rider on horseback** (§2.8, GIR). Up and down share the ramps: keep right (NORMAS). Built with a double wall around a core (TF "double-walled tubular"); **more than 140 reused capitals and bases** in the tower (§2.23). **Restorers working from 2017 found builders' sketches scratched into the bricks, a kind of medieval sketchbook** (§2.23; DATED "recently"). Restoration of the four faces 2017–2023, openings and balconies 2025 (research §2). Say the sketches or capitals are visible only if O4 finds them. **NOT:** "35 ramps"; a number of steps at the top (UNVERIFIED); "a king rode up"; "the sketches are beside you" unless seen. | TF OFF · GIR OFF · NORMAS OFF | "At the top, walk out onto the bell level and round to the side that looks down on the courtyard of orange trees: Giralda · bell level [O5]." | H E |
| 004 | W | La Giralda | Giralda · bell level | Giralda — The view from the bells | You're in the **Renaissance belfry of Hernán Ruiz the Younger** (contract 17 Dec 1557; finished 1568) on top of the minaret (§2.12). **The view: only what O5 photographs**, each sight tied to a story told elsewhere: below, the **Patio de los Naranjos**, the mosque's courtyard, where the visit ends; the **roofs and domes of the cathedral** (the crossing dome collapsed in 1511, four years after the opening, §1.11); further landmarks only as O5 lists them (with no compass words until then). DATED: since April 2026 works on the bell chamber and the Renaissance crown; "visits are not interrupted" (PH6) — mention screens only if seen. DATED: storm Leonardo, **5 Feb 2026**: one of the four bronze lily vases at the belfry's corners fell; the other three were taken down on 21 Feb 2026 (§2.25; ELESP, VISITS). **NOT:** belfry exterior details as seen from here; the lily vases on the tower; the Giraldillo (026); landmarks O5 has not confirmed; "the official 360° panorama". | AHPS OFF · GIR OFF · HIST OFF · PH6 OFF · VISITS OFF · ELESP SEC | "There's a short Extra here on the bells. Then go back down the same ramps, keeping right; the next main stop plays on the way down: Giralda · on the way down [O6]." | H E |
| 005 | X | La Giralda | Giralda · bell level | Giralda · Extra · Twenty-four bells | **24 bells** (§1.17). The largest, **Santa María la Mayor**, nicknamed "la Gorda", cast **1588** by Juan de Balabarca, "over five tonnes" (§2.20 HEDGE). DATED: Phase VI is rebuilding six bell frames with damping and replacing the 2021 shoring of this bell (PH6). Bartolomé Morel, who cast the Giraldillo, also cast seven Giralda bells (§2.21 HEDGE, optional). Point to bells only as O5 finds them. **NOT:** ringing times, "you'll hear them at…"; weights of other bells. | HIST OFF · CAMP SEC · PH6 OFF · AHPS OFF | "Down the ramps, keeping right: Giralda · on the way down." | – |
| 006 | W | La Giralda | Giralda · on the way down | Giralda — From mosque to cathedral | Heard while descending [O6]: **no "look at" instructions**. **1172**: Abu Ya'qub Yusuf orders a great Friday mosque for Seville, the Almohads' capital in al-Andalus (§1.1, §1.3); the prayer hall went up in the 1170s; the minaret was finished in 1198 under his son (§1.2). **1248**: Fernando III takes Seville; the mosque becomes the cathedral and serves for 150 years (§1.4). **1401**: the chapter votes to build a new church (§1.7). Exact safe wording of §1.8: "Tradition says one canon put it like this: 'Let us build a church so great that those who see it finished will think we were mad.' The record of the chapter's decision is more sober: a church 'so good that there is none its equal.'" Building began in earnest in the 1430s (§1.9); finished 1506, opened **11 May 1507**, a century after the decision (§1.10). What the mosque left: this tower, the courtyard and its gate, where you'll leave. **NOT:** "the minutes record 'mad'"; "al-Mansur built the mosque 1172–98"; "the mosque was demolished in 1248". | HIST OFF · ARCH SEC · LECT OFF · OVR OFF | "At the bottom, step just inside the church, out of the way of the tower door: Catedral · at the foot of the Giralda [O7]." | H E |
| 007 | R | The heart of the cathedral | Catedral · at the foot of the Giralda | The nave — A hollow mountain | Sevillians call it a "hollow mountain" (§1.16). **UNESCO calls it "the largest Gothic building in Europe"**, with five naves; **Guinness lists it as the cathedral covering the greatest area** (§1.13). Why it's so wide and almost square: **it sits on the rectangle of the mosque** (§1.19). Orientation, compass-free [O7]: the tower stands in one corner; the **Capilla Mayor and the Coro fill the middle of the central nave**, facing each other; the **Capilla Real** closes the end of the church behind the Capilla Mayor; the **sacristies and chapter house** take up the corner on the far side of this same end; the route goes to the middle, round the church, and out through the courtyard. **NOT:** nave heights in metres; "third-largest church"; "largest church in the world"; north/south/left/right. | HIST OFF · UNESCO OFF · GUIN SEC · ARCH SEC · BLDG OFF · REN OFF | "Walk to the middle of the church, where the transept crosses the nave, and face the huge gilded altarpiece behind the iron grille: the Capilla Mayor [O7, O8]." | E |
| 008 | W | The heart of the cathedral | Capilla Mayor | Capilla Mayor — The Retablo Mayor | Begun **1482** under the Flemish sculptor **Pieter Dancart** (§6.1). First phase to **1529** (after Dancart a Flemish master 1497–1505, Pedro Millán, Jorge and Alejo Fernández); side sections from **1550** (Roque Balduque, Juan Bautista Vázquez, Pedro de Heredia); **finished 1564**: "eighty-two years from first cut to last gilding" (§6.2). **Nearly 30 m high, almost 20 m wide** (§6.3). "**Often called** the largest altarpiece in the Christian world" (§6.4, OFF "considered"). **44 reliefs and more than 200 figures**, plus 8 reliefs of the Kings of Israel and Judah (§6.5). The crucifix at the top: the "**Christ of the Million**" (§6.6). Restored and re-gilded 2012–2014 (§6.7). Seen through the grilles. **NOT:** "tons of gold"; "over a thousand figures"; "the largest in the world" as fact; the guided tour that goes inside. | BLDG OFF · HIST OFF | "There's a short Extra here on the iron grilles. Then turn round: facing the altarpiece across the crossing is the Coro, the choir, behind its own Renaissance grille, with organ pipes rising above it [O8]." | H E |
| 009 | X | The heart of the cathedral | Capilla Mayor | Capilla Mayor · Extra · The iron grilles | "The gilded iron screens were made in the 1520s and 30s, largely by the Dominican friar **Francisco de Salamanca** and other Seville ironworkers" (§6.9 HEDGE); Salamanca was summoned in 1518; the high-altar pulpits are his (1531) (WILL, HEDGE). His choir grille of 1518–23 is the one you'll see next (§7.1). Describe only the grilles and pulpits O8 confirms. **NOT:** exact dates or makers for each Capilla Mayor grille; "solid gold". | WILL SEC · BLDG OFF | "Turn round to the Coro: the choir behind its Renaissance grille [O8]." | – |
| 010 | W | The heart of the cathedral | Coro | Coro — The choir and the organs | Walled except at the front, where **Fray Francisco de Salamanca's grille, 1518–1523**, faces the altar (BLDG, §7.1); crest with a Tree of Jesse (research). **117 carved seats in two tiers**, Gothic-Mudéjar; the misericords show the vices (§7.2) — "look for" only if O8 finds them visible. The **King's chair signed Nufro Sánchez, 1478**; **Dancart**, the altarpiece's first master, carried on from 1479 (§7.3). The great **lectern, 1562–65**, with bronzes by **Bartolomé Morel**, the founder of the Giraldillo (§7.4). The **twin organs, finished 1903**, adapted electronically in 1973 (§7.5). In **1888 a pillar beside the choir gave way** and was rebuilt (§1.12). **NOT:** the organ builder's name; a date for the trascoro. | BLDG OFF · HIST OFF | "Walk along the side of the choir, in the side aisle on the side where you came down from the tower, and on toward the far end of the church, to the Capilla de San Antonio: the chapel with Murillo's huge canvas of a kneeling saint and a cloud of angels [O9]." | E |
| 011 | W | Around the naves | Capilla de San Antonio | Capilla de San Antonio — Murillo's Saint Anthony | The cathedral's **baptistery chapel** (GLASS "Capilla del Bautismo"). **Murillo, *Vision of St Anthony of Padua***, set on this altar **21 Nov 1656** (§12.1); above it Murillo's ***Baptism of Christ***, 1667 (§12.2). **The theft:** in **November 1874** someone cut the kneeling saint out of the canvas (§12.4); in **January 1875** a stranger offered it in **New York** to the dealer **William Schaus** for **250 dollars**; Schaus called the Spanish consul, the seller was arrested, and Schaus handed it over at cost (§12.5); it came back via Havana and Cádiz and was set back in the same year (§12.6). "You can still make out the outline" only if O9 sees it. Two Jordaens canvases (1669) here (§12.7, optional). The stained-glass Santas Justa and Rufina in this chapel (§10.10 HEDGE; GLASS) as a hook for Goya later. **NOT:** the restorer's name as fact; "stolen by Napoleon's troops"; the seam "clearly visible" unless seen. | FERRER SEC · GLOBE SEC · 3CAT SEC · PAINT OFF · GLASS OFF | "Walk on to the far end of the church, where the great central doors stand: the Puerta de la Asunción, seen from inside [O10]." | E |
| 012 | R | Around the naves | Puerta de la Asunción · west end, inside | West end — The oldest windows and the great doors | The **Puerta de la Asunción**, centre of the west front (BLDG): completed only in the 19th century (1827–1833, Fernando Rosales; the sculptures outside by Ricardo Bellver) and opened for ceremonies, not for visitors (research row 18). **The windows:** the openings in the western half of the church and in the central nave belong to the oldest phase of building; the three west-front windows are by Vicente Menardo (GLASS). Looking back east, the length of the church: "some 126 metres" (GUIN, §1.13). **Hernando Colón**, Columbus's son, is buried in this cathedral (§8.20); his gravestone in the nave floor and its inscription **only if O10 finds and reads it** (HEDGE). **NOT:** Bellver's sculptures "behind you" (they're outside); dates for Menardo; Hernando's stone or its inscription unless O10. | BLDG OFF · GLASS OFF · GUIN SEC · AHPS-G SEC | "Along the far side of the church from the tower, to the Capilla de la Antigua: the largest chapel on that side, its medieval painted Virgin above the altar; the chapel names are over the grilles [O11]." | – |
| 013 | W | Around the naves | Capilla de la Antigua | Capilla de la Antigua — The Virgin who stayed | **Virgen de la Antigua**: a **14th-century wall painting**, anonymous, with Sienese influence (§13.1): older than the cathedral around it. Kept when the old building came down; the chapel's enlargement began in **1504** (§13.2). **Legend** says the Virgin appeared to Fernando III during the siege (§13.3). Tomb of **Cardinal Diego Hurtado de Mendoza**, placed 1510 (§13.4). Crowned **1929** (§13.5). **Columbus named the Caribbean island of Antigua after the Virgin venerated here** (§13.6 HEDGE, Britannica wording). Copies spread across Andalusia and Latin America (§13.7). San Fernando window (GLASS, optional). One sentence: if a Mass is on, listen from outside the grille (§13.8). **NOT:** Fancelli as sculptor; "Columbus prayed here before sailing"; "the Virgin saved the city". | PAINT OFF · BBVA SEC · HIST OFF · BRIT SEC · GLASS OFF | "On along this side to the south arm of the transept: the tomb of Columbus, four heralds carrying a coffin on their shoulders, just inside the Puerta del Príncipe [O12]." | E |
| 014 | W | Columbus | Sepulcro de Cristóbal Colón · south transept | Sepulcro de Colón — Four heralds | By **Arturo Mélida**, who won the 1891 competition for a tomb in **Havana** Cathedral (§8.1); installed there **19 Mar 1898** (§8.2). After the war of 1898 the remains left Havana (12 Dec 1898) and reached Seville in **January 1899** (§8.3); **the monument was set up here in 1902** (§8.4). **Four heralds for the kingdoms of Castile, León, Aragon and Navarre** carry the coffin (§8.5); Mélida's own reading (§8.6, optional). Why he's raised up: it was designed for Havana's crossing (§8.9). Custom, framed as custom: touching a herald's foot (§8.10, optional). The pomegranate on a lance tip only after O12 (§8.7). The door beside it: the **Puerta del Príncipe, also called the Puerta de San Cristóbal**, built in Gothic style by Adolfo Fernández Casanova (BLDG, research row 20). **NOT:** "the remains came in 1902"; heralds looking up/down for supporters/opponents; "he swore never to lie in Spanish soil" as fact. | OHC SEC · HIST OFF · UPO26 SEC · BLDG OFF | "Stay here for the bones themselves: Sepulcro de Colón." | H E |
| 015 | W | Columbus | Sepulcro de Cristóbal Colón | Sepulcro de Colón — Whose bones? | "Columbus travelled more dead than alive": Valladolid 1506, the Cartuja in Seville, Santo Domingo, Havana, back to Seville (§8.11 HEDGE, no exact dates beyond 1506 and 1898–99). **1877**: a lead box inscribed for Columbus found in Santo Domingo; the Dominican Republic says it has him too (§8.12). University of Granada (J. A. Lorente): 2003–05 "possible compatibility" (§8.13); **May 2006** mitochondrial DNA matched his brother Diego (§8.14); **Oct 2024** Lorente said the Seville bones are Columbus's, compared with his son **Hernando** and brother Diego; not peer-reviewed (§8.15). Only **part** of a skeleton is here; the Santo Domingo remains have never been tested (§8.16–17). **Safe line (§8.19), verbatim in substance.** Origin claims made on television in 2024 "have not been published scientifically" (§8.18). **Hernando**, the bibliophile, lies in this cathedral (§8.20); his books, some owned by his father, "for the use and benefit of all his fellow men" (BIB §5.4–5.5) — the library is not on the visit. **NOT:** "DNA proved he was a Sephardic Jew / Spanish"; "his whole body is here"; percentages; "Columbus and his son Diego are buried here". | OHC SEC · UPO26 SEC · AP06 SEC · EFE24 SEC · ALJ SEC · AHPS-G SEC · BIB OFF | "Into the sacristies: along this side aisle, away from the great west doors, to the Capilla de los Dolores and through it into the Sacristía de los Cálices — look for Goya's tall painting of two saints with a lion at their feet and the Giralda behind them [O13]." | E |
| 016 | W | Sacristies and chapter house | Sacristía de los Cálices | Sacristía de los Cálices — Goya's potter saints | **Goya, *Santas Justa y Rufina*, 1817**, over three metres tall (309 × 177 cm) (§10.1). Commissioned through his friend **Ceán Bermúdez**, who chose the subject and asked for the saints "in decorous postures" (§10.2); paid 28,000 reales; delivered 14 Jan 1818 (§10.3). Look for: potters' vessels, a **lion licking Rufina's feet**, a broken pagan idol, and **the Giralda behind them** (§10.4). **Legend:** Sevillians believe the two saints held the tower up in the earthquake of 1504 (§10.5). Local artists resented the commission (§10.7). The rumour about models: "a later rumour, never proved" or omit (§10.6). Juan Núñez panel, c.1480, in the same room (§10.8, if O13 sees it). **NOT:** Zurbarán in this room; "prostitutes" as fact. | GOYA SEC · HIST OFF · CT SEC · PAINT OFF | "There's a short Extra in the Sala del Pabellón, the exhibition room [O13]. The next main stop is the Sacristía Mayor, the great domed sacristy: look up at a dome carved in rings of figures [O13]." | E |
| 017 | X | Sacristies and chapter house | Sala del Pabellón | Sala del Pabellón · Extra · Zurbarán and a visiting El Greco | The exhibition area (research row 10; location O13, ALT-G). **Two Zurbaráns** (1635–45; 1645–50), two Valdés Leal, Pacheco 1620 (PAINT) — **titles only as on the labels** (O13). DATED: **El Greco's *Santa María Magdalena***, on loan from the parish of San Eutropio in Paradas while that church is restored, shown here since about January 2026 (GRECO) — only if O13 finds it. **NOT:** titles not on labels; Artemisia Gentileschi ("en restauración"); Zurbarán "in the Cálices". | PAINT OFF · GRECO OFF | "On to the Sacristía Mayor: the great domed room, with a dome carved in rings of figures [O13]." | – |
| 018 | W | Sacristies and chapter house | Sacristía Mayor | Sacristía Mayor — Campaña's Descent | **Pedro de Campaña**, a Flemish painter working in Seville, ***Descent from the Cross*, 1547** (§9.3; OFF date, not c.1570), hanging "in front of the central chapel" (REN) — that's where to look [O13]. Painted for a chapel in the parish church of **Santa Cruz**, which the French demolished in **1810** (§9.4). An 18th-century writer tells how **Murillo** would stand before it, saying he was waiting "until they finish taking Our Lord down from the cross" (§9.5 HEDGE, Ponz). Murillo was buried in that same church (§9.6). **NOT:** "c.1570"; Murillo "buried beneath this painting" as fact. | PAINT OFF · REN OFF · GEIIC SEC · MUR SEC | "There's a short Extra here on the dome and two bishops by Murillo. The next main stop is in this room too: the great silver monstrance, the Custodia de Arfe [O13]." | E |
| 019 | X | Sacristies and chapter house | Sacristía Mayor | Sacristía Mayor · Extra · A dome of the Last Judgment | Greek-cross plan, dome on pendentives; **the whole dome is the Last Judgment, in three rings** (§9.1). Used as an exhibition space for almost 200 years (§9.2). **Murillo, *San Isidoro* and *San Leandro*, 1655** (§9.7). Statue of **San Fernando**, made for his 1671 canonisation, and an Immaculate on facing pillars (§9.15). Only what O13 sees. **NOT:** the keys of Seville (§9.14). | REN OFF · PAINT OFF | "The Custodia de Arfe, the tall silver monstrance, in this room [O13]." | – |
| 020 | W | Sacristies and chapter house | Sacristía Mayor | Sacristía Mayor — The Custodia de Arfe | **Juan de Arfe y Villafañe, 1580–1587**; "considered the best of its kind" (GOLD: attribute it) (§9.8). Still **carried through the streets at Corpus Christi** (§9.9). "Taller than a person" (no figures, §9.10). The cathedral holds about **900 gold and silver pieces** (§9.12); name other pieces only if O13 sees them (§9.13). **NOT:** height, weight or "three tons"; the crowning figure swap (§9.11); "Tablas Alfonsíes, Alfonso X's gift" as fact. | GOLD OFF · TERAMO SEC | "Through the Antecabildo, the antechamber, and along the curved corridor to the Sala Capitular: the oval chapter house, with Murillo's Virgin presiding over a ring of round paintings [O13]. There's a short Extra on the room itself first." | E |
| 021 | X | Sacristies and chapter house | Sala Capitular | Sala Capitular · Extra · An oval for the chapter | You came through the Antecabildo and a curved corridor (REN; §11.6). An **elliptical** chapter house, begun under **Hernán Ruiz II** — the architect of the Giralda's belfry — and completed by **Asensio de Maeda** (§11.1). The programme and Latin inscriptions by **Canon Francisco Pacheco** (§11.2). The Cathedral says the oval gives clear sightlines and "exceptional acoustics" (§11.3). **Pablo de Céspedes**, Virtues, 1592; reliefs by Vázquez el Viejo, Diego de Velasco and Marcos Cabrera; Velasco's armchair, 1592 (§11.4). The chapter that met here is the body that voted in 1401 (§1.7). **NOT:** "test the echo"; contents of the Antecabildo (none sourced). | REN OFF · HIST OFF | "Stay here: Murillo's Immaculate, above the ring of round paintings." | – |
| 022 | W | Sacristies and chapter house | Sala Capitular | Sala Capitular — Murillo's Immaculate | **Murillo, *Immaculate Conception***, commissioned **1667**, painted 1667–68 (§11.5), presiding over **eight saints of Seville on round canvases** (REN). Murillo's cathedral, as a thread: the *San Isidoro* and *San Leandro* next door (1655), *St Anthony* (1656), and works in other chapels listed by the Cathedral (PAINT: Ángel de la Guarda 1665–66; Capilla de Santiago 1674) — name chapels without directions. Campaña's *Descent*, which Murillo admired (callback 018). **NOT:** "1662"; names of the eight saints unless O13 reads labels; Murillo biography not in FACTS. | REN OFF · PAINT OFF · MUR SEC | E: bridge. Full: "Back into the church and to its far end, behind the Capilla Mayor: the Capilla Real, the Royal Chapel, behind its great iron grille [O13, O14]." | E |
| 023 | W | Royal chapel and the way to the courtyard | Capilla Real · outside the grille | Capilla Real — The king who took Seville | **Worship only; seen from outside the grille** (NORMAS). It "occupies the head of the temple" (REN). Designed by **Martín de Gainza from 1551**; dome finished about **1568 by Hernán Ruiz II**; lantern rebuilt after a 1754 collapse (§14.1). The **Virgen de los Reyes**, a 13th-century Gothic image "of French origin" (§14.2; the gift of St Louis is LEGEND). Tombs of **Alfonso X** and his mother **Beatriz of Swabia**; in the crypt Pedro I and María de Padilla (§14.3). The **silver urn of San Fernando** by Laureano de Pina, after 1671 (§14.4) — Fernando III, who took Seville in 1248 (§1.4). The **entrance grille, 1771**, paid for by Charles III (§14.5). DATED: reopened **18 Feb 2026** after restoration (§14.6). ALT-F: "look through the grille" vs "behind the grille, which is often closed" [O14]. **NOT:** "walk in" or "visit at Mass times" with times; the crypt as visible; St Louis's gift as fact. | REN OFF · GOLD OFF · HIST OFF · NORMAS OFF | "To the courtyard: the north arm of the transept, on the side where you came down from the tower, and the Puerta de la Concepción, under a tall window of the Ascension [O15]." | – |
| 024 | R | Royal chapel and the way to the courtyard | Puerta de la Concepción · north transept | Puerta de la Concepción — Back to the mosque's courtyard | The door "on the north front of the transept" that "opens onto the Orange Tree Courtyard" (BLDG); finished only in modern times by **Adolfo Fernández Casanova**, who also built the Puerta del Príncipe (BLDG; **no date spoken**: 1887 vs 1917 conflict). Above it, the **Ascension** window (GLASS); the transept's saints windows by Arnao de Flandes (GLASS). DATED, only if O15 finds it back: the **Altar de Plata**, Juan Laureano de Pina, 1688, normally in this arm of the transept, restored 2025–26 (PLATA, GOLD). Through this door, the mosque's courtyard (callback 006). ALT-D: if visitors use another door, the cue says "follow the Salida signs". **NOT:** 1887 or 1917; the Altar de Plata unless seen. | BLDG OFF · GLASS OFF · PLATA OFF · GOLD OFF | "Out into the Patio de los Naranjos: rows of orange trees around a fountain [O15, O16]." | – |
| 025 | W | Patio de los Naranjos | Patio de los Naranjos | Patio de los Naranjos — The mosque's courtyard | **The mosque's ablutions courtyard**, where worshippers washed before prayer; original pillars and pointed horseshoe arches survive (§3.1). Three galleries once; the west one was demolished for the **Sagrario** church, 1618–1662 (§3.2). Orange trees in a grid, linked by **channels that still carry water** (§3.3). The fountain: modern, but "the upper bowl is Visigothic" (§3.4, Cathedral's wording). The tower above you was this mosque's minaret (callback 002). DATED, only if O16 sees them: the three lily vases taken down in Feb 2026, on supports here for study (§3.11). **NOT:** "Roman fountain"; the Sagrario as part of the visit; toilets. | PATIO OFF · ARCH SEC · HIST OFF · ELESP SEC | "Find a spot where you can see the top of the Giralda: Patio de los Naranjos · the Giraldillo [O16]." | H E |
| 026 | R | Patio de los Naranjos | Patio de los Naranjos · view of the Giralda | Patio de los Naranjos — The Giraldillo | Look up [O16; ALT-C]. **The Giraldillo**, "the little thing that turns": a **four-metre bronze of Faith Triumphant**, about 1,500 kg, a working weathervane, and the figure that gave the tower its name (§2.14). Cast by **Bartolomé Morel** (contract 27 Aug 1566), probably to a design by **Luis de Vargas** (§2.15); hoisted **13 Aug 1568** (§2.12). Probably modelled on a print of the goddess Athena (§2.16 HEDGE). Restored many times (§2.19, optional); taken down for study in 1998 and **put back on 22 July 2005**: the one on top is the original (§2.17). A full-size replica stands outside the Puerta del Príncipe (§2.18 HEDGE; O12). Morel also cast the choir lectern's bronzes (callback 010). **NOT:** "the one on top is a copy"; "made by Juan Bautista Vázquez". | AHPS OFF · GIR OFF · IAPH SEC | "To the covered gallery along the side of the courtyard nearest the tower: the Nave del Lagarto, with a crocodile hanging from its ceiling [O17]." | – |
| 027 | R | Patio de los Naranjos | Nave del Lagarto | Nave del Lagarto — A crocodile, a tusk and a giraffe | Hanging overhead: a crocodile (the "lagarto"), an elephant tusk, a rod and a bridle (§4.1) [O17]. **The chronicle of Alfonso X** records an embassy of the Mamluk Sultan of Egypt, c.1260, bringing "un marfil" (an ivory tusk), a giraffe and a zebra (§4.2). **Tradition** adds a Nile crocodile; the 17th-century annalist Ortiz de Zúñiga says its stuffed body hung here (§4.3). **What you see today is a wooden copy** (§4.4 HEDGE). The rod and bridle: named, no story (§4.6–4.7). Above this gallery is **Hernando Colón's library**, not open on the visit (§5.1, §5.6). ALT-H if the gallery is closed off. **NOT:** "the original stuffed crocodile"; the bridle "of the giraffe" as fact; the marriage-proposal story as fact; directions to the library. | UPO24 SEC · RUIZ SEC · PATIO OFF · BIB OFF | "Last stop: the Puerta del Perdón, the tall arched gateway in the middle of the far side of the courtyard, opposite the cathedral [O18]." | – |
| 028 | CLOSE | Closing | Puerta del Perdón | Puerta del Perdón — The way out | An **original Almohad gate**, the mosque courtyard's main entrance, **aligned with the mosque's central nave and its mihrab** (BLDG); carved plaster inside the arch (§3.5). Christian figures added in the 1520s: terracottas by **Miguel Florentín, 1520**; Plateresque plasterwork by **Bartolomé López, 1522** (§3.6); the relief of the **Expulsion of the Merchants** above the arch (BLDG) — which face, O18. DATED, optional: recorded in 3D by the Factum Foundation with the Cathedral, Nov 2025 (FACTUM). Recap of the layers: minaret, courtyard and gate from the mosque; the Gothic church; the Renaissance sacristies, chapter house and belfry. **The roofs** can be walked on a separate guided visit (ROOF; no price, booking or times). Once through, the visit is over (NORMAS). **NOT:** the doors' bronze cladding or knockers with a date (§3.8); "Perdón = an indulgence" (§3.9); St Vincent Ferrer (§3.10); the Salvador church or what the ticket includes. | BLDG OFF · FACTUM SEC · RECIO SEC · ROOF OFF · NORMAS OFF | — | H E |

The H/E column matches the membership lists in section 3.

**Held (not in the guide; restore only with a source or an ONSITE photo):** Hernando Colón's gravestone X at the west end (O10: position and legible inscription; content §5.2–5.5, §8.20) · Altar de Plata X in the north transept (O15: back in place?) · Sala del Tesoro (antigua Contaduría) X (O13: what is on show; §9.13) · Chapels of the north aisle R (S021: Santiago, Belén, Evangelistas, Ángel de la Guarda — OFF painting list; MAP-1 must place them) · Artemisia Gentileschi X (if back from restoration) · Biblioteca Colombina (not on the visit; never a stop).

## 3. Lengths

Midpoints: W 300 · R 230 · X 190 · ANCHOR/CLOSE 320 words, at 125 words/min. **Walking and climbing** are my estimates at visitor pace in crowds; with no map they are rough and need the stopwatch walk (O19). **Overlap:** 002 and 003 are heard on the ascent and 006 on the descent, so their listening time is already inside the climb and is subtracted once.

### Walking and climbing estimate by segment (minutes)
| Segment | Full | E | H |
|---|---|---|---|
| Entrance → Giralda door (Lagarto ≈ 1–2; Príncipe ≈ 3–4) | 3 | 3 | 3 |
| Tower access control / wait | 2 | 2 | 2 |
| Ascent, 34 ramps (≈ 10 min, TRV) | 10 | 10 | 10 |
| At the top beyond the tracks (round the four sides) | 2 | 2 | 2 |
| Descent | 6 | 6 | 6 |
| Foot of the tower (inside) → crossing | 2 | 2 | 2 |
| Crossing → San Antonio (north aisle) | 2 | 2 | – |
| San Antonio → west end → Antigua | 3 | 3 | – |
| Antigua → Columbus (south transept) / H: crossing → Columbus | 1 | 1 | 1 |
| Columbus → Dolores → Cálices | 1 | 1 | – |
| Cálices → (Pabellón) → Sacristía Mayor | 2 | 1 | – |
| Sacristía Mayor → Antecabildo → corridor → Sala Capitular | 2 | 2 | – |
| Sala Capitular → Capilla Real → north transept (E: Sala Capitular → north transept → Patio) | 4 | 4 | – |
| North transept → Patio (H: Columbus → north transept → Patio) | 1 | – | 2 |
| Patio → Nave del Lagarto → Perdón (E, H: Patio → Perdón) | 2 | 1 | 1 |
| **Total** | **≈ 43** | **≈ 40** | **≈ 29** |
| of which the Giralda (wait, up, top, down) | 20 (+ 3.9 listening at the top in Full; 2.4 in E/H) | 20 | 20 |

The tower takes ≈ 22–24 min in all with the top-level tracks, inside the skeleton's "≈ 20–30 min up and down".

### Counts
| Version | Tracks | W | R | X | ANCHOR+CLOSE | Words | Listening | Walking + climb | Overlap | **Visit** |
|---|---|---|---|---|---|---|---|---|---|---|
| Full | 28 | 15 | 6 | 5 | 2 | ≈ 7,470 | ≈ 59.8 min | ≈ 43 | − 6.6 | **≈ 96 min (96–102)** |
| Essential | 18 | 14 | 2 | 0 | 2 | ≈ 5,300 | ≈ 42.4 min | ≈ 40 | − 6.6 | **≈ 76 min** |
| Highlights | 9 | 6 | 1 | 0 | 2 | ≈ 2,670 | ≈ 21.4 min | ≈ 29 | − 6.6 | **≈ 44 min** |

**Full is ≈ 96 min, not 110.** The skeleton's 9,000 words assumed more sourced, placeable content than exists, and ignored that the climb can carry three tracks. Ways to close the gap (lead's call):
- (a) restore held items as ONSITE allows: Hernando's gravestone, Altar de Plata, Sala del Tesoro, north-aisle chapels (+≈ 1.5–1.8 min each, ≈ +7 min) → ≈ 103;
- (b) let Full-only R tracks with rich sources (026 Giraldillo, 027 Lagarto) run to the top of the R range (+≈ 1 min);
- (c) accept ≈ 100 min and have 001 say "about an hour and three-quarters" for the full route (after O19);
- don't pad.

### Highlights (9 tracks, ≈ 2,670 words)
| # | @room | Type | Words |
|---|---|---|---|
| 001 | Entrada · Puerta del Lagarto or Puerta del Príncipe | ANCHOR | 320 |
| 002 | Giralda · first ramps | W | 300 |
| 003 | Giralda · ramps | R | 230 |
| 004 | Giralda · bell level | W | 300 |
| 006 | Giralda · on the way down | W | 300 |
| 008 | Capilla Mayor | W | 300 |
| 014 | Sepulcro de Cristóbal Colón · south transept | W | 300 |
| 025 | Patio de los Naranjos | W | 300 |
| 028 | Puerta del Perdón | CLOSE | 320 |

### Essential (18 tracks, ≈ 5,300 words). Every Highlights track plus:
| # | @room | Type | Words |
|---|---|---|---|
| 007 | Catedral · at the foot of the Giralda | R | 230 |
| 010 | Coro | W | 300 |
| 011 | Capilla de San Antonio | W | 300 |
| 013 | Capilla de la Antigua | W | 300 |
| 015 | Sepulcro de Cristóbal Colón | W | 300 |
| 016 | Sacristía de los Cálices | W | 300 |
| 018 | Sacristía Mayor | W | 300 |
| 020 | Sacristía Mayor | W | 300 |
| 022 | Sala Capitular | W | 300 |

Full order of Essential: 001 002 003 004 006 007 008 010 011 013 014 015 016 018 020 022 025 028.
Full order of Highlights: 001 002 003 004 006 008 014 025 028.

**Membership changes from the skeleton**, all for time:
- Highlights loses S015 Sacristía Mayor (≈ 2.4 min + ≈ 3 min walking) and S020 San Antonio (≈ 2.4 + ≈ 4); it gains 003 and 006, heard while walking the tower (no added time).
- Essential loses S023 Concepción (024, ≈ 1.8 min); it gains 006 (no added time), 013 Antigua (≈ 3.4 with walking) and 015 Columbus's bones (2.4).
- If O19 comes in shorter than estimated, add back in this order: H 018 Sacristía Mayor (+≈ 5 min); E 023 Capilla Real (+≈ 3 min).

### Bridges (spoken "next stop" lines for the shorter versions; writers draft them later)
A bridge is appended after the track's normal cue in that version; the track itself is unchanged, so every bridge must make sense right after the normal cue ("On this shorter tour, skip…: …"). A bridge is needed only where the next track in that version is not the Full cue's next main stop. Extras need no bridge. Every bridge inherits its cue's [Oxx] tags.

| Track | Version | Next in that version | Bridge destination (Spanish name + thing to look for) |
|---|---|---|---|
| 006 | H | 008 | From the foot of the tower straight to the middle of the church, where the transept crosses the nave: the huge gilded altarpiece behind the iron grille, the Capilla Mayor (007 skipped) [O7, O8] |
| 008 | H | 014 | From the crossing into the arm of the transept on the far side from the tower: the tomb of Columbus, four heralds carrying a coffin, just inside the Puerta del Príncipe (009–013 skipped) [O8, O12] |
| 011 | E | 013 | Past the great west doors and along the far side of the church to the Capilla de la Antigua: the largest chapel on that side, its medieval painted Virgin above the altar (012 skipped) [O10, O11] |
| 014 | H | 025 | Back through the crossing to the arm of the transept on the tower's side, and follow the Salida signs into the Patio de los Naranjos: rows of orange trees around a fountain (015–024 skipped) [O15, O16] |
| 022 | E | 025 | Back into the church and to the arm of the transept on the side where you came down from the tower; follow the Salida signs into the Patio de los Naranjos: rows of orange trees around a fountain (023–024 skipped) [O13, O15, O16] |
| 025 | E, H | 028 | To the Puerta del Perdón, the tall arched gateway in the middle of the far side of the courtyard, opposite the cathedral (026–027 skipped) [O18] |

**Never-skip rule:** 001 (both entrances, the Giralda first, the non-climbers' line) and 028 (the way out) are in all three lengths. The 014 H bridge carries the only route instruction Highlights gets between Columbus and the courtyard: record it only after O15.

## 4. NEVER

**Never send people:**
- into the **Capilla Real** (worship only: "seen through the grille", never "walk in"; no Mass times);
- to the **Biblioteca Colombina** (not on the cultural visit);
- out of the cathedral and back in (no re-entry), e.g. to see the Giraldillo replica outside the Puerta del Príncipe;
- through the **Puerta de la Asunción** (ceremonial);
- into a chapel during a Mass (Antigua, Capilla Real, Altar de Plata);
- up to the **roofs** (separate guided visit: mention only, in 028);
- to the **Salvador** church, the shop, toilets or the ticket office.

**Never in speech:**
- prices, hours, ticket types ("online", "ticket office"), booking, time slots, queues, security, bags, the free Sunday visit, the tower's earlier closing;
- the official audioguide, its numbers, or any numbering of chapels;
- left/right, "straight ahead", compass words, distances or "next to" that section 1 does not allow or MAP/ONSITE has not confirmed;
- "next track";
- "look at…" instructions in 002, 003 (beyond walls and ramps) and 006;
- "on this day" / "this year" hooks (DATED sentences only, cuttable);
- cross-tour assumptions ("as you saw at the Alcázar").

**Banned claims** (FACTS §17 and the table):
- "They'll think us mad" as the minutes' wording (it is tradition; §1.8).
- "Largest church in the world" / "third-largest church".
- "The mosque was built 1172–98 by al-Mansur".
- Stairs; "35 ramps"; a number of final steps; "a king (or muezzin) rode a horse to the top".
- "Tafaforas"; "same architect as the Koutoubia"; "first public clock in Spain".
- "The Giraldillo on top is a copy"; "made by Juan Bautista Vázquez".
- The lily vases "on the tower"; belfry details "as you can see" without O5.
- "Columbus's remains came in 1902"; "Columbus and his son Diego are buried here".
- "DNA proved he was a Sephardic Jew / Spanish"; "his whole body is here"; percentages of the skeleton.
- The heralds looking up/down for supporters/opponents; "he swore never to lie in Spanish soil".
- The pomegranate on the lance, unless O12 sees it.
- "The crocodile is the stuffed original"; the bridle "of the giraffe" as fact; the marriage proposal as fact.
- "Goya used prostitutes as models".
- "Zurbarán hangs in the Sacristía de los Cálices"; "Artemisia's Magdalene is on display".
- "Campaña's Descent, c.1570"; "Murillo is buried beneath it".
- "Over a thousand figures" / "tons of gold" on the Retablo.
- Custodia height or weight; "the keys of Seville on display"; "Tablas Alfonsíes, Alfonso X's gift" as fact.
- Exact dates or makers of the Capilla Mayor grilles; the organs' builder; nave heights in metres.
- Puerta de la Concepción "1887" or "1917" as certain.
- The Perdón's doors as Almohad bronze with a date; "Perdón = indulgence"; St Vincent Ferrer's pulpit.
- The Virgen de los Reyes as a gift of St Louis; Fancelli as Mendoza's sculptor; "Columbus prayed in the Antigua before sailing".
- "You can see where the canvas was cut" unless O9 sees it.
- St Anthony's restorer's name as fact.

## 5. ONSITE + MAP checklist (also in `v5/ONSITE_CHECKLIST.txt`)

**MAP (desk, as soon as the paper plan arrives; save it in `research/map/`):**
- **MAP-1 CRITICAL — The plan.** Get the plan/leaflet handed out at the doors or shown in the official app (the user has been asked for a photo). Is it given out on paper? Does it name the chapels? Does it number them, and do the numbers match signs in the building? (We still won't speak numbers.) If it places the north-aisle chapels, restore the held R.
- **MAP-2 — Read off every relation the cues need:** the Lagarto entry path into the church; the Príncipe entry and where Columbus's tomb is; the Giralda door; crossing, Capilla Mayor, Coro; San Antonio's position along the north aisle; the west end; the Antigua; Dolores → Cálices; the Sala del Pabellón; the Sacristía Mayor's door; Antecabildo → corridor → Sala Capitular; the Sala del Tesoro; the Capilla Real grille; the door into the Patio; the Nave del Lagarto; the Perdón; any one-way arrows and ENTRADA/SALIDA labels. Then rewrite the [Oxx] cues with left/right where the plan is unambiguous.
- **MAP-3 — Service icons** (lifts, toilets): positions for step-free notes only.

**ONSITE (one walk of the Full route with the guide before recording):**
- **O1 CRITICAL** — Puerta del Lagarto entry (001): the path after the check; does it pass under the crocodile in the Nave del Lagarto? Which door into the church? Where to stand for 001 without blocking? How far, and how signed, is the Giralda door?
- **O2 CRITICAL** — Puerta del Príncipe entry (001; ALT-A): where to stand for 001; is Columbus's tomb in sight? **Are Príncipe entrants sent to the Giralda first, free to choose, or made to do it last?** (Ask staff; read the signs.) Can they walk through the crossing to the tower door?
- **O3 CRITICAL** — The Giralda door (001–002): position (NE corner inside); access control and waiting spot; can 002 be started at the foot; same door up and down? Sign wording ("Giralda"? "Torre"?).
- **O4** — The ramps (002–003): time the ascent; ramp numbering on the walls?; the chambers visible?; steps at the very top?; are builders' sketches or reused capitals visible or labelled?; can people listen while climbing (noise, crowding)?
- **O5 CRITICAL** — The bell level (004–005, 026): Phase VI screens or scaffolding; which sides are open; **photograph the view from each side and list the landmarks** (the Patio below? the cathedral roofs and domes? the Alcázar? others); which bells can be seen; is the Giraldillo visible from here?
- **O6** — The descent (006): time it; can people listen while walking down?
- **O7** — The foot of the tower inside (006–007): where visitors come out; what is in view (the Capilla Real grille? the crossing?); the way to the crossing.
- **O8 CRITICAL** — The crossing (007–010): can listeners stand facing the Capilla Mayor's grille? Barriers or chairs? Which grilles and pulpits are visible? Is the coro's grille opposite? Organ pipes visible above the choir? Misericords visible?
- **O9** — Capilla de San Antonio (010–011): how far along the north aisle toward the west doors; grille open? The Murillo visible; the outline of the cut visible?; the *Baptism* above; the font; the Justa and Rufina window; the Jordaens.
- **O10** — The west end (011–012): the Puerta de la Asunción from inside; the west windows; **Hernando Colón's gravestone** (where; inscription legible?) → held X; is the area open?
- **O11** — Capilla de la Antigua (012–013): on the south side, west of the Príncipe door (WIKI-ES only)? The largest chapel on that side? Open or roped off? The wall painting visible; Mendoza's tomb; the San Fernando window.
- **O12** — Columbus (001, 013–015, 026): exact position relative to the Príncipe door; visible from the crossing?; a pomegranate on a lance tip?; any panel on the DNA; the Giraldillo replica outside the door (do Príncipe entrants pass it?).
- **O13 CRITICAL** — The SE block (015–022; ALT-B, ALT-G): the way in (through the Capilla de los Dolores?) and out; the order of rooms; one-way? Goya and the Núñez panel on view; **where the Sala del Pabellón is and what is in it** (Zurbarán titles; El Greco loan still there?; *Los Rostros de Cristo*?); Sacristía Mayor: Campaña "in front of the central chapel", the dome, the Murillos, the San Fernando statue, the **Custodia on view?**; the Sala del Tesoro (antigua Contaduría): what is on show; Artemisia back?; the Antecabildo and curved corridor; Sala Capitular: Murillo, the round canvases, Céspedes, the armchair; the way back into the church.
- **O14** — Capilla Real (022–023; ALT-F): where visitors can look in through the 1771 grille; open, closed or curtained; visible: the Virgen de los Reyes, the urn, the tombs; Masses; any exhibit in the Trasaltar.
- **O15 CRITICAL** — North transept and the door into the Patio (023–025; ALT-D; E and H bridges): **which door do visitors use into the Patio — the Concepción, or another?** The Ascension window above it; the Altar de Plata back in this arm? The Salida signs.
- **O16** — The Patio (025–026; ALT-C): the lily vases still on display?; the fountain and water channels; the Sagrario side; **can the Giraldillo be seen from the Patio** (works?); where listeners can stand out of the flow.
- **O17** — The Nave del Lagarto (026–027; ALT-H): reachable or visible from the Patio at the end?; the crocodile, tusk, rod and bridle; any panel.
- **O18 CRITICAL** — The Perdón (027–028; bridges): is it the exit?; which face shows the Expulsion relief, Florentín's figures and the plaster; the doors; where to stand.
- **O19** — Stopwatch each length (walking and climbing only): H ≈ 29 min, E ≈ 40, Full ≈ 43 (tower ≈ 20 of each). Correct 001 and section 3 if far off.
- **O20** — Step-free notes for 001: the Giralda is ramps (no wheelchairs or strollers, NORMAS); steps in the SE block, the Patio, the Perdón; lifts?
- **O21** — Signage: Spanish names on signs? Chapel names over the grilles? Any numbers posted?
- **O22** — The day before: re-read catedraldesevilla.es news (Masses, closures, special days, Giralda works, exhibitions); retry the blocked Spanish pages (research §1).

## 6. DATED list (cut or revise on these dates; re-read the official news before recording)

| Date / trigger | Item | Track(s) |
|---|---|---|
| Phase VI end (~early 2028; started 14 Apr 2026) | Works sentence in or out; screens at the bell level; re-check before every re-record | 004, 005, 026 |
| 1 Jan 2027 | Lily vases: say "in February 2026", not "earlier this year"; Patio sentence only while they are displayed | 004, 025 |
| Capilla Real reopened 18 Feb 2026 | "Recently restored" until end 2027 | 023 |
| El Greco *Magdalena* on loan (from ~5 Jan 2026, no end date) | Only while on show; cut when it returns to Paradas | 017 |
| Altar de Plata (restoration from Jan 2025; Aug 2026 Novena suggests it is back) | Sentence in or out after O15 | 024 |
| Artemisia *Magdalena* ("en restauración") | Not used; if back on view, possible X | held |
| Columbus DNA (last statement 10 Oct 2024; no peer-reviewed paper found by 30 Oct 2026) | Re-check before each re-record; if published, revise 015 | 015 |
| Turris Fortissima findings (Nov 2025) | "Recently found" until end 2027 | 003 |
| Factum Foundation 3D recording (Nov 2025) | Optional, "in 2025" | 028 |
| Entrance doors by ticket type (OFF, Apr 2026) | If the doors change, rewrite 001's two paragraphs | 001 |
| Special days (e.g. 4–8 Dec 2025: entry by the Perdón, Giralda only) | One-offs, never in speech; check O22 | 001, 028 |
| Retablo restoration 2012–14 | Never "recent" | 008 |
| Puerta de la Concepción 1887 vs 1917 (two OFF pages) | No date spoken until resolved | 024 |
| *Los Rostros de Cristo* exhibition (from 7 Feb 2026) | Not used | – |
| A new official plan or signage numbering | Re-check every cue and the MAP items | all |

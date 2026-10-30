# Audit fixes — tracks 001–028 (30 Oct 2026)

Applies `research/AUDIT_V5_001-028.md` (MUST-FIX M1–M7, SHOULD-FIX S1–S19) plus the lead's decisions. `python3 v5/lint.py` prints OK for all 28 tracks after the fixes. PLAN.md was not edited (see "For the lead").

## Pages re-read for these fixes (WebFetch, one at a time, 30 Oct 2026; quotes as relayed)
| Page | What it confirmed for the fix |
|---|---|
| ARAMCO archive.aramcoworld.com/issue/199401/the.giralda.htm | "The central core consisted of seven rooms, probably used for storage or as quarters for guards"; 34 ramps (002, 003) |
| TF catedraldesevilla.es/en/the-giralda-reveals-new-secrets-at-the-international-congress-turris-fortissima/ | "Drawing book" is one speaker's hypothesis (J. M. Puerta Vílchez, "as if it were a drawing book"; news text "would function as"); "double-walled tubular"; the page doesn't say whether the centre is solid (003) |
| AHPS Junta PDF Info_web_diciembre_2022.pdf | Hernán Ruiz contract "fechado el 17 de diciembre de 1557" (004); Morel's name appears in "la fundición de siete campanas de la Giralda" in a list of works (005); Giraldillo contract 27 Aug 1566, "acabada en ocho meses", placed 13 Aug 1568 "dos años después de lo pactado" (026); Morel and the choir lectern (026) |
| GLOBE dynamic-rsnz.natlib.govt.nz/newspapers/GLOBE18750417.2.19 | "Thus the chapel in the Seville Cathedral regains, if there is no counterfeiting in the case, its complete altar-piece"; account "given in the New York Nation" (011) |
| OHC repositoriodigital.ohc.cu/…/598d896c….pdf | "ni ella guardó nunca sus cenizas" (about the bronze monument); no author named, part of a larger book; Mélida: "Aragón y Navarra, que si no tomaron parte en la gloria, vienen a tomarla en el duelo" (014) |
| AP06 nbcnews.com/id/wbna12871458 | Undated page, but it is set on the eve of the 500th anniversary of Columbus's death, so May 2006. Castro: "absolute matchup" of mitochondrial DNA with brother Diego. Mieses, director of the Columbus Lighthouse: "The remains have never left Dominican territory." (015) |
| PAINT catedraldesevilla.es/en/?p=53309 | Zurbarán ×2 (1635–1645; 1645–1650), Valdés Leal ×2 (c.1656; 1657–1658), Pacheco 1620, all "Sala del Pabellón". The list gives no titles or techniques and says nothing else about Zurbarán. It does not mention El Greco (017) |
| REN catedraldesevilla.es/en/the-cathedral/building/renaissance-additions-royal-chapel-chapter-house-and-main-sacristy | San Fernando "next to one of the pillars of the head"; "On the opposite pillar is the Immaculate Conception" (019); "designed by Canon Francisco Pacheco" (021); Royal Chapel "occupies the head of the temple" (022/023) |
| HIST catedraldesevilla.es/en/the-cathedral/its-history/ | "The left pillar of the choir collapses and is rebuilt. (1888)" (010) |

## Changes, track by track (before → after; why)
**001** (ANCHOR, 354 → 357 w)
- M6 / lead: "you walked under a hanging crocodile" → "you **may have passed** under a hanging crocodile". Why: O1 is unconfirmed, and 027 hedges the same fact.
- S2: "The numbers may jump, but every stop names…" → "Every stop names the next place in Spanish, as on the signs, with something to look for. On a shorter tour the numbers jump, and any Extra that's announced isn't on your phone: just go on to the next main stop." Why: E and H listeners hear Extras announced in 004, 008, 016, 018 and 020 that aren't on their phone. The audit's wording was merged with the "numbers may jump" line and has no semicolon (lint).
- Trims to stay ≤ 360 words, with no content dropped:
  - "stands on the site of a great mosque, built by the Almohads in the twelfth century. Its bell tower began life as the mosque's minaret." → "stands where the Almohads built a great mosque in the twelfth century. Its bell tower was the mosque's minaret."
  - "at the very end" → "at the end".
  - "For now, cross through the middle of the church … transept. Then follow" → "Cross the middle of the church … transept, and follow".
  - "Wherever you came in, start the next stop as you begin the climb, on the first ramps" → "Climbing? Start the next stop on the first ramps" (this pairs with "Not climbing?").
- @what: added "Extras not on the shorter versions".

**002**
- M1: "between the outer wall and a solid inner core" → "an inner core"; @where "the solid central core" → "the central core". Why: the core holds seven rooms (ARAMCO), and the old wording contradicted 003.

**003** (234 → 242 w)
- M1: "a solid core rises in the middle, and the ramps turn" → "a central core rises in the middle, with the seven chambers stacked inside it, and the ramps turn". Why: ARAMCO and TF.
- S3: "One scholar describes them as a drawing book" → "One scholar suggests they served as a drawing book". Why: TF presents it as a hypothesis.

**004**
- S17: "He signed his contract just before Christmas." → "He signed his contract in December 1557." Why: the year was never given (AHPS: 17 Dec 1557). With this change 004 speaks 1557, 1568 and 1511, plus the two cuttable DATED sentences for 2026.

**005**
- S4: "also cast seven of the Giralda's bells" → "also had a hand in casting seven of the Giralda's bells". @what changed to match. Why: AHPS lists the bells among works that bear his name, and does not make him sole founder.

**006**
- S5: "[wry] The record of the chapter's decision is more sober. It asks for a church…" → "[wry] The decision itself, as it has come down to us, is more sober. It speaks of a church…". @what and @listen changed to match. Why: the 1401 act is not preserved in the original (FACTS §1.7, evidence column). This departs from FACTS §1.8's verbatim safe wording only by hedging it further, so it does not conflict with the brief's "use the safe wording" rule.

**007**
- S6: "The tower you've just come down stands in one corner." → "The Giralda, the tower, stands in this corner of the church." Why: 001 sends non-climbers straight here.

**008**
- S7: cue "Then turn round: facing the altarpiece across the crossing is the Coro…" → "The next main stop is behind you: turn round to the Coro, the choir, behind its own Renaissance grille, with organ pipes rising above it." Why: PLAN's Extra-announcement pattern.
- S18 (optional, applied): "One wall of gold." → "One wall of gilded wood." Why: it is gilded wood (FACTS §6.8).

**009**
- S18 (optional, applied): hook "a friar who, between commissions, also mended" → "a friar who, the story goes, between commissions also mended". Why: the source is Williams 1907, after Ceán.

**010**
- S8: "In 1888 one of its pillars collapsed" → "In 1888 one of the great pillars beside the choir collapsed". Why: HIST says "the left pillar of the choir", and the choir enclosure has no pillars of its own.

**011**
- M5 / lead: "One New York report of the time ended on a careful note. All was well, it said, if there is no counterfeiting in the case." → "One New York paper of the time, The Nation, ended its report on a careful note. The chapel regains its complete altarpiece, it said, "if there is no counterfeiting in the case."" Why: the old line paraphrased the quote. This is the audit's exact wording, re-read on the Globe page, which reprints *The Nation*. @sources updated.

**012**
- S18 (optional, applied): "and almost all of it lies in front of you" → "and it stretches away in front of you". Why: the choir blocks the view.

**014** (lead: keep the Havana story, attributed, with the softer opening)
- S9: "And there, it never held Columbus at all." → "And there, it seems, it never held Columbus at all."
- S9: "According to the Havana historians' own archive, the new tomb never held his remains at all." → "According to an old Havana account, kept by the city historian's office, the new tomb never held his remains." Why: the source is an anonymous chapter of a book in the OHC repository, not a study by the historians themselves.
- S9: "The two behind, Aragon and Navarre, took no part in the glory, he wrote, but they come to share in the mourning." → "The two behind, Aragon and Navarre, come, as he put it, to share in the mourning if they had no share in the glory." Why: Mélida's "si no tomaron parte" is a conditional.
- Not changed: "Look for the castle and the lion." This is CHECK-ONSITE with no replacement, so O12 now says to cut it if the arms aren't clearly visible.

**015**
- S10: "In the words of the director of its Columbus Lighthouse, the remains have never left Dominican territory." → "In 2006 the director of its Columbus Lighthouse put it plainly: the remains have never left Dominican territory."
- S10: "In 2006 it matched them with the DNA of Columbus's brother Diego." → "In May 2006 it reported a match with the DNA of Columbus's brother Diego." I added "May" so the two consecutive "In 2006" sentences don't read as a repeat; AP06 is set on the eve of the 20 May 2006 anniversary.

**016**
- S11: "Justa and Rufina were sisters, and potters." → "Tradition makes Justa and Rufina sisters, and potters." Why: this is hagiography.

**017** (X, 180 → 173 w; lead: hold the El Greco, retitle to what is confirmed)
- @title "Sala del Pabellón · Extra · Zurbarán and a visiting El Greco" → "Sala del Pabellón · Extra · Zurbarán and Seville's painters". This is the audit's fallback title. It doesn't say "both", because the cathedral also has Zurbarán's San Pedro chapel paintings (biografiasyvidas, low grade).
- M2: "Plenty of guides will tell you that Zurbarán hangs in the chalice sacristy. The Cathedral's own list of its paintings puts both of its Zurbaráns here, in the Sala del Pabellón, the exhibition room." → "Two paintings by Francisco de Zurbarán hang here, in the Sala del Pabellón, the exhibition room. That's where the Cathedral's own list of its paintings places them. The list gives no titles, only dates: one was painted between the mid-1630s and the mid-1640s, the other in the later 1640s."
- Valdés Leal: "from the 1650s" → "painted within a year or two of each other in the later 1650s". Pacheco: "+ from 1620, the oldest picture of the group". These dates come from PAINT, so the new content is all list-confirmed.
- M3: the El Greco paragraph is **held** (text below). It is replaced by "[pause] Five pictures by three painters, spanning close to forty years of one city's art." (1620–1658, from PAINT.)
- Payoff "Seville's painters, side by side, with a famous guest." → "Seville's painters, side by side."
- @where, @what, @listen, @brief and @sources: all El Greco wording removed. @sources notes the loan page as held, not spoken.

**018**
- S12: "The painting was saved and came here." → "The painting survived, and in time it came to the cathedral." Why: we have no source for when it came.

**019**
- S13: "On one stands a statue of King Fernando the Third…" → "**Beside** one stands a statue of King Fernando the Third…" (REN: "next to one of the pillars").
- "On the pillar opposite stands the Immaculate Conception." → "On the pillar opposite **is** the Immaculate Conception." The audit's "Beside the pillar opposite stands…" is partly declined: REN (re-read) says "**On** the opposite pillar is the Immaculate Conception". The work's form is unconfirmed, so "stands" was dropped. Added to O13.
- @where "the statues on the facing pillars" → "the statue of San Fernando beside one pillar and the Immaculate Conception on the pillar opposite"; @what changed to match.

**020** (269 → 282 w)
- S7: cue "Through the Antecabildo … ring of round paintings. There's a short Extra on the room itself first." → "There's a short Extra on the chapter house itself first. Then the next main stop, in the same room, is Murillo's Immaculate. Through the Antecabildo, the antechamber, and along the curved corridor to the Sala Capitular: the oval chapter house, with Murillo's Virgin presiding over a ring of round paintings." This is the audit's text with one change: "on the room itself" → "on the chapter house itself", because the room isn't named yet at that point.

**021**
- S14: "A learned canon, Francisco Pacheco, planned…" → "A learned canon, Francisco Pacheco, not the painter of the same name, planned…". Why: the painter Pacheco is in 017.

**022**
- M4: cue "Now back into the church and on to its far end, behind the Capilla Mayor" → "Now back into the church, to the end behind the Capilla Mayor". Why: everywhere else "far end" means the west doors.

**023**
- M4: @where "at the far end of the church behind the Capilla Mayor" → "at the end of the church behind the Capilla Mayor".
- Lead / O15: cue "Go to the arm of the transept on the side where you came down from the tower. Look for the Puerta de la Concepción, the door under a tall stained-glass window of the Ascension." → "Go to the arm of the transept on the side where you came down from the tower, to the Puerta de la Concepción: the tall doorway at its end." Why: GLASS contradicts itself on which transept gable has the Ascension window, so the cue no longer needs it.

**024**
- @where: "a tall Gothic doorway with a great stained-glass window of the Ascension above it" → "the tall Gothic doorway at the end of this arm of the transept". It now matches 023's cue and does not depend on the window.
- Body unchanged. The audit marks the facts OK, but the window's position is CHECK-ONSITE (O15). Fallback if O15 finds the Ascension window at the opposite end of the transept: replace "[pause] Now look up above the door, at the great window of the Ascension." with "[pause] Now look back along the transept to the great window of the Ascension at its far end." Also replace "So the door is new, and the light above it is Renaissance." with "So the door is new, and that light is Renaissance."

**026**
- S15: "two years later than agreed" → "two years after the contract was signed". Why: under the 8-month contract (AHPS) she was in fact about 16 months late.
- S15: "you have seen his work up close" → "you have already seen his work". Why: the lectern is inside the walled coro.
- @sources: AHPS quote expanded.

**027**
- S16: "The crocodile you see today is a wooden copy." → "…is said to be a wooden copy." @what changed to match. Why: UPO24 is the only source, and it is internally inconsistent.

**Unchanged:** 013, 025, 028. The audit has no fix for them except CHECK-ONSITE items, which were already in the checklist (O11, O16, O18).

## Bridges (`v5/bridges/021-028.txt`; 001-010 and 011-020 already complied)
- 022 E>025, two sentences → one (39 w). Before: "On this shorter tour, skip the Capilla Real. Go back into the church, … into the Patio de los Naranjos: orange trees around a fountain." After: "On this shorter tour, skip the Capilla Real: go back into the church, to the arm of the transept on the tower's side, and follow the Salida signs into the Patio de los Naranjos, orange trees around a fountain." It now follows 022's corrected cue cleanly.
- 025 E>028 and 025 H>028, two sentences → one (35 w): "…skip the Giraldillo and the crocodile. Go on to the Puerta del Perdón, …" → "…skip the Giraldillo and the crocodile and go on to the Puerta del Perdón, …".
- All seven bridges are now one sentence of ≤ 40 words (34–39) starting "On this shorter tour,". None uses the Ascension window. The 014 H>025 bridge should still be recorded only after O15 (PLAN never-skip rule).

## ONSITE_CHECKLIST.txt
- Added a block, "ADDED AFTER THE INDEPENDENT AUDIT":
  - O1: restore "you walked under" only if confirmed.
  - O12: the castle and lion on the heralds' tunics.
  - O13: the El Greco (CRITICAL for 017), the Zurbarán labels and the Artemisia.
  - O13: the 019 pillar placements.
  - O15 CRITICAL: the Ascension window's position (GLASS conflict), with the 024 fallback.
  - O19: the 001 full-tour duration.
  - O22: the S19 DATED re-checks.
- The El Greco trigger line now says the painting is held, and gives the restore rule.

## Declined or partly declined (with reasons)
1. **S1, 001 Full duration** ("an hour and three-quarters" → "an hour and a half"): **declined**. WRITER_BRIEF prescribes "the full tour about an hour and three-quarters", and PLAN §3(c) keeps that wording as the lead's option after O19. The audit's figure follows PLAN's ≈ 96-min estimate. The conflict is logged at O19 for the lead to settle by stopwatch.
2. **S13, 019 Immaculate "Beside the pillar opposite"**: **partly declined**. The re-read REN page says "On the opposite pillar". Only the San Fernando change was applied.
3. **001 optional "Some numbers will be missing on the shorter tours; that's fine."**: not used as written, because of the semicolon (lint) and the 360-word cap. Its meaning is merged into the S2 sentence.
4. **S7 for 020 and S10 for 015**: applied with one-word adjustments ("chapter house"; "May 2006"), for the reasons given above.
5. **Regnal numbers / Roman numerals**: no change needed. All speech already says "Fernando the Third", "Pedro the First", "Charles the Third", "Hernán Ruiz the Younger" and "Vázquez the Elder", and no Roman numeral appears in any spoken body. "Fernando III" and "Hernán Ruiz II" remain only in @what / @sources metadata, which is not spoken.
6. **CHECK-ONSITE rows with no replacement text** (001 Príncipe paragraph, 003/004 view, 008–010 crossing, 012 cue, 013 cue, 015 cue, 025, 026 cue, 027, 028 face): not edited. They are tracked in the checklist (several now with added detail).

## Held text (017) — restore only if O13/O22 confirm the painting is on show
- Title: "Sala del Pabellón · Extra · Zurbarán and a visiting El Greco".
- Paragraph: replace the "Five pictures by three painters…" line, which would no longer be true, with:
  > [pause] Since early 2026 the room has also held a visitor: a Santa María Magdalena, Saint Mary Magdalene, attributed to El Greco and his workshop. It has come from the parish church of San Eutropio in the town of Paradas, and stays here while that church is restored. It is a loan, so enjoy it while it lasts.
- Payoff: "[warmly] Seville's painters, side by side, with a famous guest. A short detour, and a good one."
- Restored length ≈ 220 words (X max 230).
- Also restore El Greco in @where / @what / @listen and the GRECO line in @sources.

## For the lead
- PLAN.md still has 017's old @title and 023's old cue ("under a tall window of the Ascension"). Update those rows if you accept these fixes. I did not edit PLAN.
- Spoken words, tags excluded: 7,509 after the fixes, up from 7,453 before (+56). The brief's guide target is ≈ 7,800.

## Respelling list (synthetic English voice)
Convention: Seville's own **seseo** ("s" for z/ce/ci), applied consistently. Stress is in capitals. Held items are marked (held).

| Text | Respell |
|---|---|
| Giralda | hee-RAHL-dah |
| Giraldillo | hee-rahl-DEE-yoh |
| Catedral de Sevilla | kah-teh-DRAHL deh seh-VEE-yah |
| Catedral (in English sentences, e.g. 006 cue) | kah-teh-DRAHL (not "cathedral") |
| Alcázar | al-KAH-sar |
| Puerta del Lagarto | PWEHR-tah del lah-GAR-toh |
| Puerta del Príncipe | PWEHR-tah del PREEN-see-peh |
| Puerta de San Cristóbal | san krees-TOH-bahl |
| Puerta de la Asunción | ah-soon-SYOHN |
| Puerta de la Concepción | kon-sep-SYOHN |
| Puerta del Perdón | pehr-DOHN |
| Patio de los Naranjos | PAH-tyoh deh lohs nah-RAHN-hohs |
| Nave del Lagarto | NAH-veh del lah-GAR-toh |
| Capilla Mayor / Capilla Real | kah-PEE-yah mah-YOR / reh-AHL |
| Capilla de San Antonio | kah-PEE-yah deh san ahn-TOH-nyoh |
| Retablo Mayor | reh-TAH-bloh mah-YOR |
| Coro | KOH-roh |
| Sacristía de los Cálices | sah-krees-TEE-ah deh lohs KAH-lee-ses |
| Sacristía Mayor | sah-krees-TEE-ah mah-YOR |
| Sala del Pabellón | SAH-lah del pah-beh-YOHN |
| Antecabildo | ahn-teh-kah-BEEL-doh |
| Sala Capitular | SAH-lah kah-pee-too-LAR |
| Capilla de los Dolores | doh-LOH-res |
| Capilla de la Antigua | ahn-TEE-gwah |
| Capilla de Santiago | sahn-TYAH-goh |
| Sepulcro de Colón | seh-POOL-kroh deh koh-LOHN |
| Custodia de Arfe | koos-TOH-dyah deh AR-feh |
| Virgen de los Reyes | VEER-hen deh lohs RAY-es |
| San Fernando | san fehr-NAHN-doh |
| Sagrario | sah-GRAH-ryoh |
| Salida (bridges) | sah-LEE-dah |
| Santa María la Mayor / la Gorda | SAHN-tah mah-REE-ah lah mah-YOR / lah GOR-dah |
| Abu Ya'qub Yusuf | AH-boo yah-KOOB yoo-SOOF |
| al-Mansur | al-man-SOOR |
| Ahmad ibn Baso | AH-mahd ib'n BAH-soh |
| Ali al-Ghumari | AH-lee al-goo-MAH-ree |
| yamur | yah-MOOR |
| Ibn Sahib al-Salat | IB'n sah-HEEB as-sah-LAHT |
| Almohad | AL-moh-had |
| sahn / mihrab | SAHN / MEE-rahb |
| Mamluk | MAM-look |
| Hernán Ruiz | ehr-NAHN roo-EES |
| Juan de Balabarca | hwahn deh bah-lah-BAR-kah |
| Bartolomé Morel | bar-toh-loh-MEH moh-REL |
| Luis de Vargas | loo-EES deh VAR-gahs |
| Pieter Dancart | PEE-ter DAHN-kart |
| Pedro Millán | PEH-droh mee-YAHN |
| Jorge, Alejo Fernández | HOR-heh, ah-LEH-hoh fehr-NAHN-des |
| Roque Balduque | ROH-keh bahl-DOO-keh |
| Juan Bautista Vázquez | hwahn bow-TEES-tah VAHS-kes |
| Fray Francisco de Salamanca | fry frahn-SEES-koh deh sah-lah-MAHN-kah |
| rejas | REH-hahs |
| Nufro Sánchez | NOO-froh SAHN-ches |
| Gothic-Mudéjar | moo-DEH-har |
| Bartolomé Esteban Murillo | ehs-TEH-bahn moo-REE-yoh |
| William Schaus | SHOWSS (rhymes with "house") |
| Cádiz | KAH-dees |
| Fernando Rosales | roh-SAH-les |
| Ricardo Bellver | bel-VEHR |
| Enrique Alemán | en-REE-keh ah-leh-MAHN |
| Vicente Menardo | vee-SEN-teh meh-NAR-doh |
| Diego Hurtado de Mendoza | oor-TAH-doh deh men-DOH-sah |
| Arturo Mélida | MEH-lee-dah |
| Adolfo Fernández Casanova | ah-DOL-foh fehr-NAHN-des kah-sah-NOH-vah |
| Valladolid | bah-yah-doh-LEED |
| Cartuja | kar-TOO-hah |
| Santo Domingo | SAHN-toh doh-MEEN-goh |
| José Antonio Lorente | hoh-SEH ahn-TOH-nyoh loh-REN-teh |
| Hernando Colón | ehr-NAHN-doh koh-LOHN |
| Santas Justa y Rufina | HOOS-tah ee roo-FEE-nah |
| Ceán Bermúdez | seh-AHN behr-MOO-des |
| reales | reh-AH-les |
| Goya | GOY-ah |
| Zurbarán | soor-bah-RAHN |
| Juan de Valdés Leal | vahl-DEHS leh-AHL |
| Francisco Pacheco | pah-CHEH-koh |
| Diego Velázquez | DYEH-goh veh-LAHS-kes |
| El Greco; San Eutropio, Paradas (held) | el GREH-koh; eh-oo-TROH-pyoh, pah-RAH-dahs |
| Santa María Magdalena (held) | SAHN-tah mah-REE-ah mahg-dah-LEH-nah |
| Pedro de Campaña | kahm-PAH-nyah |
| Santa Cruz | SAHN-tah KROOS |
| Antonio Ponz | PONS |
| San Isidoro / San Leandro | ee-see-DOH-roh / leh-AHN-droh |
| Alonso de Herrera | ah-LON-soh deh eh-REH-rah |
| Juan de Arfe y Villafañe | hwahn deh AR-feh ee vee-yah-FAH-nyeh |
| Asensio de Maeda | ah-SEN-syoh deh mah-EH-dah |
| Pablo de Céspedes | SES-peh-des |
| Diego de Velasco | veh-LAHS-koh |
| Marcos Cabrera | kah-BREH-rah |
| Martín de Gainza | mar-TEEN deh GAIN-sah |
| Juan Laureano de Pina | low-reh-AH-noh deh PEE-nah |
| Beatriz of Swabia | beh-ah-TREES, SWAY-bee-ah |
| María de Padilla | pah-DEE-yah |
| Jerónimo Roldán | heh-ROH-nee-moh rol-DAHN |
| Arnao de Flandes | ar-NAH-oh deh FLAHN-des |
| Ortiz de Zúñiga | or-TEES deh SOO-nyee-gah |
| Miguel Florentín | mee-GEL flo-ren-TEEN |
| Bartolomé López | LOH-pes |
| Plateresque | plat-uh-RESK |

**Numbers to check in the TTS proof**
- **Years with a zero in the middle** may be read as "one thousand four hundred one". If needed, spell them for the voice:
  - 1401 "fourteen-oh-one"
  - 1504 "fifteen-oh-four"
  - 1506 "fifteen-oh-six"
  - 1507 "fifteen-oh-seven"
  - 1902 "nineteen-oh-two"
  - 1903 "nineteen-oh-three"
- **New this round:** 1557 (004) "fifteen fifty-seven".
- **Decades** in 017, "mid-1630s" and "1640s", should be read "sixteen-thirties" and "sixteen-forties".
- **Amounts:** 28,000 reales "twenty-eight thousand"; 250 dollars "two hundred and fifty"; 126 metres "a hundred and twenty-six".
- **The apostrophe in "Ya'qub"** may cause a pause or glitch; the respelling avoids it.
- **"The Nation"** (011) is a title: there should be no pause inside it.

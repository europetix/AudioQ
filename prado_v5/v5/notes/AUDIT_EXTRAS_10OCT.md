# Audit of the 22 Extras and the renumbered route, Prado v5 (independent, 10 Oct 2026)

**Scope:** v5/tracks/001–081, focusing on the 22 `@type: X` tracks (006, 007, 009, 014, 018, 021, 022, 023, 028, 030, 034, 036, 038, 046, 052, 063, 065, 068, 072, 075, 076, 079) and the core tracks on either side of each one. I edited no tracks.

**Method**
- **Facts:** I read every Extra's official museodelprado.es page with WebFetch, one fetch at a time (31 pages, plus the ES pages for Mary Tudor, Palafox and Correggio).
- **Rooms:** I compared each Extra against research/extras/*_result.tsv.
- **Route:** I compared each track's last paragraph against research/map/floor0–2.png.
- **Duplication:** I ran a scripted term search over the spoken text of the three tracks on either side of each Extra.
- **Lint:** `v5/lint.py` passes on all 81 tracks.

## Verdict
- **A. Facts:** two HIGH problems. **014:** Correggio's *Noli me tangere* is out on loan. **038:** the reason the blind man can't be Gonnelli is reversed. All other load-bearing claims match the official pages. A few are WEAK in wording (see the table).
- **B. Rooms: pass.** Every Extra's @room and every work it names matches the official room (TSV, and re-confirmed on each page today), with one exception: Correggio, which is now on loan (see A).
- **C. Route: pass.** Every core track before an Extra announces it. Every Extra's last paragraph leads to the next track's room, and visitors who skip Extras still get the full directions to the next main stop (005, 008, 013, 017, 020, 027, 029, 033, 035, 037, 045, 051, 062, 064, 067, 071, 074, 078). No track says "next track". The spoken text has no stale numbers and no reference to the Room 74 Christina Extra.
- **Stale numbering:** it survives only in @sources metadata (not spoken) and in `i18n/assemble.py` (`N_TRACKS = 59`).
- **D. Duplication:** minor overlaps only (LOW).

## Findings

| Track | Sev | Issue | Suggested fix wording |
|---|---|---|---|
| 014 (and 013 last para) | HIGH | **Correggio's *Noli me tangere* is not in Room 49.** The official page (EN and ES, read 10 Oct 2026) gives no room: "En exposición temporal — Dresde, Gemäldegalerie Alte Meister, exhibition 'Correggio', 19.09.2026 – 10.01.2027". The TSV row (049) is out of date. Visitors are sent to look for a painting that isn't there. This affects 014's @title, @where, @what, @listen and paragraph 3, and 013's cue. | **014:** cut the Correggio paragraph and retitle: "Room 49 · Extra · Raphael — Christ Falls on the Way to Calvary". Replace paragraph 3 with a closing line on the Spasimo, e.g. "[quietly] A shipwreck nobody can prove, a mother who will not faint, and a king who wanted it above his altar." **013:** "Before you go, there's a short Extra on Raphael's Christ Falls on the Way to Calvary in this room." (If you would rather keep Correggio, use a dated hedge, e.g. "Until January 2027 Correggio's Noli me tangere is on loan to Dresden…", but cutting is safer for a recording.) Re-check after 10 Jan 2027. |
| 038 | HIGH | **WRONG: "But he looks too young for it."** The page says "the apparent age of Ribera's character discounts him from being Gambassi". It describes "the aged and wrinkled figure of the blind man" and gives Gonnelli's birth as 1603, which makes him 29 in 1632. The figure is too **old**, not too young. | "For two centuries he was taken for a real blind sculptor, Gonnelli. But Gonnelli was not yet thirty, and this man is old." (or simply "But he looks far too old for it.") |
| i18n/assemble.py | MED | `N_TRACKS = 59` (line 14), and the docstring says "59 tracks". After the renumbering, the translation assembler's missing-track check ignores 060–081. | Set `N_TRACKS = 81` and update the docstring. |
| 034 | LOW (WEAK) | The script says "Five versions survive… They were probably begun at about the same time." The page dates Madrid, Paris and probably Ponce to c. 1619, but places the London (Dulwich) "replica" in the late 1630s and calls the Auckland attribution "a matter of great complexity". So "five… begun at about the same time" overstates it. | "Reni painted Saint Sebastian more than once; versions hang in Paris, London, Puerto Rico and New Zealand. The museum doesn't believe one is the original and the rest copies. Some were probably begun together, then finished to different degrees, as each client wished." |
| 023 | LOW (WEAK) | The script says "Saturn, the old god linked to Time". The page identifies Saturn with the Greek **Cronos**, god of agriculture. The page as read does not make the Time (Chronos) link. | "Saturn, the old god the Greeks called Cronos, devoured his own children…" |
| 065 | LOW (WEAK) | The script says "…and that Mengs would make them." The page says Mengs's **workshop** was to make the copies, with Bayeu and Maella painting them. | "…and that Mengs's workshop would make them." |
| 076 | LOW (WEAK) | The script says "The little boy… grew up, and in 1950 he left this painting to the Prado." The page records the legacy of Mariano Fortuny y Madrazo, handed over by Henriette Fortuny in 1950. He died in 1949, so "in 1950 he left" is slightly off. | "The little boy on the divan grew up, and left this painting to the Prado. It arrived in 1950." |
| 018 | LOW | The script says "It once hung beside a bear." This is a wall painting: the page says it was "on the wall alongside the Bear". Also, @what gives "135 × 205 cm", but the page has height 205 and width 135. Every other @what gives height × width. | "It was once painted beside a bear…" Change @what to "205 × 135 cm". |
| 021 | LOW | The script says "Van Dyck's portrait of Isabel Clara Eugenia, the princess with the wreath back in Room 55". This only makes sense to someone who played Extra 007. A visitor who skipped the Extras has not met her. | "…Van Dyck's portrait of Isabel Clara Eugenia, Philip the Second's daughter, who later governed the Netherlands herself." (If you want the callback, add "(if you played the Room 55 Extra, the girl with the wreath)".) |
| 028 | LOW | The script says "Leone Leoni, maker of the emperor's bronze in Room 1". Core 027 itself hedges that the Leoni group may have moved to Room 27, so this line can contradict what the visitor saw. | "…Leone Leoni, the sculptor of the emperor's bronze you've just met…" |
| 014 / 013 / 011 | LOW (dup) | Charles I of England is named as a former owner in 011 (Mantegna), 013 (The Pearl) and again in 014 ("It even passed through…"). That makes three tracks in a row. If Correggio is cut (HIGH above), this goes away. | If kept: "Like The Pearl, it passed through the collection of Charles the First of England." |
| 068 / 067 | LOW (dup) | 067 has just explained that the cartoons were for the Prince and Princess of Asturias at El Pardo (the future Charles IV and María Luisa). 068 repeats "the Prince and Princess of Asturias at El Pardo". The rooms differ (dining room vs bedchamber), and the facts are correct. | "…one of twenty that Mengs ordered from him for the same royal couple at El Pardo, this time for their bedchamber." |
| 072 / 071 | LOW (dup, OK) | The script says "In Goya's house, a portrait of her faced the wall where Saturn hung" (072). 071 has just said this. It is framed as a callback ("You've just met her name in Room 67"), which is acceptable. | Optional trim: "You've just met her name in Room 67, across from Saturn." |
| 075 | LOW | The script says "After it fell, he went to France." The official ES text says only that he moved to France after the fall. He actually went as a prisoner of the French; that is not on the official page, so leaving it out is allowed, but the line reads as voluntary. | Optional: "After it fell, he was taken to France." (Only if a secondary source is acceptable; otherwise leave as is.) |
| 022 / 023 / 063 / 065 / 072 @sources | LOW | Old core numbers are left in metadata (not spoken): "core track 046" (now 061), "core track 053" (now 071), "core 047" (now 062), "core 049" (now 066), "core 053" (now 071). | Replace them with the new numbers or with room names, e.g. "core 061, Room 29". |
| PLAN_EXTRAS.md | LOW | The note for x20 still says "play after: x19". In the new order x20 (072) plays **before** x19 (075). This is a planning doc only. | Add a line: "superseded by RENUMBER_10OCT2026.md". |
| 061 | LOW (optional) | 022 says "Keep this picture in mind" about the later Judgement of Paris in Room 29, but 061 makes no callback. Nothing is wrong, but the payoff is missing. | Optional in 061: "If you played the Extra in Room 78, you've seen the young Rubens paint this same contest." |

## Facts checked and found correct (official page, 10 Oct 2026)

- **006 Mor, Mary Tudor:**
  - The page confirms her parents, that she was proclaimed queen in 1553, and the July 1554 wedding at Winchester, with Philip eleven years younger.
  - It confirms that Van Mander says Charles V sent Mor in 1554.
  - It confirms the details of the chair, the rose in her right hand and the jewelled gloves in her left.
  - It confirms Philip's jewel. The ES displayed-objects note confirms the Peregrina and "descubierta por un esclavo en el archipiélago de las Perlas (Panamá)".
  - It confirms her plain features and tense pose, and her death in 1558. Room 056.
- **007 Anguissola, Philip II:** Cremona; arrival in 1559 as lady-in-waiting; no official post; the X-ray changes to the cape and hand; the rosary. Room 055.
  - **Sánchez Coello, the Infantas:** adult conventions; the wreath; succession and marriage politics; Savoy and the Netherlands. Room 055.
  - **Pantoja, Elisabeth of Valois:** Sofonisba was lady-in-waiting and painting instructor; her 1561 original was lost in the 1604 El Pardo fire; this is a copy of about 1605. Room 055.
- **009 Baldung Grien:** all the iconography. It was attributed to Dürer in the 1834 and 1857 inventories and kept in the Sala Reservada in 1834. The Harmony details (moonlit forest, book, lute, putto with score and swan, serpent on the laurel, Golden Age) are confirmed. Both are in 055B.
- **014 Raphael:**
  - Commissioned by Jacopo Basilio for the Monastery of Santa Maria dello Spasimo.
  - The Virgin is shown conscious, not fainting.
  - The viceroy arranged for it to go to Philip IV, who placed it on the Alcázar chapel altar.
  - Vasari's shipwreck story is doubted because it resembles the Annunziata legend.
  - Room 049. The Correggio facts are correct, but the painting is on loan (HIGH).
- **018 Murals:**
  - San Baudelio: exported to the USA in 1926 and split up; the elephant went to the Met (1926–57) and has been on deposit at the Prado since 1957; the humility and castle symbolism; the Bear; all secular subjects; red ground.
  - Maderuelo: transferred to canvas in 1947 and reconstructed faithfully; the arch scenes; Romanesque style; Master of Taüll.
  - Room 051C.
- **021 Teniers:** all claims confirmed. Room 077.
- **022 Rubens, Judgement of Paris:** all claims confirmed, including the inventory sequence (Rubens 1666–1747, school 1772–1796, Jordaens 1827–1857). Room 078.
- **023 Rubens, Saturn:** the Torre de la Parada commission, painted by Rubens himself; the scythe; the child's gaze; the three stars; Galileo in 1610; a hypothesis only; Rubens in Rome; the corrections. Room 079.
- **028 Titian, self-portrait:** his age (73–75); profile used only for dead sitters (François I); Roman coins; mirrors; Castiglione's black; the Golden Spur; the brush; Leoni's 1537 medal "PICTOR ET EQUES"; Vasari in 1566. Room 041.
- **030 Titian:**
  - *Salome*: the 1516 Doria version; servant and room removed; the Lavinia idea discarded; X-ray changes to the eyes and left arm.
  - *Christ Carrying the Cross*: the first version for Philip II's Escorial chapel; Simon of Cyrene as Zuccato (Ridolfi), son of Titian's first teacher; the tearful gaze as a plea, unusual for Titian.
  - Both in Room 043.
- **034 Reni:** the 23 Feb 1619 Rinaldi letter; the Dying Alexander; the life study; Isabel Farnese at La Granja in 1746; the cleaning that removed the added loincloth and revealed the arm and the loop of rope. Room 004.
- **036 Guercino:** all claims confirmed (Ludovisi 1617; Crouching Aphrodite; lilies; the hand gesture; Ludovisi until 1664, then Philip IV). Room 006.
- **038 Ribera:**
  - *The Sense of Touch*: the head of Apollo (1857 inventory); the painted face and the painting-versus-sculpture debate; the light through forehead, nose and eyelids; the Gonnelli identification during the 17th and 18th centuries (correct apart from the age error).
  - *Saint Bartholomew*: the Counter-Reformation apostle series; the knife; valued at fifty doubloons in 1701–1703.
  - Both in Room 008.
- **046 Velázquez:** painted in Seville in 1619, his largest early work; the San Luis novitiate and the Jesuits; Serrera's "family portrait"; Pacheco; the supposed self-portrait; the daughter born in 1619 ("pointed out on various occasions"); Botticelli; the palette. Room 010.
- **052 Room 26:**
  - *Hippomenes and Atalanta*: the myth; the third apple behind his back; Madrid vs Naples and Pepper's view; Serra, then Peñaranda for Philip IV in 1664.
  - *Venus, Adonis and Cupid*: Ovid; bought in 1664 from the heirs of the Genoese Serra.
  - *The Finding of Moses*: painted in London when he was nearly 70; delivered by his son Francesco; all figures female except Moses.
  - All in Room 026.
- **063 Goya, self-portrait 1815:** all claims confirmed, including the signature incised with the brush handle. Room 036.
- **065 Mengs, Charles III:** the official image and replicas; Grimaldi in 1773 and the Empress of Russia; the three orders; the baton in the right hand and the gesture with the left; "severe but not haughty"; the queen's portrait not painted from life. Room 039.
- **068 Goya, The Pottery Vendor:** one of 20 cartoons Mengs commissioned in October 1777 for the bedchamber of the Prince and Princess of Asturias at El Pardo; the invoice wording; the glances; the 9 January letter to Zapater about four paintings. Room 093.
- **072 Goya, The Milkmaid of Bordeaux:** all claims confirmed. Room 066.
- **075 Goya, Palafox:**
  - Born in Zaragoza in 1775; Captain General 26 May 1808; declared war 31 May; no battlefield victory.
  - Commissioned by Palafox himself in 1814; no decorations shown.
  - "Slightly theatrical… vanity"; the letters of Dec 1814 and Jan 1815; payment to Javier in 1831; the inscription lower left.
  - Room 064.
- **076 Fortuny:** all claims confirmed, apart from the 1950 wording. Room 063B.
- **079 Madrazo:** her age (32); the novels *Berta* and *Ledia*; the soirées; the friendship; the fan and fingers; Ingres in Paris; "the most emblematic"; the 1944 legacy of the II Count of Vilches. Room 061.

## Route in playing order (C): checked against the floor plans

- **Floor 0, north:**
  - **005→006→007→008:** 56 → 55 → 55B. Rooms 56 and 55 share a strip, and 55 faces 55B.
  - **008→009→010:** 55B → 56B, next door in the same strip.
  - **013→014→015:** the far end of 49 → 58B → 58.
  - **017→018→019:** 58A → 58 → 58B → 50 → 51 (51C side room) → 51B → 51A. Whether 51C opens straight into 51B is still to be confirmed on site (already item 8 of AUDIT_ROUTE_10OCT).
- **Floor 2, north:** 020 → 021/022/023 → 024: 76 → 77 → 78 → 79 → 79B. The rooms are in one row.
- **Floor 1:**
  - **027→028→029→030→031:** 1 → 40 → 41 → 42 → 43 → 44.
  - **033→034→035→036→037→038→039:** 3 → 4 → 5 → 6 → 7 → 7A → 7 → 8 → 8B.
  - **045→046→047:** 10 → 11.
  - **051→052→053:** 26 → 25.
  - **062→063→064→065→066:** 32 → 34–37 → 38 → 39 (past the lift) → staircase landing → 23.
- **Floor 2, south:** 067 → 068 → 069: 90 → 91 → 92 → 93 and back past 90 to 85. Skippers go straight back past the stairs to 85.
- **Floor 0, south:**
  - **071→072→073:** 67 → 66 → 65 → 64.
  - **074→075→076→077:** 64 → 63 → 63B → 75. 074 announces both Extras, and 075 adds a skip line.
  - **078→079→080:** 61B → 61 → 60 → 60A.
- **Searches:**
  - The spoken text has no "next track", no "track NNN" and no x-numbers.
  - "Room 74" and the Christina Extra are absent. The only mentions of Christina of Sweden are historical: 008 (her gift of the Dürer panels) and 070 (provenance of the San Ildefonso Group).

# Audit fixes applied to tracks 001–035 (EN), 30 Oct 2026

Applies `research/AUDIT_V5_001-035.md` (sections A–G) with the lead's decisions of 30 Oct. Files changed: `v5/tracks/001–035.perf.txt` (31 of the 35; unchanged: 004, 009, 010, 029), `v5/bridges/*.txt`, `v5/ONSITE_CHECKLIST.txt`, and one cell of `v5/PLAN.md` (the 035 title). `python3 v5/lint.py` prints OK for all 35, with the lint ranges unchanged. Bridges: all 10 are one sentence of 15–40 words and start "On this shorter tour,". Spoken words: 9,093 before, 9,240 after (+147, all 35 tracks including the 2 CRA Extras).

## Re-verification (WebFetch, one page at a time, 30 Oct)

Every changed fact was re-read on its source. No curl, no browser, no CAPTCHA.

| Source | What it confirmed |
|---|---|
| TAB18, Tabales & Vargas Lorenzo 2018 (tabula 19784) | The heraldic plaster is on the east and north walls of the pool's walkway ("andén de la alberca"), not on the pavilion. The cenador is "monofásica". The Pedro date is "muy probablemente", a "hipótesis de trabajo". |
| CALV, Calvert 1921 (Gutenberg 60790) | Panel 10 is "the sack of Tunis, hostilities against those who offer resistance". Panel 9: "the Emperor allows it to be sacked". |
| ANDG, andalucia.com gothic.htm | Only the Salón de los Tapices' vaulted ceiling "was replaced by late Baroque transverse arches". The Vault Room keeps its Gothic rib vault. The chapel "conserves its original Gothic roof". The stone baroque portico is later 18th century. |
| ARAM, AramcoWorld 1993 | I'timad "suddenly burst into tears" and called him cruel not to give her that sight every winter. The Sierra of Córdoba was "planted thick with almond trees". |
| GPC, García Parody & Caballero 2018 (dialnet 7042473) | Arrival "sábado 10 de marzo", with no time of day. Vows "en la cuadra grande, que llaman media naranja". After midnight, "fué aderezado un altar en una cámara del alcázar". The couple "se pasaron a cenar a sus aposentos". They spent "los dos meses" in Seville (departure 18 Mar per Sandoval or 13 May per Cadenas). Proxy esponsales on 1 Nov 1525, repeated 20 Jan 1526. |
| TAB16, Tabales 2016 (tabula 9631) | "Forro de torre, lienzo de tapia y puerta… forman un único proceso". The sightline is only reported ("Se ha querido ver en esto…"). The authors read the side spaces as "independientes y cerrados". The 1936–37 clearance was partial: the mirador and two houses were kept. |
| ITIN, Patronato school itineraries PDF | "el Patio de la Montería tiene ese nombre ya que era el lugar donde se citaba la partida de caza del rey y su corte". Also the unsourced banquet line and "No hay rigor histórico". The document is addressed to teachers. |
| MARCH, alcazarsevilla.org ?p=11106 | The gateway was owned by the Duke of Osuna from the 18th century, and the seller is not named. The 1540 reform "marcaron el cambio de linaje producido en el señorío". |
| EXPO, EXPO-MERCURIO-FINAL.pdf | Works "comenzó en noviembre de 2022". The pool was emptied and cleaned in the later phase. "El Jardín de la Danza… data del siglo XVIII". The columns damaged by Storm Bernard sit "junto a la escalinata", under the heading "Trabajos en el Jardín de la Danza", and the left one has a new pedestal. This is consistent with 024 (added to O20). |
| PLEG, Pleguezuelo (core.ac.uk 51386392) | The oratory is today's "Sala del techo de Carlos V". The "escenario de la misa de esponsales" is stated with no source cited. The queen's 1504 Visitación altar survives, but the page does not say on which floor (O13). |
| UAH, Real Provisión 1503 | The Atarazanas were rejected "debido a la humedad allí existente por su proximidad al río". The part used was the "Cuarto de los Almirantes". |
| CAB, Cabeza Méndez (core.ac.uk 51402338) | They lifted the "solería de mármol" and removed "el nivel renacentista". 22 Aug 2002. Tabales. Finished spring 2005. |

The new sources are also added at the end of each changed track's `@sources` line ("AUDIT FIX 30 Oct").

## Lead decisions applied

- **MUST-FIX 11 (regnal numbers).** `@title`/`@room`/`@where`/`@what` keep the leaflet's names ("Salón del Techo de Carlos V"). In speech, people are "Charles the Fifth" and "Felipe the Second", as already written. Spanish space names are now written to be read correctly:
  - 011, 014, 015: "Salón del Techo de Carlos V" → "Salón del Techo de Carlos Quinto".
  - 014, 015: "Salón del Techo de Felipe II" → "Salón del Techo de Felipe Segundo".
  - 026, 027, 031: "Pabellón de Carlos V" → "Pabellón de Carlos Quinto".
  - A grep finds no other Roman numerals left in speech.
- **MUST-FIX 12 (001).** "about two hours" is kept. The map sentence now says "These are the numbers on the Alcázar's own map, 1 to 53, and the route map that comes with this guide uses the same numbers." It does not say where to get a paper map.
- **028:** version (b) is now the spoken text. Version (a) is held below.
- **Hunting party (006):** used exactly as audit §D advises: one attributed sentence, in 006 only (Full only). The unattributed "hunters gathered here with the king" stays banned.
- **No left/right:** kept. A grep of the speech finds only non-directional "left"/"right".

## Track-by-track changes (before → after, why)

| Track | Before | After | Why |
|---|---|---|---|
| 001 | "Every stop has a number." | "Almost every stop has a number." | SHOULD-FIX: the Cuarto del Príncipe (017) has no leaflet number. |
| 001 | "…1 to 53, and that map is also printed on the route map that comes with this guide." | "…1 to 53, and the route map that comes with this guide uses the same numbers." | MUST-FIX 12, lead wording. |
| 002 | "the gate, its tower and the wall beside it went up in a single campaign" | "the gate, the wall beside it and the casing of its tower went up in a single campaign" | MUST-FIX 7. TAB16 says "forro de torre". |
| 002 | "Nobody knows yet who made that lion, or when." | "Who made that lion, and when, has not been established." | SHOULD-FIX (hedge). |
| 002 | "In the 1930s the architect Juan Talavera cleared them away…" | "In the 1930s, to designs by the architect Juan Talavera, most of them were cleared away…" | SHOULD-FIX. TAB16: the clearance was partial. |
| 002 | "The archaeologists think this was deliberate. It lined up a direct view…" | "One reading is that this was deliberate, to line up a direct view…" | MUST-FIX 7. TAB16 reports this view and does not hold it. |
| 002 | "It is a king's welcome, aimed at his own front door." | "It is a king's work, perhaps aimed at his own front door." | MUST-FIX 7 (closing line). |
| 002 @what | "tower lining… maker and date unknown… cleared 1936–37 by Juan Talavera" | "tower casing… not established… largely cleared 1936–37 to designs by Juan Talavera" | Keeps the metadata consistent with the speech. |
| 003 | "Bourbon kings refurbished the rooms upstairs." | "Bourbon monarchs added and refurbished the rooms upstairs." | SHOULD-FIX: Isabel II was a queen. |
| 005 | "before his famous palace existed" (also @listen) | "before his famous palace was ready" | MUST-FIX 8: the palace was begun in 1356. |
| 005 | "who ruled al-Andalus in the twelfth century" | "…from the twelfth century into the early thirteenth" | SHOULD-FIX: Seville was Almohad until 1248. |
| 005 | "the tower we now call the Giralda" | "the minaret we now call the Giralda" | SHOULD-FIX: the belfry is 16th century. |
| 005 | "Pedro's own building swept much of it away." | "Later palaces swept much of it away." | SHOULD-FIX: the original was unsourced. |
| 006 | "Almost everything in the Alcázar opens off this courtyard sooner or later." | "Much of the Alcázar opens off this courtyard, sooner or later." | SHOULD-FIX. |
| 006 | (none) | Added after "…la montería.": "The Alcázar's own notes for schools say this is where the king and his court gathered before a hunt." | Lead decision, worded as in audit §D. The gate-name sentence is kept. |
| 007 | "Look for the sign with its name." | "Look for the sign Casa de la Contratación." | SHOULD-FIX (cue ambiguous). The wording depends on O5 (added to the checklist). |
| 008 | "too damp, and goods would spoil" | "too damp, being so close to the river" | SHOULD-FIX. UAH re-read. |
| 008 | "then called the Cuarto de los Almirantes" | "known as the Cuarto de los Almirantes" | SHOULD-FIX. |
| 011 | "Under a sixteenth-century floor of marble" | "Under the later marble paving and a sixteenth-century level" | SHOULD-FIX. CAB re-read. |
| 011 | cue "Salón del Techo de Carlos V" | "…Carlos Quinto" | MUST-FIX 11. |
| 012 | "…not in the Gothic palace, whatever some old guides say." | "…not in the Gothic palace." | SHOULD-FIX: the original was meta and disparaging. |
| 012 | (none) | "His altar for the queen, made the same year, survives upstairs." | The audit's optional link to 034. PLEG confirms the altar survives. The floor is O13. |
| 012 | "The historian Alfonso Pleguezuelo also identifies this room as the setting of the Mass for the marriage…" | "The historian Alfonso Pleguezuelo identifies this room as the place where, after midnight, the wedding Mass of Charles the Fifth and Isabel of Portugal was said. The vows themselves, the chronicler tells us, were exchanged in the great domed hall, number 15, the Salón de los Embajadores." | MUST-FIX 6 / §C: consistent wedding wording. |
| 012 | "rooms once used by the king's daughters" | "rooms said to have been used by the king's daughters" | SHOULD-FIX (SEC only). |
| 013 | "It replaced an earlier dome from Pedro's own time." (and @what) | "It is said to have replaced…" | SHOULD-FIX (unverified). |
| 014 | "he married a woman he had never met" | "he married in person a woman he had never met" | Audit hedge. GPC records an earlier proxy betrothal. The optional extra sentence was not added. |
| 014 | "He arrived in the evening, and nobody waited." | "He arrived that day, and nobody waited." | MUST-FIX 6. GPC gives the date only. |
| 014 | "After midnight, now 11 March, the Archbishop of Toledo said Mass in the palace and gave the couple the nuptial blessing." | "After midnight, now 11 March, an altar was set up in a chamber of the palace, and the Archbishop of Toledo said Mass there and gave the couple the nuptial blessing. One historian of the Alcázar places that Mass in the king's old oratory, number 13, the Salón del Techo de Carlos Quinto." | MUST-FIX 6 / §C (also @what). |
| 014 | cue "Number 16 on your Alcázar map, the Salón del Techo de Felipe II" | "Number 16 on the Alcázar map, the Salón del Techo de Felipe Segundo" | MUST-FIX 11 and map wording. |
| 015 | "Salón del Techo de Carlos V" / "…Felipe II" | "…Carlos Quinto" / "…Felipe Segundo" | MUST-FIX 11. |
| 015 | Number 17 "carries two names that pull in opposite directions… Ferdinand and Isabel. It is also called the Dormitorio de los Reyes Moros… [amused] Two names, two very different sets of kings, and one ceiling to settle the argument." | "Number 17 on the Alcázar map, the Sala de los Reyes Católicos, is named after the Catholic Monarchs, Fernando and Isabel. Its wooden ceiling is worked with ribbons and heraldic emblems. [amused] In this palace, look up and the ceiling usually tells you whose room it was." | SHOULD-FIX: RIBA559 ties the alias to the Doncellas rooms. Also the Fernando form (alias removed from @what too). |
| 017 | "The prince in these names is Juan, son and heir of Ferdinand and Isabel" | "…is usually said to be Juan, son and heir of Fernando and Isabel" | SHOULD-FIX (hedge plus Fernando). |
| 018 | "He gave his name to the Cantigas" | "He is credited with the Cantigas de Santa María" | SHOULD-FIX. |
| 018 | "It was repaired, its old vaulted ceilings were replaced with late Baroque arches, and its entrance was given a stone Baroque portico." | "It was repaired. Its great hall, number 32 on the Alcázar map, the Salón de los Tapices, lost its old vaulted ceiling, which was replaced with late Baroque arches. And the entrance was given a stone Baroque portico." | MUST-FIX 3. ANDG re-read. The first mention of 32 moves here, and the cue becomes "Into number 32, the Salón de los Tapices" (also @what). |
| 019 | "The tapestries show the victory. They do not show the sack." | "The series does not hide the sack: one of its twelve scenes shows it. But every scene is framed as a victory for the faith." | MUST-FIX 2. CALV panel 10. Whether that panel hangs here is O15. |
| 019 @listen | "and what the pictures leave out" | "and how they frame the sack of Tunis" | Consistency with the speech. |
| 020 | "keeps its medieval rib vaults, Gothic like the rest of Alfonso the Wise's palace" | "keeps its medieval rib vaults, from Alfonso the Wise's Gothic palace" | MUST-FIX 3. Number 32 lost its vaults. |
| 021 | "They say the wedding banquet was held in this room." | "…held in this room, though the account of the wedding night has the couple dining in their own rooms." | SHOULD-FIX. GPC re-read. |
| 023 | "she wept with delight at a rare snowfall in Córdoba. So he had almond trees planted on the hills…" | "she burst into tears watching snow fall, and told him he was cruel not to give her that sight every winter. So he had the hills of Córdoba planted with almond trees…" | MUST-FIX 5. ARAM re-read. |
| 023 | "al-Mu'tamid" / "Al-Mu'tamid" (speech) | "al-Mutamid" / "Al-Mutamid" | Audit §G: one spelling in speech, matching the leaflet's "Columna de Al-Mutamid". This avoids a glottal glitch on the apostrophe. |
| 023 @where | "at the western end of the garden front" | "at the end of the garden front" | Audit A1: no direction in listener-facing text until MAP-2. |
| 025 | "He looks exactly like the bronze set up here in 1576." | "He is a faithful copy of the bronze set up here in 1576." | SHOULD-FIX. |
| 025 | "Then, in November 2022, the restorers drained the pool." | "Then, in November 2022, the restoration began." | SHOULD-FIX. EXPO: the pool was emptied in a later phase. |
| 025 | "So the figure you see now is a faithful replica" | "So the figure you see now is a replica" | Avoids repeating "faithful". |
| 026, 027 | "Pabellón de Carlos V" | "Pabellón de Carlos Quinto" | MUST-FIX 11. |
| 027 | "Today the organ works on its own, running on…" | "The restored organ was made to run on its own, on…" | SHOULD-FIX: never promise it plays. |
| 028 | "They stayed in Seville only until May." | "They stayed in Seville about two months." | SHOULD-FIX. GPC: departure dates conflict. |
| 028 | "most accounts date it to the 1540s" | "it is usually dated to the 1540s" | SHOULD-FIX. |
| 028 | "Now look at it. Inside it is a single square room" | "Inside, there is a single square room" | MUST-FIX 4. |
| 028 | "And look down. The floor traces the outline…" | "And its floor traces the outline…" | My change: "look down" assumes the listener is inside, which conflicts with version (b). |
| 028 | "After a full restoration, the pavilion is open again, so you can see the tiles and that floor up close." | "If the pavilion is still behind screens, look at its tiled outer walls. The room, the ceiling and that floor are waiting inside." | MUST-FIX 4, lead decision (version b). |
| 030 | "When restorers worked on this pavilion in 2017, the archaeologists found an older story hiding in its walls." | "When restorers worked here in 2017, archaeologists found an older story hiding in the walls of the pool." | MUST-FIX 1. |
| 030 | "Under the plaster of the pavilion… Only two walls showed it. But if they are right, parts of these walls are some three centuries older than the pavilion itself." | "On two walls of the old walkway round the pool, the team found traces of late medieval heraldic decoration in the plaster… But if they are right, the walls round the pool are some three centuries older than the pavilion behind it." | MUST-FIX 1 (TAB18). I wrote "walls round the pool" rather than the audit's "the pool's walls", because paragraph 3 says the pool itself was rebuilt after the pavilion. |
| 030 | "So look at the pavilion behind the lion. On the surface… Underneath, it may hold something much older." | "So look past the pavilion to the pool. The seventeenth-century garden room is the newcomer here. The walls round the water may be much older." | MUST-FIX 1. Same adjustment ("walls round the water", not "the water"). @listen/@what updated. |
| 031 | "Most of what you have seen so far is older. The Italianate gardens… belong to the Renaissance." | "The Italianate gardens… go back to the Renaissance, though they have been remade since." | MUST-FIX 9 (EXPO: the Danza is 18th century). The first sentence was cut to stay within X ≤230. |
| 031 | "bought a Gothic gateway from the town of Marchena" | "bought a Gothic gateway that came from the town of Marchena" | SHOULD-FIX. MARCH: owned by Osuna. |
| 031 | "Pabellón de Carlos V" | "Pabellón de Carlos Quinto" | MUST-FIX 11. |
| 032 | "In 1540 the lordship passed to a new family line, and the heraldry had to follow." | "In 1540, after a change in the family line, the heraldry had to follow." | SHOULD-FIX. MARCH "cambio de linaje". |
| 033 | "Its wall is the oldest that archaeologists have found here, from the eleventh century…" | "Its enclosure wall is the oldest archaeologists have found here, probably from the eleventh century…" | SHOULD-FIX. |
| 033 | "Renaissance gardens, and twentieth-century ones." | "Renaissance gardens, and newer ones beyond." | Audit's optional fix: E and H never reach the 20th-century gardens. |
| 033 | "the remains of King Pedro, after a long journey." | "the remains of King Pedro, who took centuries to come back to Seville." | SHOULD-FIX: Highlights never hears 010. |
| 034 | "the emblems of Isabel and Ferdinand" | "…Isabel and Fernando" | SHOULD-FIX (one form). |
| 035 | `@title: CRA 23 · Extra · Where the King still dines` | `@title: CRA 23 · Extra · A royal house still in use` | MUST-FIX 10 (unsourced). The PLAN row was changed to match, so that "@title exactly as PLAN" (WRITER_BRIEF) still holds. |
| all | "on your Alcázar map" (24 spoken uses in 013–035, plus bridges) | "on the Alcázar map" | SHOULD-FIX (unify). See the note below. |

**Map wording.** I chose "on the Alcázar map" because WRITER_BRIEF prescribes it, and 001–012 already used it. PLAN's Conventions say "on your Alcázar map". "The" is also safer while MAP-1 is open (it does not assume the listener holds the leaflet). The ONSITE listening check now says "on the Alcázar map". **Lead:** if you prefer "your", run one global replace in tracks and bridges.

## Bridges

| Bridge | Before | After |
|---|---|---|
| 001 H>007 | "…and stop at number 5, the palace façade, with its bands of lettering." | "On this shorter tour, go through number 1, the Patio del León, and its triple arch into number 4, the Patio de la Montería, up to number 5, the Fachada del Palacio del Rey Don Pedro, with bands of lettering." The audit's text was 43 words, trimmed to 40. |
| 002 E>004 | "skip the long look at the centuries" | "skip that look at the centuries" |
| 005 E>007 | "don't stop in the middle of the Montería: walk on up to number 5, the Fachada…, close enough to see the bands of lettering high on its front." | "don't stop in the Montería: walk on up to number 5 on the Alcázar map, the Fachada…, close enough to see the bands of lettering on its front." Adds the first-mention form for E listeners, trimmed to 38 words. |
| **009 H>011 (new)** | (none) | "On this shorter tour, walk on into number 10, the Patio de las Doncellas, to the edge of the long pool in the middle." (24 words) |
| 016 H>022 | "follow the signs through the Gothic palace, numbers 31 to 33, out to number 38, …and into number 34, …a long vaulted pool." | "On this shorter tour, follow the Palacio Gótico signs through number 31, the Patio del Crucero, out to number 38, the Jardín de la Danza, then into the vaulted pool of number 34, the Baños de Doña María de Padilla." (40 words) The audit's version was two sentences and about 58 words. I kept the sign wording and the Spanish names, and dropped the bare "halls numbered 32 and 33" to fit WRITER_BRIEF's one sentence of ≤40 words. Record only after O12, O17, O18. |
| 022 E/H>025 | "number 39 on your Alcázar map" | "number 39 on the Alcázar map" |
| 025 H>033 | "skip number 40's long look and the outer gardens: … number 53 on your Alcázar map…" | "On this shorter tour, skip the painted gallery and the outer gardens: follow the Salida signs to number 53 on the Alcázar map, the Apeadero, the columned hall that opens onto the Patio de Banderas." |
| 028 E>033 | "on your Alcázar map" | "on the Alcázar map" |

## Held for after the on-site check

**028 version (a)**, to swap in if O24 finds the pavilion open. Replace the (b) paragraph with:

> After a full restoration, the pavilion is open again, so you can see the tiles and that floor up close.

With (a) you may also restore "And look down. The floor traces the outline of the old labyrinth."

## ONSITE_CHECKLIST.txt additions

- **MAP-1:** confirm that a Yo Tours route map ships with the guide and uses numbers 1–53, with Patronato permission if it reproduces the plan. Otherwise cut the clause from 001.
- **O2:** is the off-centre middle arch visible as such (002)?
- **O5:** is there a sign that reads exactly "Casa de la Contratación" (007 cue)?
- **O13:** is Pisano's 1504 altar for the queen upstairs (012 "survives upstairs")?
- **O15:** is the Sack of Tunis panel among those hung?
- **O18:** are the remains of the Mannerist fountain visible in the Baths (022)?
- **O20:** is one column visibly on a new pedestal (024)?
- **O24:** a pointer to the held 028(a) sentence.
- **LISTENING:**
  - `pronunciation.py` is missing, so the render will fail (see Declined, item 1).
  - New check that the regnal numbers are read as spoken.
  - "on the Alcázar map".
  - "Carlos Quinto", "Felipe Segundo" in the names list.

## Declined or partly applied (with reasons)

1. **MUST-FIX 11, second half: creating `build/static/pronunciation.py`. Not done in this pass.** The lead's decision for item 11 is to write regnal numbers as spoken, which is done. A respelling module rewrites every listed name in every track at render time, so each entry must be ear-tested on the chosen voice (Ava multilingual). Untested CAPS-stress respellings can make a good native reading worse. The seed list is below. **Risk:** `v5/pipeline/render_edge.py` line 11 does `from pronunciation import apply_respelling`, so any render fails until the module exists. This is flagged at the top of the ONSITE listening checks.
2. **Audit §G "format fixes" for dates and years** ("10 March 1526" → "the tenth of March, fifteen twenty-six"; "913", "767" in words). Not applied in the text: WRITER_BRIEF requires years as digits. These belong in the lexicon or listen-QA (seed list below).
3. **016 H bridge and 001 H bridge:** the audit's exact wording was not used. WRITER_BRIEF limits a bridge to one sentence of 15–40 words. Content was kept as described in the Bridges table.
4. **014 optional sentence** ("They had already been married by proxy in Portugal."): not added. The optional "in person" carries the point (GPC: proxy esponsales 1 Nov 1525), and GPC calls the proxy act esponsales rather than a marriage.
5. **Fernando/Ferdinand:** unified to "Fernando" for the Catholic King (009 already, 015, 017, 034). **Kept** "Saint Ferdinand" in 020: it is the painting's subject (San Fernando, Fernando III), and "Saint Ferdinand" is the usual English name for the saint. **Lead:** if you want "Saint Fernando" to echo 003's "Fernando the Third", change one word in 020.
6. **024 "Hence, perhaps, the name."** This is not a fix item. The audit marks it OK (EXPO, re-read: "data del siglo XVIII… pequeño escenario destinado a danzas"), but it overrides PLAN's NOT ("any story behind the name 'Danza'"). It is left as written. **Lead to confirm.**
7. **Section D:** the hunting sentence is used only in 006. 002's PLAN NOT "hunters gathered here with the king" is untouched.

## Names an English voice may mispronounce (seed for `pronunciation.py`; ear-test each)

Stress is in CAPS. Castilian z/ce/ci is given as "th", as in the audit. If the lead prefers the Seville "s", apply it to every entry. Entries marked * are mine. The rest are the audit's §G list.

**Format items:**
- Regnal numbers are now in speech as "Carlos Quinto" (KAR-los KEEN-toh) and "Felipe Segundo" (feh-LEE-peh seh-GOON-doh).
- Dates: "10 March 1526", "3 March", "11 March", "20th of January 1503", "22nd of August 2002" should be read as dates. Check that "1st century" in 033 is now "first century before Christ" in speech.
- "913" → "nine hundred and thirteen".
- "767" → "seven hundred and sixty-seven".
- "1402" and "1404" (era years) must be read as years.
- "al-Mutamid" is now one spelling in speech.
- "I'timad" → ee-tee-MAHD.
- "Jaime" (Lannister) → JAY-mee.

| Name | Respelling |
|---|---|
| Alcázar / Real Alcázar | al-KAH-thar / ray-AHL al-KAH-thar |
| Puerta del León / Patio del León | PWEHR-tah del leh-OHN / PAH-tyoh del leh-OHN |
| Puerta de la Montería* | PWEHR-tah deh lah mon-teh-REE-ah |
| Sala de la Justicia | SAH-lah deh lah hoos-TEE-thyah |
| Patio del Yeso / Palacio del Yeso* | PAH-tyoh / pah-LAH-thyoh del YEH-soh |
| Patio de la Montería / montería / Corral de la Montería | PAH-tyoh deh lah mon-teh-REE-ah / koh-RAHL deh lah mon-teh-REE-ah |
| Fachada del Palacio del Rey Don Pedro | fah-CHAH-dah del pah-LAH-thyoh del RAY don PEH-droh |
| Cuarto del Almirante / de los Almirantes | KWAR-toh del al-mee-RAHN-teh / deh los al-mee-RAHN-tes |
| Casa de la Contratación | KAH-sah deh lah kon-trah-tah-THYOHN |
| Capilla de la Virgen de los Navegantes / Mareantes | kah-PEE-yah deh lah VEER-hen deh los nah-veh-GAHN-tes / mah-reh-AHN-tes |
| Patio de las Doncellas | PAH-tyoh deh lahs don-THEH-yahs |
| Salón del Techo de Carlos Quinto | sah-LOHN del TEH-choh deh KAR-los KEEN-toh |
| Sala de los Infantes | SAH-lah deh los een-FAHN-tes |
| Salón de los Embajadores | sah-LOHN deh los em-bah-hah-DOH-res |
| media naranja | MEH-dyah nah-RAHN-hah |
| Salón del Techo de Felipe Segundo | sah-LOHN del TEH-choh deh feh-LEE-peh seh-GOON-doh |
| Sala de los Reyes Católicos | SAH-lah deh los RAY-es kah-TOH-lee-kos |
| Dormitorio de los Reyes Moros (no longer in speech) | dor-mee-TOH-ryoh deh los RAY-es MOH-ros |
| Patio de las Muñecas | PAH-tyoh deh lahs moo-NYEH-kahs |
| Cuarto del Príncipe / Jardín del Príncipe | KWAR-toh / har-DEEN del PREEN-thee-peh |
| Cuarto Real Alto | KWAR-toh reh-AHL AHL-toh |
| Palacio Gótico | pah-LAH-thyoh GOH-tee-koh |
| Patio del Crucero | PAH-tyoh del kroo-THEH-roh |
| Salón de los Tapices | sah-LOHN deh los tah-PEE-thes |
| Sala de las Bóvedas | SAH-lah deh lahs BOH-veh-dahs |
| Salón Gótico / Sala de las Fiestas | sah-LOHN GOH-tee-koh / SAH-lah deh lahs FYES-tahs |
| Baños de Doña María de Padilla | BAH-nyos deh DOH-nyah mah-REE-ah deh pah-DEE-yah |
| Columna de Al-Mutamid / al-Mutamid | koh-LOOM-nah deh al-moo-TAH-mid |
| Fuente de Troya | FWEN-teh deh TROY-ah |
| Jardín de la Danza | har-DEEN deh lah DAHN-thah |
| Jardín de las Damas*; Damas, Galera, Flores | har-DEEN deh lahs DAH-mahs; DAH-mahs, gah-LEH-rah, FLOH-res |
| Estanque de Mercurio | es-TAHN-keh deh mer-KOO-ryoh |
| Galería del Grutesco / Grutesco | gah-leh-REE-ah del groo-TES-koh |
| Fuente de la Fama | FWEN-teh deh lah FAH-mah |
| Pabellón de Carlos Quinto | pah-beh-YOHN deh KAR-los KEEN-toh |
| Cenador del León | theh-nah-DOR del leh-OHN |
| Jardín Inglés | har-DEEN een-GLES |
| Jardín del Laberinto | har-DEEN del lah-beh-REEN-toh |
| Jardín Marqués de la Vega Inclán / Vega-Inclán | mar-KES deh lah VEH-gah een-KLAHN |
| Puerta de Marchena | PWEHR-tah deh mar-CHEH-nah |
| Jardín de la Alcubilla | har-DEEN deh lah al-koo-BEE-yah |
| Apeadero | ah-peh-ah-DEH-roh |
| Patio de Banderas | PAH-tyoh deh bahn-DEH-rahs |
| Salida | sah-LEE-dah |
| Dormitorio de Isabel la Católica | dor-mee-TOH-ryoh deh ee-sah-BEL lah kah-TOH-lee-kah |
| Antecomedor / Comedor de Gala / Sala de Fumar | an-teh-koh-meh-DOR / koh-meh-DOR deh GAH-lah / SAH-lah deh foo-MAR |
| Archivo de Indias | ar-CHEE-voh deh EEN-dyahs |
| Atarazanas | ah-tah-rah-THAH-nahs |
| Alcalá de Henares | al-kah-LAH deh eh-NAH-res |
| Cádiz / Córdoba / Marchena / Osuna / Arcos | KAH-deeth / KOR-doh-bah / mar-CHEH-nah / oh-SOO-nah / AR-kos |
| Toledo* / Granada* / Extremadura* / Andalucía* | toh-LEH-doh / grah-NAH-dah / ex-treh-mah-DOO-rah / an-dah-loo-THEE-ah |
| al-Andalus* | al-AN-dah-loos |
| Abd al-Rahman | ab-dul-rah-MAHN |
| al-qasr | al-KASR |
| al-Mubarak | al-moo-BAH-rak |
| Abbadid / Almohad / Almoravid / Marinid / Nasrid | AB-bah-did / AL-moh-had / al-MOR-ah-vid / MAR-in-id / NAS-rid |
| Mudéjar | moo-DEH-har |
| sebka | SEB-kah |
| Kufic | KOO-fik |
| wa-la ghaliba illa Allah | wah-LAH GHAH-lee-bah IL-lah al-LAH |
| muqarnas | moo-KAR-nas |
| qubba | KOOB-bah |
| Giralda / Giraldillo | hee-RAHL-dah / hee-rahl-DEE-yoh |
| Alhambra* | al-AHM-brah |
| Río Salado | REE-oh sah-LAH-doh |
| Afonso (IV of Portugal) | ah-FON-soo |
| Enrique / Trastámara(s) / Montiel | en-REE-keh / tras-TAH-mah-rah(s) / mon-TYEL |
| Puebla de Alcocer | PWEH-blah deh al-koh-THER |
| Santo Domingo el Real | SAHN-toh doh-MEEN-goh el reh-AHL |
| Pedro* / Fernando* / Juan* / Felipe* | PEH-droh / fer-NAHN-doh / HWAHN / feh-LEE-peh |
| Miguel Ángel Tabales | mee-GEL AHN-hel tah-BAH-les |
| Cristina Vargas | krees-TEE-nah VAR-gas |
| Juan Talavera | hwahn tah-lah-VEH-rah |
| Julie Marquer | zhoo-LEE mar-KAIR |
| Antonio Almagro / Luis Ramón-Laca | an-TOH-nyoh al-MAH-groh / LWEES rah-MON LAH-kah |
| Alejo Fernández | ah-LEH-hoh fer-NAHN-deth |
| Pinzón / Sancho de Matienzo | peen-THON / SAHN-choh deh mah-TYEN-thoh |
| Hernán Cortés* | er-NAHN kor-TES |
| Amerigo Vespucci* | ah-meh-REE-goh ves-POO-chee |
| Carla Rahn Phillips* | KAR-lah RAHN FIL-ips |
| Saint Elmo* / Patmos* | ELL-moh / PAT-mos |
| Niculoso Pisano / Niculoso Francisco | nee-koo-LOH-soh pee-SAH-noh / frahn-THEES-koh |
| Alfonso Pleguezuelo | al-FON-soh pleh-geh-THWEH-loh |
| Diego Ruiz | DYEH-goh RWEETH |
| Diego de Esquivel | DYEH-goh deh es-kee-VEL |
| Salviati | sal-VYAH-tee |
| Sandoval | sahn-doh-VAHL |
| Duke of Calabria* / Countess of Haro | kah-LAH-bryah / AH-roh |
| King Manuel* / María of Aragon* | mahn-WEL / mah-REE-ah, AR-ah-gon |
| Constanza | kon-STAHN-thah |
| Blanche of Bourbon* / John of Gaunt* | BLAHNSH of BOOR-bon / GAWNT |
| María de Padilla | mah-REE-ah deh pah-DEE-yah |
| Cantigas de Santa María* | kahn-TEE-gahs deh SAHN-tah mah-REE-ah |
| Barbarossa* / Tunis* | bar-bah-ROSS-ah / TYOO-nis |
| Jan Cornelisz Vermeyen | yahn kor-NAY-lis fer-MAY-en |
| Pieter Coecke | PEE-ter KOO-keh |
| Willem de Pannemaker | VIL-em deh PAN-eh-mah-ker |
| Vandergoten | van-der-GOH-ten |
| Antwerp* | ANT-werp |
| Mulay Hasan | MOO-lay HAH-san |
| Virgen de la Antigua | VEER-hen deh lah an-TEE-gwah |
| Diego de Castillejo | DYEH-goh deh kahs-tee-YEH-hoh |
| Domingo Martínez | doh-MEEN-goh mar-TEE-neth |
| Virgen de los Reyes | VEER-hen deh los RAY-es |
| Hermenegild | her-MEN-eh-gild |
| I'timad | ee-tee-MAHD |
| Aghmat / Marrakesh* | AGH-maht / mar-rah-KESH |
| Carmona | kar-MOH-nah |
| Storm Bernard* | BER-nard |
| Diego de Pesquera | DYEH-goh deh pes-KEH-rah |
| Bartolomé Morel | bar-toh-loh-MEH moh-REL |
| caduceus | kuh-DOO-see-us |
| Vermondo Resta | ver-MON-doh RES-tah |
| Leonardo Lombardi / Rodney Briscoe* | leh-oh-NAR-doh lom-BAR-dee / ROD-nee BRIS-koh |
| Juan Hernández | hwahn er-NAHN-deth |
| Polido | poh-LEE-doh |
| Diego Martín Orejuela | DYEH-goh mar-TEEN oh-reh-HWEH-lah |
| Juan de Medina / Benito Valladares | hwahn deh meh-DEE-nah / beh-NEE-toh vah-yah-DAH-res |
| Esteban Jamete | es-TEH-bahn hah-MEH-teh |
| Juan Guas | hwahn GWAHS |
| Tanto Monta | TAHN-toh MON-tah |
| La Granja | lah GRAHN-hah |
| Areo Hotah / Ellaria / Myrcella / Trystane / Doran | AIR-ee-oh HOH-tah / el-LAIR-ee-ah / mur-SEL-ah / TRISS-tayn / DOR-an |
| Martell* / Dorne* / Bronn* / Jaime Lannister* | mar-TEL / DORN / BRON / JAY-mee LAN-is-ter |

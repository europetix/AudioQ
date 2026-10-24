# ES review, Uffizi 24 Oct 2026 (independent reviewer)

Scope: all 67 tracks, read paragraph by paragraph against /home/claude/audioq/uffizi_v5/v5/tracks/NNN.perf.txt, plus all 23 bridge lines.
`assemble.py --check … es` gives 67/67 OK and exit code 0 after the edits.
A backup of the files as they were before the review is in /tmp/claude-0/-home-claude/98e7af58-dd32-56e0-a687-5f082c01b624/scratchpad/es_rev/es_backup_before_review/. It is outside the work folder, so assemble does not read it.

## Results of the scripted scans (after the edits)
- **Room codes:** the codes in every body appear in the same sequence as in the English. This also holds for every last paragraph and every @where. Every @title begins with the same map code as the English.
- **Botticelli tracks:** these titles start "Salas de Botticelli". No A9 to A12 code appears anywhere.
- **Bridges:** all 23 English keys are present, each exactly once, with nothing missing and nothing extra. Every line starts with "En esta versión corta," and its codes match the English.
- **TTS safety:** no symbols (+ & % × ° ; parentheses) and no abbreviations or Roman numerals in any body. Dashes appear only in titles.
- **Numbers:** the remaining non-year digits are 24/4/27 (dates), 173 pinturas, 56 esculturas, 144 pinturas and 750 metros. None of them needs a feminine hundreds form.
- **Additions:** nothing that is not in the English was found. "Tratado de Viena" (022) is in the English and is kept, as instructed.

## Changes to tracks (before → after, why)
| Track | Before | After | Why |
|---|---|---|---|
| 001 | El museo **lo** llama uno de los primeros museos | El museo **la** llama… | The pronoun refers to la galería |
| 004 | «…Cimabue creyó dominar el campo, ahora Giotto tiene la fama, **y la del otro se va apagando**» | «…ahora Giotto tiene la fama, **de modo que la del otro se va apagando**» | Faithful to Longfellow's "so that the other's fame is growing dim". It is still presented as a translation of Longfellow, not as Dante's Italian. |
| 005 | Hoy se fecha hacia 1290 **o** 1300 | Hoy se fecha **entre 1290 y 1300, aproximadamente** | The English gives a range ("about 1290 to 1300"). "o" made it two alternative years. |
| 007 | hacia 1300 **o** 1305 | **entre 1300 y 1305, aproximadamente** | Same reason (range) |
| 008 | Probablemente murieron por ella. | Probablemente murieron **de peste**. | Natural Spanish ("die of the plague") |
| 008 | Cerca, en la sala A6, está su Santa Humildad. | **Pietro tiene otra obra cerca**, su Santa Humildad, en la sala A6. | The English says "Pietro has one more painting". "su" was ambiguous after the paragraph on the Madonna. |
| 009 | y **su mirada** sigue el camino del sonido | y **usted sigue con la vista** el camino del sonido | "your eye" was ambiguous (it could be read as Gabriel's look) |
| 015 | **La sala siguiente** tiene un breve Extra | **La siguiente sala de Botticelli** tiene un breve Extra | The English says "The next Botticelli room". This is navigation. |
| 017 | title "Botticelli — Primavera" | "Botticelli — **La Primavera**" | Title unification (see the titles section) |
| 018 | breve Extra sobre las Vírgenes redondas junto a la Venus y la Calumnia | … junto a la Venus **y sobre** la Calumnia | The old wording read as "beside the Venus and the Calumny". The English means the Extra is on the Madonnas AND on the Calumny. |
| 018 | una gema helenística tallada, **de** Lorenzo el Magnífico | … tallada **que fue de** Lorenzo el Magnífico | "that belonged to". Bare "de" could suggest he made it. |
| 019 | quizá colgó en **un tribunal** de la República florentina | quizá colgó en **una sede** de la República florentina | The English "court" is ambiguous. The new wording is neutral, per the lead. |
| 022 | 5780 piezas | **cinco mil setecientas ochenta** piezas | The TTS would read the digits as masculine "setecientos". Not a year, so the digit check is unaffected. |
| 029 | Hacia 1470 **o** 1475 | **Entre 1470 y 1475, aproximadamente** | The English says "Between about 1470 and 1475" |
| 037 | Baje por la escalera Lanzi \*un solo\* piso, hasta la primera planta, y no hasta la calle | … \*una sola\* planta, hasta la primera, y no hasta la calle | Unified with the floor term "planta". The warning is kept exactly (one floor only, not to the street). |
| 037 | Baje un solo piso y deje la escalera… | Baje **una sola planta** y deje… | Same reason |
| 038 | @where carried "El plano no dibuja una puerta entre la B1 y la B2: la B2 se abre a la B4 y da al rellano de la escalera." | sentence removed | Aligned to the cleaned English @where, which has no production note. 041, 043 and 060 @where were checked and already match the cleaned English. |
| 040 | contempla al **niño** | contempla al **Niño** | Consistent capitalisation of the Christ Child |
| 047 | Rafael murió en Roma en 1520, pero su estilo no murió con él. | … pero su estilo **le sobrevivió**. | Saves two words so that the next fix fits the length limit. The meaning is unchanged. |
| 047 | Mire al **niño**. | Mire al **Niño**. | Capitalisation, as in 040 |
| 047 | **Allí**, el Niño de Perin del Vaga… | **En esta sala**, el Niño de Perin del Vaga… | The English says "In the same room". "Allí" came right after "en Roma" and could be read as "in Rome". |
| 051 / 052 | Eleonora **di** Toledo (title 052, bodies 051 and 052) | Eleonora **de** Toledo | One form everywhere, per the lead. It keeps the museum's first name, Eleonora, which matches the label, with the Spanish particle "de". Every other mention is "Eleonora" alone. |
| 063 | El mundo, por fin, **la** ha alcanzado. | El mundo **se ha puesto al día**. | "The world has caught up". "la" was ambiguous (Florence? the painter?). |

## Changes to bridges
- **Wording unified:** "sáltese" (first half) and "omita" (second half) now read "omita" everywhere: 002 E>004, 002 H>006, 007 H>017, 009 E>012, 025 E>029, 025 H>030 and 031 E>034.
- **007 H>017:** "Si está cerrado" became "Si **el paso** está cerrado" (English: "If the way through is closed", and track 014 uses the same words). "siga los carteles de Botticelli" became "siga los carteles **del museo hacia** Botticelli" (English: "the museum's Botticelli signs"). The line is now 76 words against the English 73. This is accepted for navigation fidelity.
- **025 E>029 and 025 H>030:** "pase la sala A34" became "pase **la puerta de** la sala A34" (English: "pass the doorway of Room A34"). "Pasar la sala" can be heard as "go through the room". The wording now matches track 027.
- **037 E>041:** "baje un solo piso" became "baje **una sola planta**".
- **Second-half bridges:** these ran 5 to 10 words over the English. They were tightened with no loss of route content.
  - 035 H>037 is now 35 words against the English 35.
  - 037 E>041 is now 38 against 38.
  - 037 H>046 went from 50 to 46 against 40.
  - 046 H>052 is now 39 against 39.
  - 049 E>052 went from 42 to 40 against 33.
  - 052 H>057 went from 45 to 41 against 39.
  - 055 E>057 went from 42 to 41 against 34.
  - 057 H>062 went from 45 to 40 against 39.
  - 064 H>067 is now 30 against 31.
- **Routes unchanged:** every route, order and condition is the same as the English (checked line by line). This includes "asking a warden if blocked", "past the Vasari Corridor door without going through it" and "up the Verone, then turn left".

## Unification decisions (now consistent across 001–067)
- **Extras:** "La sala X tiene un breve Extra sobre … La siguiente parada principal es la sala …" No "A continuación, la sala…" remains.
- **Floors and staircases:** "la segunda planta" and "la primera planta". "La escalera Lanzi / Buontalenti / Granducal / Magliabechi". Lanzi: "una sola planta, hasta la primera, y no hasta la calle".
- **Rulers:**
  - Cosme Primero, Segundo and Tercero.
  - Francisco Primero, Fernando Primero, Pedro Leopoldo, Cosme el Viejo and Lorenzo el Magnífico.
  - Where the English gives no number, the Spanish gives none: "el gran duque Fernando" (023, 064) and "Francisco" (001, 002, 055).
  - The della Rovere and Gonzaga keep their Italian names: Francesco Maria Segundo, Eleonora Gonzaga.
- **Artists:** Tiziano, el Veronés ("Paolo Veronés" once, in 059), Miguel Ángel, Rafael, Pedro Pablo Rubens, Anton van Dyck. The @where map labels stay as the signs read («Veronese» and so on).
- **Room codes:** "la sala A4" on first mention. When the English itself drops "Room" (for example "C4 and C5" or "past D14"), the Spanish drops "sala" too ("la C4"). No code was added or removed.

## Titles (no translator checked any; reviewer's choice, the forms usual in Spanish art writing)
- **In @title, with the article:**
  - La Primavera; El nacimiento de Venus; La batalla de San Romano.
  - La Virgen del jilguero; La Virgen del cuello largo; La Venus de Urbino.
  - El Tondo Doni; El tríptico Portinari; Los duques de Urbino.
- **Without an article in @title:**
  - Maestà de Santa Trinita; Madonna Rucellai; Maestà de Ognissanti.
  - Anunciación; Adoración de los Magos; Coronación de la Virgen.
  - San Jerónimo en el desierto; Judit decapitando a Holofernes; Baco; Medusa; Flora.
- **In running speech:** the short name takes a lowercase article: la Primavera, el Nacimiento de Venus, el Tondo Doni, la Calumnia de Apeles. This is common Spanish practice and is not audible. "La batalla de San Romano" keeps its capital article in the body.
- **Not verified online:** none of these titles was checked against a page. They are the forms I know to be standard in Spanish, but I did not look any of them up. Treat them as reviewer-standard, not museum-verified. The museum has no Spanish pages.

## Quotations
- Every quotation was checked against brief rule 11. None was originally Spanish. All are faithful translations of the English and are introduced the same way.
- 001 and 067 keep reported speech without quotation marks, as in the English.
- 004 (Dante) uses no Spanish edition. It is a faithful translation of the English Longfellow text and is presented as such.

## For the lead
1. **Eleonora de Toledo:** this is the form used everywhere. If you prefer the established Spanish "Leonor de Toledo", change three places: 051 body, 052 title and 052 body. The bridges 046 and 049 say "Eleonora" only.
2. **Bridge lengths:** four second-half bridges are still 2 to 7 words over the English (037 H>046, 049 E>052, 052 H>057, 055 E>057). So is 007 H>017, by 3 words. Spanish needs the articles, and the check does not cover bridges.
3. **Conditions kept as written:** 059 (listed in the Veronese Corridor) and 060 (the Verone described as open and pale green) are both in the English and are kept.
4. **Remaining flags:** 052 "a pocas semanas de su hijo" stays ambiguous, as the English is. 022 "Tratado de Viena" is kept as instructed.

## Verdict
Ready.

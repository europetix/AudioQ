# ES review, all 70 tracks (23 Oct 2026)

I compared every track sentence by sentence against the English in /home/claude/audioq/thyssen_v5/v5/tracks/NNN.perf.txt. I checked facts, hedges, every "if", the navigation, tags, register (usted) and TTS safety. I then ran a separate scan of every last paragraph and every @title (part B).
`assemble.py --check … es`: **all 70 OK** after the edits (exit 0). No track is longer than the English. 004, 023, 029, 031, 033, 034, 067 and 069 are now exactly equal to the English count.

## 0. Sync
- **031**: before: «antes de que un derrame cerebral en 1835 acabara con su obra al óleo». After: «… acabara **en gran parte** con su obra al óleo» (= "largely ended"). To stay within the word count, «Esta es la última sala de la planta» became «Es la última sala de la planta».

## Unified phrasing (the two halves now use the same forms)
- **Extra announcements**: already the same in both halves: «La sala N tiene un breve Extra sobre …». Variants that follow the English («Antes, la sala 36 tiene…», «La sala 50, «Informalismos», tiene…») keep that core. No change needed.
- **Next main stop**: already «La siguiente parada principal es la sala N» everywhere. No change needed.
- **"Next, Room X"**: both halves mixed «Después,» and «A continuación,». Every navigation cue now reads **«A continuación, la sala …»**. Changed in 012, 013, 019, 022, 023, 027, 029, 033, 034, 035, 038, 054, 055, 061 and 067. 068's «Después, la salida» means "After that, the way out" and stays as it is.
- **Floors are always "planta"**: 031 «un piso más abajo» → «una planta más abajo, en la planta 1». 032 «baje un piso» → «baje una planta, hasta la planta 1». 066 «un piso con estudio» (meaning a flat, and Spain-only) → «una vivienda con estudio».
- **Room word**: «sala» throughout. A–J and the numbers match the English exactly.
- **US nationality**: 035 already said «estadounidense». The 036–070 half said «americano» for people. Now:
  - 045 «rico amigo estadounidense»
  - 052 «los pintores / esos estadounidenses»
  - 055 «el primer estadounidense», and «vida negra americana» → «vida afroamericana»
  - 058 «fotorrealismo estadounidense»
  - 059 «jóvenes estadounidenses»
  - 061 «los estadounidenses de entonces», and «naturaleza salvaje norteamericana» to match the room titles
  - 064 «El estadounidense Childe Hassam»

  Kept as they are: 041 «decidió sonar americano», which is idiomatic, and 033 «Revolución americana», the established name.
- **Work titles**: the museum's Spanish titles are used consistently in both halves. Pierrot contento appears in 025, 026 and 056. El columpio, Marrón y plata uno/dos, «La tradición cubista uno/dos» and «Abstracción norteamericana uno» match their titles.

## Lead's points
- **Room 28**: the 030 @where uses the Spanish map wording «Siglo XVII. Pintura holandesa. Ruisdael». The navigation is unchanged.
- **The See-Saw (023/024)**: in speech, the earlier text could not keep the two pictures apart. The voice reads «El columpio» (the Thyssen title) and «el famoso columpio de la Colección Wallace» the same way, because lowercase is not audible. Changes in 024:
  - «Pintó El columpio hacia 1750» → «Pintó **este lienzo**, El columpio, hacia 1750».
  - «El famoso columpio de la Colección Wallace…» → «Y **el cuadro de Londres**, en la Colección Wallace, unos quince años posterior, también fue suyo». This refers back to paragraph 1 ("Está en Londres"). The Wallace picture is no longer called «columpio» after the title is introduced.
  - The see-saw action is still «balancín». The meaning is unchanged.
- **054 Rosenblum**: confirmed verbatim on https://www.museothyssen.org/coleccion/artistas/rothko-mark/sin-titulo-verde-sobre-morado: «buscan lo sagrado en un mundo profano». The quote now uses it, replacing «lo sublime».
- **067 Goncharova**: the Spanish page (…/goncharova-natalia/pesca-pescadores) says «cronológicamente la artista femenina más importante del siglo XX en Rusia». That is a different claim ("most important"), so I kept the translation of the English: «la primera, cronológicamente, de las grandes artistas rusas del siglo veinte». The Cubism quote matches the page.
- **049 Dalí**: https://www.museothyssen.org/exposiciones lists «El universo freudiano de Dalí», 20 Oct 2026 – 24 Jan 2027. The title is official and the dates match. No change.
- **Room 47 name**: https://www.museothyssen.org/visita/recursos/plano and the Rothko page give no title for Sala 47, because the list jumps from 46 to 48. So it is no longer presented as an official title:
  - 053 speech: «la sala 47, «Abstracción norteamericana dos»» → «la sala 47, **la segunda de abstracción norteamericana**».
  - 054 @where: «En la sala 47, «Abstracción norteamericana II», la sala pequeña…» → «En la sala 47, la segunda sala de abstracción norteamericana, la pequeña…».
- **069 "veinte pies"**: → «hasta los espejos, **a unos seis metros**» (20 ft = 6.1 m). Metric is what listeners in Spain and Latin America picture, and "about" keeps it from being more precise than the English. To fit the count: «Después de siete siglos» → «Tras siete siglos».
- **Room I**: there is one spoken mention, in 067. «Después, la sala I:» became «A continuación, **la sala de la letra i**:». The Roman-numeral glyph is not in speech at all, so the voice cannot say "uno". 068 and the titles and @where fields are not spoken and keep «Sala I». To fit the count: «Ese es el espíritu de este cuadro» → «… del cuadro»; the Diaghilev sentence → «Después diseñó en París para montajes de Diáguilev como El gallo de oro y El pájaro de fuego» (closer to the English "productions"); «y en muñecas» → «y muñecas».

## Other changes (track: before → after, why)
- 004: «Los especialistas ven detrás a Robert Campin» → «ven ahí la influencia de Robert Campin». "Detrás" could send the listener looking behind the figure. Also «como el Redentor» → «como Redentor», for the word count.
- 007: «La tabla mide unos veintiocho» → «mide **solo** unos veintiocho», to match the English "only about".
- 016: «Sus ojos siguen las diagonales … y llegan a su mirada» → «Siga con la vista las diagonales … hasta llegar a su mirada». The old wording read as Catherine's eyes, but the English means the visitor's eye.
- 022: «la familia de Frans Hals ante un paisaje» → «el Grupo familiar ante un paisaje, de Frans Hals». The old wording meant Hals's own family. Also «Este conde vive para la música» → «Este conde es un melómano», because "a man of music" is not "lives for music".
- 029: «horizonte muy bajo» → «horizonte bajo». The English says "a low horizon", and this kept the count.
- 034: «había perdido a uno de sus hijos» → «había perdido un hijo», for the count. The nav cue → «A continuación, la sala 32: Sargent retrata de cuerpo entero a Millicent, duquesa de Sutherland».
- 041: «Con los nazis, colgó en su exposición» → «figuró en su exposición». A picture is hung; it does not hang itself.
- 042: «casi grises» → «casi deslucidos». The English is "drab", not "grey".
- 054: «Entonces, sus colores» → «Por entonces», for "Around then".
- 055: Rauschenberg's «hagas lo que hagas con ellas» → «se haga lo que se haga con ellas». This is an impersonal generic "you", which avoids a lone tú in a usted guide. The meaning is the same.
- 057: «cofundó CoBrA, por Copenhague…» → «siglas de Copenhague…», so it is clear the name comes from the cities.

## Verified, no change
- Navigation scan (B): all 70 last paragraphs match the English. Rooms, order, floors, stairs and lift, "next door", "turn the corner", "stay in this room", the Extras and the next main stop are all correct. The script's only mismatches were false positives: the "A" of «A continuación», Roman numerals spoken as «uno/dos», and «número siete». Every @title starts with «Sala N ·» or «Sala A–J ·». Extras carry «· Extra ·». 001 and 070 have no room.
- Quotations: there are no originally Spanish quotes in «». Münter (039) uses the museum's Spanish wording, and Liebermann (050) is a translation. Both are allowed for ES under rule 11.
- No ; ( dashes or symbols in speech. Regnal numbers are in words. Years are digits.

## For the lead
1. **Audio QA**:
   - 067 «la sala de la letra i». Confirm Dalia says "i".
   - 056/057 «J. Y. M.». The voice might read the «Y» as the conjunction "i" instead of "i griega". If it does, change the speech to «jota, i griega, eme».
2. **041 Mehring**: «Reminiscencias de la entrada a Manhattan» is my rendering of a title the Spanish page gives only in English. It is presented as a title, not a quote. Replace it if an established Spanish form exists.
3. **Room 47** has no official Spanish title on the site. The @title still reads «Sala 47 ·», which is correct.
4. 070 re-entry advice (rule 14 borderline) and 069 dimensions are kept as in the English.

Verdict: **ready**, subject to the audio checks in point 1.

- Lead, after review: 056/057 body "J. Y. M." spoken as "jota, i griega, eme" so the voice cannot read "Y" as "and".
- Lead: 065 title accent «Érase una vez».

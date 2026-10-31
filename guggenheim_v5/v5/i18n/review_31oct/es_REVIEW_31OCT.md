# ES review: Guggenheim Bilbao 001–029 and bridges (independent editor, 31 Oct 2026)

Files edited: `es/001`–`029.json` (21 tracks touched) and `es/bridges.txt`. I did not touch `bridges_001-029.txt`, so it is now out of date. Use `bridges.txt`.
Check: `assemble.py --check … es` gives **29/29 OK**. 012 is now 302/303 (it was 304/303).
Bridges: all 10 keys match the English. Every line starts with «En esta versión corta,» and none is longer than the English.
Pre-review copy of the files: `scratchpad/rev/es_before/`.

## Verdict
**Ready.** Navigation matches the English in all 29 last paragraphs and in all 10 bridges. That covers places, order, level, left/right, both exit variants in 021, the Extras and "la siguiente parada principal". Every spoken cue matches its track title.
I found no added facts and no dropped hedges or conditions. 003 is plain and respectful.

## Lead's points
1. **012 (Serra).** The museum's ES teachers' guide (relacion-obra-de-arte-espectador, WebFetch) prints Serra's words in Spanish. Its source is "Entrevista realizada a R. Serra en Cat. expo. Richard Serra. Escultura 1985–1999", p. 212. The original language is not stated.
   - The guide's wording: «Es un tiempo acelerado el que tienen estas piezas, y es un tiempo trastornado.» and «Es como un salto trastocado en el tiempo. No es lineal; no es narrativo.»
   - Our own back-translations were in «», so I replaced them with the guide's wording, verbatim. I kept only what the English keeps and cut before "; no es narrativo".
   - Note: «trastornado» and «trastocado» are a little stronger than the EN "changed" and "abrupt". They are the museum's own words.
   - Before → after:
     - ¶1 «Estas piezas tienen un tiempo acelerado», dijo Richard Serra. «Es un tiempo cambiado.» → «Es un tiempo acelerado el que tienen estas piezas», dijo Richard Serra, «y es un tiempo trastornado.»
     - ¶5 Serra lo dijo con sus propias palabras: «Es como un salto brusco en el tiempo. No es lineal.» → Serra lo expresó así: «Es como un salto trastocado en el tiempo. No es lineal.»
     - ¶5 «parecen estar en perpetuo movimiento» e incluyen al espectador… → «parecen estar en perpetuo movimiento e implican al espectador en su movimiento» (verbatim from the guide)
   - Tightening:
     - ¶4 hasta que se está en él → hasta estar en él
     - ¶8 una parte de él → parte de él
     - ¶4 Note si → Observe si
   - Also verified verbatim from the same guide:
     - «se pierde la referencia y no se sabe lo que hay delante»
     - «a menos que la obra sea formalmente innovadora, nada cambiará»
     - 011 «la unidad constructiva básica»
     - 013 «se transforman de forma inesperada a medida que el visitante las recorre y rodea»
     - 016 Serra's «el alzado de las piezas siempre queda parcialmente oculto»
     - 009 Serra's «un espacio público, abierto, donde cualquiera pueda venir, sobre todo los jóvenes» (Hal Foster conversation, 2004)
2. **010 (same issue).** The guide also prints Serra's torsion quote in Spanish. Our own versions were in «», so I replaced them with the guide's wording.
   - «Son formas torsionadas que, al entrar en ellas, permiten moverse…» → «Son formas torsionadas que cuando entras en ellas te mueves para entender su torsión.»
   - «Cuando te mueves, ellas también se mueven, de modo que siempre intentas atraparlas.» → Y añadió que «al moverte ellas también se mueven, de modo que siempre estás intentando atraparlas».
   - «con palabras que el museo publica en inglés» → «con palabras que recoge el museo». Saying "in English" before a Spanish quote would be false.
3. **Maman.** The museum's ES page (la-coleccion/obras/mama) has H1 «Mamá», with «Maman» as its subtitle. The body says «Mamá (Maman)». So BRIEF.md's claim that the museum keeps "Maman" is wrong.
   - Decision: keep **Maman** in speech and in all titles and cues (001, 015, 023, 024, 025, 029 and the bridges). The English is built on the French word, and naming the ES title would add a fact.
   - 025 ¶1: «Se llama Maman, «mamá» en francés.» → «Se llama Maman, que en francés significa «mamá».» This is clearer for the ear. A Spanish listener who sees «Mamá» on a sign will make the link.
   - To fit the length limit, ¶5 «vuelve siempre al recuerdo de «una dolorosa…»» → «vuelve siempre a «una dolorosa…»».
   - If you prefer the museum's ES title, the change is mechanical, but every cue and the bridges would change too.
   - Verified verbatim on that page: «tanto para fabricar el capullo como para cazar a su presa», «una dolorosa infancia marcada por un padre infiel y una madre cariñosa pero cómplice de la situación», «unas patas que semejan arcos góticos», «funcionan al mismo tiempo como jaula y como guarida protectora», «peligrosamente adheridos a su abdomen».
4. **Floors.** The museum's ES express route (rutas/rutas-expres) writes «1ª planta, Atrio», «2ª planta, balcón» and «Asciende a la tercera planta: desde el balcón ubicado frente a la sala 304». The teachers' guide says «El balcón de la segunda planta».
   - So the Atrium is the museum's first floor, and «segunda planta» / «tercera planta» match the museum's own Spanish and the gallery numbers 2xx/3xx.
   - It is used the same way in all 7 places (015–019, bridges 009 and 015). No change.
   - The same page confirms 018's «una vista espectacular del Atrio».
5. **Neutral Spanish.**
   - «diseñado por computadora» → «diseñado digitalmente» (002), and «en computadora» → «digitalmente» (017).
   - «Métase» → «Entre» (009).
   - «curadora», «costo» and «video» are understood in Spain and suit the Mexican voice, so I left them.
6. **003.** Only one change: «Murió por sus heridas.» → «Murió de las heridas.» The rest is plain, respectful and accurate. The @where no longer says "city side".

## Other changes (track, before → after, why)
- 001 ¶5: «le indica adónde ir» → «adónde ir después» (EN "where to go next").
- 002 ¶7: «hay jardineros trabajando» → «los jardineros están trabajando» (EN "the gardeners").
- 004 ¶5: «la orilla de trabajo» → «la orilla portuaria». The old wording was a calque of "working riverbank". 001 and 029 now use the same image.
- 005 ¶2: «con la rienda corta» → «bajo estricto control» (more natural).
- 006 ¶3: «aproximación al edificio de Frank O. Gehry» → «aproximación al edificio» de Frank Gehry. The quote is cut before the name, so the voice cannot read "O." as «o» ("or").
- 006 ¶6, 007 @where, bridges 004 E/H: «mirar justo hacia arriba» → «mirar directamente hacia arriba».
- 008 ¶7 and 009 @where: «ver la sala a lo largo» → «en toda su longitud» (EN "down the length of the room").
- 009 ¶4: «el título va en serio» → «el título es literal» (EN "meant literally").
- 010 ¶2: «cerrado, abierto…» → «cerrada, abierta…». This agrees with «espiral» and matches 012.
- 010 ¶5: «note el momento» → «fíjese en el momento», and «Y note si» → «Y observe si».
- 015 ¶1: «Tulipanes no está expuesta» → «Tulipanes no se expone» (grammatical agreement).
- 015 ¶6: «lo encontró corriendo… lo eligió» → «la encontró mientras corría… la eligió». The antecedent is «esta orilla», and «corriendo» could be heard as "in a hurry".
- 016 ¶2: «le manda aquí» → «le envía aquí».
- 017 ¶6: «de unos catorce metros de media» → «de longitud media» (EN "long on average").
- 019 ¶4: «cuatro mil millones de euros para la economía vasca» → «aportados a la economía vasca» (EN "added to").
- 020 ¶2: «tiradores» → «francotiradores» (EN "marksmen").
- 022 ¶4: «Un juego.» → «Le propongo un juego.» (EN "So here's a game").
- 023 ¶2: «de la japonesa» → «de la artista japonesa» (EN "the Japanese artist").
- 025 ¶5: «sugieren protectora y depredadora a la vez» → «evocan a la vez protección y depredación». The old phrase was ungrammatical. It stays reported speech, since the ES page words it differently.
- 026 ¶9: «que cruza el extremo del museo» → «que pasa sobre el extremo» (EN "crosses over the end").
- 027 ¶6: «un rubor rojo» → «un reflejo rojizo» (natural Spanish for "a blush of red").
- 029 ¶1: «no tenía paciencia para hablar de» → «no soportaba que se hablara de». The old version meant he didn't want to talk. EN: "had no patience for talk of".
- 029 ¶2: «un muelle de trabajo» → «un muelle portuario» (see 004).

Bridges:
- 009 H>018: «…asómese al balcón de la segunda planta frente a la doscientos cuatro, y en el de la trescientos cuatro escuche…» → «…asómese al balcón de la segunda planta frente a la sala doscientos cuatro. En el de la trescientos cuatro, escuche…». The new version names «sala» for 204 and splits the sentence. It is 46 words, the same as the English.
- 015 E>017: «asómese al Serra desde el balcón frente a la doscientos cuatro… e inicie en él» → «mire el Serra desde el balcón frente a la sala doscientos cuatro… y, dentro, inicie». This is clearer, and it is 46/46 words.

## Quotations verified by me this session (WebFetch, one page at a time)
- Teachers' guide (3 reads), rutas-expres, obras/mama, obras/la-materia-del-tiempo, el-edificio/el-exterior, el-edificio/el-interior, obras/consejo-al-espacio-v, obras/instalacion-para-bilbao, and El Independiente 2017.
- Confirmed verbatim:
  - 004 «la plaza y la entrada principal del Museo se encuentran enfilando la calle Iparragirre»
  - 005, both quotes
  - 008 Holzer panels, «DIGO TU NOMBRE» / «GUARDO TU ROPA»
  - 009 «una enorme galería libre de columnas», «la totalidad de la sala es parte del campo escultural», «siempre imprevistos»
  - 009 / 012 «desde la relativa sencillez de una elipse doble hasta la complejidad de una espiral», «secciones de toros y esferas»
  - 013 «una progresión del tiempo»
  - 015 Chillida, all quotes, including «Construir es crear en el espacio.» (Chillida to Mario Terès)
  - 027 «lo integra, de forma eficaz, en el edificio»
  - 002 Lucía Agirre «Existe la idea de que Puppy se quedó en Bilbao por aclamación popular» / «No es así.» and the paper's «recién llegado de Australia»
- Not re-verified by me: the translator says these were verified, and I found nothing suspicious.
  - 006 ZERO
  - 017 CATIA
  - 021
  - 022 Kapoor
  - 023 Nakaya
  - 024 Klein
  - 026 titanium
  - 028 Isozaki stairs and «arquitectos de renombre internacional»

## For the lead
- BRIEF.md's line «ES "Mamá"? NO — the museum keeps "Maman"» is wrong. See point 3.
- 012 and 010: if you'd rather not use «trastornado» / «trastocado», the only safe alternative is reported speech with no «». An own translation in «» is not safe, because the museum publishes these words in Spanish.
- 018 H>025 still says «salga» rather than «salga del museo». There's no room within the length limit, and it is unambiguous in context.
- `bridges_001-029.txt` is now stale. Delete it or overwrite it with `bridges.txt` if the pipeline reads it.

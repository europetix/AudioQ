# ES review, Barcelona Cathedral 001–036 (edition of 14 Nov 2026)

Independent review of es/001–036.json and es/bridges.txt. I compared every track sentence by sentence with the current English, did a navigation scan of every last paragraph, and checked every bridge.

**Result:** `assemble.py --check … es` passes for all 36 tracks (exit 0). I found no errors of fact, hedging or navigation. The changes below are one late source change, the cathedral's own names, and wording for the ear.

## Late source change
- **005** (English changed at 10:25, per the lead): "So Gaudí did draw for this front. On paper only." Before: "Así que Gaudí sí trabajó en esta fachada. Sobre el papel." After: "Así que Gaudí sí dibujó para esta fachada. Solo sobre el papel." No other track or bridge changed after the translator's work. The only newer file is 031 (10:20), and the translator's notes already cover it.

## The cathedral's own names (lead note and brief rule 3)
I checked catedralbcn.org/es/visita-turistica/espacios-visitables/ with one WebFetch.
- **Lepanto chapel**: titles and cues used the short "La capilla de Lepanto". The site's name is "Capilla del Santo Cristo de Lepanto", and the body already used it. I changed it to **"La capilla del Santo Cristo de Lepanto"** everywhere it is used as a place name:
  - 006 cue
  - 007 title and cue to 008
  - 008 title
  - 027 body ("de la capilla del Santo Cristo de Lepanto a la cripta")
- **Pietat door** (rule 3 lists it as a name to take from the site): the site says "puerta de la Piedad". I changed "la puerta de la Pietat" to **"la puerta de la Piedad"** in 030 (last paragraph), 031 @where and 031 body. It is not used in any title, cue or bridge.
- Unchanged, as required by brief rule 3: Sant Iu (site: "San Ivo") and Santa Llúcia (site: "Santa Lucía").
- Unchanged, and **for the lead to decide**: the site writes "puerta de Santa Eulalia". The ES text spells the saint "Eulàlia" everywhere (about forty times, in the 036 title, cues and bridges). The two spellings sound the same, so I kept "Eulàlia" for consistency. If the lead wants the site's spelling, switch all of them at once and not only the door. That would also avoid the grave accent with the es-MX voice.
- Kept as they are, and matching the site: Las terrazas, El coro, Sala Capitular, Memoria judía, El claustro, La cripta.

## Wording and accuracy (track: before → after, why)
- 001: "algo más si espera el ascensor" → "algo más si hay que esperar el ascensor". The old wording was ambiguous.
- 002: "Mire al pie de la muralla" → "Mire abajo, al pie de la muralla". Restores "look down".
- 006: "se eleva cuarenta y un metros" → "alcanza cuarenta y un metros". More natural.
- 006: "A la vuelta, el dinero parece que se acabó." → "A la vuelta, al parecer, se acabó el dinero." Clearer hedge.
- 006: "Mire las nervaduras" → "Mire arriba, a las nervaduras". Restores "look up".
- 007: "lo oscuro que es" → "lo oscuro que está". It is a state, not a quality.
- 007: "construyó esta sala en 1407 para las reuniones de los canónigos" → "construyó en 1407 esta sala de reuniones de los canónigos". Shortened to make room for the longer chapel name.
- 007: "Y cuenta la historia que" → "Cuenta la historia que". Same reason, and the hedge is kept.
- 010: "Mire su alta vidriera" → "Levante la vista hacia su alta vidriera". Restores "look up".
- 011: "donde aquella cara giraba los ojos" → "donde antaño aquella cara movía los ojos". Restores "once", and "giraba" was odd.
- 016: "La fila baja de asientos llegó… Lo ganó un tallista" → "La sillería baja llegó… El encargo lo ganó un tallista". The "Lo" had no antecedent ("that job"), and "sillería baja" matches "sillería alta".
- 017 @where: "Nunca levante un asiento usted." → "Nunca levante usted un asiento." Word order.
- 017: "los de vista aguda" → "los de buen ojo". Idiomatic for "keen-eyed".
- 018: "Solo una docena, más o menos, se sentaron bajo ellos." → "Solo unos doce caballeros se sentaron realmente bajo ellos." Restores "knights" and "actually".
- 021: "la deja aún abierta" → "aún deja abierta la cuestión". "la" had no clear antecedent.
- 028: "Deja ambas abiertas." → "Deja abiertas ambas posibilidades." "ambas" had no noun.
- 028: "quizá haya sobrevivido" → "quizá sobrevivió". Saves one word to stay within the limit.
- 029: "a la pequeña bóveda." → "a la pequeña bóveda sobre la fuente." Restores "over the fountain".
- 032: "sobre una losa con cuatro columnas" → "sobre una losa apoyada en cuatro columnas". "over four columns" means the slab rests on them.

## Quotations
- **019, 1519 relation**: re-checked with one WebFetch of the cited Knighton PDF (CMIB 39, p. 169). The wording is confirmed exactly: "y luego los cantores de la capilla, y el gran órgano, cantaron muy solemnemente vísperas y completas". I kept the original wording, with "en español" dropped as rule 11 allows.
- All other quotes are faithful translations of the English, with their attributions kept. 016 and 017 keep "en catalán (antiguo)", and 032 keeps "molt mediocre". I re-verified no other quote.

## Navigation and bridges
- Every last paragraph has the same places, order, directions and conditions as the English. All 38 cues match the destination's translated title exactly, and the order of destinations matches the English.
- Bridges: 15/15, with the same keys as the English. Each starts "En esta versión corta,", none is longer than the English (word count), and each cue matches the destination title. There are no Lepanto or Pietat names in the bridges, so they needed no changes. I did not change any bridge.
- 030 E/H>034 omits the English "Inside,". I tried "Dentro, busque…", but that makes the line longer than the English (42 > 39 words), so I left it. "busque el cuadro" after "hasta el museo" still sends the listener in.

## Confirmed, no change
- 031 "El canónigo que lo pagó": he kneels in the relief, so he paid for the carving (lead's decision).
- Tour names: "el recorrido completo", "la versión esencial", "los imprescindibles".
- The NEVER list was checked: marble, not alabaster, for Eulàlia's tomb. 1448 is the cloister. Gaudí built nothing and drew on paper only. Lepanto is kept as tradition and story. The thirteen geese are "según la tradición". There is no UNESCO.

## For the lead
1. Spelling of Eulàlia versus the site's "Eulalia" (see above). This needs a decision. It does not block, because the two sound the same.
2. Spot-check the es-MX voice on the Catalan names, as the translator noted.

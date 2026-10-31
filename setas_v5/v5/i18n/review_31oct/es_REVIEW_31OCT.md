# ES review, Setas de Sevilla edition 5.1, tracks 001–021 and bridges (31 Oct 2026, independent editor)

Verdict: READY. I checked all 21 tracks sentence by sentence against the 5.1 English. I concentrated on the new tracks 006, 018 and 021 and on the expanded tracks 002, 004, 005, 007–013, 015, 016 and 020. Every paragraph was diffed against the reviewed 5.0 EN/ES.

Navigation is accurate in every track and every bridge. Facts, hedges and conditionals match the English. I found no additions, and every sentence that 5.1 dropped is gone from the ES.

I made 8 small edits to tracks and 2 to bridges. Two bridges were longer than the English, and both are now fixed.

`assemble.py --check … es`: all 21 tracks OK after the edits. 016 is the tightest, at 202 of 202 words.

## Changes to tracks (track: before → after, why)
- 002: "Eso es lo que va a recorrer." → "Lo que descubrieron es lo que va a recorrer." After "El estacionamiento nunca se construyó", the word "Eso" could be heard as the car park. The English says "What they uncovered".
- 004: "había un barrio de sus casas" → "había un barrio de casas". This is more natural. The meaning ("a quarter of its houses") is unchanged.
- 005: "La Casa de la Ninfa, un espíritu de manantiales y ríos." → "La Casa de la Ninfa. Una ninfa es un espíritu de manantiales y ríos." The old apposition made the house sound like the spirit.
- 006: "Se recompuso pieza a pieza en la pared" → "Se recompuso y se montó en la pared". The English says it was pieced back together and set on the wall. The old wording implied it was reassembled on the wall itself.
- 009: "Sevilla preguntó a arquitectos de todo el mundo." → "Sevilla lanzó una pregunta a arquitectos…". "Preguntó" with no object was incomplete before the question that follows.
- 009: "En junio se supo el ganador" → "En junio de ese año se supo el ganador". The English says "That June", meaning June 2004. Bare "En junio" was vague.
- 016: "Sacyr la considera parte de una renovación completa" → "Sacyr la presenta como parte de…". The English says "Sacyr calls it". "Presenta como" keeps the attribution and does not suggest an opinion.
- 020: "siga las indicaciones hasta la calle" → "siga las indicaciones para bajar a la calle". The way out: the English says "follow the signs *down* to the street".

## Changes to bridges.txt
- 001 H>009 was 41 words against 40 in the English. "Suba en el ascensor y empiece" → "Suba en ascensor y empiece". It is now 40.
- 013 H>020 was 37 words against 35. "omita las paradas de la pasarela" → "omita las paradas de pasarela", and "Escuche allí la última parada:" → "Escuche allí la última:". It is now 35. The route is unchanged: the way down, past the exhibition, to the Plaza Mayor, the big raised square under the parasols.
- All 5 lines are now ≤ the English: 38/38, 40/40, 38/40, 35/35, 38/38. Keys are identical to the English (001 E>008, 001 H>009, 009 H>013, 013 H>020, 014 E>017). Every line starts "En esta versión corta,", and every English line has exactly one ES line. bridges_001-021.txt was not touched.

## Navigation scan (all 21 last paragraphs, @titles)
- Every last paragraph has the same places, order, levels and things to look for as the English:
  - the door of the Antiquarium
  - the first good view down into the remains
  - the label for the Casa de la Columna
  - the mosaic with two birds
  - the casa almohade label, with its "si ya pasó por ella…" fallback
  - the exit signs to the lifts beside the Antiquarium entrance, the Mirador access
  - "al cerrarse las puertas" and "mientras sale a la pasarela"
  - the Giralda in clear view
  - facing west with the Giralda on your left
  - the steps up to the Mirador
  - back down the steps toward the way down
  - the Extras and the next main stop past the exhibition
  - the Feeling Sevilla door
  - at the end of the way down, the Plaza Mayor with the timber overhead
  - a quiet spot away from the way down
  - the way out, now "para bajar a la calle, por la escalera fija o la mecánica"
  - the final Extra for full-tour listeners only
- Every spoken next-stop title matches the target track's ES @title.
- @titles start with the same place as the English: Antiquarium, Plaza de la Encarnación, Setas, Pasarela, Mirador 360º, La bajada, Plaza Mayor, "Pasarela · Extra ·", "Feeling Sevilla · Extra ·" and "Después de la visita · Extra ·" (021, as the brief asks). The opening title has no place.
- Every "if…" is kept: 001 closed Antiquarium, 004 "si la encuentra", 006 label match and "si ya pasó", 015 film or not, 016 "o si no entra", 018 "si puede ver uno de los troncos", 020 full tour.

## TTS, style, neutrality
- Body and bridges contain none of + & % · × ° º ² ; ( ) and no dashes. "Mirador 360º" appears only in the 013 @title and @where. In speech it is "Mirador trescientos sesenta" (001, 012, bridge 009 H>013). Regnal number: "Fernando Tercero". "Treinta por ciento" is written in words.
- Usted throughout. I found no coger, vale, vosotros, móvil, ordenador, celular, aparcamiento or coche. The ES uses "estacionamiento", "teléfono", "vehículos estacionados" and "inundación", not "riada".
- Delivery tags are in the same order and paragraphs as the English, as the checker confirms.

## Quotations
- 014 «como a un Cristo dos pistolas» and «una moderna catedral urbana» were re-verified today with one WebFetch of Público, "El legado de Monteseirín": https://www.publico.es/actualidad/legado-monteseirin.html. Both are verbatim.
- 011 «Hispalis, puerto romano de la Bética» is unchanged from 5.0. It was verified in the 30 Oct review.
- None of the new 5.1 material (006, 008, 015, 016, 017, 018, 019, 021) puts an originally Spanish source in quotation marks. These are all in reported speech without quotes:
  - the operator
  - Sacyr
  - de la Peña
  - the Mercasa study
  - the regional tourism office
  - the ZARCH study
  - the city on the ficus
- 018 "indignados" is the original term, so it needs no gloss and no quotes. The quotes from non-Spanish sources (Mayer, Arup, MoMA, Fraunhofer/Kruse, Kallio, Rowan Moore) are translated inside « », as rule 11 allows.

## For the lead (no action needed)
- Translator note checked: 010 "Early in the 1400s" → "A principios del siglo quince" is correct for 5.1. The old "1401" is gone.
- 012 "Los ingenieros, Arup, también trabajaron…" is a little stiff, but it is correct and has no word budget left (278/280). I left it.
- 014 "icono": Mexican usage prefers "ícono", but the RAE accepts both. I left it, as the 5.0 review did.
- 019 opens "Junto a los ascensores, escuchó…", which refers back to 008. The Highlights version never plays 019, and Essential does play 008, so this is consistent. It mirrors the English.

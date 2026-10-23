# ES review: Bernabéu tracks 001–028

Reviewer: independent editor. I read every track sentence by sentence against the current English. I checked facts, directions, quotations (rule 11), usted, football idiom, Latin American/Spain neutrality and TTS safety.
`assemble.py --check … es` passes for all 28 tracks after the edits. Backup of the translator's files: scratchpad/es_review_bak/.

## Verdict
Ready. The translation was accurate and natural. No direction number or zone was wrong. The edits fix one out-of-date sentence (008, after the English changed), a few ambiguous directions, a few ambiguous pronouns, and spell out three names for the voice.

## Sync with the English
- 008 ¶3: the English changed after translation. "En diciembre de 1985, el Real Madrid perdió por cinco goles a uno en casa del Borussia Mönchengladbach… Ya aquí, Valdano marcó…" → "En el otoño de 1985, el Real Madrid perdió por cinco goles a uno en casa del Borussia Mönchengladbach, en la Copa de la UEFA. De vuelta aquí, en diciembre, Valdano marcó dos de cabeza…". The first leg is now in autumn and the return leg in December, as in the English.
- I checked file times: 008 is the only English track changed after the Spanish was written (06:47 against 06:46).

## B. Directions scan (all 28)
- Last paragraphs 001–028 match the English. Numbers checked: 001 and 003 nueve; 007 and 008 veintitrés and veintisiete; 019, 020 and 021 veintidós; 020 veintiuno; 022 cuatro and veintisiete; 025 veintiséis.
- Case instructions in 001, 003, 007, 008 and 019–022 are exact: match day and the day before, museum first, "if it's closed today", "if you haven't been up to the top tier yet".
- Fixed: in 007, 008 and 021, "Si hoy está cerrado…" came straight after a sentence naming both the museum and the dressing room (both masculine). It now says "Si el vestuario está cerrado hoy…", so the listener knows which room is meant. The conditions and numbers are unchanged.
- @title zones match the glossary: Exterior, Panorámica, Museo, Sala de trofeos, Vestuario, Banquillos, Sala de prensa, Tienda. Extras 008, 020, 021, 022 and 026 use "· Extra ·". 001 and 028 have no zone.

## Quotations
- 019 AFP: I re-checked both sources (WebFetch, 23 Oct 2026). Both carry the exact wording "Y el Real Madrid no está donde no se le respeta", credited to AFP. Teletica (AFP byline, 28 Oct 2024): https://www.teletica.com/internacional/real-madrid-gana-premio-al-mejor-equipo-del-mundo-en-gala-de-la-que-se-ausento_369952 ; Soccerway (AFP): https://es.soccerway.com/noticias/futbol-laliga-ea-sports-no-es-bueno-para-el-futbol-dice-de-la-fuente-sobre-el-boicot-del-real-madrid/ltmPpw1t . The translator had dropped the opening "Y". I restored it, so the quote is now verbatim: "Y el Real Madrid no está donde no se le respeta". The attribution stays "Una fuente del club dio a la agencia AFP…", as in the English.
  FOR THE LEAD: both Spanish outlets credit the words to "el club madrileño" (the club itself, speaking to AFP), not to "a source at the club". The English and all three translations say "a source at the club". This is a small attribution difference in the English, not in the ES.
- 009: "En palabras del propio club, el Real Madrid es un club propiedad de sus socios" presented a back-translation as the club's own words. I changed it to reported speech: "Según el propio club, el Real Madrid es propiedad de sus socios."
- The rest are fine. 003 faraónico, 005, 007, 011, 023 and 026 are reported speech without quotation marks. 016 "minuto noventa y Ramos" is the Spanish fan phrase that the English itself quotes. 012 has the English lyric and song title.

## TTS: gmp, L35, S10, Ribas y Ribas (RESPELL=0 for ES, so the voice gets the raw text)
- 002 "gmp" → "ge eme pe". A Spanish voice may try to read a consonant cluster as a word, and the letter names make it certain.
- 002 "L35" → "ele treinta y cinco". This is how the studio name is said in Spanish.
- 028 "S10" → "ese diez". This is how Madrid says the bus line. Without the change it could be read with the English letter name or as "es diez".
- "Ribas y Ribas" (002) reads naturally, and it is how the studio's name "Ribas & Ribas" is said aloud. Kept.
- Also: 010 "AC Milan" → "el Milan". This is the usual Spanish name and avoids "AC". 020 "CD Tacón" → "Club Deportivo Tacón", which expands the abbreviation. Kept, because Spanish says them as words or letters naturally: UEFA, FIFA, NFL, AFP.

## Changes (track: before → after, why)
- 001: "cada parada le dirá adónde ir" → "…adónde ir después". This is closer to "where to go next". Also "espere un suelo desnudo, no un prado" → "espere ver un suelo desnudo, no hierba", because "prado" for "lawn" sounded odd.
- 002: TTS spellings as above. Also "Más de un año, en las temporadas…" → "Durante más de un año…", which is grammatical. "En junio de 2026, las cuentas…" → "Al cierre de junio de 2026…", which keeps the "by June", cumulative sense. "Esos huecos están a propósito" → "…están ahí a propósito".
- 003: "lo califica de faraónico" → "califica el proyecto de faraónico", because "lo" had no clear referent. "España salía hacía pocos años de su guerra civil, en la que él luchó…" → "Hacía pocos años que había terminado la guerra civil española, en la que él había luchado…", which is more natural and has the correct tense. "más que nunca después" → "una cifra nunca igualada después". In the directions, "reproduzca el número nueve" → "reproduzca en su lugar el número nueve", which keeps "instead".
- 004 @where: "el tercer nivel según el folleto" → "la del tercer anfiteatro según el folleto". This is the Spanish brochure's own wording, and it matches the body's "tercera grada". Also "simplemente llénese los ojos" → "simplemente disfrute de lo que ve", because the first was not idiomatic.
- 005: "todas de otros clubes" → "todas entre otros clubes", which is clearer that Madrid did not play. "Su entrenador esa noche" → "El entrenador del Inter esa noche", because "Su" could mean Inter or Bayern.
- 006: "y en otros dos enfrente" → "y en otras dos enfrente". "Two more" means two more towers, so "torres" takes the feminine. "mucho menos que con acero corriente" → "mucho menos de lo que exigiría el acero corriente", which is clearer. "en el añadido" → "en el tiempo añadido", which is neutral for Mexico and Spain.
- 007: "Lo llama el hipogeo, como las galerías…" → "…, el nombre de las galerías…", which keeps "borrowing the name". "la sociedad del estadio del club" → "la sociedad del club que gestiona el estadio". The directions fix is described above.
- 008: the sync is described above. "La hizo famosa…" → "La expresión la hizo famosa…". The feminine "la" had no antecedent, because the previous sentence used "un nombre". "para el pavor de…" → "para hablar del pavor a…". The directions fix is described above.
- 009: the quote handling is described above.
- 010: "AC Milan" → "Milan". "La UEFA aún la registra como récord" → "…registra esa racha como récord", because "la" had no referent.
- 011: "con una vieja cara" → "con una cara conocida", because the first was a calque of "old face".
- 012 @title: "Las seis de Gento, y el Ye-yé" → no comma, as Spanish punctuation requires. Also "estuvo solo en los libros de récords" → "tuvo un récord en solitario", which is idiomatic. "el largo hueco previo" → "el largo hueco que la precede".
- 013 @title: "Treinta y dos años, y La Séptima" → "Treinta y dos años y luego La Séptima". Also "no pudo ganar su mayor trofeo" → "…el mayor trofeo europeo", because "su" was ambiguous. "la primera que vieron ganar" → "…ganar a su club".
- 014: "tres goles a cero" → "por tres goles a cero". "el campo donde… vencieron" → "el mismo campo donde… habían vencido", which keeps "the very ground" and fixes the tense. "el capitán que levantó" → "que levantaría", to agree with "sería".
- 015: "frente al presidente en ejercicio" → "tras derrotar al presidente en ejercicio". The gerund calque "con uno de los futbolistas… llegando cada verano" → "Luego se hizo costumbre: cada verano llegaba uno de…". "se reconstruyó con él" → "…bajo su mandato".
- 016: "Un gol abajo" → "Perdiendo por un gol", which is neutral across regions. The run-on "…de penalti, cuatro goles a uno para…" was split: "…de penalti. Cuatro goles a uno para…".
- 017 @title: comma removed, as in 012. Also "Presente en todo ello estaba Cristiano Ronaldo" → "Y en el centro de todo, Cristiano Ronaldo", because the first was stiff. "Era la primera vez" → "Fue la primera vez".
- 018: "Dos goles al final" → "Dos goles en el tramo final". "que hizo costumbre de lo imposible" → "que convirtió lo imposible en costumbre", which is idiomatic.
- 019: the AFP "Y" is restored as described above. Also "además de los dos ordinarios ganados aquí" → "además de los dos que ya había ganado aquí". "se ha ganado doce veces con la camiseta de este club, por ocho hombres distintos" → "lo han ganado doce veces jugadores de este club, ocho hombres distintos en total", because the passive was awkward.
- 020: "el Real Madrid no lo tuvo" → "no tuvo equipo femenino", which makes it explicit and keeps "well over a century" as "mucho más de un siglo". "CD Tacón" → "Club Deportivo Tacón". "O siga al vestuario" → "O siga directamente al vestuario", which keeps "straight on".
- 021: "La primera Liga, en la temporada…, la ganó invicto" → "La primera Liga fue en la temporada de 1931 a 1932, y la ganó invicto". "república" → "República". "volvió a ser el Madrid Football Club" → "volvió a llamarse Madrid Football Club". The world-club sentence was reworded: "Súmele nueve mundiales de clubes. El club los cuenta uniendo la antigua Copa Intercontinental y los torneos de clubes de la FIFA." The club's-own-count hedge is kept. "donde comprarla es decisión suya" → "donde comprar la foto…", because "la" had no referent. The directions fix is described above.
- 022: "se queda en la sala" → "se queda en el vestuario".
- 023: "con un gol en contra ante el Paris Saint-Germain" → "perdiendo por un gol ante el Paris Saint-Germain".
- 024: "Esos catorce" → "Esos catorce títulos". "en mayo siguiente" → "en mayo del año siguiente". "dio la vuelta a todo al final" → "remontó en el último momento".
- 025 @title: "Las remontadas finales" → "Las remontadas de última hora", because "finales" also means "finals". Also "perdía de dos en el global" → "perdía por dos goles en el global". "En el añadido" → "En el tiempo añadido".
- 027: "se convirtió en nombre" → "…en su nombre". "Las cuentas de la temporada" → "Las cuentas del club de la temporada". "lo ha puesto en cabeza" → "ha puesto al Real Madrid en cabeza", because "lo" was ambiguous. Also "hacia la puerta" → "hasta la puerta".
- 028 @title: "La salida, y la despedida" → no comma. Also "el opuesto a su entrada" → "el lado opuesto a donde entró". "S10" → "ese diez".
- 026: no change.

## For the lead
- 019 attribution: the Spanish sources say the club itself spoke to AFP, not "a source at the club" (see Quotations). The ES follows the English, as instructed.
- Length: four tracks are now at or within one word of the English limit: 006 305/305, 008 204/204, 021 222/223 and 027 294/295. They pass the check but miss the "about 5% shorter" aim. 002 grew to 324/328 because of the spelled-out names.
- The spellings "ge eme pe", "ele treinta y cinco" and "ese diez" are written for the voice. If the Spanish text is ever shown on screen as a transcript, it should show gmp, L35 and S10 instead.

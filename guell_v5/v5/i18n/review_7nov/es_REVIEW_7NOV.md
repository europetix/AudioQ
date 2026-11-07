# ES review: Park Güell 001–045 (7 Nov 2026 edition), independent editor

**Verdict: ready**, provided the lead accepts the García Ávila correction (point 1 under "For the lead").

## What I checked
- I read all 45 tracks (@title, @where and body) sentence by sentence against `guell_v5/v5/tracks/NNN.perf.txt`, and all 21 bridges against `v5/bridges/*.txt`.
- `assemble.py --check … es` passes for all 45 (exit 0). Headroom is zero in 004, 024, 025, 032, 035, 037 and 038 (and 1 word in 018, 028, 044, 045). Any later edit there must be word-neutral.
- A script checked every in-body cue and every bridge cue. Each one matches an ES @title exactly (with " — " read as " · "), and each points to the same destination track, in the same order, as the English. All 21 bridges have the English key, start with "En esta versión corta,", end with the exact ES cue, and are no longer than the English line (word count).
- Navigation: every last paragraph has the same places, the same order and the same things to look for. Left and right, "the one without the tower", "on your right as you face the stairway", "on your right as you look out over the bench" and "before the check" all match the English. Nothing is added or dropped.
- Formal "usted" is used throughout. There are no TTS-unsafe symbols (+ & % · × ; ( ) appear nowhere outside the cue separator). Regnal numbers are in words ("Alfonso trece") and so are centuries ("siglo veinte", "siglo dieciocho"). Years are digits. The only other digits are inside quotes, as in the English ("60", "50 pesetas", "86"). The NEVER list is respected, and nothing is put in Gaudí's mouth.
- Backup of the files as received: `scratchpad/es_backup_before_review/`. `es/bridges_001-045.txt` is untouched; `es/bridges.txt` is the edited file.

## Quotes kept in the original Spanish (WebFetch, one page at a time, 7 Nov 2026)
| Track | Page | Result |
|---|---|---|
| 004, 006, 010 | core.ac.uk/download/230705175.pdf | All three confirmed verbatim ("…mayoritariamente de depósitos sobrantes y defectuosos de fábricas de cerámica", "sufrieron muchos cambios y mutilaciones", "La obra se inicia en 1900 con la construcción de los caminos") |
| 014 | Andruet PDF, fundacionantoniogaudi.org | Confirmed: "excelentes condiciones higiénicas", "renombre de barrio de la salud" (the ES gives this as reported speech, as before), and "torres donde vivir cómoda e independientemente los habitantes de Barcelona sin dejar de vista sus negocios habituales". The page really says "sin dejar de vista". |
| 017, 020 | park ES flyer PDF | Both confirmed verbatim ("un caño en forma de cabeza de serpiente sobre el escudo de Cataluña", "un trípode que parece formado por tres serpientes") |
| 017, 020, 021, 022 | revistes.ub.edu Ar@cne article | All six phrases confirmed verbatim. **But the byline is "Manuel-Blas García Ávila"** (artist and designer), not María-Belén. See point 1 for the lead. |
| 027 | timeout.es | "fiel al estilo de su maestro" confirmed. The page spells the architect "Batllever". The ES keeps the English's "Batllevell", which is outside the quote. |

None needed converting to translation or reported speech.

## Changes requested by the lead
| Track | Before | After | Why |
|---|---|---|---|
| 001 | "La versión completa dura… la esencial… y la de lo más destacado…" | "El recorrido completo dura… la versión esencial… y los imprescindibles…" | House names for the tour lengths |
| 006, 012, 024, 034 | "Si hace la versión completa" | "Si hace el recorrido completo" | Same (word-neutral) |
| 039 | "…el Pórtico de la Lavandera, aunque las páginas del parque en inglés lo llaman Laundry Room Portico." | "…el Pórtico de la Lavandera." | Lead: drop the alternative-name clause. The Catalan name is now given once, followed by the official ES name. |
| 018 | "algunos autores… ven en esta criatura" | "…han visto en esta criatura" | The English is now past ("have seen") |
| 017 | "Una estudiosa de este parque" | "Un estudioso de este parque" | The lead approved "Una estudiosa", but the article's byline is a man (see point 1) |

## Other changes
| Track | Before | After | Why |
|---|---|---|---|
| 001 @where | "justo después de la puerta" | "justo dentro de la puerta" | The English says "just inside". It now matches the phrase used everywhere else. |
| 001 | "El Park Güell no nació como parque." | "El Park Güell nunca se pensó como parque." | "was never meant to be" |
| 001 | "uno de ellos, del guarda" | "uno de ellos, el del guarda" | Grammar |
| 001 | "cada parada le dice adónde ir" | "…adónde ir después" | "where to go next" |
| 001 | "Mire hacia la puerta y el muro" | "Vuélvase hacia la puerta y el muro" | "Turn to face": the listener arrives facing the stairway |
| 004 | "Gaudí la usó por primera vez…" | "Gaudí usó la cerámica rota por primera vez…" | "la" could be heard as the tile of the previous sentence. Paid for by "A los guías [turísticos]". |
| 007 | "Pequeña como es, esta casa se hizo con gran cuidado." | "Aunque es pequeña, esta casa se hizo con gran esmero." | Calque |
| 011 | "cada columna sigue la trayectoria que quiere tomar la carga" | "cada columna se inclina hacia donde quiere ir la carga" | The English says the column "is tilted along" the load path |
| 015 | "Así que: una cima pelada…" | "Recapitulemos: una cima pelada…" | "Así que:" with a colon does not work aloud |
| 015 | "Cada comprador pagaba una cuota" | "Cada comprador debía pagar una cuota" | "had to pay" |
| 017 | "Mire un momento lo que hay aquí." / "casi todo el mundo mira" | "Deténgase un momento en lo que hay aquí." / "casi todos miran" | "Stop for a moment on what's here". The second change keeps the word count. |
| 018 | "Suba unos escalones sobre el dragón" | "Suba unos escalones por encima del dragón" | "sobre el dragón" can be heard as "climb onto the dragon" |
| 020, 021, 022 | "la investigadora María-Belén García Ávila" | "el investigador Manuel-Blas García Ávila" | Byline of the cited article (point 1) |
| 021 | "lo dijo en 2023 más claro" | "fue más tajante en 2023" | "more bluntly" |
| 021 | "la fachada se asentaba" | "la fachada estaba cediendo" | "settling" means sinking. "se asentaba" can be heard as "was being settled". |
| 021 | "construido antes que sus clientes" | "construido antes de tener clientes" | Clearer to the ear |
| 023 | "Llévese el nombre de Jujol." | "Quédese con el nombre de Jujol." | Idiom |
| 025 | "Su agua viene de minas de la colina." | "Su agua sale de galerías de la colina." | In Spanish, "minas" suggests ore mines. These are water galleries. |
| 026 | "desde donde se ven de un lado a otro" | "desde donde pueda verlos de lado a lado" | Clumsy and ambiguous ("where you can see across them") |
| 028 | "firmados Gaudí" | "firmados por Gaudí" | Spanish grammar. This is a translated Catalan quote. |
| 028 | "ningún comprador vino" | "ningún comprador apareció" | Idiom |
| 028 | "Siga con la casa rosa a la vista:" | "Quédese con la casa rosa a la vista:" | Navigation: "Siga" sounds like "walk on". 029 is heard at the same spot. |
| 031 | "El parque cuenta aquí veinticinco tipos de aves" | "El parque registra aquí…" | "cuenta" is ambiguous (counts / tells) |
| 032 | "esto era el Teatro Griego. Después fue \"rebautizada…\"" / "con las terrazas alrededor como gradas" | "esta plaza era el Teatro Griego…" / "con las terrazas como gradas" | Gender agreement with "rebautizada". The second change keeps the word count. |
| 033 | "donde corre el largo banco" | "donde se extiende el largo banco" | Ear |
| 035 | "Quédese en el banco y mire la ciudad" | "Quédese junto al banco y mire hacia la ciudad" | The English line is identical to 034's. The Spanish is now identical too. |
| 037 | "a unos ciento ochenta metros" / "un periódico barcelonés, el Diario de Barcelona" | "a unos ciento ochenta metros de altitud" / "un periódico, el Diario de Barcelona" | Height above sea level, not distance. The second change keeps the word count, since the newspaper's name already says Barcelona. |
| 040 | "Mírela de cerca, y lo que lleva." | "Mírela de cerca, y fíjese en lo que lleva." | Grammar |
| 042 | "La masía fue con el parque." | "La masía iba incluida." | "went with the park" means was included |
| 045 | "Ese junio murió Gaudí." / "salga cuando esté listo" | "Aquel junio…" / "salga cuando quiera" | Distant past. The second avoids a gendered "listo". |
| Bridges 015 H>018, 016 E>018 | "algo sobre las franjas" | "algo por encima de las franjas" | "algo sobre" can be heard as "something about the stripes" |
| Bridge 032 E>034 | "el borde de la plaza sobre la escalinata" | "…del lado de la escalinata" | "on the stairway side". It now matches 033. |

Considered and left as they are, because the English word budget has no room: 024 H>034 ("encima", with "tiled" dropped), 036 H>039 ("siga entre los pinos"), 034 "Entre sus marcas" (Jujol's), 038 "Mire los pinos".

## For the lead
1. **García Ávila's name and gender (EN error, affects all languages).** The Ar@cne article (revistes.ub.edu, download 42208/39309, 1 March 2023, DOI 10.1344/ara2023.276.42208) is signed "GARCÍA ÁVILA, Manuel-Blas", "Artista plástico y proyectista". The English tracks 020, 021 and 022 say "María-Belén García Ávila", with "she" in 020. So does the PLAN_V2 pronunciation table. In the ES I corrected the name and used the masculine ("el investigador", and "Un estudioso" in 017). Please fix the EN, FR and DE to match: DE 017 has "Eine Forscherin". Or tell me to revert.
2. **014 "sin dejar de vista"**: verified verbatim, but a Spanish listener will hear it as a slip by the guide ("perder de vista" is the idiom). "torres" (meaning villas) may also be heard as "towers". Keep the quote verbatim, as now, or switch to a translation?
3. 044 ("visitantes de pago", "gratis") is translated as written, as you approved.

# ES independent review: Real Alcázar de Sevilla, 001–035 and bridges (30 Oct 2026)

Verdict: **ready**. The check reports all 35 tracks OK after the edits (`assemble.py --check … es`). Assemble was not run without `--check`.

## Method
- Every track compared paragraph by paragraph with v5/tracks/NNN.perf.txt: facts, hedges, conditionals, map numbers, Spanish names, left/right, @title/@where.
- Last paragraph of all 35 compared with the English. Same rooms, same order, same left/right, same things to look for.
- All 10 bridge lines compared with v5/bridges/*.txt. Same keys, one line per English line, each starts "En esta versión corta,".
- Scan for symbols, Roman numerals, abbreviations, Spain-only/LatAm-only vocabulary, dashes and quotation marks. Nothing found apart from the verified quotes below.
- Usted throughout. Paragraph and tag order unchanged.

## Changes (before → after, why)
| Where | Before | After | Why |
|---|---|---|---|
| bridges 022 E>025 and 022 H>025 | "omita el frente de los jardines:" | "omita las paradas junto al muro del palacio y el Jardín del Príncipe:" | The English bridge now reads "skip the stops along the palace wall and the Jardín del Príncipe". Rest of each line unchanged (38 → steps → 39). |
| 007 P5 | "y se terminó a menos de dos años de esta inscripción" | "y se terminó en los dos años siguientes a esta inscripción" | The English now says "finished within two years after this inscription". The old wording could also mean "before" it. |
| 001 P5 | "La completa … la esencial … la de lo más destacado" | "El recorrido completo … la versión esencial … la de imprescindibles" | Version names made explicit. They follow the approved Uffizi ES guide (recorrido completo / versión esencial / imprescindibles). 001 is the only track that names the versions. Bridges use the generic "versión corta". |
| 016 P7, 017 P5 | "Gire a la derecha, con la fachada del palacio a su derecha, y camine…" | "Gire a la derecha, mantenga la fachada del palacio a su derecha y camine…" | Renders "keep the palace front on your right" exactly, as rule 9 asks. |
| 029 P3 | "En los Baños de María de Padilla" | "En los Baños de Doña María de Padilla" | One form for no. 34 everywhere (see below). |
| 034 @where | "la escalera al Cuarto Real Alto" | "la Escalera al Cuarto Real Alto" | Leaflet name for no. 19, as in 016. |
| 034 P2 | "Escúchelo al pie de la escalera…" | "Este breve Extra es para el pie de la escalera…" | Keeps the English Extra announcement and the glossary term "breve Extra". |
| 034 P1/P2 | "las estancias reales de arriba" / "están sobre el palacio de Pedro" | "las estancias reales altas" / "coronan el palacio de Pedro" | Trims to stay within the English word count (218/218). Meaning unchanged. |

## Space names
- **No. 34:** "Baños de Doña María de Padilla" is now the only form in titles, body text and bridges (016 H>022). The leaflet legend prints "Baños Doña María de Padilla". The English uses the "de" form, and so does the Alcázar's own teaching PDF (02-Itinerarios-y-Actividades.pdf). The lead accepted this form.
- **No. 19:** "Escalera al Cuarto Real Alto" wherever the leaflet name is used. The generic "la escalera" is kept where the English says "the stair".
- Every other number and Spanish name matches the English and the legend. @title/@where keep "Carlos V" and "Felipe II". Speech uses "Carlos Quinto" and "Felipe Segundo".

## Quotations, re-verified today (WebFetch, one page at a time, no CAPTCHA)
1. **007:** «El muy alto et muy noble et muy poderoso et muy conqueridor don Pedro por la gracia de Dios rey de Castilla et de León». It matches Marquer, *Anales de Historia del Arte* 23 (2013), verbatim: https://revistas.ucm.es/index.php/ANHA/article/download/42850/40706/62639
2. **014:** «la cuadra grande, que llaman media naranja». It matches Sandoval as quoted in García Parody & Caballero (2018), verbatim: https://dialnet.unirioja.es/descarga/articulo/7042473.pdf. The same page confirms "los desposó por palabras de presente", which the ES uses without quotation marks.
3. **022:** «No hay rigor histórico». It matches the teachers' note (nota 4), verbatim: https://alcazarsevilla.org/wp-content/uploads/2024/11/02-Itinerarios-y-Actividades.pdf. The same PDF confirms "la Sala de las Fiestas" (021).
- **010:** The Arabic greeting «Gloria a nuestro señor el sultán don Pedro, ayúdele Dios» faithfully renders the English. It also matches Marquer's Spanish (same URL). Fine under rule 11.
- **007 motto:** «no hay vencedor sino Dios» faithfully renders the English.
- **034 Pisano signature:** reported speech, which is correct.

## Game of Thrones
Spain-dub forms are used consistently: Juego de Tronos, Ellaria Arena (022 and 029), las Serpientes de Arena (028 and 029), Jaime Lannister / Jaime, los Jardines del Agua de Dorne, la casa Martell.

## For the lead
- **Version names:** please confirm that the app's ES labels for the three lengths are "Recorrido completo / Versión esencial / Imprescindibles". If they differ, 001 P5 needs the same wording as the app.
- **010 P1, left as is:** "en casi todos los zócalos" drops "in the building". The meaning holds, and adding the words would exceed the word count by 1.
- I found no added facts, no dropped hedges or conditionals, and no left/right errors. 028 "if the pavilion is still behind screens" → "Si el pabellón sigue cubierto por vallas de obra" is correct.
- Backup of the pre-review files: /tmp/claude-0/-home-claude/98e7af58-dd32-56e0-a687-5f082c01b624/scratchpad/es_backup_review/

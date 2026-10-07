# ES review — Pitti, 7 Oct 2026 (independent editor, neutral Spanish / Dalia es-MX)

Verdict: **ready to ship after these edits.** The 24 JSON tracks match the new English in meaning, hedges, fallbacks and
navigation. "The room marked Sala di X" is rendered the same way every time ("la sala con el letrero Sala di X").
All 24 tracks pass `assemble.py --check es` (exit 0). The 039/040 swap is correct: 039 is "Hacia el siglo veinte" and 040 is "La Rotonda di Palmieri".
Track 017 (new) was checked in full against the English. It is accurate and complete, and needed only one small wording fix.

## Part A — edits made (es/*.json)

### Meaning and navigation errors
| Track | Was | Now | Why |
|---|---|---|---|
| 019 where | "retírese para ver toda la **tabla**" | "aléjese un poco para ver todo el **cuadro**" | The Baldacchino is oil on canvas, not a panel. "Retírese" can also be heard as "leave". |
| 019 | "es el añadido del príncipe, no Rafael" | "…no **de** Rafael" | Grammar error that changed the meaning. |
| 019 | "como la Granduca" | "como la Madonna del Granduca" | Spoken Spanish needs the full name. |
| 016 | "So she's probably not a woman from a doorway" was missing | added "Así que seguramente no era una mujer vista en una puerta." | Restores a sentence that had been left out. |
| 016 | "el azul intenso" | "el azul ultramar intenso" | "Ultramarine" had been lost. |
| 018 | "No la pintó Rafael. / Rafael **la** pintó hacia 1506…" | "Rafael pintó a esta Virgen…" | The listener would hear "la" as the darkness. The line now also says "por la misma época que La Gravida" instead of "como La Gravida". |
| 018 | "lo que le espera" | "lo que le espera al Niño" | "Le" was ambiguous. |
| 023 | "La tradición ofrecía dos Juanes… Andrea no eligió ninguna" | "…daba a los pintores dos maneras de mostrar a Juan" | Gender agreement and closer to the English. |
| 027 | Vasari "dijo que era una cosa rara" | "la calificó de obra excepcional" | In Spanish "cosa rara" means "a strange thing". |
| 037 | "Un rey francés entra… convertido en gran espectáculo" | "…y el cuadro lo convierte en un gran espectáculo" | The old line said the king became the spectacle. |
| 037 | "pintar el pasado… Acaba de ver uno" | "un cuadro del pasado lejano solía ser un comentario sobre el presente" | "Uno" had no noun to refer to. |
| 040 | "bien vestidas" | "completamente vestidas" | "Bien vestidas" means well-dressed. The English says fully dressed. |
| 040 | "Ninguna figura supera su uña" | "Ninguna figura es más grande que una uña" | "Su" could mean her nail or yours. |
| 010 cue | "Omita las pistas de la Ilíada… con el nombre de su puerta" | "Omita las pistas de la Sala dell'Iliade… que llevan el nombre de su puerta" | Uses the door-sign name, matching the 002 tip. |
| 004 | "un taller **de corte**" | "un taller **de la corte**" | In a track about cutting stone, "taller de corte" sounds like a cutting workshop. |

### Naturalness and fidelity
- 002 title: aligned with the English, "Galleria delle Statue — Las primeras salas de la Galería Palatina".
- 002: "Así que no espere cuadros sueltos sobre paredes blancas". The old line, "un solo cuadro", could be heard as "only one painting".
- 002: "mire el letrero **sobre** la puerta".
- 002: "…Sala del Castagnoli, **que tiene** una gran mesa…" avoids saying "con… con" twice.
- 004: "figuras diminutas **que se mueven por** las habitaciones" ("moving through").
- 005: "**Guarde** su pista para esa sala" ("keep", not "leave").
- 007 where: "Aléjese" instead of "Retírese".
- 010: "techos planetarios" changed to "techos de las Salas de los Planetas", the term used in the other tracks.
- 015: "y luego otra vez, por un príncipe" changed to "y comprado de nuevo, más tarde, por un príncipe Médici".
- 016: "casi seguro" changed to "casi con certeza".
- 017: "baje la mirada, bajo las nubes" changed to "baje la vista, por debajo de las nubes", which avoids the repeated "baje… bajo".
- 018: "y así llegó al Pitti".
- 025: "con sus propias palabras".
- 027: "de este tipo", and "la última del recorrido de hoy" ("on today's route").
- 033: "una de las colecciones de Macchiaioli más ricas del mundo". The old wording could be heard as "the world of the Macchiaioli".
- 033: "Las propias salas son parte de la historia".
- 035: "quería que el escultor más famoso de Europa fijara su rostro en mármol", and "Si ha recorrido la Galería Palatina".
- 037: "Así formaba a sus alumnos".
- 038: "…más ricas del mundo" ("anywhere").

Left unchanged on purpose: the double gloss "Sala di Marte, la Sala de Marte" (020/023/025), which mirrors the English. Formal *usted* is consistent throughout.

## Part B — navigation scan, all 61 tracks (@where and final cue)

Room names, room numbers, directions and "look for…" descriptions match the English in every track. Palatine rooms use the
Italian door sign wherever the English @where or cue uses it. Where the English uses a gloss, Spanish uses a gloss too: 021 @where "salas de Saturno y de Marte" and 008 "Sala de la Ilíada".
I found no navigation errors. Minor wording issues in tracks outside the JSON set, listed only (not edited):

| Track | Sentence | Suggested fix |
|---|---|---|
| 042 cue | "donde el resto de la colección **rota**" | "donde el resto de la colección **se expone por turnos**". Heard aloud, "la colección rota" sounds like "the broken collection". |
| 041 cue | "Lo más antiguo y raro… la ropa… **Búsquelas** primero" | "**Busque esas prendas** primero". The pronoun has no matching noun. |
| 031 cue | "Queda un Tiziano más, el último cuadro…" | "Queda un Tiziano más **en esta sala**, …". The English says "in this room". |
| 030 cue | "…treinta y cinco años después: su retrato del escritor Pietro Aretino: un hombre…" | Replace the second colon with a comma. |
| 012 @where | "Retírese lo suficiente…" | "Aléjese lo suficiente…", consistent with 007 and 019. |
| 003 title | "La Sala Castagnoli" | "La sala del Castagnoli", to match the door sign used in its @where. |

Already noted by the translator, in the English and outside my scope: in 006, the @sources line ("Saturn room") contradicts the text ("Sala di Prometeo"), and the 006 @id still reads "Sala di Saturno".

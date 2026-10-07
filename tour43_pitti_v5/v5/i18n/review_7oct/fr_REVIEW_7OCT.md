# FR review, 7 Oct 2026 (independent native editor, voice Vivienne)

Verdict: **ready to assemble.** The meaning, hedges, fallbacks and navigation of all 24 JSON tracks match the new English, including
round B and the 039/040 swap (confirmed by title). Track 017 (new) is complete and accurate, and Vasari is in reported speech.
"Room marked Sala di X" is translated as "la salle marquée Sala di X" every time (13 of 13, same as the EN). Every Palatine room in a @where or cue line uses its
Italian door sign wherever the English does. `assemble.py --check … fr` passes for all 24 tracks.

## Part A: edits made (fr/*.json)
| Track | Change | Why |
|---|---|---|
| 002 title | "Antichambre et galerie des Statues" → "Les premières salles de la galerie Palatine" | Now matches the EN title |
| 002 body | "On doit d'abord ressentir la richesse." → "Il s'agit d'abord de ressentir la richesse." | Matches "you're meant to" more closely |
| 006 body | "au milieu de la vingtaine" → "Il avait alors environ vingt-cinq ans." | Calque, and ambiguous by ear next to "vers 1507". Wording now matches 019 |
| 010 cue | "Si elle est fermée" → "Si cette salle est fermée" | "elle" would have attached to "Sa piste" |
| 014 cue | "prêté ailleurs" → "en prêt" | More idiomatic |
| 015 cue | adds "la Madonna della Seggiola" before "la Vierge à la chaise" | Matches the EN and the Italian museum label |
| 016 body | "qu'il fut peint" → "que le tableau fut peint" | Unclear antecedent after "pommeaux" |
| 017 body | "gravées" → "incisées" | "scratched into the surface" |
| 018 body | "une vingtaine d'années" → "un peu plus de vingt ans" | "early twenties" |
| 019 body | "Il commence plutôt" → "Il entame plutôt" | Reads better aloud |
| 035 body | The attribution sentence is rewritten to say that the museum gives the head to Canova and workshop, and that only tradition gives it to the master himself | The old version was muddled and blurred the hedge |
| 036 body | "C'est l'homme qui" → "C'est lui qui" | More natural |
| 038 cue | "un minuscule panneau, des femmes sous…" → "un minuscule panneau avec des femmes sous…" | Awkward apposition (246/246) |
| 039 cue | "haut de douze centimètres seulement, des femmes assises" → "haut de douze centimètres, avec des femmes assises" | Same problem. "minuscule" already carries "only" (191/191) |
| 040 title | "La Rotonde de Palmieri" → "La Rotonda di Palmieri" | Now matches the EN title and the 039 cue |
| 040 body | "se renverse" → "s'adosse", "De toute façon" → "Quoi qu'il en soit", "Quand vous avez terminé" → "Quand vous aurez terminé" | Wrong nuance / register / tense |

Left as is, on purpose:
- "salle marquée": slightly literal, but clear and used consistently in 13 places, including 003, which is outside the JSON set.
- 027 "itinéraire du jour": consistent with 024, 026, 028 and 031.

## Part B: navigation scan of all 61 FR tracks (@where + final cue)
No room name, room number or direction differs from the English. No Palatine room is named in French where the English uses the door sign.
The following are outside the 24 JSON files and were not edited:
1. **041 cue**, "Les plus anciens et les plus rares sont toujours exposés.": the noun is missing, so the listener doesn't know what to look for.
   Fix: "Les vêtements les plus anciens et les plus rares sont toujours exposés."
2. **032 cue vs 043 cue / 044 @where + cue**: the same meeting place is called "atrium d'entrée" in 032 and "hall d'entrée" in 043 and 044.
   Fix: use "atrium d'entrée" in 043 and 044, or "hall d'entrée" in 032.
3. **003 cue** (minor), "écoutez sa piste là-bas": "là-bas" sounds odd when the table is right there. Fix: "écoutez sa piste devant elle."

## English oddities (FR mirrors the EN)
- 039: the EN mentions "In Room nineteen, look for one more Fattori…" before the closing "Before you go on to Room nineteen, look in Room eighteen…". The order reads backwards.
- 017: Vasari's "a Christ painted like Jupiter" is followed by "God the Father". This is faithful to the sources but may confuse listeners.

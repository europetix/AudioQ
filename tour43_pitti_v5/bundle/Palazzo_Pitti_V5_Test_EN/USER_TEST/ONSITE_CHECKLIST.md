# On-site checklist (V5.1, 61 tracks): things no official web source could confirm

Bring this on the first test day, or have a staff member walk it. Each line says what to check and what to do if it is wrong. Track numbers are V5.1 numbers (mapping from V5.0: `v5/RENUMBER_5OCT2026.md`).

## Palatine Gallery (first floor)

| ✓ | Check | Tracks | If it's wrong |
|---|---|---|---|
| ☐ | The ticket office is on the right-hand side of the façade; stairs and lifts on the right side of the courtyard | 001 | Fix the cue in 001 |
| ☐ | From the Castagnoli Room, with the Volterrano Wing closed, the signed route leads on to the Sala di Prometeo | 004 | Fix the cue in 004 |
| ☐ | Caravaggio's Sleeping Cupid hangs in the Sala dell'Educazione di Giove (ministry catalogue says so; no uffizi.it page) | 007–008 | Change the room in 008 and the cue in 007 |
| ☐ | Rubens's Consequences of War is in the Sala di Marte (only secondary sources give the room) | 024–025 | Move the cue; the track already says "usually hangs here" |
| ☐ | The Doni portraits are in Saturn. Are their painted backs visible? | 020 | If the backs aren't visible, rephrase "look at the back" |
| ☐ | Exit from Venus through the Sala delle Nicchie leads to the Palatine entrance atrium, with stairs/lift up to the second floor | 032–033 | Fix the cue in 032 |
| ☐ | After 25 Oct 2026: the Iliad Room has reopened | 009 | Remove the detour line from 009 and the Iliad box in `build/route_sheet.py`; rebuild |

## Second floor

| ✓ | Check | Tracks | If it's wrong |
|---|---|---|---|
| ☐ | Modern Art: from the landing, the corridor goes left | 032–033 | Fix the cue |
| ☐ | Bezzuoli's portrait of Elisa Baciocchi is in the first rooms | 034 | Change the line |
| ☐ | Fattori's Rotonda di Palmieri is on view, and in which room | 038–039 | Add the room to 039's card |
| ☐ | Fashion museum: corridor goes right, two short flights of stairs, stair-lift working | 040–041 | Fix the cue |
| ☐ | The Medici funeral garments are on display (official: permanently) | 042 | Hold the track if not |
| ☐ | Royal Apartments: from the Fashion museum, one floor down reaches the Palatine entrance atrium meeting point; the staff-led visit takes about 30 minutes; ticket arrangement as sold | 043–045 | Fix the cue in 043 / 045 |

## Ground floor

| ✓ | Check | Tracks | If it's wrong |
|---|---|---|---|
| ☐ | Russian Icons and Palatine Chapel open off the courtyard; which room holds the "All Creatures Rejoice" icon | 046–047 | Fix the card |

## Boboli

| ✓ | Check | Tracks | If it's wrong |
|---|---|---|---|
| ☐ | The Bacchino is reached by going LEFT (east) from the back of the courtyard | 049–050 | Fix the cue |
| ☐ | Grotta Grande comes before the Grotta di Madama, and the path between them works | 051–052 | Re-order |
| ☐ | Neptune: the pose (on a rock, trident swung down) matches the statue | 054 | Fix the description |
| ☐ | The Kaffeehaus is visible from the path up from Neptune, to the east | 054–055 | Fix the cue |
| ☐ | Abundance can be reached, or at least seen, while it is under restoration | 055–056 | Adjust the "fence" line |
| ☐ | The Limonaia lies north of the Isolotto, and the Annalena gate is close by | 058–059 | Fix the cue |
| ☐ | Restoration fences match the tracks: Amphitheatre tiers, Neptune basin, Abundance, inner Isolotto, Limonaia gates | 053, 054, 056, 058, 059 | Update the lines |

## Listening checks (on site, with earphones)

| ✓ | Check |
|---|---|
| ☐ | Pronunciation of Italian names in 5 random tracks. 69 respellings were added on 5 Oct without listening; note any that sound wrong (fix in pronunciation.py, or set APPLY_RESPELLING = False to compare). |
| ☐ | Loudness: no track noticeably louder or quieter than the others in a noisy room. |
| ☐ | Length: no single track feels too long to stand through (the longest run just under 3 minutes). |

# On-site checklist (7 Oct 2026 edition, 61 tracks): things to confirm on site

Bring this on the first test day, or have a staff member walk it. Each line says what to check and what to do if it is wrong. Track numbers are the 7 Oct 2026 numbers. Room locations were read on the museum's own artwork pages that day (research/OFFICIAL_LOCATIONS_7OCT2026.md); these lines cover what a page cannot prove.

## Palatine Gallery (first floor)

| ✓ | Check | Tracks | If it's wrong |
|---|---|---|---|
| ☐ | The ticket office is on the right-hand side of the façade; stairs and lifts on the right side of the courtyard | 001 | Fix the cue in 001 |
| ☐ | **Every Palatine door sign reads as the guide says** (Galleria delle Statue, Sala del Castagnoli, Sala di Prometeo, Sala di Ulisse, Sala dell'Educazione di Giove, Sala della Stufa, Sala dell'Iliade, Sala di Saturno, Sala di Giove, Sala di Marte, Sala di Apollo, Sala di Venere). Note the exact wording of each | 002–032 | Change the room name in the titles and cues |
| ☐ | Raphael's La Gravida is in the Sala di Prometeo (museum page, 7 Oct) or back in the Sala dell'Iliade (ministry record) | 005–006 | The track already covers both; drop the unused branch |
| ☐ | Raphael's Ezekiel's Vision is back in the Sala di Saturno (on loan to New York until 28 Jun 2026) | 016–017 | Hold 017 and point 016's cue to the Granduca |
| ☐ | The Iliad Room has reopened after 25 Oct 2026; route Stufa → Iliade → Saturno → Giove | 010–015 | Keep the closure line in 010 until it reopens, then shorten it |
| ☐ | From the Castagnoli Room, with the Volterrano Wing closed, the signed route leads on to the Sala di Prometeo | 004 | Fix the cue in 004 |
| ☐ | Caravaggio's Sleeping Cupid hangs in the Sala dell'Educazione di Giove (ministry catalogue says so; no uffizi.it page) | 008–009 | Change the room in 009 and the cue in 008 |
| ☐ | Rubens's Consequences of War is in the Sala di Marte (only secondary sources give the room) | 024–025 | Move the cue; the track already says "usually hangs here" |
| ☐ | The Doni portraits are in Saturn. Are their painted backs visible? | 020 | If the backs aren't visible, rephrase "look at the back" |
| ☐ | Exit from Venus through the Sala delle Nicchie leads to the Palatine entrance atrium, with stairs/lift up to the second floor | 032–033 | Fix the cue in 032 |
| ☐ | After 25 Oct 2026: the Iliad Room has reopened | 009 | Remove the detour line from 009 and the Iliad box in `build/route_sheet.py`; rebuild |

## Second floor

| ✓ | Check | Tracks | If it's wrong |
|---|---|---|---|
| ☐ | Modern Art: from the landing, the corridor goes left | 032–033 | Fix the cue |
| ☐ | Bezzuoli's portrait of Elisa Baciocchi is in the first rooms | 034 | Change the line |
| ☐ | Fattori's Rotonda di Palmieri is on view in Room 18 (ministry catalogue) | 039–040 | Fix the room in 039's cue and 040 |
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

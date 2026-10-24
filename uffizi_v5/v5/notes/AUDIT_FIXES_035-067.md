# Audit fixes: tracks 035–067 (24 Oct 2026)

Applied from `research/AUDIT_V5_035-067.md` (all 10 MUST-FIX, the SHOULD-FIX list as noted below), with the lead's decisions of 24 Oct 2026. Routes were re-read from the map myself: `research/map/p-2.png` plus a fresh 300 dpi render of PDF page 2 (first floor, B block, D block, D19–E4), `hi-3.png` / `p-3.png` (second-floor west end) and `p-1.png`. `pronunciation.py` was not edited. `v5/bridges/020-037.txt` was not edited. Tracks 001–034 were not touched. Lint: `python3 v5/lint.py 035 … 067`: all 33 OK.

## BRIDGES 035–037 (lead to merge)

Replacement lines for `v5/bridges/020-037.txt`. Each one is played **after** the track's normal cue.

```
035 H>037: On this shorter tour, skip the Niobe Room: walk on along the corridor, past Room A39 and the closed rooms A40 to A42, to the top of the Lanzi staircase, and stop before the stairs.
037 E>041: On this shorter tour, go down one floor only, then skip the other Contini rooms: walk the whole hall, Room B1, from the Info Point to its far end, Room B8: Bernini's marble saint lying on his grill.
037 H>046: On this shorter tour, skip the Contini rooms: go the other way, into the long room, Room C1, and follow the museum's route to Room D1, asking a warden if blocked, then Room D4: the Madonna with the Long Neck.
```

- **035 H>037: unchanged** (37 words). The audit found it OK, and it still follows 035's cue.
- **036: no bridge.** 036 is Essential only, and 037 comes straight after it in E.
- **037 E>041** (38 words). Before: "On this shorter tour, go down one floor only, then walk the whole hall of the Contini Bonacossi rooms, Room B1, from the Info Point to its far end, Room B8: …". The audit had no objection. I added "skip the other Contini rooms" because the new 037 cue now points at B2, and the bridge has to cancel that.
- **037 H>046** (40 words, MUST-FIX 2). Before: "…go down one floor only, walk from Room C1 through the self-portraits and the rooms being rehung to Room D1, asking a warden if blocked, then on to Room D4…". That line never said to skip the Contini rooms, and never said where C1 is, right after a cue that sends people into B1/B2.
  - Direction from the map (300 dpi). At the stair foot, the B1 hall runs off east, with the dotted out-and-back. C1 is the long green room on the opposite (west) side, and the orange line curls into it through a doorway near the Info Point level. So "the other way" means away from the hall the cue has just described.
  - C6–C12 stays conditional: "follow the museum's route … asking a warden if blocked" (NEVER list).
  - "Go down one floor only" is dropped from this bridge to stay within 40 words. 037's own body and cue say it twice in every version.

## Track changes (before → after, why)

**037 · A24 Lanzi** (MUST 3, MUST 4 with the lead's decision, SHOULD 18; 277 w)
- Terrace. Before: "the panoramic terrace is at this end of the floor, with the museum's café. The route doesn't come back up here, so if you'd like the view, go now." After: "Before you go down: the panoramic terrace, with the museum's café, is at this end of the floor. The route doesn't come back up here, so if you'd like the view, see it now, then come back to these stairs. If reaching it means going through an exit, skip it."
  - Why: lead decision to keep the plain café line, which the brief allows. hi-3 draws the terrace off the stair-head landing, right beside the exit icon (the end of the Fast itinerary), so the instruction is now conditional and does not assume a layout. ONSITE O17b.
- Before: "you can't come back in, and the cloakroom and audioguide desk are on the other side" → After: "you can't get back to the cloakroom or the audioguide desk, which are on the other side of the building". Why: the map's own wording, with no re-entry rule.
- Cue. Before: "Turn into the hall of the Contini Bonacossi collection, Room B1, beside the Info Point. The first room off it, Room B2, has…" After: "At the foot, the hall of the Contini Bonacossi collection, Room B1, leads away from the stairs. Room B2 is at its near end, on the side away from the Info Point: look for a big gold altarpiece…"
  - Why: the 300 dpi render draws no B1→B2 doorway. B2 is open to B4, with no partition, and faces the landing. I did not use the audit's "Ahead is the hall": the stair flight is drawn arriving facing the Info Point (south), with B1 off to the side, so "ahead" could be wrong.
- Trims to fit R ≤ 280 (no facts changed): "a new grand entrance was built, the one still in use"; "its ancient statues in facing pairs under painted ceilings"; "The stairs carry on down to a street exit. Don't follow them."; "Downstairs, a great deal more is waiting: … the sixteenth century, with Bronzino and Titian" (cut "and the painters who came after Raphael and Michelangelo").
- @sources: notes the lead decision and the map evidence.

**038 · B2** (MUST 3, MUST 10)
- Before: "Since 2018 they have filled eight rooms off this hall." → After: "Since 2018 they have filled eight rooms here, the long hall among them." Why: B1 is one of the eight. I did not say "this hall" because the listener is standing in B2.
- Cue. Before: "Back in the hall, the next room on the same side is Room B4…" → After: "Next is Room B4, Giovanni Bellini, right beside this room on the same side of the hall. Look for…" (the Cima warning is kept). Why: no partition is drawn between B2 and B4, so the line holds either way (O19b).
- @where: now "at the near end of the long hall … on the side away from the Info Point, beside Room B4", plus a note on the map.

**040 · B5 Bramantino** (MUST 9; page re-read)
- "the saint with the long sword is Martin of Tours" → "…is probably Martin of Tours". The page says "could be".
- "A poor man kneels with his back to us, adoring the Child." → "A poor man, with his back to us, is adoring the Madonna." The page says "adoring the Madonna, his back facing the onlooker", and does not say he kneels.
- "Under the surface, the experts have found many first ideas, painted over." → "Look closely and you can see many of those changes on the surface of the paint." The page says "from close up, it is possible to see many pentimenti".
- @sources updated with the quotations.

**041 · B8** (SHOULD 23): @where "Walk round it if you can, and look at the face from the head end." was replaced by a note that this is unconfirmed (O19b). Nothing spoken changed.

**043 · C2 Viola** (SHOULD 19): cut "and you hear the water the whole time". The page lists stereo sound, but whether it plays aloud in the room is unknown (O20b). @where was adjusted to match.

**046 · D4 Long Neck** (MUST 1, SHOULD 5; 358 w)
- Before: "D12 opens off that passage on the river side: … Don't take the staircase." → After: "D12 opens off that passage, on your left as you walk down from the corridor: … Don't take the staircase. If the passage is closed, ask a warden whether Room D12 can be reached. If not, walk on along the corridor to Room D14, Bronzino."
- Why the fallback: the notice lists D9 as work in progress, and Essential listeners skip 047 silently (046 E>048), so they never hear 047's fallback. The fallback uses what the map shows: D12's only drawn doorway is on D9 (its D10 side is shaded work in progress), and the corridor carries on to D14.
- Why "left": walking down D9 from the corridor you face map-south, and D12 is on the map-east side, so it is on your left. ONSITE O24b.
- No bridge needed the fallback. The only bridge that skips 047, 046 H>052, goes back through D1 along the corridor and never uses D9. The silent 046 E>048 skip is why the fallback sits in the cue itself.

**047 · D5–D8** (SHOULD 4): "the lobby at the top of the Buontalenti staircase" → "the landing of the Buontalenti staircase". On the first floor the stair continues down, and the Classic line arrives up it, so "top" was misleading.

**048 · D12** (SHOULD 11): "They are the founders of what we now call Mannerism" → "They are among the first painters of what we now call Mannerism". The superlative had no source.

**049 · D12 Moses** (SHOULD 12): "They echo the tangle of soldiers…" → "The bodies echo the tangle of soldiers…". When heard, "They" pointed back at "strips".

**050 · D12 Angel** (SHOULD 13): "That copy lets us guess…" → "That later altarpiece lets us guess…". The page says the composition "can be inferred" from Vanni's altarpiece. It does not call that altarpiece a copy.

**051 · D14** (SHOULD 20): "Down at his feet, a black puppy peers out at you, curious." → "Down at his feet sits a small black puppy." The French phrase is in the pronunciation list below.

**052 · D15 Eleonora** (SHOULD 1)
- Cue. Before: "Room D19, the narrow room through the second doorway in the back wall of D15, where the Vasari Corridor begins." After: "Room D19, where the Vasari Corridor begins: the narrow room through the second doorway in the back wall, the one farther from Room D14, where you came in."
- Why: the audit's "farther from the Bronzino room you came from" is ambiguous, because D15 itself hangs a Bronzino. Map, 300 dpi: in D15's back wall, the gap near the D14 end leads to D16 and the far gap leads to D19. O27b.

**053 · D15 Extra** (SHOULD 1; trimmed to 225 w)
- Cue. Before: "Room D16, through the first doorway in the back wall of D15, … Room D19, the narrow room through the second doorway." After: "Room D16, through the doorway in the back wall nearer Room D14, where you came in, has a short Extra… The next main stop is Room D19, the narrow room through the other doorway, farther along."
- Trims: "Here's the link to keep in mind" → "Here's the link"; cut ", the one you've just seen".

**054 · D16** (SHOULD 14): "A crown and a sceptre tumble from the sky." → "A crown, a sceptre and books tumble down." The page says "falling crown, sceptre, books". @where now counts the doorway from D14.

**055 · D19** (SHOULD 15): "over the roofs" → "above the streets". @where now counts the doorway from D14.

**056 · D20** (MUST 8, SHOULD 16; page re-read; 277 w)
- "Born on Crete, he trained in Venice and Rome, then settled in Toledo." → "Born on Crete, where he trained, he worked in Venice and Rome, then settled in Toledo." The page says "carried out his apprenticeship in his birth land", then Venice 1566, Rome four years later, Toledo 1577.
- "a son of Cosimo de' Medici" → "a son of Duke Cosimo the First".
- @where "about half a metre high" → "about two-thirds of a metre high" (66 × 50 cm).
- Trim: cut ", past El Greco's two saints," from the cue.

**057 · D23 Venus** (MUST 5; page re-read)
- Before: "She was soon too famous to stay in Urbino. She came to Florence in the dowry of Vittoria della Rovere." After: "Later she came to Florence, in the dowry of Vittoria della Rovere, the last of her family, who married a Medici grand duke."
- Why: the page gives no year and no cause. It says "the last member of the family and wife of Grand Duke … Ferdinando II". I chose the audit's no-time alternative over "almost a century", which is not on the official page.

**058 · D23 Flora** (MUST 6; page re-read; 226 w)
- Body. Before: "Her hair gave a colour its name." After: "Her hair is the colour of so many of Titian's women that it carries his name." The page says "the typical hair colour of women painted by Titian (hence the term 'Titian red')".
- @listen: "The painting that gave its name to 'Titian red', …" → "The hair colour named after Titian, …".
- Cut, to fit X ≤ 230: "You may remember her from Botticelli's Primavera upstairs." This also removes a dependence on O7.

**059 · D26 Veronese** (SHOULD 9; page re-read)
- "Adriano, the eldest of his seven children" → "Adriano, his first-born son, one of seven children" (page: "his first-born son, Adriano, one of the seven children…").
- "According to its museum page, Veronese's Holy Family … hangs in the Veronese Corridor, D27" → "Veronese's Holy Family … is listed in the Veronese Corridor, D27". This keeps the hedge until O34 and leaves only one "the museum" in the track. O34b says to change it to "hangs in" once confirmed.

**060 · D28 Verone** (SHOULD 21)
- "The Uffizi calls the Verone a covered loggia on the Arno. Its walls are a very pale, elegant green, and it gathers…" → "The Uffizi calls the Verone a covered loggia on the Arno, with walls of a very pale, elegant green, a place for ancient and Renaissance statues." The description is now attributed to the 2023 page, not stated as present fact (O35b).
- "The museum presents the statue under a single word, fatherhood." → "Its theme fits in a single word, fatherhood." This drops the second "the museum".
- @where was adjusted to match.

**061 · E4** (SHOULD 10): "Italian word for shadows" → "for darkness". "This room and the three after it follow them." → "…carry the story through the seventeenth century." (E7 is not Caravaggisti.) @what "(063, 064)" → "(062, 063)".

**062 · Medusa** (SHOULD 6): cut "and seems to push out toward you". The optical claim had no source.

**063 · Artemisia** (MUST 7, SHOULD 17): "the daughter of a Roman painter, Orazio" → "the daughter of the painter Orazio Gentileschi, who worked in Rome" (he was born in Pisa). The quotation is now introduced with "As the Book of Judith puts it, …". @sources updated.

**064 · Bacchus** (SHOULD 7): "a young man from Caravaggio's studio" → "a real young man posing". Cut "The face does not." "And many notice that fruit on the turn is…" → "And the fruit on the turn may be…".

**066 · E7** (SHOULD 8; page re-read): "It came back to Florence after his fall." → "It stayed there until his fall, and only years later came back to Florence." The page has Paris 1799–1815 and the return to Florence in 1834. I left the year 1815 out of speech to keep within about 3 dates per track (the brief).

**067 · Close** (SHOULD 22): "That is why you could stand in front of the Primavera today, in the city that made it." → "…in front of the Venus of Urbino today, in the city that kept her." I applied the audit's alternative now rather than holding it, so the track no longer depends on O7. The Venus is in D23 on every version's route. O7b keeps the restore option.

Unchanged (audit OK, or listen-QA only): 035, 036, 039, 042, 044, 045, 065.

## Bridges edited in my files

- `v5/bridges/038-055.txt`, **052 H>057** (SHOULD 2; 39 w). Before: "…go through the second doorway in D15's back wall into the narrow Room D19, on into the strip of Room D21, …". After: "On this shorter tour, walk through Room D19, past the Vasari Corridor door without going through it, into the strip of Room D21 at its far end, then through the antechamber, D22, into Room D23: Titian's Venus of Urbino."
  - Why: Highlights skips 055's warning. The 052 normal cue already says which doorway leads to D19, so the bridge starts inside D19. The map draws the Corridor entrance arrow at D19's far end, next to the D21 opening.
- `v5/bridges/056-068.txt`, **057 H>062** (SHOULD 3; 39 w): "…then turn left into Room E4" → "…then turn left along the corridor to Room E4". On the map the line turns left at the top of the Verone along a short grey corridor before it enters E4.
- Unchanged: 046 H>052, 049 E>052, 055 E>057, 064 H>067 (all OK by the audit and still consistent with the edited cues).

## PLAN housekeeping (SHOULD 25)

Edits in `v5/PLAN.md`:
- §3 "A bridge replaces the track's last cue paragraph…" now says that bridges are **appended after** the normal cue (make_lengths.py), with a renumbering note: Tintoretto held; rows 060–068 are now 059–067; the 037/038/046/052/053/057 cues were revised by this audit and the track files are authoritative.
- Bridge rows: "057 E>060" is marked removed; "057 H>063" → "057 H>062" ("left along the corridor"); "065 H>068" → "064 H>067".
- Row 057 cue → "next main stop is Room D26, Veronese… (Tintoretto held)". Row 058 cue → "Through Room D24 and Room D25 into Room D26".
- Row 037: records the lead's café decision and the conditional terrace line.

## Declined or adapted (and why)

- **MUST 4, PLAN-compliant terrace line without the café**: declined, per the lead's decision to keep the café line (the brief allows it). The "go now" part was made conditional instead, and O17b was added.
- **037 cue, the audit's "Ahead is the hall"**: adapted to "leads away from the stairs" (map orientation, see 037 above).
- **052/053, the audit's "farther from the Bronzino room"**: adapted to "farther from Room D14", because D15 holds a Bronzino too.
- **057 "almost a century"**: not used. It is not on the official page, so I used the audit's no-time alternative.
- **059 "drop 'According to its museum page'"**: the audit tied this to O34, which has not been done. I made it "is listed in" for now, which removes the repeated "museum" but keeps the hedge.
- **066 "until 1815, the year of his fall"**: the year was left out to respect the brief's ~3 dates per track. The meaning is unchanged.
- **041 "smouldering embers"**: optional in the audit. Not applied, because "coals" is OK by the audit.
- **036 "second century AD"** and **051 French phrase**: these are listen-QA items. There is no text change, because the respellings belong in pronunciation.py, which I may not edit (see the list below and the ONSITE listening line).
- **SHOULD 25, full renumbering of PLAN's track table**: not done row by row. I added the renumbering note and fixed the cue and bridge rows that could reintroduce errors. Rewriting a 68-row shared table while another fixer edits PLAN risks conflicts, and lengths.json is authoritative.

## ONSITE items appended to v5/ONSITE_CHECKLIST.txt

I re-read the file right before appending, and only appended. Items added: O17b (terrace door and the one-way exit), O19b (B1→B2 doorway, B4 beside B2, "the other way" to C1, Bernini walk-round), O20b (Viola sound), O24b (D12 on the left in D9; another way in if D9 is closed; "landing" in 047), O27b (D15 doorways counted from D14; passing the Corridor door in D19), O34b ("is listed" → "hangs" in 059), O35b (Verone walls), O36b (E4 first to the left at the top of the Verone), O7b (067 now names the Venus; option to restore the Primavera), and one listening line.

## Names an English voice may mispronounce (035–067): suggested respellings for pronunciation.py

Already in pronunciation.py: Lanzi (Loggia dei Lanzi), Castagno, Leopoldo/Pietro Leopoldo, Pontormo, Bronzino, Garzia, Allori, Buontalenti, Caravaggio, Gentileschi, Giorgione, Ghirlandaio, Vasari, Cosimo, Medici, Boboli, Lucrezia, Rovere / Vittoria della Rovere, Accademia, Agnolo, Doni, Andrea del Sarto, Aretino.

Not yet in it:
- 035: Nasi → NAH-zee · Michele di Ridolfo → mee-KEH-leh dee ree-DOHL-foh · sfumato → sfoo-MAH-toh
- 036: Niobe → NYE-oh-bee · Latona → lah-TOH-nah · Georgofili → jor-GOH-fee-lee · Nencioni → nen-CHOH-nee · Capolicchio → kah-poh-LEEK-kyoh · "AD" → "A.D." (letters)
- 038: Contini Bonacossi → kon-TEE-nee boh-nah-KOHS-see · Sassetta → sahs-SET-tah · Santa Maria Maggiore → mahd-JOH-reh · Trebbio → TREB-byoh · Pazzi → PAHT-tsee
- 039: Bellini → bel-LEE-nee · Ravenna → rah-VEN-nah · Rimini → REE-mee-nee · Cima da Conegliano → CHEE-mah dah koh-nel-YAH-noh
- 040: Bramantino → brah-mahn-TEE-noh · Bramante → brah-MAHN-teh
- 041: Gian Lorenzo Bernini → jahn loh-REN-tsoh ber-NEE-nee · Domenico → doh-MEH-nee-koh
- 043: Bill Viola → vee-OH-lah
- 044: Cerquozzi → cher-KWOHT-tsee · Bambocciate → bahm-boht-CHAH-teh · Il Bamboccio → eel bahm-BOHT-choh
- 045/046: Parmigianino → par-mee-jah-NEE-noh · Correggio → kor-RED-joh · Antonio Allegri → ahl-LEH-gree · Francesco Mazzola → frahn-CHES-koh maht-TSOH-lah · Dosso Dossi → DOHS-soh DOHS-see · Ferdinando → fer-dee-NAHN-doh · Elena Baiardi Tagliaferri → EH-leh-nah bah-YAR-dee tahl-yah-FER-ree
- 047: Garofalo → gah-ROH-fah-loh · Giulio Romano → JOO-lyoh roh-MAH-noh · Perin del Vaga → peh-REEN del VAH-gah · Salviati → sahl-VYAH-tee
- 048–050: Jacopo Carucci → YAH-koh-poh kah-ROOT-chee · Pontorme → pon-TOR-meh · Empoli → EM-poh-lee · Rosso Fiorentino → ROHS-soh fyoh-ren-TEE-noh · Santa Maria Nuova → NWOH-vah · Ognissanti → oh-nyee-SAHN-tee · Zipporah → zih-POR-ah · Bandini → bahn-DEE-nee · Fontainebleau → fon-ten-BLOH · Francesco Vanni → VAHN-nee
- 051: Panciatichi → pahn-CHAH-tee-kee · "sans fin amour dure" → sahn fan ah-MOOR DÜR (French; or keep French phonemes if the engine allows) · Lyon → lee-OHN
- 052–054: Eleonora di Toledo → eh-leh-oh-NOH-rah dee toh-LEH-doh · lapis lazuli → LAP-iss LAZ-yoo-lee · Eleonora Gonzaga → gon-DZAH-gah · Guidobaldo → gwee-doh-BAHL-doh · Federico Barocci → feh-deh-REE-koh bah-ROHT-chee · Jacopo Ligozzi → lee-GOHT-tsee
- 055: Joanna of Austria (OK) · Santa Felicita → feh-LEE-chee-tah · Palazzo Vecchio → pah-LAHT-tsoh VEK-kyoh · Ponte Vecchio → PON-teh VEK-kyoh
- 056: Lorenzo Lotto → LOHT-toh · Ludovico Beccadelli → loo-doh-VEE-koh bek-kah-DEL-lee · disegno → dee-ZEN-yoh · colore → koh-LOH-reh
- 057/058: toccamano → tohk-kah-MAH-noh · Manet → mah-NAY · Zephyr → ZEF-er
- 059: Paolo Veronese → PAH-oh-loh veh-roh-NEH-zeh · Giuseppe da Porto → joo-ZEP-peh dah POR-toh · Adriano → ah-dree-AH-noh · Levi → LEE-vye · Gallerie dell'Accademia → gahl-leh-REE-eh del-lahk-kah-DEH-myah · scudi → SKOO-dee
- 060: Verone → veh-ROH-neh · Silenus → sye-LEE-nus · Jacopo del Duca → del DOO-kah
- 061: Ranuccio Tomassoni → rah-NOOT-choh toh-mahs-SOH-nee · tenebrism → TEN-eh-briz-um · Caravaggisti → kah-rah-vahd-JEE-stee · Maffeo Barberini → mahf-FEH-oh bar-beh-REE-nee · Gherardo delle Notti → geh-RAR-doh DEL-leh NOHT-tee · Guido Reni → GWEE-doh REH-nee
- 062: Francesco Maria del Monte → del MON-teh · Medusa / Perseus / Athena (OK)
- 063: Artemisia → ar-teh-MEE-zyah · Holofernes → hol-oh-FUR-neez · Orazio → oh-RAHT-tsyoh · Agostino Tassi → ah-goh-STEE-noh TAHS-see · Galileo Galilei → gah-lee-LEH-oh gah-lee-LAY-ee
- 064: Roberto Longhi → LON-ghee (hard g) · Antinous → an-TIN-oh-us
- 065: Gerrit van Honthorst → GHER-rit vahn HONT-horst · Utrecht → YOO-trekt
- 066: Saskia → SAHS-kee-ah · Anthony van Dyck → van DIKE
- 067: Magliabechi → mahl-yah-BEH-kee · Uffizi → oof-FEET-see · Anna Maria Luisa → loo-EE-zah

## Verification (WebFetch, one page at a time, 24 Oct 2026)

uffizi.it pages: Bramantino *Madonna and Child with eight saints* ("could be St Martin"; "adoring the Madonna, his back facing the onlooker"; "from close up … many pentimenti") · El Greco *Saints John and Francis* (apprenticeship in Crete; Venice 1566; Rome four years later; Toledo 1577) · Titian *Venus of Urbino* (dowry of Vittoria, "the last member of the family"; no year) · Titian *Flora* ("hence the term 'Titian red'") · Rembrandt *Old Rabbi* (Paris 1799–1815; back in Florence 1834) · Veronese *Count Giuseppe da Porto* ("his first-born son, Adriano, one of the seven children").

The other changes are hedges, cuts or navigation wording, and need no new fact. Orazio Gentileschi's birth in Pisa is general reference, the audit's FIX.

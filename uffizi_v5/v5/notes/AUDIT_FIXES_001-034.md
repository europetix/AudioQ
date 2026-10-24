# Audit fixes, tracks 001–034 (24 Oct 2026)

Source: `research/AUDIT_V5_001-034.md` (independent audit, 24 Oct 2026). Every MUST-FIX and SHOULD-FIX was considered. Items were applied, applied in a modified form, or declined, with the reason given below. Tracks 035–067 were not touched. `pronunciation.py` was not touched; the respelling list is in §5.

**Lint:** `python3 v5/lint.py 001 … 034` gives all OK.

**Length:** the tracks went from 9,041 to 9,038 spoken words (−3). The bridges for 001–034 went from 467 to 503 words (+36), almost all of it the M1 fallback in 007 H>017. By version:

| Version | Track words | Bridge words | Net |
|---|---|---|---|
| Full | −3 | – | −3 |
| Essential | −22 | +1 | −21 |
| Highlights | −36 | +36 | 0 |

Small trims (§3) pay for the additions, so no version grows.

**Map check:** I read `research/map/p-3.png` and crops of `hi-3.png` myself. The doorway gaps I found agree with the audit's §0:

- **Vestibule end:** A3 sits on the far side of the vestibule (A1) and the lift block, at the short Palazzo Vecchio end of A2, and has its own corridor door. A5 has no corridor door, so A4 is the first doorway down the long corridor.
- **A4 to A8:** A4↔A5 is near the corridor. A4's far side has two doorways side by side: A7's on the A5 side, then A8's. There is no A7↔A8 doorway. A6↔A7 is a gap at the back of their shared wall, and A6 also has a gap on the vestibule side.
- **A8 and the Botticelli rooms:** A8 has **no corridor door**. Its only drawn way on is the gap into A9, which is shaded not open. A9 opens to A10, A10 to A11–12 at the back, and A11–12 to A13 near the corridor. A10 and A11–12 have no corridor door.
- **A13 to A16:** A14 opens only into A13. A15 links A13 to the Tribune.

Every cue changed here goes through a doorway that is drawn on the map.

## 1. MUST-FIX

| # | Track | Before → after | Why / source |
|---|---|---|---|
| M1 | bridge 007 H>017 | "Take the far-side doorway of Room A4 into Room A8, Masaccio's room, then follow the museum's Botticelli signs through to the Primavera…" → "On this shorter tour, skip Room A5. Take the far-side doorway of Room A4 into Room A8, not the one beside it into Room A7, and follow the museum's Botticelli signs to the Primavera, the wide, dark grove of nine figures. If the way through is closed, go back through Room A4 to the corridor, on to Room A13, with its big Flemish altarpiece, and enter the Botticelli rooms from the far end." | The bridge now names which of the two side-by-side doorways to take and adds the A13 fallback (Highlights listeners never hear 014). It follows the lead's wording for the Botticelli entry. It makes no corridor-door claim for A8, and it never says A9–A12. **At 73 words it is above the brief's 15–40 range.** The fallback cannot be fitted in 40 words, and the audit allowed about 70. The lead can render it as two sentences or as a short clip. |
| M2 | 014 cue | "The Botticelli rooms come straight after this room. Follow the museum's Botticelli signs from Room A8 and start in the first one… If that way is closed, go back to the corridor and on to Room A13… then through into the Botticelli rooms to the room of Virtues." → "The Botticelli rooms come next. Follow the museum's Botticelli signs from Room A8. If the way through is closed, go back through Room A4 to the corridor, walk on to Room A13, with its big Flemish altarpiece, and enter the Botticelli rooms from the far end. Either way, begin in the room lined with painted Virtues in gilded frames." | This is the lead's decision: the cue holds either way. "Straight after this room" was dropped, because it is only true through A9. The fallback now goes back through A4, since A8 has no corridor door. With the A13 entry, the Virtues room really is at the far end (A10, behind A11–12). The audit's "record ALT-014b if O7 is unsettled" is superseded by the lead's decision. O7 stays critical (checklist updated). |
| M3 | 021 cue | "Through Room A15 to the Tribune, Room A16, next door: …" → "Go back into Room A13 and through Room A15, the small Room of Mathematics, to the Tribune, Room A16: red velvet walls and a dome of mother-of-pearl." | On the map, A14 opens only into A13. |
| M4 | 027 | "In 1496 the Augustinian friars of San Donato a Scopeto asked him for this Adoration of the Magi. They had a reason." → "In 1496 Filippino finished this Adoration of the Magi for the Augustinians of San Donato a Scopeto. They had a reason for asking him." | OFF page re-read: the panel is signed "…ADDI 29 DI MARZO 1496" and the page gives no commission year. The sentence also applies S18. |
| M5 | 027 cue (+ PLAN, FLOOR2) | "a short Extra on Signorelli's round paintings" → "a short Extra on Signorelli" | The A32 *Madonna with Child* is 170 × 115 cm, not a tondo (028 @what, OFF). Errata were made in PLAN row 027 (cue), PLAN row 028 ("A second tondo" → "A second Signorelli … **not** a tondo") and FLOOR2 (§3 row and §4 A32 row). |
| M6 | 031 | "In July 1481, Leonardo signed a contract to paint this altarpiece within thirty months." → "A document of July 1481 records that Leonardo had taken on this altarpiece, and promised to finish it within thirty months." | OFF artwork page re-read: "A document from July 1481 states that Leonardo da Vinci had received a commission…", "undertook to finish within 30 months". |
| M7 | 031 | "Unusually for his time, he worked the composition out directly on the panel, not on paper first." → "The restoration showed that, unusually for his day, he worked the composition out directly on the panel." | **Applied in a modified form.** The audit called "unusually for his time" unsourced, but the OFF event page (re-read) says the restoration showed that, "unusually for his day", Leonardo "developed the composition directly on the panel rather than on paper". The claim is therefore official. It is now attributed to the restoration, and the absolute "not on paper first" was dropped so it doesn't clash with the known drawings. I did **not** add the audit's "a separate perspective study for it survives too": no uffizi.it page confirms it (WebSearch found only Wikipedia and secondary pages), and the brief forbids an unverified load-bearing fact. **Lead's call:** add it only with a confirmed source, e.g. the Uffizi Prints and Drawings record. |
| M8 | 006 | "In 1854 a Florentine scholar realised…" → "In 1854 the scholar Gaetano Milanesi realised…" | SEC finestresullarte re-read: "Gaetano Milanesi, who in 1854, scanning a 1790 work by a Florentine friar, Vincenzio Fineschi…". No origin is given (Milanesi was Sienese). |
| M9 | 023 | "The rooms you walked past, A17 to A21, hold northern Renaissance painting, and they are closed while they are rearranged." → "The rooms you walked past, A17 to A21, normally show painting from beyond the Alps and from fifteenth-century Siena. They are closed while they are rearranged." | Map legend: A17–A20 "Renaissance beyond the Alps", A21 "15th Century in Siena". The 15 Sep notice lists A17/A21 as work in progress. |
| M10 | 009 | `"AVE GRATIA PLENA DOMINUS TECUM." Hail, full of grace, the Lord is with you.` → `The greeting begins "Ave gratia plena": hail, full of grace, the Lord is with you.` | This is the lead's decision: normal case, kept short for an English voice. Only the first three Latin words are spoken, and "begins" keeps it accurate. The full inscription stays in @sources/@what. |
| M11 | – | Pronunciation | `pronunciation.py` was not edited (the lead does it). The full list with suggested respellings is in §5. Possessives (Duccio's, Gentile's, Uccello's) need no special handling, because `apply_respelling` uses `\b` and the apostrophe is a word boundary. |

## 2. SHOULD-FIX

| # | Track | Before → after | Status / why |
|---|---|---|---|
| S1 | 002 cue | "Room A3 is the very first doorway, at the start of the corridor, right beside the vestibule you came through, on the side away from the windows." → "Room A3 is close by, but not down the long corridor. As you leave the vestibule, turn the other way, to the short end of the corridor nearest Palazzo Vecchio. A3 is the doorway there, away from the windows." (look-for kept) | Applied. The map shows A3 beyond the lift block, at the Palazzo Vecchio end ("← Palazzo Vecchio" label). **Knock-on:** bridges 002 E>004 and H>006 said "Go the other way along the corridor", which would now be ambiguous after the new cue. Both now say "Walk down the long corridor instead, to its first doorway on the side away from the windows: Room A4…". Map: A5 has no corridor door. The 003 @where and the 002 @sources map note were also corrected. |
| S2 | 009 cue, 010 cue, bridge 009 E>012 | 009: "…go back into the Maestà room, A4, and through the doorway on its far side, away from the corridor." → "…go back into the Maestà room, A4. On its far side, away from the corridor, are two doorways side by side. Take the one on the Room A5 side, into Room A7, with a huge gold procession of kings." · 010 fallback: "A7 is through the doorway on A4's far side" → "take the one of the two far-side doorways that leads into A7" · bridge 009 E>012: "…through the doorway on its far side into Room A7, to Gentile's huge golden procession of kings" → "…take the far-side doorway into Room A7, not the one beside it into Room A8, to the huge golden procession of kings." | Applied. "On the Room A5 side" comes from the map: A7's gap is west of A8's, toward A5. It is not a left/right instruction, so it respects O3/O4. The bridge also avoids "Gentile's" (M11 note). |
| S3 | 007 | "two centuries later" → "two and a half centuries later" | Applied (Vasari's *Lives*, 1550). |
| S4 | 007 | "[wry] Remember Dante's line, that Giotto now "has the cry"." → "[wry] Dante wrote that Giotto now "has the cry", the fame that had been Cimabue's." | Applied. Highlights skip 004. |
| S5 | 007 | "served by the monks of the Humiliati order" → "run by the religious order of the Humiliati" | Applied. Note: the OFF page (re-read) itself says "the Humiliati monks who officiated in the church", so the old wording was not wrong on the museum's terms. The new wording is neutral and compatible with it. |
| S6 | 009 | "[curious] Most painters show a voice by painting an open mouth. Simone Martini wrote the words themselves…" → "[curious] Simone Martini didn't leave the angel's greeting to your imagination. He wrote the words themselves…" | Applied. |
| S7 | 009 | "Simone was a star, a friend of the poet Petrarch, who worked for kings…" → "Simone was a star. He was a friend of the poet Petrarch, and he worked for kings…" | Applied. |
| S8 | 009 | "The name written at her feet says Judith, and that is wrong." | **Declined.** The audit says the page gives no position. The OFF page (re-read) says "the inscription at her feet, which identifies her as Judith, is incorrect", so the current sentence is exactly what the page says. |
| S9 | 004 | "Every painter on this floor learned something from what happened in this room." → "Much of what you'll see on this floor grows out of what happened in this room." | Applied. |
| S10 | 003 | "…to the entombment." → "…to Christ's descent into limbo." | Applied. OFF cross_432 re-read: "the descent into limbo of Christ resurrected". |
| S11 | 012 | "He knew it was something special." → "Perhaps he knew it was something special." | Applied. |
| S12 | 013 | "…for the church of Sant'Ambrogio." → "…, according to Vasari." · "four centuries ago" → "more than four centuries ago" | Applied. OFF re-read: "as specified in the Lives by Giorgio Vasari". The Glorification predella was separated "in the second half of the 16th century". |
| S13 | 015 | "From here the Botticellis follow his life in order. The sequence opens with his Adoration of the Magi." → "After this room, the Botticellis follow his life in order, opening with his Adoration of the Magi." | Applied. **Also (O7):** the cue's "…nine figures, a little further on." became "…nine figures." With the A13 entry the Primavera is back the way you came, so the cue now holds either way, as the lead asked for 014. |
| S14 | 018 | "Look from the goddess to the Virgin of the Magnificat…" → "Look from the goddess to the Madonna of the Magnificat, the round painting beside her where Mary is writing in a book…" | Applied; it does not say "larger". OFF Magnificat page re-read: round, 118 cm, Mary "writing the canticle". To pay for the words, "Now the two are together again, facing each other across the passage, in new airtight cases instead of the old glass screens. Either side of Venus hangs a round Madonna." became "Now the two are together again, facing each other, in new airtight cases instead of the old glass." The flanking Madonnas are still named in 017 and in this sentence. |
| S15 | 020 | "In 1483, a ship from Flanders unloaded a painting at Pisa that would make every painter in Florence stop and stare." → "In 1483 a painting arrived in Florence from Flanders, shipped by sea to Pisa, and it made every painter in the city stop and stare." · "around 1477 he ordered this huge altarpiece from Hugo van der Goes." → "there he ordered this huge altarpiece from Hugo van der Goes, who painted it around 1477 or 1478." · optional: "It came by sea, and the museum says Florentine painters found it extraordinarily new. They had never seen oil paint handled like this, on this scale." → "Florentine painters found it extraordinarily new, and the museum says they especially praised its realism." | Applied, including the optional line. OFF re-read: "arrival in Florence in 1483, having first reached Pisa by sea"; date "1477-1478 c."; no commission year; "extraordinarily innovative"; painters "particularly praised the realistic likeness…". |
| S16 | 022 | "Ferdinando de' Medici, the cardinal from the Room of the Maps, bought her in Rome." → "Ferdinando de' Medici, then a cardinal in Rome, bought her there." · optional: "the peace treaty of Vienna" → "the Treaty of Vienna" | Applied. OFF medici-venus re-read: purchased by Ferdinando and kept at Villa Medici in Rome (bibliography "Le collezioni del Cardinal Ferdinando"); "to comply with the Treaty of Vienna". |
| S17 | 023 | "…together with Ponte Vecchio". It held." → "…together with Ponte Vecchio"." | Applied (unsourced). |
| S18 | 027, 031 | 027: "Augustinian friars" → "the Augustinians" · 031: "a monastery of Augustinian canons" → "a monastery of the Augustinians"; "The canons waited in vain, and finally hired…" → "The Augustinians finally hired…" | Applied. OFF pages say "friars" / "monks". PLAN row 031 still says "Augustinian canons" (core content, not speech). Left for the lead. |
| S19 | 028 | "Around 1487 he made this round Holy Family for the audience hall of the Guelph Party." → "Around 1487 he painted this round Holy Family, which Vasari says was made for the audience hall of the Guelph Party." · "the Medici from Filippino's Adoration" → "the Medici who may appear in Filippino's Adoration" | Applied. OFF re-read: "Vasari testifies that the painting … was made for the Sala delle Udienze of the Capitani di Parte Guelfa". The words "made for", not "hung in", follow the page. |
| S20 | 030 | "Nobody knows who ordered this painting, or where it first hung." → "Nobody knows who ordered this painting." · "The museum suggests a viewpoint from the right, because the panel once hung over a side altar." → "The museum suggests it was planned to be seen from the right and from lower down, over a side altar." · "He was already testing how our eyes really see. In his early twenties, he was asking questions no one around him thought to ask." → "Barely twenty, he was already asking his own questions about how our eyes really see." | Applied. I merged the two sentences so "how we see" is not said twice. OFF re-read: "a lateral viewpoint (from the right) and lowered, due to the original location of the painting, over a side altar". "Take a few steps to your right" is kept, with an on-site item added (O14b). |
| S21 | 031 | "You saw his Adoration in Room A28." → "His Adoration hangs in Room A28, back along this floor." | Applied (Essential skips A28). |
| S22 | 032 | "twelve Roman reliefs" → "twelve ancient reliefs, almost all Roman," | Applied. OFF news re-read: "twelve reliefs, almost all of Roman era". |
| S23 | 033 | "It's in London now." → "It is now identified with a relief in London's Victoria and Albert Museum." | Applied. The OFF page re-read says "now identified as the so-called Dudley Madonna, preserved in the Victoria and Albert Museum", so I used "identified" (the page's word) instead of "thought to be". |
| S24 | 034 | "Remember Signorelli's Madonna, with its nudes in the background?" → "Signorelli's Madonna in Room A32 also has nudes in its background." · "the Doni's daughter" → "the couple's daughter" | Applied. |
| S25 | 015–019 @room | – | **@room not changed.** The brief says "@room exactly as PLAN", and PLAN's conventions keep A10/A11/A12 there until O7. The audit's goal (never print the codes in the written script) was met in the build instead: `build/scripts_md.py` now prints "Botticelli rooms" (and the ES/FR/DE/IT equivalents) for any @room of A9–A12. I tested it: 015–019 print "Botticelli rooms". @title stays "Botticelli rooms · …", as the lead asked. `route_map.py`, `make_bundle.py` and `levels.txt` already hide these codes. |
| S26 | 010 cue | "Room A7, Gentile da Fabriano: if a doorway leads straight on from this room into A7, take it. Otherwise…" → "Room A7, Gentile da Fabriano, is next door. If the doorway at the back of this room, away from Room A5, leads into A7, take it. Otherwise go back through A5 into A4, and take the one of the two far-side doorways that leads into A7." | **Applied in part.** The cue now describes the doorway the map draws (at the back, away from A5, which also tells it apart from the vestibule-side gap). It stays conditional, because the audit itself makes the direct cue primary only "if O4 confirms". The O4 item is updated. |
| S27 | PLAN, FLOOR2 | PLAN §1 step 3: "No A6–A7 doorway is drawn" → "The high-resolution map draws an A6–A7 gap at the back of their shared wall (erratum…)". PLAN §5 O4: "A6↔A7 (none drawn)" → "(a gap is drawn at the back of their shared wall)". PLAN row 028 and FLOOR2: tondo errata (see M5). | Applied. Originals were backed up in the scratchpad. |

**Not synced (lead's call):** PLAN's own cue texts for rows 014 and 021, and its bridge-table row 007 H, still carry the older wording. The tracks are now the reference. I didn't rewrite the lead's binding table beyond the errata the audit asked for.

## 3. Length trims (to keep the guide from growing)

None of these trims removes a fact from the route, a cue or a load-bearing claim.

- **002** "The museum says the word gallery is widely believed to come from this very setting." was cut. The opening line already says it. "began to fill it" became "began to fill the loggia". "…to walk where you are walking now." became "…to walk here."
- **005** "Santa Trinita, a church a few streets from here." became "Santa Trinita."
- **007** "The Child raises his hand in blessing and holds a rolled scroll." was cut.
- **009** "She had been reading, and her book is still in her hand." became "Her book is still in her hand."
- **018** See S14.
- **025** The closing "A duke and duchess of the Marche, at home in Florence." was cut.
- **028** "They are so big and solid that they seem to press out of the frame toward you." became "They are so solid they seem to press out of the frame." "Keep them in mind too." was cut. This keeps the X track under the 230-word cap after S19.
- **031** "Look into the background now, and you see what visitors before then could hardly make out." became "Look into the background now: visitors before then could hardly make it out."
- **032** "The room was once open to the sky. It began as a terrace, built in 1658," became "The room began as an open terrace, built in 1658,". This makes room for S22 under the 230-word cap.
- **033** "Raphael himself is waiting downstairs. His self-portrait is in the first self-portrait room, on the first floor." became "Raphael's own self-portrait waits downstairs, in the first self-portrait room."

**Word counts (before → after):**

| Track | Words | Track | Words |
|---|---|---|---|
| 002 | 290→284 | 015 | 255→250 |
| 003 | 247→249 | 018 | 308→308 |
| 004 | 259→262 | 020 | 309→308 |
| 005 | 291→284 | 021 | 198→207 |
| 006 | 289→290 | 022 | 331→326 |
| 007 | 286→282 | 023 | 251→255 |
| 009 | 312→322 | 025 | 297→286 |
| 010 | 203→214 | 028 | 227→225 |
| 012 | 308→309 | 030 | 289→278 |
| 013 | 229→234 | 031 | 320→323 |
| 014 | 309→308 | 032 | 229→226 |
| | | 033 | 234→236 |
| | | 034 | 313→315 |

027: 267→267 (reworded, net 0). Unchanged: 001, 008, 011, 016, 017, 019, 024, 026, 029.

## 4. On-site items added to `v5/ONSITE_CHECKLIST.txt`

Each one is marked "[audit 24 Oct]".

- **O2** A3 is at the short Palazzo Vecchio end, beyond the vestibule and lift. Confirm the new 002 cue and the 002 E/H bridges ("first doorway down the long corridor: A4").
- **O4** The map *does* draw an A6–A7 gap. If it is open, make 010's direct cue the only cue. Confirm that A4's far side has two doorways side by side, with A7's on the A5 side (009, 010, bridges 009 E and 007 H).
- **O7** The new wording of the 014 cue and the 007 H bridge is noted on the checklist. If only the A13 entry works, record it as the primary. Then re-check 015 (the Virtues room is at the far end), 016, 017 ("Room A13 comes after it") and 018/019.
- **O8** Is A14 entered, or only seen from its door (021 says "ceiling above you")? 021's cue now goes back into A13.
- **O9** Are the Wrestlers and the Knife Grinder visible from where visitors stand (022)?
- **O14b (new)** In front of the Annunciation (030), can visitors step to the right?
- **Listening checks:** a line was added with the 001–034 names (§5).

## 5. Names an English voice may mispronounce (001–034). Suggested respellings for `pronunciation.py`

None of these is in the current dictionary, which was carried over from Pitti. Tracks are in brackets; "b" = also in a bridge.

**Critical** (they would be read as English words or badly misplaced):

| Name | Respelling | Tracks |
|---|---|---|
| Gentile / Gentile da Fabriano | Jen-tee-leh / Jen-tee-leh da Fah-bree-ah-no | 010, 011, 012, 031 |
| Marche | Mar-keh | 025 |
| Maestà | My-es-tah | 004, 006, 009 |
| Uffizi / Piazzale degli Uffizi | Oof-fee-tsee / Pyat-tsah-leh del-yee Oof-fee-tsee | 001, 005, 006, 030, 031 |

Notes:
- **Gentile** would be read as the English word "gentile". The entry must stay case-sensitive. `\bGentile\b` does not touch "Gentileschi".
- **Marche** would be read as "march".
- **Uffizi** is optional. Check it in the listening pass.

**Painters and people:**

| Name | Respelling | Tracks |
|---|---|---|
| Cimabue | Chee-ma-boo-eh | 004–007 |
| Duccio di Buoninsegna | Doot-cho dee Bwon-een-sen-ya | 004–006; b 002 H, 004 E |
| Ognissanti | On-yee-sahn-tee | 007, 010 |
| Rucellai | Roo-chel-lye | 005, 006; b 004 E |
| Laudesi | Low-day-zee | 006 |
| Milanesi | Mee-la-nay-zee | 006 |
| Humiliati | Oo-mee-lyah-tee | 007 |
| Oderisi | Oh-deh-ree-zee | 004 |
| Lorenzetti | Lo-ren-tset-tee | 008, 010 |
| Ambrogio | Am-broh-jo | 008 |
| Simone Martini | See-moh-neh Mar-tee-nee | 008, 009; b 007 E |
| Lippo Memmi / Lippo | Leep-po Mem-mee / Leep-po | 009 |
| Giottino | Jot-tee-no | 010 |
| Giovanni da Milano | Jo-vahn-nee da Mee-lah-no | 010 |
| San Remigio | San Reh-mee-jo | 010 |
| Faenza | Fah-en-tsa | 010 |
| Lorenzo Monaco | Lo-ren-tso Moh-na-ko | 011 |
| Camaldolese | Ka-mal-doh-lay-zeh | 011 |
| Santa Maria degli Angeli | San-ta Ma-ree-a del-yee Ahn-jeh-lee | 011 |
| Palla | Pahl-la | 012 |
| Masolino | Mah-zo-lee-no | 012, 013 |
| Sant'Anna Metterza | Sahnt Ahn-na Met-tair-tsa | 013 |
| Sant'Ambrogio | Sahnt Am-broh-jo | 013 |
| Pontassieve | Pon-tas-syeh-veh | 013 |
| Fra Angelico | Fra An-jeh-lee-ko | 013 |
| Uccello | Oo-chel-lo | 013, 014; b 012 E |
| Lionardo Bartolini Salimbeni | Lyo-nar-doh Bar-toh-lee-nee Sa-leem-beh-nee | 014 |
| San Romano | San Ro-mah-no | 013, 014 |
| Tolentino | To-len-tee-no | 014 |
| Bernardino della Carda | Ber-nar-dee-no del-la Kar-da | 014 |
| Pollaiolo | Pol-lye-oh-lo | 015 |
| Tribunale di Mercanzia | Tree-boo-nah-leh dee Mer-kahn-tsee-a | 015 |
| Savonarola | Sa-vo-na-roh-la | 015, 019 |
| Gaspare del Lama | Gahs-pa-reh del Lah-ma | 016 |
| Pierfrancesco | Pyair-fran-ches-ko | 017, 027, 028 |
| Poliziano | Po-lee-tsyah-no | 018 |
| Portinari | Por-tee-nah-ree | 020 |
| Pigello | Pee-jel-lo | 020 |
| Baroncelli | Ba-ron-chel-lee | 020 |
| Margherita | Mar-geh-ree-ta | 020 |
| Hugo van der Goes | Hyoo-go van der Khoos | 020 |
| Sassetti | Sas-set-tee | 020 |
| Jacopo Zucchi | Yah-ko-po Tsook-kee | 021 |
| Ludovico Buti | Loo-doh-vee-ko Boo-tee | 021 |
| Stefano Bonsignori | Steh-fa-no Bon-see-nyoh-ree | 021 |
| Willem Tetrode | Vil-lem Teh-troh-deh | 021 |
| Cleomenes | Klee-om-eh-neez | 022 |
| Domenico Veneziano | Do-meh-nee-ko Veh-neh-tsyah-no | 024 |
| Castagno | Kas-tahn-yo | 024 |
| Federico da Montefeltro | Feh-deh-ree-ko da Mon-teh-fel-tro | 025 |
| Battista Sforza / Ludovico Sforza | Bat-tees-ta Sfor-tsa / Loo-doh-vee-ko Sfor-tsa | 025, 031 |
| Piero della Francesca | Pyeh-ro del-la Fran-ches-ka | 024, 025 |
| Piero (alone, and Piero di Cosimo / del Pollaiolo) | Pyeh-ro | 015, 016, 025, 027, 030 |
| Urbino | Oor-bee-no | 024, 025 |
| Rosselli | Ros-sel-lee | 025 |
| Perugino | Peh-roo-jee-no | 025, 026 |
| Vannucci | Van-noot-chee | 026 |
| Perugia | Peh-roo-ja | 026 |
| Signorelli | See-nyo-rel-lee | 027, 028, 034 |
| Verrocchio | Ver-rok-kyo | 029, 030 |
| Francesco | Fran-ches-ko | 001, 002, 022, 034 |
| Francesco del Tasso | Fran-ches-ko del Tahs-so | 034 |
| Maddalena | Mad-da-lay-na | 034 |
| Pompeo Colonna | Pom-peh-oh Ko-lon-na | 033 |

**Places:**

| Name | Respelling | Tracks |
|---|---|---|
| Santa Trinita | San-ta Tree-nee-ta, stress on TREE | 005, 012 |
| Vallombrosan | Val-lom-broh-zan | 005, 029 |
| Via Larga | Vee-a Lar-ga | 014, 017 |
| Castello | Kas-tel-lo | 017, 018 |
| Sant'Egidio | Sahnt Eh-jee-dyo | 020 |
| Santa Maria Nuova | San-ta Ma-ree-a Nwoh-va | 020 |
| Palazzo Vecchio | Pa-lat-tso Vek-kyo | 002, 023 |
| Ponte Vecchio | Pon-teh Vek-kyo | 023 |
| Santa Lucia de' Magnoli | San-ta Loo-chee-a deh Man-yoh-lee | 024 |
| Città della Pieve | Cheet-tah del-la Pyeh-veh | 026 |
| San Giusto alle Mura | San Joos-toh al-leh Moo-ra | 026 |
| San Donato a Scopeto | San Do-nah-toh a Sko-peh-toh | 027, 031 |
| San Salvi | San Sal-vee | 029 |

**Latin, Greek and other words:**

| Name | Respelling | Tracks |
|---|---|---|
| Ave gratia plena | Ah-veh grah-tsya pleh-na | 009 |
| mala medica | mah-la meh-dee-ka | 014 |
| lettuccio | let-toot-cho | 017 |
| Magnificat anima mea Dominum | Mahn-yee-fee-kat ah-nee-ma meh-a Doh-mee-noom | 019 |
| Spinario | Spee-nah-ryo | 032 |
| Polykleitos | Pol-ee-kly-tos | 032 |
| Laocoön | Lay-ok-oh-on | 034 |

Already in the dictionary and fine: Giotto, Masaccio, Vasari, Medici, Cosimo, Buontalenti, Ghirlandaio, Filippino, Filippo Lippi, Strozzi, Soderini, Fra Bartolomeo, Doni, Agnolo, Cortona, Niccolò, Parigi, Opificio delle Pietre Dure, Vittoria della Rovere, Signoria.

Collision check for the lead: `\b` matching means "Lippo" does not hit "Lippi", "Giottino" does not hit "Giotto", and "Piero" does not hit "Pierfrancesco". Add the longer keys ("Piero della Francesca", "Gentile da Fabriano") before the short ones; the code already sorts by length.

## 6. Facts re-verified (WebFetch, one page at a time, 24 Oct 2026; no curl, no browser, no CAPTCHA)

**uffizi.it pages:**

| Page | Confirms |
|---|---|
| `cross_432` | S10 |
| `…ognissanti-maesta` | S5: "Humiliati monks who officiated" |
| `annunciation-with-st-margaret-and-st-ansanus` | M10; S8 declined |
| `saint-anne-masaccio` | S12 |
| `angelico-glorification` | S12 |
| `adoration-of-the-shepherds…` (Portinari) | S15 |
| `medici-venus` | S16; page also says the Venus reached Florence in 1677, consistent with "Later" |
| `adoration-of-the-magi-filippino-lippi` | M4, S18 |
| `holy-family-signorelli` | S19 |
| `leonardo-adoration-of-the-magi` | M6, S18 |
| events `leonardo-s-magic-cosmos…` | M7: "unusually for his day … directly on the panel rather than on paper"; no perspective study mentioned |
| `annunciation` | S20 |
| `adoration-of-the-child-fra-bartolomeo` | S23 |
| news `…hall-of-ancient-marbles…` | S22 |
| `botticelli-madonna-of-the-magnificat` | S14 |

**Other sources:**
- SEC finestresullarte, Rucellai: M8.
- One WebSearch, for the perspective study (M7): no official page was found.

The facts behind each change are also noted in that track's @sources ("AUDIT FIX 24 Oct 2026").

## 7. Files changed

- **Tracks:** `v5/tracks/002–007, 009, 010, 012–015, 018, 020–023, 025, 027, 028, 030–034 .perf.txt`. That is speech, plus the @where of 003 and @sources notes.
- **Bridges:** `v5/bridges/001-019.txt`, lines 002 E>004, 002 H>006, 007 H>017 and 009 E>012. `v5/bridges/020-037.txt` is unchanged (every 001–034 line there was OK in the audit).
- **Other:**
  - `v5/PLAN.md` (errata only: §1 step 3, rows 027 cue and 028, §5 O4);
  - `research/FLOOR2_LOCATIONS_OCT2026.md` (tondo errata);
  - `v5/ONSITE_CHECKLIST.txt`;
  - `build/scripts_md.py` (S25: Botticelli codes not printed).
- **Backups** of every original are in the session scratchpad, `orig/`.

# Uffizi Gallery, second floor: where the old guide's works hang now (research of 24 Oct 2026)

## 0. Method

- **Map:** the museum's October 2026 visitor map (`source/map.txt`, `research/map/p-1.png` to `p-3.png`). It matches the English PDF that uffizi.it offers today, `https://www.datocms-assets.com/103094/1791457668-mappauffizien_ottobre2026.pdf`. That link is on https://www.uffizi.it/en/the-uffizi, which I read on 24 Oct 2026. I also read the PDF itself, and its legend wording is identical to `map.txt`. The asset ID prefix 1791457668 is a Unix timestamp for **8 Oct 2026, 11:07 UTC**. The same rule dates the not-on-display PDF exactly: 1792572271 is 21 Oct 2026, 08:44 UTC, the same minute as its notice page's last modification. So the map was uploaded around 8 Oct 2026.
- **Works:** I read each work's official page on www.uffizi.it (`/en/artworks/<slug>`) with WebFetch, one page at a time. I found slugs with WebSearch limited to uffizi.it. The "Location" (Collocazione) field is quoted exactly. Where WebFetch exposed the page's `modified_time` metadata, I give it, because it shows how fresh the Location field is.
- **Notices:** I read the notices index, the room-closure notice (EN and IT), the not-on-display notice and its Uffizi PDF, the strike notice, the Vasari Corridor rules, and the news items on the Botticelli rooms and the 2026 works programme. Details are in `NOTICES_OCT2026.md`.
- **Not used:** curl, a browser, CAPTCHAs, or Wikipedia.
- **Source grades:** **OFF** = official uffizi.it page (or the official map/PDF) read directly. **SEC** = reliable secondary source (none used). **SNIP** = search-result snippet only. **MAP** = my own reading of the official map image (line colours, room shading).

### Status key
- **SAME**: the official Location field names the same room as the old guide, and the room is open on the map.
- **MOVED**: the work is officially in a different room.
- **ON LOAN**: the work is on the official not-on-display list as lent to an exhibition.
- **RESTORATION**: the work is on the official list as under restoration.
- **NOT ON DISPLAY**: the work's room is closed or "work in progress", so it cannot be seen there.
- **NOT FOUND**: I found no official page.
- **CHECK**: official sources contradict each other. Confirm on site, or with the museum, before recording.

## 1. Caveats (read first)

1. **The Botticelli rooms: the official sources conflict. CHECK. This is the biggest open question.**
   - **Map legend (8 Oct 2026, newest dated source):** "A9 Botticelli, The Spring and Venus" and "A10-A11-A12 Work in progress". The photo strip also labels the Venus "A9 Botticelli".
   - **The same map's floor plan (MAP):** A9 is drawn in the **pale blue** that the map uses for rooms that are not open. A10 and A11–A12 are drawn in the **dark blue** of open rooms. Pixel check: A9 is RGB 151,173,216, the same as A17–A21, A33, A36 and A40–A42; A10 and A11–A12 are RGB 83,119,190, the same as the open rooms. On the first floor the same pale shading marks exactly the legend's WIP and closed rooms (D3, D10, D11, C6–C12). The second-floor plan therefore contradicts its own legend.
   - **Closure notice** "Uffizi: restoration and rearrangement works and rooms temporarily closed" (last modified 15 Sep 2026, OFF): "Work in progress rooms A9, A17/A21, A40/A42 (2nd floor), C7/C12, D3, D9/D11 (1st floor)." It names **A9**, not A10–A12.
   - **News, 16 Jun 2026, "The new permanent installation of the Botticelli Rooms" (OFF):** the Birth of Venus and the Primavera "are now displayed facing one another" in "jewel-box rooms" joined by a passage. The Magnificat and the Pomegranate Madonna flank the Venus. The sequence opens with the Lama Adoration and closes with the Calumny. A Pollaiolo room holds the Virtues. No room codes are given.
   - **Artwork pages, most edited 11–12 Sep 2026 (OFF):** Fortitude "A10. Pollaiolo e Botticelli", Primavera "A11. Botticelli, La Primavera", Birth of Venus "A12. Botticelli, La Venere".
   - **Reading:** the June news, the September pages, the September notice and the map's own shading all agree: the Botticellis are in **A10–A12** and **A9** is closed. Only the map's legend text says A9, and that text matches the pre-June 2026 temporary arrangement. The old guide's track 014 describes that same arrangement. The legend is the newest dated item, but it looks like text carried over from an earlier edition. **Recommendation:** do not hard-code "A9" in the Botticelli tracks until someone has walked the rooms or the museum has confirmed. Name the works, and use cues that hold either way ("the Botticelli rooms, after the Masaccio–Angelico–Uccello room A8").
2. **A17–A21 (Renaissance beyond the Alps and 15th-century Siena): probably closed. CHECK.** The map legend names these rooms normally. But the 15 Sep notice lists "A17/A21" as work in progress, and the plan shades A17–A21 pale. A works-programme news item (5 Aug 2026, last modified 9 Sep 2026, OFF) lists "Reopening of the rooms of the Flemish Masters" and says the Flemish Masters rooms "will be given a new layout and an updated lighting system". The Dürer page puts his Adoration in A20, not A17.
3. **A40–A42: closed.** The map, the notice and the shading all agree. The notice says their works "can now be viewed in rooms C9/C10 (floor 1)". But the map marks C6–C11 as "Work in progress" and C7–C8 as "Temporarily closed". **CHECK** whether C9/C10 are open.
4. **A36, the Hall of Ancient Inscriptions, is shaded pale.** The 5 Aug 2026 news says "the gallery of ancient inscriptions" "will be opened to the public", which is future tense. Treat it as **not open** (CHECK). The Classic line runs past it to the Buontalenti staircase.
5. **A33: "Work in progress"** (map legend and shading).
6. **Pages may be stale.** The Doni portraits page gives "Saturn Room" (Pitti), but its own text says the portraits have been shown at the Uffizi since 5 June 2018. Pages for works in closed rooms (A41, A42) still give those rooms.
7. **Strike on 30 Oct 2026:** the Uffizi opens only 1:30 to 6:30 pm, and "Closures and disruptions may therefore occur." (OFF)

## 2. Not-on-display list: second-floor extract (OFF, list updated 21 Oct 2026)

Source: https://pdf.uffizi.it/1792572271342-aggiornamento-al-21.10.26.pdf, linked from https://www.uffizi.it/en/notices/artworks-not-on-display (page last modified 21 Oct 2026).

| Room | Work | Inv. | Reason | Dates |
|---|---|---|---|---|
| A6 (Il Trecento a Firenze) | Giovanni da Milano, *Polittico di Ognissanti* (title cut off in source) | 1890 n. 459 | Restoration | not stated |
| A6 | Giottino, *Deposizione* ("Pietà di San Remigio") | 1890 n. 454 | Restoration | not stated |
| A15 (Stanzino delle Matematiche) | Willem Tetrode, *Venere* (bronze) | Bargello Bronzi n. 131 | Loan, Ashmolean Museum, Oxford | 8 Oct 2026 – 11 Apr 2027 |
| A42 (and Palazzo Davanzati n. 385) | Francesco Granacci, *Giuseppe condotto in prigione* | 1890 n. 2150 | Loan, Scuderie del Quirinale, Rome | 8 Oct 2026 – 7 Feb 2027 |

None of the old guide's headline works is on the list. The first-floor entries are in `NOTICES_OCT2026.md`.

## 3. Works table: everything named in old tracks 001–036

All URLs are https://www.uffizi.it/en/artworks/… and all were read directly (OFF) unless marked otherwise. "Mod." is the page's last-modified date, where WebFetch showed it.

| Track | Artist, title (official) | Date (official) | Medium; inv. | Official URL | Location field (verbatim) | Old room | Status | Note |
|---|---|---|---|---|---|---|---|---|
| 001 | (outside; Tribune mentioned) | – | – | – | – | courtyard | – | Says "the Classic route" ends with Caravaggio and Rembrandt. On the map that is the end of the Classic and Complete routes on floor 1 (E-rooms). Tickets are nominal (name must match ID) since 13 Oct 2025. |
| 002 | Eastern Corridor (ancient sculpture, grotesque ceiling) | – | – | – | Map: "A2 Eastern Corridor" | A2 | SAME | General description only. |
| 003 | 13th-century room, sample: Pisan painter, *Painted cross* | "12th century" | Tempera on wood, gold ground; 1890 no. 432 | /cross_432 | "A3. Medieval Painting" | A3 | SAME | The map calls A3 "13th Century painting"; the page calls it "Medieval Painting". |
| 004–005 | Cimabue, *Virgin and Child Enthroned, and Prophets (Santa Trinita Maestà)* | "1290-1300 ca." | Tempera on wood, gold background; 384 x 223 cm; 1890 no. 8343 | /virgin-and-child-enthroned-and-prophets-santa-trinita-maesta | "A4. Giotto - Cimabue" | A4 | SAME | The old date "about 1280" is wrong; use 1290–1300. The wall positions (right, left, centre) are not on any official page: CHECK on site. |
| 004, 006 | Duccio di Buoninsegna, *Virgin and Child enthroned, surrounded by angels (Rucellai Madonna)* | "1285 ca." | Tempera on wood, gold background; 450 x 290 cm; inv. not shown | /virgin-and-child-enthroned-surrounded-by-angels-known-as-the-rucellai-madonna | "A4. Giotto - Cimabue" | A4 | SAME | On deposit from Santa Maria Novella. |
| 004, 007 | Giotto, *Virgin and Child enthroned, surrounded by angels and saints (Ognissanti Maestà)* | "1300-1305 c." | Tempera on wood, gold background; 325 x 204 cm; 1890 no. 8344 | /virgin-and-child-enthroned-surrounded-by-angels-and-saints-ognissanti-maesta | "A4. Giotto - Cimabue" | A4 | SAME | The old date "about 1310" is wrong; use 1300–1305. |
| 008–009 | Simone Martini and Lippo Memmi, *Annunciation with St. Maxima and St. Ansanus* | "1333" | Tempera on wood, gold background; 184 x 168 cm; 1890 nos. 451, 452, 453 | /annunciation-with-st-margaret-and-st-ansanus | "A5. Lorenzetti - Simone Martini" | A5 | SAME | The page's alt text says "St. Margaret"; the heading says "St. Maxima". Use the heading. |
| 008 | Ambrogio Lorenzetti, *Presentation at the Temple* | "1342" | Tempera on wood, gold background; 1890 no. 8346 | /presentation-at-the-temple | "A5. Lorenzetti - Simone Martini" | A5 | SAME | A Lorenzetti sample for track 008. |
| 008 | Pietro Lorenzetti, *Virgin and Child enthroned, with angels* | "1340 c." | Tempera on panel, gold; 1890 no. 445 | /lorenzetti-madonna-majesty | "A5. Lorenzetti - Simone Martini" | A5 | SAME | |
| 008 (ref.) | Pietro Lorenzetti, *Saint Humility and scenes from her life* | "1335 - 1340 ca." | Tempera on wood, gold; 1890 nn. 6120-6126, 6129-6131, 8347 | /saint-humility-and-scenes-from-her-life | "A6. 14th Century" | (A5 implied) | MOVED (info) | Not named in the old guide, but this Lorenzetti hangs in A6, not A5. |
| 010 | Lorenzo Monaco, *Coronation of the Virgin* | "1414" | Tempera on wood, gold background; 1890 n. 885 | /coronation-of-the-virgin | "A7. Lorenzo Monaco - Gentile da Fabriano" | A7 | SAME | |
| 010–011 | Gentile da Fabriano, *Adoration of the Magi* | "1423" | Tempera on wood; 300 x 282 cm; 1890 n. 8364 | /adoration-of-the-magi | "A7. Lorenzo Monaco - Gentile da Fabriano" | A7 | SAME | The predella Presentation is a modern copy; the original is in the Louvre. The old guide says "three small predella scenes" without noting this. |
| 012 | Masolino and Masaccio, *Saint Anne, Madonna and Child, five angels ("Sant'Anna Metterza")* | "1424-1425 ca." | Tempera on wood; 1890 no. 8386 | /saint-anne-masaccio | "A8. Masaccio - Beato Angelico - Paolo Uccello" | A8 | SAME | |
| 012 | Beato Angelico, *Glorification of Mary* (with predella) | "1431-1435" | Tempera on wood, gold; 1890 no. 1612 | /angelico-glorification | "A8. Masaccio - Beato Angelico - Paolo Uccello" | A8 | SAME | Predella reunited in 2024 (news, OFF). |
| 012 | Beato Angelico, *Madonna and Child Enthroned with Angels* | "1435" | Tempera on wood, gold; Deposits no. 143 | /madonna-child-pontassieve | "A8. Masaccio - Beato Angelico - Paolo Uccello" | A8 | SAME | |
| 012–013 | Paolo Uccello, *Battle of San Romano* | "1435-1440 ca." | Tempera on wood; 182 x 323 cm; 1890 n. 479 | /battle-of-san-romano | "A8. Masaccio - Beato Angelico - Paolo Uccello" | A8 | SAME | The old guide's "rooms ten to twelve are closed" matches the map legend but not the notice or the pages (caveat 1). |
| 014–015 | Sandro Botticelli, *Birth of Venus* | "1485 ca." | Tempera on canvas; 172.5 x 278.5 cm; 1890 n. 878 | /birth-of-venus | "A12. Botticelli, La Venere" | A9 | **CHECK** | Map legend: A9. Page, June news, Sep notice and map shading: A10–A12. See caveat 1. |
| 014, 016 | Sandro Botticelli, *Spring* (Primavera) | "1480 c." | Tempera grassa on wood; 207 x 319 cm; 1890 n. 8360 | /botticelli-spring | "A11. Botticelli, La Primavera" (mod. 12 Sep 2026) | A9 | **CHECK** | Same conflict. The old guide's "slightly larger than the Venus and painted on wood" is correct. |
| 014 | Sandro Botticelli, *Virgin and Child, and Angels (Madonna of the Magnificat)* | "1483 c." | Tempera on wood; 1890 n. 1609 | /botticelli-madonna-of-the-magnificat | "A12. Botticelli, La Venere" (mod. 12 Sep 2026) | A9 | **CHECK** | The June news says it flanks the Venus. |
| 014 | Sandro Botticelli, *Adoration of the Magi* (Lama altarpiece) | "1470-1475" | Tempera grassa on wood; 1890 no. 882 | /boticelli-adoration-lami | "A11. Botticelli - Spring" (mod. 28 May 2026) | A9 | **CHECK** | The June news says it opens the Botticelli sequence. |
| 014 | Sandro Botticelli, *Pallas and the Centaur* | "1480-1485 c." | Tempera on canvas; Pitti Objects of Art 1911 n. 752 / Deposits n. 29 | /pallas-and-the-centaur | "A11. Botticelli - Spring" (mod. 3 Oct 2024) | A9 | **CHECK** | This page is older than the June 2026 rehang. |
| 017–018 | Hugo van der Goes, *Adoration of the Shepherds with angels and saints and the Portinari family (recto); Annunciation (verso)* (Portinari Triptych) | "1477-1478 c." | Oil on wood; 1890 nn. 3191, 3192, 3193 | /adoration-of-the-shepherds-with-angels-and-saints-recto-annunciation-verso | "A13. Hugo van der Goes" | A13 | SAME | The A13 track's lead-in from A9 ("next open room") depends on caveat 1. |
| 019 | *Medici Venus*, Hellenistic art | "Late 2nd century B.C. - Early 1st century B.C." | Parian marble (lychnite); h. 153 cm; 1914 no. 224 | /medici-venus | "A16. Tribune" | A16 | SAME | The Cleomenes signature on the base did not originally belong to the statue. |
| 019 (ref.) | *Wrestlers*, Roman art | "First century A.D." | Parian marble; 1914 n. 216 | /wrestlers | "A16. Tribune" | A16 | SAME | Also in the Tribune. |
| 019 (ref.) | *Knife Grinder (the Scythian)*, Roman art | "2nd century A. D." | Marble from Asia Minor; 1914 n. 230 | /knife-grinder-tribune | "A16. Tribune" | A16 | SAME | Also in the Tribune. |
| 020–021 | Albrecht Dürer, *Adoration of the Magi* | "1504" | Oil on wood; 1890 n. 1434 | /adoration-of-the-magi-durer | "A20. Renaissance beyond the Alps III" (mod. 4 Oct 2024) | A17 | **MOVED + CHECK** | The page says A20, not A17. The 15 Sep notice lists A17/A21 as work in progress, and the map shades A17–A21 pale, so the suite is probably closed (caveat 2). |
| 020 | Lucas Cranach the Elder (Adam and Eve; Luther portraits) | – | – | no artwork page found; news /news/aperte-le-nuove-sale-dei-fiamminghi (31 Jul 2024, OFF) | News: "three frescoed rooms" between the Tribune and the Cabinet of Miniatures | A17 | **NOT FOUND + CHECK** | The 2024 news puts Cranach, Dürer, Baldung Grien, Memling and Van der Weyden in these rooms. The rooms may be closed now. |
| 020 | "works in the orbit of Holbein": Holbein, *Portrait of Sir Richard Southwell* (1536) | 1536 (news) | – | news /news/uffizi-futuro-nell-antico-le-cornici-dei-maestri-d-oltralpe (25 Mar 2025, OFF) | no room given | A17 | **NOT FOUND + CHECK** | The news says it is "at the Uffizi"; no artwork page found. |
| 022 | Southern Corridor (*Dying Alexander*, porphyry she-wolf, Muse by Atticus) | – | – | /il-corridoio-di-mezzogiorno (mod. 10 Jun 2026) | Map "A23 Southern Corridor" | A23 | SAME | The view of the Arno and the Ponte Vecchio is confirmed. The page does not mention the Vasari Corridor. |
| 023 | Domenico Veneziano, *Madonna and Child enthroned with St. Francis, John the Baptist, St. Zenobius and St. Lucy* (Santa Lucia de' Magnoli) | "1445 c." | Tempera on wood; 1890 n. 884 | /veneziano-madonna-and-child-enthroned | "A25. Domenico Veneziano - Piero della Francesca" | A25 | SAME | |
| 023–024 | Piero della Francesca, *The Duke and Duchess of Urbino Federico da Montefeltro and Battista Sforza* | "1473-1475 c." | Oil on wood; 1890 nn. 1615, 3342 | /the-duke-and-duchess-of-urbino-federico-da-montefeltro-and-battista-sforza | "A25. Domenico Veneziano, Piero della Francesca" | A25 | SAME | The old guide is wrong on two facts. Its date "around 1465-72" should be 1473–1475. Its medium "oil and tempera" should be oil on wood. Also, Battista died in 1472, so the portrait is after her death, not "about the time". |
| 025 | Perugino, *Pietà* | "1493-1496ca." | Oil on wood; 1890 no 8365 | /pieta-perugino-uffizi-en | "A27. Pietro Perugino" | A27 | SAME | |
| 025 | Perugino, *Oration in the Garden* | "1493-1496ca" | Oil on wood; 1890 n. 8367 | /oration-in-the-garden | "A27. Pietro Perugino" | A27 | SAME | |
| 025 | Perugino, *Portrait of Francesco delle Opere* | – | – | no page found (two searches) | – | A27 | **NOT FOUND** | Confirm on site. Map room A34 is "Botticelli, Perugino", so Perugino works may also be there. |
| 026 | Filippino Lippi, *Adoration of the Magi* | "1496" | Tempera grassa on wood; 1890 n. 1566 | /adoration-of-the-magi-filippino-lippi | "A28 - Filippino Lippi, Piero di Cosimo" | A28 | SAME | The old guide says Leonardo's Adoration is "two rooms along". It is not: it is in A35, about seven rooms on. |
| 026 | Piero di Cosimo, *Perseus frees Andromeda* | "1510-1515" | Tempera grassa on wood; 1890 no. 1536 | /perseus-frees-andromeda | "A28. Filippino Lippi - Piero di Cosimo" | A28 | SAME | |
| 026 (ref.) | Filippo Lippi, *Madonna with Child and two Angels* ("Lippina") | "1460 - 1465 c." | Tempera on wood; 1890 n. 1598 | /lippi-madonna-and-child-with-two-angels | "C6" (mod. 28 Jan 2026) | "downstairs" | **CHECK** | It is on the first floor, as the old guide says. But the map marks C6–C11 "Work in progress", so it may not be visible. |
| 027 | Luca Signorelli, *Holy Family* (tondo, 124 cm diameter) | "1487 - 1488 c." | Oil on wood; 1890 n. 1605 | /holy-family-signorelli | "A31. Signorelli" | A31 | SAME | A second Signorelli tondo, *Madonna with Child* (1890 n. 502), is in A32. |
| 028 | Andrea del Verrocchio and Leonardo da Vinci, *The Baptism of Christ* | "1470 - 1475 c." | Tempera and oil on panel; 1890 n. 8358 | /verrocchio-leonardo-baptism-of-christ | "A35. Leonardo da Vinci" | A35 | SAME | |
| 028–029 | Leonardo da Vinci, *Annunciation* | "1472 c." | Oil on wood; 1890 n. 1618 | /annunciation | "A35. Leonardo da Vinci" | A35 | SAME | The page gives "Oil on wood"; the old guide's "oil and tempera" is wrong. |
| 028, 030 | Leonardo da Vinci, *Adoration of the Magi (San Donato in Scopeto)* | "1482 c." | Charcoal, watercolour ink and oil on wood; 1890 n. 1594 | /leonardo-adoration-of-the-magi | "A35. Leonardo da Vinci" | A35 | SAME | The old text says "Gentile's gorgeous procession upstairs". That is wrong: A7 is on this floor. |
| 031–032 | Michelangelo, *Holy Family, known as the "Doni Tondo"* | "1505-1506" | Tempera grassa on wood; 1890 n. 1456 | /holy-family-known-as-the-doni-tondo | "A38. Raphael and Michelangelo" | A38 | SAME | On the Classic route A38 is only a dotted detour (section 5). |
| 031–032 | Raphael (and Maestro di Serumido), *Portraits of Agnolo and Maddalena Doni* | "1504-1507 c." | Oil on basswood; 1912 nos. 61, 59 | /portraits-doni-raffaello | "Saturn Room" (Museum: Pitti Palace) (mod. 3 Sep 2026) | A38 | **CHECK** | The structured field says Pitti, but the body says "displayed in the Uffizi Galleries" since 5 June 2018. A 2023 Doni Day event page refers to "the Raphael and Michelangelo Room (A38)". Confirm on site before telling listeners they are "in this same room". |
| 031, 033 | Raphael, *Mary, Christ and the young John the Baptist ("Madonna of the Goldfinch")* | "Before February 1506" | Oil on wood; 1890 n. 1447 | /mary-christ-and-the-young-john-the-baptist-known-as-the-madonna-of-the-goldfinch | "A38. Raphael and Michelangelo Room" | A38 | SAME | |
| 031 (ref.) | Raphael, *Self portrait* | "1506" | Oil on panel; 1890 n. 1706 | /raphael-self-portrait | "C1. Self-portraits - From the origins to the 17th century" | ("other Raphael works") | MOVED (info) | Not in A38; it is on the first floor (C1). |
| 034 | *Niobe with her younger daughter*, Roman art | "First half of the 2nd century A.D." | Pentelic marble; 1914 no. 294 | /niobe-with-her-younger-daughter | "A39 - Niobe Room" | A39 | SAME | Found in Rome in 1583 and brought to Florence in 1770. On the Classic route A39 is a dotted detour only (section 5). |
| 035 | Andrea del Sarto, *Virgin and Child between St Francis and St John the Evangelist ("Madonna of the Harpies")* | "1517" | Oil on panel; 1890 no. 1577 | /andrea-del-sarto-harpies | "A41. Andrea del Sarto" (mod. 28 Jan 2026) | A41 | **NOT ON DISPLAY in A41 / CHECK** | The map has A41 as "Work in progress". The notice says A40/A42 works "can now be viewed in rooms C9/C10 (floor 1)", but the map has C6–C11 as WIP. The map's floor-1 room D9 is "Andrea del Sarto and Pontormo", yet the notice lists D9/D11 as WIP. Location today is unconfirmed. |
| 035 (ref.) | Andrea del Sarto, *Portrait of a Young Lady with a Book* | "1528" | Oil on panel; 1890 no. 783 | /young-lady-with-a-book | "A40. Fra Bartolomeo and School" | – | NOT ON DISPLAY in A40 / CHECK | A40 is WIP. |
| 036 | Francesco Granacci, *Giuseppe condotto in prigione* | – | 1890 n. 2150 | PDF list (OFF) | List: "Palazzo Davanzati n. 385; A42" | A42 | **ON LOAN** | Scuderie del Quirinale, Rome, 8 Oct 2026 – 7 Feb 2027. |
| 036 | Alonso Berruguete, *Madonna and Child* | "1510-1512 c." | Oil on wood; 1890 n.5852 | /madonna-and-child-berruguete | "A42. Franciabigio - Granacci - Berruguete - Beccafumi" (mod. 16 Oct 2024) | A42 | **NOT ON DISPLAY in A42 / CHECK** | A42 is WIP (map, notice, shading). The works may be in C9/C10 on the first floor (notice), which the map marks WIP. |
| 036 | Franciabigio, Beccafumi (unnamed works) | – | – | not searched individually | (A42 per room name) | A42 | NOT ON DISPLAY in A42 | Same as above. The track also routes visitors down the Lanzi staircase, which is wrong for the Classic route (section 5). |

**Count.** I checked 52 named works or spaces.
- **Wrong in the old guide (4 placements):**
  - Dürer, *Adoration of the Magi*: A20, not A17, and the suite is probably closed.
  - Madonna of the Harpies: A41 is closed.
  - The A42 room (Granacci on loan; Berruguete and the rest in a closed room).
  - The route: the old guide's walk through A40–A42 and down the Lanzi staircase is the Complete line, not the Classic.
- **Unconfirmed (CHECK):**
  - The 5 Botticellis.
  - The Doni portraits.
  - Cranach and Holbein, which have no pages and sit in probably closed rooms.
  - The Lippi Madonna in C6.
  - Francesco delle Opere (no page).
- **Factual errors in the text (not placements):**
  - Cimabue's date, Giotto's date, the Piero date and medium, and the Leonardo Annunciation medium.
  - "Gentile … upstairs".
  - "Leonardo's Adoration two rooms along".

## 4. Per-room content: what the official Location fields name today

Map titles come from the map legend. "Light" means the plan shades the room pale (MAP), which on this map marks rooms that are not open.

| Room (map title) | Map status | Works whose official Location names this room (grade) | Note |
|---|---|---|---|
| A1 Lorenese Vestibule | open; start of all routes | none found | Entrance from the Granducal staircase. |
| A2 Eastern Corridor | open | ancient sculpture (general) | |
| A3 13th Century painting | open | *Painted cross*, Pisan painter, 12th c., 1890 no. 432, "A3. Medieval Painting" (OFF); search also showed *Painted cross* 1890 n. 434, *Stigmata of St Francis*, *St Luke* (Master of the Maddalena) (SNIP) | |
| A4 Giotto, Cimabue | open | Cimabue *Santa Trinita Maestà*; Duccio *Rucellai Madonna*; Giotto *Ognissanti Maestà*; Master of St Cecilia, *Saint Cecilia and stories from her life*, ca. 1305-1310, 1890 no. 449 (all OFF) | |
| A5 Lorenzetti, Simone Martini | open | Simone Martini and Lippo Memmi *Annunciation*; Ambrogio Lorenzetti *Presentation at the Temple* (1342); Pietro Lorenzetti *Virgin and Child enthroned, with angels* (c.1340) (OFF) | |
| A6 14th Century | open | Pietro Lorenzetti *Saint Humility and scenes from her life* (OFF). **Under restoration (list):** Giovanni da Milano *Ognissanti Polyptych*; Giottino *Pietà di San Remigio* | Two headline works of the room are away. |
| A7 Lorenzo Monaco, Gentile da Fabriano | open | Gentile *Adoration of the Magi* (1423); Lorenzo Monaco *Coronation of the Virgin* (1414) (OFF) | |
| A8 Masaccio, Beato Angelico, P. Uccello | open | Uccello *Battle of San Romano*; Masolino and Masaccio *Sant'Anna Metterza*; Angelico *Glorification of Mary* with predella; Angelico *Madonna and Child Enthroned with Angels* (Pontassieve) (OFF) | |
| A9 "Botticelli, The Spring and Venus" | legend: open; **plan: light**; notice: WIP | **No artwork page gives A9.** | **CHECK** (caveat 1). |
| A10 / A11–A12 "Work in progress" | legend: WIP; **plan: dark (open)** | A10 "Pollaiolo e Botticelli": Botticelli *Fortitude* (1470). A11 "Botticelli, La Primavera": *Spring*; *Adoration of the Magi* (Lama); *Pallas and the Centaur*; *Virgin and Child enthroned with Saints* (c.1470). A12 "Botticelli, La Venere": *Birth of Venus*; *Madonna of the Magnificat*; *Calumny of Apelles* (c.1495); *Annunciation* (1489-90) (all OFF, most mod. 11–12 Sep 2026) | June 2026 news adds the *Madonna of the Pomegranate*, the *Madonna of the Rose Garden*, the *Madonna of the Cherubim*, the Annunciation fresco, the *Portrait of a man with a medal* and the *Stories of Judith* (no rooms given). |
| A13 Hugo van der Goes | open | *Portinari Triptych* (OFF) | |
| A14 Room of the Maps | open | no artwork page found; news "Terrazzo delle Carte geografiche reopens to the public after 20 years" exists (SNIP) | |
| A15 Room of Mathematics | open | Tetrode *Venere* (bronze) **on loan** to Oxford until 11 Apr 2027 (list) | |
| A16 Tribune | open (view from the doors; not verified) | *Medici Venus*; *Wrestlers*; *Knife Grinder* (OFF) | No official page I read says whether visitors can enter: CHECK. |
| A17–A20 Renaissance beyond the Alps | legend: open; **plan: light**; notice: "A17/A21" WIP | A20 "Renaissance beyond the Alps III": Dürer *Adoration of the Magi* (OFF). 2024 news: Dürer *Apostles* and *Madonna*, Cranach *Adam and Eve* and *Luther* portraits, Baldung Grien *Adam and Eve*, Memling *Portrait of a Man with a Letter*, Van der Weyden *Lamentation*, Froment *Triptych* (OFF news, no codes). 2025 news: Holbein *Sir Richard Southwell*, Dürer *St James* and *St Philip* (OFF news, no codes) | **Probably closed: CHECK** (caveat 2). |
| A21 15th Century in Siena | **light**; notice WIP | none found (one search) | Probably closed. Sassetta's *Madonna of the Snow* is on floor 1 in B2 (OFF). |
| A22 Cabinet of Miniatures | open | none found | |
| A23 Southern Corridor | open | *Dying Alexander* (head), porphyry she-wolf, Muse by Atticus of Aphrodisias (OFF corridor page) | |
| A24 Western Corridor | open | ancient sculpture (a page "The West Corridor (or Third Corridor)" exists, SNIP) | All routes run along it. |
| A25 Domenico Veneziano, Piero della Francesca | open | Piero *Duke and Duchess of Urbino*; Domenico Veneziano *Santa Lucia de' Magnoli Altarpiece* (OFF) | |
| A26 Cosimo Rosselli | open | Cosimo Rosselli *Madonna and Child Enthroned, angels, St Anthony Abbot and St Nicholas of Bari* (c.1470) (OFF) | |
| A27 Pietro Perugino | open | Perugino *Pietà* (1493-96); *Oration in the Garden* (1493-96) (OFF) | |
| A28 Filippino Lippi, Piero di Cosimo | open | Filippino *Adoration of the Magi* (1496); Piero di Cosimo *Perseus frees Andromeda* (1510-15) (OFF) | |
| A29 Lorenzo di Credi | open | none found | |
| A30 Piero di Cosimo | open | none found | |
| A31 Luca Signorelli | open | Signorelli *Holy Family* tondo (OFF) | |
| A32 Luca Signorelli | open | Signorelli *Madonna with Child* tondo (c.1490) (OFF) | |
| A33 Work in progress | WIP, light | – | |
| A34 Botticelli, Perugino | open | **no artwork page found** (three searches) | CHECK on site. |
| A35 Leonardo Da Vinci | open | Leonardo *Annunciation*; Leonardo *Adoration of the Magi*; Verrocchio and Leonardo *Baptism of Christ* (all OFF) | All three of the old guide's works are here. |
| A36 Hall of Ancient Inscriptions | **light**; news (Aug 2026): "will be opened" | – | Probably not open: CHECK. The Classic route turns down beside it. |
| A37 The Cabinet of Marbles | open | *Spinario* (1st c. BC), "A37. Gabinetto dei marmi" (OFF). 2024 news: *Menander*, green basalt *Doryphoros* torso, *Zeus Ammon*, Hermaphrodite and Pan, Roman reliefs (OFF news) | The Classic line reaches the Buontalenti staircase at A37. |
| A38 Raphael and Michelangelo | open | Michelangelo *Doni Tondo*; Raphael *Madonna of the Goldfinch*; Raphael *St John the Baptist as a Boy* (c.1518); Fra Bartolomeo *Adoration of the Child* / *Presentation in the Temple* (c.1497) (all OFF). The Doni portraits: CHECK | Raphael's *Self portrait* is in C1, not here. |
| A39 Niobe Room | open | *Niobe with her younger daughter* (OFF) | |
| A40–A42 Work in progress | WIP, light; notice WIP | Pages still say A40 (Andrea del Sarto *Young Lady with a Book*), A41 (*Madonna of the Harpies*), A42 (Berruguete *Madonna and Child*) (OFF) | Notice: the works are shown in C9/C10 on floor 1. The map marks C6–C11 WIP: CHECK. |

## 5. The route (from `p-3.png`, MAP)

- **Start:** all three lines (Fast in cyan, Classic in red, Complete in orange) begin at "VISIT START" at the top of the **Granducal staircase**. They enter A1 and turn right along the Eastern Corridor A2. The arrows point towards the Tribune and A22. The lines then run down the Southern Corridor A23 and turn into the Western Corridor A24, heading back north (arrows pointing left).
- **The split at the Buontalenti staircase:**
  - The **red Classic line** leaves the corridor and turns down beside A36 to the **Buontalenti staircase**, between A38 and A36, with A37 below it. The bottom strip of the map labels this "CONTINUE CLASSIC ITINERARY".
  - From that point a **red dotted line** carries on west along the Western Corridor, with a dotted spur into **A39, the Niobe Room**. I read this as an optional detour for Classic visitors. It runs past A38, but no dotted spur enters A38. In the bottom strip the red dotted segment runs only from the Buontalenti box towards the A37 thumbnail. The A38 and A39 thumbnails hang only from the cyan and orange lines.
- **Answer to the question:** **A38 (Raphael and Michelangelo) and A39 (Niobe) are not on the solid Classic line.** They lie on the Fast and Complete lines, beyond the Buontalenti staircase, towards the Lanzi staircase. A Classic visitor reaches them only by the dotted detour, then must walk back east to the Buontalenti staircase. The old guide's order (A35 → A38 → A39 → A41 → A42 → Lanzi) follows the **Complete** line, and it sends visitors into closed rooms A40–A42.
- **Lanzi staircase:**
  - The **cyan Fast** and **orange Complete** lines continue to the west end of A24 and go down the **Lanzi staircase**.
  - The bottom strip says "LANZI STAIRCASE – END OF FAST ITINERARY – CONTINUE COMPLETE ITINERARY".
  - On p-1, Fast ends at the ground-floor "EXIT – END FAST ITINERARY" by the Loggia dei Lanzi. Complete continues on floor 1 from the Lanzi staircase into the C-rooms (p-2).
- **A contradiction inside the map:** the legend text on p-1 and in `map.txt` says Classic is "DESCENT FROM 2ND TO 1ST FLOOR (THROUGH THE LANZI STAIRCASE)". But every drawn line says Classic goes down the **Buontalenti** staircase: p-3, the 3D drawing on p-1, and p-2, where the Classic line starts at the Buontalenti staircase on floor 1. Follow the drawn lines and note the text error.
- **The warning:** next to the Lanzi staircase, with crossed cloakroom and audioguide icons: "ONCE OUT, IT IS NO LONGER POSSIBLE TO ACCESS THE CLOACKROOM AND AUDIOGUIDE DESK" (sic). The p-1 Fast text says: "If you leave through this exit, you will miss the Cloakroom, the Audioguide Return Desk and the Main Museum Shop." A Classic guide must not send people down the Lanzi staircase, or they cannot return audioguides or collect coats.
- **Panoramic terrace and café:** at the far west end of the second floor, to the left of the Lanzi staircase and A42, there is a "PANORAMIC TERRACE" block with café cup icons and an outdoor-space sun icon. It sits where the Fast and Complete lines end, on the corridor side of the exit symbol as far as the drawing shows. It is not on the solid Classic line. A Classic visitor would have to walk the whole Western Corridor beyond the Buontalenti staircase and come back. Whether the terrace can be reached without passing the "once out" point: CHECK on site. There is a lift icon at the Lanzi staircase and at the Buontalenti staircase, and a WC beside A40.
- **Floor 1 (p-2):** Classic comes down the Buontalenti staircase to around D9/D10. It runs east through the D-rooms (D12 Rosso, D15 Bronzino, D23 Titian), passes the Vasari Corridor entrance at D19 ("reservation only"), goes up the Verone corridor D27 to E4–E7 (Caravaggio, Artemisia, Rembrandt) and ends at the **Magliabechi staircase** ("END OF CLASSIC ITINERARY"). Complete adds the C-rooms and the B-rooms (Contini Bonacossi, dotted to B8) and ends at the same place.

## 6. CHECK list (confirm on site or with the museum before recording)

1. Which room holds the Birth of Venus and the Primavera today: A9 (map legend) or A11/A12 (pages, June news, Sep notice, map shading)? Is A9 open, and what is in it?
2. Are A17–A21 (northern masters and 15th-century Siena) open? Is Dürer's *Adoration* on view, and in which room (page: A20)? Where are Cranach and Holbein?
3. Are Raphael's Doni portraits in A38 (page body, and the 2023 event page) or at Pitti, Saturn Room (structured field)?
4. A34 "Botticelli, Perugino": which works? (No page found.) Is Perugino's *Francesco delle Opere* in A27 or A34?
5. A40–A42 works (*Madonna of the Harpies*, Berruguete, Franciabigio, Beccafumi): are they in C9/C10 on floor 1 (notice), and are C9/C10 open (map: C6–C11 WIP)?
6. Filippo Lippi's "Lippina" (page: C6): on view?
7. A36 Hall of Ancient Inscriptions: open or not?
8. Tribune A16: can visitors enter, or only look in from the doors?
9. A4: confirm which wall holds each Maestà (the old guide says Cimabue right, Duccio left, Giotto centre).
10. 30 Oct 2026 strike: afternoon-only opening, possible room closures.

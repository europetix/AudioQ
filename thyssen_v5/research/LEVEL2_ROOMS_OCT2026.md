# Thyssen-Bornemisza, Level 2 (rooms 1–29): what is on the walls, room by room (research of 23 Oct 2026)

> **Update 23 Oct 2026 (audit):** Daret's *The Nativity* (inv. 124) now reads "Not exhibited" (EN) / "No expuesta" (ES). Track 004 was rebuilt on Gerard David's *The Crucifixion* (Room 3) and the Bouts follower's *The Virgin and Child* (Room 3).

**Purpose:** a menu for the lead to choose 2–4 stops per room for the new Yo Tours guide.
**Builds on:** `CURRENT_LOCATIONS_OCT2026.md`. Works already checked there are reused, not re-researched. They are marked "(known)".

**Method**
- Every row comes from the work's own museothyssen.org collection page, read one page at a time with WebFetch.
- "Room wording" is the location label printed under "Inv. no." / "Nº INV.".
- The EN page was read unless the row says ES.
- Room titles come from `source/map.txt` (Dec 2025 map) and `research/map/p-2.png`.

**What I could not use:**
- The site has no list of works by room. The collection search (`/buscador/...`) is blocked to crawlers (robots), the room anchors on work pages (`#sala-N`) only point to the map, and no thematic tour gives room numbers.
- So candidates came from my knowledge of the collection, artist pages and the "More works of art from the Collection" links on each page. Those links group works by school and date, not by room. Every work was then confirmed on its own page.
- Two EN pages returned a JavaScript "you are being redirected" check and were skipped: Grimaldi (read in ES instead) and Wijnants. No other bot checks were met.

**Caveat:** the pages can be stale (the Van Eyck page still says Room 3 while the diptych is in The Hague). Confirm the final picks in the galleries before recording.

---

## 0. Key findings for route planning

1. **About 40 Level 2 works checked here are "Not exhibited" today.** Many are probably in The Hague ("Masterpieces from Madrid", 15 Oct 2026 – 17 Jan 2027) or were displaced when rooms 19–21 became the "Classical rooms". Do not script any of these:
   - Rogier van der Weyden, *Virgin and Child enthroned*
   - Fra Angelico, *Virgin of Humility*
   - Giovanni Bellini, *Nunc Dimittis*
   - Titian, *Virgin and Child* and *Antonio Anselmi*
   - Bronzino, *Cosimo de Medici in Armour*
   - Gossaert, *Adam and Eve*
   - Baldung, *Adam and Eve*
   - Cranach, Saxony altarpiece wings
   - Wolf Huber
   - Correggio
   - Dosso
   - Veronese, *Annunciation*
   - Tintoretto, *Senator*
   - Bassano, *Sower*
   - Ludovico Carracci
   - Guercino
   - Velázquez, *Mariana of Austria*
   - Van der Hamen
   - Maffei
   - Romanelli
   - Van Dyck, *Jacques Le Roy*
   - Rubens: *Rosary*, *Samson* and *Venus and Cupid*
   - Canaletto: *Bucintoro* and *Warwick Castle*
   - Giandomenico Tiepolo
   - Pittoni (x2)
   - Panini
   - Piazzetta, *Sacrifice of Isaac*
   - Amorosi
   - Koninck
   - **All three Goyas** (*Asensio Julià* and *Ferdinand VII* are "Not exhibited"; *El tío Paquete* is in a temporary show, per the known file)
2. **Room 29 ("Goya and Romanticism") has no Goya on display today.** Build it on Friedrich and Delacroix.
3. **The Flemish 17th century (Rubens, Van Dyck, Jordaens, Teniers, Brouwer) is effectively off Level 2.** None of the pages checked place any of it in a room. The Mauritshuis show itself brings a Brueghel/Rubens *Garden of Eden* to the Classical rooms.
4. **Odd location labels:**
   - Bernini, *San Sebastian* (marble, private loan): EN "Room de anoxia", ES "Sala de anoxia". It is not in Room 12, which is presumably a conservation/anoxia treatment space.
   - Tintoretto, *Paradise*: "Central hall", the ground-floor hall, not Room 11.
   - Carpioni, *Bacchanal*: "Pasillo de la sala 10 a la 15" (corridor).
   - Several works you might expect upstairs are on Level 0, Room A (Carmen Thyssen collection): Saraceni *Venus and Mars*, Francesco Guardi *Giudecca*, G. A. Guardi *Seraglio*, Zocchi *Arno*, Jan Brueghel *Garden of Eden*, Frans Post *Brazil*, Salomon van Ruysdael *Vecht*, Friedrich *Fishing Boat*.
5. **Room 6 (Villahermosa Gallery)** is a mix. It has a 16th-century Bordone next to 17th-century Roman/Bolognese works (Mola, Grimaldi). I could confirm only 3 works.
6. **Women artists on Level 2:** only **Louise Moillon** (*Still-Life with Fruit*, Room 24) was confirmed.
   - Giulia Lama appears as a sitter (Piazzetta's portrait of her, Room 18). She was herself a Venetian painter.
   - No other woman artist was found on a Level 2 page.
7. **EN/ES checks:**
   - No new EN/ES disagreements in the spot checks. These matched: Mola (Sala 6), Linard (Sala 21), Bernini (anoxia).
   - Known conflicts are still open, from the earlier file: Petrus Christus (EN not exhibited / ES Sala 3) and Goya *El tío Paquete*.
   - Grimaldi was read in ES only, because the EN page was blocked.
8. **The Thyssen's own Linard, *Chinese Bowl with Flowers*, is labelled "Room 21"** (EN and ES), inside the Mauritshuis exchange show. It is probably hung in dialogue with the Dutch still lifes.

---

## Room 1. 14th Century. Early Italian Painting

| Artist | Title | Date | Technique | URL | Room wording | Story line |
|---|---|---|---|---|---|---|
| Duccio di Buoninsegna | Christ and the Samaritan Woman | 1310 - 1311 | Tempera and gold on panel | https://www.museothyssen.org/en/collection/artists/duccio-di-buoninsegna/christ-and-samaritan-woman | "Room 1" / Level 2 / Permanent Collection (known) | A panel from the predella of Siena's great *Maestà*, the altarpiece the city carried to its cathedral in procession. |
| Master of the Magdalen | The Virgin and Child enthroned with Saints Dominic and Martin, and two angels | ca. 1290 | Tempera and gold on panel | https://www.museothyssen.org/en/collection/artists/master-magdalen/virgin-and-child-enthroned-saints-dominic-and-martin-and-two | "Room 1" / Level 2 / Permanent Collection | The page calls it the "oldest painting in the Thyssen-Bornemisza collection", and it still has its original stuccoed frame. This is where the museum begins. |
| Simone Martini | St. Peter | s.f. (text: c. 1325–1328) | Tempera and gold on panel | https://www.museothyssen.org/en/collection/artists/martini-simone/st-peter | "Room 1" / Level 2 / Permanent Collection | Part of a five-panel polyptych restored by Siena in 1448. It then vanished for two centuries and resurfaced under another painter's name. |
| Ugolino di Nerio | The Crucifixion with the Virgin, Saint John and Angels | ca. 1330 - 1335 | Tempera and gold on panel | https://www.museothyssen.org/en/collection/artists/nerio-ugolino-di/crucifixion-virgin-saint-john-and-angels | "Room 1" / Level 2 / Permanent Collection (inv. 412) | The panel was cut down, so the mourners are truncated. Ask listeners to imagine the missing half. |
| Giovanni di Paolo | St. Catherine before the Pope at Avignon | ca. 1460 - 1463 | Tempera and gold on panel | https://www.museothyssen.org/en/collection/artists/paolo-giovanni-di/st-catherine-pope-avignon | "Room 1" / Level 2 / Permanent Collection (inv. 162) | A woman tells the Pope to go home: Catherine of Siena urging Gregory XI to return the papacy from Avignon to Rome. |
| Giovanni di Paolo | The Virgin of Humility | ca. 1440 | Tempera and gold on panel | https://www.museothyssen.org/en/collection/artists/paolo-giovanni-di/virgin-humility | "Room 1" / Level 2 / Permanent Collection (inv. 161) | The Virgin seated on the ground, a "humble" pose. It stands in for Fra Angelico's *Virgin of Humility*, which is "Not exhibited". |

**Best for the main route:** Duccio (known track) + Master of the Magdalen ("the oldest painting in the museum").

## Room 2. 15th Century. German and Spanish Painting

| Artist | Title | Date | Technique | URL | Room wording | Story line |
|---|---|---|---|---|---|---|
| Joan Mates | Saint John the Baptist and Saint John the Evangelist with a Donor | ca. 1410 | Oil on panel (191 x 121 cm) | https://www.museothyssen.org/en/collection/artists/mates-joan/saint-john-baptist-and-saint-john-evangelist-donor | "Room 2" / Level 2 / Permanent Collection (inv. 282) | A big Catalan International Gothic panel. It was "anonymous" until 1989, when it was given back to Mates. |
| Jaume Huguet (circle of) | Pilgrims' Mass | ca. 1450 - 1500 | Tempera and gold on panel | https://www.museothyssen.org/en/collection/artists/huguet-jaume-circle/pilgrims-mass | "Room 2" / Level 2 / Permanent Collection (inv. 199) | Catalan gold-ground painting. Its title and attribution changed several times before 1992. |
| Anonymous German artist, active in Konstanz | The Birth of the Virgin | ca. 1430 | Panel | https://www.museothyssen.org/en/collection/artists/anonymous-german-artist-active-konstanz-ca-1430/birth-virgin | "Room 2" / Level 2 / Permanent Collection (inv. 262) | A 15th-century lying-in room: women bathe the newborn Mary, cook and help St Anne wash. It is drawn from the apocryphal gospels. |
| Anonymous German artist, Middle Rhine | The Descent from the Cross (recto) | ca. 1420 | Oil on panel | https://www.museothyssen.org/en/collection/artists/anonymous-german-artist-active-middle-rhine-area-ca-1420/descent-cross-recto | "Room 2" / Level 2 / Permanent Collection (inv. 268.a) | A two-sided panel. The verso (*Christ bearing the Cross*) shows a nun following Christ with her own cross. Not separately checked: the companion *Presentation in the Temple* (Konstanz) |

**Best for the main route:** Konstanz *Birth of the Virgin* (everyday life in a holy scene) + Joan Mates (Spanish link).

## Room 3. 15th Century. Early Netherlandish Painting

| Artist | Title | Date | Technique | URL | Room wording | Story line |
|---|---|---|---|---|---|---|
| Jacques Daret | The Nativity | ca. 1434-35 | Oil on panel | https://www.museothyssen.org/en/collection/artists/daret-jacques/nativity | "Room 3" / Level 2 (inv. 124) | Salome the doubting midwife reaches out to test the miracle and is healed. The apocryphal Pseudo-Matthew story makes a vivid scene for listeners. |
| Gerard David | The Crucifixion | ca. 1475 | Oil on panel | https://www.museothyssen.org/en/collection/artists/david-gerard/crucifixion | "Room 3" / Level 2 / Permanent Collection (inv. 125) | It came from the Augustinian abbey of St Florian near Linz and joined the collection at Villa Favorita in 1928. |
| Dirck Bouts (follower of) | The Virgin and Child | ca. 1465 | Oil on panel | https://www.museothyssen.org/en/collection/artists/bouts-dirck-follower/virgin-and-child | "Room 3" / Level 2 / Permanent Collection (inv. 60) | Built on Jan van Eyck's *Virgin of the Fountain*. A way to talk about Van Eyck's influence while his diptych is in The Hague. |
| Petrus Christus | The Virgin of the dry Tree | ca. 1465 | – | (see known file) | EN "[Not exhibited]" / ES "Sala 3": **CONFLICT** (known) | Do not use until confirmed. |

Not on display or elsewhere:
- Van Eyck, *Annunciation Diptych*: on loan to The Hague (known).
- Rogier van der Weyden, *Virgin and Child enthroned* (https://www.museothyssen.org/en/collection/artists/weyden-rogier-van-der/virgin-and-child-enthroned): "Not exhibited".
- Campin and Memling are in Room 5.

**Best for the main route:** Daret *Nativity* (the midwife story) + Gerard David. Mention briefly that the Van Eyck is away.

## Room 4. 15th Century. Italian Painting

| Artist | Title | Date | Technique | URL | Room wording | Story line |
|---|---|---|---|---|---|---|
| Bramantino (Bartolomeo Suardi) | The Risen Christ | ca. 1490 | Mixed media on panel | https://www.museothyssen.org/en/collection/artists/bramantino-bartolomeo-suardi/risen-christ | "Room 4" / Level 2 / Permanent Collection (inv. 61) | A pale, haunting Christ against a night landscape. For years scholars argued whether it was by Bramantino or Bramante. |
| Paolo Uccello | The Crucifixion with the Virgin, Saint John the Baptist, Saint John the Evangelist and Saint Francis | ca. 1460 - 1465 | Tempera on panel | https://www.museothyssen.org/en/collection/artists/uccello-paolo/crucifixion-virgin-saint-john-baptist-saint-john-evangelist-and | "Room 4" / Level 2 / Permanent Collection (inv. 411) | Vasari's perspective-obsessed recluse, "ending up as poor as he was famous". |
| Cosmè Tura | Saint John the Evangelist in Patmos | ca. 1470 - 1475 | Tempera on panel | https://www.museothyssen.org/en/collection/artists/tura-cosme/saint-john-evangelist-patmos | "Room 4" / Level 2 / Permanent Collection (inv. 410) | St John writing the Apocalypse in exile, with his eagle holding the inkwell. |
| Marco Zoppo | Saint Jerome in the Desert | ca. 1450 - 1455 | Mixed media on panel | https://www.museothyssen.org/en/collection/artists/zoppo-marco/saint-jerome-desert | "Room 4" / Level 2 / Permanent Collection (inv. 446) | Jerome with his lion, books and cardinal's hat. Scholars still disagree on whether it dates from the 1450s or about 1471. |
| Anonymous Valencian artist | The Crucifixion | ca. 1450 - 1460 | Oil on panel | https://www.museothyssen.org/en/collection/artists/anonymous-valencian-artist-active-1450-1460/crucifixion | "Room 4" / Level 2 / Permanent Collection | An attribution detective story: Dalmau, then Colantonio, then the young Antonello, then a Neapolitan, and finally Valencia. |

Not on display:
- Fra Angelico, *Virgin of Humility* (https://www.museothyssen.org/en/collection/artists/angelico-fra-fra-giovanni-da-fiesole/virgin-humility): "Not exhibited".
- Antonello, *Portrait of a Man*: "Not exhibited" (known).

**Best for the main route:** Bramantino + Uccello.

## Room 5. 15th and 16th Centuries. Renaissance Portraiture

| Artist | Title | Date | Technique | URL | Room wording | Story line |
|---|---|---|---|---|---|---|
| Domenico Ghirlandaio | Portrait of Giovanna degli Albizzi Tornabuoni | 1489 - 1490 | Mixed media on panel | https://www.museothyssen.org/en/collection/artists/ghirlandaio-domenico/portrait-giovanna-degli-albizzi-tornabuoni | "Room 5" (known; it is the map's cover image) | A posthumous portrait of a young Florentine wife who died in childbirth. The museum's poster image. |
| Hans Holbein the Younger | Portrait of Henry VIII of England | ca. 1537 | Oil on panel | https://www.museothyssen.org/en/collection/artists/holbein-hans-joven/portrait-henry-viii-england | "Room 5" / Level 2 / Permanent Collection (known) | The tiny portrait that fixed Henry's image for ever. |
| Hans Memling | Portrait of a Young Man praying (recto) | ca. 1485 | Oil on panel | https://www.museothyssen.org/en/collection/artists/memling-hans/portrait-young-man-praying-recto | "Room 5" (known) | The back (*Flowers in a Jug*, verso) is one of the earliest still lifes. |
| Robert Campin | Portrait of a Stout Man. Robert de Masmines (?) | ca. 1425 | Oil on panel | https://www.museothyssen.org/en/collection/artists/campin-robert/portrait-stout-man-robert-masmines | "Room 5" / Level 2 (inv. 74) | A blunt, unflattering early Netherlandish face. It was unpublished until 1957, when it was found with descendants of the sitter's family. |
| Francesco del Cossa | Portrait of a Man with a Ring | ca. 1472 - 1477 | Oil on panel | https://www.museothyssen.org/en/collection/artists/cossa-francesco/portrait-man-ring | "Room 5" / Level 2 / Permanent Collection (inv. 105) | He holds up a ring to us. It was long thought to show the painter Francia, until Longhi gave it to Cossa. |
| Raphael and Collaborator | Portrait of a Young Man | ca. 1518 - 1519 | Oil on panel | https://www.museothyssen.org/en/collection/artists/raphael-and-collaborator/portrait-young-man (read via https://www.museothyssen.org/en/node/16611) | "Room 5" / Level 2 / Permanent Collection (inv. 330) | Raphael's last years, with a shared studio hand. Good for "who really painted it?". |
| Lorenzo Lotto | Self-Portrait | not stated on page | Oil on panel | https://www.museothyssen.org/en/node/17028 (canonical slug not confirmed) | "Room 5" / Level 2 / Permanent Collection (inv. 230) | A painter's own face among the patrons. |

**Best for the main route:** Ghirlandaio + Holbein. Optional third: Memling (turn to the flower back).

## Room 6. 16th Century. Villahermosa Gallery

| Artist | Title | Date | Technique | URL | Room wording | Story line |
|---|---|---|---|---|---|---|
| Paris Bordone | Portrait of a Young Woman | ca. 1543 - 1550 | Oil on canvas | https://www.museothyssen.org/en/collection/artists/bordone-paris/portrait-young-woman | "Room 6" / Level 2 / Permanent Collection | A Venetian beauty with roses and a monkey on a chain, read as a coded allusion to love, Venus and vice. |
| Pier Francesco Mola | Saint John the Baptist Preaching in the Desert | ca. 1650 - 1655 | Oil on canvas | EN https://www.museothyssen.org/en/collection/artists/mola-pier-francesco/saint-john-baptist-preaching-desert · ES https://www.museothyssen.org/coleccion/artistas/mola-pier-francesco/san-juan-bautista-predicando-desierto | EN "Room 6" / Level 2; ES "Sala 6" / Planta segunda (match) | A 17th-century Roman landscape with a preacher. Note that Room 6 now mixes centuries. |
| Giovanni Francesco Grimaldi ("il Bolognese") | Landscape with Tobias and the Archangel Raphael (ES *Paisaje con Tobías y el arcángel Rafael*) | ca. 1650 | Oil on canvas | ES https://www.museothyssen.org/coleccion/artistas/grimaldi-giovanni-francesco/paisaje-tobias-arcangel-rafael (EN page https://www.museothyssen.org/en/collection/artists/grimaldi-giovanni-francesco/landscape-tobias-and-archangel-raphael returned a JS check and was skipped) | ES "Sala 6" / Planta segunda | Tobias opens a magic fish whose organs will cure his bride Sara's curse and his father's blindness. |

Not on display:
- Titian, *Virgin and Child*
- Bronzino, *Cosimo in Armour*
- Ridolfo Ghirlandaio, *Capponi*
- Bronzino, *St Sebastian* and Sebastiano, *Carondelet* (on loan, known)

**Gap:** only 3 works confirmed. Check this room in person; it may hold more 17th-century Italian canvases.
**Best for the main route:** Bordone (striking, and a woman sitter with a story).

## Room 7. 16th Century. Italian Painting

| Artist | Title | Date | Technique | URL | Room wording | Story line |
|---|---|---|---|---|---|---|
| Vittore Carpaccio | Young Knight in a Landscape | ca. 1505 | Oil on canvas | https://www.museothyssen.org/en/collection/artists/carpaccio-vittore/young-knight-landscape | "Room 7" / Level 2 / Permanent Collection (known) | One of the earliest full-length portraits in Western painting, full of hidden animal and plant symbols. |
| Titian | Portrait of Doge Francesco Venier | ca. 1554 - 1556 | Oil on canvas | https://www.museothyssen.org/en/collection/artists/titian/portrait-doge-francesco-venier | "Room 7" / Level 2 / Permanent Collection (inv. 405) | Titian's own replica of the official portrait. The original was lost in the 1577 Doge's Palace fire, so this is the surviving image. |
| Gentile Bellini | The Annunciation | ca. 1475 | Mixed media on panel | https://www.museothyssen.org/en/collection/artists/bellini-gentile/annunciation | "Room 7" / Level 2 / Permanent Collection (inv. 38) | Gentile or his brother Giovanni? It has been given to Gentile since 1937. |
| Palma Vecchio | The Virgin and Child with Saints and a Donor | ca. 1518 - 1520 | Oil on panel transferred to canvas | https://www.museothyssen.org/en/collection/artists/palma-vecchio/virgin-and-child-saints-and-donor | "Room 7" / Level 2 / Permanent Collection (inv. 309) | It passed from the Venetian Senate to Napoleon's stepson Eugène de Beauharnais. (Palma's *La Bella* is in The Hague.) |
| Veronese (Paolo Caliari) | Portrait of a Woman with a Dog | ca. 1560 - 1570 | Oil on canvas | https://www.museothyssen.org/en/collection/artists/veronese/portrait-woman-dog | "Room 7" / Level 2 / Permanent Collection (inv. 423) | A noblewoman and her lapdog. Veronese, or his brother or son? |
| Domenico Beccafumi | The Virgin and Child with the Infant Saint John and Saint Jerome | ca. 1523 - 1525 | Oil on panel | https://www.museothyssen.org/en/collection/artists/beccafumi-domenico/virgin-and-child-infant-saint-john-and-saint-jerome | "Room 7" / Level 2 / Permanent Collection (inv. 33) | A Sienese Mannerist tondo, little known until 1983. |
| Bartolomeo Veneto | Portrait of a Man | ca. 1525 - 1530 | Oil on panel | https://www.museothyssen.org/en/collection/artists/veneto-bartolomeo/portrait-man | "Room 7" / Level 2 / Permanent Collection | – |

Not on display: Giovanni Bellini, *Nunc Dimittis*; Titian, *Antonio Anselmi*; Correggio; Dosso.

**Best for the main route:** Carpaccio + Titian's *Doge Venier*.

## Rooms 8–9. 15th and 16th Centuries. German Painting

| Room | Artist | Title | Date | Technique | URL | Room wording | Story line |
|---|---|---|---|---|---|---|---|
| 8 | Lucas Cranach the Elder | The Virgin and Child with a Bunch of Grapes | ca. 1509-1510 | Oil on panel | https://www.museothyssen.org/en/collection/artists/cranach-lucas-elder/virgin-and-child-bunch-grapes | "Room 8" / Level 2 / Permanent Collection (inv. 114) | Early Cranach. The grapes foretell the Eucharistic wine. |
| 8 | Hans Burgkmair the Elder | Christ's body carried to the Tomb | ca. 1520 | Oil on panel | https://www.museothyssen.org/en/collection/artists/burgkmair-hans/christs-body-carried-tomb | "Room 8" / Level 2 (inv. 71) | Augsburg painting. The Peutinger arms on the tomb were once thought to link it to a lost altarpiece. |
| 8 | Bartholomäus Bruyn the Elder | The Nativity | ca. 1520 | Oil on panel | https://www.museothyssen.org/en/collection/artists/bruyn-bartholomaus/nativity | "Room 8" / Level 2 / Permanent Collection | The Nativity set among Renaissance ruins, as in Cologne painting of the time. |
| 9 | Lucas Cranach the Elder | Portrait of the Emperor Charles V | 1533 | Oil on panel | https://www.museothyssen.org/en/collection/artists/cranach-lucas-elder/portrait-emperor-charles-v | "Room 9" / Level 2 / Permanent Collection (inv. 112) | **The Madrid hook:** Spain's emperor, painted by Luther's friend and court painter to Charles V's Protestant rivals. |
| 9 | Hans Holbein the Elder | Portrait of a Woman | ca. 1518 - 1520 | Oil on panel | https://www.museothyssen.org/en/collection/artists/holbein-hans-elder/portrait-woman | "Room 9" / Level 2 / Permanent Collection (inv. 189) | It was once wrongly identified, with its pair, as **Martin Luther and Katharina von Bora**. The father of the Henry VIII painter. |
| 9 | Albrecht Altdorfer | Portrait of a young Woman | ca. 1522 | Oil on panel | https://www.museothyssen.org/en/collection/artists/altdorfer-albrecht/portrait-young-woman | "Room 9" / Level 2 / Permanent Collection | A mystery sitter. The page says the theories that she is Altdorfer's wife or Barbara Blomberg (Charles V's lover, mother of Don John of Austria) were rejected for lack of evidence. |
| 9 | Hans Baldung Grien | Portrait of a Lady | 1530 (?) | Oil on panel | https://www.museothyssen.org/en/collection/artists/baldung-grien-hans/portrait-lady | "Room 9" / Level 2 / Permanent Collection | It was catalogued in 1934 as a princess of Baden-Durlach. |

Not on display:
- Dürer, *Jesus Among the Doctors*: on loan to The Hague (known).
- Cranach, *Nymph at the Fountain*: not exhibited (known).
- Cranach, *St Anne with Duchess Barbara of Saxony* wing: "Not exhibited".
- Baldung, *Adam and Eve*: "Not exhibited".
- Master of the Thyssen Adoration: "Not on display".
- Wolf Huber: "Not on display".
- Holbein the Younger is in Room 5.

**Best for the main route:** Cranach's *Charles V* (Room 9) + Holbein the Elder's *Woman* ("not Luther's wife"). In Room 8, Cranach's *Virgin with Grapes* if time allows.

## Room 10. 16th Century. Netherlandish Painting

| Artist | Title | Date | Technique | URL | Room wording | Story line |
|---|---|---|---|---|---|---|
| Joachim Patinir | Landscape with the Rest on the Flight into Egypt | ca. 1518 - 1524 | Oil on panel | https://www.museothyssen.org/en/collection/artists/patinir-joachim/landscape-rest-flight-egypt | "Room 10" / Level 2 / Permanent Collection (inv. 314) | The inventor of the "world landscape", where the holy family shrinks inside a panorama. Ties in well with the Prado's Patinirs. |
| Jan Wellens de Cock | The Temptation of Saint Anthony | ca. 1520 | Oil on panel | https://www.museothyssen.org/en/collection/artists/cock-jan-wellens/temptation-saint-anthony | "Room 10" / Level 2 (inv. 93) | Bosch-style fantasy: the hermit prays while the Devil sends naked women through a weird landscape. |
| Jan Mostaert | The Expulsion of Hagar | ca. 1520 - 1525 | Oil on panel | https://www.museothyssen.org/en/collection/artists/mostaert-jan/expulsion-hagar | "Room 10" / Level 2 / Permanent Collection (inv. 294) | Abraham sends Hagar and Ishmael into the desert at Sarah's request. A story about women. |
| Jan Provost | Portrait of a Female Donor | ca. 1505 | Oil on panel | https://www.museothyssen.org/en/collection/artists/provost-jan/portrait-female-donor | "Room 10" / Level 2 / Permanent Collection (inv. 328) | Half of a lost triptych. Her husband's portrait is in Philadelphia. |

Not on display: Gossaert, *Adam and Eve* (https://www.museothyssen.org/en/collection/artists/gossaert-jan/adam-and-eve), "Not exhibited".

**Best for the main route:** Patinir + Jan de Cock's *Temptation*.

## Room 11. Tiziano, Tintoretto, Bassano and El Greco

| Artist | Title | Date | Technique | URL | Room wording | Story line |
|---|---|---|---|---|---|---|
| Titian | The Penitent Saint Jerome | ca. 1575 | Oil on canvas | https://www.museothyssen.org/en/collection/artists/titian/penitent-saint-jerome | "Room 11" / Level 2 / Permanent Collection (known) | Late Titian, painted almost with the fingers. |
| El Greco | The Annunciation | ca. 1576 | – | https://www.museothyssen.org/en/collection/artists/greco-domenikos-theotokopoulos/annunciation-0 | "Room 11" (known) | The small early one, painted before Toledo. The large c. 1596–1600 one is in The Hague. |
| Tintoretto | The Meeting of Tamar and Judah | ca. 1555 - 1559 | Oil on canvas | https://www.museothyssen.org/en/collection/artists/tintoretto/meeting-tamar-and-judah | "Room 11" / Level 2 (inv. 401) | A widow outwits her father-in-law, and he is forced to admit "she is more righteous than I". A strong woman-centred story. |
| Tintoretto | The Annunciation to Manoah's Wife | ca. 1555 - 1559 | Oil on canvas | https://www.museothyssen.org/en/collection/artists/tintoretto/annunciation-manoahs-wife | "Room 11" / Level 2 / Permanent Collection (inv. 402) | The angel announces Samson's birth to a woman thought barren. A pendant to *Tamar*. |

Notes:
- Tintoretto, *Paradise* (https://www.museothyssen.org/en/collection/artists/tintoretto/paradise) is labelled **"Central hall"**, not Room 11. It is the sketch for the Doge's Palace competition after the 1577 fire.
- Not on display: Bassano, *Parable of the Sower*; Veronese, *Annunciation*; Tintoretto, *Senator* (c. 1580).
- No Bassano was confirmed in the room despite the title. Check in person.

**Best for the main route:** El Greco (the Toledo connection) + Tintoretto's *Tamar*.

## Room 12. 17th Century. Caravaggio and Baroque Painting

| Artist | Title | Date | Technique | URL | Room wording | Story line |
|---|---|---|---|---|---|---|
| Caravaggio | Saint Catherine of Alexandria | ca. 1598-99 | Oil on canvas | https://www.museothyssen.org/en/collection/artists/caravaggio-michelangelo-merisi/saint-catherine-alexandria | "Room 12" / Level 2 / Permanent Collection (known) | A Roman courtesan (traditionally Fillide Melandroni) posed as a royal martyr, beside her spiked wheel. |
| Jose de Ribera | The Pietà | 1633 | Oil on canvas | https://www.museothyssen.org/en/collection/artists/ribera-jose/pieta | "Room 12" / Level 2 / Permanent Collection (inv. 336) | The Valencian in Naples, moving from tenebrist darkness toward colour. |
| Jose de Ribera | Saint Jerome in penitence | 1634 | Oil on canvas | https://www.museothyssen.org/en/collection/artists/ribera-jose/saint-jerome-penitence | "Room 12" / Level 2 / Permanent Collection (inv. 335) | Old, wrinkled skin painted like sculpture. Compare it with Titian's Jerome in Room 11. |
| Orazio Gentileschi (workshop of) | Lot and His Daughters | ca. 1621 - 1623 | Oil on canvas | https://www.museothyssen.org/en/collection/artists/gentileschi-orazio-workshop/lot-and-his-daughters | "Room 12" / Level 2 / Permanent Collection (inv. 155) | The daughters' drastic plan to continue the family line. It also opens a door to Orazio's daughter Artemisia (not in the collection). |
| Tommaso Salini | Young Peasant with a Flask | ca. 1610 | Oil on canvas | https://www.museothyssen.org/en/collection/artists/salini-tommaso/young-peasant-flask | "Room 12" / Level 2 / Permanent Collection (inv. 363) | A Caravaggesque street type. Salini was a Caravaggio rival. |

Notes:
- Bernini, *San Sebastian* (https://www.museothyssen.org/en/collection/artists/bernini-gian-lorenzo/san-sebastian): EN "Room de anoxia" / ES "Sala de anoxia". Not in the room.
- Ludovico Carracci: "Not exhibited".

**Best for the main route:** Caravaggio + Ribera's *Pietà*.

## Rooms 13–15. 17th Century. Italian, French and Spanish Painting

| Room | Artist | Title | Date | Technique | URL | Room wording | Story line |
|---|---|---|---|---|---|---|---|
| 13 | Claude Lorraine | Pastoral Landscape with the Flight into Egypt | 1663 | Oil on canvas | https://www.museothyssen.org/en/collection/artists/lorraine-claude/pastoral-landscape-flight-egypt | "Room 13" / Level 2 / Permanent Collection (inv. 226) | Painted for Prince Colonna in the year Claude fell gravely ill and made his will. |
| 13 | Simon Vouet | The Rape of Europa | ca. 1640 | Oil on canvas | https://www.museothyssen.org/en/collection/artists/vouet-simon/rape-europa (read via https://www.museothyssen.org/en/node/16785) | "Room 13" / Level 2 / Permanent Collection (inv. 428) | Jupiter as a white bull carries off the princess. Big, colourful, mythological. |
| 13 | Antoine Le Nain | The Young Musicians | ca. 1640 | Oil on copper | https://www.museothyssen.org/en/collection/artists/nain-antoine/young-musicians | "Room 13" / Level 2 / Permanent Collection (inv. 218) | Children's band on copper, by the eldest of the three Le Nain brothers. |
| 13 | Sébastien Bourdon | The Holy Family, with Saint Elisabeth and the Infant Saint John the Baptist | ca. 1653 - 1657 | Oil on canvas | https://www.museothyssen.org/en/collection/artists/bourdon-sebastien/holy-family-saint-elisabeth-and-infant-saint-john-baptist | "Room 13" / Level 2 / Permanent Collection (inv. 59) | – |
| 14 | Luca Giordano | The Judgement of Solomon | ca. 1665 | Oil on canvas (250.8 x 308 cm) | https://www.museothyssen.org/en/collection/artists/giordano-luca/judgement-solomon | "Room 14" / Level 2 / Permanent Collection (CTB.1991.8) | A huge canvas with the baby dangled by the ankle at its peak. Giordano later worked for Charles II in Madrid. |
| 14 | Mattia Preti | The Concert | 1630-35 | Oil on canvas | https://www.museothyssen.org/en/collection/artists/preti-mattia/concert | "Room 14" / Level 2 (inv. 327) | Caravaggesque musicians. The painting once hung at Daylesford, the Thyssens' English house. |
| 14 | Bernardo Cavallino | Lot and his Daughters | ca. 1640 - 1645 | Oil on panel | https://www.museothyssen.org/en/collection/artists/cavallino-bernardo/lot-and-his-daughters | "Room 14" / Level 2 / Permanent Collection (CTB.1994.3.1) | A Neapolitan version of the Room 12 subject. Good for comparison. |
| 15 | Francisco de Zurbarán | Christ on the Cross | ca. 1630 | Oil on canvas (214 x 143.5 cm) | https://www.museothyssen.org/en/collection/artists/zurbaran/christ-cross | "Room 15" / Level 2 / Permanent Collection (inv. 447) | A sculptural Christ against black, painted for Seville piety. It replaces the missing *Saint Casilda*. |
| 15 | Bartolomé Esteban Murillo | The Virgin and Child with Saint Rose of Viterbo | ca. 1670 | Oil on canvas | https://www.museothyssen.org/en/collection/artists/murillo-bartolome-esteban/virgin-and-child-saint-rose-viterbo | "Room 15" / Level 2 / Permanent Collection (inv. 296) | Late, soft Murillo, bought in Spain by an English lord. A female saint. |
| 15 | Carlo Maratta | Saint Mark the Evangelist | ca. 1655 - 1660 | Oil on canvas | https://www.museothyssen.org/en/collection/artists/maratta-carlo/saint-mark-evangelist | "Room 15" / Level 2 / Permanent Collection (inv. 278) | – |
| 15 | Carlo Dolci | The Infant Christ with a Floral Wreath | 1663 | Oil on canvas | https://www.museothyssen.org/en/collection/artists/dolci-carlo/infant-christ-floral-wreath | "Room 15" / Level 2 / Permanent Collection (inv. 129) | – |
| 15 | Bernardo Strozzi (workshop of) | Saint Cecilia | ca. 1625 - 1630 | Oil on canvas | https://www.museothyssen.org/en/collection/artists/strozzi-bernardo-workshop/saint-cecilia | "Room 15" / Level 2 / Permanent Collection | Patron saint of music. Downgraded from Strozzi to his workshop after technical study. |

Notes:
- Carpioni, *Bacchanal*: "Pasillo de la sala 10 a la 15" (corridor).
- Not on display:
  - Guercino, *Christ and the Woman of Samaria*
  - Velázquez, *Mariana of Austria*
  - Van der Hamen
  - Maffei
  - Romanelli
  - Zurbarán, *Saint Casilda* (known)
  - Rubens, *Venus and Cupid* (known)
- No Velázquez is on display.

**Best for the main route:** Room 13: Claude. Room 14: Giordano, *Judgement of Solomon*. Room 15: Zurbarán *Christ on the Cross* + Murillo.

## Rooms 16–18. 18th Century. Italian Painting

| Room | Artist | Title | Date | Technique | URL | Room wording | Story line |
|---|---|---|---|---|---|---|---|
| 16 | Giambattista Tiepolo | The Death of Sophonisba | ca. 1760 | Oil on canvas | https://www.museothyssen.org/en/collection/artists/tiepolo-giambattista/death-sophonisba | "Room 16" / Level 2 / Permanent Collection (inv. 396) | A Numidian queen drinks the poison her husband sends rather than be paraded in Rome. |
| 16 | Pietro Longhi | The Tickle | ca. 1755 | Oil on canvas | https://www.museothyssen.org/en/collection/artists/longhi-pietro/tickle (read via https://www.museothyssen.org/en/node/16836) | "Room 16" / Level 2 / Permanent Collection (inv. 224) | A young woman tickles a sleeping man with a feather. Venetian domestic comedy. |
| 16 | Giambattista Piazzetta | Portrait of a Young Woman in Profile with a Mask in her Right Hand | ca. 1720-1730 | Oil on canvas | https://www.museothyssen.org/en/collection/artists/piazzetta-giambattista/portrait-young-woman-profile-mask-her-right-hand | "Room 16" / Level 2 / Permanent Collection (CTB.1999.5) | A Carnival glance with a mask and the black *bautta*. She may be Rosa Muziolo, the painter's future wife. |
| 16 | Sebastiano Ricci | Bacchus and Ariadne | ca. 1691-1694 | Oil on canvas | https://www.museothyssen.org/en/collection/artists/ricci-sebastiano/bacchus-and-ariadne | "Room 16" / Level 2 / Permanent Collection (inv. 341) | Abandoned Ariadne, consoled by a god who turns her crown into stars. |
| 17 | Canaletto | The Grand Canal from San Vio, Venice | ca. 1723 - 1724 | Oil on canvas | https://www.museothyssen.org/en/collection/artists/canaletto/grand-canal-san-vio-venice | "Room 17" / Level 2 / Permanent Collection (known) | – |
| 17 | Canaletto | The Piazza San Marco in Venice | ca. 1723 - 1724 | Oil on canvas | https://www.museothyssen.org/en/collection/artists/canaletto/piazza-san-marco-venice | "Room 17" / Level 2 / Permanent Collection (inv. 75) | Early Canaletto, the pair to San Vio. It came from the Liechtenstein collection. |
| 17 | Giambattista Tiepolo | The Death of Hyacinthus | ca. 1752 - 1753 | Oil on canvas (287 x 232 cm) | https://www.museothyssen.org/en/collection/artists/tiepolo-giambattista/death-hyacinthus (read via https://www.museothyssen.org/en/node/16655) | "Room 17" / Level 2 (inv. 394) | Apollo's beloved is killed in a game. Tiepolo updates Ovid's discus to a tennis match, with racquet and balls on the ground, and the hyacinth blooms in the corner. |
| 17 | Bernardo Bellotto | Capriccio with a River and Bridge | ca. 1745 | Oil on canvas | https://www.museothyssen.org/en/collection/artists/bellotto-bernardo/capriccio-river-and-bridge (read via https://www.museothyssen.org/en/node/16644) | "Room 17" / Level 2 (inv. 40) | Canaletto's nephew invents a place from real buildings. |
| 17 | Francesco Guardi | The Grand Canal with Santa Lucia and Santa Maria di Nazareth (+ pendant *with San Simeone Piccolo and Santa Lucia*) | ca. 1780 | Oil on canvas | https://www.museothyssen.org/en/collection/artists/guardi-francesco/grand-canal-santa-lucia-and-santa-maria-di-nazareth · https://www.museothyssen.org/en/collection/artists/guardi-francesco/grand-canal-san-simeone-piccolo-and-santa-lucia | both "Room 17" / Level 2 (inv. 174, 175) | Canaletto's crisp light versus Guardi's flickering brush, with the same canal half a century apart. |
| 18 | Giambattista Piazzetta | Portrait of Giulia Lama | ca. 1715 - 1720 | Oil on canvas | https://www.museothyssen.org/en/collection/artists/piazzetta-giambattista/portrait-giulia-lama | "Room 18" / Level 2 / Permanent Collection (inv. 316) | **A woman painter (1681–1747)**, Piazzetta's pupil, portrayed by her master. The best way to bring a woman artist into the 18th-century rooms. |
| 18 | Andrea Locatelli | Landscape with Nymphs and Satyrs | s.f. | Oil on canvas | https://www.museothyssen.org/en/collection/artists/locatelli-andrea/landscape-nymphs-and-satyrs | "Room 18" / Level 2 / Permanent Collection (CTB.1999.24) | – |

Not on display:
- Canaletto, *Bucintoro* and *Warwick Castle*
- Giandomenico Tiepolo, *Money-changers*
- Tiepolo & workshop, *Christ on the route to Calvary*
- Pittoni (x2)
- Panini, *Pool at Bethesda*
- Piazzetta, *Self-Portrait* drawing and *Sacrifice of Isaac*
- Cestaro

**Gap:** Room 18 is thin (2 works confirmed).
**Best for the main route:** Room 17: Canaletto *San Vio* + Tiepolo *Hyacinthus*. Room 16 or 18: Piazzetta's *Giulia Lama*, or the masked woman.

## Rooms 19–21. Classical rooms: temporary exhibition "Mauritshuis ♥ Thyssen-Bornemisza: Masterpieces from The Hague", 9 Oct 2026 – 10 Jan 2027

Sources:
- https://www.museothyssen.org/en/exhibitions/thyssen-bornemisza-mauritshuis ("Classical Rooms", Level 2, Permanent Collection; 25 works, 1615–1705)
- https://www.museothyssen.org/en/exhibitions/thyssen-bornemisza-mauritshuis/room-texts

The pages divide the show into three sections but **do not map them to room numbers 19/20/21**:
1. Still lifes and genre: Bosschaert, Weenix, Coorte, van Anraadt, ter Borch, Dou, de Hooch, van Beyeren, Claesz, Maes, Steen.
2. Landscapes and figures: Saenredam, Both, Rembrandt, Hals, J. van Ruisdael, S. van Ruysdael, Honthorst, Avercamp.
3. Garden of Eden and *View of Delft*.

| Section | Artist | Title (as on room-texts page) | Date | Story line (from the museum's texts) |
|---|---|---|---|---|
| 3 | Johannes Vermeer | View of Delft | ca. 1660-1661 | "Apart from The Little Street, it is the only cityscape in his small body of work". It is shown "in a special space within the room". **The headline stop.** |
| 3 | Jan Brueghel the Elder and Peter Paul Rubens | The Garden of Eden with the Fall of Man | ca. 1615 | Two friends paint one picture: Brueghel's animals, Rubens's Adam and Eve. "A harmonious world where all species coexist". |
| 2 | Rembrandt van Rijn | Simeon's Song of Praise | 1631 | Young Rembrandt's tiny, glowing temple scene. Pair it with his Thyssen self-portrait in Room 27. |
| 2 | Pieter Saenredam | The Mariaplaats with the Mariakerck in Utrecht | 1659 | **The same church as the Thyssen Saenredam in Room 26**, so the guide can send listeners there. |
| 2 | Jacob van Ruisdael | View of Bentheim Castle | ca. 1652-1654 | The castle recurs in more than twelve of his paintings. |
| 2 | Gerrit van Honthorst | The Violin Player | 1626 | – |
| 1 | Pieter de Hooch | Figures in a Courtyard | ca. 1658-1660 | He refills her glass: a drinking game. |
| 1 | Jan Steen | As the Old Sing, So Pipe the Young | ca. 1668-1670 | Bad habits passed down the generations. |
| 1 | Gerrit Dou | The Young Mother | 1658 | "Dou made it his life's work to render every individual brushstroke invisible". |
| 1 | Ambrosius Bosschaert the Elder | Vase of Flowers in a Window | ca. 1618 | "Nothing lasts forever, not even these flowers". |

The main exhibition page also names images of Adriaen Coorte (*Still Life with Wild Strawberries*), Avercamp (*Ice Scene*) and Rembrandt (a "tronie" of a man with a feathered beret). The room-texts page does not describe them. No women artists are named.

**Thyssen work hung here:** Jacques Linard, *Chinese Bowl with Flowers*, 1640, oil on canvas. EN https://www.museothyssen.org/en/collection/artists/linard-jacques/chinese-bowl-flowers says "Room 21" / Level 2 / Permanent Collection. ES https://www.museothyssen.org/coleccion/artistas/linard-jacques/porcelana-china-flores says "Sala 21" / Planta segunda. They agree. This suggests a still-life section is in Room 21. Not confirmed.

**Best for the main route:** Vermeer, *View of Delft*, plus the Brueghel/Rubens *Garden of Eden*. Optionally, Saenredam as a set-up for Room 26.
**Time-limited:** record this as a removable track (ends 10 Jan 2027).

## Room 22. 18th Century. Italian Painting

| Artist | Title | Date | Technique | URL | Room wording | Story line |
|---|---|---|---|---|---|---|
| Giuseppe Maria Crespi | Portrait of Count Fulvio Grati | ca. 1720 - 1723 | Oil on canvas (228 x 153 cm) | https://www.museothyssen.org/en/collection/artists/crespi-giuseppe-maria/portrait-count-fulvio-grati | "Room 22" / Level 2 / Permanent Collection (inv. 116) | A full-length Bolognese nobleman, almost life-size. |
| Giuseppe Maria Crespi | Peasants with Donkeys | ca. 1709 | Oil on copper | https://www.museothyssen.org/en/collection/artists/crespi-giuseppe-maria/peasants-donkeys | "Room 22" / Level 2 / Permanent Collection (CTB.1994.1.2) | Tiny everyday-life coppers, inspired by the *Bamboccianti*, from Crespi's Florence visits. |
| Giuseppe Maria Crespi | Interior with a Family of Peasants | ca. 1709 | Oil on copper | https://www.museothyssen.org/en/collection/artists/crespi-giuseppe-maria/interior-family-peasants | "Room 22" / Level 2 / Permanent Collection (CTB.1994.1.1) | The pendant to the above: a grand count and humble peasants by the same hand. |

Not on display: Amorosi, *Girl Sewing*; Panini.

**Gap:** only Crespi confirmed.
**Best for the main route:** Crespi's *Count Fulvio Grati* with the peasant coppers (the contrast), or make this a pass-through.

## Room 23. 17th Century. Dutch Painting. Landscape

| Artist | Title | Date | Technique | URL | Room wording | Story line |
|---|---|---|---|---|---|---|
| Frans Hals | Family Group in a Landscape | 1645 - 1648 | Oil on canvas | https://www.museothyssen.org/en/collection/artists/hals-frans/family-group-landscape | "Room 23" / Level 2 / Permanent Collection (known) | The 2021 press release says the first landscape room was built around "the great painting by Frans Hals". |
| Attributed to Frans Hals | Fisherman Playing the Violin | ca. 1630 | Oil on canvas | https://www.museothyssen.org/en/collection/artists/hals-attributed-frans/fisherman-playing-violin | "Room 23" / Level 2 (inv. 178) | Catalogued as a Hals until 1990, then downgraded to "attributed". |
| Jan Josephsz. van Goyen | Winter Landscape with Figures on Ice | 1643 | Oil on panel | https://www.museothyssen.org/en/collection/artists/goyen-jan-josephsz-van/winter-landscape-figures-ice | "Room 23" / Level 2 / Permanent Collection (inv. 167) | The frozen Oude Maas at Dordrecht: skating, fishing and hauling goods across the ice. |

**Best for the main route:** Hals, *Family Group* + van Goyen's ice scene.

## Room 24. 18th Century. French and English Painting

| Artist | Title | Date | Technique | URL | Room wording | Story line |
|---|---|---|---|---|---|---|
| Jean-Honoré Fragonard | The See-Saw | ca. 1750 - 1752 | Oil on canvas | https://www.museothyssen.org/en/collection/artists/fragonard-jean-honore/see-saw | "Room 24" / Level 2 / Permanent Collection (known) | Rococo flirtation in motion. |
| Thomas Gainsborough | Portrait of Sarah Buxton | ca. 1776 - 1777 | – | https://www.museothyssen.org/en/collection/artists/gainsborough-thomas/portrait-sarah-buxton | "Room 24" / Level 2 / Permanent Collection (known) | – |
| Jean Antoine Watteau | Pierrot Content | ca. 1712 | Oil on canvas | https://www.museothyssen.org/en/collection/artists/watteau-jean-antoine/pierrot-content | "Room 24" / Level 2 / Permanent Collection (inv. 432) | A fête galante with commedia dell'arte figures. The canvas was later cut down. |
| François Boucher | La Toilette | 1742 | Oil on canvas | https://www.museothyssen.org/en/collection/artists/boucher-francois/toilette | "Room 24" / Level 2 / Permanent Collection (inv. 58) | A Parisian woman's morning in her boudoir, commissioned by Sweden's ambassador Count Tessin. |
| **Louise Moillon** | Still-Life with Fruit | ca. 1637 | Oil on canvas | https://www.museothyssen.org/en/collection/artists/moillon-louise/still-life-fruit | "Room 24" / Level 2 / Permanent Collection | **The only woman artist confirmed on Level 2.** A Paris still-life specialist; the page calls this a key work in how her style changed between 1629 and 1637. (A 17th-century work hung in the 18th-century room.) |

Other works on the Fragonard page's list, not checked: Lancret, *The Swing*; Fragonard, *Portrait of a Young Lady*.

**Best for the main route:** Fragonard + Louise Moillon. Alternative: Boucher *La Toilette* for the women's-world angle.

## Room 25. 17th Century. Dutch Painting. Scenes of Daily Life and Interiors

| Artist | Title | Date | Technique | URL | Room wording | Story line |
|---|---|---|---|---|---|---|
| Nicolaes Maes | The Naughty Drummer | ca. 1655 | Oil on canvas | https://www.museothyssen.org/en/collection/artists/maes-nicolaes/naughty-drummer | "Room 25" / Level 2 / Permanent Collection (inv. 241) | Mum scolds the drummer boy before he wakes the baby. It has been read as a family scene, an allegory and a political image. |
| Jan Havicksz. Steen | Self-Portrait playing the Lute | ca. 1663 - 1665 | Oil on panel | https://www.museothyssen.org/en/collection/artists/steen-jan-havicksz/self-portrait-playing-lute | "Room 25" / Level 2 / Permanent Collection (inv. 373) | The comic genius casts himself as a merry musician. It came via the dealer Goudstikker. Steen also appears in the Mauritshuis show. |
| Pieter Hendricksz. de Hooch | Interior of the Council Chamber of Amsterdam Town Hall | ca. 1663 - 1665 | Oil on canvas | https://www.museothyssen.org/en/collection/artists/hooch-pieter-hendricksz/interior-council-chamber-amsterdam-town-hall | "Room 25" / Level 2 / Permanent Collection (inv. 196) | De Hooch leaves the Delft courtyard for civic grandeur. Compare it with his *Courtyard* from the Mauritshuis. |
| Willem Kalf | Still Life with a Chinese Bowl, Nautilus Cup and Other Objects | 1662 | Oil on canvas | https://www.museothyssen.org/en/collection/artists/kalf-willem/still-life-chinese-bowl-nautilus-cup-and-other-objects | "Room 25" / Level 2 / Permanent Collection (inv. 203) | Global luxury of the Dutch Golden Age: Chinese porcelain and a nautilus shell. It once belonged to Count Orlov-Denisov. |
| Emanuel de Witte | Interior of the Nieuwe Kerk, Amsterdam, during a Service | ca. 1658 | Oil on canvas | https://www.museothyssen.org/en/collection/artists/witte-emanuel/interior-nieuwe-kerk-amsterdam-during-service | "Room 25" / Level 2 / Permanent Collection (CTB.1995.25) | A crowded sermon with children, old people and dogs, all in church. |

**Best for the main route:** Maes, *Naughty Drummer* + Kalf. Alternative: Steen, a self-portrait as entertainer.

## Room 26. 17th Century. Dutch Painting. Landscape

| Artist | Title | Date | Technique | URL | Room wording | Story line |
|---|---|---|---|---|---|---|
| Pieter Jansz. Saenredam | The West Façade of the Church of Saint Mary in Utrecht | 1662 | Oil on panel | https://www.museothyssen.org/en/collection/artists/saenredam-pieter-jansz/west-facade-church-saint-mary-utrecht | "Room 26" / Level 2 / Permanent Collection (known) | He measured on site, then "improved" reality, removing two ruined structures. The Mauritshuis Saenredam next door shows the same church. |
| Aelbert Jacobsz. Cuyp | Landscape with a Sunset | ca. 1655 | Oil on panel | https://www.museothyssen.org/en/collection/artists/cuyp-aelbert-jacobsz/landscape-sunset | "Room 26" / Level 2 / Permanent Collection (inv. 117) | A cowherd heading home in golden light, the kind of scene that made Cuyp a favourite of British collectors. |
| Jan Lievens | Landscape with the Rest on the Flight into Egypt | ca. 1640 - 1645 | Oil on panel | https://www.museothyssen.org/en/collection/artists/lievens-jan/landscape-rest-flight-egypt | "Room 26" / Level 2 / Permanent Collection (inv. 222) | Rembrandt's studio-mate in Leiden. The painting was once given to Brouwer or to Rembrandt's circle. |
| Hercules Pietersz. Segers | Landscape with Armed Men | 1620s | Oil on canvas | https://www.museothyssen.org/en/collection/artists/segers-hercules-pietersz/landscape-armed-men | "Room 26" / Level 2 / Permanent Collection (inv. 370) | A rare Segers painting (Rembrandt collected his works), long mistaken for Salomon van Ruysdael. |
| Meindert Lubbertsz. Hobbema | Woodland Pond | ca. 1660 - 1663 | Oil on canvas | https://www.museothyssen.org/en/collection/artists/hobbema-meindert-lubbertsz/woodland-pond | "Room 26" / Level 2 / Permanent Collection (inv. 187) | – |
| Adriaen van de Velde | Pastoral Scene | 1663 | Oil on canvas | https://www.museothyssen.org/en/collection/artists/velde-adriaen-van/pastoral-scene | "Room 26" / Level 2 / Permanent Collection (inv. 417) | – |

Skipped: Jan Wijnants, *Castle in a Forest* (EN page returned a JS check).

**Best for the main route:** Saenredam (link it to the Mauritshuis twin) + Cuyp.

## Room 27. 17th Century. Dutch Painting. Portrait

| Artist | Title | Date | Technique | URL | Room wording | Story line |
|---|---|---|---|---|---|---|
| Rembrandt | Self-portrait wearing a hat and two Chains | ca. 1642 - 1643 | – | https://www.museothyssen.org/en/collection/artists/rembrandt-harmensz-van-rijn/self-portrait-wearing-hat-and-two-chains | "Room 27" / Level 2 / Permanent Collection (known) | Painted around the year his wife Saskia died (1642). Gold chains, a hat and a darkening mood. |
| Thomas Hendricksz. de Keyser | Portrait of Two Women and a Boy | 1632 | Oil on panel | https://www.museothyssen.org/en/collection/artists/keyser-thomas-hendricksz/portrait-two-women-and-boy | "Room 27" / Level 2 / Permanent Collection (inv. 209) | The older woman shows us a watch and the boy points at it. Is it the passing of time, or an absent father? |
| Govert Flinck | Portrait of a Man | 1640 | Oil on panel | https://www.museothyssen.org/en/collection/artists/flinck-govert/portrait-man | "Room 27" / Level 2 / Permanent Collection (inv. 143) | Rembrandt's pupil, painting in his master's manner. |
| Bartholomeus van der Helst | Portrait of a Man with Documents | ca. 1655 | Oil on canvas | https://www.museothyssen.org/en/collection/artists/helst-bartholomeus-van-der/portrait-man-documents | "Room 27" / Level 2 / Permanent Collection (inv. 184) | The fashionable alternative to Rembrandt in 1650s Amsterdam. |

**Best for the main route:** Rembrandt + de Keyser's *Two Women and a Boy*.

## Room 28. 17th Century. Dutch Painting. Landscape

| Artist | Title | Date | Technique | URL | Room wording | Story line |
|---|---|---|---|---|---|---|
| Jacob Isaacksz. van Ruisdael | View of Naarden | 1647 | Oil on panel | https://www.museothyssen.org/en/collection/artists/ruisdael-jacob-isaacksz-van/view-naarden | "Room 28" / Level 2 / Permanent Collection (known) | An early masterpiece by the 18-year-old Ruisdael: a low horizon with a huge sky. |
| Jacob Isaacksz. van Ruisdael | Stormy Sea with Sailing Vessels | ca. 1668 | Oil on canvas | https://www.museothyssen.org/en/collection/artists/ruisdael-jacob-isaacksz-van/stormy-sea-sailing-vessels | "Room 28" / Level 2 / Permanent Collection (inv. 359) | Three-quarters sky. Turner may have seen it in London and answered with *Port Ruysdael*. |
| Jacob Isaacksz. van Ruisdael | Road trough Grain Fields near the Zuider Zee | ca. 1660 - 1662 | Oil on canvas | https://www.museothyssen.org/en/collection/artists/ruisdael-jacob-isaacksz-van/road-trough-grain-fields-near-zuider-zee | "Room 28" / Level 2 / Permanent Collection (inv. 357) | Ripe wheat, walkers and the Zuider Zee beyond, perhaps near Naarden again. (The official title has the typo "trough".) |

**Best for the main route:** *View of Naarden* + *Stormy Sea*. Ruisdael's whole career in one room, ending with the marine painting the 2021 press release promised for this room.

## Room 29. 19th Century. European Painting. Goya and Romanticism

| Artist | Title | Date | Technique | URL | Room wording | Story line |
|---|---|---|---|---|---|---|
| Caspar David Friedrich | Easter Morning | ca. 1828 - 1835 | Oil on canvas | https://www.museothyssen.org/en/collection/artists/friedrich-caspar-david/easter-morning | "Room 29" / Level 2 / Permanent Collection (known) | Late Friedrich, from just before the 1835 stroke that ended his oil painting. |
| Eugène Delacroix | Arab Rider | ca. 1854 | Oil on panel | https://www.museothyssen.org/en/collection/artists/delacroix-eugene/arab-rider | "Room 29" / Level 2 / Permanent Collection (inv. 126) | A memory of his 1832 Morocco trip, twenty years later: a rider by a fire and a restless black horse. |
| Eugène Delacroix | The Duke of Orleans showing his Lover | ca. 1825 - 1826 | Oil on canvas | https://www.museothyssen.org/en/collection/artists/delacroix-eugene/duke-orleans-showing-his-lover | "Room 29" / Level 2 / Permanent Collection (inv. 127) | A scandalous medieval tale: the duke shows his naked, face-hidden mistress to her own husband, who does not recognise her. |
| Christian E. B. Morgenstern | Oaks beside the Water | 1832 | Oil on canvas | https://www.museothyssen.org/en/collection/artists/morgenstern-christian-e-b/oaks-beside-water | "Room 29" / Level 2 / Permanent Collection (inv. 292) | – |
| Ferdinand Georg Waldmüller | Bad Ischl | 1833 (image caption: 1836) | Oil on canvas | https://www.museothyssen.org/en/collection/artists/waldmuller-ferdinand-georg/bad-ischl | "Room 29" / Level 2 / Permanent Collection (inv. 429) | Biedermeier Austria: the spa town below blue-violet mountains. The page's date (1833) and image caption (1836) disagree. |

No Goya is on display:
- *Portrait of Asensio Julià* (https://www.museothyssen.org/en/collection/artists/goya-francisco/portrait-asensio-julia): "Not exhibited".
- *Portrait of Ferdinand VII* (https://www.museothyssen.org/en/collection/artists/goya-francisco/portrait-ferdinand-vii): "Not exhibited".
- *El tío Paquete*: temporary exhibition / ES "No expuesta" (known).
- Friedrich, *Fishing Boat by the Baltic Sea*, is in Room A, Level 0, not here.

**Best for the main route:** Friedrich + Delacroix, *Arab Rider*. Say plainly that the room's Goyas are off display this season.

---

## Pages with no room or an unusual label (Level 2 candidates)

| Work | URL | Label |
|---|---|---|
| Bernini, *San Sebastian* (marble, private loan) | https://www.museothyssen.org/en/collection/artists/bernini-gian-lorenzo/san-sebastian · ES https://www.museothyssen.org/coleccion/artistas/bernini-gian-lorenzo/san-sebastian | EN "Room de anoxia" / ES "Sala de anoxia" (no room number) |
| Tintoretto, *Paradise* | https://www.museothyssen.org/en/collection/artists/tintoretto/paradise | "Central hall" |
| Carpioni, *Bacchanal* | https://www.museothyssen.org/en/collection/artists/carpioni-giulio/bacchanal | "Pasillo de la sala 10 a la 15", no level given |
| Lotto, *Self-Portrait* | https://www.museothyssen.org/en/node/17028 | "Room 5"; the page gives no date and the canonical slug was not confirmed |
| Grimaldi, *Landscape with Tobias* | EN page blocked by JS check | ES "Sala 6" only |

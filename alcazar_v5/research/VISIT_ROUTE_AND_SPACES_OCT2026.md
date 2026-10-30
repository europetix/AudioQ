# Real Alcázar de Sevilla: visit route, spaces, objects and notices (as of 30 Oct 2026)

For the Yo Tours v5 rebuild of the 20-track guide (old/001–020; overview source/old.txt 1–190).
Main job: put each track in the right place, and leave out or flag anything that is closed or has moved.

## Method

- Tools used: WebFetch and WebSearch only. I fetched one page at a time, never in bursts. I did not use curl or a browser, and I hit no CAPTCHA.
- Grades:
  - **OFF**: an official page I read directly. Official sites are alcazarsevilla.org, its PDFs, and the Patronato's official ticketing site alcazardesevilla.infoticketing.com.
  - **SEC**: a secondary source I read directly (press, blogs, image agencies).
  - **SNIP**: search snippet only.
- Pages I could not read (permission prompt not answered). These were **not** used. Re-try them by hand if possible:
  - MuseumMate official audioguide: https://app.museummate.net/museums/NzctUEFUUk9OQVRPIFJFQUwgQUxDQVpBUiBERSBTRVZJTExB/ . It probably holds the Patronato's own stop order, so it is the best remaining source for the official route.
  - Ticketing home page: https://alcazardesevilla.infoticketing.com/es (the Cuarto Real Alto ticket page on the same site *was* read).
  - es.wikipedia "Real Alcázar de Sevilla"; Wikimedia Commons tapestry files.
  - andaluciainforma.es article on the Patio de las Doncellas restoration (https://andaluciainforma.es/actualidad/patio-de-las-doncellas-rehabilitacion-alcazar-sevilla/).
  - planomato.com pages: site error.
- No Wikipedia claim is used anywhere below.
- Prices and hours are noted only as context. They must **not** go into scripts.

## 1. The official visit

### Entrance: Puerta del León (Plaza del Triunfo)
- **OFF.** The Cuarto Real Alto ticket page says entry is through the Lion Gate (Puerta del León), from 60 min before to 30 min after the ticket time, "to allow for security checks". Reduced-rate proof is shown "at the Lion Gate".
  - https://alcazardesevilla.infoticketing.com/en/entradas/visita-real-alcazar-cuarto-real-alto
- **OFF.** The Patronato's teaching itineraries start "Puerta del León". Note: large school groups enter via the Jardines de Murillo instead.
  - https://alcazarsevilla.org/wp-content/uploads/2024/11/02-Itinerarios-y-Actividades.pdf
- **SEC.** El Español, 17 Jun 2026: the security controls, scanners and shop are "situados junto a la Puerta del León". A separate entrance for people born in or living in Seville is planned through Casas 7 y 8 of the Patio de Banderas. No opening date has been given. It is not built yet.
  - https://www.elespanol.com/sevilla/20260617/real-alcazar-contara-entrada-exclusiva-sevillanos-independiente-acceso-general/1003744290179_0.html
- **SEC.** Civitatis gives the meeting point as "Puerta del León (puerta principal)". European Traveler (12 Feb 2025) also says entrance through the Lion Gate.
- **OFF.** The ticket office (taquilla, card payment only, opens 09:00) is in the **Patio de Banderas**, not at the gate (https://alcazarsevilla.org/prepara-la-visita/). Visitors who arrive without a ticket buy it in the Patio de Banderas and then walk round to the Puerta del León.
- **OFF, 16 Jul 2026.** Five weeks of conservation work on the gates between Plaza del Triunfo and Patio de Banderas. It restricted **vehicles only** (Mon–Fri 08:00–15:00) and did not change pedestrian access. It should be over by now.
  - https://alcazarsevilla.org/noticia/trabajos-de-conservacion-en-las-puertas-de-acceso-entre-plaza-del-triunfo-y-patio-de-banderas/

### Exit: Patio de Banderas (via the Apeadero)
- **SEC.** European Traveler, 12 Feb 2025: you may stay until closing "as long as visitors don't exit the entire complex (at Patio de Banderas)". There is no re-admission.
- **SEC, undated.** omviajesyrelatos: "no se entra por el Patio de Banderas, ya que ésta es la salida".
- **OFF.** The official triptych places the words ENTRADA / SALIDA next to "PATIO DE BANDERAS". This comes from text extraction without coordinates, so their exact positions are not confirmed.
- **CHECK.** The Apeadero (triptych no. 53) is the passage between the Patio de la Montería area and the Patio de Banderas. The Puerta del Apeadero opens into the Patio de Banderas (OFF, prepara-la-visita). No source read states in so many words that "visitors exit through the Apeadero". That is standard practice, but it is unverified here.
- **CHECK, geography.** Old track 20 calls the Patio de Banderas "the small plaza on the south side of the complex". Every source puts it beside the Plaza del Triunfo, next to the Puerta del León, at the north/north-east front, and the gardens lie to the south (OFF triptych text). Re-word it, for example: "the square just east of where you came in".

### Official route / order
- **The Patronato publishes no compulsory route.**
  - "Prepara la visita" has no itinerary (OFF).
  - The triptych has no route line (OFF).
  - European Traveler (SEC, Feb 2025): "generally no one-way restrictions", and rooms can be revisited.
- **The de facto official order is the triptych numbering (OFF).** It runs from the entrance inward:
  - Patio del León → Sala de la Justicia → Patio del Yeso → Patio de la Montería → façade of Pedro I's palace → Cuarto del Almirante → chapel of the Virgen de los Navegantes → Pedro I's palace (Doncellas, Embajadores, Muñecas) → stair to the Cuarto Real Alto.
  - Then the Gothic Palace (Patio del Crucero, Tapices, Bóvedas, Baños).
  - Then the gardens, from the Jardín del Príncipe to the Apeadero (no. 53, last number = the way out).
- **SEC.** The self-guided route at thecreativeadventurer.com follows the same order: León → Yeso/Justicia → Montería → Admiral's Quarters (Virgin) → Pedro I façade → Doncellas → Embajadores → Infantes → Felipe II → Muñecas → Prince's rooms → gardens. It has the Baths reached from the Jardín de la Danza.
- **OFF.** The audioguide is MuseumMate, opened by QR code or link. Its stop order could not be read (see Method).

### Visitor map / plano (official)
- **OFF, PDF.** https://alcazarsevilla.org/wp-content/uploads/2024/11/triptico_alcazar_sevilla.pdf
  - Linked from "Prepara la visita", which says to print it.
  - Uploaded Nov 2024. Spanish only. Read through WebFetch as text; it was **not** downloaded into research/map/.
  - If the lead wants the image, fetch it by hand from that URL.
- No compass is shown. The text says the palaces face the gardens from the north, the gardens run south below the Almohad wall, the Vega-Inclán garden is to the east and the English Garden to the west.
- Other labels on the map: PATIO DE BANDERAS, CALLEJÓN DEL AGUA, JARDINES DE MURILLO, CUARTO REAL ALTO, TRASERA DEL CASERÍO DE LA CALLE SAN FERNANDO. Services shown: Tiendas, Cafetería, Aseos (their positions were not extracted).
- One of the map's place labels reads "Casa de la Contratación". Its text names the Italianate gardens "de las Damas, la Danza, Troya, Galera y Flores".
- Full numbered legend, as printed:

| No. | Palacios, estancias, patios | No. | Palacio Gótico | No. | Jardines | No. | Cuarto Real Alto (upper floor) |
|---|---|---|---|---|---|---|---|
| 1 | Patio del León | 31 | Patio del Crucero | 35 | Jardín del Príncipe | 20 | Dormitorio de Isabel la Católica |
| 2 | Sala de la Justicia | 32 | Salón de los Tapices y Capilla | 36 | Columna de Al-Mutamid | 21 | Capilla de Isabel la Católica |
| 3 | Patio del Yeso | 33 | Sala de las Bóvedas | 37 | Fuente de Troya | 22 | Antecomedor |
| 4 | Patio de la Montería | 34 | Baños Doña María de Padilla | 38 | Jardín de la Danza | 23 | Comedor de Gala |
| 5 | Fachada del Palacio del Rey Don Pedro | | | 39 | Estanque de Mercurio | 24 | Sala de Fumar |
| 6 | Cuarto del Almirante | | | 40 | Galería del Grutesco | 25 | Mirador de los Reyes Católicos |
| 7 | Capilla de la Virgen de los Navegantes | | | 41 | Fuente de la Fama | 26 | Dormitorio de Pedro I |
| 8 | Patio del Asistente | | | 42 | Fuente de Neptuno | 27 | Antesala de Audiencias |
| 9 | Patio de Levíes | | | 43 | Gruta de las Sultanas | 28 | Sala de Audiencias (upper floor, NOT the Contratación one) |
| 10 | Patio de las Doncellas | | | 44 | Pabellón de Carlos V | 29 | Sala de Billar |
| 11 | Alcoba Real | | | 45 | Cenador del León | 30 | Exposición Lozas y Azulejos de Triana. Colección Carranza |
| 12 | Salón de los Pasos Perdidos | | | 46 | Jardín Inglés | | |
| 13 | Salón del Techo de Carlos V | | | 47 | Jardín del Laberinto | | |
| 14 | Sala de los Infantes | | | 48 | Entrada Puerta de la Alcoba | | |
| 15 | Salón de los Embajadores | | | 49 | Jardín de los Poetas | | |
| 16 | Salón del Techo de Felipe II | | | 50 | Jardín Marqués de la Vega Inclán | | |
| 17 | Sala de los Reyes Católicos | | | 51 | Puerta de Marchena | | |
| 18 | Patio de las Muñecas | | | 52 | Jardín de la Alcubilla | | |
| 19 | Escalera al Cuarto Real Alto | | | 53 | Apeadero | | |

- Two quirks of the map:
  - The number 11 appears twice on the drawing.
  - The Gothic Palace numbers (31–34) are listed straight after 19.
- Important for scripts:
  - The **Salón del Techo de Carlos V (13) is inside Pedro I's palace**, not in the Gothic palace.
  - The Gothic palace is reached through the **Patio del Crucero (31)**. The legend lists no upstairs Gothic floor.
  - The European Traveler numbers "10 and 15" for Doncellas and Embajadores match this free map.

## 2. Spaces: status as of 30 Oct 2026

"Open" means part of the general ticket, with no closure notice found. The general ticket covers the ground floor of the palaces plus the gardens (OFF, price ordinance). The Patronato warns that spaces or gardens may close occasionally for maintenance or weather, with no refund (OFF). I found **no current long-term closure notice** for any space below.

| Space (ES / EN) | Where | Status (source, date) | What to see / notes |
|---|---|---|---|
| Puerta del León / Lion Gate | Façade on Plaza del Triunfo | Open, main visitor entrance (OFF ticketing, read Oct 2026) | Tile lion panel above the arch, outside |
| Patio del León / Lion Courtyard | Ground floor, first space | Open (OFF triptych no. 1) | Triple arch through to the Montería |
| Sala de la Justicia / Hall of Justice | Off the Patio del León | Open. **One-off closure** 09:30–11:00 on a Monday for a press conference (OFF notice, listed 24 Jul 2026). Not ongoing | Qubba from the time of Alfonso XI, with a floor fountain. Leads into the Patio del Yeso |
| Patio del Yeso | Next to the Sala de la Justicia | Open (OFF triptych no. 3) | Almohad portico with sebka work; pool. Archnet (SEC): Almohad residence, later reformed, restored 1918–20 and 1969–71 |
| Patio de la Montería / Hunting Courtyard | Ground floor, centre | Open (OFF no. 4). Used for events (opera Sept 2025) | Façade of Pedro I (no. 5). Cuarto del Almirante on the right (west) when facing the façade |
| Cuarto del Almirante / Casa de la Contratación | West side of the Montería | Open (OFF nos. 6–9; map label "Casa de la Contratación") | Sala de Audiencias = **"Capilla de la Virgen de los Navegantes" (no. 7)**. Also Patio del Asistente (8) and Patio de Levíes (9) |
| Palacio de Pedro I (Mudéjar palace) | Ground floor | Open | Nos. 10–18 |
| Patio de las Doncellas | Pedro I's palace | Open. **Restoration in phases** (SEC vivirediciones, 20–21 Jul 2026): alfarjes (flat wooden ceilings) done; yeserías and tiles "en las próximas fases". **CHECK for scaffolding** | Sunken garden and pool |
| Alcoba Real, Salón de los Pasos Perdidos, Salón del Techo de Carlos V, Sala de los Infantes | Pedro I's palace | Open (OFF nos. 11–14) | Salón del Techo de Carlos V (coffered ceiling) is here, off the Doncellas |
| Salón de los Embajadores / Hall of Ambassadors | Pedro I's palace | Open. Used for Christmas recitals (OFF news 27 Nov 2025) | 1427 dome |
| Salón del Techo de Felipe II; Sala de los Reyes Católicos | Pedro I's palace | Open (OFF nos. 16–17) | |
| Patio de las Muñecas / Dolls' Courtyard | Pedro I's palace | Open (OFF no. 18) | **New since Mar 2025:** a restored passage from the Patio de las Muñecas to the Jardín del Príncipe is open to the public, with LED lighting and newly revealed polychromy on the plaster (OFF news, 20 Mar 2025) |
| Cuarto del Príncipe / Prince's rooms | Off the Patio de las Muñecas | Open, as far as I can tell (SEC creativeadventurer). Not named in the triptych legend. **CHECK** | |
| Escalera al Cuarto Real Alto | Pedro I's palace (no. 19, listed after Muñecas) | Access point for the upper-floor ticket | |
| **Cuarto Real Alto** / Upper Royal Apartments | **Upper floor** of Pedro I's palace | **Separate ticket, timed** (OFF ordinance and ticketing). Must be "at the door of the Upper Royal Room (Second Floor) 15 minutes before"; late arrivals cannot visit. Audio-guided group with strict slots (SEC, European Traveler, Feb 2025) | Nos. 20–30, including Isabel la Católica's bedroom and chapel, the gala dining room, Pedro I's bedroom, the Sala de Audiencias, and the Carranza collection of Triana ceramics. Still a royal residence |
| Patio del Crucero | Gothic palace | Open (OFF no. 31) | Raised courtyard above the cisterns |
| Palacio Gótico: Salón de los Tapices y Capilla | Gothic palace, reached via the Crucero | Open (OFF no. 32). No 2025–26 notice found about the tapestries being moved | Tunis tapestries (see section 3) |
| Sala de las Bóvedas (Salón Gótico / Sala de Fiestas) | Gothic palace | Open (OFF no. 33). "Restoration of the historic sargas (painted cloths) of the Salón Gótico" listed among works done (SEC, Jul 2026) | Tiles; view into the garden through the glass gallery. Two naval tapestries made for the 1929 Expo (SEC andalucia.com) |
| Baños de Doña María de Padilla | Below the Patio del Crucero | Open (OFF no. 34). No closure found | Reached from the Jardín de la Danza at garden level (SEC creativeadventurer; OFF teaching itinerary pairs Mercurio–Danza–Baños) |
| Apeadero | Between the Montería area and the Patio de Banderas | Open (OFF no. 53). Façade restoration listed as done (SEC, Jul 2026) | The way out |
| Patio de Banderas | Outside the paid area | Public square with the ticket office | Archaeological crypt (separate visits). Future Seville-residents entrance (Casas 7 y 8) |
| Jardín del Príncipe | Gardens | Open (OFF no. 35). Now also reached by the Muñecas passage | |
| Columna de Al-Mutamid, Fuente de Troya, Jardín de la Danza | Gardens | Open (OFF nos. 36–38). Danza columns repaired in 2024 (OFF Expo-Mercurio PDF) | |
| Estanque de Mercurio / Mercury Pool | Gardens | **Open, restoration finished.** Works ran Nov 2022 to 2024 and the pool was refilled Feb 2024 (OFF Expo-Mercurio PDF). Reported "luce renovado" on 5 Mar 2025 (OFF news). Reopening reported Apr 2025 (SEC UPO) | Statue in the pool is a **new bronze replica** (see section 3) |
| Galería del Grutesco | Gardens, behind the Mercury pool | Open (OFF no. 40). Paintings restored Jul 2023 by MARVE (OFF PDF) | Paintings by Diego de Esquivel, finished 1629 (OFF PDF) |
| Fuente de la Fama, Fuente de Neptuno, Gruta de las Sultanas | Gardens | Open (OFF nos. 41–43) | |
| Jardín de las Damas, Jardín de las Flores, Jardín de la Galera | Gardens | Named in the triptych text (OFF); no number in the legend | |
| **Pabellón / Cenador de Carlos V** | Gardens | **Under / recently under full restoration (€1.6 m).** 1 Jul 2026: "Avanzan las obras… continúa con los trabajos" (SEC vivirediciones). 20 Jul 2026: listed as having "permitido recuperar" it (SEC). Completion and reopening are unconfirmed. **CHECK before scripting the interior** | Juan Hernández; Polido tiles, 16th century (OFF old page alcazarsevilla.org/?p=11014) |
| Cenador del León | Gardens | Open (OFF no. 45) | |
| Jardín Inglés, Jardín del Laberinto | Gardens | Open (OFF nos. 46–47) | |
| Puerta de la Alcoba (Cenador de la Alcoba) | Gardens | Open (OFF no. 48) | |
| Jardín de los Poetas, Jardín Marqués de la Vega Inclán, Puerta de Marchena, Jardín de la Alcubilla | Gardens | Open (OFF nos. 49–52). Vega-Inclán pergola restored Dec 2022 (SEC) | |
| Shops (Tiendas) | Near the Puerta del León (SEC) | **Closed temporarily**, no reopening date, because the operator is changing (OFF notice, modified 19 Oct 2026) | Do not send listeners to the shop |

## 3. Where specific objects are now

- **Virgen de los Mareantes / Navegantes (Alejo Fernández, 1531–36).**
  - Location: Sala de Audiencias of the Casa de la Contratación, in the Cuarto del Almirante. The official map calls this room "Capilla de la Virgen de los Navegantes" (no. 7) (OFF triptych).
  - Owned by Patrimonio Nacional, kept in the Alcázar by the Ayuntamiento (OFF Patrimonio Nacional PDF, 14 Feb 2017).
  - A 2017 agreement says any restoration would be done in situ in Seville, after which the work returns to "su emplazamiento habitual". The Patronato refused to send it to Madrid (SEC Sevilla Secreta, 9 Feb 2017).
  - No 2025–26 report of it being moved or loaned. On display = yes (SEC; no contrary evidence).
  - **Do not confuse** it with the Sala de Audiencias in the Cuarto Real Alto (no. 28).
  - Side panels: San Sebastián, Santiago, San Telmo, San Juan Evangelista. Predella with ships (SEC fotograrte).
- **Tunis tapestries.**
  - Location: Salón de los Tapices, Gothic palace (OFF no. 32; SEC andalucia.com, modified Apr 2026).
  - They are **18th-century copies**, woven at the royal tapestry factory by Francisco Ignacio Vandergoten (1704–1774) after Willem de Pannemaker's 16th-century originals, mid-18th century (SEC Bridgeman caption).
  - The originals belong to Patrimonio Nacional in Madrid. That is well known, but I found no source I could read that gives their current location. **CHECK.**
  - Old track 15 says "woven in the seventeen thirties" and "six enormous tapestries". Commons file names reach "Paño XII", which suggests more panels. **CHECK the date and count.**
  - Old track 15's "originals in storage" claim is unverified.
- **1364 façade inscriptions (Pedro I's palace).** Still in place on the façade in the Patio de la Montería (OFF no. 5).
  - SEC (Bluffton): a frieze with Gothic and Kufic inscriptions runs above the windows; the 1364 date relates to the portal and the start of building.
  - Exact wording and position were not verified from a source I could read. **CHECK** before quoting "era 1402" or "wa-lā ghālib illā Allāh".
- **Mercury bronze.**
  - **The figure now in the pool is a bronze replica.** It was made from a 3D scan (EinScan HX), printed in PLA, lost-wax cast by FundirMetal Amando, and gilded by electroplating. Some gilding was found on the original during cleaning (OFF EXPO-MERCURIO-FINAL.pdf, https://alcazarsevilla.org/wp-content/uploads/2025/01/EXPO-MERCURIO-FINAL.pdf).
  - Original: Diego de Pesquera (sculptor), Bartolomé Morel (founder), set up in **1576** (OFF PDF). Old track 17 says 1573. **Fix it.**
  - April 2024: the plan was to tender a restoration of the original and later "que el original sea expuesto nuevamente en el Real Alcázar" (SEC vivirediciones, 11 Apr 2024).
  - **Where the original is now: not found. CHECK.** Scripts should say "a faithful bronze copy now stands in the pool".
- **Ali al-Gumari / Patio del Yeso.**
  - No source read attributes the Patio del Yeso to Ali al-Gumari. Archnet (Almagro and Ramón-Laca) names no architect.
  - Al-Gumari is associated with the Giralda/minaret works, not this patio.
  - **CHECK, probably remove** old track 5's "designed by Ali al-Gumari".
- **Other audio-relevant items.**
  - Carranza collection of Triana ceramics: Cuarto Real Alto, no. 30 (OFF).
  - Columna de Al-Mutamid: gardens, no. 36 (OFF).
  - Restored Muñecas–Príncipe passage with newly revealed polychromy (OFF, Mar 2025).
  - Atlas Miller exhibition "Marco Polo y las maravillas…" was in the **Sala Cantarera** in 2025 (OFF news, 25 Apr 2025). End date not given. **CHECK; probably closed.**

## 4. Notices from alcazarsevilla.org/noticias (2025–2026) that affect visitors

All OFF. Dates come from the listing timestamps.

| Date | Notice | Effect on the visit |
|---|---|---|
| 19 Oct 2026 | Cierre temporal de las tiendas | Shops closed until a new operator takes over; no date given |
| 9 Oct 2026 | "El Fauno Encendido", 16–17 Oct | Evening garden show; over |
| 22 Sep 2026 | Bases Concursos de Carlos V | None |
| 24 Jul 2026 | Cierre temporal de la Sala de la Justicia por rueda de prensa | 09:30–11:00 on one Monday; over |
| 16 Jul 2026 | Conservation of the gates between Plaza del Triunfo and Patio de Banderas | 5 weeks; vehicles only; over |
| 12 Jun 2026 | Noches en los Jardines XXVII, 63 concerts Jun–Sep | Evenings only; over |
| 5 Jun 2026 | Guided visits to the Archivo Histórico | Special visits |
| 19 May 2026 | Visitas Nocturnas Teatralizadas (Boda Imperial) | Night visits, separate ticket |
| 4 Mar 2026 | Free registration for the congress "Las bodas de Carlos V en Sevilla" and the V Centenario theatrical visits | No closures stated |
| 2 Mar 2026 | Ayuntamiento presents the V Centenario programme (wedding of 11 Mar 1526) | Recreation, theatrical visits, congress through 2025–26. **No exhibition, moved works or closed rooms are named** |
| 28 Nov 2025 | Christmas programme | Events |
| 27 Nov 2025 | "Los Embajadores de la Navidad": recitals in the Salón de Embajadores | Events |
| 29 Sep 2025 | Naturaleza Encendida (3rd edition) | Evening show |
| 12 Sep 2025 | Gardens reopen after the preventive closure | Gardens were closed 4–12 Sep 2025 (dead ducks); now normal |
| 6 Aug 2025 | Opera "Il Califfo di Bagdad", Patio de la Montería, 26–27 Sep | Events |
| 25 Apr 2025 | Exhibition "Marco Polo y las maravillas en los manuscritos iluminados", Sala Cantarera | Temporary |
| 20 Mar 2025 | A historic passage is recovered (Muñecas → Jardín del Príncipe) | **New route segment open** |
| 5 Mar 2025 | Estanque de Mercurio "luce renovado" after restoration | **Open; statue is a replica** |
| Jan–Feb 2025 | Exhibition "Fotógrafos por la Libertad y la Paz" | Over |

- Non-news official page: https://alcazarsevilla.org/restauracion-estanque-mercurio/ (dossier credits; it also repeats the Muñecas passage item).
- Related V Centenario items from SEC sources:
  - vivirediciones, 12 Jan 2026: the exhibition "Los libros del Emperador" in the Alcázar and the University Library. No dates or room given. **CHECK whether it is on now.**
  - The Rubens / Carlos V cope / Inca gold show was at the **Espacio Santa Clara**, not the Alcázar (11 Mar–30 May 2026).
  - Free V Centenario routes for Seville residents covered the "Cenador de Carlos V y la antigua capilla" (vivirediciones, 1 Feb 2026).
- **Not found:** any 2026 exhibition inside the paid route that is running now, or any notice that the Tunis tapestries or the Virgin have been taken down.

## 5. Old-guide placement errors to fix

- **T15 (Gothic palace).** It says to "climb" a "staircase at the southeast corner of the Patio de las Doncellas" to the "Salones de Carlos V". Wrong on two counts:
  - The Salón del Techo de Carlos V (no. 13) is inside Pedro I's palace.
  - The Gothic palace (Tapices no. 32, Bóvedas no. 33) is reached through the Patio del Crucero (no. 31), with no climb to an upper floor.
- **T14 (Baths).** "Climb back to the upper level and head to the Salón del Techo de Felipe II". Felipe II (no. 16) is in Pedro's palace. The Baths are best taken from the gardens (Jardín de la Danza) or right after the Crucero.
- **T19 (Cuarto Real Alto).** It is placed in the gardens, but the visit is upstairs in Pedro I's palace. The stair (no. 19) is listed after the Patio de las Muñecas, and the visit has a strict time slot. Place the track at the stair, or make it an "anywhere" track.
- **T17.** Mercury 1573 → 1576. The statue in the pool is now a replica.
- **T20.** The Patio de Banderas is not on the south side.
- **T5.** Remove the al-Gumari attribution.
- **T6.** "To your left, the entrance to the Gothic Palace". andalucia.com (SEC) says the Gothic palace connects to the Montería by a porticoed gallery. Plausible. **CHECK.**

## CHECK list (unresolved)

1. MuseumMate official audioguide stop order. Page blocked; it is the best remaining source for the official order.
2. Pabellón / Cenador de Carlos V: works finished and interior open as of Oct 2026?
3. Patio de las Doncellas: current phase of plaster and tile works, and any scaffolding or closed galleries.
4. Where the original Mercury bronze is now (on display or not).
5. Tunis tapestries: number of panels in the Salón de los Tapices, weaving dates, and where the Pannemaker originals are now.
6. Exact wording and position of the 1364 façade inscriptions.
7. Exit through the Apeadero into the Patio de Banderas: confirm on site or from an official source.
8. Cuarto Real Alto: guided or audio-guided, duration, photo rule. Official page only says timed, 15 min early.
9. "Los libros del Emperador" exhibition: dates and room, and whether it is in the paid route now.
10. Is the Cuarto del Príncipe open as a named space? It is not in the triptych legend.
11. Shops reopening (affects any "gift shop" mention; best to avoid).

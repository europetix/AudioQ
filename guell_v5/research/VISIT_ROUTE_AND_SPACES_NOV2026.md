# Park Güell (Barcelona): visitor route, spaces and status (research as of 6 Nov 2026)

Prepared for: Yo Tours audio guide (guell_v5). Researcher: subagent, 6 Nov 2026.
Scope (USER_DECISIONS.md): ticketed Monumental Zone + nearest viaducts + Laundry Room Portico (free park); Gaudí House Museum from outside only; lengths 45 / 75 / 120 min including walking.
Method: WebSearch + WebFetch only, one page at a time per site. No curl, no browser, no CAPTCHA.

Grades:
- **OFF**: official operator page or file, fetched (parkguell.barcelona = Park Güell / BSM, Ajuntament de Barcelona).
- **OFF-AJ**: Ajuntament de Barcelona page other than parkguell.barcelona, fetched.
- **SEC**: secondary page, fetched (type in brackets).
- **SNIP**: search snippet only; a lead, not a fact.
- **INF**: my inference from the graded facts listed with it; verify on site.

Unless noted every page was fetched 6 Nov 2026.
Quote limits: the fetch tool returns only short excerpts, so quotes are short.

Status: complete for desk research (6 Nov 2026). The raw graded notes behind every row are in Appendix A. The fetch log is in Appendix B.

---

## 0. Key facts for the script (summary)

1. **The brief's "free park" premise is out of date.** OFF, `parkguell.barcelona/en/planning-your-visit/the-restricted-area`: *"The ticket provides access to the 12 hectares of the Park."* Access control of the whole 12 ha began on **29 June 2020** (OFF, Governance Report 2020: the regulated zone grew *"from 1.7 to 12 regulated hectares"*). The ticket therefore covers the viaducts, the Laundry Room Portico, the Casa del Guarda and the area around the Gaudí House Museum. The museum's interior needs a combined ticket. The old 2013 split ("Monumental Zone" paid, the rest free) survives only on reseller blogs. One example is headout.com (updated 2 May 2025), which lists the Portico and the viaducts under "Free Access Area". **That is exactly the kind of misplacement customers complained about. Do not repeat it.**
2. **There is an inner zone inside the ticketed park.** OFF, same page: the high-concentration spots *"are found within the section that has a second controlled access point, where visitors follow a one-way route"* and *"are likely to have to wait to visit them."* The listed spots are **Pl. Natura, the Hypostyle Room, the Laundry Room Portico, the Dragon Stairway and the Austria Gardens**. The official flyers (EN/ES/CA) carry the matching legend: *"Espais amb un segon punt de control i possible temps d'espera"* / *"Zona d'alta concentració"*. **So the Washerwoman Portico is inside the one-way inner section (OFF).**
3. **The Carrer d'Olot main gate (between the two pavilions) is an exit, not a visitor entrance.**
   - OFF, `why-are-the-access-points-regulated`, fetched 6 Nov 2026: there are 9 entries. Four are for neighbours and citizens only, four are for visitors and citizens, and there is *"one exit at carrer Olot"*.
   - OFF, Governance Report 2020: the shared visitor gates are *"Carmel, Olot, Sant Josep de la Muntanya and baixada de la Glòria"*, and there is *"Exit only: one gate on carrer d'Olot"*.
   - OFF, `node/268`: the Olot-side visitor entry is *"Carrer de Larrard (entry from the Carrer d'Olot / Carrer Marianao side lane)"*.
   - INF: visitors enter beside the main gate, through the Marianao/Larrard side lane, and then stand inside the gate on the entrance esplanade. **Our "start at the main gate" must therefore be "start just inside the main gate, between the two pavilions, with your back to Carrer d'Olot".** Verify on site (O1).
4. **Entry rules** (OFF, `access-regulations`):
   - *"Tickets allow entry into the Park for 30 minutes after the time-band reserved."*
   - *"Once the ticket has been validated at an access control point it will no longer be possible to leave and then re-enter."*
   - Casa del Guarda: the ticket *"does not guarantee entry"* because capacity is limited.
   - *"You may not use megaphones, speakers or any similar voice-amplification devices during tours inside the premises."* **The guide must be headphone-only.** Never tell listeners to play it aloud.
5. **Official names.** EN / ES / CA as the operator prints them, from the OFF flyers 2025–26 and the emblematic-features pages:

   | EN | ES | CA |
   |---|---|---|
   | Porter's Lodge | Casa del Guarda | Casa del Guarda |
   | Monumental Staircase / Dragon Stairway | Escalinata Monumental | Escalinata Monumental |
   | Hypostyle Room / Hypostyle Hall | Sala Hipóstila | Sala Hipòstila |
   | The Greek Theatre or Nature Square | El Teatro Griego o Plaza de la Naturaleza | El Teatre Grec o Plaça de la Natura |
   | Austria Gardens | Jardines de Austria | Jardins d'Àustria |
   | Laundry Room Portico / Washerwoman's Portico / Portico of the Washerwoman | Pórtico de la Lavandera | Pòrtic de la Bugadera |
   | Three Viaducts: Low / Middle / High (flyer: "Lower, Middle, and High Bridges") | Puente de Abajo / del Medio / de Arriba | Pont de Baix / Pont del Mig / Pont de Dalt ("Viaducte de Dalt" in the 2026 disruption notice) |
   | Palm Trees Path | — | Passeig de les Palmeres (on the services page) |
   | Larrard House | Casa Larrard | Casa Larrard |
   | Trias House | Casa Trías | Casa Trias |
   | Gaudí House Museum / Gaudí Museum House | Casa Museo Gaudí | Casa Museu Gaudí |
   | Hill of the Three Crosses | Colina de las Tres Cruces | Turó de les Tres Creus |
6. **Pavilions** (OFF entrance-pavilions page):
   - *"The one to the left was the one actually used as a Porter's Lodge, with a waiting room and telephone booth, while the one to the right was the porter's lodge … today part of the Barcelona History Museum."*
   - The Laie Park Güell Shop is *"in one of the entrance pavilions"* (OFF services page). INF: the shop is in the left pavilion.
   - ES Wikipedia (SEC, never alone) agrees that one pavilion is the museum and the other is a bookshop/souvenir shop. It puts the four-armed-cross tower on the administration (shop) pavilion.
   - **The point of view for "left/right" is not stated.** Verify on site (O2).
7. **Works, Nov 2026** (OFF disruptions page, last updated 2 Nov 2026):
   - The route **from Casa Trias to the Viaducte de Dalt** is closed, as is **Coll del Portell – Forat del Vent**. The works are *"expected to last 18 months."*
   - Maintenance on *"the steps-ramp between the Marianao entrance and the Lower Viaduct"* (from Nov 2024) *"will not affect the visit."*
   - **Effect on us:** the High Viaduct and Casa Trias cannot be reached by the usual viaduct climb. Keep the Pont de Dalt out of every loop (it is beyond "nearest viaducts" anyway).
8. **Gaudí House Museum** (outside stop only): reopened **9 July 2024** after façade and interior works. Entry is with the combined ticket from the official Park Güell site (OFF-AJ, 9 Jul 2024). Its exterior is pink stucco with a pointed tower (OFF, Sagrada Família). It is photographed *"from Passeig de les Palmeres"*.
9. **2026 Gaudí Year** (SEC press): Park Güell centenary dinner on 26 Apr 2026, and a photo exhibition *"A recer del Park Güell"*. Its dates conflict: 14 May – 13 Dec 2026 (The Local) or 31 Oct – 13 Dec 2026 (ad-hoc-news). **Its location in the park is unknown (O8).** No route change linked to the centenary was found.

---

## 1. Current visitor access (as of 6 Nov 2026)

### 1.1 Gates

| Gate (as named in the source) | Visitor use today | Grade | Evidence |
|---|---|---|---|
| **Carrer d'Olot main gate** (between the pavilions; Casa Vicens palm-leaf iron gates) | **Exit only** | OFF | *"one exit at carrer Olot"* (why-are-the-access-points-regulated, fetched 6 Nov 2026); *"Exit only: one gate on carrer d'Olot"* (Governance Report 2020). The page still calls it *"The main Park Güell entrance, located in Carrer d'Olot"* historically. |
| **Olot side / Carrer de Larrard / Marianao lane** | Visitor entrance | OFF | *"Carrer de Larrard (entry from the Carrer d'Olot / Carrer Marianao side lane)"* (node/268). The Governance Report lists "Olot" among the 4 shared gates. The 2026 mobility map names "Marianao Street". The disruption notice names *"the Marianao entrance"*. |
| **Carretera del Carmel, 23** (coach park, taxi rank) | Visitor entrance, **the operator's recommended one**, and the one for reduced mobility | OFF | FAQ and accessibility pages. The Bus Turístic blue stop "Park Güell" is on Av. de la Mare de Déu de Montserrat, *"through Av. Pompeu Fabra"*. |
| **Avinguda del Santuari de Sant Josep de la Muntanya** (escalator) | Visitor entrance | OFF | *"entry by escalator"* (node/268). Recommended from Lesseps L3. The sustainable-access page names escalators *"in Passatge de Sant Josep de la Muntanya"*. |
| **Baixada de la Glòria** (escalator, from Vallcarca L3) | Shared gate per the 2020 report. The 2026 how-to page instead says to take the escalator *"and then go to the entrance on Avinguda del Santuari de Sant Josep de la Muntanya"*. | OFF | **Unclear whether it is still a gate. Irrelevant for an Olot start.** |
| 4 residents-only gates | Not for visitors | OFF | not named |
| "Rambla del Brasil" | **No source found. Not a Park Güell gate.** Do not use. | — | — |
| CCTV and remote bollards installed "at each of the park's nine gates" | Jul 2022 – Apr 2023 | OFF | renovation item 13 |

### 1.2 Ticket checks and flows

- **First check:** at the gate you enter (*"validated at an access control point"*). No box-office sales: tickets are online only since 1 Jul 2024 (OFF-AJ Gràcia measure, May 2024). The map legend says *"Tickets online only"*.
- **Second check:** at the entrance to the high-concentration section (Pl. Natura, Hypostyle, Laundry Room Portico, Dragon Stairway, Austria Gardens). Inside it the route is **one-way** (OFF).
  - **Its exact location and the flow direction are not published in any text I could read.** The regulated-zone map image `Mapa_La_zona_regulada.jpg` was blocked, and the official app is JS-only.
  - Best evidence (INF): the pre-2020 reduced-mobility plan (OFF, CAT V2) shows three accesses to the old *"EIX MONUMENTAL"*: *"ACCÉS C. D'OLOT"*, *"ACCÉS AV. DE SANT JOSEP DE LA MUNTANYA"* and *"ACCÉS PLAÇA DE LA NATURA"*. Today's recommended-routes page has three tabs with the same names ("Sant Josep de la Muntanya", "Carrer Olot", "Plaça de la Natura"). It says *"The recommended routes allow all the points to be visited, whichever point of entry you use"*.
  - So the inner zone almost certainly has (or had) controlled mouths at (a) the entrance esplanade, at the foot of the stairway, (b) the Sant Josep de la Muntanya side, and (c) Plaça de la Natura from Passeig de les Palmeres.
  - **Which of these is entry and which is exit today is the No. 1 on-site question (O1).**
- **Official recommended route (stops A–I, the order as published):** A Entrance and concierge; B The guardhouse; C Monumental staircase; D The hypostyle room, outdoor; E The hypostyle room, inside; F The Austria Gardens; G Nature square; H The roadways, paths and viaducts; I Ramp and house Larrard. *"Follow the recommended route in order to visit all the points of interest signposted within the restricted area."* (OFF)
  - INF: this is the "Carrer Olot" order. It climbs the stairway, does the Hypostyle and Austria Gardens, reaches the Square, then goes out along the viaduct/portico path and down the spiral ramp to Casa Larrard, which is back near the Olot side. **It is a loop that ends near the Olot exit. That fits the "exit at Olot" rule.**
- **Re-entry:** none. *"once you have exited, you cannot re-enter."* (OFF FAQ)
- **Stay:** *"you can stay as long as you like"* (OFF FAQ).

### 1.3 Accessibility (for cueing only)

- The operator recommends arriving via **Carretera del Carmel** (OFF): *"irregular paths and steep ramps"*.
- The official **2026 reduced-mobility plan** has two routes:
  - "Visit to emblematic features / Architectural", approx. **50 min**.
  - "Other visitable places", approx. **20 min**, along the viaduct path up to Casa Trias. **Partly closed beyond Casa Trias, Nov 2026.**
  - Plan points: 1 High bridge, 2 Casa Trias, 3 Views of middle bridge, 4 Palm Trees Path, 5 Lower bridge, 6 Porter's lodge pavilions, 7 Stairway, 8 **Views of** The Laundry Room Portico, 9 Hypostyle Room, 10 Dragon or Salamander, 11 The Austria Gardens, 12 Nature Square.
  - INF: wheelchair users **see** the Portico rather than walk under it, and reach the square by the Palm Trees Path rather than the stairway.
- The Dragon Stairway is a stair: *"divided into three sections"* (OFF).
- **No official gradients, step counts or distances are published.**
- Wheelchairs can be booked. There are 3 reduced-mobility parking places at the Carmel coach park.

### 1.4 Toilets and services (OFF, maps-and-services)

- Toilets: (1) at the Carretera del Carmel gate; (2) on Passeig de les Palmeres next to Plaça de la Natura; (3) next to the Carrer d'Olot entrance.
- Free Wi-Fi *"inside the Monumental Core"*, for viewing QR information.
- Pets are not allowed in Nature Square, the Hypostyle, the Dragon Stairway, the Austria Gardens or the Laundry Room Portico.
- No prices or hours appear here (operations only).

---

## 2. Spaces in scope: names, placement, links

Placement grades. Positions use the official texts first. Where they are silent, I use rough komoot highlight coordinates (SEC-user, map-centre points, ±20 m): Dragon Staircase 41.413704, 2.152871; Greek Theatre/Plaça de la Natura 41.413929, 2.152209; Portico of the Washerwoman 41.413636, 2.151911. The Escola Baldiri Reixac address point (OFF-AJ guia.barcelona.cat) is 41.41348, 2.15311. **Distances derived from these are INF estimates. Walking minutes are my estimates at a slow tourist pace with stops excluded.**

| # | Space (EN / ES / CA) | Where (relative to neighbours) | What you see | Getting to the next stop | Zone |
|---|---|---|---|---|---|
| 1 | **Entrance esplanade inside the Carrer d'Olot gate** | South side of the park, on Carrer d'Olot (OFF). *"From the entrance, visitors can see the stairway with the hypostyle room."* (OFF) | Rustic stone wall topped with ceramic tiling and *"medallions bearing the name of Park Güell"*. Palm-leaf iron gates *"came from Casa Vicens"*. The stairway rising ahead. | The stairway foot is directly ahead (INF: a few tens of metres; under 1 min) | Ticketed 12 ha. INF: before the second control. |
| 2 | **Porter's Lodge / Casa del Guarda** (right pavilion per OFF) and the **other pavilion** (left per OFF: waiting room and phone booth; INF: today the Laie shop) | Either side of the gate (OFF) | Two pavilions with *"very beautiful roofs … covered with 'trencadís'"*. Casa del Guarda: MUHBA exhibition *"Güell, Gaudí and Barcelona, the expression of an urban ideal"* on 3 floors (house / park / city), included in the ticket but capacity-limited. | Next to stop 1 | Ticketed. INF: outside the inner section (not in the OFF list). |
| 3 | **Monumental Staircase / Dragon Stairway** — Escalinata Monumental | Rises *"[f]rom the entrance esplanade"* to the Hypostyle Room. The last flight is *"sheltered under the hypostyle room"* (OFF). | Twin flights in three sections; grottos (the right-hand one a waiting shelter); goblin shapes on the first landing; the emblem of Catalonia halfway; *"the dragon, or salamander"*; odeon-shaped bench on the last flight (OFF). The flyer adds a serpent-head spout and a tripod. | Climb up. INF: about 40–60 m of stairs; 2–3 min plus queues. | **Inner, one-way section** (OFF) |
| 4 | **Hypostyle Room** — Sala Hipóstila / Sala Hipòstila | At the top of the stairway, under the square (OFF) | *"86 striated columns inspired in the Doric order"*; ceiling of small domes with Jujol trencadís. The dragon's mouth is the overflow of the tank (OFF). The recommended route has "outdoor" (D) and "inside" (E) stops. | INF: the square is reached by the side paths and ramps around the Hypostyle. **The exact connection is not sourced (O4).** | Inner section |
| 5 | **Austria Gardens** — Jardines de Austria / Jardins d'Àustria | Official text gives no position. From its centre you see Casa Trias and the Gaudí House Museum (OFF). It is *"on the other side"* of the stairway from the school (SEC-wiki). Thebettervacation (SEC) says "northeastern". | Former plots, then the municipal nursery; trees donated by Austria in 1977 (OFF); "good views" (OFF). | INF: up to the square. Recommended stop order F→G. | Inner section |
| 6 | **Nature Square / Greek Theatre** — Plaza de la Naturaleza / Plaça de la Natura | *"Right at the centre of Park Güell"*; part dug into rock, part on top of the Hypostyle (OFF) | The undulating trencadís bench by Jujol on the stairway side acts as a balustrade. *"A viewpoint over the city"* (OFF). The bench trencadís was restored (renovation item 03, undated). | **To the Portico:** INF about 40 m (komoot points), 1–2 min | Inner section |
| 7 | **Laundry Room Portico** — Pórtico de la Lavandera / Pòrtic de la Bugadera | OFF: *"On the eastern side of the Greek Theatre square there is an original iron door which leads to where there used to be the gardens of Casa Larrard"*, along a path above the house through a pine grove, ending in a spiral ramp *"which takes visitors down to the house"*. SEC-wiki: *"Entre la plaza del teatro griego y la casa Larrard"*. **CONFLICT:** komoot coordinates put the Portico south-west of the square and west of the stairway. **East vs west is unresolved (O3).** | A *"great wave atop slanting columns"*; a double colonnade as buttress; a retaining wall of unworked stone; one column is a caryatid washerwoman carrying her tools (OFF CA flyer). The surrounding pavement was restored Jun–Aug 2022 after Storm Glòria (OFF). | Spiral ramp down towards Casa Larrard (recommended-route stop I). INF: 2–4 min. | **Inner one-way section** (OFF) |
| 8 | **Casa Larrard** (Escola Baldiri Reixac) | Beside the stairway on one side (SEC-wiki). Reached by the spiral ramp from the Portico path (OFF). Address point Carrer d'Olot 1–13 (OFF-AJ). | A former farmhouse of Can Muntaner de Dalt, Güell's residence, *"became a municipal public school in 1931, with the name of Baldiri Reixac"* (OFF). **Interior not visitable** (OFF flyer). A working school: never cue listeners into it. | INF: down to the Olot exit area | Ticketed area / school grounds. INF: after the inner section. |
| 9 | **Pont de Baix / Low Viaduct** (ES-wiki: "viaducto del Museo") | The *"first viaduct, near the central area, heading east toward the Carretera del Carmel exit"* (OFF). A steps-ramp links it to the Marianao entrance (OFF disruptions). | Curved, *"supported by two rows of inclined columns forming a parabola"*, rough stone; railing of planted pots (OFF). Restoration item 03 (*"recovering … the Viaducte de Baix"*). | INF: along Passeig de les Palmeres towards the Gaudí House (O5) | Ticketed, outside the inner section (INF) |
| 10 | **Pont del Mig / Middle Viaduct** (ES-wiki: "viaducto del Algarrobo") | Above the Pont de Baix on the climb towards Casa Trias (INF from order). The 2026 mobility plan has *"Views of middle bridge"*, between Casa Trias and the Palm Trees Path. | *"The carob bridge, where the natural growth of this interesting tree is respected"* (OFF); viaducts *"simulate natural caves"* (OFF). | **Beyond: the Casa Trias – Viaducte de Dalt section is CLOSED (Nov 2026).** | Ticketed |
| 11 | **Pont de Dalt / High Viaduct** ("viaducto de las Jardineras") | Reaches *"the highest part of the estate"* (OFF) | *"The bridge of the lovers, with terraced benches and gardeners with atzavares"* (OFF); stone planters on top (SEC-upc 1927 postcard). | **Closed approach from Casa Trias (OFF, 2 Nov 2026).** Not in our loops. | Ticketed |
| 12 | **Palm Trees Path** — Passeig de les Palmeres | The 10 m transversal road *"which connects the Carretera del Carmel with the Sant Josep de la Muntanya exit"* and runs *"around the great square from above"* (OFF). There are toilets on it next to Plaça de la Natura (OFF). | *"The widest road in Park Güell"* (OFF) | The route spine between the Carmel side, the square and the Gaudí House | Ticketed |
| 13 | **Gaudí House Museum** — Casa Museo Gaudí / Casa Museu Gaudí (outside only) | Seen *"from Passeig de les Palmeres"* (OFF Sagrada Família). Visible from the Austria Gardens (OFF). On the "camino del Rosario" (SEC-wiki). | Pink stucco house with a pointed tower and trencadís chimneys; Berenguer design; Gaudí lived there 1906–1925 (OFF). Interior needs the combined ticket (OFF). | INF: back along the Palm path | Ticketed park; interior on a combined ticket |
| 14 | **Casa Trias** | On *"the only two plots that were ever sold"* (OFF). On the viaduct path (accessibility page: *"follow the viaduct's path up to Casa Trias"*). | Batllevell, 1903–06, *"continues to be a private residence"*; **interior not visitable** (OFF) | **The path beyond it is closed.** | Ticketed park |
| 15 | **Turó de les Tres Creus** (context only, not a stop) | *"the highest part of Park Güell at 182.30 metres above sea level"* (OFF) | — | **The Coll del Portell – Forat del Vent route is closed (Nov 2026).** | — |
| 16 | **Viewpoints** | Nature Square (OFF "viewpoint over the city"); Austria Gardens ("good views", OFF); the Tres Creus summit (context); Baixada de la Glòria viewpoint (outside the park, renovation item 07) | Which landmarks are visible from each: **not sourced (O7)** | — | — |

**Also on the official list but out of scope:** the Biodiversity Itinerary (195 m, OFF) and the "Volta dels carruatges" carriage turn by the entrance (named on the MUHBA itinerary, OFF-AJ). INF: the Volta dels carruatges is a possible short add-on at the start; ask on site (O6).

---

## 3. The official park plans

| Plan | URL | Readable? | What I could read |
|---|---|---|---|
| "Imprescindibles" flyer map, EN | https://parkguell.barcelona/sites/default/files/mapa/ParkGuell_Flyer_Imprescindibles_en_red_c.pdf | Text only | Space names and short texts. Legend: "Spaces with control points and possible waiting times"; "Area with high concentration". The printed numerals (1,4,5,3,1,4,5,2,3) **could not be tied to labels**. |
| Same flyer, ES / CA / FR | `…/ParkGuell_Flyer_Imprescindibles_es_red_c.pdf`, `…_cat_red_c.pdf`, `…_fr_red_c.pdf` | ES and CA text read; FR not fetched | The official ES/CA names in section 0. Footnotes: Larrard and Trias *"Interior … no visitable"*; Gaudí House *"Acceso con entrada combinada"*. |
| **2026 reduced-mobility plan, EN** | https://parkguell.barcelona/sites/default/files/mobilitat/PKG_2026_Pl%C3%A0nol_Mobilitat_Redu%C3%AFda_np_opt_EN.pdf | Text only | Points 1–12 (section 1.3). Streets: Olot Street, Carmel Road, Marianao Street. Legend: Entrances, Information point, W.C., Exit, Rest area, Fountains, Taxis, Car Park, Food and Drink. **No positions.** |
| **Regulated-zone map** (shows the 12 ha and probably the inner zone and its control points) | https://parkguell.barcelona/sites/default/files/inline-images/Mapa_La_zona_regulada.jpg | **BLOCKED** (permission not answered) | **The lead should open it in the user's Chrome. It is the most important missing source.** |
| Services plan image (2021) | https://parkguell.barcelona/sites/default/files/2021-03/2021_Planols_i_serveis_800x390.jpg | Not fetched (image) | — |
| Official web app (accessible routes, points) | https://osam.bcn.cat/parkguell/inici | **BLOCKED** (JS app, permission not answered) | Open it in Chrome |
| Recommended-routes page (3 tabs + stops A–I) | https://parkguell.barcelona/en/planning-your-visit/recommended-routes | Text read; per-tab map is JS | Stops A–I only |
| Old reduced-mobility plan CAT V2 (pre-2020) | https://www.barcelonaturisme.com/files/9877-15-ArxiuCAT/PARK_GUELL_MOBILITAT_REDUIDA_CAT_V2.pdf | Text | The old "Eix Monumental" with three accesses (Olot, Sant Josep de la Muntanya, Plaça de la Natura) and "Zona de lliure accés". **Historical: do not script it.** |
| Virtual visit | https://parkguell.barcelona/visitavirtual/ | Not fetched | — |
| Works PDF (drainage etc.) | https://parkguell.barcelona/sites/default/files/PDF/Obres/Park%20G%C3%BCell%20-%20Obres%20de%20millora%20del%20sistema%20de%20drenatge%2C%20sanejament%20i%20reg%20v2610.pdf | Text | Segments "Coll del Portell – Forat del Vent" and "Forat del Vent – Casa Trias" |
| Official home page | https://parkguell.barcelona/en | **BLOCKED** | — |

**Lead action:** in Chrome, open (1) `Mapa_La_zona_regulada.jpg`, (2) the EN flyer PDF, (3) the 2026 mobility PDF, and (4) the osam app. Mark: where the second control is; the arrows of the one-way route; which side of the square the Portico is on; and where the Laie shop and Casa del Guarda are.

---

## 4. Changes 2013–2026 (dated)

| Date | Change | Grade |
|---|---|---|
| Oct 2013 | The Monumental Area is regulated (ticketed), about 1.7 ha | OFF |
| May–Sep 2017 | Baixada de la Glòria escalator: the 4th section is replaced and cables are put underground | OFF (item 08) |
| 17 Jan 2018 | Strategic Plan 2017–2022 approved | OFF |
| Jan 2020 | Storm Glòria damage near the Laundry Room Portico (two 200-year-old trees fell) | OFF (item 10) |
| 14 Mar – 20 May 2020 | Park closed (Covid) | OFF |
| **29 Jun 2020** | Access control of the **whole 12 ha** begins; Olot gate becomes exit-only | OFF (Governance Report 2020) |
| 21 Mar 2022 | Gaudí House Museum reopens after the Covid closure | OFF (Sagrada Família) |
| Jun–Aug 2022 | Pavements around the Portico of the Washerwoman restored | OFF |
| Jul 2022 – Apr 2023 | CCTV and remote bollards at all 9 gates | OFF |
| Undated, since 2017 | Restorations: Nature Square; Monumental Staircase; Hypostyle medallions; bench trencadís; Viaducte de Baix; Carmel gate; Olot/Marianao wall; the salamander's front right foot | OFF (renovation list; dates not printed) |
| 1 Jul 2024 | Tickets online only | OFF-AJ |
| **9 Jul 2024** | Gaudí House Museum reopens after façade and interior works; combined ticket via the Park Güell site | OFF-AJ |
| Nov 2024 → | Maintenance on the Marianao steps-ramp to the Lower Viaduct; *"will not affect the visit"* | OFF |
| 22 Oct 2025 | Council approves cutting available tickets from 4.5 M to 4 M over two years | SEC (Catalan News) |
| 2026 Gaudí Year | Centenary dinner 26 Apr; photo exhibition "A recer del Park Güell" (dates conflict, place unknown) | SEC |
| **Nov 2026 (notice updated 2 Nov 2026)** | Drainage, sewerage, irrigation, lighting and Wi-Fi works, about 18 months. **Closed: Coll del Portell – Forat del Vent, and Casa Trias – Viaducte de Dalt.** | OFF |
| — | Casa del Guarda: MUHBA exhibition continues; capacity-limited | OFF / OFF-AJ (no 2026 change found) |

---

## 5. Proposed loops (start: just inside the Carrer d'Olot gate)

**Design rule:** the inner section is one-way, and nobody can re-enter the park. So each loop does the outer-park items (pavilions, viaducts, Gaudí House) **either before the second control or after its exit**, never by doubling back through it. Two variants cover the unknown flow direction (O1).

### Variant A: the inner section is entered at the foot of the stairway (the official A–I order)

| Length | Sequence | Notes |
|---|---|---|
| **45 min** | 1 Esplanade + both pavilions (exterior) → 3 Dragon Stairway → 4 Hypostyle (outside, then inside) → 5 Austria Gardens → 6 Nature Square bench and view → 7 Laundry Room Portico → spiral ramp → 8 Casa Larrard (exterior) → exit area at Olot | Pure official A–I. About 15–20 min of walking (est.), plus queue buffers at the second control. |
| **75 min** | As 45, but after the Square leave the inner section towards **Passeig de les Palmeres** (O1: only if the exit allows it) → 13 Gaudí House exterior → 9 Pont de Baix → (10 view of Pont del Mig from below) → back down to Olot via the **Marianao steps-ramp** | Needs the inner section to exit onto the Palm path. Otherwise use Variant B. **The Portico must be done before you leave the inner section.** |
| **120 min** | As 75, plus the **Casa del Guarda interior** (3 floors; capacity-limited; at the start, before the climb) plus a longer stop in the Austria Gardens | **Honest note:** in the Nov 2026 scope (no Pont de Dalt, no Casa Trias approach, no Tres Creus, no museum interior), the material runs out at about **95–105 min** without padding. Recommend calling it a "Full ~100 min" length. The held items are: the Pont de Dalt and Casa Trias (closed approach), the Turó de les Tres Creus (out of scope), and the Gaudí House interior (combined ticket, out of scope). |

### Variant B: the inner section is entered from Plaça de la Natura or the Palm path and exits down the stairway to Olot

| Length | Sequence |
|---|---|
| **45 min** | 1 Esplanade + pavilions → (outer path) up to **Passeig de les Palmeres** → second control at the square → 6 Nature Square → 7 Portico → 5 Austria Gardens → 4 Hypostyle → 3 Dragon Stairway (down) → back at the esplanade/exit |
| **75 min** | 1 → Marianao steps-ramp → 9 Pont de Baix → (10 Pont del Mig, view only) → 13 Gaudí House exterior → Palm path → inner section as in the 45-min version → down the stairway to the Olot exit |
| **120 min** | As 75, plus the Casa del Guarda interior at the end, before the exit. **Same honesty note: a realistic Full is about 100 min.** |

**Time basis:** the OFF reduced-mobility plan gives about 50 min for the architectural route and about 20 min for the viaduct-to-Casa-Trias route. My walking estimates are INF, from komoot points: about 60 m stairway→square, about 40 m square→Portico, about 80 m Portico→stairway line.

### On-site decisions (only a visit can settle these)

| ID | Question | ALT options |
|---|---|---|
| **O1** | Where is the **second control point**, and which way does the **one-way** inner route run? Can you leave the inner section onto Passeig de les Palmeres, or only down to Olot? | ALT-A: entry at the stairway foot (official A–I) → use Variant A. ALT-B: entry at Plaça de la Natura → Variant B. ALT-C: entry from Sant Josep de la Muntanya → start the inner section at the Square from the north and keep Variant B's order. |
| **O2** | Which pavilion is the **Casa del Guarda** (MUHBA) and which is the **Laie shop**, seen from inside the gate? Does "right/left" on the OFF page mean as seen from the street? | ALT-A: Casa del Guarda on the right facing the stairway. ALT-B: on the left. Script landmark-first: "the pavilion with the museum sign" or "the pavilion with the tall tower and the cross". |
| **O3** | Is the **Laundry Room Portico** on the **west** or the **east** side of the Nature Square? (OFF text says "eastern"; komoot points and the Larrard placement suggest west/south-west.) Is it inside the one-way flow before or after the square? | ALT-A: west, reached from the square's west end → ramp down to Larrard. ALT-B: east. Use only landmark cues ("the wave-shaped stone portico with the washerwoman column") until verified. |
| **O4** | Exact link between the Hypostyle Room and the Square (side ramps or steps? which side?) | — |
| **O5** | Can a visitor walk the **Pont de Baix** and see the **Pont del Mig** in Nov 2026? Where does the closure start ("Casa Trias – Viaducte de Dalt")? Are the Marianao steps-ramp works still on? | ALT: if closed, view the Pont de Baix from the Palm path only |
| **O6** | Is the **Volta dels carruatges** (carriage turn) visible and open at the entrance? | Add as 1 min at the start, or drop |
| **O7** | Which landmarks are visible from the Nature Square bench and the Austria Gardens (Sagrada Família, sea, Montjuïc, Tibidabo)? | — |
| **O8** | Where is the 2026 exhibition **"A recer del Park Güell"**, and is it in our path? | Ignore unless it is on the route |
| **O9** | Is the Olot-side visitor entrance still the Marianao/Larrard lane? Can a listener who entered elsewhere (Carmel, Sant Josep) reach the inside of the Olot gate without crossing the inner section? | If not: provide a "start from Carmel" intro track |
| **O10** | Where do the queues for the inner section actually form? We need a waiting-friendly track (the history of the estate) at that point. | — |

---

## 6. What I could NOT find or verify

1. The location of the second control point, and the one-way direction (O1). The regulated-zone map image and the app were blocked.
2. Left/right viewpoint for the pavilions. Official confirmation that the Laie shop is in the left pavilion.
3. East vs west of the Portico (official text vs coordinates).
4. Official distances, gradients or step counts for any path.
5. Whether the Baixada de la Glòria gate is still a visitor gate in 2026.
6. The venue of the 2026 photo exhibition.
7. Catalan/Spanish pages of the emblematic features (a constructed CA URL was blocked). The names come from the CA/ES flyers instead.

---

## Appendix A. Raw graded notes

- OFF `how-to-get-there`: Lesseps L3 "20-minute walk" -> "we would recommend the entrance on Avinguda del Santuari de Sant Josep de la Muntanya, which has an escalator"; Vallcarca L3 -> "take the escalator on Baixada de la Glòria, and then go to the entrance on Avinguda del Santuari de Sant Josep de la Muntanya"; bus H6/D40 Travessera de Dalt -> Av. Santuari "with automatic stairs system" "or from Carrer Larrard"; Bus Turístic blue "Park Güell" stop on Av. de la Mare de Déu de Montserrat -> "entrance on Carretera del Carmel through Av. Pompeu Fabra"; taxi stand on Carretera del Carmel; coaches -> parking platform via Carretera del Carmel.
- OFF `maps-and-services`: map PDF `sites/default/files/mapa/ParkGuell_Flyer_Imprescindibles_en_red_c.pdf`; services plan image `sites/default/files/2021-03/2021_Planols_i_serveis_800x390.jpg`. Toilets: Carretera del Carmel at the park entrance gate; Passeig de les Palmeres next to Plaça de la Natura; next to the Carrer d'Olot entrance. Porter's Lodge at the Carrer d'Olot entrance, exhibition, included. Laie Park Güell Shop "in one of the entrance pavilions". Pets not in Nature Square, Hypostyle Room, Dragon Stairway, Austria Gardens, Laundry Room Portico. Free Wi-Fi "inside the Monumental Core". Tickets "online only" (legend).
- OFF flyer PDF (EN): Porter's Lodge (1901–1903, caretaker's residence); Monumental Staircase (three-section double stairway, fountain, dragon, tripod); Greek Theatre or Nature Square (bench by Jujol 1909–1914); Austria Gardens (former municipal nursery, named for 1977 tree donation); Hypostyle Hall (86 fluted columns); Three Viaducts: "Lower, Middle, and High Bridges"; Washerwoman's Portico (wave-shaped, caryatid column). Other points: Hill of the Three Crosses, Biodiversity Itinerary, Larrard House, Trias House, Gaudí House Museum. Footnotes: Larrard & Trias "Interior of these spaces not open to visitors"; Gaudí House Museum "Access with a combined ticket". Legend: "Spaces with control points and possible waiting times"; "Area with high concentration".
- OFF `emblematic-features`: 16 features (Dragon Stairway; Laundry Room Portico; Three Crosses 182.30 m a.s.l.; Gaudí Museum House; High Viaduct; entrance & porter's lodge pavilions "main Park Güell entrance, located in Carrer d'Olot"; Trias House; Middle Viaduct; Larrard House; Biodiversity Itinerary 195 m long; Greek Theatre or Nature Square; Hypostyle Room; Austria Gardens; Low Viaduct; Roadways, Paths and Viaducts; Palm Trees Path "width of 10 meters, which connects the Carmel road with the exit…").
- OFF `recommended-routes`: three routes named "Sant Josep de la Muntanya", "Carrer Olot", "Plaça de la Natura"; stops A–I: A Entrance and concierge; B The guardhouse; C Monumental staircase; D Hypostyle room, outdoor; E Hypostyle room, inside; F Austria Gardens; G Nature square; H Roadways, paths and viaducts; I Ramp and house Larrard. "Follow the recommended route in order to visit all the points of interest signposted within the restricted area." "The recommended routes allow all the points to be visited, whichever point of entry you use". Per-route order not in extracted text (JS map).
- OFF `faqs`: recommended entrance "Carretera del Carmel, 23, where there is also a coach park"; "tickets give access to the monument area, the green area and the panoramic areas"; "Reservations are held open for half an hour after the reserved time"; "Once you are inside Park Güell, you can stay as long as you like, but once you have exited, you cannot re-enter."; "Park Güell occupies 12 hectares"; "limited to 1400 visitors per hour"; reduced mobility: "irregular paths and steep ramps", recommends Carretera del Carmel, "a choice of two routes".
- OFF `why-are-the-access-points-regulated`: regulated since 2013 "to prevent tourist overcrowding"; monumental area = WHS 12 ha; adjacent 8 ha woodland; 9 entries: 4 neighbours/citizens only, 4 visitors+citizens, "one exit at carrer Olot"; 7:00–9:30 and 18:00–22:00 reserved for citizens (OPS ONLY); 9:30–17:30 shared.
- OFF `node/268`: three recommended entrances: "Carretera del Carmel, 23"; "Carrer de Larrard (entry from the Carrer d'Olot / Carrer Marianao side lane)"; "Avinguda del Santuari de Sant Josep de la Muntanya, entry by escalator."
- OFF `entrance-pavilions`: main entrance "on the south side, on Carrer d'Olot"; left pavilion "was the one actually used as a Porter's Lodge", "a waiting room and telephone booth"; right pavilion "the porter's lodge, whence the name"... "today part of the Barcelona History Museum" (extraction ambiguous — VERIFY); iron gates "in the shape of palm leaves… came from Casa Vicens"; wall rustic stone with ceramic tiling and medallions "bearing the name of Park Güell".
- OFF-AJ MUHBA `barcelona.cat/museuhistoria/en/heritages/els-espais-del-muhba/muhba-park-guell`: "Casa del Guarda (porter's lodge)"; exhibition "Güell, Gaudí and Barcelona, the expression of an urban ideal"; "the house, the park and the city – one for each of the building's three floors"; "Visits to the Casa del Guarda are included in the visit to the Park Güell Monumental Area"; address c/ d'Olot s/n.
- OFF-AJ MUHBA PDF `bcn.cat/museuhistoriaciutat/docs/casadelguardaeng.pdf` (undated): built 1901–1903; "located at the entryway to the complex"; no left/right.
- OFF `accessibility`: recommends "the entrance to Carretera del Carmel"; Architectural route "roughly 50 minutes"; Other visitable sites route "follow the viaduct's path up to Casa Trias… roughly 20 minutes"; app https://osam.bcn.cat/parkguell/inici; mobility map PDF (2026); wheelchairs bookable; 3 PRM parking places at the coach park near Carretera del Carmel; taxi stands rambla de Mercedes and carretera del Carmel.
- OFF `laundry-room-portico`: "On the eastern side of the Greek Theatre square there is an original iron door which leads to where there used to be the gardens of Casa Larrard"; path above the house through a pine grove; portico "adopts the shape of a great wave atop slanting columns", "a double colonnade that acts as a buttress", backs onto "a retaining wall made from unworked stone"; spiral ramp "which takes visitors down to the house"; name from "the sculpted figure on one of the columns"; Casa Larrard "since 1931 been a school". Image filenames use "bugadera". NOTE "eastern" side conflicts with other placement — VERIFY on plan/site.
- OFF `viaducte-baix`: curved, "supported by two rows of inclined columns forming a parabola"; "two rows of columns covered with rough stone"; railing of pots on small columns; "includes the central vault". URL slug "viaducte baix".
- OFF `roadways-paths-viaducts`: 3 km road network; three viaducts "five metres" wide winding up from Carrer d'Olot main entrance to the Turó de les Tres Creus; **Pont de Baix** = first, near central area, heading east toward the Carretera del Carmel exit; **Pont del Mig**; **Pont de Dalt** reaches the highest part; sloping columns & vaults of unhewn site stone; planted balustrades; transversal road "ten-meters-wide, which connects the Carretera del Carmel with the Sant Josep de la Muntanya exit" running around the great square from above; footpaths "three meters-wide".
- OFF `middle-viaduct` (title also "Viaducte del mig" in index.php URL): "The carob bridge, where the natural growth of this interesting tree is respected"; viaducts "simulate natural caves while, in parallel, acting as buttresses and retaining walls"; roads for vehicles on top, shelter below.
- OFF `high-viaduct`: subtitle "The bridge of the lovers, with terraced benches and gardeners with atzavares"; "With the aim of keeping the steep slopes in this area."
- OFF `disruptions` (fetched 6 Nov 2026): (1) drainage/sewerage/irrigation/lighting/Wi-Fi works, "Last updated 2/11/2026", "expected to last 18 months"; "The route between Coll del Portell and the Forat del Vent Stairway is closed"; also closed "from Casa Trias to the Upper Viaduct (Viaducte de Dalt)". PDF `sites/default/files/PDF/Obres/Park%20G%C3%BCell%20-%20Obres%20de%20millora%20del%20sistema%20de%20drenatge%2C%20sanejament%20i%20reg%20v2610.pdf` (title "Obres de millora del sistema de drenatge, sanejament i reg i de l'enllumenat al Park Güell"; segments "Coll del Portell – Forat del Vent" and "Forat del Vent – Casa Trias"). (2) Maintenance on "the steps-ramp between the Marianao entrance and the Lower Viaduct", "Start: November 2024 - End: -", "The works will not affect the visit." (3) outside: Jardins de la Font del Carbó Jan 2026–c. Jan 2028; (4) Carrer del Torrent del Remei / Farigola 16 Jan 2026–Jan 2027.
- OFF `renovation-works-status` ("since 2017"): 01 Nature Square; 02 Monumental Staircase; 03 Hypostyle Room medallions – Nature Square bench's trencadís – recovering the Font de la Sarva and the Viaducte de Baix; 04 Camí de la Pressió – Biodiversity Itinerary – children's play area c/ Olot; 05 Font de Sant Salvador – Forat del Vent; 06 Mur de les Llàgrimes; 07 Baixada de Glòria viewpoint; 08 overhead cables underground and the c/ Baixada de la Glòria escalator; 09 Carmel sports centre football ground; 10 "Restorations of the surrounding pavements of Portico of Washerwoman"; 11 lighting forest path from Av. Coll del Portell; 12 surroundings of bus stop 1223 Carretera Carmel; 13 Security Improvement and Access Control Plan; 14 Carmel entrance gate; 15 reinforcement of entrance wall c/ Olot/Marianao; 16 restoration of the front right foot of the salamander.
- OFF item 10: June 2022 – August 2022; Storm Glòria 2020 felled two 200-year-old trees, roots broke ceramic roof of a water mine that fed Casa Larrard; mine not visitable.
- OFF item 13: July 2022 – April 2023: "CCTV cameras and remotely controlled bollards were installed at each of the park's nine gates"; part of Park Güell Strategic Plan 2022-2026.
- OFF `the-restricted-area` ("Park Güell regulation"): "The ticket provides access to the 12 hectares of the Park."; "In October 2013, Barcelona City Council restricted access to the Monumental Area of Park Güell"; "There are parts of the park with a high concentration of visitors." "These are found within the section that has a second controlled access point, where visitors follow a one-way route" "...and are likely to have to wait to visit them." High-traffic spots: "Pl. Natura", "the Hypostyle Room", "the Laundry Room Portico", "the Dragon Stairway", "the Austria Gardens". Map image `sites/default/files/inline-images/Mapa_La_zona_regulada.jpg` -> FETCH BLOCKED (permission not answered; not retried).
- **KEY FINDING (OFF): the Laundry Room Portico is NOT in a free park; it is inside the ticketed 12 ha AND inside the inner second-control, one-way, high-concentration section with Nature Square, Hypostyle, Dragon Stairway, Austria Gardens.**
- OFF Governance Report 2020 PDF `sites/default/files/memoria/ParkGuell_memoria_web_en.pdf`: 9 gates: 4 residents/Gaudir+ only (unnamed); 4 shared with visitors "at Carmel, Olot, Sant Josep de la Muntanya and baixada de la Glòria"; "Exit only: one gate on carrer d'Olot"; access control began 29 June 2020; regulated zone to grow "from 1.7 to 12 regulated hectares"; Strategic Plan 2017-2022 approved 17 Jan 2018 (Park 19 ha, 1.7 regulated then); Casa del Guarda proposals 7.3-14/15. Closure 14 Mar 2020, reopened 20 May 2020, new model 1 Jul 2020.
- OFF entrance-pavilions (verbatim pieces): "To either side are the two pavilions that form the Porter's Lodge." "The one to the left was the one actually used as a Porter's Lodge, with a waiting room and telephone booth," "while the one to the right was the porter's lodge, whence the name The Porter's Lodge," "though it is today part of the Barcelona History Museum." Roofs Catalan clay tiles with trencadís. => RIGHT pavilion = Casa del Guarda (MUHBA). Viewpoint for left/right not stated (INF: probably facing the park from Carrer d'Olot) — VERIFY ON SITE.
- SEC (blog, thecreativeadventurer.com, published 2025-06-20): Portico of the Washerwoman "Tucked along one of the winding paths beneath the Nature Square"; "Lower Viaduct and Middle Viaduct staircases" "currently undergoing maintenance" (cites Feb 12, 2025); confuses Caretaker's Lodge with gift shop (unreliable).
- OFF `gaudi-museum-house`: built to plans of "Francesc Berenguer i Mestres", initiated by Josep Pardo i Casanovas; "In 1906 it was acquired by Antoni Gaudi's father, and the architect lived there until 1925".
- OFF (Sagrada Família Junta Constructora) `sagradafamilia.org/en/gaudi-house-museum`: caption "View of the exterior from Passeig de les Palmeres in Park Güell"; Berenguer (1866-1914), Gaudí signed plans; Gaudí lived 1906–1925; museum inaugurated 28 Sep 1963; three floors, basement, pointed tower; chimneys and tower roof trencadís; pink stucco walls; page still says "Gaudí House Museum is closed temporarily" and management passes to BSM "Starting in 2024" (STALE page).
- OFF (SF news 21 Mar 2022): reopened 21 Mar 2022 after closure since Mar 2020; "you must also have a ticket to Park Güell".
- OFF-AJ `barcelona.cat/infobarcelona/en/reopening-of-the-casa-museu-gaudi-at-park-guell_1418380.html` (9 Jul 2024): reopened "from 9 July" 2024 after works on façade and "various spaces inside"; combined ticket on official Park Güell site; coincided with 40th anniversary of WHS listing.
- OFF `house-larrard`: farmhouse of old Can Muntaner de Dalt estate; "became a municipal public school in 1931, with the name of Baldiri Reixac."
- OFF `trias-house`: on "the only two plots that were ever sold"; Juli Batllevell i Arús; 1903–1906; Martí Trias i Domènech (Güell family lawyer); "continues to be a private residence".
- OFF ES flyer `ParkGuell_Flyer_Imprescindibles_es_red_c.pdf`: COLINA DE LAS TRES CRUCES; ITINERARIO DE LA BIODIVERSIDAD; CASA LARRARD*; CASA TRÍAS*; CASA MUSEO GAUDÍ**; CASA DEL GUARDA; ESCALINATA MONUMENTAL; EL TEATRO GRIEGO O PLAZA DE LA NATURALEZA; JARDINES DE AUSTRIA; SALA HIPÓSTILA; LOS TRES VIADUCTOS ("Puente de Abajo", "el Puente del Medio", "el Puente de Arriba"); PÓRTICO DE LA LAVANDERA. Legend "Espacios con un segundo punto de control y posible tiempo de espera."; "Zona de alta concentración"; "Otros puntos de interés". "* Interior de estos espacios no visitable"; "** Acceso con entrada combinada."
- OFF CA flyer `ParkGuell_Flyer_Imprescindibles_cat_red_c.pdf`: TURÓ DE LES TRES CREUS; ITINERARI DE LA BIODIVERSITAT; CASA LARRARD*; CASA TRIAS*; CASA MUSEU GAUDÍ**; ESCALINATA MONUMENTAL; EL TEATRE GREC O PLAÇA DE LA NATURA; JARDINS D'ÀUSTRIA; SALA HIPÒSTILA; CASA DEL GUARDA; PÒRTIC DE LA BUGADERA (heading split in extraction); viaducts "Pont de Baix", "Pont del Mig", "Pont de Dalt". Legend "Espais amb un segon punt de control i possible temps d'espera."; "Zona d'alta concentració". Portico: one column is a caryatid of a laundress with her tools. Hypostyle 86 fluted columns, ceiling elements by Jujol. Escalinata: double staircase in three sections; serpent-head spout, dragon, tripod.
- OFF FR flyer also exists: `ParkGuell_Flyer_Imprescindibles_fr_red_c.pdf` (not fetched). DE flyer: not found in search.
- OFF reduced-mobility FR older version exists: `sites/default/files/PARK_GUELL_MOBILITE_REDUITE_FR_V2.pdf` (search hit, not fetched).
- OFF `dragon-stairway`: rises "[f]rom the entrance esplanade"; last flight "sheltered under the hypostyle room"; twin flight, walls with merlons forming terraces; two grottos beneath, right-hand grotto a waiting shelter on a conical central column; "divided into three sections"; first landing goblin-like shapes; halfway the emblem of Catalonia; then "the dragon, or salamander"; last flight an odeon-shaped bench; water from "tank under the hypostyle room".
- OFF `hypostyle-room`: "The great entrance stairway leads to the Hypostyle Room."; "86 striated columns inspired in the Doric order"; ceiling "formed of small domes" "decorated with original tile-shard mosaics made by Josep M. Jujol"; market; rainwater from the square to underground tank; overflow = "the stairway dragon's mouth".
- OFF `greek-theatre`: "Right at the centre of Park Güell"; part "dug into the rock", part "held up on top of the hypostyle room"; bench "planned by Josep M. Jujol, acting as a balustrade" on the stairway side; meta "A viewpoint over the city".
- OFF `austria-gardens`: from the garden's centre "the two houses that were built in Eusebi Güell's time can be seen" (Casa Trias, Gaudí House Museum); planned as plots; municipal nursery; 1977 tree donation from Austria.
- OFF `palm-trees-path`: "The widest road in Park Güell"; listing teaser: "With a width of 10 meters, which connects the Carmel road with the exit…" (= transversal road Carretera del Carmel – Sant Josep de la Muntanya exit, per roadways page). Toilets on Passeig de les Palmeres next to Plaça de la Natura (maps page). Gaudí House seen "from Passeig de les Palmeres" (SF).
- OFF-AJ MUHBA itinerary `barcelona.cat/museuhistoria/en/node/2415` ("El Park Güell, arquitectura i natura"): meeting point "Porta d'accés al Park Güell per carretera del Carmel"; stops "Casa del Guarda; Entrada del Park; Volta dels carruatges; Sala hipòstila; Viaducte de la Bugadera; Plaça del Teatre Grec"; c. 2 h.
- SEC-wiki (es.wikipedia.org/wiki/Parque_Güell; never alone): "Entre la plaza del teatro griego y la casa Larrard se halla el llamado «pórtico de la Lavandera»"; viaducts: lower "viaducto del Museo o pont de Baix" (gothic, inclined columns, benches); middle "viaducto del Algarrobo o pont del Mig" (carob trunk); upper "viaducto de las Jardineras o pont de Dalt" (planters with agaves); Casa Larrard = CEIP Baldiri Reixac "on one side of the escalinata", Austria garden on the other side; Casa-Museo Gaudí "en el camino del Rosario"; porter's pavilion with tower-mirador (interpretation centre); administration pavilion with tower topped by four-armed cross, now bookshop/souvenir shop (CHECK: conflicts in part with OFF which says the right pavilion = MUHBA porter's lodge; both agree one = museum, other = shop).
- SEC-upc (UPCommons, Editorial Canosa postcard 1927): "Camí amb jardineres de pedre de la part superior del Pont de Dalt" -> corroborates Pont de Dalt = viaduct of the planters.
- SEC (thebettervacation.com, mod. 2026-03-30): "On the eastern side of Nature Square, the Wash House Portico" (copies OFF wording); Austria Gardens "Located in the northeastern part of Park Güell". INF CONFLICT: if Austria Gardens are NE and on the opposite side of the stairway from Casa Larrard, the Portico (between square and Larrard) is on the WEST. OFF says "eastern side". UNRESOLVED -> O-question.
- SEC (headout.com blog, updated 2 May 2025): lists the Laundry Room Portico and viaducts under "Free Access Area" -> WRONG vs OFF 2026 (example of the misplacement customers complained about).
- OFF `access-regulations`: 2.08 "Tickets allow entry into the Park for 30 minutes after the time-band reserved."; 2.11 "Once the ticket has been validated at an access control point it will no longer be possible to leave and then re-enter."; 3.05 Casa del Guarda: ticket "does not guarantee entry" (limited capacity); 3.22 guided tours only by official guides qualified by the Generalitat; 3.23 "You may not use megaphones, speakers or any similar voice-amplification devices during tours inside the premises." (=> our guide must be headphone-only; never ask listeners to play aloud).
- OFF old (pre-2020) reduced-mobility map CAT V2 (hosted barcelonaturisme.com/files/9877-15-ArxiuCAT/PARK_GUELL_MOBILITAT_REDUIDA_CAT_V2.pdf): labels "ACCÉS C. D'OLOT", "ACCÉS AV. DE SANT JOSEP DE LA MUNTANYA", "ACCÉS PLAÇA DE LA NATURA" to the "EIX MONUMENTAL"; "Zona de lliure accés"; "Sortida"; points A–I. INF: these three historical accesses to the old 1.7 ha zone match the three route tabs on today's recommended-routes page and are the likely sites of today's "second controlled access point" — VERIFY.
- OFF-AJ Gràcia district measure (file 240515, i.e. 15 May 2024): "A partir del proper 1 de juliol la venda d'entrades per visitar el parc serà exclusivament online" (=> online-only from 1 Jul 2024); main entrance "el seu accés més reconeixible al carrer Olot"; 83% online in 2023.
- SEC (Catalan News, 22 Oct 2025): council approved reducing available tickets from 4.5 M to 4 M "progressively done during the next two years" (before 2027); ~130 fewer per hour.
- OFF 2026 reduced-mobility map raw order: 1 High bridge; 2 Casa Trias; 3 Views of middle bridge; 4 Palm Trees Path; 5 Lower bridge; 6 Porter's lodge pavilions; 7 Stairway; 8 Views of The Laundry Room Portico; 9 Hypostyle Room; 10 Dragon or Salamander; 11 The Austria Gardens; 12 Nature Square. Legend: "Architectural / Visit to emblematic features" ~50 min; "Other visitable places" ~20 min; streets Olot Street, Carmel Road, Marianao Street.
- OFF 2026 reduced-mobility map `sites/default/files/mobilitat/PKG_2026_Pl%C3%A0nol_Mobilitat_Redu%C3%AFda_np_opt_EN.pdf`: streets Olot Street, Carmel Road, Marianao Street; points 1 High bridge; 2 Casa Trias; 3 Views of middle bridge; 4 Palm Trees Path; 5 Lower bridge; 6 Porter's lodge pavilions; 7 Stairway; 8 Views of The Laundry Room Portico; 9 Hypostyle Room; 9[10?] Dragon or Salamander; 11 The Austria Gardens; 12/10 Nature Square (numbering garbled in extraction). Legend: Architectural / Visit to emblematic features / Other visitable places / approx. duration 50 min / approx. 20 min / Recommended route for people with reduced mobility / Entrances, Information point, W.C., Exit, Rest area, Fountains, Taxis, P Car Park, Food and Drink.

## Appendix B. Log of fetches (all 6 Nov 2026)

| URL | Result |
|---|---|
| https://parkguell.barcelona/en | FAILED (permission request not answered in time; not retried) |
| https://parkguell.barcelona/en/planning-your-visit/how-to-get-there | OK |
| https://parkguell.barcelona/en/planning-your-visit/maps-and-services | OK |
| https://parkguell.barcelona/sites/default/files/mapa/ParkGuell_Flyer_Imprescindibles_en_red_c.pdf | OK, partial (text only; map numbering not linkable to labels) |
| https://parkguell.barcelona/en/park-guell/emblematic-features | OK (16 features listed) |
| https://parkguell.barcelona/en/planning-your-visit/recommended-routes | OK, partial (route order per entrance is JS) |
| https://parkguell.barcelona/en/planning-your-visit/faqs | OK |
| https://parkguell.barcelona/en/a-park-for-everone/why-are-the-access-points-regulated | OK |
| https://parkguell.barcelona/en/node/268 | OK |
| https://parkguell.barcelona/en/park-guell/emblematic-features/entrance-pavilions | OK (left/right ambiguous) |
| https://barcelona.cat/museuhistoria/en/heritages/els-espais-del-muhba/muhba-park-guell | OK |
| https://bcn.cat/museuhistoriaciutat/docs/casadelguardaeng.pdf | OK, no left/right |
| https://parkguell.barcelona/en/accessibility | OK |
| https://parkguell.barcelona/sites/default/files/mobilitat/PKG_2026_Pl%C3%A0nol_Mobilitat_Redu%C3%AFda_np_opt_EN.pdf | OK, text only; numbering garbled |
| /en/park-guell/emblematic-features/laundry-room-portico, /viaducte-baix, /roadways-paths-viaducts, /middle-viaduct; /en/park-historic/espais-emblematics/high-viaduct | OK |
| https://parkguell.barcelona/en/disruptions (2 prompts) + works PDF v2610 | OK |
| https://parkguell.barcelona/en/renovation-works-status + items 10, 13 | OK |
| https://parkguell.barcelona/en/planning-your-visit/the-restricted-area (2 prompts) | OK |
| https://parkguell.barcelona/sites/default/files/inline-images/Mapa_La_zona_regulada.jpg | FAILED (permission not answered; not retried) |
| https://parkguell.barcelona/sites/default/files/memoria/ParkGuell_memoria_web_en.pdf | OK |
| https://thecreativeadventurer.com/the-ultimate-self-guided-tour-of-park-guell-updated-2025/amp/ | OK (SEC blog, low reliability) |
| https://parkguell.barcelona/en/park-guell/emblematic-features/gaudi-museum-house, /house-larrard, /trias-house | OK |
| https://sagradafamilia.org/en/gaudi-house-museum ; /en/-/la-casa-museu-gaudi-es-podra-visitar-a-partir-del-21-de-marc | OK |
| https://www.barcelona.cat/infobarcelona/en/reopening-of-the-casa-museu-gaudi-at-park-guell_1418380.html | OK |
| ES and CA flyer PDFs (sites/default/files/mapa/...) | OK (text only) |
| https://parkguell.barcelona/ca/park-historic/espais-emblematics | FAILED (permission not answered; constructed URL; not retried) |
| https://parkguell.barcelona/index.php/en/park-guell/emblematic-features | OK (EN only) |
| /en/park-guell/emblematic-features/dragon-stairway, /hypostyle-room, /greek-theatre, /austria-gardens, /palm-trees-path | OK |
| https://barcelona.cat/museuhistoria/en/node/2415 (MUHBA itinerary) | OK |
| https://en.wikipedia.org/wiki/Park_G%C3%BCell | OK, little layout detail |
| https://es.wikipedia.org/wiki/Parque_G%C3%BCell | OK (SEC-wiki; used only with OFF corroboration) |
| https://upcommons.upc.edu/entities/publication/5eb8c2b9-2507-411d-a067-9fb840277947/full | OK |
| https://voicemap.me/tour/barcelona/park-guell-tour-a-fun-and-cultural-look-into-gaudi-s-world/sites/portic-de-la-bugadera-2 | OK, preview only |
| https://nominatim.openstreetmap.org/search?q=... | FAILED (permission not answered; not retried) |
| https://osam.bcn.cat/parkguell/inici | FAILED (permission not answered; not retried) |
| https://thebettervacation.com/barcelona/park-guell-monumental-zone/amp/ | OK (SEC blog, mod. 2026-03-30) |
| https://parkguell.barcelona/en/planning-your-visit/access-regulations | OK |
| https://parkguell.barcelona/en/planning-your-visit/recommended-routes?q=... (2nd prompt) | OK, same content |
| https://bcnroc.ajuntament.barcelona.cat/.../Encargo%20Gest.%20accesos%20P.G%c3%bcell.pdf | OK (13 Feb 2013; 800 visitors/h then) |
| https://ajuntament.barcelona.cat/gracia/sites/default/files/documentacio/240515%20MdG%20Mesures%20mobilitat%20park%20G%C3%BCell.pdf | OK |
| https://www.barcelonaturisme.com/files/9877-15-ArxiuCAT/PARK_GUELL_MOBILITAT_REDUIDA_CAT_V2.pdf | OK (old plan) |
| https://www.catalannews.com/discover-catalonia/item/barcelona-reducing-park-guell-visitors-2027-22-october-2025 | OK |
| https://www.apd.cat/... -> redirect apdnoticies.com | FAILED (redirect target permission not answered; not retried) |
| https://parkguell.barcelona/en/a-park-for-everone/sustainable-access | OK |
| https://parkguell.barcelona/en/renovation-works-status/08-baixada-gloria-escalator | OK |
| https://www.thelocal.es/20260325/everything-you-need-to-know-about-barcelonas-gaudi-year-2026 | OK (SEC press) |
| https://parkguell.barcelona/en/info-expo | OK (2024 coupDefouet exhibition, past) |
| https://www.ad-hoc-news.de/unterhaltung/reisen/park-gueell-opens-an-exhibition-on-31-october-2026/70405243 | OK (SEC aggregator, low reliability) |
| https://www.barcelona.cat/ciutatcuidadora/en/detail/escola-baldiri-reixac_92168164500 ; https://guia.barcelona.cat/en/detall/patis-escolars-oberts-al-barri-escola-baldiri-reixac_99400677266.html | OK (address; route-link coords 41.41348, 2.15311) |
| https://www.komoot.com/highlight/5642019 (Portico), /highlight/5642064 (Dragon), /de-de/highlight/5642007 (Greek Theatre) | OK (SEC-user map-centre coordinates) |
| https://headout.com/blog/park-guell-map | OK (SEC reseller, outdated "Free Access Area") |

Prices and hours: deliberately omitted (operations only; not for scripts).

# Spotify Camp Nou / FC Barcelona Museum: visitor route, spaces and status (research as of 14 Nov 2026)

Prepared for: Yo Tours audio guide (campnou_v5). Researcher: route-and-spaces subagent, 14 Nov 2026.
Scope (USER_DECISIONS.md): the **Museum ticket only** ("Museum + Digital Audio Guide" + "Construction Viewpoint") and the outside of the stadium as reached on that ticket. Not the Spotify Camp Nou Experience (stadium panorama), Match Day Tour (pitch walk), Barça Sky Tour, BarçaBus or Training City products. Lengths 30 / 60 / 90 min including walking.
Method: WebSearch + WebFetch only, one page at a time per site. No curl, no browser, no CAPTCHA. Wikipedia not used at all. Every claim carries a URL in Appendix A. Failed pages are listed in Appendix B and were not retried.
Status: complete for desk research (14 Nov 2026). The lead read the old guide only as a lead (USER_DECISIONS: "start fresh"). §7 records which of its spaces still exist.

Grades:
- **OFF**: FC Barcelona's own page or file, fetched (fcbarcelona.com / .es; club PDFs).
- **OFF-AJ**: Ajuntament de Barcelona listing (agenda500.barcelona.cat). Official-city, not the operator, and often stale.
- **SEC**: secondary page, fetched. The type is in brackets: press, StadiumDB, blog, reseller, accessibility NGO. **SEC-WEAK** is an aggregator blog or reseller with stale signs.
- **SNIP**: search snippet only. It is a lead, not a fact.
- **INF**: my inference from the graded facts listed with it. **Verify on site before scripting any INF placement.**

Every page was fetched on 14 Nov 2026. The fetch tool returns short excerpts, so quotes are short.
**No prices or hours in scripts.** Where hours or prices appear below, they are marked OPS ONLY.

---

## 0. Key facts for the script (summary)

1. **On 14 Nov 2026 the Museum ticket is still the "Barça Immersive Tour".** It is a temporary museum in the former **Palau de Gel** (the club's old ice rink), "next to the Palau Blaugrana", and it is **not inside the stadium** (OFF: ticket page live 14 Nov 2026; news 27 Jan 2026; news 6 Jun 2023). It covers about 2,400 m² and opened on 6–7 Jun 2023. The live ticket page still says "the FC Barcelona Museum has temporarily moved to a spectacular 2,400 m² space". The official audio guide is the "Digital Audio Guide".
2. **BIGGEST RISK: a move is imminent.** The club aims to open the **new museum inside Spotify Camp Nou in November 2026** (SEC press: Ara, 7 Oct and 10 Oct 2026; Crónica Global, 19 Jun 2026; OFF news, 27 Jan 2026: "expected to reopen during 2026"). The new museum is 2,800 m² and was designed by Mediapro Exhibitions. Moving the collection takes **about 15 days with no visitors**, during which the Immersive Tour closes (Ara, 7 Oct 2026). As of 14 Nov 2026 **no closure, move date or new-museum location is published** on any official page I could read. The timetable shows normal exceptions through December, and the Flexible ticket is valid to 28 Feb 2027. → **Before any script is locked, the lead must check the official ticket page and news (O2). If the new museum opens, §2 and §5 must be re-researched.** Keep tracks topic-keyed (Cruyff, Messi, 1992…) rather than room-keyed so they survive the move.
3. **Official space list (OFF ticket page, ES and EN, in page order).** Items 5 and 6 are paid extras and are **NOT on the Museum ticket**.
   | # | ES (official) | EN (official) | CA | On Museum ticket? |
   |---|---|---|---|---|
   | 1 | Trofeos del Museo del FC Barcelona | FC Barcelona Museum Trophies | not read (O13) | yes |
   | 2 | Historia del Barça | Barça History | not read | yes |
   | 3 | Zona Messi | Messi Zone | not read | yes |
   | 4 | Macro Sala 360° (= "SPOTIFY CAMP NOU LIVE" show) | 360° Macro Room | not read | yes |
   | 5 | RoboKeeper Challenge | RoboKeeper Challenge | — | **no** (Total Experience / add-on) |
   | 6 | Barça Virtual Dream | Barça Virtual Dream | — | **no** (Total Experience / add-on) |
   | 7 | Mirador de las Obras | Mirador de las Obras / "Construction Viewpoint" | Mirador de les obres (SNIP, VERIFY) | yes |
   - The "Construction Viewpoint" item also covers "a full exhibition on the architectural project for the future Espai Barça, with **models and audiovisual pieces**" (OFF ticket text, published 2 Feb 2023 and still linked).
4. **Entrance: OFF pages conflict, so this is the No. 1 on-site question (O1).**
   - The **newest OFF page** (non-match-day access page; maps uploaded 2–8 Oct 2026) says **Access 9, Av. de Joan XXIII**, is the "Most direct access to the Museum, the Official Store...". It says **Access 15 (c. Arístides Maillol)** and **15A (Travessera de les Corts)** serve the **Spotify Camp Nou Experience** stadium tour, the OAB and Cal Blay.
   - The **older OFF practical page** (2023 text) gives "C/ Arístides Mallol s/n (Main Access No. 15) or … (Boulevard Access: No. 9)".
   - The user's old guide, a reseller's guided tour and a 2026 blog all put the museum door on **Arístides Maillol / Access 15**. The address is "Carrer d'Arístides Maillol, 12–18" (OFF-AJ).
   - INF: both gates lead onto the club campus, and the museum building is inside it. Script "follow the signs for the Museum / Barça Immersive Tour" until O1 is settled. **Do not name a gate number in scripts yet.**
5. **The visit sequence is one-way in practice and ends at the Construction Viewpoint** (OFF: "you'll conclude the tour at the Spotify Camp Nou Construction Viewpoint"). The exhibition "finishes in the large immersive space" (OFF). The viewpoint is reached "from what used to be the entrance to the old museum" (OFF, 2023 text). The old museum was in the Tribuna (main stand) area (OFF), so INF: **the viewpoint is at the main-stand side of the stadium, outdoors on a balcony/deck**. The old guide says you climb stairs to a wooden deck. **Exit: whether it is through the Barça Store is NOT stated by OFF.** The old guide says it is (O7).
6. **Audio guide.** It runs on the visitor's own phone from a **QR code on a card at the entrance**, and visitors should "Bring headphones" (OFF accessibility page). **Languages conflict:** CA/ES/EN + Catalan Sign Language (OFF accessibility page) vs 14 languages (OFF ticket text from 2023). Ours (EN, ES, FR, DE) adds placement and stories. Check whether the official guide uses numbered stops we could cue to (O6).
7. **Health warning (OFF).** The 360° immersive room is "not recommended for people with epilepsy or photosensitivity". Lighting is "subdued" throughout. **Put a skip cue in the track before the 360 room.**
8. **The stadium works on 14 Nov 2026 (dated, §4).**
   - The stadium has been back in use since **22 Nov 2025**, first at 45,401 (Phase IB). Since **10 Mar 2026** it holds **62,652** (Phase 1C), with the **Gol Nord** opened and a South Goal supporters' stand, "**Gol 1957**" (OFF).
   - The **third tier is not open and will not open this season**. The **roof is not built**: the 830 m compression ring was completed on 5 Oct 2026, and the roof goes in from summer 2027 (SEC, Ara, 10 Oct 2026).
   - The club expects to **leave for Montjuïc in May 2027** for the roof lift and return around **Jan 2028** (SEC FGG, citing The Athletic). It plans 105,000 seats when finished.
   - So in Nov 2026 a viewer sees **a working stadium with an unfinished top**: the third-tier structure, the compression ring, cranes, no roof. It is **not** a demolition site any more. The OFF viewpoint copy ("follow the demolition and rebuilding") is 2023 text, and **scripts must not repeat it**.
9. **Statues.**
   - The **Kubala** (2009) and **Cruyff** (bronze, 3.5 m, 2019, by Corry Ammerlaan-van Niekerk) statues stood on the forecourt at the **Tribuna entrance**, side by side (OFF 2019; SEC).
   - **Where they are in Nov 2026 is not documented** (O9).
   - **There is no Messi statue.** In Nov 2025 Laporta said the club is "working on it", with no design and no date (SEC StadiumDB). **Never script "the Messi statue".**
10. **Match days (OPS ONLY).** The Museum closes early on event days: 17 Nov until 17:00, 22 Nov until 14:00, 2 Dec until 21:30 and 8 Dec until 15:00 (OFF timetable; 2 and 8 Dec are the Atlético and Man City Match Day Tour dates). Crowds and security on those days will change approach and exit (O8).

---

## 1. Current access (as of 14 Nov 2026)

### 1.1 What the Museum ticket includes (OFF ticket pages, live 14 Nov 2026)
| Item | Included? | Source / grade |
|---|---|---|
| Museum (Barça Immersive Tour, former ice rink) | Yes | OFF |
| Digital Audio Guide (own phone, QR card, headphones) | Yes | OFF |
| Construction Viewpoint (Mirador de las Obras) + Espai Barça models and audiovisuals | Yes | OFF |
| 360° Macro Room / "Spotify Camp Nou Live" show | Yes (part of the museum) | OFF |
| RoboKeeper, Barça Virtual Dream (VR), digital souvenir photo | **No**: Total Experience or add-ons | OFF |
| Stadium interior: stands, panorama, dressing room, pitch, tunnel | **No.** Panorama = Spotify Camp Nou Experience (Access 15, first tier, guided). Pitch = Match Day Tour (match days only). "Due to the works … the tickets do not include a tour of the interior of the stadium" (OFF-AJ) | OFF / OFF-AJ |
| Visit length | "The duration of the visit is 1h" (OFF). 45–60 min (SEC 2023). Museum c. 45 min plus viewpoint 5–10 min (SEC-WEAK 2026) | OFF / SEC |

### 1.2 Getting in
| Step | What sources say | Grade |
|---|---|---|
| Transport | Metro L3 Palau Reial, Les Corts, Zona Universitària, Maria Cristina. L5 Collblanc, Badal, Ernest Lluch. L9S/L10 Collblanc. Tram T1–T3 (Palau Reial, Pius XII, Av. de Xile…). Buses incl. the sightseeing bus blue route. Car access removed by the works. | OFF (Oct 2026 page) / SEC |
| Gate | **Access 9, Av. Joan XXIII** = "Most direct access to the Museum, the Official Store" (OFF, Oct 2026) **vs Access 15, Arístides Maillol** (OFF 2023 text, reseller, old guide, blog) | CONFLICT → O1 |
| Building | The former Palau de Gel ice rink, "next to the Palau Blaugrana" (OFF ×3). The old guide calls it a "low building marked Barça Immersive Tour or FCB Museum". | OFF / lead |
| Ticket check and desk | An entrance information desk lends 2 wheelchairs and a portable induction loop and has the audio-guide QR cards (OFF). Ticket booths open 15 min before the tour starts (OFF). Under-4s collect a free ticket at the ticket office (OFF). There is an orientation map in the lobby (SEC-access). A cloakroom takes luggage and pushchairs (SEC-WEAK reseller). | OFF / SEC |
| Security screening | Not documented | O1 |
| Re-entry | Not documented. Treat as no re-entry (INF). | — |

### 1.3 Accessibility (for cueing only)
- "The entrance is flat"; the visit is "fully accessible", "fully adapted for people with reduced mobility and wheelchair users" (OFF). There are adapted lifts (SEC-access). Toilets are adapted and have baby changing (OFF).
- Catalan Sign Language audio guide, tactile QR codes, noise-cancelling headphones on loan, and Quiet Hours (OPS ONLY) are offered (OFF).
- A **rest area and drinking fountains are on "Rambla del Barça"** (OFF). Its position is unknown (O10).
- Conflict: the old guide says stairs lead up to the viewpoint deck, while OFF says "fully accessible". INF: there is a lift or ramp alternative (O4).
- The **360 room is not advised for epilepsy or photosensitivity**; visitors should tell staff (OFF).

### 1.4 Temporary relocations (verified)
- **Museum:** it left the stadium on 28 May 2023 and has been in the former ice rink since 6–7 Jun 2023, as the "Barça Immersive Tour" (OFF). That was due to last until the 2024/25 season (OFF 2023), a date that slipped. A new in-stadium museum is targeted for Nov 2026 but not yet open or announced (SEC/OFF, §0.2).
- **Ice rink:** a new provisional rink opened on UB land (Carles Ferrer Salat 7) in May 2026 and was inaugurated on 5 Jun 2026 (SEC ×2). The old Palau de Gel building still houses the museum.
- **Palau Blaugrana:** the current building still stands. A new one on the former Miniestadi site is planned from 2028 (SEC).

---

## 2. Spaces on the Museum-ticket visit (Barça Immersive Tour, Nov 2026)

**Caveat.** The OFF room list is short (4 museum spaces + viewpoint). Room-level content and order come partly from opening-day press (Jun 2023) and the user's old guide (lead). **No official room plan exists online** (§3). Everything marked SEC-2023 or lead **must be checked on site (O3)**.

| # | Space (official name where one exists) | Where / order | What is there | To the next stop | Grade |
|---|---|---|---|---|---|
| S0 | Approach and campus | Access 9 (Joan XXIII) or 15 (Arístides Maillol) → campus → museum building (O1) | The stadium bowl with cranes over the upper ring (SEC 2026 photo caption); the third tier under construction, no roof (§4); the Palau Blaugrana beside the museum building (OFF). The Masia de Can Planes is on the official campus map (OFF); its position relative to the route could not be read (O10). Statues: O9. | Follow the museum signs | OFF / SEC |
| S1 | Museum entrance hall (former Palau de Gel) | Ground level; flat entrance (OFF) | Information desk, QR audio-guide cards, wheelchairs and induction loop (OFF); orientation map (SEC-access) | Into the exhibition | OFF / SEC |
| S2 | Opening audiovisual | First room (lead: "a large dark space with a long curved screen") | Not documented by OFF. INF: the start of "Historia del Barça". | — | lead only |
| S3 | **Trofeos del Museo del FC Barcelona / FC Barcelona Museum Trophies** | 1st on the OFF list | "All the Champions League titles, La Liga titles, and other accolades" (OFF); five men's European Cups, women's titles and a **mosaic of 200 jerseys** (SEC 2023). The women's 2nd UWCL trophy was placed in a cabinet at the opening (OFF 2023). Collection: >100 football trophies, 25 women's football, 50 other sections (OFF 2024). | — | OFF / SEC-2023 |
| S4 | **Historia del Barça / Barça History** | 2nd on the OFF list | "the history of all our teams and their most memorable milestones" (OFF). SEC-2023 / SEC-2026 / lead name these zones: **legends** (Cruyff and the Dream Team; Messi); **'Masia' academy zone**; **interactive room with 11 columns** (one per main men's and women's player); **values / "Més que un club"** and Catalan identity (SEC-WEAK); **a tunnel dedicated to the men's and women's teams** (SEC blog Aug 2026); 18 interactive and audiovisual installations in total (SEC blog Aug 2026; the old guide says "Eighteen rooms"). **Founding documents (1899, Gamper): NOT found in any source (O12).** | — | OFF / SEC |
| S5 | **Zona Messi / Messi Zone** | 3rd on the OFF list | "his Ballon d'Or awards and Golden Boots" (OFF). Lead: a darkened circular room with a low curved central display. | Follow the floor arrows (lead) | OFF / lead |
| S6 | **Macro Sala 360° / 360° Macro Room**, show "**SPOTIFY CAMP NOU LIVE**" | 4th on the OFF list; the exhibition "finishes in the large immersive space" (OFF) | Circular main space; projections on walls **6 m high and 78 m long** (OFF 2023); "the largest immersive room in a sports museum in Europe" (OFF); a 10-min show with AI/deepfake "holograms" of Cruyff, Messi, Ronaldinho, Iniesta, Putellas, Pedri (SEC 2023: content may have been updated). **Photosensitivity warning (OFF).** | Exit door to the viewpoint (lead: door marked "Mirador de las Obras") | OFF / SEC |
| S7 | Extras (not on ticket): RoboKeeper, Barça Virtual Dream | Somewhere on the route (SEC reviews 2023: goal-kicking after the film) | Skip cue for Museum-ticket holders | — | OFF |
| S8 | **Espai Barça exhibition** (models and audiovisuals) | Part of the "Construction Viewpoint" item (OFF). Its order relative to S9 conflicts: OFF 2023 copy says the tour leads into the Espai Barça display; the old guide puts the model gallery **after** the deck. | "models and audiovisual pieces" of the future stadium (OFF); the old guide: "a large, illuminated 3D scale model". **Still there in Nov 2026? (O5)** | — | OFF / lead |
| S9 | **Mirador de las Obras / Construction Viewpoint** | **Last stop** (OFF); reached "from what used to be the entrance to the old museum" (OFF 2023) → INF: main-stand side, outdoors | A balcony over the works; screens with an inside view of the stadium; **original benches from the old stadium** to sit "where former club players once sat" (OFF 2023 → INF: the old dugout benches); a photocall. **In Nov 2026 it should show the working stadium, the unfinished third tier, the compression ring and cranes (INF from §4); not documented (O4).** | To the exit | OFF / INF |
| S10 | Exit | Not documented by OFF. Lead: through doors marked "Megastore" into the Barça Store. The store is reached via Access 9 (OFF). StadiumDB (Dec 2025): only the Barça Botiga stays inside the stadium, "integrated with VIP areas, the museum and locker rooms". | — | O7 |

---

## 3. The official plan or map

| Plan | URL | Readable? | Notes |
|---|---|---|---|
| **Barça Campus Map** (PDF, upload 28 Nov 2025) | https://www.fcbarcelona.com/fcbarcelona/document/2025/11/28/f9a46e94-ab9a-4f2f-ab43-4ca9f10844d4/MAPA_CAMP_NOU.pdf | **Text only**; the map is an image | Key: 1 Spotify Camp Nou, 2 Palau Blaugrana, 3 Masia de Can Planes, 4 Auditori 1899, 5 Seu Social-OAB, 6 Centre de Documentació, 7 Sala París. Icons for Museu, Botiga, Taquilles, Accés-Estadi/Campus/VIP, wheelchair access. Streets: Av. Joan XXIII, Carrer d'Elisabeth Eidenbenz. Unexplained letters and numbers (probably doors). **Lead: open in Chrome and record where the Museu icon is, which access is nearest, the Masia position and the Botiga.** |
| Campus map, 1C phase (PDF, 13 Mar 2026; also club-election polling layout) | https://www.fcbarcelona.com/fcbarcelona/document/2026/03/13/e60ba067-28bc-4685-9bac-98821659b15d/campus-1C-ok-DEF.pdf | Text only | Same key; adds Entrada/Sortida, Portes, Grada d'animació. **Lead: open in Chrome.** |
| Non-match-day access map (WEBP, 2 Oct 2026) | https://www.fcbarcelona.com/fcbarcelona/photo/2026/10/02/f13b23bd-66a2-4e21-91b3-c5b7430a1f13/1-Mapes__acces-no-partit-eng.webp | **FAILED** (server error) | **The newest official access map. Lead: open in Chrome; record Access 9 / 15 / 15A and where the Museum is.** |
| On-foot map (WEBP, Oct 2026) | https://www.fcbarcelona.com/fcbarcelona/photo/2026/10/02/5c93c681-6c12-4391-a70c-5038db31210b/2-Mapes_Peu-2-eng.webp | Not fetched | Lead |
| All-modes accessible map (WEBP, 8 Oct 2026) | https://www.fcbarcelona.com/fcbarcelona/photo/2026/10/08/30609f95-6551-491c-af2f-735d4bf034c8/10-Mapes__accessible_TotsMitjans-NoPartit-eng.webp | Not fetched | Lead |
| Old getting-there images (2023) | https://www.fcbarcelona.com/photo-resources/2023/06/23/297c4375-fcca-4224-929d-e692977a2ab2/MicrosoftTeams-image-23-.png · https://www.fcbarcelona.com/photo-resources/2023/06/15/b78b0989-de09-469e-8fc5-c301d878e7e0/getting-to-the-palau-map.png | First **FAILED** (client error); second not fetched | Historical only |
| Non-match-day access page | https://www.fcbarcelona.com/en/club/getting-here/spotify-camp-nou/non-match-day | Text read | Access 9 = Museum (§1.2) |
| Museum ticket pages (EN / ES) | https://www.fcbarcelona.com/en/tickets/camp-nou-experience/barca-museum-visits · https://www.fcbarcelona.es/es/entradas/camp-nou-experience/visitas-museo-barca | Text read | Official space names (§0.3). **Lead: also open the Catalan version for the CA names (O13).** |
| Ticket hub | https://www.fcbarcelona.com/en/tickets/museum | Text read | Products and inclusions |
| Barça Immersive Tour FAQ | https://support.fcbarcelona.com/faq/s/topic/0TO7S000000bsKIWAY/6bar%C3%A7a-immersive-tour?language=en_US | **BLOCKED** (permission prompt not answered) | **Lead: read in Chrome; it probably answers entrance, exit, lockers, photos and re-entry.** |
| **Museum room plan** | **None found.** No PDF, no app plan. Accessibility NGO: "orientation map in the lobby" | — | **Photograph the lobby map on site (O3).** |
| Barça app | Not searched. No source mentions a museum map in the app. | — | Lead: check the Culers/official app |

---

## 4. Stadium works state (dated)

| Date | Event | Grade |
|---|---|---|
| 28 May 2023 | Last match at the old Camp Nou (v Mallorca); the old museum (Tribuna area) closes | OFF |
| 6–7 Jun 2023 | Barça Immersive Tour opens in the former Palau de Gel next to the Palau Blaugrana | OFF |
| Oct 2023 | Construction Viewpoint ("Mirador 23-24") page and photos | OFF |
| 22 Nov 2025 | Return to Spotify Camp Nou, Barça 4–0 Athletic Club; Phase IB, max 45,401; 909 days away | OFF |
| 29 Dec 2025 | c. 45,000; 1C licence pending; third tier and roof to come; commercial boulevard moved outside, Barça Botiga inside | SEC (StadiumDB) |
| 27 Jan 2026 | Immersive Tour still "in the former Ice Rink"; 1,059,611 visitors in 2025; new museum "expected to reopen during 2026"; Spotify Camp Nou Experience (panorama) and Match Day Tour launched | OFF |
| **10 Mar 2026** | **Phase 1C licence: 62,652; Gol Nord opens; "Gol 1957" South Goal stand; Pitch Club and Main Hub (Grandstand), Mini Hub (Lateral)** | OFF |
| 7 May / 19 Jun 2026 | New museum "inside the future Spotify Camp Nou", first late summer, then Nov 2026, "sujeta a imponderables" | SEC (Crónica Global ×2) |
| 5 Jun 2026 | New provisional ice rink inaugurated (UB Campus Sud) | SEC |
| 23 Sep 2026 | c. 62,000; club expects to leave in May 2027 for the roof works (Montjuïc), return target Jan 2028; 105,000 finished | SEC (FGG citing The Athletic) |
| **5 Oct 2026** | **Last piece of the 830 m compression ring placed** | SEC (Ara, 10 Oct) |
| 7 Oct 2026 | Club aims to open the new museum and stadium-interior tours in Nov 2026; ~15-day museum closure for the move; museum works certificate expected from Limak c. 9 Oct | SEC (Ara) |
| **10 Oct 2026** | **Third tier will not open this season**; roof from summer 2027 (c. 18,000 seats removed, ring lifted from the pitch); phasing: museum and first-team dressing room first, then the main-stand noble area, then the third tier; "the museum will probably reopen next month" | SEC (Ara) |
| **14 Nov 2026** | Official ticket pages still sell the Immersive Tour + Construction Viewpoint; **no closure or move posted**; Match Day Tours 2 and 8 Dec | OFF |

**What the viewpoint will show in Nov 2026 (INF, from the above):** a bowl in use (first and second tiers, Gol Nord, Gol 1957), the unfinished third-tier ring, the closed compression ring at the top, cranes, no roof. On match days the pitch will have grass; at other times the state of the pitch is unknown. **Which side and which stands the balcony faces is not documented (O4).** The OFF copy's "demolition" language is out of date.

---

## 5. Proposed routes (start: the campus gate; end: the exit)

**Design rule.** The visit is a single fixed line: entrance hall → history and trophies → Messi → 360 room → models/viewpoint → exit. So the 30 / 60 / 90 versions differ by **depth per space plus outside tracks**, not by which rooms they visit. The OFF visit is "1h". **Honest length:** the ticketed interior honestly supports about **60–70 min** of listening and walking. A true **90 min** needs about 8 tracks of outside and approach material (campus, Palau Blaugrana, Masia, statues if present, the stadium exterior) plus 2–3 tracks per major room. Without that it would be padding. **Recommend stating the 90-min guide honestly as ≈ 80–90 min with 30–34 tracks** unless on-site material supports 36.

**Track budget.** 30 min ≈ 10–12 tracks; 60 min ≈ 20–24; 90 min ≈ 30–34 (user target 32–36).

### 30 min (11 tracks)
T00 welcome and safety (before the gate; no gate number until O1) → T01 the stadium from the campus (S0: the bowl, the cranes, no roof) → T02 the museum building (former ice rink, next to the Palau Blaugrana) → T03 trophies (S3) → T04 Cruyff and 1992 (S4) → T05 La Masia (S4) → T06 Messi (S5) → T07 before the 360 room (photosensitivity skip cue; S6) → T08 the models (S8) → T09 the viewpoint: what you are looking at (S9) → T10 exit and close (S10).

### 60 min (22 tracks)
The 30-min route plus: T-a the Palau Blaugrana and campus (outside) · T-b the founding story, 1899, as the history section opens (S4; find the 1899 object, O12) · T-c "Més que un club" and the Franco era (attributed, even-handed; S4) · T-d Kubala and the 1950s (S4, or at his statue if present, O9) · T-e the women's team (S3/S4) · T-f European Cup nights: Wembley 1992, Paris 2006, Rome 2009, Wembley 2011, Berlin 2015 (S3, 2 tracks) · T-g the jersey mosaic (S3) · T-h the 11 columns / current squads (S4) · T-i Messi part 2, the 2021 exit (S5) · T-j the old stadium, 1957 (S9, sitting on the old benches) · T-k the new stadium in phases (S9).

### 90 min (32 tracks)
The 60-min route plus: the approach from the Metro (1) · the Masia de Can Planes as seen from the route, if visible (O10) (1) · the Cruyff and Kubala statues, if present (O9) (1–2) · Gamper and the founders (1) · Les Corts 1922–57 (1) · Dream Team players (1) · Guardiola 2008–12 (1) · women's 2021–24 (1) · the Ballon d'Or table (1) · the 360 show's after-track (1) · the roof and third tier explained at the viewpoint (1) · Montjuïc and the 2027–28 move (1).

### On-site decisions
| ID | Question | ALT options |
|---|---|---|
| **O1** | Which **gate** do Museum ticket holders use: **Access 9 (Av. Joan XXIII)** or **Access 15 (Arístides Maillol)**? Where is the museum door, and what is written on it? Is there a security check? Where are the ticket booths? | ALT-A: Access 9 → campus walk past the Barça Store. ALT-B: Access 15 → museum to your left (old guide). Until settled: "follow the Museum signs". |
| **O2** | **Is the Immersive Tour still open on the visit date, or has the new in-stadium museum opened (or is the ~15-day move closure on)?** Check the OFF ticket page and news the day before. | If the new museum is open: **stop**, re-research §2 and §5 (new rooms, new door, likely inside the main stand). |
| **O3** | Real room order and names; how many rooms; floor arrows; one-way or free? Photograph the **lobby orientation map**. | Until read: landmark cues only ("the room with the golden boots"). |
| **O4** | **Viewpoint**: where is it (stairs, lift), which side of the stadium and which stands does it face, what is visible today (third tier, ring, cranes, pitch)? Are the old benches and screens still there? Is it closed on match days or in bad weather? | If closed: replace with the models track. |
| **O5** | Is the **Espai Barça model** still on show, and is it before or after the viewpoint? | Move T08 accordingly. |
| **O6** | The official audio guide: languages (3 or 14), numbered stops? | If numbered, cue ours to the same numbers. |
| **O7** | **Exit**: through the Barça Store? Onto which street or gate? Any exit that skips the shop? | ALT: end the last track at the viewpoint. |
| **O8** | Match days: earlier closing, crowds, closed gates; any change to the route. | Add a match-day note to T00. |
| **O9** | Are the **Kubala and Cruyff statues** in place? Where? Visible from the route? | Drop the statue tracks if they are absent. |
| **O10** | Are the **Masia de Can Planes**, the **Palau Blaugrana** and the "**Rambla del Barça**" visible from the route? From where? | Context-only tracks if not visible. |
| **O11** | 360 room: photo rules, show length, where the strobe warning is posted; can visitors walk past it? | Skip cue in T07. |
| **O12** | Where is the club's founding material (Gamper, 1899), Cruyff's space, the women's-team section, the jersey mosaic? | Topic-keyed tracks. |
| **O13** | Catalan official names of the spaces (read the CA ticket page in Chrome). | — |

---

## 6. Outside, within the visit or on the way in

| Item | Status Nov 2026 | Grade |
|---|---|---|
| Spotify Camp Nou exterior | In use; third tier and roof unfinished; cranes (§4) | OFF / SEC |
| Palau Blaugrana | Stands next to the museum building (former ice rink) | OFF |
| Masia de Can Planes | On the campus map (key 3); position relative to the route unread | OFF (map text) |
| Kubala statue (2009) and Cruyff statue (2019, 3.5 m, bronze) | Historically on the Tribuna forecourt, side by side; **2026 position not documented** | OFF 2019 / SEC |
| Messi statue | **Does not exist** (planned; no design or date, Nov 2025) | SEC |
| Plaques | None found | — |
| Columbarium/memorial | Gol Nord, level 20, gate 35 (separate project; not on our ticket) | SEC |
| Rambla del Barça | Rest area and fountains (OFF); location unknown | OFF |

---

## 7. The user's old guide vs Nov 2026 (requested by the lead)

| Old-guide space | Still on the Museum ticket, Nov 2026? | Where |
|---|---|---|
| Entrance "the former ice rink on Carrer d'Arístides Maillol" | **Building: yes** (OFF, 27 Jan 2026 and live ticket page). **Street/gate: CONFLICT.** The Oct 2026 OFF access page sends Museum visitors to Access 9, Av. Joan XXIII. | Former Palau de Gel, next to the Palau Blaugrana (O1) |
| "Barça Immersive Tour" | **Yes**, still the official name on 14 Nov 2026 (H1 of the ticket page) | Same building. **May be replaced by the new museum in late 2026 (O2).** |
| "360 Degree Room" | **Yes**: officially "Macro Sala 360° / 360° Macro Room", show "Spotify Camp Nou Live" | Last museum room before the viewpoint |
| "Construction Viewpoint" (Mirador de las Obras) | **Yes**, on the ticket | The last stop, reached from the old museum entrance area (main-stand side, INF). What it shows has changed: a working stadium, not a demolition site. |
| "The Model" (scale model of the finished stadium) | **Probably**: the OFF ticket text still lists "models and audiovisual pieces" under the Construction Viewpoint, but that text is from 2023 (O5) | Next to the viewpoint |
| Exit through the megastore | **Not confirmed** by OFF (O7) | — |
| "Eighteen rooms" | Partly supported: "18 interactive and audiovisual installations" (SEC blog, Aug 2026); "10 exhibition rooms" (SEC-WEAK) | — |
| "Stadium itself is closed" | **Outdated.** The stadium reopened on 22 Nov 2025, but not on our ticket. | — |

---

## 8. What I could NOT find or verify
1. The date of the new in-stadium museum and where it is inside the stadium. Whether the Immersive Tour closes in Nov/Dec 2026.
2. The Museum gate (9 or 15) and the exact door; security; whether the exit is through the store.
3. Any official room plan; the room order beyond the 4 OFF names; the Catalan names.
4. The viewpoint's position, its access (stairs or lift) and its view in Nov 2026.
5. The Kubala and Cruyff statues' 2026 position; the Masia's visibility from the route.
6. Founding documents / 1899 material in the current display.
7. The FAQ page (blocked); all map images (failed or image-only).


## Appendix A. Raw graded notes (in fetch order)

### A.1 Official ticket and practical pages (fetched 14 Nov 2026)
- OFF `fcbarcelona.com/en/tickets/museum` (14 Nov 2026): products: Museum; Museum Flexible ("Valid until 02/28/2027"); Barçabus Experience; Players Experience - Training City; Match Day Tour Spotify Camp Nou (next sessions "12/02 (Atlético de Madrid) | 12/08 (Manchester City)"); Total Experience Museum (adds "Robokeeper 3 goals" and "Barça Virtual Dream"); Spotify Camp Nou Experience ("Panoramic view at Spotify Camp Nou"; sessions CA/ES/EN); Barça Sky Tour. **Museum ticket = "Museum + Digital Audio Guide" + "Construction Viewpoint".** Match Day Tour includes "Walk on the pitch". The page still uses "Barça Immersive Tour" in its planning/FAQ sections. No entrance, route, map.
- OFF `.../camp-nou-experience/plan-your-visit` (Activities subpage; undated; construction-viewpoint image path 2026/08/20; tracking "26-27"): Barça Virtual Dream (VR); Construction Viewpoint ("Visitors can witness the transformation of FC Barcelona's iconic stadium in real time"); Robokeeper. No logistics.
- OFF `.../new-spotify-camp-nou-construction-viewpoint` (undated; gallery labelled "Mirador 23-24" → **page written 2023-24, possibly stale**): "you'll conclude the tour at the Spotify Camp Nou Construction Viewpoint"; reached "from what used to be the entrance to the old museum"; balcony to watch the works "day by day"; screens with "an internal view of the stadium in its current state of construction"; **original benches from the old stadium** to sit on; **photo booth**. Calls it part of the new museum's "BARÇA IMMERSIVE TOUR".
- OFF `.../camp-nou-experience/practical-information` (undated; car-park notice "from 1 June 2023"): address "C/ Arístides Mallol s/n (Main Access No. 15) or Av- De Joan XVIII [sic] (Boulevard Access: No. 9), 08028 Barcelona"; pedestrian: **Access 9 on Av. de Joan XXIII, Access 15 on Av. Arístides Maillol**. "The duration of the visit is 1h." Last access 45 min before closing (OPS ONLY). Ticket booths open 15 min before the start of the "Barça Inmersive [sic] Tour". Maps (images, 2023): `photo-resources/2023/06/15/b78b0989-.../getting-to-the-palau-map.png`; `photo-resources/2023/06/23/297c4375-.../MicrosoftTeams-image-23-.png`.

### A.0 The user's old guide (lead only; USER_DECISIONS says "start fresh")
- `/home/claude/audioq/campnou_v5/source/old_guide.txt` (11 tracks, ~70 min; written for the closed-stadium period): entrance "the former ice rink on Carrer d'Arístides Maillol, not the main stadium gate"; "the low building marked Barça Immersive Tour or FCB Museum. It used to be the Palau de Gel"; "Not the megastore door, which is the exit". Sequence: entry video room (curved screen) → trophy gallery → Cruyff → La Masia gallery → circular Messi room (Ballons d'Or) → "360 Degree Room" (strobe warning) → door "Mirador de las Obras" → stairs up to a wooden viewing deck → architectural gallery with a large illuminated scale **Model** of the finished stadium/Espai Barça → doors "Megastore" → exit through the megastore. Claims "Eighteen rooms". **Every claim to be checked against 2026 sources (see §0, §2).**

### A.2 Where the museum is: ice rink vs new museum (fetched 14 Nov 2026)
- OFF news `fcbarcelona.es/es/noticias/3828009/explorando-espacios-el-nuevo-museo` (18 Dec 2023): the museum occupies "los 2.400m2 de la antigua pista de hielo"; "Museo 100% interactivo"; ends in **SPOTIFY CAMP NOU LIVE**, "Un show inmersivo" in 360º; the Barça Immersive Tour then leads into the Espai Barça display (architectural project with **models and audiovisual pieces**) and the construction viewpoint.
- SEC (press, NHL.com/es, 14 Sep 2026): the Palau de Gel "cerró sus puertas" in 2022 and the building "pasó a utilizarse temporalmente para acoger el museo del FC Barcelona"; a **new provisional ice rink** on UB land (Campus Sud) opened May 2026, inaugurated 5 Jun 2026. Says nothing on whether the museum is still in the old building.
- OFF news `fcbarcelona.com/en/club/news/4440134/...` (27 Jan 2026): the Barça Immersive Tour, a "temporary exhibition", is "located in the former Ice Rink"; 1,059,611 visitors in 2025; opened May 2023; matches have returned to Spotify Camp Nou; new products: Ciutat Esportiva tours, Barça Sky Tour; **a fully renovated new Barça Museum "expected to reopen during 2026"** (no date, no location).
- SEC (press, Ara en Castellano, Martí Molina, 7 Oct 2026): club aims to open the **new museum in November 2026** and restart stadium-interior tours; "La decisión final está en manos de los técnicos"; the move of the collection takes **about 15 days with no visitors admitted**; the provisional museum (Barça Immersive Tour, ice rink) closes for those ~2 weeks; new museum 2,800 m², designed by **Mediapro Exhibitions**, history, shirts, trophies, immersive experience; old museum was in the tribuna area of the old Camp Nou; Limak's certificate of final works for the museum expected "este viernes" (= 9 Oct 2026); planned tour route through stand, palco and dressing rooms; interior visits so far only on match days (security); "gran auge" of visitors not until "se haya instalado la cubierta y la tercera grada esté disponible" (roof and third tier not complete, Oct 2026).
- OFF ticket page `fcbarcelona.com/en/tickets/camp-nou-experience/barca-museum-visits` (live 14 Nov 2026; image paths 2025/03/26 and 2026/08/18; Museum Flexible "Valid until 02/28/2027"): H1 "Barça Immersive Tour"; "BARÇA MUSEUM - BARÇA INMERSIVE TOUR"; "As Spotify Camp Nou is being transformed, the FC Barcelona Museum has temporarily moved to a spectacular 2,400 m² space." **Spaces in page order:** (1) "FC Barcelona Museum Trophies" ("All the Champions League titles, La Liga titles, and other accolades"); (2) "Barça History" ("the history of all our teams and their most memorable milestones"); (3) "Messi Zone" ("his Ballon d'Or awards and Golden Boots"); (4) "360° Macro Room"; (5) RoboKeeper Challenge (extra); (6) Barça Virtual Dream (VR, extra); (7) "Mirador de las Obras". Audio guide = "Digital Audio Guide" (Museum and Total Experience tickets); languages not stated. **No closure/move notice on 14 Nov 2026.**
- OFF news 3530980 (6 Jun 2023): Immersive Tour in "the building that used to house the Palau de Gel, next to the Palau Blaugrana"; c. 2,400 m² "split into different areas"; "the largest immersive room in a sports museum in Europe"; developed by Mediapro Exhibitions; opened to the public 7 Jun 2023; to run until the new museum at the future Spotify Camp Nou opens (then planned for 2024/25 — slipped). The 2nd Women's Champions League trophy placed in a cabinet at the opening.
- OFF news 3447515 (21 May 2023): temporary museum "where, until a few months ago, the Club's Ice Rink was located", "next to the Palau Blaugrana"; circular main space, projections on walls **6 m high and 78 m long**; a closing audiovisual space using VR to evoke the new stadium; old museum's last day 28 May 2023.

### A.3 Stadium works state (fetched 14 Nov 2026)
- SEC (press, Ara en Castellano, Martí Molina, 10 Oct 2026, "Cuenta atrás para que la lluvia deje de ser un problema en el Camp Nou"): stadium back in use "for almost a year" at **c. 60 % capacity**; last piece of the **830 m compression ring** placed on Mon 5 Oct 2026; **roof to be installed "from next summer"** (2027), tensegrity system; c. **18,000 first/second-tier seats** to be removed first, the ring assembled on the pitch and lifted (4–5 months; membrane 6–9 months, can be fitted during matches); roof contract reportedly 99 % awarded to Limak. **Third tier will NOT open this season** (originally Aug 2026, then Q1 2027; now next season); side-only opening in Mar/Apr considered and rejected. **Phasing: first the museum and the first-team dressing room, then the noble area of the lateral (main stand), finally the whole third tier.** "Return to the stadium" (in context: the completed stadium) planned Jan 2028 rather than Nov 2027 [AMBIGUOUS wording in the extraction — VERIFY]; 2027-28 budget assumes 92,000 spectators vs 104,000 finished; press/security booths in the second tier until summer 2028; 2029 Champions League final. **"The museum will probably reopen next month"** (= Nov 2026); interior tours can continue during the roof works.
- OFF ticket page `fcbarcelona.com/en/tickets/camp-nou-experience/3044593/museum` ("Published date 02 Feb 23", still linked from the live ticket page): Museum ticket = "Museum + Digital Audio Guide" + "Construction Viewpoint" = "a full exhibition on the architectural project for the future Espai Barça, with models and audiovisual pieces"; ends with the 360º "SPOTIFY CAMP NOU LIVE" show; 2,400 m², "100% interactive"; route through past, present and future, finishing in the large immersive space. **Audio-guide languages: CA, ES, EN, FR, DE, IT, PT, NL, JA, ZH, AR, KO, RU, PL** (14). Accessibility: "fully adapted for people with reduced mobility and wheelchair users"; accessible audio guide, adapted toilets, assistance dogs, induction loop, baby changing. **Immersive room "not recommended for people with epilepsy or photosensitivity".** Under-4s collect a free ticket at the ticket office.
- SEC (press, Crónica Global/Culemanía, 19 Jun 2026): new museum expected **November 2026**, "queda sujeta a imponderables"; location not given; separate project: **columbarium/memorial on level 20 of the Gol Nord, gate 35** (Eternal Sports Memorial). Immersive Tour = Mediapro Exhibitions.

### A.4 Access points (fetched 14 Nov 2026)
- OFF `fcbarcelona.com/en/club/getting-here/spotify-camp-nou/non-match-day` (no page date; map images uploaded **2–8 Oct 2026**): **Access point 9: Av. Joan XXIII** (towards Av. Diagonal, c. Martí i Franquès, Av. Doctor Gregorio Marañón) — "Most direct access to the Museum, the Official Store..."; **Access point 15: carrer Arístides Maillol** → OAB, **Spotify Camp Nou Experience**, Gastrobar Cal Blay; **Access point 15A: Travessera de les Corts** → Spotify Camp Nou Experience, OAB. Museum and Barça Store both via Access 9. Hours and access "may vary" with Espai Barça works. Metro: L3 Palau Reial, Les Corts, Zona Universitària, Maria Cristina; L5 Collblanc, Badal, Ernest Lluch; L9S/L10 Collblanc; L9S Zona Universitària. Tram T1–T3: Av. de Xile, Palau Reial, Ernest Lluch, Pius XII, Zona Universitària, Maria Cristina. Coach area c. Martí i Franquès; taxi rank Joan XXIII / Martí i Franquès; accessible parking mainly Martí i Franquès. Map images (WEBP, Oct 2026): access points `fcbarcelona.com/fcbarcelona/photo/2026/10/02/f13b23bd-66a2-4e21-91b3-c5b7430a1f13/1-Mapes__acces-no-partit-eng.webp`; on foot `.../2026/10/02/5c93c681-6c12-4391-a70c-5038db31210b/2-Mapes_Peu-2-eng.webp`; metro `.../2026/10/02/a9053ccc-cf0f-4d96-a542-f1621200ca1b/4-Mapes__metro-2-eng.webp`; all modes accessible `.../2026/10/08/30609f95-6551-491c-af2f-735d4bf034c8/10-Mapes__accessible_TotsMitjans-NoPartit-eng.webp`.
- **CONFLICT:** the older practical-information page (2023 text) calls Arístides Maillol "Main Access No. 15"; the old guide says the entrance is "off Carrer d'Arístides Maillol". The Oct 2026 non-match-day page puts the Museum at **Access 9, Av. Joan XXIII**. Prefer the Oct 2026 page (OFF, newer) but **verify on site (O1)**.
- OFF news 4440096 "Spotify Camp Nou tours are back" (27 Jan 2026): **Spotify Camp Nou Experience** = Museum access + "panoramic view" of the stadium, which "reopened last November"; includes "a section with many stairs", not wheelchair-accessible (designated wheelchair viewing area). **Match Day Tour** (matchdays only): pitch walk, VIP areas, press room, interview zone, presidential box + flexible Museum entry. (Both OUT OF SCOPE for our Museum-ticket guide.)
- OFF news 4407735 (23 Nov 2025): first match back **Sat 22 Nov 2025, Barça 4–0 Athletic Club**; 45,157 attendance; Phase IB licence "maximum attendance of 45,401"; **909 days** away (last match 28 May 2023 v Mallorca).
- SEC (StadiumDB, 29 Dec 2025): c. 45,000; 1C licence submitted → c. 62,000 with **Gol Nord** and the full first and second tiers; third tier and roof still to come; the internal commercial boulevard moved outside; only the Barça Botiga stays inside, "integrated with VIP areas, the museum and locker rooms"; main-stand fans pass the Botiga.
- SEC (Football Ground Guide, 23 Sep 2026, citing The Athletic / VP Ferran Olive): capacity c. **62,000** (Sep 2026); third tier to "progressively reopen from early 2027" **[CONFLICTS with Ara 10 Oct 2026: not this season — prefer the newer Ara]**; club "expect to leave Camp Nou in May 2027" for the roof lift (materials on the pitch), playing at the Estadi Olímpic Lluís Companys for about half of 2027-28, return target **Jan 2028**; 105,000 finished; fully operational 2028-29. (This explains Ara's "return to the stadium … Jan 2028".)
- OFF ticket page `.../barca-tours/4418722/spotify-camp-nou-experience` (undated): (OUT OF SCOPE product) "Panoramic view at Spotify Camp Nou" + guided (CA/ES/EN) + "Flexible Museum Ticket + audio-guide"; meet at **"Access 15, 15 minutes before the visit"**; panoramic view on the **first tier** ("go down just before the supporters' section and sit in the seats"); "return to the entry point along the same path"; late arrivals "will be able to visit the Barça Immersive Tour Museum". → Access 15 (Arístides Maillol) is the **stadium-tour** start, not the Museum's (INF, consistent with the non-match-day page).
- OFF `fcbarcelona.com/en/club/accessibility-facilities/camp-nou-experience` (undated): Barça Immersive Tour: "The entrance is flat, without any difficulties for access"; "fully accessible"; 2 free wheelchairs from the **entrance information desk**; **audio guide on the visitor's own phone via a QR code on a card at the entrance, "Bring headphones"**, all sounds transcribed in a scrollable window; languages here CA/ES/EN + **Catalan Sign Language (LSC)** [CONFLICT with the 14-language list on the ticket page — VERIFY, O6]; portable induction loop from the desk; "Spotify Camp Nou 360" immersive room "not recommended" for epilepsy/photosensitivity — tell staff; "Lighting throughout the tour is subdued"; tactile QR codes; noise-cancelling headphones on free loan; adapted toilets with baby changing; **rest area and drinking fountains on "Rambla del Barça"**. Quiet Hours Saturdays 15:00–17:00 (OPS ONLY). No lifts/stairs/levels/exit/viewpoint info.

### A.5 Visitor-facing secondary pages and the outside (fetched 14 Nov 2026)
- SEC-WEAK (aggregator blog, thebettervacation.com/barcelona/camp-nou-tour, upd. 2 Apr 2026; the Bernabéu file flags this site as often stale): "Tour entrance is between Barça Café and Barça Store Camp Nou"; address "C/ d'Arístides Maillol, 12, 08028" (= the stadium's postal address, not necessarily the door); "10 exhibition rooms" 1899–today; Trophy Gallery, Messi Zone ("three Golden Boots", Ballons d'Or, goals reel), **Values Section** ("Més que un club", Catalan identity), **Joan Miró lithograph**, **La Masia** tribute, interactive walls, **Spotify Camp Nou Live Room**; viewpoint shows "the new third tier and the foundations for the future roof" [roof wording dubious]; audio guide 12 languages. Lead only.
- OFF news 1326899 (26 Aug 2019): **Cruyff statue**, bronze, 3.5 m, 1,500 kg, by Corry Ammerlaan-van Niekerk; on "the Camp Nou forecourt" at the **grandstand (tribuna) entrance**, "close to the one of Ladislau Kubala"; No. 9 on his back, outstretched arm (1970s pose).
- SEC (futbolretro.es, upd. 27 Apr 2023): **Kubala statue**, bronze c. 2 m, unveiled 2009, popular subscription started by the Agrupació (veterans); on the esplanade giving access to the tribuna; Cruyff's very close by. Nothing on the works.
- SEC (StadiumDB, 16 Nov 2025): Laporta: Messi statue "we are working on it"; no design, no date; would stand on the grounds of the new stadium; family consent needed. Old Camp Nou had the Kubala and Cruyff statues — **current whereabouts not stated.** → **No Messi statue exists (Nov 2026 as far as found). Kubala/Cruyff: current position during works UNVERIFIED (O9).**

### A.6 Official maps (fetched 14 Nov 2026)
- OFF PDF `fcbarcelona.com/fcbarcelona/document/2025/11/28/f9a46e94-ab9a-4f2f-ab43-4ca9f10844d4/MAPA_CAMP_NOU.pdf` (upload 28 Nov 2025): "BARÇA CAMPUS MAP"; streets labelled **Carrer d'Elisabeth Eidenbenz** and **Av. Joan XXIII**; key 1 Spotify Camp Nou, 2 Palau Blaugrana, 3 **Masia de Can Planes**, 4 Auditori 1899, 5 Seu Social-OAB, 6 Centre de Documentació, 7 Sala París; icons: Accés-Campus, Accés-Estadi, Accés VIP-Estadi, Accés Preferent Cadira de Rodes, Centre d'Acreditacions, Taquilles, Botiga, **Museu**, Serveis, Restauració; "T'ACOMPANYEM"; unexplained letters (G, Y, X, H, U, Q, D, V, F, W, K) and numbers (7E, 12–23) = probably access/door numbers. **Text extractable, positions NOT (image map). Lead: open in Chrome.**
- OFF PDF `fcbarcelona.com/fcbarcelona/document/2026/03/13/e60ba067-28bc-4685-9bac-98821659b15d/campus-1C-ok-DEF.pdf` (upload 13 Mar 2026; "1C" = the 1C licence phase; also a polling-station layout, so probably the club-elections map): same key 1–7; numbers 8–23 and letters unexplained; legend adds Portes, Sortida, Entrada, Grada d'animació, Zona afició visitant, Punts d'informació. **Positions NOT readable. Lead: open in Chrome.**
- SEC (blog, barcelonaurbana.com, Reinel González, 21 Aug 2026): main address Arístides Maillol 12; "Main door is access 15"; Access 9 on Av. de Joan XXIII [does not say which the Museum uses]; Metro Palau Reial / Les Corts (L3), Collblanc / Badal (L5), 10–15 min walk; works "han eliminado el acceso en vehículo privado"; Immersive Tour "in an adapted space next to the stadium" with **18 interactive and audiovisual installations, a 360-degree audiovisual, and a tunnel dedicated to the men's and women's teams**; viewpoint = "un punto de observación sobre una obra activa", "No es una grada ni un balcón sobre el césped"; photo caption: cranes over the upper ring.
- SEC-reseller (thetourguy.com, guided Immersive Tour, undated, says renovation done "August 2026" → stale): meet at **"Access 15 of Camp Nou, Carrer Aristides Maillol, 4"**, ends back there; order: museum entrance → trophies and shirts (Messi, Cruyff) → Catalan identity / "Més que un club" → 360º "Spotify Camp Nou Live" → Espai Barça construction exhibition ("Detailed models and videos"); 1 h; "wheelchair accessible".
- SEC-reseller (barcelona-tickets.com plan-your-visit, © 2014–2026): accesses 9 (Joan XXIII), 15 (Arístides Maillol), 15A and 18 (Travessera de les Corts); cloakroom for luggage and pushchairs; durations "1 hr – 2 hrs 10 mins".
- OFF news `fcbarcelona.es/es/noticias/4128584/...` (24 Sep 2024, "Cuarenta años de historia del Museo"): museum opened **24 Sep 1984** (Núñez presidency; idea from 1928 under Arcadi Balaguer), designed by Josep Casals and Francesc Pulido, "la zona de la Tribuna del Camp Nou"; 950 m² → 1,650 (1994) → 2,700 (1997–98) → 3,600 m² (2010, "Camp Nou Experience"); closed in the stadium 28 May 2023; reopened provisionally 6 Jun 2023 [news 3530980 says public opening 7 Jun] in the former ice rink next to the Palau Blaugrana, c. 2,400 m²; >100 football trophies, 25 women's-football trophies, 50 from other sections; peña gifts; art collection.
- SEC-access (Apropa Cultura accessible-culture PDF, `apropacultura.org/sites/default/files/museu_del_fc_barcelona_nou_cast.pdf`, undated, post-2023): address Arístides Maillol s/n; on foot **Access 9 (Av. Joan XXIII), Access 12 and 15 (Arístides Maillol)**; visit c. 45 min; former ice rink; section of models and audiovisuals of the new stadium; ends in the **Spotify Camp Nou Live** space ("como si estuvieras en el centro del estadio"); **adapted lifts**, accessible toilets, pictogram signage, **"orientation map in the lobby"**, rest areas; multimedia audio guide on own phone/tablet (bring headphones).
- SEC (press, Crónica Global, Oriol Solé Vicente, 7 May 2026): new ice rink at Carles Ferrer Salat 7 (UB land, next to Masia de Can Rigalt); **new museum "inside the future Spotify Camp Nou"**, then planned for late summer 2026, to replace the Immersive Tour "in the former Palau de Gel"; to open 365 days; part of the stadium not given; new Palau Blaugrana on the former Miniestadi site, works from 2028, c. 2030 (not yet started → **the current Palau Blaugrana still stands**).
- SEC (Catalan News, 6 Jun 2023 — **opening-day content, may have changed**): zones named: 'Masia' training-academy zone; **legends** (Messi "his several Ballon d'Or", Cruyff/Dream Team); women's team special place (UWCL 3 Jun 2023); **interactive room with "11 columns"**, one per main men's/women's player (info, trophies, moments, Spotify playlist); **immersive circular space**, 10-min show with deepfake/AI, "four-meter tall holograms" (Ronaldinho, Messi, Iniesta, Cruyff, Putellas, Pedri); **"Camp Nou future" projection-mapping** area; **mosaic of 200 jerseys** + dozens of trophies incl. five men's Champions League; **VR experience as last stop** (30–40 people). Visit 45–60 min.
- SEC (digitalavmagazine, 7 Jun 2023): location "Next to the Palau Blaugrana, in the building that formerly housed the Palau de Gel"; "divided into different areas"; immersive room "considered the largest in Europe in a sports museum".
- OFF `fcbarcelona.es/es/entradas/camp-nou-experience/mirador-obras-nuevo-spotify-camp-nou` (images 3 and 31 Oct 2023; gallery "Mirador 23-24"): Mirador is "the final stop of the new museum visit"; "terminaréis la visita en el Mirador de las Obras el Spotify Camp Nou"; reached "from what used to be the entrance of the old museum" (= the old museum was in the Tribuna area, OFF 4128584 → INF: **the Mirador is on the main-stand (Tribuna) side of the stadium, at/near the old museum door**); balcony; screens with an inside view "en su estado actual de construcción" (written for the demolition era); **"the original benches from the old stadium, so visitors can sit where former club players once sat"** (= old dugout benches, INF); photocall. **2023 text; what the balcony shows in Nov 2026 is NOT documented by OFF (O4).**
- SEC-WEAK (artvisitguide.com, "Last verified" May 2026; no visit stated): museum c. 45 min; total 60–90 min; viewpoint 5–10 min, shows partly dismantled upper tiers / structural frame / cranes [generic, possibly stale]; Ballon d'Or section; original match kits; 1899–present timeline.
- SEC-review (headout reviews, latest early 2025): "virtual stadium with surround sound" (Feb 2024); viewer "wouldn't see ANYTHING" of the stadium (Jan 2024); film at the end then goal kicking (Oct 2023); "Even the shop was impressive" (Oct 2023); "considerable walk" to get there.
- OFF `fcbarcelona.com/en/tickets/camp-nou-experience/timetable` (fetched 14 Nov 2026; year not printed): exceptions **17 Nov open until 17:00; 22 Nov until 14:00; 2 Dec until 21:30; 8 Dec until 15:00** (2 Dec and 8 Dec = Match Day Tour dates v Atlético and Man City on the ticket page → **match days change Museum closing times; INF: 22 Nov and 17 Nov likewise event days**); closed 25 Dec and 1 Jan; visit "about one hour". OPS ONLY. **No closure for a museum move is posted as of 14 Nov 2026.**
- OFF-AJ (city listing agenda500.barcelona.cat "Museu Barça Immersive Tour", undated): address "Carrer d'Arístides Maillol, 12*18", Les Corts (la Maternitat i Sant Ramon); "Museu temporal fins que estigui inaugurat el nou Museu del futur Spotify Camp Nou, la temporada 2024/25" (stale date); "Due to the works at the Spotify Camp Nou the tickets do not include a tour of the interior of the stadium."
- OFF `.../practical-information/getting-to-the-camp-nou` (2023 text; image paths 2023–2024): repeats "Main Access No. 15" Arístides Maillol / "Boulevard Access: No. 9" Joan XXIII. Map images FAILED (see App. B).
- OFF statement 4465846 (10 Mar 2026): Phase **1C** first-occupancy licence → **62,652**; **Gol Nord opened**; VIP spaces between the first and second tiers (**Pitch Club and Main Hub in the Grandstand [Tribuna]; Mini Hub in the Lateral**); South Goal supporters' stand "**Gol 1957**" activated.

## Appendix B. Fetch log (14 Nov 2026; one page at a time; no retries)

| # | URL | Result |
|---|---|---|
| 1 | https://www.fcbarcelona.com/en/tickets/museum | OK |
| 2 | https://www.fcbarcelona.com/en/tickets/camp-nou-experience/plan-your-visit | OK (activities only) |
| 3 | https://www.fcbarcelona.com/en/tickets/camp-nou-experience/new-spotify-camp-nou-construction-viewpoint | OK (2023 text) |
| 4 | https://www.fcbarcelona.com/en/tickets/camp-nou-experience/practical-information | OK (2023 text) |
| 5 | https://www.fcbarcelona.es/es/noticias/3828009/explorando-espacios-el-nuevo-museo | OK (Dec 2023) |
| 6 | https://www.nhl.com/es/news/el-barca-reestrena-su-pista-de-hielo | OK |
| 7 | https://www.fcbarcelona.com/en/club/news/4440134/barca-museum-reaches-one-million-visitors-again-in-year-of-return-to-spotify-camp-nou | OK |
| 8 | https://es.ara.cat/deportes/fc-barcelona/turistas-visitan-camp-nou-tendran-alegria-noviembre_1_5872320.html | OK |
| 9 | https://www.fcbarcelona.com/en/tickets/camp-nou-experience/barca-museum-visits | OK |
| 10 | https://www.fcbarcelona.com/en/news/3530980/fc-barcelona-inaugurates-the-barca-immersive-tour-featuring-the-largest-immersive-room-in-a-sports-museum-in-europe | OK |
| 11 | https://www.fcbarcelona.com/en/news/3447515/fc-barcelona-museum-temporary-change-of-location | OK |
| 12 | https://es.ara.cat/deportes/fc-barcelona/cuenta-lluvia-deje-problema-camp-nou_1_5875274.html | OK |
| 13 | https://cronicaglobal.elespanol.com/culemania/palco/20260619/espai-barca-abrira-fuentes-ingresos-museo-columbario/1003742772718_0.html | OK |
| 14 | https://www.fcbarcelona.com/en/tickets/camp-nou-experience/3044593/museum | OK |
| 15 | https://support.fcbarcelona.com/faq/s/topic/0TO7S000000bsKIWAY/6bar%C3%A7a-immersive-tour?language=en_US | **BLOCKED** (permission prompt not answered; not retried) |
| 16 | https://www.fcbarcelona.com/en/club/getting-here/spotify-camp-nou/ | OK (navigation only) |
| 17 | https://www.fcbarcelona.com/en/club/getting-here/spotify-camp-nou/non-match-day | OK |
| 18 | https://www.fcbarcelona.com/fcbarcelona/photo/2026/10/02/f13b23bd-66a2-4e21-91b3-c5b7430a1f13/1-Mapes__acces-no-partit-eng.webp | **FAILED** (server error) |
| 19 | https://www.fcbarcelona.com/en/news/4440096/spotify-camp-nou-tours-are-back | OK |
| 20 | https://www.fcbarcelona.com/en/news/4407735/first-game-back-at-spotify-camp-nou-in-figures | OK |
| 21 | https://footballgroundguide.com/news/barcelona-to-leave-camp-nou-again-as-major-redevelopment-decision-now-revealed-amid-2-2bn-debts.html | OK |
| 22 | https://stadiumdb.com/news/2025/12/spain_fc_barcelona_ready_for_62000_fans_camp_nou_step_by_step_toward_full_capacity | OK |
| 23 | https://www.fcbarcelona.com/en/tickets/camp-nou-experience/barca-tours/4418722/spotify-camp-nou-experience | OK |
| 24 | https://www.fcbarcelona.com/en/club/accessibility-facilities/camp-nou-experience | OK |
| 25 | https://thebettervacation.com/barcelona/camp-nou-tour/ | OK (SEC-WEAK) |
| 26 | https://futbolretro.es/en/the-statues-of-the-soccer-players-that-can-be-seen-in-the-camp-nou/ | OK |
| 27 | https://stadiumdb.com/news/2025/11/spain_laporta_wants_messi_statue_at_new_camp_nou | OK |
| 28 | https://www.fcbarcelona.com/en/club/news/1326899/johan-cruyff-statue-unveiled-at-camp-nou | OK |
| 29 | https://www.barcelona-tickets.com/camp-nou-tour/plan-your-visit-camp-nou | OK (reseller) |
| 30 | https://thetourguy.com/tours/barcelona/barca-immersive-tour-museum-guided | OK (reseller) |
| 31 | https://www.fcbarcelona.com/fcbarcelona/document/2025/11/28/f9a46e94-ab9a-4f2f-ab43-4ca9f10844d4/MAPA_CAMP_NOU.pdf | Text only (image map) |
| 32 | https://www.fcbarcelona.com/fcbarcelona/document/2026/03/13/e60ba067-28bc-4685-9bac-98821659b15d/campus-1C-ok-DEF.pdf | Text only (image map) |
| 33 | https://barcelonaurbana.com/blog/visitar-camp-nou-durante-obras | OK |
| 34 | https://www.fcbarcelona.es/es/noticias/4128584/cuarenta-anos-de-historia-del-museo-del-fc-barcelona/amp | OK |
| 35 | https://www.apropacultura.org/sites/default/files/museu_del_fc_barcelona_nou_cast.pdf | OK |
| 36 | https://cronicaglobal.elespanol.com/culemania/palco/20260507/espai-barca-senales-acompanan-spotify-camp-nou/1003742758869_0.html | OK |
| 37 | https://www.digitalavmagazine.com/en/2023/06/07/el-fc-barcelona-inaugura-su-nuevo-espacio-expositivo-que-incluye-una-gran-sala-inmersiva | OK |
| 38 | https://www.catalannews.com/sports/item/barca-unveils-new-temporary-museum-with-immersive-technology | OK |
| 39 | https://www.fcbarcelona.es/es/entradas/camp-nou-experience/mirador-obras-nuevo-spotify-camp-nou | OK (2023) |
| 40 | https://www.artvisitguide.com/camp-nou-museum-barcelona-review/ | OK (SEC-WEAK) |
| 41 | https://headout.com/reviews/23489/spain/barcelona/tickets-to-fc-barcelona-immersive-tour-sport-experience | OK (reviews to early 2025) |
| 42 | https://www.fcbarcelona.com/en/tickets/camp-nou-experience/timetable | OK |
| 43 | https://www.fcbarcelona.com/en/tickets/camp-nou-experience/plan-your-visit/shops | OK (no location) |
| 44 | https://agenda500.barcelona.cat/en/detall/museu-barca-immersive-tour_92163150849.html | OK |
| 45 | https://www.fcbarcelona.com/en/tickets/camp-nou-experience/practical-information/getting-to-the-camp-nou | OK (2023 text) |
| 46 | https://www.fcbarcelona.com/photo-resources/2023/06/23/297c4375-fcca-4224-929d-e692977a2ab2/MicrosoftTeams-image-23-.png | **FAILED** (client error) |
| 47 | https://www.fcbarcelona.com/en/news/4465846/fc-barcelona-official-statement | OK |
| 48 | https://www.fcbarcelona.es/es/entradas/camp-nou-experience/visitas-museo-barca | OK |

Not attempted (leads for Chrome): the Catalan ticket page; the other Oct 2026 WEBP maps; the Barça app.

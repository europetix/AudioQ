# REAL ALCÁZAR DE SEVILLA V5 (Yo Tours, English) — PLAN, 30 Oct 2026. Built from the lead's SKELETON.md (30 Oct 2026).

**Binding for writers.** Navigation and placement come first: customers complained that earlier guides described things in the wrong place. Every cue names the destination by its **number on the official Alcázar map** (the Patronato's leaflet, *tríptico*, Nov 2024, spaces 1–53) **and its Spanish name**, plus one thing to look for. Placements come from `research/VISIT_ROUTE_AND_SPACES_OCT2026.md` (the leaflet legend and space statuses). Facts come from `research/AUDIT_OLD_GUIDE_FACTS_OCT2026.md`, in its corrected wording, plus eight official or secondary pages read for this plan on 30 Oct 2026 (marked "read 30 Oct, plan" in the source key). The old guide (`old/001–020.txt`) is for stories and tone only: many of its facts and places are wrong.

**The leaflet's drawing is not yet available as an image.** So the destinations and the order below are binding, but every left/right, "in front of you" and door-level wording is **PROVISIONAL**. Cues name the destination's number and Spanish name plus one thing to look for. Wherever geometry matters there is an ONSITE or MAP item (section 5 and `v5/ONSITE_CHECKLIST.txt`). Writers must not add directions of their own.

## 1. Header

### User decisions (30 Oct 2026, from the skeleton)
- Rebuild from scratch to the series standard ("the work is quite old and not great").
- **Three lengths along ONE walking order**: Highlights ≈ 45 min, Essential ≈ 75 min, Full ≈ 120 min, as visit times including walking. One recording. The shorter versions get hand-written spoken "next stop" bridges (as for the Uffizi). Writers do the bridges later; section 3 lists where they are needed.
- **Optional section for the Cuarto Real Alto** (a separate timed visit of the upper floor): Extras outside the three lengths. The skeleton asked for 4–5. Only 2 can be sourced today (see Changes).
- Languages EN, ES, FR, DE. The map numbers are language-neutral, which helps all four.
- Must beat the official guides (the free MuseumMate QR web guide; the paid Artymax concession app) and the competitors (`research/OFFICIAL_AUDIO_COMPARISON_OCT2026.md`). The gaps we fill are: stop numbers that match the printed map (a 12 Oct 2026 review says the official guide's numbers don't), the Casa de la Contratación in depth, the reopened Muñecas passage, the restored Mercury pool, the outer gardens, and a Cuarto Real Alto companion.

### Targets
- Skeleton: Full ≈ 10,500 spoken words (≈ 85 min listening + ≈ 35 min walking), Essential ≈ 6,300, Highlights ≈ 3,400.
- **This plan:** Full **33 tracks ≈ 8,680 words**, Essential **20 tracks ≈ 5,900 words**, Highlights **10 tracks ≈ 3,040 words**, plus Cuarto Real Alto **2 Extras ≈ 380 words** outside the lengths. Section 3 explains why: walking takes longer than the skeleton assumed (≈ 40–45 min for the Full garden loop), and five skeleton Extras cannot be sourced. **Full lands at ≈ 110–115 min, not 120** (open question for the lead).
- Type lengths (V5 standard): R 180–280 (aim 230) · W 250–360 (aim 300) · X 150–230 (aim 190) · ANCHOR/CLOSE 250–360 (aim 320).

### Conventions
- **@room** = `No. <n> · <Spanish name exactly as on the leaflet>`, e.g. `No. 15 · Salón de los Embajadores`. The opening track is `Outside · Puerta del León`. Where a track covers several numbers, @room is the number where the listener presses play (named in the table). The Cuarto del Príncipe is not in the leaflet legend, so its Extra uses `No. 18 · Patio de las Muñecas`.
- **@title** = `<n> · <Spanish name> — <title>`, e.g. `15 · Salón de los Embajadores — The dome of 1427`. Extras: `<n> · Extra · <title>`, e.g. `13 · Extra · The chapel under the emperor's ceiling`. Cuarto Real Alto Extras: `CRA <n> · Extra · <title>`, e.g. `CRA 20 · Extra · Isabel's rooms and a tiled altar`. ANCHOR 001 takes a plain title (`Welcome to the Real Alcázar`). CLOSE follows the room pattern (`53 · Apeadero — The way out`).
- **How numbers are spoken.** The first time a number is spoken in the guide (in Full order), say "**number 15 on your Alcázar map**, the Salón de los Embajadores". After that say "**number 15**, the Salón de los Embajadores". **Always give the Spanish name with the number**, because the signs on site use the Spanish names. An English gloss may follow once per track ("…de los Embajadores, the Hall of Ambassadors"). 001 explains this once in all three lengths: the numbers are the ones on the Alcázar's own map, and the signs use the Spanish names. 001 must not say how or where to get the map until ONSITE O1 / MAP-1 is answered.
- **Never say "number 11".** The leaflet prints 11 twice on its drawing, and no track stops at 11 or 12.
- **Cue pattern.** The last paragraph of every track except CLOSE gives the destination number, its Spanish name and one thing to look for. A track before an Extra announces it like this: "Number 13 has a short Extra on…; the next main stop is number 15, the Salón de los Embajadores…". Then a listener who skips the Extra still knows where to go. Never say "next track" (lint).
- **Directions.** Until MAP/ONSITE confirm them, write no left/right, no "straight ahead" and no "far side" (the table marks every such need). Allowed: "through the triple arch", "off this courtyard", "back the way you came", "follow the Salida signs", "up the steps", and the named feature to look for. Each cue's provisional element is tagged [Oxx].
- **Lint.** The Uffizi `lint.py` room-cue regex (`Rooms? [A-E]\d…`) does not fit this guide. The Alcázar lint must accept `[Nn]umber \d{1,2}` and `Salida|Patio de Banderas` as a cue. (For the lead: copy and adapt it before writing starts.)
- **Dated items** are written as a separate sentence that can be cut ("DATED" in the table; section 6).
- **Writing rules** as in the series standard (`uffizi_v5/v5/V5_AUDIO_STANDARD.md` until it is copied here). Contested identifications are voiced as tradition ("tradition sees…"), never as fact. Present the Alcázar's own claims as its own ("the Alcázar calls itself…"). No prices, hours, tickets, booking, queues, security or bag advice. No shop or café (the shops are closed: notice of 19 Oct 2026). "The Alcázar says" at most once per track.

### Sections (one folder each, in walking order)
| Folder | Section | Tracks | Map numbers |
|---|---|---|---|
| `01_Opening` | Opening | 001 | outside the Puerta del León |
| `02_The_first_courtyards` | The first courtyards | 002–007 | 1–5 |
| `03_Casa_de_la_Contratacion` | Casa de la Contratación | 008–009 | 6–7 |
| `04_Palace_of_King_Pedro` | Palace of King Pedro | 010–017 | 10, 13, 15, 16, 18 |
| `05_Gothic_palace` | Gothic palace | 018–022 | 31–34 |
| `06_The_gardens` | The gardens | 023–032 | 35–51 |
| `07_Closing` | Closing | 033 | 53 |
| `08_Optional_Cuarto_Real_Alto` | Optional: Cuarto Real Alto | 034–035 | 19–24 |

### The route (reasoning; binding order, provisional geometry)
**Fixed points (sourced).**
- **Entrance:** the Puerta del León on the Plaza del Triunfo (OFF ticketing page; OFF school itineraries).
- **Order:** there is no compulsory route and "generally no one-way restrictions" (SEC European Traveler, Feb 2025). The leaflet's numbering 1–53 runs from the entrance inward. It is the de facto official order (OFF leaflet), and it is the order of this guide.
- **Exit:** through the **Apeadero (53)** into the **Patio de Banderas**. Supporting evidence: the leaflet prints SALIDA beside "PATIO DE BANDERAS" (OFF, position unconfirmed); the Puerta del Apeadero opens into the Patio de Banderas (OFF, prepara-la-visita); reports say you exit at the Patio de Banderas and cannot get back in (SEC). No source states in so many words that visitors leave through the Apeadero (ONSITE O28).

**Nos. 1–9.** León (1) → Sala de la Justicia (2), which leads into the Patio del Yeso (3) (route research) → back to the León and through its triple arch into the Montería (4) → the façade (5) → the Cuarto del Almirante (6) and its chapel (7) → back across the Montería to the palace door. Nos. 8–9 (Patio del Asistente, Patio de Levíes) are part of the Cuarto del Almirante but have no sourced content: walk past, no track.

**Pedro's palace, nos. 10–18.** Doncellas (10) → Salón del Techo de Carlos V (13, its door opens off the Doncellas: SEC photo record) and Infantes (14) → Embajadores (15) → Felipe II (16) and Reyes Católicos (17) → Muñecas (18). The stair to the Cuarto Real Alto (19) is near the Muñecas (leaflet order). Nos. 11–12 have no track.

**Muñecas → Gothic palace → gardens: the open question, worked out.**
- **Evidence:**
  1. The leaflet numbers the Gothic palace 31–34 straight after 19, with the Baths last (34) and the gardens starting at the Jardín del Príncipe (35).
  2. The Baths are the lower level of the Patio del Crucero. Felipe III gave them "an opening to the Jardín de la Danza" (OFF Baños page). A self-guided route reaches the Baths from the Jardín de la Danza (SEC), and the Patronato's school itinerary pairs Mercurio–Danza–Baños (OFF).
  3. The Gothic palace connects to the Montería by a porticoed gallery (SEC andalucia.com). A Patronato school itinerary walks "del Patio de las Doncellas … hasta el Patio de Crucero" (OFF, read 30 Oct). So the Crucero can be reached from the palace side, without the gardens.
  4. The garden numbers 35–39 sweep from the Jardín del Príncipe toward the Mercury pool.
  5. Since Mar 2025 a restored passage runs from the Muñecas to the Jardín del Príncipe (OFF). It is newer than the Nov 2024 leaflet. Its direction rules (one-way or not) are unknown.
- **Chosen order (A):** Muñecas (18) → back toward the Doncellas and on to the **Patio del Crucero (31)**, by the way the signs give (default: back out to the Montería and through the gallery; ONSITE O12) → **Salón de los Tapices and chapel (32)** → **Sala de las Bóvedas (33)** → out into the gardens → down into the **Jardín de la Danza (38)** → **Baths (34)** → out again and along the garden front to the **Jardín del Príncipe (35)** and the **column of Al-Mu'tamid (36)**. This is the start of the leaflet's garden sweep, where the garden end of the new passage can be seen. → Back along the front past the **Fuente de Troya (37)** to the **Jardín de la Danza (38)** → up to the **Estanque de Mercurio (39)**.
  - Why: it follows the leaflet's numbers (31→34→35→39). It uses the documented garden-level way into the Baths. It does not depend on entering the Gothic palace from the garden side, whose garden door may be exit-only.
  - Cost: one short out-and-back along the garden front (≈ 4 min) between the Baths and the Mercury pool. Essential and Highlights skip it.
  - The passage itself is told as an Extra (017) at its palace end, and pointed out from its garden end in 023. **We do not send listeners through it**, unless ONSITE O11 finds it is the only way on (ALT-B).
- **Rejected (held as ALT-B):** Muñecas → passage → Príncipe (35) → Troya and Danza → Baths → Mercury → into the Gothic palace from the garden (33 → 32 → 31) → back out. It uses the passage, but it reverses 31–33 and needs a two-way garden door into the Gothic palace, which nothing confirms. If O11 finds the passage is a one-way exit and the palace cannot be re-entered, the lead re-sequences tracks 018–024 to this order (a re-plan of section 05/06, not a cue swap).

**Gardens 39–53.** Follow the leaflet numbers: Mercurio (39) → Grutesco (40) → Fama (41) → [Neptuno 42, Sultanas 43: walk past] → Pabellón de Carlos V (44) → Cenador del León (45) → Jardín Inglés (46) and Laberinto (47) → [Puerta de la Alcoba 48, Poetas 49, Vega Inclán 50: walk past] → Puerta de Marchena (51) → [Alcubilla 52] → Apeadero (53) → Patio de Banderas. Essential leaves the line after the Pabellón (44), and Highlights after the Mercury pool (39). Both take the signed way out to the Apeadero (O28).

**What the map (or the site) must confirm:** see MAP-1 to MAP-4 and the CRITICAL ONSITE items O4, O7, O11, O12, O18, O24 and O28 (section 5).

### ALT cues (held: swap in after the map or the on-site check, without re-planning)
- **ALT-C (the Crucero is reached directly from the Doncellas, O12):** 016 and 017 cues: "Go back into number 10, the Patio de las Doncellas, and through [the doorway found] to number 31, the Patio del Crucero…". Same for the 016 H bridge.
- **ALT-D (no garden door from the Bóvedas, O17):** 021 cue: "Go back through number 31, the Patio del Crucero, and out to the gardens by [the way found], then down into number 38, the Jardín de la Danza…".
- **ALT-E (the Baths are entered from the Crucero, not the garden, O18):** 021 cue sends listeners to the Baths first, and 022's cue sends them out into the Danza and on to number 35.
- **ALT-F (Pabellón still closed or screened, O24):** 028 records its "behind screens" sentence instead of its "open" sentence (both are written; see DATED).
- **ALT-B (passage one-way, O11):** re-plan, not a swap (see above).

### Changes from the skeleton
1. **Five skeleton Extras dropped: their content cannot be sourced** (no official or secondary page found; the leaflet gives names only):
   - S009 Patio del Asistente and Patio de Levíes (8–9);
   - S012 Alcoba Real and Salón de los Pasos Perdidos (11–12; one SEC line only, and 11 is printed twice on the map);
   - S029 Fuente de Neptuno and Gruta de las Sultanas (42–43);
   - S034 Puerta de la Alcoba and Jardín de los Poetas (48–49);
   - S035's Jardín de la Alcubilla (52).
   They are **held**: each can come back as a 190-word Extra if O5, O8, O23 or O27 photographs an official panel with usable facts (+1.5 min each to Full).
2. **Cuarto Real Alto: 2 Extras, not 5.** Held: S039 Mirador (25), S040 Dormitorio de Pedro I and Sala de Audiencias (26–28), S041 Sala de Billar and the Carranza collection (29–30). Only names are sourced. Two sources were tried and blocked by bot-protection pages: an academic article on revistas.uam.es and *Reales Sitios* 1992. I did not get round the blocks. Sources needed: official panels or the Patronato's own handout (O13), or Pleguezuelo, *Lozas y azulejos de la Colección Carranza* (2002).
3. **S035's Puerta de Marchena is promoted to a main R (032).** The Patronato's own page (`alcazarsevilla.org/?p=11106`, read 30 Oct) is rich. S034's slot (Alcoba and Poetas, unsourced) is replaced by it, and the two tracks merge into one.
4. **New 003 R (Full only): "Eleven centuries on one site"** in the Patio del León. The audit's verified timeline (913 → Abbadids → Almohads → 1248 → Alfonso X → Pedro → the Catholic Monarchs → Charles V → the Bourbons → the 1931 cession to the city → the royal residence today) had no home: 001 has room only for a one-line summary. Delete it if the lead prefers (Full −1.8 min).
5. **Type changes**, where the verified material is rich:
   - S007 Contratación R→W (the comparison makes it a flagship gap);
   - S010 Pedro R→W (Marquer's "sultan" inscriptions; his posthumous journey);
   - S019 Crucero R→W;
   - S024 Príncipe and Al-Mu'tamid R→W;
   - S031 Cenador del León X→R (an official archaeological report, read 30 Oct);
   - S032 Jardín Inglés R→X (only one official line).
6. **S033 Dorne moved to straight after the Pabellón de Carlos V (now 029)**, where the fight scene was filmed (OFF Film Commission). In the skeleton it followed the English garden, which no scene used.
7. **S013's coffered ceiling is now sourced.** The Salón del Techo de Carlos V was designed as a chapel and has a Renaissance coffered ceiling of 1543 (SEC andalucia.com, mod. 9 Apr 2026). S028's water organ is sourced too (OFF `?p=11076`), and so is S021's chapel (OFF `?p=10886`). All three Extras stay.
8. **Membership changes to hit the times** (section 3):
   - Highlights drops S002 (Lion Gate) and S020 (Tapestries). It keeps the wedding, the Virgin and the Baths.
   - Essential drops S005 (Montería), S024 (Príncipe), S025 (Danza) and S032 (English garden). Those cost walking time or overlap.
9. **Renumbering** (skeleton → plan):
   - S001–S002 → 001–002; **003 new**; S003–S008 → 004–009; S009 dropped; S010–S011 → 010–011; S012 dropped;
   - S013–S028 → 012–027; S029 dropped; S030 → 028; **S033 → 029 (moved)**; S031 → 030; S032 → 031;
   - S034 + S035 → **032 (Puerta de Marchena)**; S036 → 033; S037–S038 → 034–035 (CRA); S039–S041 held.

## 2. Track table

**Source key** (codes used in the table; URLs as logged by research, or read for this plan on 30 Oct 2026).

| Code | Grade | Source |
|---|---|---|
| LEAF | OFF | Official leaflet (tríptico), Nov 2024: https://alcazarsevilla.org/wp-content/uploads/2024/11/triptico_alcazar_sevilla.pdf (legend 1–53; re-read 30 Oct, plan, for its few descriptive lines) |
| HIST | OFF | https://alcazarsevilla.org/historia/ (913; Abbadid "al-Mubarak", which this page misdates to the 10th century) |
| HOME | OFF | https://www.alcazarsevilla.org/ (banner "El Palacio Real en uso más antiguo de Europa") |
| PREP | OFF | https://alcazarsevilla.org/prepara-la-visita/ (Puerta del Apeadero opens into the Patio de Banderas; the leaflet link) |
| TICK | OFF | https://alcazardesevilla.infoticketing.com/en/entradas/visita-real-alcazar-cuarto-real-alto (entry via the Lion Gate; placement only) |
| ITIN | OFF | https://alcazarsevilla.org/wp-content/uploads/2024/11/02-Itinerarios-y-Actividades.pdf (school itineraries; re-read 30 Oct, plan: gate named from the tile lion over the arch; "del Patio de las Doncellas … hasta el Patio de Crucero"; two columns on the upper level of the Danza; Sala Gótica tiled "hasta unos 2 metros") |
| BANOS | OFF | https://www.alcazarsevilla.org/?p=10943 (Baños = lower level of the Crucero) |
| MUN | OFF | https://www.alcazarsevilla.org/?p=10868 (Patio de las Muñecas) |
| CENC5 | OFF | https://www.alcazarsevilla.org/?p=11014 (Cenador / Pabellón de Carlos V) |
| CAPG | OFF | https://www.alcazarsevilla.org/?p=10886 (Capilla del Palacio Gótico; read 30 Oct, plan) |
| ORG | OFF | https://www.alcazarsevilla.org/?p=11076 (Órgano hidráulico, Fuente de la Fama; read 30 Oct, plan) |
| MARCH | OFF | https://www.alcazarsevilla.org/?p=11106 (Puerta de Marchena; read 30 Oct, plan) |
| EXPO | OFF | https://alcazarsevilla.org/wp-content/uploads/2025/01/EXPO-MERCURIO-FINAL.pdf (Mercury, Grutesco, Danza, aqueduct) |
| MERC | OFF | https://alcazarsevilla.org/restauracion-estanque-mercurio/ (Mercury restoration; repeats the Muñecas passage item of 20 Mar 2025) |
| TAB16 | OFF | Tabales, Puerta del León, AAA 2016, Junta de Andalucía: juntadeandalucia.es/cultura/tabula/…/9631 (as logged) |
| TAB18 | OFF | Tabales & Vargas, Cenador y Estanque del León: https://juntadeandalucia.es/cultura/tabula/bitstream/20.500.11947/19784/1/AAA_2018_197_tabalesrodriguezmigela_cenadoryestanquedelleon_sevilla_borrador.pdf (read 30 Oct, plan) |
| ARCH-Y / ARCH-D | OFF | Archnet sites 20835 (Patio del Yeso) / 20755 (Patio de las Doncellas), Almagro & Ramón-Laca (archnet.org/sites/…) |
| GAC | OFF | Ayuntamiento de Sevilla / Real Alcázar on Google Arts & Culture: "A Walk Through the Royal Alcázar"; "Hall of Ambassadors' Dome" |
| MARQ | OFF | J. Marquer, *Anales de Historia del Arte* 23 (2013), revistas.ucm.es |
| PHIL | OFF | C. R. Phillips, "Visualizing Imperium", *Renaissance Quarterly* 58 (2005) |
| UAH | OFF | Real Provisión, 20 Jan 1503: https://cisneros.web.uah.es/carpeta/images/pdfs/093_real.pdf |
| ALH | OFF | Alhambra Patronato, Court of the Lions: alhambra-patronato.es/en?p=10173 |
| PN | OFF | Patrimonio Nacional, Galería de las Colecciones Reales, Isabel of Portugal |
| PN17 | OFF | Patrimonio Nacional PDF, 14 Feb 2017 (the Virgin: ownership, restoration in situ) |
| BAD | OFF | Diputación de Badajoz, Puebla de Alcocer, Iglesia de Santiago (ENG PDF, 2026) |
| AFC | OFF | Andalucía Film Commission: https://www.andaluciadestinodecine.com/en/localizacion/reales-alcazares/ |
| ANDO | OFF | Junta tourism: https://andalucia.org/en/sevilla-visitas-real-alcazar-de-sevilla (read 30 Oct, plan: Niculoso Pisano altar 1504; 19th-century Bourbon top-floor rooms, tapestries, La Granja crystal lamps) |
| CAB | SEC | J. M. Cabeza Méndez, Doncellas garden restoration: https://core.ac.uk/download/51402338.pdf |
| MGON | SEC | J. J. Martín González, "Escenas de mar…", uvadoc.uva.es |
| GP | SEC | García Parody & Caballero, *Revista de Estudios Taurinos* 42 (2018), dialnet 7042473 |
| CAT | SEC | *El arte del poder* catalogue p. 106, accioncultural.es (Tunis tapestries) |
| BRID | SEC | Bridgeman caption (F. I. Vandergoten, 1704–1774) |
| ANDC | SEC | andalucia.com: https://andalucia.com/cities/seville/alcazar/mudejar.htm (mod. 9 Apr 2026; read 30 Oct, plan) and its Gothic palace / Bóvedas text as logged by research |
| RIBA | SEC | RIBApix, Oratorio de los Reyes Católicos altarpiece: https://www.architecture.com/image-library/RIBApix/image-information/poster/alcazar-seville-oratorio-de-los-reyes-catolicos-altarpiece/posterid/RIBA108556.html (read 30 Oct, plan: "the Visitation framed by the Tree of Jesse", 1504) |
| ELD | SEC | eldiario.es, 8 May 2025 (Cuarto Alto = official residence) |
| ARAM | SEC | AramcoWorld, "The Poet-King of Seville" (1993) |
| VIV | SEC | vivirediciones.es: 11 Apr 2024 (Mercury original), 12 Jan, 1 Feb, 1 Jul, 20–21 Jul 2026 (restorations, programme) |
| IBZ | SEC | Periódico de Ibiza, 9 Oct 2014 (season 5 shoot) |
| DIV | SEC | Divisare project record, Patio de Banderas excavation 2009–13 |
| EUT | SEC | European Traveler, 12 Feb 2025 (no one-way rules; exit at the Patio de Banderas) |
| MAK | SEC | Placement only: MAK photo record, door to the Salón de Carlos V in the Patio de las Doncellas: https://sammlung.mak.at/de/collect/fotografie-der-tuer-zum-salon-von-carl-v-im-patio-de-las-doncellas-im-alcazar-in-sevilla_297102 |
| SNIP | — | Standard reference fact or search snippet, not fetched. **Confirm before recording**, or use the hedged wording given. |

Key: H = Highlights, E = Essential (E includes every H), CRA = optional Cuarto Real Alto section, "–" = Full only. [Oxx] = provisional wording that depends on ONSITE item Oxx. **NOT** = what must not be said.

| # | Type | Section | @room | @title | Core content (corrected wording; **NOT** = do not say) | Sources | Cue to next (number + Spanish name + one thing to look for) | H/E/CRA |
|---|---|---|---|---|---|---|---|---|
| 001 | ANCHOR | Opening | Outside · Puerta del León | Welcome to the Real Alcázar | Where you stand: the Puerta del León, named after the **tile lion above the arch**. "Alcázar" from Arabic *al-qasr*. A seat of power since **913**, when **Abd al-Rahman III, then emir of Córdoba**, ordered a new seat of government here. Palaces of many eras side by side: an Almohad courtyard, a 13th-century Gothic palace, King Pedro's 14th-century Mudéjar palace, Renaissance and 20th-century gardens. The Alcázar calls itself "the oldest royal palace still in use in Europe" (attribute it). The upper floor is the Royal Family's official residence in Seville. UNESCO World Heritage since 1987, together with the Cathedral and the Archivo de Indias (SNIP: confirm). How the guide works: the numbers are those on the **Alcázar's own map**, 1 to 53; the signs use the Spanish names; three lengths; Extras are announced; the Cuarto Real Alto has its own short section at the end "if your visit includes the upper floor". **NOT:** tickets, queues, prices, hours, security, bags, the shop; "walls first laid in 913"; a "12th-century Almohad gate"; "continuously occupied for 1,100 years"; "17 hectares"; visitor caps; "Renaissance dome"; "nineteenth-century English gardens"; any "we visited yesterday"; how or where to get the map (O1/MAP-1). | HOME OFF · HIST OFF · ITIN OFF · ELD SEC · LEAF OFF · UNESCO SNIP | Through the gate into **number 1 on your Alcázar map, the Patio del León**: the courtyard just inside, with a triple arch leading on. [O1, O2] | H E |
| 002 | W | The first courtyards | No. 1 · Patio del León | 1 · Patio del León — The Lion Gate and a lost theatre | The gate, the tower lining and the adjoining wall were built in **one campaign under Pedro I, in the 1350s** (radiocarbon centred on 1368). The gate was long called the **Puerta de la Montería**; "del León" comes from the tile panel, a later addition (no date or maker known). **The patio was a theatre**: the Corral de la Montería, from the 1620s until a **fire in 1691**. Then it was stables and housing, and it was **cleared in 1936–37 by Juan Talavera** to make today's visitor entrance. Claim visible traces of the theatre only if O2 finds them. **NOT:** "Almohad" or "12th-century" gate; "same workshops as the Giralda"; "1894, Mensaque factory"; "Ad utrumque"; "ninth-century walls" or "913 masonry"; "a thousand metres to the Giralda"; "hunters gathered here with the king"; "three Almohad arches". | TAB16 OFF · ITIN OFF | Stay in **number 1, the Patio del León**, for a short look at eleven centuries before we go in. | E |
| 003 | R | The first courtyards | No. 1 · Patio del León | 1 · Patio del León — Eleven centuries on one site | A timeline for reading the layers. **913**: Abd al-Rahman III, then emir, later (929) the first caliph of Córdoba. 11th century: the Abbadid palace **al-Mubarak, "the Blessed"**. Almohads: a residence of **about 1190** (Patio del Yeso). **1248**: Fernando III takes Seville after a siege of more than a year (SNIP); he dies here in 1252 (SNIP). 13th century: **Alfonso X's Gothic palace**. From **1356**: Pedro I's palace (leaflet). The Catholic Monarchs; Charles V's wedding in 1526; Bourbon rooms upstairs in the 19th century. **1931**: the Republic ceded the Alcázar to the city; today the city's Patronato runs it, and the upper floor is the King's official residence in Seville. The oldest wall archaeologists have found is **11th-century** (possibly Almoravid). **NOT:** "first caliph in 913"; "independent of Damascus"; "unbroken royal use"; "Visigothic basilica"; "a hundred metres square"; "his masonry survives in the Patio de Banderas". | HIST OFF · ARCH-Y OFF · TAB16 OFF · LEAF OFF · ANDO OFF · ELD SEC · SNIP | **Number 2, the Sala de la Justicia**, opens off this courtyard: a small square hall with a fountain set in its floor. [O2] | – |
| 004 | R | The first courtyards | No. 2 · Sala de la Justicia | 2 · Sala de la Justicia — Alfonso XI's hall | Built **at the time of Alfonso XI**, 14th century, around the 1340s, "**possibly** after his victory at the Río Salado" (1340; Alfonso XI with Afonso IV of Portugal against the Marinids and Granada, "the last great Marinid expedition into Iberia", SNIP). Islamic-inspired (Mudéjar) decoration for a Christian king; the floor fountain. The Order of the Band (founded by Alfonso XI around 1330, SNIP) only if its shield is seen (O2). **NOT:** "built to celebrate Salado" as fact; "justice dispensed here for 500 years"; "entirely Islamic"; "Burgos and León would have felt foreign"; the fountain channel into the Yeso unless seen; **no "on this day" hook** (Salado was 30 October). | GAC OFF · SNIP | Through to **number 3, the Patio del Yeso**: a lattice of brick arches over a long pool. [O2, O3] | E |
| 005 | W | The first courtyards | No. 3 · Patio del Yeso | 3 · Patio del Yeso — What the Almohads left | The remnant of an **Almohad residence of about 1190**, the Islamic "Palacio del Yeso" (leaflet). The **sebka** lattice is the same motif as on the Giralda. **Pedro I lived here in 1358**, before his new palace existed. Hidden for centuries and **rediscovered in 1855**; restored **1918–20 and 1969–71**. "More than eight centuries old." **NOT:** Ali al-Gumari (unsourced); the Torre del Oro (1220–21); "840 years"; "twenty-six American presidents"; Quranic "theological humility"; mint, jasmine and citrus; Tubino; "the Almohads designed it to sound like this". | ARCH-Y OFF · LEAF OFF | Back through the Patio del León and its triple arch into **number 4, the Patio de la Montería**: the big open courtyard with a tall decorated palace front. [O3, O4] | E |
| 006 | R | The first courtyards | No. 4 · Patio de la Montería | 4 · Patio de la Montería — Reading the courtyard | Orientation, with every direction provisional [O4]: the façade of Pedro's palace (number 5); the Cuarto del Almirante, home of the Casa de la Contratación (6); the way to the Gothic palace (31) by a gallery (SEC); and the Apeadero (53), the way out at the end, only if O4 confirms it opens here. The name: the Lion Gate was long the Puerta de la Montería; *montería* is the royal hunt ("the name refers to the royal hunt"). Pedro's palace was begun in 1356 (leaflet). **NOT:** "hunters gathered here with the king"; events or the 2025 opera; "the Casa ran the entire empire". | TAB16 OFF · LEAF OFF · ANDC SEC | Walk up to **number 5, the façade of King Pedro's palace (Fachada del Palacio del Rey Don Pedro)**, close enough to see the bands of lettering high on the front. [O6] | – |
| 007 | W | The first courtyards | No. 5 · Fachada del Palacio del Rey Don Pedro | 5 · Fachada del Palacio del Rey Don Pedro — A king's name in two scripts | The Gothic Castilian inscription is dated Spanish era **1402 = 1364**: "El muy alto et muy noble et muy poderoso et muy **conqueridor** don Pedro por la gracia de Dios rey de Castilla et de León… mandó…" (keep *conqueridor*). It frames the Nasrid Kufic motto ***wa-la ghaliba illa Allah*, "there is no victor but God"**, on blue and white tiles. The palace was begun from 1356 and finished by 1366. **Craftsmen from Seville and Toledo, and probably from Nasrid Granada.** The Alhambra's Palace of the Lions (1362–1391) is a close contemporary, partly later. Point to the bands only as O6 locates them. **NOT:** "craftsmen who had just finished the Court of the Lions"; "repeated four times in each direction"; "three-three-three proportions"; "built in 1364 after returning to power"; "Pedro the Cruel because he was friendly to Muslims and Jews" (say only that his enemies' propaganda included that charge); the Comares façade as earlier. | MARQ OFF · GAC OFF · LEAF OFF · ALH OFF · CAB SEC | **Number 6, the Cuarto del Almirante**, opens off this courtyard: the range where the Casa de la Contratación worked (look for its name on the sign). [O4] | H E |
| 008 | W | Casa de la Contratación | No. 6 · Cuarto del Almirante | 6 · Cuarto del Almirante — The Casa de la Contratación | Founded by a **Real Provisión of the Catholic Monarchs**, Alcalá de Henares, **20 January 1503**. The damp Atarazanas were rejected, and the Casa was put in the Cuarto de los Almirantes, where it **stayed until 1717** (then Cádiz). It **ran trade and shipping with the Americas**: it licensed ships, cargoes and passengers, "including the slave trade under royal licence". Say this plainly, without list rhetoric. Collecting the royal fifth and training pilots: "widely stated" (SNIP, general wording only). Its papers are now in the Archivo de Indias, "across the plaza". The leaflet labels this block "Casa de la Contratación". **NOT:** "founded by Queen Isabel"; "ran the entire empire"; "every enslaved African registered…"; the ceiling paintings, marble bench or heraldic tapestries unless seen (O5); "twenty metres away"; confusing its Sala de Audiencias with the upper-floor Sala de Audiencias (CRA no. 28). | UAH OFF · GAC OFF · PHIL OFF · LEAF OFF | Through to **number 7, the Capilla de la Virgen de los Navegantes**, the old audience hall: the Virgin spreading her cloak over a crowd, with ships at her feet. [O5] | E |
| 009 | W | Casa de la Contratación | No. 7 · Capilla de la Virgen de los Navegantes | 7 · Capilla de la Virgen de los Navegantes — Alejo Fernández | Painted **1531–36**, "now attributed" to **Alejo Fernández**, a Seville painter "of German origin", for the chapel of the Casa's audience hall. Also called the Virgen de los Mareantes; the leaflet says "Navegantes". **Tradition** sees Columbus (the figure in gold), a Pinzón, Charles V (the red-haired man, "generally thought") and perhaps Cortés; Vespucci, or perhaps Sancho de Matienzo. **All these identifications are disputed.** Indigenous men and women stand in the background in simple white wraps. The ships: a carrack, caravels, a galley and smaller craft. Side panels: St Sebastian, St James, St Elmo, St John (on Patmos). Phillips reads it as an imperial and evangelical self-portrait (attribute it). Owned by Patrimonio Nacional and kept in the Alcázar; a 2017 agreement keeps any restoration in Seville. "**One of the earliest** European paintings tied to the Atlantic voyages." **NOT:** "the first depiction of the Americas"; "seven ship types"; Juan de la Cosa; "lost in the 19th century, rebuilt in the 1960s"; "Buen Aire"; "bare-chested"; "the first images in a major altarpiece". | PHIL OFF · MGON SEC · PN17 OFF · LEAF OFF | Back across the Montería and through the palace door in **number 5, the façade**, into **number 10, the Patio de las Doncellas**: a long pool between sunken garden beds. [O4, O7] | H E |
| 010 | W | Palace of King Pedro | No. 10 · Patio de las Doncellas | 10 · Patio de las Doncellas — The king hailed as sultan | Play at the near end of the courtyard. Pedro I: born 1334; king at **15**, in 1350 (SNIP). He built this palace from 1356; it was finished by 1366. Arabic bands in the palace read ***'izz li-mawlana al-sultan don Bidru ayyadahu Allah*: "Glory to our lord the sultan Don Pedro, may God help him"** (Marquer). Point only to bands that O7 locates. Civil war with his half-brother Enrique: deposed in 1366, back in 1367, **killed at Montiel in 1369, by most accounts by Enrique himself**, and the Trastámara dynasty began. "El Cruel" or "el Justiciero": two nicknames, two propagandas. His body's journey: Puebla de Alcocer → **1446** Santo Domingo el Real, Madrid → after that convent was demolished, the Museo Arqueológico → **Seville Cathedral**. He helped restore Muhammad V of Granada in 1362 (SNIP). **NOT:** "sheltered Muhammad V in Seville in 1359"; "in 1364, after returning to power"; "crowned at sixteen"; "moved to Seville at Constanza's request"; "fifty metres from where we stood yesterday"; "craftsmen from the Court of the Lions". | MARQ OFF · BAD OFF · LEAF OFF · CAB SEC · SNIP | Stay in **number 10, the Patio de las Doncellas**, and walk to the edge of the long pool. [O7] | E |
| 011 | W | Palace of King Pedro | No. 10 · Patio de las Doncellas | 10 · Patio de las Doncellas — The buried garden | On **22 Aug 2002** Tabales's team found the walks, pool and beds of Pedro's sunken patio under a 16th-century level (digs in 2002 and 2004). **By 1584** the courtyard had been paved over, with a central fountain under Felipe II. Almagro and Ramón-Laca: the garden was buried soon after Pedro's murder and was **possibly never finished or used**. Restored by the **Alcázar's Patronato** (Cabeza, its director). A long pool between two sunken beds, about a metre below the walkway. The arcades were remodelled in the 16th century, with Renaissance columns. The name: a medieval legend of a tribute of a hundred maidens. **DATED** (one cuttable sentence, only if O7 finds scaffolding): conservation is under way in phases. **NOT:** Roman or Visigothic columns here (they are in the Muñecas); "T-shaped pool"; "the cathedral chapter"; "as his court saw it in 1366"; "replanted from 14th-century records"; "lowered by 40 cm"; arch counts unless counted on site; Game of Thrones here. | CAB SEC · ARCH-D OFF · GAC OFF · VIV SEC | **Number 13, the Salón del Techo de Carlos V**, has a short Extra on the palace chapel and its Renaissance ceiling: its door opens off this courtyard [O8]. The next main stop is **number 15, the Salón de los Embajadores**, the hall under the gilded dome. [O7] | H E |
| 012 | X | Palace of King Pedro | No. 13 · Salón del Techo de Carlos V | 13 · Extra · The chapel under the emperor's ceiling | The room was designed as a **chapel**. It has a **Renaissance coffered ceiling of 1543 with busts of human figures** (SEC). Marquer notes that in the palace's former chapel the Arabic word ***malik* (king) replaces *sultan***: use it **only** if the writer confirms in Marquer 2013 that her "former chapel" is this room; otherwise omit. Next door, **number 14, the Sala de los Infantes**: rooms of the king's daughters (SEC). This room is in **Pedro's palace**, not the Gothic palace. **NOT:** double eagle or Plus Ultra unless seen (O8); "Salones de Carlos V = the Gothic palace"; any staircase. | ANDC SEC · MARQ OFF (conditional) · MAK SEC (placement) | Back into the Doncellas and on to **number 15, the Salón de los Embajadores**: look up for the gilded wooden dome. [O8] | – |
| 013 | W | Palace of King Pedro | No. 15 · Salón de los Embajadores | 15 · Salón de los Embajadores — The dome of 1427 | Pedro's throne room and main hall. The **dome (*media naranja*) built by Diego Ruiz in 1427**, a gilded 15th-century dome that "replaced the original ceiling" (hedged). A square room like a qubba: the square stands for the earth, the dome for the universe (Ayuntamiento). An Arabic inscription on the **doors** dates the work to Spanish era **1404 = 1366**. **Wrought-iron balconies**, late 16th century, under Felipe II. Portraits of kings by **Diego de Esquivel, 1599**. **NOT:** "Renaissance dome"; "16-sided, only four others in the world"; "16 metres high"; "wooden balconies"; a qibla wall, a changed orientation or al-Thurayya "on this spot"; ambassadors from "the Aztec emperor's heirs"; "56 kings, Pedro on the south wall". | GAC OFF · MARQ OFF | Stay in **number 15, the Salón de los Embajadores**: picture it on a March night in 1526. | H E |
| 014 | W | Palace of King Pedro | No. 15 · Salón de los Embajadores | 15 · Salón de los Embajadores — The night the emperor married | Isabel of Portugal entered Seville on **3 March 1526**. Charles came **from Toledo** and arrived on **10 March**. That night **Cardinal Salviati** married them by words of present consent in the great domed hall, the *media naranja*. After midnight, now **11 March**, the **Archbishop of Toledo** said the nuptial Mass in a chamber of the palace. Godparents: the **Duke of Calabria and the Countess of Haro**. Ages **26 and 22**. Isabel was the daughter of Manuel I and **María** of Aragon. Papal dispensation. A dowry of **900,000 ducats**. The city's seven arches showed Prudence, Fortitude, Clemency, Peace, Justice, the Theological Virtues and Glory. News of the death of Charles's sister, Queen Isabel of Denmark, **cut the celebrations short**. Seville until May, then a long stay in Granada. Isabel died on 1 May 1539 after her last childbirth; Charles **never remarried**. The dome was "nearly a century old". **DATED** (one cuttable sentence, or leave the year out): "In 2026 Seville marked the 500th anniversary." **NOT:** "from Madrid"; "23"; "Isabel of Aragon"; the Pedro Mexía quote; "the emperor's memoir"; a "next-morning wedding Mass in the cathedral"; Felipe II "conceived within weeks" or "born nine months later"; "fifteen or twenty people"; "doblas" or "one of the largest dowries in history"; the arches' locations; the Dancart retablo; Lent reasoning; the Santa Clara exhibition; "this year"; Charles "using" the garden pavilion. | GP SEC · PN OFF · VIV SEC | **Number 16, the Salón del Techo de Felipe II**, has a short Extra on the Peacock Arch and two painted ceilings. The next main stop is **number 18, the Patio de las Muñecas**: the smallest courtyard in the palace. [O10] | H E |
| 015 | X | Palace of King Pedro | No. 16 · Salón del Techo de Felipe II | 16 · Extra · The Peacock Arch and two ceilings | A short Extra (150–190 words). Number 16 is named after its **semi-barrel wooden ceiling**. The **Peacock Arch** leads to the Hall of Ambassadors. **Number 17, the Sala de los Reyes Católicos** (also called the Dormitorio de los Reyes Moros): a wooden ceiling of **ribbons and heraldic emblems**. Describe only what O10 confirms. **NOT:** dates or makers (none sourced); peacock symbolism. | ANDC SEC | On to **number 18, the Patio de las Muñecas**: the small two-tier courtyard. [O10] | – |
| 016 | W | Palace of King Pedro | No. 18 · Patio de las Muñecas | 18 · Patio de las Muñecas — Columns from older buildings | The private heart of the palace, around which the private rooms were organised; the smallest courtyard on the visit. The name: **small heads carved where the arch nearest the entrance springs** (no number given) [O11]. **Reused Caliphal and Roman columns and capitals.** The **two upper floors are 19th-century**. The rooms around it were remodelled under the Catholic Monarchs. María de Padilla, correct version and short (SNIP: confirm the dates): Pedro's companion, who **died in 1361**, before this palace was finished; in 1362 Pedro declared he had married her before his 1353 marriage to Blanche. Their daughter Constanza married John of Gaunt. The line to Isabel the Catholic and Catherine of Aragon only after a fetched reference confirms it (audit §3.17). Number 19, the stair to the Cuarto Real Alto, is near here: one sentence pointing to the optional section at the end of this guide; **no tickets or slots**. **NOT:** "the harem"; craftsmen's graffiti; "upper galleries by Felipe II"; María "held court", "lived here" or "fetched water"; a "secret marriage in 1361"; Henry VII, "every English monarch" or "Henry VIII's mother"; "unchanged for 650 years". | MUN OFF · ITIN OFF · SNIP | The Cuarto del Príncipe, beside this courtyard, has a short Extra on the rediscovered passage to the gardens [O11]. The next main stop is **number 31 on your Alcázar map, the Patio del Crucero**, the courtyard of the Gothic palace: follow the signs for the Palacio Gótico (default: back through the Doncellas and the palace door to the Montería, then the gallery) [O12; ALT-C]. | H E |
| 017 | X | Palace of King Pedro | No. 18 · Patio de las Muñecas | 18 · Extra · The Prince's rooms and a forgotten passage | In **March 2025** the Alcázar reopened a **historic passage from the Patio de las Muñecas to the Jardín del Príncipe**, with LED lighting and **newly revealed painted colour on the plasterwork**. No competitor mentions it. The Cuarto del Príncipe was used as the queen's bedroom until the upper floor was built for Isabel the Catholic (SEC, hedged). **Prince Juan**, son of the Catholic Monarchs, was born in the Alcázar in **1478** and died in 1497, aged 19 (SNIP: **only if confirmed** before recording). Tell listeners they will see the passage's garden end at number 35, and **not** to take it now (unless ALT-B). **NOT:** "the royal baby died at 19 days" (an andalucia.com error); the harem; the passage as "secret". **DATED:** say "since 2025", not "just reopened". | MERC OFF · ANDC SEC · SNIP | **Number 31, the Patio del Crucero**: follow the signs for the Palacio Gótico (default via the Doncellas, the palace door and the Montería gallery) [O12; ALT-C]. | – |
| 018 | W | Gothic palace | No. 31 · Patio del Crucero | 31 · Patio del Crucero — Alfonso X's Gothic palace | Alfonso X, "the Wise", built a **Gothic palace in the 13th century** over the Almohad palace. Much of the Patio del Crucero is Islamic in origin (leaflet). The leaflet's line: the Gothic palace "staged the drastic transition to the new Christian order" (quote the leaflet, translated). The courtyard's **lower level survives as the "Baths"**: a sunken summer garden of Almohad origin, its vaults made Gothic under Alfonso X and reworked under Felipe III. Alfonso X: the *Cantigas de Santa María*, translations, Castilian prose (SNIP, general). He was Pedro's **great-great-grandfather**. After the 1755 Lisbon earthquake the palace was repaired and given a Baroque front (hedged; O14). **NOT:** "1254–1260"; "great-grandfather"; "felt in Finland"; Van der Borcht by name; "climb a staircase"; an upper Gothic floor. | HIST OFF · LEAF OFF · BANOS OFF · GAC OFF · SNIP | Into **number 32, the Salón de los Tapices**: a great hall hung with huge tapestries of a sea campaign. [O14, O15] | E |
| 019 | W | Gothic palace | No. 32 · Salón de los Tapices y Capilla | 32 · Salón de los Tapices — The conquest of Tunis | **1535**: Charles V's expedition took Tunis from Barbarossa and **restored Mulay Hasan as his vassal** (SNIP). The originals: **Willem de Pannemaker**'s contract of **1545**, woven 1548–54, **12 panels**, cartoons by **Jan Cornelisz Vermeyen and Pieter Coecke**; they are in the Spanish royal collection (Patrimonio Nacional). Here: **18th-century copies made in Madrid for Felipe V** by the Vandergoten family's royal manufactory (founded 1720); Francisco Ignacio Vandergoten (1704–1774). How many are on view: count them on site (O15). **NOT:** "six tapestries"; "woven in the 1730s"; "originals in storage"; "taken from a vassal of Charles"; "*Non plus ultra* was a Roman saying". | CAT SEC · BRID SEC · LEAF OFF · ANDC SEC · SNIP | The **chapel of the Gothic palace**, part of number 32, has a short Extra [O16]. The next main stop is **number 33, the Sala de las Bóvedas**: walls tiled to about two metres, under Gothic vaults. [O17] | E |
| 020 | X | Gothic palace | No. 32 · Salón de los Tapices y Capilla | 32 · Extra · The chapel of the Gothic palace | It keeps its **medieval rib vaults**; a Renaissance dado was added in the 16th century. The altarpiece holds a **copy of the Virgen de la Antigua**, the venerated medieval image in its chapel in Seville Cathedral. The writer must check on the page whether Diego de Castillejo painted the copy. **Domingo Martínez, *Virgen de los Reyes* between St Hermenegild and St Ferdinand, 1742.** Also an *Inmaculada con donante y Cristo como sacerdote*. Say only what O16 finds on view. **NOT:** anything that is not on the page. | CAPG OFF | On to **number 33, the Sala de las Bóvedas**: the tiled hall under Gothic vaults. [O16, O17] | – |
| 021 | R | Gothic palace | No. 33 · Sala de las Bóvedas | 33 · Sala de las Bóvedas — The vaulted hall | Also called the Salón Gótico or Sala de Fiestas. Gothic vaults; **walls tiled up to about 2 metres**. **Two naval tapestries made for the 1929 Ibero-American Exposition** (SEC). The historic *sargas* (painted cloths) of the Salón Gótico have been restored (SEC, Jul 2026; say "recently restored" only if O17 confirms they are on view). The view into the garden. **NOT:** a tile maker's name (none sourced); "Charles V's apartments". | ITIN OFF · ANDC SEC · VIV SEC | Out into the gardens and down into **number 38, the Jardín de la Danza**. **Number 34, the Baños de Doña María de Padilla**, opens off it under the palace: a doorway into a long pool under Gothic vaults. [O17, O18; ALT-D, ALT-E] | E |
| 022 | W | Gothic palace | No. 34 · Baños de Doña María de Padilla | 34 · Baños de Doña María de Padilla — A garden underground | **Not baths and not a cistern**: the **lower level of the Patio del Crucero**, a sunken summer garden of Almohad origin. Its vaults were made **Gothic under Alfonso X**, and it was remodelled under **Felipe III**, with a Mannerist fountain and an **opening to the Jardín de la Danza**. Built for the heat: "noticeably cooler". **The name is a legend**: María de Padilla, Pedro's companion, died in 1361 (SNIP), and nothing shows she bathed here. One line of Game of Thrones: this is where guards **arrest Ellaria Sand**. **NOT:** "she bathed here"; "Almohad cisterns"; "Almohads of the late 1200s"; "the same brick as the Giralda, the Yeso and the Torre del Oro"; "fifteen degrees cooler"; "residual seepage kept for effect"; "the Sand Snakes plot here"; "the tower you climbed yesterday". | BANOS OFF · AFC OFF · SNIP | Back out into the Danza and along the garden front, through the small Italianate gardens, to **number 35, the Jardín del Príncipe**: look for **number 36, the Columna de Al-Mutamid**. [O19] | H E |
| 023 | W | The gardens | No. 35 · Jardín del Príncipe | 35 · Jardín del Príncipe — The poet king | The gardens: **more than 20,000 plants of at least 187 species**; Islamic origins and a Renaissance redesign under Charles I and Felipe II. **Al-Mu'tamid**, the 11th-century Abbadid king of Seville and a poet; his palace was **al-Mubarak, "the Blessed"**. In **1091** the Almoravids banished him to **Aghmat** in Morocco, where he died in **1095**. **No quotation** unless taken from a sourced translation with the translator credited. The column (36): describe it and its inscription only as photographed (O19). The **garden end of the Muñecas passage** (O19). **NOT:** "he wanted to be buried in Seville"; the "Allah grant that I may die in Sevilla" epigraph; "17 hectares"; "oranges descended from Almohad plantings"; "Persian cypresses"; "trees older than four centuries"; temperature-drop claims. | GAC OFF · HIST OFF · EXPO OFF · ARAM SEC · MERC OFF | Back along the garden front past **number 37, the Fuente de Troya**, to **number 38, the Jardín de la Danza**: two columns stand on its upper level. [O19, O20] | – |
| 024 | R | The gardens | No. 38 · Jardín de la Danza | 38 · Jardín de la Danza — Water from Carmona | The Italianate gardens "**de las Damas, la Danza, Troya, Galera y Flores**" (leaflet). A Renaissance redesign under Charles I and Felipe II. The Danza's **two columns on the upper level**, repaired in 2024. Water came by the **old Carmona aqueduct**. Felipe III's opening from the Baths onto this garden. The Fuente de Troya: only what O19 sees. **NOT:** "springs north of the city"; "still fed from…"; any story behind the name "Danza" (none sourced); storm closures. | LEAF OFF · EXPO OFF · ITIN OFF · BANOS OFF | Up the steps to **number 39, the Estanque de Mercurio**: the big raised pool with a bronze god in the middle. [O20] | – |
| 025 | W | The gardens | No. 39 · Estanque de Mercurio | 39 · Estanque de Mercurio — Mercury and his twin | The pool is of Islamic origin, redesigned, and fed by the Carmona aqueduct. The statue was **designed by Diego de Pesquera and cast by Bartolomé Morel**, the founder of the Giraldillo, and **added in 1576**. Restoration ran Nov 2022 to 2024; the pool was refilled in Feb 2024 and shown restored in 2025. **The figure in the pool today is a faithful bronze replica**: 3D-scanned, printed in PLA, lost-wax cast by FundirMetal Amando, gilded by electroplating. Traces of gilding were found on the original. **Where the original is now: say nothing** (O21). One optional line: in Game of Thrones, Doran Martell sits by the Grutesco in front of this pool. **NOT:** "1573"; "designed by Morel, cast by Pesquera"; "the original stands in the pool"; "the original is in a museum"; "the Giraldillo five years earlier"; "still fed by springs". **DATED:** the April 2024 plan to show the original again (one cuttable sentence, or omit). | EXPO OFF · MERC OFF · VIV SEC · AFC OFF | **Number 40, the Galería del Grutesco**: the long painted gallery wall along one side of this pool. [O22] | H E |
| 026 | W | The gardens | No. 40 · Galería del Grutesco | 40 · Galería del Grutesco — An old wall in costume | **Vermondo Resta** turned the old Islamic wall into the Grutesco, **1613–1621**. **Diego de Esquivel** spent seven years painting it and **finished in 1629**. It stands on the pool's **east** side (EXPO; spoken only if O22 confirms it is useful). Restored from **July 2023** (MARVE). Describe the paintings' subjects only as seen. Whether the upper walk is open: O22. **NOT:** "1593–1612"; "south of the pond"; "an Italian at the Spanish court" (Resta's origin is SNIP: omit); "restored in the 1990s"; named fresco subjects unless seen. | EXPO OFF | **Number 41, the Fuente de la Fama**, has a short Extra on its water organ [O22]. The next main stop is **number 44, the Pabellón de Carlos V**: a small tiled pavilion in the lower gardens. [O24] | E |
| 027 | X | The gardens | No. 41 · Fuente de la Fama | 41 · Extra · The water organ | "The **only 17th-century organ fountain preserved in Spain**" (Patronato). Its hydraulic mechanism moved air to make sound. **Restored in 2006** by the Italian archaeology professor **Leonardo Lombardi**, with the British craftsman **Rodney Briscoe**. The restored organ runs automatically on air pressure produced by water. **Never promise it will play**, and give no times. | ORG OFF | On to **number 44, the Pabellón de Carlos V**: the small tiled pavilion. [O22, O24] | – |
| 028 | W | The gardens | No. 44 · Pabellón de Carlos V | 44 · Pabellón de Carlos V — A pavilion for a wedding | It began as a **Muslim qubba**. By **Juan Hernández**, built **in honour of the 1526 marriage**, in the 1540s. Tiles from the **Polido workshop**; **its floor traces an old labyrinth**. Charles never came back to Seville after 1526. **DATED, two versions; record one after O24:** (a) "After a full restoration, the pavilion is open again…"; (b) "If it is still behind screens, look at its tiled outer walls…" (ALT-F). **NOT:** "Charles used it as a retreat" or "dined here"; "converted 1543–46 from an Almohad qubba" as fact; "the oldest standing building in the gardens"; "500 years of use"; the Myrcella–Trystane kiss; the cost of the works. | CENC5 OFF · VIV SEC · AFC OFF | Stay here for a short Extra on **Dorne: the Alcázar on screen**. The next main stop is **number 45, the Cenador del León**: a pavilion behind a pool presided over by a lion. [O25] | E |
| 029 | X | The gardens | No. 44 · Pabellón de Carlos V | 44 · Extra · Dorne: the Alcázar on screen | Filmed in **October 2014 for Game of Thrones season 5** (aired 2015). The scenes, as the Film Commission gives them: the **Salón de los Embajadores** is Prince Doran Martell's hall, where Jaime is brought before him; **Doran, Areo Hotah and Ellaria at the Grutesco in front of the Mercury pool**; **Myrcella and Trystane walk in the Jardín de las Damas**; the **Sand Snakes fight Jaime and Bronn beside this pavilion**; **Ellaria is arrested in the Baths**. Later seasons: the Film Commission lists other GoT years for the site without seasons, so say "season 5" only. **NOT:** "the Sand Snakes plot in the Baths"; "the kiss in the pavilion"; walks in the Doncellas; the Dan Weiss quote; scouting in 2013; "hundreds of thousands of new visitors". | AFC OFF · IBZ SEC | **Number 45, the Cenador del León**: a pavilion behind a pool presided over by a lion. [O25] | – |
| 030 | R | The gardens | No. 45 · Cenador del León | 45 · Cenador del León — The lion's pavilion | Built **1644–45** to designs by **Diego Martín Orejuela**; the painted decoration is by **Juan de Medina**. Named because it stands right behind the pool presided over by the lion. The **pool is older**: it was enlarged in the 16th century and rebuilt after the pavilion went up. Under the plaster, archaeologists found traces of late-medieval heraldic decoration, "**very probably from Pedro I's time**". This is the authors' provisional hypothesis: present it as one. Archaeological watch during the **2017 restoration**. **NOT:** the hypothesis as fact; details of the lion that O25 has not seen. | TAB18 OFF | **Number 46, the Jardín Inglés**, has a short Extra on the twentieth-century gardens. The next main stop is **number 51, the Puerta de Marchena**: a Gothic stone gateway standing in the garden, with carved wild men holding shields. [O26, O27] | – |
| 031 | X | The gardens | No. 46 · Jardín Inglés | 46 · Extra · The twentieth-century gardens | The English Garden: "a sample of the styles that dominated at the start of the 20th century" (leaflet). The **Vega Inclán garden (50)** is in the French style (leaflet). The **Marquis de la Vega-Inclán bought the Marchena gateway on behalf of King Alfonso XIII "to place it in the new gardens"**. The Laberinto (47): only what O26 sees. **NOT:** "nineteenth-century English gardens"; designers' names; "17 hectares"; Vega-Inclán's role in the 1918–20 Yeso restoration (unsourced). | LEAF OFF · MARCH OFF | Through **number 47, the Jardín del Laberinto**, and on (past numbers 48 to 50) to **number 51, the Puerta de Marchena**: the Gothic gateway with wild men holding shields. [O26, O27] | – |
| 032 | R | The gardens | No. 51 · Puerta de Marchena | 51 · Puerta de Marchena — A gateway that travelled | The **former front of the Dukes of Arcos's palace in Marchena**. **Built in 1492**, under Isabel I, and **reformed in 1540**: the arms were changed for a new family line, and the **wild-man figures holding shields** were added. **Sculptures by Esteban Jamete, datable to 1544**; its design may be linked to **Juan Guas**. Owned by the Dukes of Osuna from the 1700s. **The Marquis de la Vega-Inclán bought it on behalf of Alfonso XIII** for the Alcázar's new gardens. Gothic decoration, Renaissance heraldry, Mudéjar traits. The **Jardín Marqués de la Vega Inclán (50)**, French style, lies around it (O27). **NOT:** a purchase year (none sourced). | MARCH OFF · LEAF OFF | Follow the **Salida** signs, past **number 52, the Jardín de la Alcubilla**, to **number 53, the Apeadero**: the covered way out to the Patio de Banderas. [O27, O28] | – |
| 033 | CLOSE | Closing | No. 53 · Apeadero | 53 · Apeadero — The way out | Play inside or just beyond the Apeadero [O28]. You leave through the Apeadero into the **Patio de Banderas**, which lies in the **oldest walled enclosure** of the Alcázar (its wall is 11th-century, possibly Almoravid). Under it, excavations in 2009–13 found a **Roman building of the 1st century BC**, about 5 m down. Recap of the layers: Almohad, Gothic, Mudéjar, Renaissance, 20th century. Nearby, without logistics: the Cathedral, and the Archivo de Indias, "across the plaza", which holds the Contratación's papers (callback to 008). A Giralda view only if O28 confirms it. Position the Patio de Banderas only as O28 confirms (research: "the square just east of where you came in"). **NOT:** "the small plaza on the south side"; "Abd al-Rahman III's ninth-century fort"; "913 masonry"; "admission is free"; prices, hours, bus times; re-entry advice; orange blossom "at exactly this moment"; Santa Cruz "a Jewish quarter until 1492" (say "the old Jewish quarter"); Casa de Pilatos "consensus"; Itálica claims; the shop. | TAB16 OFF · DIV SEC · PREP OFF · EUT SEC · LEAF OFF | — (end of the guide) | H E |
| 034 | X CRA | Optional: Cuarto Real Alto | No. 20 · Dormitorio de Isabel la Católica | CRA 20 · Extra · Isabel's rooms and a tiled altar | Opening line: listen at the foot of **number 19, the stair to the Cuarto Real Alto**, before going up, or afterwards; play it upstairs only if O13 allows. The Cuarto Real Alto is the **upper floor of Pedro's palace** (leaflet rooms 20–30). It was remodelled for Isabel the Catholic (SEC, hedged: "built for"). In **number 21, the Capilla de Isabel la Católica**: a **tiled altar made in 1504 by Francisco Niculoso Pisano** (OFF), showing **the Visitation framed by the Tree of Jesse** (SEC). Pisano, an Italian-born ceramicist working in Seville. Today the upper floor is the **Royal Family's official residence in Seville**, where the King stays on official visits and holds official events. **NOT:** "the Annunciation"; "Isabel knelt here regularly"; "the 1470s"; "Charles V spent much of his Spanish residency here"; Felipe II's childhood; "fifteen rooms"; photography, slots, arrival or bag rules; Versailles or Hampton Court comparisons. | ANDO OFF · RIBA SEC · LEAF OFF · ANDC SEC · ELD SEC | The next Cuarto Real Alto stop is **number 23, the Comedor de Gala**: the long state dining room. [O13] | CRA |
| 035 | X CRA | Optional: Cuarto Real Alto | No. 23 · Comedor de Gala | CRA 23 · Extra · Where the King still dines | Rooms **22 Antecomedor, 23 Comedor de Gala, 24 Sala de Fumar** (leaflet). In the **19th century the Bourbon monarchs added rooms on the top floor** and refurbished old ones **with tapestries and crystal lamps from La Granja** (OFF). The upper floor is the head of state's official residence in Andalucía, with bedrooms, a sitting room, an office, an oratory and original royal furniture; the **King stays here and holds official events** (SEC). Describe only what O13 sees. **NOT:** the royals' private habits; "the lawnmower"; "cleaned every week"; Isabel II's rooms or the billiard room (unsourced); visitor caps. | ANDO OFF · ELD SEC · LEAF OFF | That is the end of the Cuarto Real Alto stops. Back downstairs, pick up the main tour where you left it, usually at **number 18, the Patio de las Muñecas**. [O13] | CRA |

**Held (not in the guide; restore only with a source):** 8–9 Patio del Asistente / Patio de Levíes · 11–12 Alcoba Real / Salón de los Pasos Perdidos (one SEC line: the Alcoba Real is "two chambers used by the king") · 42–43 Fuente de Neptuno / Gruta de las Sultanas · 48–49 Puerta de la Alcoba / Jardín de los Poetas · 52 Jardín de la Alcubilla · CRA 25 Mirador de los Reyes Católicos · CRA 26–28 Dormitorio de Pedro I, Antesala and Sala de Audiencias · CRA 29–30 Sala de Billar and the Colección Carranza (Triana pottery and tiles; Pleguezuelo 2002 catalogue).

## 3. Lengths

Midpoints: W 300 · R 230 · X 190 · ANCHOR/CLOSE 320 words, at 125 words/min. **Walking** is my estimate for the route at visitor pace in crowds. Without the map it is rough, and it needs the stopwatch walk (O29).

### Walking estimate by segment (minutes)
| Segment | Full | E | H |
|---|---|---|---|
| Plaza del Triunfo → Patio del León (1) | 1 | 1 | 1 |
| 1 → 2 → 3 → back → Montería (4) (H: 1 → 4 direct) | 3 | 3 | 1 |
| Montería → 6 → 7 → back to the palace door | 4 | 4 | 4 |
| Doncellas (10) → 13/14 → 15 → 16/17 → 18 (+ Cuarto del Príncipe) | 3 | 2 | 2 |
| 18 → back to the Montería → Crucero (31) [O12] | 3 | 3 | 3 |
| 31 → 32 (+ chapel) → 33 → garden → Danza (38) → Baths (34) | 4 | 4 | 4 |
| Baths → west to 35/36 and back via 37/38 → Mercury (39) (E, H: Baths → 39 direct) | 5 | 1 | 1 |
| 39 → 40 (+ 41) → 44 | 4 | 3 | – |
| 44 → 45 → 46/47 → 48–50 → 51 → 52 → 53 | 12 | – | – |
| 44 → 53 by the signed way (E) / 39 → 53 (H) [O28] | – | 6 | 5 |
| 53 → Patio de Banderas | 1 | 1 | 1 |
| **Total** | **≈ 40 (40–45)** | **≈ 28 (27–29)** | **≈ 22 (20–22)** |

### Counts
| Version | Tracks | W | R | X | ANCHOR+CLOSE | Words | Listening | Walking | **Visit** |
|---|---|---|---|---|---|---|---|---|---|
| Full | 33 | 17 | 7 | 7 | 2 | ≈ 8,680 | ≈ 69 min | ≈ 40–45 min | **≈ 110–115 min** |
| Essential | 20 | 16 | 2 | 0 | 2 | ≈ 5,900 | ≈ 47 min | ≈ 27–29 min | **≈ 74–76 min** |
| Highlights | 10 | 8 | 0 | 0 | 2 | ≈ 3,040 | ≈ 24 min | ≈ 20–22 min | **≈ 44–46 min** |
| Cuarto Real Alto (optional) | 2 | – | – | 2 | – | ≈ 380 | ≈ 3 min | during the upstairs visit | outside the lengths |

**Why the word totals are below the skeleton's.**
- Walking takes longer than the skeleton assumed: the Full garden loop alone is ≈ 12 min. So Essential and Highlights need fewer words to land on 75 and 45 min.
- Full is short because five Extras cannot be sourced.
- **Full lands at ≈ 110–115 min, not ≈ 120.** Ways to close the gap (lead's call):
  - (a) restore held Extras as O5, O8, O23 and O27 yield official panel text (+1.5 min each);
  - (b) let Full-only R tracks with rich sources (003, 030, 032) run to the top of the R range (+≈ 1 min);
  - (c) accept ≈ 115 min and say "about two hours" in 001.
  - Don't pad.

### Highlights (10 tracks, ≈ 3,040 words)
| # | @room | Type | Words |
|---|---|---|---|
| 001 | Outside · Puerta del León | ANCHOR | 320 |
| 007 | No. 5 · Fachada del Palacio del Rey Don Pedro | W | 300 |
| 009 | No. 7 · Capilla de la Virgen de los Navegantes | W | 300 |
| 011 | No. 10 · Patio de las Doncellas | W | 300 |
| 013 | No. 15 · Salón de los Embajadores | W | 300 |
| 014 | No. 15 · Salón de los Embajadores | W | 300 |
| 016 | No. 18 · Patio de las Muñecas | W | 300 |
| 022 | No. 34 · Baños de Doña María de Padilla | W | 300 |
| 025 | No. 39 · Estanque de Mercurio | W | 300 |
| 033 | No. 53 · Apeadero | CLOSE | 320 |

### Essential (20 tracks, ≈ 5,900 words). Every Highlights track plus:
| # | @room | Type | Words |
|---|---|---|---|
| 002 | No. 1 · Patio del León | W | 300 |
| 004 | No. 2 · Sala de la Justicia | R | 230 |
| 005 | No. 3 · Patio del Yeso | W | 300 |
| 008 | No. 6 · Cuarto del Almirante | W | 300 |
| 010 | No. 10 · Patio de las Doncellas | W | 300 |
| 018 | No. 31 · Patio del Crucero | W | 300 |
| 019 | No. 32 · Salón de los Tapices y Capilla | W | 300 |
| 021 | No. 33 · Sala de las Bóvedas | R | 230 |
| 026 | No. 40 · Galería del Grutesco | W | 300 |
| 028 | No. 44 · Pabellón de Carlos V | W | 300 |

Full order of Essential: 001 002 004 005 007 008 009 010 011 013 014 016 018 019 021 022 025 026 028 033.
Full order of Highlights: 001 007 009 011 013 014 016 022 025 033.

**Membership changes from the skeleton**, all for time:
- Highlights loses S002 (Lion Gate; the gate is still named in 001) and S020 (Tapestries; Highlights still walks through the Gothic palace, and the Baths track gives its context).
- Essential loses S005 (Montería; it overlaps 007), S024 (Príncipe) and S025 (Danza) (the garden-front out-and-back, ≈ 4 min of walking), and S032 (English garden; the outer loop, ≈ 6 min).
- If the stopwatch walk (O29) comes in shorter than estimated, add back in this order: E 023 (Príncipe, +3.5 min including walking), then H 019 (Tapestries, +2.4 min).

### Bridges (spoken "next stop" lines for the shorter versions; writers draft them later)
A bridge is appended after the track's normal cue in that version, and the track itself is unchanged. So every bridge must make sense right after the normal cue ("On this shorter tour, skip…: …"). A bridge is needed only where the next track in that version is not the Full cue's next main stop. Extras need no bridge (skipped silently). Every bridge inherits its cue's [Oxx] tags.

| Track | Version | Next in that version | Bridge destination (number + Spanish name + thing to look for) |
|---|---|---|---|
| 001 | H | 007 | Through number 1, the Patio del León, and its triple arch into number 4, the Patio de la Montería. Stop at number 5, the palace façade, with its bands of lettering (002–006 skipped) [O2, O4, O6] |
| 002 | E | 004 | Number 2, the Sala de la Justicia, off this courtyard: the small square hall with a fountain in its floor (003 skipped) [O2] |
| 005 | E | 007 | Back through the Patio del León and its triple arch into number 4, the Patio de la Montería, and up to number 5, the façade, with its bands of lettering (006 skipped) [O3, O4] |
| 007 | H | 009 | Into number 6, the Cuarto del Almirante, and through to number 7, its chapel: the Virgin spreading her cloak over a crowd (008 skipped) [O4, O5] |
| 016 | H | 022 | Follow the signs to the Gothic palace, number 31, through its halls, numbers 32 and 33, and out into the gardens. Go down into number 38, the Jardín de la Danza; number 34, the Baths, opens off it: a long pool under Gothic vaults (017–021 skipped) [O12, O17, O18] |
| 022 | E, H | 025 | Back out into the Jardín de la Danza and up the steps to number 39, the Estanque de Mercurio: the bronze Mercury in the middle of the pool (023–024 skipped) [O20] |
| 025 | H | 033 | Follow the Salida signs to number 53, the Apeadero, the covered way out to the Patio de Banderas (026–032 skipped) [O28] |
| 028 | E | 033 | Follow the Salida signs to number 53, the Apeadero (029–032 skipped) [O28] |

**Never-skip rule:** 001 (the way in and the map convention) and 033 (the way out) are in all three lengths. The 016 H bridge carries the most important instruction in Highlights, the route from Pedro's palace through the Gothic palace to the Baths. It is recorded only after O12, O17 and O18.

## 4. NEVER

**Never send people:**
- through the Muñecas → Jardín del Príncipe passage (017 and 023 point it out only), unless O11 makes ALT-B the route;
- up the stair to the Cuarto Real Alto (19) as part of the main route. The CRA section is optional, and we never tell anyone how to get in;
- through the Patio de Banderas **before** the end. It is the exit, and there is no re-admission. Never advise leaving and coming back;
- to the shop or café (the shops are closed: notice of 19 Oct 2026);
- to the planned Seville-residents' entrance (Casas 7 y 8 of the Patio de Banderas: not built).

**Never in speech:**
- prices, hours, tickets, booking, time slots, queues, security, bag storage, visitor caps, "free entry", "the free hour";
- the 19 Oct 2026 shop closure, or any shop;
- left/right or "straight ahead" that MAP/ONSITE has not confirmed;
- "number 11" (printed twice on the drawing);
- "next track";
- any "on this day" or "this year" hook: 30 October is the anniversary of the battle of Salado, and 2026 is the wedding's 500th year (one cuttable DATED sentence at most, in 014);
- cross-tour assumptions ("we visited yesterday", "the tower you climbed").

**Banned claims:**
- María de Padilla **bathed in the Baths**, "held court" or "lived" in the Muñecas, or married Pedro secretly in 1361.
- An **"Almohad" or 12th-century Lion Gate**; walls or masonry "from 913"; "ninth-century walls".
- **Ali al-Gumari** and the Patio del Yeso (unsourced).
- The **Al-Mu'tamid quotation** "Allah grant that I may die in Sevilla…", or any other verse, unless it comes with a sourced translation and translator.
- **Game of Thrones swaps:** Sand Snakes "plotting" in the Baths (it is Ellaria's arrest); the Myrcella–Trystane kiss in the pavilion (it is the fight scene; they walk in the Jardín de las Damas); walks in the Doncellas; the Dan Weiss quote.
- "Almohad cisterns" for the Baths; "the same brick as the Giralda".
- Mercury "1573", "by Morel after Pesquera", "the original in the pool", or any location for the original.
- Grutesco "1593–1612", "south of the pond", "restored in the 1990s".
- Charles V "used", "dined in" or "retreated to" the pavilion; Charles "lived in the Cuarto Real Alto".
- The wedding errors: Madrid, Isabel "23", "Isabel of Aragon", the Mexía quote, the memoir, the cathedral Mass, Felipe II "born nine months later".
- "Court of the Lions just finished" before 1364.
- Muhammad V sheltered in Seville in 1359; Constanza ordering Pedro's reburial.
- Doncellas columns as Roman spolia; "T-shaped pool"; "cathedral chapter".
- Muñecas upper floors "by Felipe II"; Henry VII / "every English monarch" / "Henry VIII's mother".
- "Renaissance dome"; "wooden balconies"; "16-sided, one of five"; "56 kings".
- "Six tapestries"; "woven in the 1730s"; "originals in storage".
- The Annunciation (it is the Visitation); "Isabel knelt here regularly".
- "The royal baby died at 19 days" (andalucia.com error).
- "17 hectares"; "the first depiction of the Americas"; "seven ship types"; "ran the entire empire".
- "The Patio de Banderas, on the south side".
- Unverified sensory claims ("fifteen degrees cooler", "listen: designed to sound like this").
- The old guide's sources note ("every claim verified").
- Exhibitions: Espacio Santa Clara (over), "Los libros del Emperador", the Marco Polo / Atlas Miller show in the Sala Cantarera (none confirmed on the route now).

## 5. ONSITE + MAP checklist (also in `v5/ONSITE_CHECKLIST.txt`)

**MAP (desk, as soon as the leaflet image arrives; save it as `research/map/`):**
- **MAP-1 — Leaflet availability.** Is the Nov 2024 tríptico still the current edition? Is it handed out on paper at the Puerta del León, or only downloadable ("Prepara la visita" says to print it)? If visitors may not hold it, the app must show the plan: the lead should ask the Patronato for permission to reproduce it, and 001 must say where the numbers are. (001; all cues)
- **MAP-2 — Every provisional relation on the drawing:**
  - the Montería: which side is the Cuarto del Almirante (6) (research: west, right when facing the façade), the gallery to the Crucero (31) and the Apeadero (53);
  - the doors from the Doncellas to 13 and 15;
  - the sequence 15 → 16 → 17 → 18;
  - the stair (19);
  - the Muñecas ↔ Jardín del Príncipe passage;
  - the Bóvedas' garden door;
  - Danza (38) ↔ Baths (34);
  - the sequence 35 → 36 → 37 → 38 → 39;
  - the Grutesco's side of the pool;
  - where the Fama (41) is;
  - 44 → 45 → 46 → 47 → 48–52 → 53;
  - the ENTRADA/SALIDA labels.
  Then rewrite the [Oxx] cues with left/right where the drawing is unambiguous.
- **MAP-3 — The duplicate "11".** Which space carries the second 11? (Cues never say "number 11".)
- **MAP-4 — Service icons** (lifts, toilets, cafeteria, shops): positions, for the step-free notes only.

**ONSITE (one walk of the Full route with the guide before recording):**
- **O1** — Outside the Puerta del León: can a listener stand and play 001 without blocking the entry line? Is the tile lion above the arch visible from there? Where is the paper map, if any (MAP-1)? Where do visitors come out after the security area? (001)
- **O2** — The Patio del León: the triple arch to the Montería; the door into number 2 and its floor fountain; the shield of the Order of the Band (004); any visible trace of the theatre (002); does number 2 lead straight into number 3? (001–004)
- **O3** — The Patio del Yeso: the sebka arcade over the pool; the way back out (through number 2 only?). (005)
- **O4 — CRITICAL: the Montería.**
  - Is the façade (5) in front of you as you come through the triple arch?
  - Where is the door of the Cuarto del Almirante (6)?
  - Is the central door of the façade the visitors' way into the palace?
  - Where is the gallery to the Patio del Crucero (31)?
  - Does the Apeadero (53) open off this courtyard (006's "you'll leave this way")?
  - (005–010, 016–017)
- **O5** — The Cuarto del Almirante:
  - the way from 6 to 7;
  - are 8 and 9 open? Photograph their panels (held Extra);
  - the Virgin on view in 7, with the side panels and predella;
  - which furnishings are there (tapestries, bench): describe only what is seen.
  - (008–009)
- **O6** — The façade: where the Gothic Castilian band and the Kufic blue-and-white tiles are, and whether they can be read from the courtyard. (007)
- **O7 — CRITICAL: the Doncellas.**
  - Scaffolding or closed galleries (the plaster and tile phases are next)?
  - Is the sunken garden visible?
  - The Arabic dado bands: is any panel or label naming the "sultan" inscription?
  - Where to stand at the near end.
  - (009–011)
- **O8** — The door from the Doncellas into 13 (MAK photo); the coffered ceiling with busts; any *malik* inscription; is 14 open? Are 11 and 12 open, with panels (held)? (011–012)
- **O9** — The Embajadores: the iron balconies; the kings' portraits; the doors with the 1366 inscription (visible?); any event set-up. (013–014)
- **O10** — The way from 15 to 16 to 17 to 18, or 15 to 18 direct; where the Peacock Arch is; the ceiling of 17. (014–016)
- **O11 — CRITICAL: the Muñecas, the Cuarto del Príncipe and the passage.**
  - Which arch has the small heads?
  - Is the Cuarto del Príncipe open and signed?
  - Is the passage to the Jardín del Príncipe open, and is it **two-way, or a one-way exit** from the palace? If it is one-way and the palace cannot be re-entered, ALT-B: the lead re-sequences 018–024.
  - (016–017, 023)
- **O12 — CRITICAL:** how do visitors get from the Muñecas to number 31, the Patio del Crucero? Back through the Doncellas and the façade door to the Montería and the gallery (the default cue), or directly from the Doncellas (school itinerary; ALT-C)? What do the signs say? (016–018, 016 H bridge)
- **O13** — The Cuarto Real Alto:
  - where the stair (19) is;
  - where the upstairs visit starts and ends;
  - is commentary given upstairs (a guide, or official audio)? May visitors listen to their own audio upstairs?
  - the room order 20–30; the Pisano altar in 21;
  - photograph the official panels for 25–30 (held Extras).
  - (016, 034–035)
- **O14** — The Patio del Crucero: what visitors see (raised courtyard, walkways); the Baroque front. (018)
- **O15** — The Salón de los Tapices: how many panels are on view; their labels (Vandergoten, dates). (019)
- **O16** — The Gothic palace chapel: where it is (off 32?); the Virgen de la Antigua copy and the Domingo Martínez painting on view. (019–020)
- **O17** — The Sala de las Bóvedas: the tile dado; the two 1929 naval tapestries; the restored sargas; the view through the glass gallery; **where its garden door leads** (the Mercury terrace? the Danza?). (021; ALT-D)
- **O18 — CRITICAL: the Baths.** Entered from number 38, the Jardín de la Danza (default), or from the Crucero (ALT-E)? Open? The same door in and out? Steps (step-free note)? (021–022, 016 H bridge)
- **O19** — The garden front:
  - the walk 38 → 37 → (Galera, Flores) → 35 and back;
  - **the Columna de Al-Mutamid (36)**: what it is, and photograph any inscription or panel (a verse may be quoted only from a credited translation);
  - the Fuente de Troya;
  - is the garden end of the Muñecas passage visible?
  - (022–024)
- **O20** — The Danza: the two columns on the upper level; the Baths' opening; the steps up to the Mercury pool. (023–025)
- **O21** — The Mercury pool: the replica on the pool; any panel on where the original is (on show anywhere?). (025)
- **O22** — The Grutesco:
  - on the pool's east side (useful as a spoken cue?);
  - is the upper walkway open?
  - what the paintings show;
  - where the Fuente de la Fama is and whether the organ sounds (never script times).
  - (025–027)
- **O23** — The Fuente de Neptuno (42) and the Gruta de las Sultanas (43): photograph the panels (held Extra).
- **O24 — CRITICAL: the Pabellón de Carlos V.** Works finished? Interior open? Screens? Tiles and labyrinth floor visible? → record 028(a) or 028(b). (026–029)
- **O25** — The Cenador del León: the lion and the pool; the painted interior visible? (028–030)
- **O26** — The Jardín Inglés and the Laberinto: what can be seen; can the maze be walked; the order 45 → 46 → 47 → 48. (030–031)
- **O27** — The order 48 → 49 → 50 → 51 → 52 on the ground; the wild men holding shields on the Marchena gateway; photograph the panels at 48, 49 and 52 (held Extras). (030–032)
- **O28 — CRITICAL: the exit.**
  - Do visitors leave through the Apeadero (53) into the Patio de Banderas?
  - The Salida signs: the shortest signed way from the Mercury pool (H) and from the Pabellón (E) to 53.
  - One-way, no re-entry (never script re-entry).
  - What to look for in the Apeadero.
  - From the Patio de Banderas, can the Giralda be seen?
  - Is the Patio de Banderas the square "just east of where you came in"?
  - (025, 028, 032–033, bridges)
- **O29** — Time each length with a stopwatch (walking only): H ≈ 20–22 min, E ≈ 27–29, Full ≈ 40–45. Correct 001 and section 3 if far off.
- **O30** — Step-free: steps at the Baths, the Danza, the Mercury terrace, the Grutesco and the Gothic palace; any lifts. (001)
- **O31** — Signage: do the signs on site show the leaflet numbers, or only the Spanish names? (If only names, the cues lean on the names.)
- **O32** — Re-check the notices page the day before the walk (one-off closures, such as the Sala de la Justicia's press-conference morning in Jul 2026; weather closures of the gardens).

## 6. DATED list (cut or revise on these dates; re-read alcazarsevilla.org/noticias before recording)

| Date / trigger | Item | Track(s) |
|---|---|---|
| 31 Dec 2026 | The 500th-anniversary year of the 1526 wedding (V Centenario programme) ends. Cut or rewrite the one "2026" sentence | 014 |
| Pabellón reopening (unknown; works "advancing" 1 Jul 2026, "recovered" 20 Jul 2026, both SEC) | Choose 028(a) open or 028(b) screened; re-check before every re-record | 028, 029 |
| Doncellas restoration phases (flat ceilings done; plaster and tiles "in the next phases", SEC Jul 2026) | Scaffolding sentence in or out | 010, 011 |
| The Mercury original (Apr 2024 plan to restore it and show it again, SEC) | If it goes on show, add one sentence saying where | 025 |
| The Muñecas passage (opened Mar 2025) | Say "since 2025"; if it becomes one-way or closes, revise 017/023 (and ALT-B) | 017, 023 |
| Sargas of the Salón Gótico restored (SEC, Jul 2026) | "Recently restored" until end 2027 | 021 |
| The Grutesco paintings restored from Jul 2023; the Danza columns repaired 2024; the Mercury pool restored 2022–25 | Drop "recent" wording after 2027 | 024, 025, 026 |
| Shops closed (notice of 19 Oct 2026, no reopening date) | Never mentioned; nothing to revise | – |
| Seville-residents' entrance via Casas 7 y 8 (announced Jun 2026, not built) | If it opens and changes the entry or exit flow, re-check O1/O28 | 001, 033 |
| Exhibitions ("Los libros del Emperador", 2026; Marco Polo in the Sala Cantarera, 2025) | Not used; if one opens on the route, ignore it unless the lead decides otherwise | – |
| Nov–Dec (yearly) | Christmas recitals in the Salón de Embajadores: possible set-ups; not mentioned | 013–014 |
| Cuarto Real Alto visit format (separate, timed) | If the format changes, re-check 034–035 opening lines | 034, 035 |
| Leaflet edition (Nov 2024) | **If a new edition renumbers the spaces, every @room, @title and cue changes**: check on every re-record | all |

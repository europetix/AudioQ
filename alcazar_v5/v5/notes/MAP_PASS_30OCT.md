# Map pass, 30 Oct 2026: Real Alcázar EN, tracks 001–035

**What was done.** I read the leaflet's drawing (`source/triptico_alcazar_sevilla.pdf`, page 2), using `research/map/t-2.png` (whole plan), `crop_palaces.png` and crops of `hi-2.png` (300 dpi, zoomed 2–8×). I walked the route on it in track order and wrote into the cues, `@where` lines and bridges every direction that the drawing shows unambiguously. Where it is unclear, the wording stays number-and-name and the ONSITE item stays open.

**Rules kept.**
- Directions are relative to the visitor's direction of travel at that point. No compass points are spoken: the drawing has no compass.
- Every cue still gives the leaflet number and the Spanish name. Nothing is renumbered, and no fact is changed. The one placement correction (the stair, 19) comes from the drawing itself.
- `python3 v5/lint.py` prints OK for all 35 tracks.
- Bridges are still one sentence each, 15–40 words, starting "On this shorter tour,".

## 1. What the drawing settles, and what it does not

**Notes on the source.**
- The PDF's drawing is an Illustrator file dated **14 Mar 2016**. Page 1 still gives the old patronato-alcazarsevilla.es address. The file was re-uploaded in Nov 2024.
- It does **not** show the Muñecas → Jardín del Príncipe passage, which reopened in Mar 2025. It does not show the restored Mercury pool's state either, though that does not affect directions.

**How the plan was oriented.**
- Page 1 says the Italianate gardens "se extienden hacia el Sur", with the Vega Inclán garden to the east and the English garden to the west.
- On the plan, therefore, left ≈ north, up ≈ east, right ≈ south and down ≈ west. This was used only to check the brief's notes, never in speech.
- The brief's notes all match the drawing: 35 south of Pedro's palace; 36 and 37 along its east side; 31 the green courtyard between the Montería and the orange Gothic palace; 34 opening at the garden side of 33 next to 38; 39–40 to the north-east; 53 leading to the Patio de Banderas (SALIDA).

**Settled (drawn, used in the cues):**
- **Patio del León (1).** Four garden beds. The triple arch fills its far end. Sala de la Justicia (2) opens off its far left-hand corner as you face the arch. 3 is reached only through the far side of 2. Coming back out of 2, the arch is on your left.
- **Montería (4).** From the arch, the façade (5) faces you across the courtyard.
  - The Cuarto del Almirante (6) runs along the right-hand side behind a row of columns, with 7 at its far end.
  - The palace door is in the middle of the façade. Coming out of 6, it is to your right.
  - In the far left-hand corner, where the façade ends, a range (grey on the plan, with toilets) has doorways from the Montería and two doorways into the Crucero (31).
  - **The Apeadero (53) does not open off the Montería.** A corridor beside the Crucero leads to it.
- **Stair 19.** An arrow points to the corner of the Montería where the façade meets the Cuarto del Almirante. It is **not** "near the Muñecas", as the leaflet order had suggested.
- **Pedro's palace.** The palace door leads into a bent passage. That passage turns into a corner of the Doncellas (10), and also has an opening into the grey range (the ALT-C inner link).
  - The Doncellas is drawn longer than wide (≈ 400 : 285 on the crop). From the entry corner it runs away from you: 13 is the long room along the long side on your left, and 15 is at the far end.
- **Gothic palace.** 31 has four garden beds, and the Gothic palace runs along its right-hand side as you come in from the range, behind a portico.
  - 32 and 33 are two parallel long halls, 33 on the garden side.
  - 33's garden front is drawn open (a thin line, not a wall).
  - The **arrow for 34** points to an opening in the palace wall on the garden side of 33, at the head of the Danza (38). Coming out of 33, it is on your right.
- **Garden front.** Each step has a drawn opening:
  - 38 → 37, a small courtyard with a fountain;
  - 37 → 36, narrow beds along the palace's side;
  - 36 → an unnumbered garden with a small fountain;
  - then a colonnade on your right → 35, four beds round a small fountain, below the palace.
  - Walking out, the palace is on your right. Coming back, it is on your left.
  - 37 also has an open colonnade on its outer side onto the big formal garden (42).
- **Mercury pool and beyond.**
  - The Grutesco (40) is the long wall on the far side of the Mercury pool (39) from the Danza.
  - The Fama (41) is a semicircular niche in the same wall, beyond the end of the pool.
  - The Pabellón (44) stands in an open space at the far end of the formal gardens that run away from that wall. The Cenador del León (45) and its pool close that space.
  - The Jardín Inglés (46), with winding paths, lies beyond the Cenador. The Laberinto (47) is on the Cenador's other side.
  - 48 is in the far corner. 49 and 50 come back along the outer side. 51 stands near the head of the Grutesco wall, with the Alcubilla beds (52) just beyond it.
  - The Apeadero (53) is a columned hall with SALIDA printed at its outer end, towards the Patio de Banderas.
- **MAP-3.** The second "11" is printed in the Cuarto Real Alto inset, on the open courtyard that the upper rooms are drawn round.
- **MAP-4.**
  - Shops: at the León gatehouse and beside the Apeadero.
  - Toilets: in the Montería–Crucero range, by the Callejón del Agua wall near 50, and by 48.
  - Cafeteria: by the Callejón del Agua wall.
  - No lifts are drawn.

**Not settled, so the wording stays number-and-name and the ONSITE item stays open:**
- the doorways of the loop 15 → 16 → 17 → 18 (O10);
- the exact door of 13 (O8; the side is now spoken);
- the passage (O11);
- whether signs use the palace door or the inner link (O12);
- the exact garden door of 33 (O17);
- the column itself at 36 (O19);
- the steps between 38 and 39 (not drawn; O20);
- the path from 41 to 44 (O22);
- the signed exit route from 39 and 44 (O28; the drawing shows a passage from the pool's corner along the Gothic palace towards 52–53, but not whether it is signed);
- MAP-1: whether a paper copy is handed out, and whether a newer edition exists.

## 2. Route decision: Muñecas → Gothic palace → gardens

**Decision: keep order A, unchanged and now drawn link by link.**

18 → back through the Doncellas and out of the palace door → turn right, palace front on your right, to the corner → the range → **31** → the portico → **32** → **33** → out on the garden side → **34**, on your right at the head of the Danza → down the **Danza (38)**, palace on your right, through **37** and **36** → the colonnade on your right → **35** → back the same way, palace on your left → **38** → up the steps at its head → **39**.

**Why A.**
1. Every link it uses is drawn: the façade door; the Montería → range → 31 doorways; the portico; 32 beside 33; 33's open garden front; the opening at 34; the garden-front openings and the colonnade.
2. Its only backtracking is the garden-front strip 38 ↔ 35 (≈ 4 min, Full only) and the short way from the Muñecas back to the palace door. Essential and Highlights go straight from the Baths up to 39.
3. It does not use the passage in either direction. Its one-way status (O11) cannot break the route.
4. It keeps the leaflet order 31 → 32 → 33 → 34 and the scripts' order (018 introduces Alfonso X's palace, and 022 says the Baths lie under the courtyard "of the Gothic palace above your head"). **Nothing is renumbered.** PLAN's lengths and bridge positions are unchanged.

**Why not ALT-B** (Muñecas → passage → 35 → 36 → 37 → 38 → 34 → Gothic palace from the garden):
- After the Baths, 31–33 can be entered only through 33's garden front, used in reverse. The drawing shows no other garden-side opening.
- From 31 the only other way out is the corridor to the Apeadero (53), which is the exit. So the visitor must walk back out through 33 and 32 to the garden to reach 39.
- That means a double pass through the Gothic halls, the leaflet numbers walked backwards (33 → 32 → 31), 018–024 re-sequenced, and two doors whose direction rules are unconfirmed (the passage outbound and 33 inbound).
- All this saves only the ≈ 4-minute strip. Rejected. It is held only if O11 and O17 show that A cannot be walked.

**Also considered.**
- From 35, back through 37's outer colonnade into the formal garden and up to 39. This skips 38, where 024 is played, so 023 and 024 would have to swap (renumbering). Rejected.
- Leaving the garden next to 35 by the small gap at its foot into the lower gardens. The gap is too small to read, and the route would scramble 39–44. Rejected.

**The inner link (ALT-C).** The drawing also shows an opening from the palace's entrance passage, at the Doncellas corner, into the range that leads to 31. It is not used in the cue, because it may be a service door. It is written up as ALT-C in PLAN, to swap in if O12 finds that the signs use it.

## 3. Changes to tracks (before → after; changed span only, "…" = unchanged text)

Unchanged tracks: 002 speech, 010 speech, 013, 014, 015, 033, 034. Speech changes are in cues (last paragraph), except the 006 orientation paragraph, the stair sentence in 016 and one sentence cut from 031.

| Track | Line | Before | After |
|---|---|---|---|
| 001 | cue | …a triple arch leading on. | …a triple arch at its far end. |
| 002 | @where | …an open courtyard between the entrance wall and a wall pierced by a triple arch that leads on to the… | …an open courtyard with four garden beds, between the entrance wall and the far wall, which is pierced by a triple arch leading on to the… |
| 003 | cue | …Justicia, opens off this courtyard: a small square… | …Justicia, opens off the far left-hand corner of this courtyard as you face the triple arch: a small square… |
| 004 | @where | …Justicia, off the Patio del León: a small square… | …Justicia, off the far left-hand corner of the Patio del León as you face the triple arch: a small square… |
| 004 | cue | Through to number 3… | Through the far side of this hall to number 3… |
| 005 | @where | …del Yeso, reached through the Sala… | …del Yeso, reached only through the Sala… |
| 005 | cue | …came, through number 1, the Patio del León, and its triple arch into number 4 on the Alcázar map, the Patio de la Montería: the big open courtyard with a tall decorated palace front. | …came, through number 2, the Sala de la Justicia. The triple arch of number 1, the Patio del León, is on your left as you come out. Go through it into number 4 on the Alcázar map, the Patio de la Montería: the big open courtyard, with a tall decorated palace front facing you across it. |
| 006 | @where | …of King Pedro's palace. | …of King Pedro's palace, which faces you across it. The Cuarto del Almirante runs along the right-hand side. |
| 006 | body | Now take your bearings, by what you can see rather than by direction. The tall decorated front is number 5… | Now take your bearings. The tall decorated front facing you is number 5… |
| 006 | body | Also off this courtyard is number 6… | On your right, behind a row of columns, is number 6… |
| 006 | body | [pause] And a porticoed gallery off this courtyard leads to number… | [pause] And in the far left-hand corner, by the palace front, a porticoed gallery leads to number… |
| 007 | cue | …courtyard: the range where the Casa… | …courtyard: the range along its right-hand side as you face the palace front, behind a row of columns, where the Casa… |
| 008 | @where | …Almirante, the range off the Patio de la Montería signed as the… | …Almirante, the range behind a row of columns along the right-hand side of the Patio de la Montería as you face the palace front, signed as the… |
| 008 | cue | …the old audience hall: the Virgin spreading… | …the old audience hall at the far end of this range: the Virgin spreading… |
| 009 | cue | Back across number 4, the Patio de la Montería, and through the palace door in number 5, the façade, into number 10… | Back out into number 4, the Patio de la Montería. The palace door, in the middle of number 5, the façade, is to your right. Go through it and along the bent passage beyond, into number 10… |
| 010 | @where | …de las Doncellas, just inside the palace: a large arcaded… | …de las Doncellas, in the corner where the bent passage from the palace door brings you in: a large arcaded… |
| 011 | cue | …opens off this courtyard. The next main stop is number 15 on the Alcázar map, the Salón de los Embajadores, the hall under the gilded dome. | …opens off this courtyard, in the long side on your left as you look down the courtyard from the corner where you came in. The next main stop is number 15 on the Alcázar map, the Salón de los Embajadores, the hall under the gilded dome, at the far end of the courtyard. |
| 012 | @where | …through its door off the Patio de… | …through its door in the long side of the Patio de… |
| 012 | cue | …Salón de los Embajadores: look up for… | …Salón de los Embajadores, at the far end of the courtyard: look up for… |
| 016 | body | …Real Alto, is near this courtyard. The upper royal… | …Real Alto, is marked back in the Patio de la Montería, in the corner where the palace front meets the Cuarto del Almirante. The upper royal… |
| 016 | cue | …for the Palacio Gótico, back through the Patio de las Doncellas to the Patio de la Montería and along its gallery. | …for the Palacio Gótico: back through the Patio de las Doncellas and out of the palace door into the Patio de la Montería. Turn right, keep the palace front on your right, and walk to the corner. The way through to number 31 is there. |
| 017 | cue | …de las Doncellas to the Patio de la Montería and along its gallery. | …de las Doncellas and out of the palace door into the Patio de la Montería. Turn right, keep the palace front on your right, and walk to the corner. The way through to number 31 is there. |
| 018 | @where | …Crucero, the courtyard in front of the Gothic palace. Look for the… | …Crucero, the courtyard of four garden beds beside the Gothic palace, reached from the corner of the Patio de la Montería. The Gothic palace runs along its right-hand side as you come in. Look for the… |
| 018 | cue | Into number 32, the… | Through the portico on the Gothic palace side of this courtyard, into number 32, the… |
| 019 | cue | …Sala de las Bóvedas: walls tiled to… | …Sala de las Bóvedas, the parallel hall on the garden side: walls tiled to… |
| 020 | cue | …Sala de las Bóvedas: the tiled hall under Gothic vaults. | …Sala de las Bóvedas, the next hall towards the garden: tiled walls under Gothic vaults. |
| 021 | @where | …called the Salón Gótico: a long hall… | …called the Salón Gótico, the hall on the garden side of the Salón de los Tapices: a long hall… |
| 021 | cue | …into the gardens and down into number 38 on the Alcázar map, the Jardín de la Danza. Number 34, the Baños de Doña María de Padilla, opens off it under the palace: a doorway into… | …into the gardens on the hall's garden side, and down into number 38 on the Alcázar map, the Jardín de la Danza. Number 34, the Baños de Doña María de Padilla, opens in the palace wall on your right as you come out, at the head of the Danza: a doorway into… |
| 022 | @where | …entered from the Jardín de la… | …entered from the garden through the palace wall at the head of the Jardín de la… |
| 022 | cue | …the Danza and along the garden front, through the small Italianate gardens, to number 35, the Jardín del Príncipe: look for number 36 on the Alcázar map, the Columna de Al-Mutamid. | …the Danza and walk to its far end, keeping the palace on your right. Go on through the little courtyard of number 37 on the Alcázar map, the Fuente de Troya, and through the garden of number 36 on the Alcázar map, the Columna de Al-Mutamid: look for the column. In the garden beyond, number 35, the Jardín del Príncipe, opens through the colonnade on your right. |
| 023 | @where | …Jardín del Príncipe, at the end of the garden front below the palace, near number 36, the Columna de Al-Mutamid. The garden end… | …Jardín del Príncipe, the garden of four beds round a small fountain below the palace, entered through a colonnade. Number 36, the Columna de Al-Mutamid, is marked in the narrow garden you came through beside the palace. The garden end… |
| 023 | cue | Back along the garden front past number 37 on the Alcázar map, the Fuente de Troya, to number 38, the Jardín de la Danza: two columns stand on… | Back the way you came, through the colonnade, with the palace now on your left: past number 36 and through number 37, the Fuente de Troya, to number 38, the Jardín de la Danza. Two columns stand on… |
| 024 | cue | Up the steps to number 39… | Up the steps at the head of the Danza to number 39… |
| 025 | @where | …gallery wall along one side. | …gallery wall along its far side, opposite the way up from the Danza. |
| 025 | cue | …long painted wall along one side of this pool. | …long painted wall on the far side of this pool, opposite the way you came up. |
| 026 | @where | …that runs along one side of the Mercury pool. | …that runs along the far side of the Mercury pool, opposite the way up from the Jardín de la Danza. |
| 026 | cue | …its water organ. The next main stop is number 44 on the Alcázar map, the Pabellón de Carlos Quinto: a small tiled pavilion in the lower gardens. | …its water organ. It is set into this same long wall, beyond the end of the pool. The next main stop is number 44 on the Alcázar map, the Pabellón de Carlos Quinto: a small square tiled pavilion at the far end of the formal gardens that stretch away from this wall. |
| 027 | @where | …Fama: the fountain that the signs name Fuente de la Fama, the next number on the map after the Grutesco. | …Fama: the fountain in a semicircular niche set into the same long wall as the Grutesco, beyond the end of the Mercury pool. |
| 027 | cue | …Quinto: the small tiled pavilion. | …Quinto: the small square tiled pavilion at the far end of these formal gardens. |
| 028 | @where | …square, tiled pavilion in the garden. | …square, tiled pavilion standing in an open space at the far end of the formal gardens. |
| 028 | cue | …the Cenador del León: a pavilion behind… | …the Cenador del León, just beyond, at the end of this open space: a pavilion behind… |
| 029 | cue | …is the next stop: a pavilion behind… | …is the next stop, just beyond, at the end of this open space: a pavilion behind… |
| 030 | @where | …the Cenador del León: a garden pavilion… | …the Cenador del León, at the end of the open space beyond the Pabellón de Carlos V: a garden pavilion… |
| 030 | cue | …the Jardín Inglés, has a short… | …the Jardín Inglés, the garden of winding paths beyond this pavilion, has a short… |
| 031 | @where | …Inglés, the garden that follows the Cenador del León in the map's numbering; look for the… | …Inglés, the garden of winding paths just beyond the Cenador del León; look for the… |
| 031 | body | [pause] On the way there is a maze garden. Remember the floor… | [pause] Remember the floor… |
| 031 | cue | Go through number 47 on the Alcázar map, the Jardín del Laberinto, and on past numbers 48 to 50. The next… | Back past the Cenador del León, go through number 47 on the Alcázar map, the Jardín del Laberinto. Follow the numbers round: 48 in the far corner, then 49 and 50. The next… |
| 032 | cue | …Salida signs past number 52 on the Alcázar map, the Jardín de la Alcubilla. They lead to… | …Salida signs past the beds of number 52 on the Alcázar map, the Jardín de la Alcubilla, just beyond this gateway. They lead to… |
| 035 | cue | …where you left it, usually at number 18, the Patio de las Muñecas. | …where you left it. The Alcázar map marks the stair, number 19, in the corner of the Patio de la Montería beside the palace front. |

**Why the 031 sentence was cut.** "[pause] On the way there is a maze garden." (8 words) was cut to keep 031 within the X range (≤ 230). The cue now names the maze garden (47) and the route to it.

**Word counts** (spoken, tags excluded), before → after:
- 001 334→336 · 003 255→266 · 004 219→225 · 005 270→292 · 006 276→279 · 007 295→310 · 008 287→294 · 009 327→342 · 011 288→315 · 012 222→229 · 016 318→359 · 017 197→221 · 018 286→297 · 019 288→295 · 020 206→211 · 021 237→254 · 022 302→338 · 023 309→319 · 024 242→248 · 025 296→303 · 026 281→306 · 027 170→179 · 028 263→272 · 029 183→192 · 030 264→272 · 031 226→230 · 032 262→269 · 035 215→227.
- All 35 tracks: 9,240 → 9,602 (+362, ≈ +2.9 min listening in Full). Highlights +143 (≈ +1.1 min), Essential +247 (≈ +2.0 min).
- Tracks at or near the top of their range: 006 (279/280), 012 (229/230), 031 (230/230), 016 (359/360).

## 4. Changes to bridges (`v5/bridges/*.txt`)

| Bridge | Before | After |
|---|---|---|
| 001 H>007 | …go through number 1, the Patio del León, and its triple arch into number 4, the Patio de la Montería, up to number 5, the Fachada del Palacio del Rey Don Pedro, with bands of lettering. | …go through the triple arch of number 1, the Patio del León, and across number 4, the Patio de la Montería, to number 5, the Fachada del Palacio del Rey Don Pedro, facing you. |
| 002 E>004 | …the Sala de la Justicia, opens off this courtyard, a small square hall… | …the Sala de la Justicia, opens off the left-hand corner by the triple arch, a small square hall… |
| 005 E>007 | …walk on up to number 5… | …walk on across it to number 5… |
| 007 H>009 | …and on through to number 7, the Capilla de la Virgen de los Navegantes: the Virgin spreading her cloak over a crowd, with ships at her feet. | …and through to its far end, number 7, the Capilla de la Virgen de los Navegantes, with the Virgin spreading her cloak over a crowd. |
| 016 H>022 | …out to number 38, the Jardín de la Danza, then into the vaulted pool of number 34, the Baños de Doña María de Padilla. | …out to number 38, the Jardín de la Danza, where number 34, the Baños de Doña María de Padilla, opens in the palace wall. |
| 022 E>025, H>025 | …go up the steps to number 39 on the Alcázar map, the Estanque de Mercurio, with a bronze Mercury in the pool. | …go up the steps at its head to number 39 on the Alcázar map, the Estanque de Mercurio, with its bronze Mercury. |

Unchanged: 009 H>011, 025 H>033 and 028 E>033 (the exit route is still O28).

## 5. Changes to PLAN.md

- **Header.** The "drawing not yet available, all geometry PROVISIONAL" paragraph is replaced by a map-pass paragraph. It sets the [MAP] tag rule and notes the 2016 drawing date and the missing passage.
- **Conventions → Directions.** Before: no left/right, "straight ahead" or "far side" until MAP/ONSITE confirm. After: these are allowed only where the map pass settled them ([MAP]), always relative to the direction of travel, never compass points. Any new direction needs MAP or ONSITE.
- **Route section.**
  - "Nos. 1–9" and "Pedro's palace" now carry the drawn relations. The stair (19) moves from "near the Muñecas (leaflet order)" to "the Montería corner (arrow)".
  - "Muñecas → Gothic palace → gardens" goes from "the open question, worked out" to "decided on the drawing: order A stands". It records the evidence, the drawing's five findings, the chosen order, why A, why not ALT-B, and the alternatives rejected.
  - "Gardens 39–53" now carries the drawn layout.
  - "What the map must confirm" is replaced by "Still for the site" (O11, O12, O17, O18, O24, O28).
- **ALT cues.**
  - ALT-C is rewritten for the drawn inner link.
  - ALT-D and ALT-E are marked unlikely, with the reason from the drawing.
  - ALT-B is marked rejected on the drawing.
- **Changes from the skeleton.** Item 10 (map pass) added.
- **Track table.**
  - Cue column updated for 001, 003, 004, 005, 007, 008, 009, 011, 012, 016, 017, 018, 019, 020, 021, 022, 023, 024, 025, 026, 027, 028, 029, 030, 031, 032 and 035. Tags go from [Oxx] to [MAP; Oxx still open].
  - Core-content cells updated for 006 (orientation now from the drawing; 53 does not open off the Montería, so it is not mentioned) and 016 (the stair's position).
- **Section 3.**
  - The walking row "Baths → west to 35/36 and back via 37/38" now reads "Baths → down the Danza through 37 and 36 to 35, and back the same way to 38". The minutes are unchanged.
  - Bridge-table rows 001, 002, 005, 007, 016 and 022 are reworded to match the spoken bridges. Positions and destinations are unchanged.
  - The planned word and time totals in the Counts table are left as planned. The actual delta is in section 3 above.
- **Section 5.** The MAP block is rewritten:
  - MAP-1 partly settled (edition date; the handout is still open);
  - MAP-2 settled except the marked parts;
  - MAP-3 and MAP-4 settled.
  - A note under ONSITE points to the checklist for the item-by-item status.

## 6. Changes to `v5/ONSITE_CHECKLIST.txt`

- **Header.** "Until the map items are done, every left/right is PROVISIONAL" now reads: map pass done; every left/right was read off the drawing ("MAP OK"); check each one on the ground; "STILL" marks what needs the site.
- **MAP block.**
  - MAP-1 [~]: edition finding; the handout and newer-edition questions are still open.
  - MAP-2 [x]: the full list, with STILL notes for 13's door, 15 → 18, the passage, 33's door, the column and 41 → 44.
  - MAP-3 [x] and MAP-4 [x], with answers.
- **O-items** annotated "MAP OK: … STILL: …":
  - O2, O3, O5, O7, O8, O10, O12, O13, O14, O17, O18, O19, O20, O22, O25, O26, O27 and O28.
  - O4 is downgraded from CRITICAL: its geometry is settled, and only the door use is left.
  - O11 is downgraded from CRITICAL: route A does not depend on the passage.
  - O12, O18 and O28 stay CRITICAL.
- **New "DIRECTIONS" block.** One tick per track, so that each drawn direction is confirmed true on the ground before recording.

## 7. For the lead

1. **The stair (19).** The drawing puts it at the Montería corner by the Cuarto del Almirante. 016 and 035 now say "marked … in the Patio de la Montería". O13 confirms the door visitors actually use.
2. **One drawn direction rests on the plan's proportions.** "13 along the long side on your left; 15 at the far end" (011, 012) depends on the Doncellas being drawn longer than wide. It is in the DIRECTIONS ticks.
3. **Full gains ≈ 3 min of listening.** That brings it closer to the 120-minute target (PLAN §3 option (c) still applies). Highlights ≈ +1 min, Essential ≈ +2 min. Re-time at O29.
4. **The leaflet is a 2016 drawing.** If the Patronato issues a new edition, re-check every number (DATED list, last row).

# Fact audit, tracks 031–059 (independent check, 10 Oct 2026)

Method: I listed every load-bearing claim in each spoken body and checked it against the official museodelprado.es page(s) named in the track's @sources header. Pages were fetched one at a time with WebFetch. Room data was cross-checked with research/*_result.tsv and OFFICIAL_LOCATIONS_PRADO_10OCT2026.md. No track was edited.
Verdicts: **WRONG** = the official page (or the painting itself) contradicts the claim. **WEAK** = plausible, but the official page does not support it, or the page says it with less certainty. **UNVERIFIED** = could not be checked.
Only WEAK, WRONG and UNVERIFIED items are listed. Every other claim is OK or FRAMED. Tracks 031, 033, 034, 038, 039, 043, 044, 045, 046, 049 (except one minor item), 053, 055, 056 and 057 checked out fully. FRAMED items (fine as they stand) include the Santiago-cross story in 035, "may be the most silent painting" in 031, and "the king seems not to have minded" in 046.

---

## 032 · Feast of Bacchus
- **WEAK** — "For centuries it has simply been Los Borrachos, the drunks."
  Evidence: the-feast-of-bacchus/4a23d5e2… The 1857 catalogue says "Cuadro conocido con el nombre de los Borrachos", and the 1872–1907 catalogue says "vulgarmente llamado de Los Borrachos, y antiguamente de Baco". The 1701–1814 inventories call it a Bacchus scene, not Los Borrachos.
  Fix: "Since at least the nineteenth century it has simply been Los Borrachos…" (or "For generations…").

## 035 · Las Meninas
- **WEAK (low)** — "José Nieto, the queen's chamberlain."
  Evidence: las-meninas/9fdc7800… calls him only "the chamberlain". "The queen's" (aposentador de la reina) is correct general knowledge, but it is not on the page.
  Fix: optional. Use "the palace chamberlain", or keep as is.
- Visual details that are not on the page but are correct for the painting: María Agustina kneeling with the red jug, and Nicolasito's foot on the mastiff. No change needed.

## 036 · Charles V at Mühlberg / Furies
- **WRONG (minor, mythology)** — "the two dark canvases of giants in torment … Mary chose these punished giants".
  Evidence: sisyphus/bb56eb47… describes the series as those who "rise against the gods". Tityus is a giant, but Sisyphus is a mortal king of Corinth, not a giant.
  Fix: "two dark canvases of figures in eternal torment" and "Mary chose these punished rebels".
- **WEAK (clarity)** — "Two of the four were lost in a palace fire in 1734, and this Tityus is Titian's own later version."
  Evidence: the Sisyphus page says the two destroyed in the 1734 Alcázar fire were Ixion and Tantalus. The tityus/68555098… page says this is "Titian's own late repetition of the original" and does not say the original Tityus burned. As written, a listener may think Tityus was one of the two lost.
  Fix: "The other two, Ixion and Tantalus, were lost in the Alcázar fire of 1734. This Tityus is a later version by Titian himself."
- **WEAK (low)** — "a wheel-lock pistol on the saddle, the latest technology."
  Evidence: the ES page (el-emperador-carlos-v-en-muhlberg/e7c91aaa…) confirms only the "pistola de rueda" fixed to the saddle-bow.
  Fix: cut "the latest technology", or say "then a modern weapon".

## 037 · Veronese, Venus and Adonis
- **Note (no change needed)** — "He acquired it on his second journey to Italy."
  Evidence: venus-and-adonis/692667da… The commentary says the second Italian trip (1649–51), but the page's provenance field says "acquired in Venice in 1643". The page contradicts itself. The track follows the commentary, which is the more plausible version.

## 040 · Room 15, Buffoons
- **WRONG (location)** — "Velázquez gave ancient philosophers the same treatment. Menippus wraps himself in his cloak…" The context (and @what) puts Menippus in Room 15.
  Evidence: menippus/698f7cc0… The technical sheet today reads "Room 012 (On Display)", re-checked with a second fetch. The research TSV recorded 015 earlier, and the Velázquez itinerary already listed 012. Aesop moved the same way.
  Fix: cut the Menippus paragraph from 040, and remove Menippus from @what. Or move the line to 034 (Room 12): "Here too is Menippus, an ancient philosopher dressed like a Madrid beggar, eyeing you sideways."
- **WEAK (visual, low)** — "El Primo sits … legs straight out, fists at his hips."
  Evidence: the-buffoon-el-primo/cc7a8493… The 1872–1907 catalogue quoted on the page puts the fists "junto á las íngles", that is, resting by his groin on his thighs.
  Fix: "fists resting on his thighs".

## 041 · The Spinners / Mars
- **WRONG** — "The strip across the top, with the arch and the round window, was added in the eighteenth century, and it pushes the back room further away." The present tense tells the visitor to look at the strip.
  Evidence: the-spinners-or-the-fable-of-arachne/3d8e510d… quoted verbatim: "a wide strip (with the arch and oculus) was added to the top, along with narrower ones on the left, right and bottom (these additions are not visible in the current presentation of this work)."
  Fix: "In the eighteenth century, strips were added around the canvas, including an arch and a round window at the top. They made the back room seem further away and helped hide the myth. Today's display hides them."
- **WEAK** — "For nearly three centuries, people thought this was a factory scene."
  Evidence: the page says only that viewers "have long seen it" as a workshop scene. It ties that reading to the 18th-century additions, and the 1664 inventory already called it "a Fable of Arachne", so the misreading cannot cover three centuries.
  Fix: "For a long time, people thought this was a factory scene."
- **WEAK (visual)** — Mars "sits on an unmade bed wearing nothing but his helmet".
  Evidence: mars/ec55aa06… says "of his armour … the god only wears his helmet". In the painting a cloth is draped across his lap.
  Fix: "wearing nothing of his armour but his helmet" or "naked but for his helmet and a sheet".

## 042 · Murillo, Soult Immaculate
- **WEAK (low)** — "Later the Louvre bought it."
  Evidence: wd/76179d81… gives "1852: acquired by the Musée du Louvre" and does not say how. The purchase at the Soult sale is general knowledge and correct.
  Fix: optional. Use "Later the Louvre acquired it."

## 047 · Family of Charles IV
- **WEAK** — "Some historians read this as a cruel joke, a family too vain to notice it was being mocked."
  Evidence: the ES page la-familia-de-carlos-iv/f47898fc… says some historians read the queen's pose as "una sátira a la reina, ya mayor". "Too vain to notice" is not on the page.
  Fix: "Some historians read it as a cruel satire of the ageing queen."
- **WEAK (source)** — "The museum is rehanging Rooms 32 to 38, with no date announced."
  Evidence: the only source is a press summary (hoyesarte.com, cited in OFFICIAL_LOCATIONS…md), not museodelprado.es. That summary describes the 32–38 phase as planned with no date, not as under way.
  Fix: "The museum plans to rehang Rooms 32 to 38. If this room is closed or changed…"

## 048 · The Majas
- **WEAK** — "The museum calls both claims rumours."
  Evidence: the-naked-maja/65953b93… ties the Alba claim to rumours of an affair and calls the Pepita Tudó proposal (Madrazo's) unfounded.
  Fix: "The museum says neither claim has any foundation."
- **WEAK (source)** — the rehang line repeats the 047 item. Same fix.

## 049 · Tiepolo, Immaculate Conception
- **WEAK (low)** — "the Venetian Giambattista Tiepolo, who was then working in Madrid."
  Evidence: the-immaculate-conception/8da40987… does not say where Tiepolo was when the work was commissioned. It is correct general knowledge (he was in Madrid 1762–70).
  Fix: none needed, or "who had come to Madrid to paint the palace ceilings".

## 050 · The Parasol
- **WEAK** — "The documents show that at this stage, Goya invented his compositions himself."
  Evidence: the-parasol/a230a80f… says "Goya, himself, invented the specific composition of the present one". The page makes the claim about this cartoon only.
  Fix: "The documents show that Goya invented this composition himself."
- **WEAK (source)** — "These rooms on Floor 2 were rehung this year to bring his cartoons together."
  Evidence: the only source is the hoyesarte.com summary ("rooms 85–94 from spring 2026"). There is no museodelprado.es page for it.
  Fix: "These rooms on Floor 2 bring his cartoons together." Or keep the line if the museum confirms it on site.

## 051 · Summer / Winter
- **WRONG (visual + page)** — "two better-dressed men, probably servants from some great house, carry an enormous gutted pig." @where also says "two others carrying a pig".
  Evidence: the ES page la-nevada-o-el-invierno/4792e788…: "el otro tira de la mula cargada con un cerdo, abierto ya en canal", and the leading man "va armado con una escopeta". The pig is on a mule, not carried.
  Fix: "two better-dressed men, probably servants from some great house: one with a shotgun, the other leading a mule loaded with an enormous gutted pig." In @where: "and a mule loaded with a pig."
- **WRONG (minor)** — "a little group is trying to get a man who's already drunk to drink some more."
  Evidence: the-threshing-ground-or-summer/ec1c94c1… quoted verbatim: "a group of peasants try to inebriate another character … the village idiot". The page does not say he is already drunk.
  Fix: "a little group is trying to get one man drunk."
- **WEAK (low)** — "These cartoons stayed in the royal palaces for most of a century."
  Evidence: the provenance runs from the Royal Tapestry Factory to the Royal Palace basements (1856–57) to the Prado (1870).
  Fix: "These cartoons sat in royal storerooms for most of a century, and came to the Prado in 1870."

## 052 · San Ildefonso Group
- **WEAK** — "They were carved in Rome around 10 BC."
  Evidence: orestes-and-pylades…/a3dbf0c5… gives ca. 10 BC and calls it Roman eclecticism, but it does not say where the group was carved.
  Fix: "They were carved around 10 BC, in the age of the emperor Augustus."
- **WEAK** — "Earlier viewers simply saw what's in front of you: friendship, and a brotherly arm around the shoulder."
  Evidence: the page says "modern observers" read the embrace as friendship and brotherly love.
  Fix: "Many viewers simply see what's in front of you: friendship…"

## 054 · The 2nd of May
- **WEAK** — "The left side was badly damaged, and an early repair made things worse."
  Evidence: the-2nd-of-may…/57dacf2e… says the losses "mainly affected the left part", and "In the first restoration, in 1941 … a red ink was used." It does not say the repair made the damage worse.
  Fix: "The left side lost patches of paint, and the first repair, in 1941, simply filled them with red ink."

## 058 · Sorolla, Boys on the Beach
- **WRONG (overstated)** — "He signed this canvas with the next year's date, but the museum is sure he painted it that summer."
  Evidence: boys-on-the-beach/edd7a202… says it "most likely" dates from summer 1909, based on Doménech's book printed in December 1909, and acknowledges that most scholars have followed the 1910 signature.
  Fix: "…but the museum thinks he most likely painted it that summer."

## 059 · Closing
- **WEAK** — "This was never meant to be a museum."
  Evidence: history-of-the-museum says Villanueva's building was designed in 1785 "to house the Natural History Cabinet", which was itself a museum. The track's next lines say this too, so the opener contradicts them.
  Fix: "This collection was never meant for the public."

---

## Visual descriptions checked and found consistent (not on the pages, no change needed)
- 032: the grinning drinker with a bowl.
- 038: the disciple pulling off his stockings, and the dog.
- 039: the hair over half the face.
- 039: the dove in the Coronation (the 1857 inventory says "light of the Holy Spirit").
- 055: hiding face, fists and praying among the victims.

## Count
- Tracks audited: 29 (031–059). Pages fetched: about 50.
- **WRONG: 6.** These are: 036 "giants"; 040 Menippus room; 041 strip not visible; 051 pig on a mule; 051 "already drunk"; 058 "museum is sure".
- **WEAK: 20.** Listed above, including the repeated rehang line in 048.
- **UNVERIFIED: 0.**
- **Note (no change needed): 1** (037 page self-contradiction).

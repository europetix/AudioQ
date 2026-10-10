# DE review — Prado, 10 Oct 2026 edition (81 tracks)

Reviewer: independent native-level editor. All 81 tracks read sentence by sentence against v5/tracks/NNN.perf.txt, then a scripted navigation scan of every track (room numbers incl. letters, floors in the last paragraph, @title pattern "Saal NN · …" and "· Extra ·"). `assemble.py --check … de` passes for all 81 (exit 0).

**Verdict: ready.** Navigation was already accurate: every room number, floor, stairs/lift instruction, "next door", "stay in this room", Extra announcement and the "if you're skipping the Extras" line (075) matches the English. The fixes below are the sync items, four date errors, one reversed meaning and German idiom.

## 1. Sync with the 10 Oct English

- **030** title: „Saal 43 · Extra · Tizian — Salome, und Die Kreuztragung Christi“ → „Saal 43 · Extra · Tizian — Salome“ — Christ Carrying the Cross cut
- **030** where: „Sie ansieht: Salome. Ganz in der Nähe zeigt eine kleinere, breitere Leinwand zwei Gesichter dicht beieinander zu beiden Seiten eines Kreuzes: die Kreuztragung Christi.“ → „Sie ansieht: Tizians Salome.“ — new @where
- **030** body: „[quietly] Dann suchen Sie die kleinere Leinwand mit der Kreuztragung Christi. Tizian malte das Thema zuerst für die Privatkapelle Philipps des Zweiten im Escorial. Diese spätere Fassung beschränkt sich auf zwei Gesichter, dicht beieinander, zu beiden Seiten des Kreuzes. Der Helfer ist Simon von Cyrene. [pause] Vielleicht ist er ein Bildnis des venezianischen Mosaizisten Francesco Zuccato, des Sohnes von Tizians erstem Lehrer.“ → „[quietly] Achten Sie darauf, wie wenig es noch zu sehen gibt. Kein Raum, keine Dienerin, keine Schar von Gästen. Nur eine junge Frau, eine Schale und ein ruhiger Blick. [pause] Tizian hat aus einer Geschichte fast ein Bildnis gemacht.“ — P3 rewritten
- **030** body: „[pause] Und Christus? Seine Augen sind feucht von Tränen, und sie sehen Sie direkt an. Das Museum liest das als Bitte, sich ihm anzuschließen. Das ist bei Tizian selten.“ → „[pause] Und dieses Bildnis sieht Sie an, als wären Sie gerade in diesen Augenblick hineingeraten.“ — P4 rewritten
- **060** body: „1628 kam Rubens dann zurück nach Madrid.“ → „1628 kam Rubens dann selbst nach Madrid.“ — came to Madrid himself
- **003** body: „Isabella Farnese“ → „Isabel Farnese“ — queen's name as in 034
- **034** body: „Bis 1746 gehörte das Bild Königin Isabella Farnese.“ → „1746 gehörte das Bild bereits Königin Isabel Farnese.“ — Isabel Farnese; also 'Bis 1746' meant 'until 1746' (EN: by 1746)
- **013** where: „die Jungfrau mit dem Kind, zwei Kinder und eine ältere Frau,“ → „die Jungfrau mit dem Christuskind, dem kleinen Johannes dem Täufer und einer älteren Frau,“ — new @where
- **069** body: „Nehmen Sie nun die Treppe in der Ecke dieses Saals, dieselbe, über die Sie heraufgekommen sind.“ → „Nehmen Sie nun die Treppe in der Ecke dieses Saals.“ — 'the ones you came up' removed
- **044**: body already says „ein Geschenk“ (gift), never „vermacht“. Nothing to do.

## 2. Other changes

### Facts and meaning
- **025** body: „Bis 1666 war diese Tafel sehr wahrscheinlich in“ → „1666 war diese Tafel sehr wahrscheinlich bereits in“ — 'Bis YEAR' means 'until YEAR' in German; EN says 'by YEAR'
- **031** body: „Bis 1634 war sie gekauft,“ → „1634 war sie bereits gekauft,“ — 'Bis YEAR' means 'until YEAR' in German; EN says 'by YEAR'
- **033** body: „Bis 1727 gehörte es Philipp dem Fünften,“ → „1727 gehörte es bereits Philipp dem Fünften,“ — 'Bis YEAR' means 'until YEAR' in German; EN says 'by YEAR'
- **080** body: „Sorolla fesselte die Bewegung des Meeres selbst, und er macht daraus reine Malerei.“ → „Was Sorolla fesselte, war die Bewegung des Meeres selbst. Er macht daraus reine Malerei.“ — subject/object reversed ('Sorolla captivated the sea'); EN: what caught Sorolla was the movement
- **062** body: „Dies ist der erste von drei Goyas auf unserem Weg.“ → „Dies ist die erste von drei Begegnungen mit Goya auf unserem Weg.“ — 'drei Goyas' = three Goya paintings; EN means three Goya phases/stops
- **005** body: „entlarvten es später als Kopie“ → „entlarvten sie später als Kopie“ — pronoun refers to 'Fassung' (the copy), not the Prado picture
- **005** body: „das er gleich kassiert.“ → „das der Quacksalber gleich kassiert.“ — 'er' ambiguous (patient or quack)
- **049** body: „als er zum Ritter ernannt war.“ → „nachdem er zum Ritter ernannt worden war.“ — grammar / 'once he had been made'
- **075** body: „das Bildnis sei in jenem Winter fertig.“ → „das Bildnis sei in jenem Winter fertig geworden.“ — grammar

### Navigation wording (rooms unchanged, phrasing made natural/consistent)
- **004** body: „Bleiben Sie in Saal 56 A für zwei weitere Werke von Bosch.“ → „Bleiben Sie in Saal 56 A. Hier hängen noch zwei weitere Werke von Bosch.“ — Anglicism 'bleiben ... für'
- **010** body: „Bleiben Sie in Saal 56 B für Mantegnas kleinen Tod Mariens,“ → „Bleiben Sie in Saal 56 B. Hier hängt auch Mantegnas kleiner Tod Mariens,“ — Anglicism 'bleiben ... für'
- **011** body: „Bleiben Sie in Saal 56 B für Botticellis Nastagio-Tafeln,“ → „Bleiben Sie in Saal 56 B. Hier hängen auch Botticellis Nastagio-Tafeln,“ — Anglicism 'bleiben ... für'
- **015** body: „Bleiben Sie in Saal 58 für Antonello da Messinas Toten Christus,“ → „Bleiben Sie in Saal 58. Hier hängt auch Antonello da Messinas Toter Christus,“ — Anglicism 'bleiben ... für'
- **039** body: „Bleiben Sie in Saal 8 B für die Heilige Dreifaltigkeit,“ → „Bleiben Sie in Saal 8 B. Hier hängt auch die Heilige Dreifaltigkeit,“ — Anglicism 'bleiben ... für'
- **073** body: „Bleiben Sie in Saal 64 für das Gegenstück, den dritten Mai:“ → „Bleiben Sie in Saal 64. Hier hängt auch das Gegenstück, der dritte Mai:“ — Anglicism 'bleiben ... für'
- **056** body: „Achten Sie auf die Nummer 16 am Eingang und auf“ → „Achten Sie am Eingang auf die Nummer 16 und auf“ — standard doorway formula
- **058** body: „Achten Sie auf die Angabe 16 B am Eingang und auf“ → „Achten Sie am Eingang auf die Nummer 16 B und auf“ — standard doorway formula
- **061** body: „Achten Sie auf die 32 am Eingang und auf“ → „Achten Sie am Eingang auf die Nummer 32 und auf“ — standard doorway formula
- **077** body: „Achten Sie auf die 61 B am Eingang und auf“ → „Achten Sie am Eingang auf die Nummer 61 B und auf“ — standard doorway formula

### German idiom and clarity
- **008** body: „Diese Handschuhe sind das ganze Argument des Bildes.“ → „In diesen Handschuhen steckt die ganze Aussage des Bildes.“ — Anglicism 'Argument'
- **008** body: „nach seinem eigenen Bild,“ → „nach seiner eigenen Gestalt,“ — 'nach seinem Bild' sounds biblical; Dürer's own word is Gestalt
- **010** body: „die ihr folgen.“ → „die ihr folgten.“ — tense
- **024** body: „Zählen Sie heute, finden Sie“ → „Wenn Sie heute zählen, finden Sie“ — clearer conditional for the ear
- **026** body: „Noch eine letzte Sache zum Finden.“ → „Eine letzte Sache gibt es noch zu finden.“ — unidiomatic
- **034** body: „Eine jüngste Reinigung durch die Restauratoren des Museums entfernte den Zusatz. Sie brachte auch den ursprünglichen Umriss seines Arms und eine Seilschlinge zurück.“ → „Bei einer Reinigung entfernten die Restauratoren des Museums vor Kurzem den Zusatz. Dabei kamen auch der ursprüngliche Umriss seines Arms und eine Seilschlinge wieder zum Vorschein.“ — 'eine jüngste Reinigung' is ungrammatical
- **039** body: „sechs Bildnisse von Edelmännern von El Greco besessen“ → „sechs Edelmannbildnisse von El Greco besessen“ — double 'von'
- **080** body: „bis zu tiefem, rötlichem Bronze.“ → „bis zu einem tiefen, rötlichen Bronzeton.“ — colour noun
- **007** where: „mit dem goldenen Vlies“ → „mit dem Goldenen Vlies“ — proper name of the order
- **055** where: „die auf dem Boden sitzen und Sie alle ansehen.“ → „die auf dem Boden sitzen. Alle blicken Sie an.“ — 'Sie alle' could read as 'all of you'
- **002** where: „in der Mitte geteilt von einem breiten Fluss“ → „mittig geteilt von einem breiten Fluss“ — repetition of 'in der Mitte'

## 3. For the lead

- **Isabel / Isabella Farnese**: the DE now follows the English track by track. That gives „Isabel Farnese“ in 003 and 034, but „Isabella Farnese“ in 058, 059 and 070, because the English still says Isabella there. A listener will hear both forms for the same queen. Please choose one form for the English (the usual German form is Elisabeth Farnese), and DE can then be aligned in one pass (five occurrences).
- **030 English header is stale**: @brief („quiet and moved at Christ's tears“), @listen and @sources still describe Christ Carrying the Cross. Only the header is affected. The spoken text is fine.
- **064**: the inventory title „Zigeunerinnen“ is kept as a historical document title (EN „Gypsies“). Soften it only if Yo Tours policy requires it.
- **050 / 077**: the dates „Am 24. April 1547“ and „Am 11. Dezember 1831“ are digits with a period. Please confirm on the Katja render that they are read as ordinals.
- **067**: the cartoon pun is rendered as „Keine Pappschachteln, sondern Entwürfe …“. This is a fair German equivalent, and I left it.
- **011**: „On the museum's map“ (EN wording) is kept literally as „Auf dem Plan des Museums“.
- I fetched no museodelprado.es pages. DE uses natural German titles, and no fact needed checking against the museum's pages.

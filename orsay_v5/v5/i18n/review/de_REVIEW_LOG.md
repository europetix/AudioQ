# DE review log: Musée d'Orsay V5 (Katja, de-DE)

Reviewer: independent native German editor. Every track was read sentence by sentence against v5/tracks/NNN.perf.txt. After the edits, assemble.py --check passes 75/75.

## Global decisions
- Facts, numbers, dates, hedges and loan or option conditions (007, 008, 011/012, 020, 021, 045, 046, 052, 053, 055, 056) were checked word for word. No condition was wrong. The 018 age of 28 is kept.
- Navigation: the standard phrase "Spielen Sie dort den passenden Titel ab" is used throughout. "Hören Sie dort weiter" stays only where the English says "listen there" (loan fallbacks, 018). Two stray forms were normalised (004, 046).
- "optional" replaces "freiwillig" for the optional track (011/012). "Freiwillig" means voluntary, which is the wrong sense here.
- Spaces are named consistently. "Galerie Seine 2" and "Seine-Seite" are used everywhere, so "Flussseite" and "Seine-Galerie" were removed. Carpeaux's figures are always "Tänzerinnen".
- The Detaille quote (001/075) now has identical wording in both tracks ("prachtvoll").
- Currency: "Franc" is uninflected after numerals (004/031).
- Left as is on purpose: "Ebene N" for levels with "Etage" for the generic "floor" (natural variation, never ambiguous), and the translators' title glosses.
- Main error types: calques and literal idioms (most of the changes), false friends (in Massen, Mitarbeiter, Praktiker, totes Holz, freiwillig), meaning shifts (045 "nach" vs "under" the treaty, 050 the Fénéon portrait vs the man, 019 "turn out not to have been stolen", 068 "interned" softened, 001 tense), and grammar slips (027, 038, 052).

## Changes per track (field: before → after, why)

### 001
- body: "Mit elektrischen Loks und längeren Zügen waren seine Bahnsteige zu kurz." → "Mit elektrischen Loks und längeren Zügen wurden seine Bahnsteige zu kurz." (tense: EN "made its platforms too short" (they became too short))
- body: "Und bei der Befreiung kamen hier Gefangene und Deportierte aus Deutschland nach Hause." → "Und bei der Befreiung kehrten hier Gefangene und Deportierte aus Deutschland heim." ("kamen hier nach Hause" is unidiomatic; "arrived home" = heimkehren)
- body: "Der Bahnhof wurde als historisches Denkmal geschützt." → "Der Bahnhof wurde unter Denkmalschutz gestellt." (calque; standard German term)
### 002
- body: "Alles in diesem Museum hängt an einer langen Wirbelsäule." → "Alles in diesem Museum hängt an einem langen Rückgrat." ("Wirbelsäule" is anatomical; "Rückgrat" is the idiomatic figure)
### 003
- body: "Couture nahm sein Thema von Juvenal." → "Sein Thema fand Couture bei Juvenal." (calque "took his theme from")
- body: "Schnell lasen sie das Bild als Seitenhieb" → "Die Kritiker lasen das Bild schnell als Seitenhieb" ("sie" after "Frankreich" was ambiguous)
### 004
- body: "Sehen Sie, wie er sie hineinstellt." → "Sehen Sie, wie er sie ins Bild setzt." ("hineinstellt" unidiomatic)
- body: "Spielen Sie ihren Titel ab, sobald Sie zwischen ihnen stehen." → "Spielen Sie den passenden Titel ab, sobald Sie zwischen ihnen stehen." (standard navigation phrase (rule 9, plural form))
### 005
- body: "Ein Mythos erlaubte den Künstlern Erotik, ohne die öffentliche Moral zu verletzen." → "Ein Mythos erlaubte den Künstlern, Erotik zu zeigen, ohne die öffentliche Moral zu verletzen." ("introduce eroticism": verb was missing, sentence read as truncated)
- body: "aus einer Art rosa und weißem Marzipan" → "aus einer Art rosa-weißem Marzipan" (smoother adjective form for the ear)
### 006
- body: "um seinen Schmerz und seine Angst" → "um seinen Schmerz und seine Qual" ("anguish" = Qual, not fear)
### 007
- body: "Die Gesichter erledigen die Arbeit." → "Die Gesichter sagen alles." (calque of "The faces do the work")
### 008
- body: "Drei Frauen auf einem Feld, bei der Arbeit für die Reste." → "Drei Frauen auf einem Feld, sie arbeiten für das, was übrig bleibt." ("bei der Arbeit für die Reste" sounded clumsy)
- body: "Es krönte zehn Jahre der Forschung zum Thema der Ährenleserinnen." → "Es krönte zehn Jahre Studien zum Thema der Ährenleserinnen." (an artist's "research" = Studien, not Forschung)
- body: "Doch diesmal ist die Pause für ein Gebet." → "Doch diesmal gilt die Pause einem Gebet." (calque "the pause is for a prayer")
### 010
- body: "Es kam einfach herein." → "Es spazierte einfach hinein." ("It walked straight in": direction (hinein) and image)
### 011
- body: "damit meine ich Freunde, Mitarbeiter, Kunstliebhaber" → "damit meine ich Freunde, Kollegen, Kunstliebhaber" ("fellow workers" are not employees (Mitarbeiter))
- body: "Sein Titel ist freiwillig." → "Sein Titel ist optional." ("freiwillig" (voluntary) is the wrong word for an optional track)
### 012
- title: "(freiwillig)" → "(optional)" (same: optional, not voluntary)
- where: "Freiwillige Station." → "Optionale Station." (same)
- body: "Dieser Titel ist freiwillig." → "Dieser Titel ist optional." (same)
### 014
- body: "ein japanischer Druck mit einem Ringer" → "ein japanischer Holzschnitt mit einem Ringer" (a Japanese print (Kuniaki) is a woodblock print: standard German term)
- body: "Auch Fantin-Latour malte diese Freunde, mit Manet in ihrer Mitte." → "Auch Fantin-Latour malte diese Freunde, Manet mitten unter ihnen." ("in ihrer Mitte" read as a placement claim; EN "among them")
- body: "auf der Flussseite dieser Ebene" → "auf der Seine-Seite dieser Ebene" (glossary: Seine-Seite, consistent with every other track)
### 016
- body: "Er lieh sich bei ihr, aus zwei Quellen." → "Er bediente sich bei ihr, aus zwei Quellen." ("lieh sich bei ihr" unidiomatic)
- body: "Diese Spannung ist der ganze Sinn." → "Um genau diese Spannung geht es." (calque of "That tension is the whole point")
### 018
- body: "Es stammt aus demselben Kreis, den Fantin-Latour um Manet versammelte. In seinem großen Gruppenbild in der Seine-Galerie, und auch dort ist Bazille dabei." → "Es stammt aus demselben Kreis, den Fantin-Latour in seinem großen Gruppenbild in der Galerie Seine um Manet versammelte. Auch dort ist Bazille dabei." (sentence fragment; space name aligned with "Galerie Seine 2" used in 014/015)
- body: "das Atelier dessen, der keine Gelegenheit mehr bekam" → "das Atelier dessen, dem keine Zeit mehr blieb" ("keine Gelegenheit bekam" stiff; meaning kept (he did not get the chance))
### 019
- body: "Das sind die MNR, für Musées Nationaux Récupération." → "Das sind die MNR, kurz für Musées Nationaux Récupération." (calque "MNR, for ...")
- body: "Und manche wurden gar nicht gestohlen." → "Und bei manchen stellt sich heraus, dass sie gar nicht gestohlen wurden." (EN "turn out not to have been stolen": the finding-out was lost)
### 020
- body: "In der Hitze einer Diskussion griff er zum Pinsel" → "Mitten in einer hitzigen Diskussion griff er zum Pinsel" (calque "in the heat of a discussion")
- body: "wie brillant der Pinselstrich ist, wie bei Fragonard." → "wie brillant der Pinselstrich ist. Er erinnert an Fragonard." ("recalling Fragonard": "wie bei" overstated the likeness)
### 021
- where: "Der Saal ist nicht bestätigt," → "Sein Standort ist nicht bestätigt," ("Its room is not confirmed": the painting's room, not the room itself)
- body: "Lesen Sie nun die Familie," → "Betrachten Sie nun diese Familie genau," (calque "read the family")
- body: "Die große Fläche, die gedämpften Farben," → "Das große Format, die nüchternen Farben," ("great size" = Format; "sober colours" = nüchtern)
### 022
- body: "etwa achtzehn Tonnen davon" → "rund achtzehn Tonnen schwer" (calque "about eighteen tonnes of it")
- body: "Suchen Sie dort, im Opéra-Bereich, das große Modell" → "Suchen Sie im Opéra-Bereich das große Modell" (repeated "dort" in two consecutive sentences)
### 023
- body: "sechseinhalb Meter auf jeder Seite" → "mit sechseinhalb Metern Seitenlänge" (calque "on each side")
### 024
- body: "Lesen Sie es in vier Teilen." → "Betrachten Sie es in vier Teilen." (calque "read it in four parts")
### 025
- body: "die sich neu erbaut" → "die sich neu baut" ("sich neu erbaut" unidiomatic)
### 026
- body: "Vorbei an Carpeaux' Tänzern," → "Vorbei an Carpeaux' Tänzerinnen," (consistency with 022/025 (the dancers are women))
### 027
- body: "Fast genau das jagten die Maler in den Sälen vor Ihnen. Nicht der Stadt als Monument. Der Stadt zu einer ganz bestimmten Stunde." → "Fast genau dem jagten die Maler in den Sälen vor Ihnen nach. Nicht der Stadt als Monument. Der Stadt zu einer ganz bestimmten Stunde." (grammar: "jagten das" + dative fragments did not agree)
### 030
- where: "einem Mann, der totes Holz einen Weg entlangträgt" → "einem Mann, der dürres Holz einen Weg entlangträgt" ("totes Holz" is a calque of "dead wood"; gathered firewood = dürres Holz)
- body: "Dort trägt ein Mann eine Last aus totem Holz." → "Dort trägt ein Mann eine Last dürres Holz." (same)
### 031
- body: "sechshundertfünfundachtzig Francs" → "sechshundertfünfundachtzig Franc" (consistency with 004: currency unit uninflected after numerals)
### 033
- body: "Ein echter Mann unterrichtet also eine Klasse" → "Ein Mann, den es wirklich gab, unterrichtet also eine Klasse" ("echter Mann" reads as "a real man (manly)")
### 035
- body: "an einem Kaffeehaustisch" → "an einem Cafétisch" ("Kaffeehaus" is Austrian; German-German usage)
### 037
- body: "Renoir war fünfunddreißig im Frühjahr 1876." → "Im Frühjahr 1876 war Renoir fünfunddreißig." (word order unnatural in German)
- body: "mit dem großen Maler Solares" → "mit dem hochgewachsenen Maler Solares" ("großen Maler" reads as "great painter"; EN "tall")
- body: "In diesem Jahr wird diese Seite hundertfünfzig." → "In diesem Jahr wird diese Seite hundertfünfzig Jahre alt." (incomplete in German)
### 038
- body: "Das Einzige, das stillsteht, ist fest." → "Das Einzige, was stillsteht, ist fest." (grammar: "das Einzige, was")
### 040
- body: "Jahrelang hatte er das Licht über eine Steinfassade gejagt." → "Jahrelang war er dem Licht auf einer Steinfassade nachgejagt." ("das Licht über eine Fassade jagen" means chasing it away; EN "chasing light across")
- body: "doch der Teich scheint es nicht zu tun." → "doch der Teich scheint dort nicht aufzuhören." (calque "the pond doesn't seem to")
### 041
- body: "Ganz in der Nähe der Herkunft ihrer Modelle." → "Ganz in der Nähe des Ortes, aus dem ihre Modelle stammten." (stiff nominal phrase)
### 042
- body: "Ein langer Blick von Ihnen scheint nur fair." → "Da ist ein langer Blick von Ihnen nur fair." (anglicism "seems only fair")
### 043
- body: "Denken Sie also beim Gang an diesen Wänden entlang daran: Die letzte Etappe der Reise ist die kürzeste an Zeit." → "Denken Sie also daran, während Sie an diesen Wänden entlanggehen: Die letzte Etappe der Reise ist zeitlich die kürzeste." (clumsy construction; "kürzeste an Zeit" unidiomatic)
### 044
- body: "Und lassen Sie sich zurück prüfen." → "Und lassen Sie sich nun Ihrerseits von ihm prüfen." ("sich zurück prüfen" is not German)
### 045
- body: "In die französische Nationalsammlung kam es 1959, nach dem Friedensvertrag mit Japan," → "In die französische Nationalsammlung kam es 1959, aufgrund des Friedensvertrags mit Japan," (meaning: EN "under the peace treaty" (by virtue of), not "after" it)
### 046
- body: "Hören Sie dort den passenden Titel." → "Spielen Sie dort den passenden Titel ab." (standard navigation phrase (rule 9))
### 047
- body: "Lesen Sie sie also so wie er." → "Sehen Sie sie also so, wie er sie sah." (calque "read them as he did")
### 049
- body: "Mit aufsteigenden Linien, und Orange gibt den Ton an." → "Mit aufsteigenden Linien, und mit Orange als beherrschender Farbe." ("Orange gibt den Ton an" ambiguous; EN "orange in command")
### 050
- body: "Ihr Name war Berthe Roblès," → "Sie hieß Berthe Roblès," (smoother; also frees a word for the fix below)
- body: "Dazu gehört auch der Schriftsteller Félix Fénéon, heute in New York, im Museum of Modern Art." → "Dazu gehört auch das Bildnis des Schriftstellers Félix Fénéon, heute in New York, im Museum of Modern Art." (meaning: it is the portrait, not the writer, that is now in New York)
### 051
- body: "Gauguin drängte sie, in Massen und festen Farbflächen zu malen." → "Gauguin drängte sie, in großen Formen und festen Farbflächen zu malen." (false friend: "in Massen" means "in huge quantities")
- body: "Eine junge Frau, liegend an einem Ort namens Wald der Liebe." → "Eine junge Frau, die an einem Ort namens Wald der Liebe liegt." (participle construction stiff for the ear)
### 052
- body: "Gauguin fand wenig Reiz an den Frauen von Arles." → "Gauguin fand die Frauen von Arles wenig reizvoll." (preposition error ("Reiz an"))
### 053
- body: "vergrößerte es auf die Größe eines großen Buddhas" → "vergrößerte es auf das Format eines großen Buddhas" (repetition "Größe eines großen")
### 054
- body: "Kleine Töne von Orange und Rosa antworten ihnen," → "Kleine Akzente in Orange und Rosa antworten ihnen," ("Töne von" calque of "notes of")
### 055
- body: "Doch bei seinem letzten Aufenthalt in Paris endete seine Arbeit mit Ton mit diesem Stück." → "Doch bei seinem letzten Aufenthalt in Paris fand seine Arbeit mit Ton ihren Abschluss in diesem Stück." (double "mit", clumsy for the ear)
### 056
- body: "Sie bezaubert eine Schlange, genauso furchterregend, wie die Schlange der Genesis verführerisch war." → "Sie bezaubert eine Schlange, die genauso furchterregend ist, wie die Schlange der Genesis verführerisch war." (relative clause missing, hard to follow by ear)
### 059
- body: "Rivière fotografierte seine eigenen Kulissen." → "Rivière fotografierte, was hinter seiner eigenen Bühne geschah." ("Kulissen" = scenery; EN "his own backstage")
- body: "und fotografierte ihn von oben." → "und fotografierte ihn von der Spitze aus." ("von oben" ambiguous; EN "from the top")
### 060
- body: "In diesem Saal kommt der Weg an." → "In diesem Saal ist der Weg am Ziel." (calque "where the road arrives")
### 062
- body: "Die Ausstattung borgt bei allen Stilen" → "Die Ausstattung bedient sich bei allen Stilen" ("borgt bei" unidiomatic)
### 063
- body: "Und es brachte mehr als einen Verkauf." → "Und das Bild brachte ihm mehr als einen Verkauf." (vague pronoun; clarifies for the ear)
### 064
- where: "und eine junge Frau, die kniet und ihm nachgreift" → "und eine junge Frau, die kniend nach ihm greift" (smoother)
- body: "über die Ecke des Saals gehängt." → "über Eck gehängt." (idiom: "über Eck")
### 065
- where: "über eine Ecke gehängt" → "über Eck gehängt" (idiom: "über Eck")
- body: "über die Ecke des Saals gehängt, wie ursprünglich." → "über Eck gehängt, wie ursprünglich." (idiom: "über Eck")
### 066
- body: "Er lässt den Raum einfach da." → "Er lässt den leeren Raum einfach stehen." ("lässt den Raum da" unidiomatic)
### 067
- body: "Suchen Sie nun Saal 68, Toulouse-Lautrec und den Bühnen seines Paris gewidmet." → "Gehen Sie nun in Saal 68, zu Toulouse-Lautrec und den Bühnen seines Paris." (participle fragment; repeated "Suchen Sie")
### 068
- body: "Mit vierzehn kam sie in die Pariser Salpêtrière, ein Krankenhaus." → "Mit vierzehn wurde sie in das Pariser Krankenhaus Salpêtrière eingewiesen." (EN "was interned": the confinement was softened to "kam")
### 069
- body: "Sehen Sie nun über das Tischchen." → "Schauen Sie nun oberhalb des Tischchens." ("über das Tischchen" means across/over it; EN "above the little table")
### 070
- body: "Sein Porträt von Manet haben Sie unten vielleicht gesehen." → "Manets Porträt von ihm haben Sie unten vielleicht gesehen." (ambiguity: could be heard as a portrait of Manet by Zola)
### 071
- where: "Majorelles Bett Seerosen mit vergoldeter Bronze" → "Majorelles Seerosenbett mit vergoldeter Bronze" (unnatural apposition)
### 072
- body: "Betrachten Sie genau die beiden Oberflächen." → "Betrachten Sie die beiden Oberflächen aus der Nähe." (doubled "genau" in consecutive sentences)
- body: "Das Museum liest sie als Abschied, voller Zuversicht auf das strahlende Dasein" → "Das Museum deutet sie als Abschied, voll Vertrauen auf das strahlende Dasein" (calque "reads it as"; "Zuversicht auf" wrong preposition)
### 073
- body: "einer der gefragtesten Praktiker in Paris." → "einer der gefragtesten Marmorbildhauer in Paris." ("Praktiker" is not the German trade term for a carving assistant)
- body: "Sein eigener Praktiker, Jean-Joachim Supéry," → "Sein eigener Gehilfe, Jean-Joachim Supéry," (same)
### 075
- body: "„Der Bahnhof ist großartig und sieht aus" → "„Der Bahnhof ist prachtvoll und sieht aus" (same quote as 001: identical wording across the guide)
- body: "Und sehen Sie entlang der Terrassen selbst." → "Und schauen Sie die Terrassen selbst entlang." (ungrammatical)

Tracks changed: 60 of 75. Edits: 91.
Unchanged tracks (no error found): 009, 013, 015, 017, 028, 029, 032, 034, 036, 039, 048, 057, 058, 061, 074.

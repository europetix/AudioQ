# DE review — Barcelona Cathedral 001–036 (Yo Tours, 14 Nov 2026), independent editor

Scope: all 36 tracks checked sentence by sentence against `v5/tracks/NNN.perf.txt` (current English, including the changed 031). All 15 bridges were checked against `v5/bridges/*.txt`. `assemble.py --check … de` passes for all 36 (exit 0) after the edits.

Verdict: **ready**. The translation was already accurate and natural. The edits below are one factual sync (031), one addition removed (031), and small grammar, TTS and wording fixes. No navigation error was found.

## Navigation scan (B)
- For all 36 tracks the last paragraph matches the English: the same places, the same order and the same things to look for. Every left/right keeps "mit Blick zum Hochaltar". "Don't go out", "If Mass is on, don't go in", "If the choir/crypt is closed…" and "If you went down…" are all kept.
- Every spoken `<place> · <title>` cue matches the destination's German @title exactly. This was checked by script, including the three Extras and both cues in 007, 016 and 032.
- Bridges: there are 15 lines, one for each English bridge, with the same keys in the same order. Every line starts with "In dieser Kurzfassung", and none is longer than the English in words (whitespace count, [O…] bracket excluded). The routes are identical. No change was needed. The file `de/bridges.txt` is still identical to `bridges_001-036.txt`.
- Kapitelsaal / Kapitelhaus: "Kapitelsaal" appears only for the Chapter Hall museum (001, 003, 007, 010, 028, 031–035 and bridges 030 E/H). "Kapitelhaus" appears only where the English says "chapter house": 007 (the 1407 room, now the Lepanto chapel) and 028 (the canons' chapter house round the cloister). The two are never mixed. "Kapitel" alone stays for the meeting body, as in 016, 018, 029 and 033.
- The tour names are as the lead set them in 001: die vollständige Tour, die Kernversion, die Highlights. 007, 016 and 032 use "Wenn Sie die vollständige Tour machen".

## Changes (track: before → after, why)
| Track | Before | After | Why |
|---|---|---|---|
| 031 | „Seine Pietà, der tote Christus mit seiner Mutter, wird Michael Lochner zugeschrieben, …“ | „Sein Pietà-Relief, der tote Christus mit seiner Mutter, kam fast ein Jahrhundert später. Es wird Michael Lochner zugeschrieben, …“ (and „der sie bezahlte“ → „der es bezahlte“) | The English changed after translation ("came almost a century later"). The door is from the late 1300s and the relief came about a century later. |
| 031 | „Und der Maler selbst wurde irgendwo unter diesem Kreuzgang begraben.“ | „Der Maler selbst wurde unter diesem Kreuzgang begraben.“ | "irgendwo" (somewhere) is not in the English. It was an addition. |
| 030 cue, 031 @where | „mit einer gemeißelten Pietà darüber“ | „mit einem Pietà-Relief darüber“ | "gemeißelt" means carved in stone, but Lochner's relief is wood, and the piece over the door may be a copy. "Relief" keeps "carved" without naming a material. |
| 003 | „am 30. Januar 1938“ | „am dreißigsten Januar 1938“ | For TTS safety: the day is written as a word, as the other tracks do ("am zwölften Februar"). |
| 009 | „vom 15. Oktober 1519“ | „vom fünfzehnten Oktober 1519“ | Same reason. |
| 003, 005 | „Architektenkollegium“ | „Architektenkammer“ | "Architektenkollegium" is a calque. "Architektenkammer" is the German equivalent of the Col·legi d'Arquitectes. |
| 002 | „kann es niemand zeigen“ | „kann sie niemand zeigen“ | "sie" refers back to the first church. |
| 007 | „Es ist nicht das Museum im Kapitelsaal …“ | „Das ist nicht das Museum im Kapitelsaal …“ | "Raum" is masculine, so "Es" did not refer back to it. "Das" works as the "This is not…" the English means. |
| 011 | „waren die Köpfe abgenommen“ | „waren die Köpfe abgenommen worden“ | The English "had been taken down" is a process, so the pluperfect passive is needed. |
| 011 | „das, was sie zeigten: einen abgeschlagenen Kopf“ | „… : ein abgeschlagener Kopf“ | Case: the apposition is to the subject "das". |
| 013 | „was er zerstörte“ | „was er beschädigte“ | The English says "what it broke", not "destroyed". |
| 013 cue | „Sind Sie schon auf dem Dach, oder sobald Sie oben sind, folgen Sie …“ | „Wenn Sie schon auf dem Dach sind, oder sobald Sie oben ankommen, folgen Sie …“ | Fixes a broken construction in a navigation sentence. The meaning and route are unchanged. |
| 014 | „und viele von ihnen trugen ihren Namen“ | „… hätten ihren Namen getragen“ | Keeps the attribution: both halves are what "the cathedral says". |
| 015 | „Im Umkreis weniger Straßen zählt …“ | „Im Umkreis weniger Straßen um dieses Dach zählt …“ | Restores "of this roof", which had been dropped. |
| 019 | „Karl hörte die Orgel davor.“ | „Karl hörte ihre Vorgängerin.“ | Natural German for "the organ that came before it". |
| 021 | „Ihr Kult ist bis Ende des sechsten Jahrhunderts belegt“ | „… ist schon Ende des sechsten Jahrhunderts belegt“ | "bis" means "up until", which said the opposite of the English "by the end of". |
| 022 | „Viele Bücher nennen dieses Grab Alabaster.“ | „Viele Bücher sagen, dieses Grab sei aus Alabaster.“ | Natural German. NEVER-list point: the tomb is marble, and the next sentence says so. |
| 022 | „Hinter dem Grab, wenn Sie ihn erkennen können, steht ein viel älterer Stein“ | „…, wenn Sie es erkennen können, befindet sich ein viel älterer Stein“ | "ihn" pointed forward to a noun not yet spoken. "befindet sich" suits a plaque. |
| 025 | „nennt es seine Decke“ | „nennt ihn seine Decke“ | "Mantel" is masculine. |
| 025 | „Er war ein Dominikanerbruder.“ | „Er war Dominikaner.“ | Natural German for "a Dominican friar". |
| 027 | „Der Dekan der Kathedrale hat sie erklärt.“ | „… hat diese Entscheidung erklärt.“ | "sie" was ambiguous between the cathedral and the government. The English says "the choice". |
| 030 | „Ihre Seiten geben eine Gans „für jede …““ | „Laut ihren Seiten steht eine Gans „für jede …““ | "geben" does not work in German here. The quote and the attribution are unchanged. |
| 030 | „Sie bekommen tägliche Reinigung, einen Teich mit ständig erneuertem Wasser, eine vom Tierarzt verordnete Ernährung und regelmäßige Untersuchungen.“ | „Täglich wird gereinigt, das Wasser im Teich wird ständig erneuert, ein Tierarzt verordnet ihr Futter, und sie werden regelmäßig untersucht.“ | Natural spoken German, with the same four facts. |
| 032 cue | „Suchen Sie drinnen das Gemälde …“ | „Gehen Sie hinein, und suchen Sie das Gemälde …“ | Restores "Go in" from the English cue. The cue in 033 and bridges 030 E/H ("Inside, find…") keep „Suchen Sie drinnen“, as their English does. |
| 033 | „nach Predigten gegen die Juden, die in Sevilla begonnen hatten“ | „nach judenfeindlichen Predigten, die in Sevilla begonnen hatten“ | The relative clause could be heard as "the Jews had begun in Seville". Now it can only refer to the preaching. |

No other edits were made. Titles, @where (except 031), quotes and all other cues are unchanged.

## Quotations (rule 11)
For DE every quote is a faithful translation of the English, with the attribution and the "auf Spanisch / auf Katalanisch / auf Altkatalanisch" framing kept. The only original-language wording is what the English itself keeps: quondam, Noli me tangere, „molt mediocre“, „Opus Bartolomei Vermejo Cordubensis“. So nothing needed fetching, and nothing was fetched. In 007 the Hanß quote says „Don Juan“ for the English "Don John". It is a translated quote, so this is acceptable. I note it here only for transparency.

## For the lead
1. The 031 English change is now in the German.
2. Spelling of the historian: the English has "Hanss" and the German has "Hanß". This was the translator's choice and is fine for Katja. Keep it, unless the lead wants the English spelling everywhere.
3. Optional style point, not changed: in 036 the translator wrote „Gehen Sie behutsam.“ for "Go gently.". It is literal and slightly unusual German, but acceptable. A warmer option, „Machen Sie es gut.“, would drop "gently".
4. The translator's ONSITE list in `de_001-036.md` (008, 010, 013, 014, 015, 036) is still valid. It names the German sentences to cut if an O-item fails. None of those sentences was edited, so they still match.

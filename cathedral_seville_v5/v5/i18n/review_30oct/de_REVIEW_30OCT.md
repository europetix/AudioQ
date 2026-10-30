# DE review — Catedral de Sevilla 001–028 + bridges (30 Oct 2026)

Independent review of de/*.json and de/bridges.txt against v5/tracks/*.perf.txt and v5/bridges/*.txt.
Result after edits: `assemble.py --check … de` → all 28 OK (exit 0). Assemble was not run without --check.

## A. Changes (track: before → after, why)
- 001: „Das Wesentliche“ … die „Highlights“ → die Kernversion … die Highlights. Lead's version names (same as Uffizi and Alcázar DE). „die vollständige Tour“ was already used, in paragraphs 2 and 4. „Bei den Highlights“ in paragraph 6 is unchanged. These names occur only in 001. The bridges use the glossary term „In dieser Kurzfassung“.
- 001: „Ein angekündigtes Extra“ → „Ein angekündigter Extra-Titel“. Matches the glossary term used in 004/008/016/018/020.
- 007: „je zwei Seitenschiffen auf jeder Seite“ → „zwei Seitenschiffen auf jeder Seite“. Removes the doubled "je … auf jeder".
- 011: „Ein New Yorker Blatt … schloss seinen Bericht“ → „Eine New Yorker Wochenzeitschrift … schloss ihren Bericht“. Aligns with the revised English ("One New York weekly").
- 013: „Dieses Bild ist älter als die Kathedrale um es herum. … war sie schon da“ → „Diese Madonna ist älter als die Kathedrale um sie herum.“ Fixes the gender mismatch (Bild … sie).
- 013: last paragraph „Weiter an dieser Seite …“ → „Gehen Sie weiter an dieser Seite …“. A clearer spoken instruction. The route is unchanged.
- 014: „Trophäen der Reise und der Reconquista“ → „Trophäen der Reise nach Amerika und der Reconquista“. Aligns with the revised English. This closes translator note 014.
- 016: „Hier gibt es einen kurzen Extra-Titel in der Sala del Pabellón“ → „Es gibt …“. The Extra is in another room, and "Hier" could mislead the listener. The English has no "here".
- 019: „… aus der Kathedrale selbst. Es gehörte dem Souffleur des Chors, einem Mann namens Alonso de Herrera.“ → „… aus der Kathedrale selbst: Alonso de Herrera, der in ihrem Chor arbeitete.“ Aligns with the revised English. The "prompter" is gone, which closes translator note 019.
- 020: „Hier gibt es zuerst einen kurzen Extra-Titel über den Kapitelsaal“ → „Zuerst gibt es …“. Same reason as 016: the Extra plays in the Sala Capitular, not here.
- 023: „Hernán Ruiz der Jüngere schloss sie“ → „schloss die Kuppel“. "sie" could mean the chapel.
- 028: „mit der Kathedrale“ → „gemeinsam mit der Kathedrale“ ("working with the Cathedral").
- 028: „Eine treffende Wahl“ → „Eine vielsagende Wahl“. This keeps the wry sense of "a pointed choice".

## Checked, no change needed
- Navigation: I compared the last paragraph of all 28 tracks with the English. Rooms, order, landmarks and conditions match. "keep to the right" on the ramps is „rechts“ everywhere (002–006). The English has no other left/right. The Capilla Real is seen through the grille only (001, 023). The exit by the Puerta del Perdón has no re-entry (001, 028). Every Extra is followed by the next main stop (004, 008, 016, 018, 020).
- Conditionals: Lagarto/Príncipe entrances, "Not climbing?", "if a Mass is on", "if you stopped at the choir", "if your route took you there" and "if you can see it" are all present.
- @title: every one starts with the same Spanish space name as the English, with the Extra pattern kept. Spanish place names are unchanged throughout.
- Bridges: 7 lines and 7 English lines, with the same keys (006 H>008, 008 H>014, 011 E>013, 014 H>025, 022 E>025, 025 E>028, 025 H>028). Each line follows the same route and starts with „In dieser Kurzfassung“.
- TTS: no symbols, abbreviations or Roman numerals in speech. Regnal names are in words. Years are in digits.
- Quotations (002, 006, 011): faithful German renderings of the English, introduced the same way. Formal Sie is used throughout.

## For the lead
- Translator notes for 011/014/019 are now superseded by the revised English.
- 001 version names: if the app/store labels use other German names, the spoken text should be changed to match.

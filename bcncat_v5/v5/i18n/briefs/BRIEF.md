# Translation brief — Barcelona Cathedral, Yo Tours, edition of 14 Nov 2026 (36 tracks). ONE language: ES, FR or DE.

The English is final after two independent audits per edition and a fixer. Translate it faithfully for LISTENING (a synthetic voice reads it: ES Dalia es-MX, FR Vivienne, DE Katja). Navigation accuracy first: customers complained earlier guides sent them to wrong places.

## Files
- Source (read-only): /home/claude/audioq/bcncat_v5/v5/tracks/NNN.perf.txt (001–036). Translate only @title, @where (without any [O…]/ALT bracket at its end: drop those notes) and the spoken body after `---`.
- Bridges (read-only): /home/claude/audioq/bcncat_v5/v5/bridges/*.txt (one line per bridge, keys like `004 H>006:`).
- Context: bcncat_v5/v5/PLAN.md (conventions, NEVER list), bcncat_v5/research/FACTS_*.md (§ names, quotes with original language).
- Output: /tmp/claude-0/-home-claude/98e7af58-dd32-56e0-a687-5f082c01b624/scratchpad/bcn_i18n/<lang>/NNN.json = {"title": "...", "where": "...", "body": "..."} for all 36, and <lang>/bridges_001-036.txt (one line per English bridge, same key). Notes: bcn_i18n/notes/<lang>_001-036.md.
- Self-check (must pass for all 36): python3 /home/claude/audioq/bcncat_v5/v5/i18n/assemble.py --check /tmp/claude-0/-home-claude/98e7af58-dd32-56e0-a687-5f082c01b624/scratchpad/bcn_i18n <lang>
  It requires: the same delivery tags in the same order, no fewer [pause]/[long pause], the same number of paragraphs, NOT longer than the English (aim ~5% shorter), every year of the English as digits, no ; or ( in speech, no unknown tags.

## Rules
1. Meaning exactly as the English: every hedge ("the cathedral says", "the story goes", "according to tradition", "some scholars", "one researcher", "as reported"), every attribution, every "if you're on the full tour…", every number and date. Add nothing (no extra dates, names, views, facts). Drop nothing.
2. Formal address (ES usted, FR vous, DE Sie). Natural spoken style; short sentences; no symbols the voice may misread (+ & % · ×) except the " · " separator in the spoken cue form `<place> · <title>` at the end of each last paragraph and of each bridge, which stays.
3. Place names: the cathedral's own names. Catalan names stay as in the English (Pla de la Seu, la Seu, Casa de l'Ardiaca, Sant Iu, Santa Llúcia, Carrer del Bisbe, cimbori, trascor, cadirat, Toisó d'Or, l'ou com balla, Font de Sant Jordi). Where the English uses an English name (the Christ of Lepanto chapel / chapel of the Blessed Sacrament, the choir, the crypt, the cloister, the Chapter Hall, the lantern tower, the ambulatory, the Santa Eulàlia door, the Pietat door), use the cathedral's own name in your language if its site gives one (catedralbcn.org has ES, CA, EN pages; check once with WebFetch, one page at a time) and keep it identical in every title, cue and bridge. Keep a short glossary in your notes.
4. "Not the Sagrada Família" (001): keep it warm and natural in your language; the Sagrada Família keeps its name.
5. "As you face the high altar", left/right, "from the doorway", "if Mass is on, don't go in", "if the choir/crypt is closed": translate exactly; never add or drop a direction or a condition.
6. Spoken cue form: `<place> · <title>` exactly as your translated @title of the destination track (place part = the part before " — " or " · Extra · "). Extras: keep "Extra".
7. Bridges: one per English bridge, same key, starting ES "En esta versión corta," FR "Dans cette version courte," DE "In dieser Kurzfassung"; not longer than the English line.
8. Numbers: years as digits; other numbers as people say them (words for small numbers is fine). Regnal numbers in words: e.g. ES "Felipe Quinto", "Carlos Quinto", FR "Charles Quint", "Philippe cinq", DE "Karl der Fünfte" (inflected as needed).
9. Tense: past for the dead (Eulàlia, Bermejo, Ordóñez, Sanglada, Lochner, Desplà, the kings, Gaudí…), as the English.
10. NEVER: alabaster for Santa Eulàlia's tomb (it is marble; the alabaster is Sant Oleguer's figure), the cathedral "finished in 1448" (that is the cloister), Gaudí worked on the cathedral, the Lepanto Christ "dodged a cannonball" or "16th-century" as fact, 13 geese "because she was 13" as fact, "the anarchists spared/burned", UNESCO, any king named for the shields except as the English does. Keep every "tradition says", "the story goes" and "according to tradition".
11. Quotations. The English translates quotes originally in Spanish, Catalan, Latin or English. In ES you may give the ORIGINAL Spanish wording of a Spanish-original quote only after verifying it on the cited page (WebFetch, one page at a time, never in bursts, never curl/browser, never a CAPTCHA); otherwise translate the English faithfully and keep the attribution and the "in Spanish/in Catalan" framing adapted (ES: "en catalán" for Catalan quotes; for Spanish originals in ES you may drop "en español"). FR/DE: translate faithfully from the English, keep "auf Spanisch/en espagnol" framing. Never invent or tidy a quote. If verification fails, report it in your notes; reported speech is acceptable.
12. Tags: keep every delivery tag in place ([warmly] etc.). No asterisks.

## Notes file
List: your glossary; every quote and how handled (verified original / translated); anything ambiguous in the English; anything you think is wrong in the English (do not fix it, report it).
Final reply ≤150 words.

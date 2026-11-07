# Translation brief — Park Güell (Barcelona), Yo Tours, edition of 7 Nov 2026 (45 tracks). ONE language: ES, FR or DE.

The English is final after two independent audits per edition and a fixer. Translate it faithfully for LISTENING (a synthetic voice reads it: ES Dalia es-MX, FR Vivienne, DE Katja). Navigation accuracy first: customers complained earlier guides sent them to wrong places.

## Files
- Source (read-only): /home/claude/audioq/guell_v5/v5/tracks/NNN.perf.txt (001–045). Translate only @title, @where (without any [O…]/ALT bracket at its end: drop those notes) and the spoken body after `---`.
- Bridges (read-only): /home/claude/audioq/guell_v5/v5/bridges/*.txt (21 lines, keys like `004 H>015:`).
- Context: guell_v5/v5/PLAN_V2.md (conventions, NEVER list), guell_v5/research/FACTS_*.md (§ names, quotes with original language), research/map/OFFICIAL_ROUTE_MAP_NOTES_7NOV2026.md.
- Output: /tmp/claude-0/-home-claude/98e7af58-dd32-56e0-a687-5f082c01b624/scratchpad/gue_i18n/<lang>/NNN.json = {"title": "...", "where": "...", "body": "..."} for all 45, and <lang>/bridges_001-045.txt (one line per English bridge, same key). Notes: gue_i18n/notes/<lang>_001-045.md.
- Self-check (must pass for all 45): python3 /home/claude/audioq/guell_v5/v5/i18n/assemble.py --check /tmp/claude-0/-home-claude/98e7af58-dd32-56e0-a687-5f082c01b624/scratchpad/gue_i18n <lang>
  It requires: the same delivery tags in the same order, no fewer [pause]/[long pause], the same number of paragraphs, NOT longer than the English (aim ~5% shorter), every year of the English as digits, no ; or ( in speech, no unknown tags.

## Rules
1. Meaning exactly as the English: every hedge ("the park says", "the story goes", "some scholars", "one researcher", "as reported"), every attribution, every "if you're on the full tour…", every number and date. Add nothing (no extra dates, names, views, facts). Drop nothing.
2. Formal address (ES usted, FR vous, DE Sie). Natural spoken style; short sentences; no symbols the voice may misread (+ & % · ×) except the " · " separator in the spoken cue form `<place> · <title>` at the end of each last paragraph and of each bridge, which stays.
3. Place names: the park's official names. Catalan names stay as in the English (Carrer d'Olot, Casa del Guarda, Sala Hipòstila, Plaça de la Natura, Jardins d'Àustria, Pòrtic de la Bugadera, Pont de Baix/del Mig/de Dalt, Casa Larrard, Font Sarva, Turó de les Tres Creus, Marianao, Carretera del Carmel, Sant Josep de la Muntanya). Where the English gives an English name (Hypostyle Room, Nature Square, Austria Gardens, Dragon Stairway, Portico of the Washerwoman, Low Viaduct, the entrance esplanade, the way out), use the operator's own name in your language if its official site uses one (parkguell.barcelona has ES and FR pages: check them once with WebFetch, one page at a time; DE: the park has no German site — use natural German: Hypostylsaal, Platz der Natur, Österreichische Gärten, Drachentreppe, Portikus der Wäscherin, Unterer Viadukt…) and keep it identical in every title, cue and bridge. Keep a short glossary in your notes.
4. "Park, with a k": keep the joke — the word "Park" is English on the wall; explain it naturally in your language (e.g. ES "Park, con k, en inglés"; FR "Park, avec un k, à l'anglaise"; DE: the joke is that it's the English spelling, not Catalan "Parc" — say so, since "Park" is also German).
5. Left/right, "the one without the tower", "on your right as you face the stairway", "before the check": translate exactly; never add or drop a direction.
6. Spoken cue form: `<place> · <title>` exactly as your translated @title of the destination track (place part = the part before " — " or " · Extra · "). Extras: keep "Extra".
7. Bridges: one per English bridge, same key, starting ES "En esta versión corta," FR "Dans cette version courte," DE "In dieser Kurzfassung"; not longer than the English line.
8. Numbers: years as digits; other numbers as people say them (words for small numbers is fine). Regnal numbers in words: ES "Alfonso trece", FR "Alphonse treize", DE "Alfons der Dreizehnte" (inflected as needed).
9. Tense: past for the dead (Güell, Gaudí, Jujol, Berenguer, Bassegoda…), as the English.
10. NEVER: "longest bench", free zone/free park, a cistern capacity, Gaudí designed his own house, Gaudí invented trencadís, words in Gaudí's mouth (no quote of Gaudí exists in the English: keep it that way).
11. Quotations. The English translates quotes that were originally Spanish, Catalan or English. In ES you may give the ORIGINAL Spanish wording of a Spanish-original quote only after verifying it on the cited page (WebFetch, one page at a time, never in bursts, never curl/browser, never a CAPTCHA); otherwise translate the English faithfully and keep the attribution and the "in Spanish/in Catalan" framing adapted (ES: "en catalán" for Catalan quotes; for Spanish originals in ES you may drop "en español"). FR/DE: translate faithfully from the English, keep "auf Spanisch/en espagnol" framing. Never invent or tidy a quote. If verification fails, report it in your notes; reported speech is acceptable.
12. Tags: keep every delivery tag in place ([warmly] etc.) and *Park* asterisks as in the English.

## Notes file
List: your glossary; every quote and how handled (verified original / translated); anything ambiguous in the English; anything you think is wrong in the English (do not fix it, report it).
Final reply ≤150 words.

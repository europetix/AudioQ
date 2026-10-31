# FR review — Poble Espanyol 001–025 (31 Oct 2026)

Independent review against v5/tracks/NNN.perf.txt and v5/bridges/*.txt, per REVIEW_BRIEF.md and the lead's notes.
Result: `assemble.py --check … fr` gives OK on all 25 tracks (exit 0). Backup of the pre-review files: scratchpad/frrev/backup/.

## Verdict: READY

All 24 end-of-track cues match the next track's FR title exactly (script check). All 8 bridge keys are present, each with one line that starts with « Dans cette version courte, ». Routes match the English and no bridge is longer than the English.
Last paragraphs were checked against the English for all 25 tracks: same places in the same order, the same up/down, steps, house numbers and landmarks.

## Changes (track: before → after, why)

**Facts / hedges / navigation**
- 009 P3: « Alcañiz près de Teruel » → « Alcañiz en province de Teruel ». EN "Alcañiz in Teruel" means the province; Alcañiz is far from Teruel city, so « près de » was a factual error. (Translator note listed this as a "plain reading". It wasn't one.)
- 003 P4: « c'est là qu'était cette terrasse » → « Le magazine y situait la terrasse ». EN "That's where the magazine found the terrace". The old FR said the terrace no longer exists, a status the English deliberately does not state.
- 008 P3: « comme cette tour » → « comme celle d'Utebo ». EN "like Utebo's tower" means the original, not the replica in front of the listener.
- 001 P6: « celle des temps forts, trois quarts d'heure » → « …, environ trois quarts d'heure ». This restores the EN hedge "about".
- 001 P3: « ce qui a changé » → « ce que les bâtisseurs ont changé ». This restores EN "what the builders changed".
- 020 P2: « Puis elle est revenue. » → « Elle est revenue après. » (after the war). EN "After the war, it came back."
- 020 P3: « ignore le Poble » → « ne mentionne pas le Poble ». EN "does not mention". « ignore » suggests deliberate omission, and 020 must stay even-handed.
- 015 P4: « Deux lectures s'opposent, toutes deux sérieuses. » → « Deux lectures, toutes deux sérieusement défendues. » EN "both are argued seriously". This keeps the passage level.
- 021 P7: « Rincón del Triste est tout près » → « est juste à côté ». EN "is beside you".
- 005 P7: « partant près de la maison quarante et un » → « partant à côté de … ». EN "beside house 41".
- 006 P1: « Personne n'a jamais vraiment su de qui venait l'idée. » → « L'auteur de l'idée n'a jamais vraiment fait l'unanimité. » EN "Nobody has ever quite agreed", which is about agreeing, not knowing.
- 006 P3: « Il avait déjà essayé » → « Il avait un précédent, à Maricel… ». EN "He had done something like it before". The old FR said he had only "tried".
- 004 P2: « En septembre » → « En septembre suivant ». EN "That September" means 1927.
- 024 P5: « se redresse » → « amorce son redressement ». EN "began to recover".
- 018 P8: « en créditent un roi » → « l'attribuent à un roi ». Same meaning, now idiomatic, and it matches 025 « attribuent ».

**Consistency (Extra announcements)**
- 018 P9: « En version essentielle ou complète, un court Extra vous attend … : passez » → « Dans la version essentielle et la visite complète, il y a un court Extra … . Passez ». This now matches the 015 wording and the glossary.

**Naturalness / clarity for the ear**
- 003 P1: « n'a jamais vraiment marché » → « ne marchait jamais vraiment ». The tense now fits "never quite worked". « alors » was dropped for length; the 1990 date in the sentence before carries the year.
- 003 P2: « La solution est venue de l'intérieur des tours, devenu un lieu nocturne … Il écrivait » → « La solution était dans ces tours. Leur intérieur est devenu un lieu nocturne … Le magazine écrivait ». The old « venue de l'intérieur » read as "came from insiders", and « Il » had no clear antecedent.
- 004 P6: « une étude de la famille Reventós » → « un cabinet de la famille Reventós ». « étude » suggests a notary's office.
- 006 P5: « un terrain restant » → « un terrain délaissé ». The old wording was unidiomatic. 006 P3/P4: removed two colons to stay within length; wording otherwise unchanged.
- 017 P5: « porte en arc tenant lieu de Porqueres » → « la porte en arc qui représente Porqueres ».
- 018 P2: « pour ne pas concurrencer Séville » → « pour éviter la concurrence ». This is closer to EN "so as not to compete" and adds no name. « donc » was dropped for length.
- 019 @where: « (l'un des nombreux 61 de la rue) » → « (la rue compte plusieurs 61) ». EN says "several".

**Bridges** (bridges.txt and bridges_001-025.txt kept identical)
- 012 H>015: « sautez la maison quatre-vingt-un » → « ne vous arrêtez pas à la maison quatre-vingt-un ». EN "don't stop at house 81". The listener still walks past the house. 44/45 words.
- 004 H>008: « qui s'incurve en Calle Príncipe de Viana » left as is. Every clearer wording went over the English length of 44 words. It is understandable.

## Lead points checked
- 014: « douze jours, surtout à travers la Catalogne et l'Aragon » is present. OK.
- 022: « Casa de Águila » kept.
- Rulers: « Alphonse treize » appears in 002, 018 and 019, and « Victoire-Eugénie » in 002. There are no other forms and no Roman numerals.
- Monastery: titles and cues use « Monestir de Sant Miquel ». Speech uses « le monastère de Sant Miquel » (016, 017), and 017 adds « en catalan le Monestir de Sant Miquel » as the English does. Elsewhere speech says « le monastère ». Consistent.
- 004 « quelque 1600 lieux traversés »: in this context a French voice reads it as a count, mille six cents (seize cents is also fine). OK.
- Quotations: no quote keeps an original French wording. All quotes are translated from the English, with the English framing kept (« en espagnol », « en catalan »). The only original-language wordings are the Spanish ones the English itself quotes (007 « Castilla, Navarra y País Vasco », 009 una simbiosis, 016 leves pendientes). One WebFetch of https://poble-espanyol.com/fr/ on 31 Oct 2026 found no official French names for the photo exhibition (023), the monastery, the sculpture garden, FIESTA or the Tablao. It gives only « la Fondation Fran Daurel ». The translated titles therefore stand.
- TTS: the spoken bodies contain no + & % × ° # ; or parentheses. The only digits in speech are years, « 117 » inside the 001 quote (as in the English) and « 1600 » in 004. House numbers are spoken in words. « · » appears only in the cue titles, as in the English.
- Nothing added: no new dates, names, figures or views were found.

## For the lead (no action required for release)
- 013 P4 « Ici, le village travaille » (EN "This quarter is where the village works") and 012 P2 « version d'une maison de Rupit » (EN "the Poble's version of…") are slightly compressed. They are acceptable, but there was no word budget left to expand them.
- Many tracks sit exactly at the English word count. This is because the checker counts French spaced punctuation (« » : ?) as words. Real spoken length is shorter.
- 015 @where drops the production note "Speak only the landmarks ticked on site". Production must still trim P1 on site if needed, as the translator flagged.
- 006 « excavateurs de Montjuïc » (Mirador joke) kept. It is a literal rendering of the quote and the irony is clear.

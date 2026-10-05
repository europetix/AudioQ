# Translation brief — Musée d'Orsay audio guide, V5 (75 tracks) → ES / FR / DE

You translate English audio-guide scripts into ONE target language. The text will be read aloud by a female
synthetic voice (ES: Dalia, Mexican Spanish; FR: Vivienne, France; DE: Katja, Germany) to travellers walking through
the Musée d'Orsay with headphones. DO NOT EDIT ANY EXISTING FILE. Only write your own output JSON files (and your notes file).

## Source
/home/user/AudioQ/orsay_v5/v5/tracks/NNN.perf.txt — header lines (@title, @where, @what, @sources …), a line `---`, then the
spoken body. The body contains direction tags in square brackets: [pause] [long pause] [warmly] [quietly] [amused] [curious]
[conspiratorial] [reverent] [wry] [lightly], and *emphasis* marks. Paragraphs are separated by a blank line.
The English is fact-checked against the museum's own pages: it is the single source of truth. Read @what and @sources too:
they give the official French title, date and the museum's URL (the URL slug often spells the official French title).

## Style model (read before you start)
The client approved these translations of an earlier guide, after an independent review. Match their voice:
- ES: /home/user/AudioQ/orangerie_v5/v5/i18n/es/tracks/003.perf.txt, 020.perf.txt, 040.perf.txt
- FR: /home/user/AudioQ/orangerie_v5/v5/i18n/fr/tracks/003.perf.txt, 020.perf.txt, 040.perf.txt
- DE: /home/user/AudioQ/orangerie_v5/v5/i18n/de/tracks/003.perf.txt, 020.perf.txt, 040.perf.txt
Adapted FOR LISTENING, not translated line by line.

## Rules (all mandatory)
1. FACTS: identical to the English. Same names, dates, numbers, places, measurements, attributions and hedges ("probably",
   "the story goes", "allegedly", "if it is on show", "the museum says"). Add nothing, drop no fact, do not "improve" a fact
   from your own knowledge. If you think the English is wrong, translate it anyway and flag it in your notes.
2. YEARS AS DIGITS: every year of the English must appear in your text written as digits. The English often writes years in
   words ("eighteen sixty-five" → 1865, "nineteen hundred and six" → 1906, "nineteen-oh-four" → 1904, "twenty twenty-six" →
   2026). Decades: write them naturally (ES "la década de 1910", FR "les années 1910", DE "die 1910er-Jahre"). Days of the month
   and ages may be words or digits.
3. LENGTH: spoken word count ≤ the English word count; aim about 5% shorter. The checker counts words after removing tags.
4. STYLE FOR THE EAR: short sentences, one idea each (average 9–12 words). Split long English sentences. Natural storytelling
   in the target language, like a good live guide. No semicolons, no parentheses in the spoken text. At most two dashes (— or –)
   per track.
5. ADDRESS: formal everywhere — ES usted (never vosotros/tú), FR vous, DE Sie.
6. ES vocabulary must work for Latin America AND Spain (neutral): avoid coger, vale, ordenador, móvil, vosotros, zumo,
   "en el sitio". Prefer neutral words.
7. TAGS: keep every delivery tag ([warmly], [quietly], [amused], [curious], [conspiratorial], [reverent], [wry], [lightly])
   in the SAME ORDER and in the SAME PARAGRAPH as the English. A delivery tag colours the rest of its paragraph. Keep every
   [pause] / [long pause] of the English, and ADD [pause] where a listener needs a breath (after a reveal, before "look at…"):
   typically 3–6 pauses per track. Use only these tags. You may keep *emphasis* on the matching word or drop it.
8. PARAGRAPHS: exactly the same number of paragraphs as the English, in the same order.
9. NAVIGATION (travellers rely on it): the last paragraph tells the visitor where to go next and what to look for. Translate
   it precisely: level, room number, side (Seine side / rue de Lille side), left/right, up/down, near what, and what the next
   work looks like (colours, size, shape, figures). Never say "next track". Default phrase for "play its track there":
   ES "Escuche su pista allí." · FR "Écoutez sa piste là-bas." · DE "Spielen Sie dort den passenden Titel ab."
   (plural: su pista / leur piste / den passenden Titel). Where the English says "in front of it / beside it", keep that:
   ES "Escuche su pista frente a él/ella", FR "Écoutez sa piste devant lui/elle", DE "Spielen Sie den passenden Titel vor ihm/ihr ab".
10. LOANS AND OPTIONS: tracks 008, 021, 046 and 053 contain conditional text for when a painting is away on loan (Tokyo,
   14 Nov 2026 – 28 Mar 2027), and 012 is optional. Translate every "if…", "otherwise…", "if the wall is empty…" exactly:
   a wrong condition sends a traveller to the wrong room.
11. ARTWORK TITLES: the museum is French and its official titles are French. Where the English gives the French title plus an
   English gloss ("Un enterrement à Ornans, A Burial at Ornans"): ES/DE keep the French title and translate the gloss
   ("Un enterrement à Ornans, Un entierro en Ornans" / "…, Ein Begräbnis in Ornans"); FR uses the French title once, no gloss.
   Where the English gives only the French title, keep it in all languages. Where the English gives only an English title
   (e.g. "The Gates of Hell", "The Rouen Cathedrals"), ES/DE translate it naturally, FR uses the museum's French title
   (La Porte de l'Enfer, Les Cathédrales de Rouen…). FR: check every French title against @what / @sources (URL slug) and use the
   museum's exact wording. Same work → same name in every track.
12. QUOTATIONS (most quotes in this guide were originally said or written in French: critics, artists, Van Gogh's letters to
   Theo from Arles and Auvers, Detaille, Paul Claudel, Pompon…):
   - ES and DE: translate the English quote faithfully and keep it as a quotation, introduced the same way as the English
     ("wrote", "said", "the museum puts it…"). Do not embellish it.
   - FR: NEVER put your own back-translation in quotation marks — it would pass as the original words. Either (a) use the
     original French wording, ONLY if you have verified it verbatim with WebSearch (allowed_domains such as
     ["musee-orsay.fr"], ["vangoghletters.org"], or two reputable independent sources; at most 15 searches in total), and
     list the source URL in your notes file; or (b) turn it into reported speech without quotation marks
     ("Detaille écrit que la gare est superbe et qu'elle ressemble à un palais des beaux-arts."). Keep the meaning exact.
   - Quotes the English already gives as reported speech stay reported speech in every language.
13. "The museum says / the museum calls it": keep the attribution exactly where the English has it. Never add new ones.
14. TTS SAFETY: spell out regnal numbers (ES Napoleón Tercero, FR Napoléon trois, DE Napoleon der Dritte / des Dritten),
   "Dr" → ES el doctor / FR le docteur / DE Doktor, "St" → Saint. No symbols (& % × °), no abbreviations. Room numbers as
   digits ("sala 14", "salle 14", "Saal 14"); room 10b → "sala 10 B" / "salle 10 B" / "Saal 10 B". Levels as digits.
15. NO ticket prices, opening hours or booking talk beyond what the English says.

## Glossary (use consistently)
| English | ES | FR | DE |
|---|---|---|---|
| Musée d'Orsay | el Museo de Orsay | le musée d'Orsay | das Musée d'Orsay |
| the nave / the central aisle (of the old station) | la nave central / el pasillo central | la nef / l'allée centrale | das Mittelschiff / der Mittelgang |
| level 0 / level 5 / level 2 / ground floor | el nivel 0 / nivel 5 / nivel 2 / la planta baja | le niveau 0 / niveau 5 / niveau 2 / le rez-de-chaussée | Ebene 0 / Ebene 5 / Ebene 2 / das Erdgeschoss |
| room 14 | la sala 14 | la salle 14 | Saal 14 |
| Seine side / Lille side (rue de Lille) | del lado del Sena / del lado de la rue de Lille | côté Seine / côté rue de Lille | auf der Seine-Seite / auf der Seite der Rue de Lille |
| escalators / lifts | las escaleras mecánicas / los ascensores | les escalators / les ascenseurs | die Rolltreppen / die Aufzüge |
| sculpture terrace(s) | la terraza / las terrazas de esculturas | la terrasse / les terrasses des sculptures | die Skulpturenterrasse(n) |
| the Salon (annual exhibition) | el Salón | le Salon | der Salon |
| Salon des Indépendants, Salon d'Automne | unchanged | unchanged | unchanged |
| the State (French) | el Estado | l'État | der Staat |
| World's Fair / Universal Exposition (1900) | la Exposición Universal | l'Exposition universelle | die Weltausstellung |
| Second Empire | el Segundo Imperio | le Second Empire | das Zweite Kaiserreich |
| Impressionists / Post-Impressionism | los impresionistas / el posimpresionismo | les impressionnistes / le postimpressionnisme | die Impressionisten / der Postimpressionismus |
| the Nabis / Symbolism / Art Nouveau | los nabis / el simbolismo / el Art Nouveau | les nabis / le symbolisme / l'Art nouveau | die Nabis / der Symbolismus / der Jugendstil (Art nouveau) |
| still life / canvas / panel / plaster / bronze | bodegón / lienzo / tabla / yeso / bronce | nature morte / toile / panneau / plâtre / bronze | Stillleben / Leinwand / Tafel / Gips(modell) / Bronze |
| Musée du Luxembourg / the Louvre | el Museo del Luxemburgo / el Louvre | le musée du Luxembourg / le Louvre | das Musée du Luxembourg / der Louvre |
| Opéra (Garnier) | la Ópera / la Ópera Garnier | l'Opéra / l'Opéra Garnier | die Opéra / die Opéra Garnier |
| Theo (Van Gogh's brother) | Theo | Théo | Theo |
| loan / away on loan | préstamo / prestado | prêt / prêté | Leihgabe / ausgeliehen |
| French names of spaces seen on signs: Salon de l'horloge, Salle des fêtes, Galerie Seine 2, Terrasse Rodin, Café Campana, À qui appartiennent ces œuvres ?, Paris, capitale d'une nation moderne, SORTIE | keep in French, add the English gloss translated where the English glosses it | keep | keep in French, add the gloss translated where the English glosses it |
| Haussmann, Laloux, Victorine Meurent, Laure, Gachet, Saint-Rémy, Auvers-sur-Oise, Pont-Aven, Arles | unchanged | unchanged | unchanged |

## Output
For EACH assigned track write one file: /tmp/claude-0/-home-claude/98e7af58-dd32-56e0-a687-5f082c01b624/scratchpad/orsay_i18n/<lang>/NNN.json
  {"title": "<translated @title>", "where": "<translated @where, normal punctuation allowed>", "body": "<spoken body with tags, paragraphs separated by \n\n>"}
@title keeps the English pattern "Artist — Title"; titles with a gloss may keep it in parentheses (the title is not spoken).
Write valid JSON with Python json.dump(..., ensure_ascii=False, indent=1).

Self-check before finishing (fix and rewrite every failure, then run it again):
  python3 /home/user/AudioQ/orsay_v5/v5/i18n/assemble.py --check /tmp/claude-0/-home-claude/98e7af58-dd32-56e0-a687-5f082c01b624/scratchpad/orsay_i18n LANG
It prints one line per file: track, words yours/English, OK or the errors (tags, pauses, paragraphs, length, missing years,
semicolon/parenthesis, unknown tag). Only your own block matters, but all lines must be OK at the end.

Notes: append your flags to /tmp/claude-0/-home-claude/98e7af58-dd32-56e0-a687-5f082c01b624/scratchpad/orsay_i18n/notes/<lang>_<first>-<last>.md
(terms you were unsure of, every quotation and how you handled it, FR: the URL for each verified original quote, titles you
could not confirm, anything in the English that looked wrong).
Final report: tracks written, self-check result, the main flags. Max ~150 words.

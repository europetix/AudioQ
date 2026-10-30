# FR review: Catedral de Sevilla 001–028 and bridges (30 Oct 2026)

This is an independent review of fr/*.json and fr/bridges.txt against v5/tracks/*.perf.txt and v5/bridges/*.txt.
After the edits, `assemble.py --check … fr` reports all 28 tracks OK (exit 0). Assemble was only run with --check.

## A. Changes (track: before → after, why)
- **001:** « l'essentielle une heure et quart » → « la version essentielle une heure et quart ». This matches the version names in Alcázar FR 001 (« La visite complète … la version essentielle … celle des temps forts »).
- **001:** « Dans la version temps forts » → « Dans la version des temps forts ». Same reason.
- **001:** « Son histoire arrive en fin de visite complète » → « Son histoire vient vers la fin de la visite complète ». This is closer to "near the end of the full tour" and reads better.
- **002:** Arabic names are back to the standard French forms:
  - « Abou Yaqoub Youssouf » → « Abu Yaqub Yusuf »
  - « al-Mansour » → « al-Mansur »
  - « Ali al-Ghoumari » → « Ali al-Ghumari »

  Why: the francized « ou » spellings are popular forms, not the usual scholarly French ones. French Wikipedia uses « Abu Yaqub Yusuf » (https://fr.wikipedia.org/wiki/La_Giralda) and « Abu Yusuf Yaqub al-Mansur » (article title found by search, fr.wikipedia.org/wiki/Abu_Yusuf_Yaqub_al-Mansur). The approved Alcázar FR also keeps « al-Mutamid » with *u*. French Wikipedia calls the second master « Ali de Gómara », but « al-Ghumari » follows the English and the scholarly transliteration.
- **006:** « Abou Yaqoub Youssouf » → « Abu Yaqub Yusuf ». Keeps the spelling consistent with 002.
- **011:** « Continuez jusqu'à l'extrémité de l'église » → « jusqu'à l'autre extrémité de l'église ». The English says "far end". The new wording matches 010, 012 and 015.
- **016:** « dans des attitudes décentes qui ne distraient pas le prêtre » → « dans des attitudes bienséantes, qui ne distrairaient pas le prêtre ». "Decorous" is *bienséant*, while *décent* suggests the opposite of indecent. The conditional is also correct.
- **019:** « Contre l'un, une statue du roi » → « À côté de l'un ». The English says "Beside one". The @where « contre un pilier » → « à côté d'un pilier » was changed for the same reason. This matters because it tells the listener where to look.
- **020** (lead's point, aligned with the revised English cue):
  - Before: « Il y a d'abord un court Extra sur la salle capitulaire elle-même. Ensuite, le prochain arrêt principal, dans la même salle, est l'Immaculée de Murillo. »
  - After: « Dans la Sala Capitular, il y a d'abord un court Extra sur la salle elle-même. Le prochain arrêt principal, dans cette même salle, est l'Immaculée de Murillo. »

  The rest of the route (Antecabildo, curved corridor, oval chapter house) is unchanged. This closes translator note 020.
- **025:** « L'une est cette cour. L'autre la domine » → « Une autre la domine ». "Another" is not "the other". With « l'autre », only two parts survived, but 028 names a third, the Puerta del Perdón.
- **027:** « une ânesse à une bande blanche et l'autre sombre » → « une ânesse dont une bande était blanche, et l'autre sombre ». The old phrase was ungrammatical. The meaning is unchanged.
- **028:** « Nous espérons qu'elle restera avec vous » (an anglicism) → « Nous espérons qu'elle vous accompagnera ».

## B. Checked, no change needed
- **Navigation.** I compared the last paragraph of all 28 tracks with the English: the rooms, their order and the landmarks all match.
  - "keep to the right" is « droite » in 002–006. The English has no other left/right.
  - "side where you came down from the tower" and "far side from the tower" are rendered exactly.
  - The Capilla Real is seen through its grille only (001, 023).
  - The exit is by the Puerta del Perdón, with no re-entry (001, 028).
  - Every Extra announcement is followed by « le prochain arrêt principal » (004, 008, 016, 018, 020).
  - "Stay here" / "in this room too" are kept (014, 018, 019, 021).
- **Conditionals.** These are all present: Lagarto/Príncipe entrances, "Not climbing?", "if a Mass is on", "if you stopped at the choir", "if your route took you there", "if you can see it" and "If so" (025).
- **@title.** Every one starts with the same Spanish space name as the English. The Extras keep the « · Extra · » pattern. Spanish place names are unchanged throughout.
- **Bridges.** There are 7 English lines and 7 FR lines, with the same keys. Each follows the same route and starts with « Dans cette version courte, ». 014 H>025 « sautez la suite » is acceptable for "skip that". It skips the bones stop and everything up to 025.
- **TTS.** Speech has no symbols, semicolons, parentheses, abbreviations or Roman numerals. Regnal names are written in words (« Ferdinand trois », « Charles trois », « Pierre premier »), as in Alcázar FR (« Abd al-Rahman trois »). Years are in digits. Formal *vous* is used throughout.
- **Quotations** (002, 006, 011) are faithful renderings of the English and are introduced the same way. Hedges are kept: « Selon la tradition … l'aurait dit », « La cathédrale la dit », « serait une copie ».
- **Additions.** I found nothing added to the English.

## For the lead
- **TTS:** Vivienne may read *Yusuf* / *al-Mansur* / *al-Ghumari* with a French /y/ (as in « Abu Yaqub Yusuf »). If that sounds wrong in the render, use a pronunciation lexicon entry. Do not respell the text.
- 001 calls it « les Archives des Indes », a French gloss of the English "Archive of the Indies". Alcázar FR uses « l'Archivo de Indias » because its English used the Spanish name. Both are fine. Unify only if you want the same name in both guides.

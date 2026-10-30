# FR review — Real Alcázar de Sevilla, 35 tracks + 10 bridges (30 Oct 2026)

Reviewer: independent FR editor. Method: every paragraph of 001–035 read side by side with the current English
(v5/tracks/NNN.perf.txt), title and @where included; every bridge line against v5/bridges/*.txt.
Check: `assemble.py --check alc_i18n fr` → 35/35 OK after edits (exit 0). Backup of the translator's files:
scratchpad/frrev/fr_backup/.

## Lead's points
- Bridges 022 E>025 and 022 H>025 aligned to the current English ("skip the stops along the palace wall and the Jardín del
  Príncipe"): « laissez de côté les jardins au pied du palais : » → « sautez les arrêts le long du mur du palais et le Jardín
  del Príncipe : ». « sautez » (as in bridge 002 E>004) also trims the line (49 words vs English 46).
- 007 aligned to "finished within two years after this inscription": « et achevé à moins de deux ans de cette inscription »
  → « et achevé dans les deux années qui suivirent cette inscription ». The translator's open point on 007 is now closed.
- 013 / 026 Diego de Esquivel: kept as in the English (frieze end of the sixteenth century, Grutesco finished 1629). No change.
- Leaflet numbers and Spanish names: every @title starts with the same number and Spanish name as the English
  (CRA Extras "CRA 20 · Extra ·" / "CRA 23 · Extra ·"); all numbers in last paragraphs and bridges match the English
  (checked by script for bridges). Left/right: every instance matches the English (005, 006, 007, 009, 011, 016, 017,
  021, 022, 023 checked one by one).
- Version names: only 001 names them (« la visite complète », « la version essentielle », « celle des temps forts »),
  same pattern as the approved Uffizi FR; bridges all open « Dans cette version courte, » (glossary). Consistent.

## Changes (track, before → after, why)
| Track | Before | After | Why |
|---|---|---|---|
| 002 | Votre premier passage n'est donc pas une relique des Almohades. | Ce que vous avez franchi en premier n'est donc pas une relique des Almohades. | "the first thing you walked through"; « passage » was ambiguous (corridor). |
| 004 | Traversez cette salle jusqu'au numéro 3 | Sortez par le fond de cette salle vers le numéro 3 | Navigation: English says "through the far side of this hall". |
| 006 | La porte du Lion, par où l'on entre, | La porte du Lion, celle de votre entrée, | English "you came in by"; keep formal address to the listener. |
| 007 | achevé à moins de deux ans de cette inscription | achevé dans les deux années qui suivirent cette inscription | English changed (lead). |
| 007 | une devise qui, de toute façon, place Dieu au-dessus de lui | une devise qui, quelle que soit votre lecture, place Dieu… | "however you read it" (meaning lost). |
| 011 | aménagés en jardin creusé | aménagés en jardin en contrebas | "sunken garden": same term as the rest of the track and @where. |
| 011 | quand vous regardez la cour depuis votre angle d'arrivée | quand vous regardez la cour dans sa longueur, depuis votre angle d'arrivée | Navigation: "as you look down the courtyard" fixes which long side is on the left. |
| 014 | dans une chambre du palais … et bénit le mariage | dans une salle du palais … et donna aux époux la bénédiction nuptiale | "chamber" ≠ bedroom; "gave the couple the nuptial blessing" rendered exactly. |
| 017 | Le prince de ces noms serait, dit-on, Jean | Le prince de ces noms est en général identifié à Jean | Hedge: "is usually said to be". |
| 018 | son trisaïeul | son arrière-arrière-grand-père | Same fact (Alfonso X → Sancho IV → Fernando IV → Alfonso XI → Pedro), clearer for the ear. |
| 022 | En bas, il y avait un jardin creusé dans la terre pour l'été. | Ici, en bas, il y avait un jardin en contrebas, creusé dans la terre pour l'été. | "Down here was a sunken garden": restores "sunken", consistent term. |
| 028 | Pourtant, ce pavillon honore ce mariage. | Pourtant, ce pavillon fut élevé en l'honneur de ce mariage. | "was put up in honour of": the fact is the building's purpose. |
| 028 | Il y a ici un tour triste. | L'histoire prend ici un tour triste. | Natural French. |
| 033 | son jardin enfoui | son jardin en contrebas | "its sunken garden" (the Baths); « enfoui » is the title word of 011 (Doncellas, buried garden) and would mix the two. |
| 035 | Ce sont les derniers arrêts du Cuarto Real Alto. | C'est la fin des arrêts du Cuarto Real Alto. | "That is the end of the Cuarto Real Alto stops." |
| Bridges 022 E>025, H>025 | see above | see above | English changed (lead). |

## Verified, no change needed
- Facts, dates (all years in digits), hedges ("probably", "may", "is said to", "one reading", "tradition", "the Alcázar
  calls/says", "one historian"), every "if…" (028 screens, 035 listening upstairs, 027 "if you hear it").
- Quotations: 007, 010, 014 translated from the English and introduced the same way; 018 / 022 / 034 reported speech as in
  the English. No originally French quotation, so nothing to verify online (no pages fetched).
- TTS scan: no + & % · × ° ; ( ) in bodies, no Roman numerals in speech, no abbreviations, no spaced dashes.
- Formal « vous » throughout. Extra announcements (« a un court Extra sur… ») and « Le prochain arrêt principal est… »
  consistent; the Cuarto Real Alto always « visite séparée à horaire fixe ».
- Paragraph count, tag order and pauses: enforced by the check, all OK.

## For the lead (no action required for FR)
- Titles 004 and 018 display « Alphonse XI / Alphonse X » because the English titles use Roman numerals. Fine if titles are
  display-only; if titles are ever spoken, change to « Alphonse onze / Alphonse dix ».
- French bridges run 0–6 words longer than the English (French expansion); all keys, numbers and routes match.

Verdict: ready.

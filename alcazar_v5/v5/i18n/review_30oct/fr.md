# FR notes — Real Alcázar de Sevilla, 35 tracks + bridges (30 Oct 2026)

Files: alc_i18n/fr/001.json … 035.json, alc_i18n/fr/bridges.txt (10 lines, same keys as v5/bridges/*.txt).
Self-check: `assemble.py --check alc_i18n fr` → 35/35 OK. Total spoken words 9,309 vs English 9,602 (−3.1 %).
Every track has 3–4 pauses (English 0–1), same tags in same order, same paragraph count. No pages fetched.

## Official names used (unchanged, from the leaflet legend)
Source: https://alcazarsevilla.org/wp-content/uploads/2024/11/triptico_alcazar_sevilla.pdf (legend 1–53, as copied in
research/VISIT_ROUTE_AND_SPACES_OCT2026.md). Spoken as « le numéro N du plan de l'Alcázar, <nom espagnol> » on first mention,
then « le numéro N ». Spanish names spoken as in the English (Salón del Techo de Carlos Quinto / Felipe Segundo, Pabellón de
Carlos Quinto); @where keeps the English's "Carlos V / Felipe II" spelling. Glossary terms: « visite séparée à horaire fixe »,
« dans cette version courte », « un court Extra ».

## Name/TTS choices
King Pedro → « le roi Pierre / Pierre premier » (glossary); inscriptions keep « don Pedro ». Regnal numbers in words:
Abd al-Rahman trois, Ferdinand trois, Alphonse dix / onze / treize, Alphonse quatre de Portugal, Philippe deux / trois / cinq,
Charles Quint. Titles 004 and 018 keep « Alphonse XI / Alphonse X » because the English titles use Roman numerals (display only).
Enrique → Henri, Trastámara → Trastamare, Constanza → Constance, John of Gaunt → Jean de Gand, the Just → le Justicier,
Sand Snakes → les Aspics des Sables (French TV names), Lawrence d'Arabie.

## Quotations
- 007 Castilian façade inscription (originally Spanish): FR translation of the English rendering in « », introduced the same way.
  Arabic motto: transliteration kept + « il n'y a de vainqueur que Dieu ».
- 010 Arabic greeting: « Gloire à notre seigneur le sultan don Pedro, que Dieu l'aide. » (faithful to the English).
- 013 Arabic inscription on the doors: reported speech, as in the English.
- 014 Sandoval chronicle (originally Spanish): « la grande salle qu'on appelle la demi-orange », from the English.
- 018 leaflet line (« la transition radicale vers le nouvel ordre chrétien ») and 022 school notes (« Aucun fondement
  historique ») kept as reported speech without quotation marks, as in the English.
- 034 Niculoso's signature: reported without quotation marks, as in the English; the quote marks around "Pisano" (a word
  mention) were dropped for the ear.
- No originally French quotations.

## Things to check in the English (translated as written)
- 007 "finished within two years of this inscription": ambiguous (before or after 1364); kept ambiguous (« à moins de deux ans »).
- 002 "Stables, storerooms and houses followed": read as later buildings on the theatre site (« Puis vinrent… »), which fits
  "most of them were cleared away" in the 1930s.
- 013 and 026: Diego de Esquivel is credited with the Embajadores frieze (end of the sixteenth century) and with the Grutesco
  paintings (seven years, finished 1629). Plausible, but worth a check that it is the same painter.
- Bridge 022 E>025 / H>025 "skip the garden front": unclear phrase; rendered as « laissez de côté les jardins au pied du
  palais » (the skipped tracks are 023 Jardín del Príncipe and 024 Danza). Please confirm.
- 031 / 032 spell "Vega-Inclán" in speech but the leaflet name "Jardín Marqués de la Vega Inclán": both kept as in the English.

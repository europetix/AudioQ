# DE review, FC Barcelona Museum, 001–034 + bridges (14 Nov 2026)

Reviewer: independent DE editor. Checked every track sentence by sentence against the current English (`v5/tracks/NNN.perf.txt`), including the revised 010.

**Verdict: ready.** The translation was already accurate and natural. I made 17 small edits in 15 tracks: one sync with the revised English 010, one abbreviation removed (TTS), one hedge restored, one possible navigation confusion removed, and the rest are fluency fixes. No facts changed. Bridges unchanged.

## Checks run
- `assemble.py --check … de`: all 34 OK, exit 0 after the edits. Every track is still shorter than the English (max 282/292 in 013).
- Navigation scan by script and by eye. For all 34 tracks, the last paragraph has the same places, the same order and the same things to look for as the English. Every cue destination matches the English destination (016 and 029 both have two cues, both correct). Every spoken `<place> · <title>` matches the destination's DE @title character for character. 034 has no cue, as in the English. The script flagged 010 only because of the "." in "91.648". I checked it by hand: it matches 011.
- Place names: there are 18 distinct DE places, each used identically in every title, cue and bridge, as in the translator's glossary. "The way out" is "Der Ausgang" only as the exit's name. 024 E>026 and 025 say "dem Weg aus dem Saal hinaus", which keeps the fixed name free.
- Bridges: 10 of 10 present, with the same keys as the English and one line each. All start "In dieser Kurzfassung", all end on the exact DE destination title, and none is longer than the English (024 E>026 is equal, 31/31). Both 024 bridges keep "wenn die Show vorbei ist".
- 001 honesty frame and the 360° warning in 001 and 024: exact, not softened.
- PLAN §4 NEVER list: none of the banned items appear ("Nou Camp", biggest stadium, napkin here, Franco ordered, regime's club, money, lyrics, 2017, gate numbers). The 032 song line is a paraphrase, as in the English.
- Quotes: "Salid y disfrutad" (008) is the only original-language wording kept, as in the English. I verified it on fcbarcelona.es/es/noticias/643913 with one WebFetch: "Johan Cruyff dio las últimas instrucciones a sus hombres: "Salid y disfrutad"." All other quotes are faithful translations of the English, with their attributions and hedges kept.

## Changes (track: before → after, why)
1. **002** cue: "bleiben Sie nahe seiner Tür stehen, aus dem Weg:" → "bleiben Sie in der Nähe seiner Tür stehen, ohne den Weg zu versperren:". The bare "aus dem Weg" is unidiomatic, and the new wording is clearer as an instruction.
2. **003**: "mit rund zweitausendvierhundert Quadratmetern zu füllen." → "mit rund zweitausendvierhundert Quadratmetern, die gefüllt werden wollten." The old phrase was ungrammatical-sounding German.
3. **004**: "wie viele der Besucher um Sie herum." → "wie so manche der Besucher heute um Sie herum." This restores the English "today", which had been dropped.
4. **008**: "kam der Kapitän Alexanko für Guardiola," → "… für Guardiola ins Spiel,". "Came on" needs "ins Spiel" in German, or it reads as "came instead of".
5. **010** (English revised): "Für Xavi war es das letzte Spiel und der letzte Titel in diesen Farben." → "Für Xavi war es sein letztes Spiel und sein letzter Titel in diesen Farben." This now matches "For Xavi, it was his last game, and his last trophy in these colours." The [pause] before it is kept.
6. **011**: "…Weltrekord für den Frauenfußball, mit den Worten des Clubs." → "…, so der Club." The attribution is kept, in natural German.
7. **013**: "verweigerte die Freigabe, weil der Wechsel im Juli hätte erfolgen müssen," → "…, mit der Begründung, der Wechsel hätte im Juli erfolgen müssen,". The English says "saying it had to go through in July". This is the federation's stated reason, not a fact in our voice, so I restored the attribution.
8. **015**: "die aus ihr hervorgingen. Im WM-Finale 2010" → "die aus La Masia hervorgingen. Im Finale der Weltmeisterschaft 2010". "ihr" had a confusing referent (the sentence before is about the "Internat"). "WM" is an abbreviation, which the brief rules out for TTS.
9. **023**: "in der Saison 2011–2012" → "in der Saison 2011 bis 2012". The voice could read the dash as "minus" or skip it.
10. **024**: "wenn das Personal Sie lässt," → "wenn das Personal Sie hineinlässt,". The old verb was incomplete.
11. **025**: "das erste von Tausenden in diesem Rund." → "… in jenem Stadionrund.". The listener is standing in the *round room*, so "diesem Rund" could be heard as that room. The English "that bowl" means the old stadium.
12. **028**: "Die Mannschaft spielt hier wieder seit November 2025," → "Die Mannschaft spielt seit November 2025 wieder hier,". The new word order is natural German.
13. **028**: "der neu gebaute dritte Rang: fertig, aber noch nicht für Fans geöffnet." → "…: Er steht, ist aber noch nicht für Fans geöffnet.". The English says "built", not "finished". The stadium is explicitly unfinished, so "fertig" overstated it.
14. **028**: "für einige Monate, Richtung Montjuïc," → "für einige Monate, an den Montjuïc,". The English says "for Montjuïc", a destination, not a direction.
15. **029** @where: "stellen Sie sich daneben, aus dem Weg." → "…, ohne im Weg zu stehen." Same reason as item 1.
16. **030** cue lead-in: "für den dieses Stadion angeblich gebaut wurde:" → "für den dieses Stadion, wie man sagt, gebaut wurde:". The English says "people say". "angeblich" adds a sceptical tone the English doesn't have; 031 itself makes the correction.
17. **032**: "Sie sangen nicht nur sie." → "Sie sangen nicht nur diese Hymne." "sie … sie" is unclear by ear.

All edits are in `cn_i18n/de/NNN.json`. I mirrored them in the translator's `de_src/batch*.txt`, so re-running `de_src/build.py` reproduces the edited JSON (checked). The pre-review state is saved in `cn_i18n/de_prereview/`.

## Reviewed and left as is
- 001 "etwas über anderthalb Stunden": this follows the final English (the translator's point 3 for the lead).
- 011 "Zusammen gewannen Alexia und Aitana als Barça-Spielerinnen fünfmal den Ballon d'Or. 2026 gewann Alexia ihren dritten." This is exactly as ambiguous as the English, in two separate sentences. Adding a clarification would add content. The lead should decide in the English (F18.10).
- 012 title "Das Trikot, das fürs Tragen zahlte": an odd paradox, like the English, and the story explains it. Kept, because changing it would also mean changing 011's cue.
- 016 "in der englischen Fassung des Clubs" and 030 "in ihrer englischen Fassung": these are the English attributions translated honestly. They are slightly odd before a German quote, but accurate.
- 027 "Barça gehört niemandem. [pause] Außer seinen socis, den Mitgliedern.": this keeps the turn. Acceptable.
- 031 "aus Ländern hinter dem Eisernen Vorhang": "Ländern" adds no fact. Kept for natural German.
- Ambiguities kept as in the English: 007's "twenty-five" (inside the hundred or not) and 029's "two substitutes … scored twice".

## For the lead
1. **030 referendum percentage** ("Etwas mehr als achtundsechzig Prozent"): PLAN §4 line 352 bans "'80.8 per cent' or any referendum percentage (F18.22)". The English 030 still says sixty-eight per cent. Please confirm in the English. The DE follows the English.
2. **011 Alexia/Aitana** sentence pair (see above): decide in the English, if at all.
3. **Listen by ear in Katja:** "91.648" in the 010 cue and the 011 title (it should come out as one number), "U14" (021) and "U19" (014), "Ballons d'Or" (022), "Salid y disfrutad" (008), and "b720" (026, as in the English).
4. If the English changes again, re-run `assemble.py --check` and the cue scan. DE titles are the cue strings.

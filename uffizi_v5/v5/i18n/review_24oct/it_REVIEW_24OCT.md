# IT review: Uffizi, 24 Oct 2026 (independent reviewer)

Scope: all 67 tracks, sentence by sentence against the English (`v5/tracks/NNN.perf.txt`), plus @title, @where and both bridge files.
Check after edits: `assemble.py --check … it` gives 67/67 OK (exit 0). No assemble run without --check.
Backup of the files before review: `scratchpad/it_review/backup_before/`.

## Automatic scans (all 67 + bridges)
- Room codes: the code sequence in every body and @where now matches the English (010 was out of order, fixed). Every @title starts with the English map code; Botticelli tracks start "Sale di Botticelli"; no A9–A12 anywhere.
- Bridges: all 23 English keys (NNN ≤ 067) have exactly one Italian line, same codes, each starting "In questa versione breve,".
- TTS: no + & % × ° · ; ( in speech; regnal numbers in words throughout (Cosimo Primo/Secondo/Terzo, Francesco Primo, Ferdinando Primo, Giulio Secondo, Francesco Maria Secondo, Urbano Ottavo); no abbreviations; ≤2 dashes per track. Spoken digits are only dates and counts an Italian voice reads naturally (24 giugno, 4 novembre, 173 dipinti, 750 metri); 5,780 is already "cinquemilasettecentottanta".

## Changes (track: before → after, why)
- 001: «Il museo la definisce uno dei primi musei al mondo creati con un concetto moderno» → «Il museo la pone tra i primissimi musei al mondo a configurarsi in senso moderno». This is the museum's own Italian wording, verified at https://www.uffizi.it/news/rinasce-lingresso-storico-degli-uffizi ("tra i primissimi al mondo a configurarsi in senso moderno"), now the same as 067. No quotation marks.
- 004: «Nei versi di Dante: «…»» → «Nei versi di Dante, Oderisi dice: «…»». The English has "he says".
- Extra announcements, unified and more natural: «La sala X ha / Questa sala ha un breve Extra» → «Nella sala X c'è / In questa sala c'è un breve Extra». Changed in 009, 015, 018, 020, 027, 031, 039, 042, 046, 049, 052, 053 and 057. 015 «La sala di Botticelli seguente ha…» → «Nella sala successiva c'è…».
- 010 (navigation): «torni nella sala A4 passando per la sala A5 … prenda quella della sala A7» → «torni attraverso la sala A5 nella sala A4 … prenda quella che porta nella sala A7». This matches the English order and "the one … that leads into A7".
- Floors named (lead's point): 022, 033 «al piano di sotto» → «al primo piano»; 037 «Al piano di sotto La aspetta» → «Al primo piano…»; 042, 047, 054 «al piano di sopra» → «al secondo piano».
- 022, 057: «Venere de' Medici» → «Venere dei Medici». That is the museum's Italian title: uffizi.it search result "Venere dei Medici, arte ellenistica" (https://www.uffizi.it/en/artworks/medici-venus).
- 024 title and body: «de' Magnoli» → «dei Magnoli». That is the museum's Italian form, from its video "La Pala di Santa Lucia dei Magnoli di Domenico Veneziano" (https://www.uffizi.it/en/video/the-st-lucia-dei-magnoli-altarpiece-by-domenico-veneziano).
- @where production notes removed, so these now match the cleaned English:
  - 038: "(la mappa non disegna … O19)"
  - 041: "(Non è noto se si possa girarci intorno: O19.)"
  - 043: "(la scheda indica audio stereo … O20)"
  - 060: "(le pareti verde chiaro … O35)"
- Decades unified with 001–034 (digits, as rule 2): 044 «negli anni Quaranta del Seicento» → «negli anni 1640», 049 «anni Venti del Cinquecento» → «anni 1520», 051 «primi anni Quaranta del Cinquecento» → «primi anni 1540».
- 044 also: «guarda così sé stesso» → «rivolge lo stesso sguardo su sé stesso» ("turns the same eye on himself").
- 046 (navigation): «alla Sua sinistra venendo dal corridoio» → «… scendendo dal corridoio», for "as you walk down from the corridor".
- 047: «Nella D5, i pittori di Ferrara.» → «Cominci dalla D5, con i pittori di Ferrara.», for "Start in D5".
- 059: «Un guanto lo tiene.» → «Un guanto lo tiene infilato.» The old wording was ambiguous.
- 063 (lead's point): «gli fu negato l'onore di essere esposto in Galleria» → «al dipinto fu negato l'onore di un'esposizione privilegiata in Galleria». This is the museum's Italian page wording, verified at https://www.uffizi.it/opere/giuditta-decapita-oloferne ("negò al dipinto l'onore di un'esposizione privilegiata in Galleria").
- 067: «quella che Le è rimasta negli occhi» → «quella che Le ha fatto fermare il passo». This is closer to "the one that stopped you", avoids a gendered participle, and stops the next sentence ("the one you remember") from being a tautology.

## Lead's points: status
- Extra: «un breve Extra» everywhere. «La prossima tappa principale è la sala …» in both halves (058 «Da qui, la prossima…»).
- Floors: «il secondo piano / il primo piano / il piano terra»; no «piano di sopra/sotto» left. «In primo piano» in 012, 020 @where and 049 is the idiom for "foreground" and is clear in context.
- Staircases: «lo scalone Lanzi / Buontalenti / Magliabechi / Granducale», consistent. 037 keeps «di *un solo* piano, fino al primo piano, non fino alla strada»; bridge 037 E>041 has «scenda di un solo piano». I found no different Italian museum name for the staircases.
- Corridors: «corridoio di Levante / di Mezzogiorno / di Ponente» are consistent in both halves and the bridges, and are the museum's Italian names (https://www.uffizi.it/opere/i-corridoi-della-galleria). «Corridoio Vasariano», «Corridoio del Veronese» (D27).
- Room word «sala» throughout. «stanza» appears only for non-gallery rooms (Domus Aurea, painted studio, Tribune "one room").
- Medici names: Cosimo Primo etc. (see scans). Botticelli rooms: «le sale di Botticelli», no codes.
- 022 «il Trattato di Vienna»: kept (sourced).

## Quotations (rule 11), re-verified
- 004/007 Dante, Purg. XI 94–96: the wording matches verbatim https://centrodantesco.it/wp-content/uploads/2018/05/Purgatorio_XI.pdf ("Credette Cimabue ne la pittura / tener lo campo, e ora ha Giotto il grido, / sì che la fama di colui è scura"). Kept.
- 013 Vasari: «Oh che dolce cosa è questa prospettiva!» matches verbatim https://www.dcuci.univr.it/documenti/OccorrenzaIns/matdid/matdid802469.pdf. Kept.
- 063 «Dio lo ha colpito per mano di donna»: verbatim on the museum's Italian page (see above). Kept.
- These stay as reported speech without quotation marks, which is correct:
  - 001/067 Family Pact
  - 023 museum on the 1966 flood
  - 045 Ferdinando's letter
  - 048 Vasari on the prior
  - 063 Artemisia's trial words
- 044 «Michelangelo delle Bambocciate» and 057 «la donna nuda» are museum wording. 051 «sans fin amour dure» is French. 009/019/024/046 are Latin or translations from Latin.

## Titles: unchecked list, one uffizi.it search each
Confirmed:
- Maestà di Ognissanti: the museum's Italian video "Giotto, Maestà di Ognissanti", https://www.uffizi.it/video/uffizi-per-tutti-video-in-lis-giotto-maesta-di-ognissanti-1300-1305-c
- Maestà di Santa Trinita: "Madonna col Bambino in trono e profeti (Maestà di Santa Trinita)"
- Trittico Portinari: https://www.uffizi.it/video/il-trittico-portinari-di-hugo-van-der-goes
- Annunciazione (Simone Martini): "Annunciazione di Simone Martini"
- Madonna del Magnificat: "Madonna col Bambino e angeli (Madonna del Magnificat)"
- Madonna della Melagrana: "Madonna della melagrana"
- Madonna del Roseto: "Madonna del roseto di Sandro Botticelli"
- Calunnia: "La Calunnia di Sandro Botticelli". The body keeps «Calunnia di Apelle», as the English does.
- Sacrificio di Isacco
- Venere dei Medici and Pala di Santa Lucia dei Magnoli: changed, see above.

Not found, so the usual Italian form is kept:
- Madonna Rucellai
- Pigmalione e Galatea
- Madonna dei Cherubini. The closest page is "Madonna col bambino in gloria", which speaks of seraphim, and it is unclear whether that is the same work.

Veronese: the museum's title is "Sacra Famiglia con San Giovannino e Santa Caterina". I kept the short form «Sacra Famiglia con santa Caterina», as the English does.

## For the lead (no change made)
- "Highlights" is «la versione dei capolavori» and "essential" is «la versione essenziale» (001). Align these with the app's Italian labels if they differ.
- Tight word counts: 021 is at 207/207 and 019 at 211/215. Any later cut in the English there needs a matching Italian cut.
- 025/057 «nella dote» translates the English. The museum's Italian page has "eredità … 1631", as translator 2 noted. The English may need a check.
- The English 052 "most important collaborator" is given as the museum's Italian «braccio destro del duca». That is fine because the line is attributed to the museum.

Verdict: ready.

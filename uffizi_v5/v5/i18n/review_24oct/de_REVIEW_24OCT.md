# DE review: Uffizi, 24 Oct 2026 (independent reviewer)

I read all 67 tracks against the current English, sentence by sentence, then the 23 bridge lines.
`assemble.py --check … de` exits 0, with all 67 tracks OK. I made a backup of the files as they were before my edits:
/tmp/claude-0/-home-claude/98e7af58-dd32-56e0-a687-5f082c01b624/scratchpad/derev/backup_de/

## Navigation audit (scripted, then read by hand)
- **Room codes:** every track has the same codes in the same order as the English, in body, @where and @title. The one exception is 044: the English says "In D1, go through to Room D4, past D2", and the German says "durch D1, vorbei an D2, in Saal D4". The order differs but the route is the same.
- **Botticelli rooms:** no A9 to A12 anywhere. The Botticelli tracks use "Botticelli-Säle · …".
- **Last paragraphs:** in all 67, the rooms, their order, the floors and the things to look for match the English.
- **Conditionals:** every condition is translated, including "if the way through is closed", "if a barrier stops you", "if the passage is closed … if not", "if reaching it means going through an exit" and "until … on loan".
- **Bridges:** there are 23 English keys and 23 German lines, each with the same key. Codes and route match, and every line starts with "In dieser Kurzfassung".
- **Unification across the two halves.** I checked these terms and they were already the same in both halves:
  - Extra announcement: „In Saal X gibt es einen kurzen Extra-Titel über …“
  - Next stop: „Die nächste Hauptstation ist Saal …“. Neither half uses "Hauptstopp" or "Weiter geht es".
  - Floors: „im zweiten Stock / im ersten Stock / ins Erdgeschoss“.
  - Lanzi in 037: „die Lanzi-Treppe nur *ein* Stockwerk hinunter, in den ersten Stock, nicht hinaus auf die Straße … Folgen Sie ihr nicht.“ The bridge 037 E>041 also says „nur ein Stockwerk hinunter“.
  - Other terms: Ostkorridor / Südkorridor / Westkorridor, Tribuna, Niobe-Saal, Vasari-Korridor, Verone, Granducal-, Buontalenti-, Lanzi- and Magliabechi-Treppe.
  - "Warden" is „Aufsichtspersonal“. The one exception was in a bridge, and I fixed it (below).

## Changes (track: before → after, why)
- **003 @where:** „auf der anderen Seite des Vestibüls als der übrige Rundgang“ → „vom Vestibül aus auf der dem übrigen Rundgang entgegengesetzten Seite“. The old phrase was ungrammatical.
- **004:** „In Longfellows Übersetzung sagt er: „In der Malerei glaubte Cimabue, das Feld zu behaupten, nun hat Giotto den Ruf, sodass der Ruhm des anderen verblasst.““ → „In der Übersetzung von Philalethes sagt er: „Das Feld zu halten glaubte Cimabue als Maler, jetzt nennt alles Giottos Namen, so daß den Ruhm des andern er verdunkelt.““
  - Why: the lead allowed an established public-domain German translation. A German rendering of Longfellow's English, introduced as Longfellow, was odd for German listeners.
  - Verified verbatim three times by WebFetch: Philalethes, Purgatorio, Elfter Gesang, Projekt Gutenberg, https://projekt-gutenberg.org/authors/dante-alighieri/books/goettliche-komoedie/chapter/46
  - The verse reads: "Das Feld zu halten glaubte Cimabue / Als Maler, jetzt nennt alles Giottos Namen, / So daß den Ruhm des andern er verdunkelt."
  - Only the capitals at the start of each verse line were lowered, for running text. The wording and the old spelling „daß“ are kept.
- **004:** „Sind sie ein Muster oder eine Menschenmenge?“ → „… oder ein Gedränge?“ The old word was the wrong register for angels.
- **006:** „hing es in der Kapelle“ → „hing das Bild in der Kapelle“. The previous sentence is about the contract, so „es“ was ambiguous.
- **007:** „Dante schrieb, Giotto habe nun „den Ruf“, den Ruhm, der einst Cimabue gehörte.“ → „Dante schrieb, jetzt nenne „alles Giottos Namen“. Der Ruhm, der einst Cimabue gehörte, ist nun seiner.“ This keeps the echo of 004: the quoted fragment is verbatim Philalethes, and the meaning matches the English.
- **009:** „Er schrieb die Worte selbst“ → „Er schrieb genau diese Worte“. „selbst“ sounded like "he himself"; the English means "the words themselves".
- **010:** „Doch sein eindrucksvollstes Bild stammt heute von einem Sienesen“ → „Doch das eindrucksvollste Bild, das heute hier hängt, stammt von einem Sienesen“. The old wording sounded like an attribution that holds "today"; the English means the most striking picture on show today.
- **014:** „… besiegt hatte, angeführt vom Herzog von Mailand“ → „… die Sienesen und ihre Verbündeten unter Führung des Herzogs von Mailand besiegt hatte“. The trailing participle could be heard as Florence being led by Milan.
- **020:** „und es begann als Kapellenbild …“ → „und doch war es zuerst das Kapellenbild …“. „es“ did not agree with „Meilenstein“.
- **022:** „5.780“ → „5780“, for TTS safety. "Der Vertrag von Wien" is **kept**, per the lead's correction: the English has "Treaty of Vienna", sourced from the museum. Nothing is added: there is no Kongress and no extra date.
- **031:** „zurück auf diesem Stockwerk“ → „ein Stück zurück auf diesem Stockwerk“, to render "back along this floor" naturally.
- **033 body and @where:** „auf einem Leopardenfell“ → „in einem Leopardenfell“. The English is "in a leopard skin", meaning wearing it.
- **038, 041, 043, 060 @where:** removed the internal production notes (O19, O20, O35 and the "vor Ort prüfen" text). Each is now aligned to the cleaned English.
- **041:** „Sie ist kleiner als erwartet“ → „Die Figur ist kleiner, als man erwartet“. The pronoun had no clear referent.
- **045:** „vorbei an D2, Dosso Dossi und sein Kreis“ → „vorbei an D2 mit Dosso Dossi und seinem Kreis“, a grammar fix.
- **067:** „Nichts anderes heißt Uffizien.“ → „Nichts anderes bedeutet das Wort Uffizi.“ The English is about the word "Uffizi".
- **Bridge 037 H>046:** „Gehen Sie in Gegenrichtung … bei Sperrung fragen Sie die Aufsicht, dann in Saal D4 …“ → „Gehen Sie in die andere Richtung, in den langen Saal C1, und folgen Sie dem Rundgang des Museums bis Saal D1. Falls eine Absperrung Sie aufhält, fragen Sie das Aufsichtspersonal. Dann weiter in Saal D4: …“ This adds the missing "museum's route", unifies "warden", and fixes the run-on sentence.

## For the lead
- **019:** "may have hung in a court of the Florentine Republic" is rendered „in einem Gericht“. If the English means a magistracy or office, the German should be „Amt“. I kept the translator's reading.
- **007 and 004 Dante:** if you prefer to stay with the faithful translation of Longfellow, the backup holds the previous text.
- **001:** the version names „Das Wesentliche“ and „Highlights“ need to match the app's German labels.
- **Points already flagged by the translators, translated as written:** 064 (the Bacchus given for Cosimo's wedding) and 055 ("by reservation").
- **Verdict:** ready.

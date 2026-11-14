# Writer D notes: tracks 003 004 007 008 013 014 015 016 020 031 033 (14 Nov 2026)

Built on PLAN §2 rows, with the FACTS_GAPS "Changes proposed to FACTS rows" table and the lead's two decision sections (on §8, and after FACTS_GAPS) applied over them. Bridges: `v5/bridges/D.txt` holds one line, `008 H>022`. That is the only §3 bridge row on my tracks. 016 needs no bridge: its "Otherwise" goes to 021, which is in E. The bridge's tags [O3, O19] are left out of the spoken line, the same way the [O#] tags are kept out of every track body: the validator rejects any bracket that is not a direction tag.

`python3 v5/lint.py 003 004 007 008 013 014 015 016 020 031 033` prints OK for all eleven.

## For the lead to decide or know (most important first)

1. **The Thames story is cut from 008. The sources conflict on who jumped.**
   - The National, AU-S32 and the only source behind PLAN's line, says "future club president, Joan Laporta, even jumped into the River Thames – as he'd promised".
   - ESPN, in an oral-history piece (https://global.espn.com/football/story/_/id/37474665/...), has a player recalling "[then vice-president] Joan Gaspart jumping in the Thames".
   - Catalan News (30 years on) mentions neither man.
   - With two press sources naming different men, even "the story goes" would be telling a legend about the wrong person. If you want the scene back, you need an official or press page that settles it, most likely Gaspart. "Over a million" at the homecoming also rests on The National alone, so it is not used either.
2. **Lint false positive: the `deport` ban matches "Los Deportes"** (and "Sociedad de Deportes", and "Vida Deportiva" in 031's source).
   - So 004 calls the paper "a Barcelona sports weekly" in speech and never names it, and its Q1 quote stops before "Sociedad de Deportes".
   - If you want the paper named, make the regex `\bdeport(ed|ation|ing)?\b` or give 004 an exception.
3. **020: PLAN's "some Madrid supporters question that the visit happened at all" is not on the page.**
   - The Guardian piece (via inkl) says "though some Madridistas question the packed piece". That is about the official carrying a loaded gun, not about whether he visited.
   - 020 therefore balances the story differently:
     - Barau's own words, from the same Goal article as his quote: "That's a story that nobody has ever been able to prove", paraphrased.
     - Real Madrid's own history page, which says nothing of whistles or a visit and calls the second leg a comeback.
     - The optional sentence on Franco's honours and the 2019 vote. It is self-contained and can be cut.
4. **014: the fourteenth minute now has an official source.** The club's 2016 year review says that when the scoreboard "marked the 14th minute of the game", the crowd "burst into a spontaneous round of applause" for "Cruyff's famous number", and that the mosaic read "Gràcies Johan".
   - 014 says "for what the club calls his famous number", in the club's own words. It never says "his old number".
   - The minute's silence before kick-off rests on FourFourTwo alone. The club's 2016 review mentions a minute's silence only for Manel Vich, so it is not scripted.
5. **013 quotes Cruyff** ("I was surprised that instead of congratulating us on the win, people were saying thank you."). FACTS §21 said no Cruyff quotes except Q5, but GAPS G38 adds this one to §21 and its table overrides FACTS. I re-checked it on the club's page. Cut it if you'd rather keep Cruyff's own words to the statue phrase only.
6. **007 includes the 2–0 over Real Madrid (10 May 2026).** The "second source" PLAN asked for is the club's own match page (AU-S66). It says the win "otorgó la 29ª Liga" and calls it "la primera conseguida matemáticamente contra el eterno rival". With AU-S67 (SEC) that makes two sources. It is a separate DATED sentence and can be cut. The look line "See if you can spot the pair" assumes O16 finds the 2025–26 trophies on show. Cut it if O16 doesn't.
7. **Lengths: written in the upper half of the range, as the brief asks, so most tracks are over PLAN's aims.**

   | Track | Aim | Words | Difference |
   |---|---|---|---|
   | 003 | 190 | 245 | +55 |
   | 004 | 260 | 333 | +73 |
   | 007 | 180 | 214 | +34 |
   | 008 | 290 | 270 | −20 |
   | 013 | 260 | 319 | +59 |
   | 014 | 290 | 298 | +8 |
   | 015 | 270 | 320 | +50 |
   | 016 | 270 | 352 | +82 |
   | 020 | 280 | 306 | +26 |
   | 031 | 250 | 330 | +80 |
   | 033 | 260 | 293 | +33 |

   - In all, about +480 words, or about 3.8 min of Full listening.
   - E plays four of these tracks (008, 014, 015, 016): about +120 words, or about 1 min. H plays only 008, which is 20 words under its aim.
   - Places to trim if O21 runs long:
     - 016: the 1933 bulletin sentence's lead-in and the 1970s campaign sentence.
     - 031: the statue sentence and "You've probably heard of two of them".
     - 004: Wild's flat and the matches he played.
     - 013: Cruyff's "thank you" quote.

## Pages read (all WebFetch, one at a time, 14 Nov 2026)

| Page | Grade | What it confirmed | Track |
|---|---|---|---|
| fcbarcelona.com/en/card/645523/walter-wild-1899-1901 | OFF | "first ever president"; "his colleagues unanimously named him president"; flat in Carrer Princesa for board meetings; ten matches incl. the very first; "forced to resign on April 25, 1901 because he had to leave for England" | 004 |
| enciclopedia.cat/…/joan-gamper | SEC (GEC) | "22 de novembre de 1877"; "No volgué ser-ne el primer president, se centrà a jugar"; "el 1899 passà a residir a Barcelona" (so "the late 1890s", per G20) | 004 |
| fcbarcelona.com/en/club/news/4153324/125-years-since-the-ad-in-los-deportes | OFF | Q1 text; "former Swiss champion"; "to organise some games in Barcelona"; "Tuesday or Friday evenings between 9 and 11"; "Miscellaneous" section at the back; ad "published by himself and his compatriot Walter Wild" | 004 |
| fcbarcelona.es/es/noticias/643913/1988-96-la-era-del-dream-team | OFF | "Instantes antes de saltar al césped Johan Cruyff dio las últimas instrucciones a sus hombres: "Salid y disfrutad"."; Koeman "minuto 111" (conflicts with 112: "extra time" kept); Bern 1989, 2–0 v Sampdoria | 008 |
| fcbarcelona.es/es/ficha/2982808/la-primera-champions-del-barca-wembley-1992 | OFF | 20 May 1992; Sampdoria; Koeman in extra time beat "un esforzado Pagliuca"; "ya a la prórroga, el capitán Alexanko"; the 1961 and 1986 losses ("a la tanda de penaltis") | 008 |
| fcbarcelona.com/en/news/4198094/three-games-against-benfica… | OFF | 3–2; "Unbelievably they hit the woodwork four times."; "The goalposts were square at the time" | 008 |
| thenationalnews.com/…/on-this-day-may-20-1992… | SEC | Laporta and the Thames; "over a million" (not used: see item 1) | 008 |
| global.espn.com/football/story/_/id/37474665/… | SEC | Gaspart and the Thames; "Go out there and enjoy it" (not used) | 008 |
| catalannews.com/sports/item/wembley-92-barca-s-first-european-cup-30-years-on | SEC | says nothing on the Thames | 008 |
| fcbarcelona.com/en/news/1629219/johan-cruyff-an-incomparable-legend/ | OFF | "put into motion the best era in the history of the club"; pedestal: "Go out and have fun" (not used: see 008 notes); left in 1996 after disagreements with Núñez; died 24 March 2016 of lung cancer; Estadi Johan Cruyff opened "the following day"; coach's honours | 014 |
| fcbarcelona.com/club/news/2016-2017/2016-a-year-of-irreparable-losses | OFF | Clásico 2 April; "Gràcies Johan" mosaic; 14th-minute applause for "Cruyff's famous number" | 014 |
| fcbarcelona.com/en/news/4474399/a-decade-without-johan-cruyff | OFF | "Cruyff gave birth to the idea that today defines Barça"; "His confidence in the blaugrana youth system and in a common philosophy"; died in Barcelona | 014 |
| fcbarcelona.com/en/club/news/3619586/50-years-on-how-johan-cruyff-came-to-fc-barcelona | OFF | 13 August 1973; the Dutch federation's 1–31 July window; four friendlies | 013 |
| fcbarcelona.com/en/news/3750661/50-years-since-cruyffs-competitive-debut-for-barca | OFF | 28 Oct 1973 v Granada, 4–0, two goals; "second from bottom"; "the first of 26 games unbeaten"; the 1973/74 Liga | 013 |
| fcbarcelona.com/en/news/3897179/50-years-since-the-5-0-at-the-santiago-bernabeu | OFF | 17 Feb 1974; Asensi 31', Cruyff 39'; both quotes, verbatim | 013 |
| global.espn.com/football/story/_/id/37443918/jordi-cruyff-father-… | SEC | Jordi's quote, verbatim; "Jorge"; the Dutch-passport reply. Michels chose the date (ESPN) and Montal asked (Ara), so who decided is not said | 013 |
| fcbarcelona.es/club/instalaciones/ficha/historia-de-la-masia | OFF | 1702; "taller para la confección de la maqueta"; HQ; 20 Oct 1979; 12 + 48; "dejó de ser centro formador en 2011"; Oriol Tort 20 Oct 2011, 83; Xavi, Iniesta, Messi | 015 |
| fcbarcelona.com/en/news/3983230/… (Masia de Can Planes) | OFF | "visible to them through their bedroom windows"; land of 1950; "a work area for architects and builders"; social HQ; "return to its original state" | 015 |
| fcbarcelona.com/en/news/813768/andres-iniesta-… | OFF | "one of the worst days I have experienced"; age 12 | 015 |
| fcbarcelona.com/en/news/1096349/fifth-anniversary-of-world-cup-in-south-africa | OFF | "Seven of the eight were starters in the Final." No academy count, so "six from La Masia" is not said | 015 |
| fcbarcelona.es/es/noticias/723765/50-anos-del-mas-que-un-club | OFF | full ES wording of de Carreras (G29), in two pieces; 1933 in ES | 016 |
| fcbarcelona.com/en/news/723765/50-years-of-more-than-a-club | OFF | the official EN wording of de Carreras's first two sentences; 1933 "…much more than a mere football club"; the 1973 Javier Coma campaign. This page does not say which language he spoke: "in Catalan" rests on FACTS 3.18 [O20] | 016 |
| fcbarcelona.com/en/club/news/4555323/… (Sunyol tribute) | OFF | Elena Fort, "Institutional Vice-President": "Barça is more than a club because it represents a country, and the figure of Josep Sunyol should always remind us of that." Only the first clause is quoted: Sunyol's home is 019 | 016 |
| arxiu.fcbarcelona.cat/…/escut.html | OFF | FCB → CFB; two of four bars removed; bars back for the 50th anniversary in 1949; letters back late 1974; the crest's elements | 016 |
| realmadrid.com/static/…/1941-1950 | OFF-RM | "En Les Corts, el once azulgrana ganó 3-0."; "En la vuelta, nuestro equipo eliminó a su rival gracias a una extraordinaria remontada."; "El Madrid venció 11-1."; "Aquí nació la eterna rivalidad entre ambos clubes." | 020 |
| goal.com/en/news/they-were-overcome-by-military-pressure… | SEC | 13 June 1943; 3–0; 8–0 at half time; Benito García sent off; Barau: "Barcelona were overcome by military pressure and people close to the Falange"; "That's a story that nobody has ever been able to prove" | 020 |
| inkl.com/news/the-joy-of-six-real-madrid-v-barcelona… (Guardian) | SEC | Ya: "…with the clear intention of attacking the representatives of Spain"; "given free whistles upon entrance to the ground"; "Spain's director of state security visited their dressing room just before kick-off" | 020 |
| fcbarcelona.es/es/noticias/1371858/… (Franco's honours) | OFF | 1951 insignia, 1971 medal, 1974 medal; withdrawn in 2019, 671–2–7 | 020 |
| fcbarcelona.com/en/news/4274716/75-years-since-laszlo-kubala-signed | OFF | 8.30 pm, 15 June 1950, after a friendly at Sarrià v Espanyol; "a political refugee being pursued by the Hungarian federation"; Hungaria; no competitive football until the 1951 cup; brother-in-law Daučík; "the legendary Five Cups era"; statue outside the main stand, 2009 | 031 |
| fcbarcelona.com/en/news/1604494/barca-rewind-seven-goal-kubala… | OFF | 10 Feb 1952, 9–0, seven goals; "matched the Liga record set by Bata of Athletic Club against Barça in 1931, and has never been touched since" (2020 page: DATED); Daučík's quote, verbatim | 031 |
| fcbarcelona.com/club/history/card/1950-1961-kubalas-era | OFF | the five trophies of 1951/52; "The Club needed a bigger stadium." | 031 |
| fcbarcelona.com/en/news/742737/24-september-1957… | OFF | "Kubala did generate unprecedented interest…"; "the plans to build the new ground were already in place some time before he signed in 1950." | 031 |
| fcbarcelona.com/en/news/1138728/30-years-since-maradona-stunned-the-santiago-bernabeu | OFF | 26 June 1983, League Cup; Agustín, Juan José and the post; "The Real Madrid fans stood to applaud Maradona's goal" | 033 |
| fcbarcelona.com/en/news/1615168/the-big-read-maradona… | OFF | 4 June 1982; "the world most expensive footballer"; first-game goal in a 2–1 defeat to Valencia; hepatitis in Dec 1982; both 1983 finals v Real Madrid; the Goikoetxea ankle injury; the 1984 "battle on the field"; three-month ban; Napoli; 38 goals in 58 | 033 |
| fcbarcelona.com/en/news/1899174/15-years-to-the-day-since-a-famous-clasico | OFF | 19 Nov 2005, 3–0; Eto'o 14' "from a pass from debutante Messi"; Ronaldinho 59', 77'; standing ovation from the Madrid fans; Messi's first Clásico | 033 |
| fcbarcelona.com/en/football/first-team/honours | OFF | 29 Ligas, 32 Copas (first 1909-10), 5 Champions Leagues, 16 Super Cups | 007 |
| fcbarcelona.es/…/4501689/… (2–0, 10 May 2026) | OFF | see item 6 | 007 |
| fcbarcelona.com/en/photos/4505514/liga-and-super-cup-on-display-in-museum | OFF | headline only: "Liga and Super Cup on display in Museum", 18 May 2026 | 007 |
| fcbarcelona.es/…/4128584/cuarenta-anos-… (museum at 40) | OFF | "trofeos expuestos (más de 100 de fútbol, 25 de fútbol femenino y 50 de secciones)" | 007 |
| fcbarcelona.com/en/news/2998159/ice-rink-building-… | OFF | "The ice rink was opened in 1971"; its uses; 2,400 m²; "until the new Spotify Camp Nou opens in 2024/25" | 003 |
| fcbarcelona.com/en/news/2300514/the-palau-blaugrana-is-50-years-old | OFF | inaugurated 1971; basketball, handball, roller hockey, futsal; jerseys "retired to the Palau" | 003 |
| fcbarcelona.es/…/3530980/… (Immersive Tour opening) | OFF | the Palau de Gel building; about 2,400 m²; opened to the public 7 June; "hasta … la temporada 2024/25" | 003 |

Two WebSearch calls were used only to find pages: the Thames, and the 14th-minute tribute. No search snippet is scripted.

## Not re-read on a page; used from FACTS/AUDIT at their grade
- 003:
  - The rink closed in 2022 and the new provisional rink opened in 2026 on university land (ROUTE §1.4 SEC ×2). The closure is not given a year in speech.
  - A new arena is planned on the campus (ROUTE §1.4 SEC).
  - The old museum closed on 28 May 2023 and stood under the main stand (F6.16, F16.3 OFF).
- 004: the meeting, the twelve founders and their nationalities, and the city's name (F1.7, F1.8, F1.10); Gamper always used "Joan" (F4.8).
- 013:
  - Jordi was born in Amsterdam by a planned caesarean (AU-S33 Ara, via AUDIT). "Third child" comes from Ara's "third son", per AUDIT 220.
  - Ley 17/1977 of 4 Jan 1977 (AU-S82 BOE, via AUDIT): "in January 1977, when Catalan names could be registered".
  - The first league in fourteen years (F7.3).
- 014:
  - The Cup Winners' Cup (F7.9).
  - The Estadi Johan Cruyff is for the second team, the women and the under-19s (F7.13).
  - He coached Catalonia, 2009–13, spoken as "a few years" (F7.14, OFF [O34]; the page was re-read for other lines, not this one).
  - The statue: decision 11 wording, and G46.
- 016: the 1941 name (F3.10); "delivered in Catalan" (F3.18 / [O20]); the 1973 campaign is spoken as "the early 1970s".
- 033: the 13 June 1982 opener, Belgium 1–0 Argentina (F6.3 SEC RTBF; F6.2 OFF).

## Wording that differs from PLAN, and why
- **003**:
  - The optional "fifty other-sports trophies" clause is not used. 007 is that story's home, and both tracks are Full.
  - The sections are named from G87 (OFF).
  - The rink and the Palau Blaugrana both opened in 1971: that pairing is our linking.
- **004**:
  - The paper is not named (see item 2).
  - "Gamper had turned twenty-two the week before" is our arithmetic from G19.
  - Wild's first presidency is told as the presidents card tells it, attributed. Gamper's refusal is attributed to "a Catalan encyclopedia".
  - No sentence holds both "Gamper" and "first president", so the lint ban is respected.
- **007**: the five European Cups are given as "Europe's biggest club prize five times", with no years (their stories belong to 008–010).
- **008**:
  - "Salid y disfrutad" is said once, in Spanish, attributed to the club's history, then "Go out and enjoy it", as revised decision 4 allows.
  - Two additions:
    - the woodwork in Bern, 1961 (G62, re-read);
    - Sampdoria beaten in Bern in 1989 (G45; the city's name comes from GAPS, and the 2–0 and Sampdoria were re-read on [GO13]).
  - No statue clause: the Cruyff statue's home is 014.
  - No minute for Koeman: "with penalties not far off".
  - "Who lifted the cup" is not on the page, so Alexanko is said only to have "come on for extra time".
  - The Thames is cut (see item 1).
- **013**:
  - It opens on Jordi's own quote rather than "Ara reports".
  - Who chose the date is never said (the lead's decision).
  - The volley against Atlético and Reina's line are left out for length, as is "It's done!": the brief bans exclamation marks.
  - "Unbeaten for twenty-six games" is used, because the club's own page gives the count (the lead's condition).
- **014**: PLAN's "the club's own historians trace today's football to him" is replaced by the club's own words from March 2026 (G47), quoted.
- **015**:
  - "Six from the academy" is not said, as PLAN ruled.
  - The Iniesta line is quoted, re-checked.
  - "The residence moved out in 2011": the Spanish page gives only the year; the Oriol Tort centre opened on 20 Oct 2011.
- **016**:
  - The "other reading" sentence is dropped. G gave no sourced line, so the vice-president's words stand as "her words, and her reading of it".
  - Vázquez Montalbán (optional) is not used.
  - The 1949 year is folded into "the club's fiftieth birthday" to cut the number of dates.
- **020**: as item 3. Di Stéfano is out (the lead's decision). The honours to Franco are given without their years, to hold the date count.
- **031**:
  - The 1951-cup date is dropped ("At first he couldn't play competitive matches at all").
  - The record is phrased "equalled the league record, which had been set against Barça", from the page.
  - The statue's sculptor is added (G48).
  - The Kubala line uses lint exception 031.
- **033**:
  - Maradona's 1983 ovation is restored, per revised decision 7, and paired with Ronaldinho's for the payoff.
  - The ovation was in one of the two legs of the League Cup final. The page gives 26 June 1983 but not which leg, so the track says "One leg of that league cup final was played at the Bernabéu".
  - "Debut" is avoided ("his first official game"), to stay clear of the debut lint rule.

## Quotes re-checked, and translations
All of these were checked on the live page today.
- Q1 (004): "Our friend and colleague Mr Kans Kamper, of the foot-vall section". Quoted up to there; the rest of the ad is paraphrased.
- G43 (008), ES: "Salid y disfrutad" → "Go out and enjoy it" (the club's own English phrase on [GO15] is "go out there and enjoy it").
- G38 and G39 (013): EN, as given by the club, verbatim.
- G40 (013): Jordi, in EN, verbatim, with "vs." spoken as "versus". G41 is paraphrased.
- F7.8 (014): "the best era in the history of the club", verbatim. G47: "Cruyff gave birth to the idea that today defines Barça.", verbatim.
- AU-S76 (015): "was one of the worst days I have experienced", verbatim (EN as given by the club).
- Q3 / G29 (016):
  - The club's official English is quoted for the first two sentences.
  - The ES continuation, "más que todas las cosas, es un espíritu que llevamos muy arraigado dentro", is paraphrased without quotation marks as "More than anything, he went on, it was a spirit carried deep inside".
  - The Catalan original is still unread (G28).
- Q4 (016): the English page reads "seeks to means much more than a mere football club" (a typo). Only the fragment "much more than a mere football club" is quoted. The ES reads "quiere decir algo más que un simple club de fútbol".
- Q8 (016): "Barça is more than a club because it represents a country", verbatim, with the rest of her sentence left out.
- Q10 (020): "with the clear intention of attacking the representatives of Spain", verbatim. Q9: "were overcome by military pressure", verbatim; the rest of Barau's sentence ("and people close to the Falange") is left out.
- G1 (020), ES:
  - "una extraordinaria remontada" → "an extraordinary comeback", paraphrased in speech.
  - "Aquí nació la eterna rivalidad entre ambos clubes." → "This is where the eternal rivalry between the two clubs was born." This is our translation, spoken in quotation marks and introduced "In Spanish".
- 004, CA: "No volgué ser-ne el primer president, se centrà a jugar" → spoken as "he didn't want to be president. He wanted to play."
- Q6 (031): "Kubala scored goals today, but he didn't have a great game.", verbatim. F5.2: "being pursued by the Hungarian federation", verbatim.
- G63 (033): paraphrased: "stood up to applaud his goal".

## Pronunciation additions (§7)
- Copa Eva Duarte: KOH-pah EH-bah DWAR-teh.
- Copa Martini Rossi: KOH-pah mar-TEE-nee ROS-see.
- Montserrat Garcia Rius: mun-suh-RAT gur-SEE-uh REE-oos.
- Agustín (keeper): ah-goos-TEEN.
- Juan José: hwan ho-SEH.
- Juan Manuel Asensi: hwan mah-NWEL ah-SEN-see.
- Granada: grah-NAH-dah.
- Carrer Princesa: kuh-RAY prin-SEH-zuh.
- Elena Fort: uh-LEH-nuh FORT (already listed).
- Gràcies Johan: GRAH-see-uss YOH-hahn (already listed).

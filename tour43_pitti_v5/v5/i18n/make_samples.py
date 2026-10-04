#!/usr/bin/env python3
"""Writes the ES / FR / DE voice-sample translations of V5.1 tracks 015 and 053 (5 Oct 2026).
Translated from the fact-checked English perf files; same paragraphs and direction tags; formal address
(usted / vous / Sie). Facts are unchanged from the English. Output: v5/i18n/<lang>/tracks/NNN.perf.txt"""
import os, re
HERE = os.path.dirname(os.path.abspath(__file__)); EN = os.path.join(HERE, "..", "tracks")

T = {
"es": {
"015": ("Rafael — La Madonna della Seggiola",
"En la Sala de Saturno, delante del cuadro redondo de la Virgen abrazando a su hijo, con el pequeño san Juan en el borde derecho.",
"""[curious] Hay una historia preciosa sobre este cuadro. Rafael pasea por Roma cuando ve, en el umbral de una puerta, a una campesina sentada en un taburete bajo con su hijo en brazos. Y pinta exactamente lo que ve. [pause] Es una leyenda encantadora, y casi con toda seguridad inventada. La silla la delata.

De la silla solo se ve una parte, un montante decorado con pomos redondos. Y no es el taburete de una campesina. Es una silla de cámara, de las reservadas a los altos dignatarios de la corte papal, y esos pomos quizá aludan a las bolas del escudo de los Médici. Muchos creen que el cuadro se hizo para el papa Médici, León Décimo, cuyo retrato cuelga en esta misma sala. Rafael lo pintó hacia 1512, en sus años romanos.

Así que probablemente no es una mujer en un umbral. [warmly] Pero fíjese en cómo Rafael consigue que lo parezca. María levanta una rodilla para sostener a su hijo y lo estrecha contra el pecho. Su mejilla descansa junto a la sien del niño, y sin embargo sus ojos se vuelven hacia usted. A la derecha, el pequeño san Juan junta las manos en oración y los contempla. Sus brazos se entrelazan, y los tres cuerpos siguen el borde redondo con una soltura perfecta.

Ahora, el color. Un turbante blanco tejido con hilo de oro, y un pañuelo de verdes y rojos. Una manga roja junto a la túnica amarilla del Niño, y el azul ultramar intenso del vestido. Y en las miradas, un poco de melancolía, como si ella ya supiera lo que le espera a este niño.

En 1589 ya colgaba en la Tribuna de los Uffizi. Más tarde, el Gran Príncipe Fernando lo trajo al Pitti y lo tuvo en su dormitorio. Los ejércitos de Napoleón se lo llevaron a París, y volvió tras su caída. Llegó a ser uno de los cuadros más copiados de Rafael.

[quietly] La leyenda acierta en una cosa. Fuera quien fuera, no parece una reina de los cielos. Parece una madre que no quiere soltar a su hijo.

A continuación, busque el retrato de una joven con amplias mangas rojas y una mano apoyada en el vientre. Es La Gravida, de Rafael."""),
"053": ("El Anfiteatro",
"En el borde del anfiteatro, a ser posible en el extremo del palacio, con el palacio a su espalda y el obelisco delante. Las gradas de piedra están valladas por obras de restauración; contémplelo desde los senderos que lo rodean.",
"""[lightly] Empecemos con una idea curiosa. El palacio que tiene a su espalda salió de este hoyo.

Esta hondonada en la ladera era una cantera, y su piedra acabó en los muros del Palacio Pitti. Cuando Leonor de Toledo empezó estos jardines hacia 1550, su arquitecto, Tribolo, tuvo una idea mejor que rellenarla. La convirtió en un teatro de verdor, excavado en la propia colina. Casi un siglo después, Giulio Parigi la transformó en el anfiteatro de piedra que ve ahora, y lo terminó en 1634.

[warmly] Y entonces los Médici celebraron aquí sus fiestas. Imagine las gradas repletas de espectadores, la familia del gran duque presidiendo con toda solemnidad y, abajo, en la arena, el tipo de espectáculo que Florencia hacía mejor que nadie. Música, danzas, vestuario, decorados pintados y maquinaria escénica rodando sobre la hierba. Para los Médici, un espectáculo así era una declaración. Le decía a cada embajador de visita lo rico, y lo civilizado, que era este pequeño Estado.

[quietly] Las fiestas no duraron para siempre. La última gran representación fue en 1739, para recibir a un nuevo soberano, Francisco Esteban de Lorena, después de que se extinguiera la dinastía de los Médici. Poco después, las gradas se cubrieron de plantas, y la música se apagó.

[pause] Ahora, la pieza central. El obelisco del centro es, con mucha diferencia, lo más antiguo de este jardín. Se talló en Egipto para el faraón Ramsés Segundo, hace más de tres mil años. El emperador Domiciano lo llevó a Roma para un templo de Isis. Un cardenal Médici lo compró para su villa en Roma, y en 1790 llegó por fin aquí. La gran pila de granito rojo que tiene a sus pies vino de la misma villa, y se le unió cincuenta años más tarde.

[warmly] Así que en una sola mirada tiene usted un obelisco egipcio, una villa de los Médici, una cantera renacentista y un teatro barroco. El sendero que sube por la colina, más allá del obelisco, lleva a la Fuente de Neptuno."""),
},
"fr": {
"015": ("Raphaël — La Madone à la chaise",
"Dans la salle de Saturne, devant le tableau rond de la Vierge serrant son enfant contre elle, avec le petit saint Jean sur le bord droit.",
"""[curious] Une bien jolie histoire circule à propos de ce tableau. Raphaël se promène dans Rome lorsqu'il aperçoit, sur le seuil d'une porte, une paysanne assise sur un tabouret bas, son enfant dans les bras. Et il peint exactement ce qu'il a vu. [pause] C'est une légende charmante, et presque certainement inventée. La chaise la trahit.

On n'aperçoit qu'une partie de la chaise, un montant orné de pommeaux ronds. Et ce n'est pas le tabouret d'une paysanne. C'est un siège d'apparat, de ceux qu'on réservait aux hauts dignitaires de la cour pontificale, et ces pommeaux évoquent peut-être les boules des armoiries des Médicis. Beaucoup pensent que le tableau a été fait pour le pape Médicis, Léon Dix, dont le portrait est accroché dans cette même salle. Raphaël l'a peint vers 1512, pendant ses années romaines.

Ce n'est donc probablement pas une femme sur le pas d'une porte. [warmly] Mais regardez comment Raphaël nous le fait croire. Marie relève un genou pour soutenir son fils et le serre contre sa poitrine. Sa joue repose contre la tempe de l'enfant, et pourtant ses yeux se tournent vers vous. À droite, le petit saint Jean joint les mains en prière et les contemple. Leurs bras s'enlacent, et les trois corps épousent le bord du cercle avec une aisance parfaite.

Maintenant, la couleur. Un turban blanc tissé de fil d'or, et une écharpe de verts et de rouges. Une manche rouge contre la tunique jaune de l'Enfant, et le bleu outremer profond de sa robe. Et dans les regards, un peu de mélancolie, comme si elle savait déjà ce qui attend cet enfant.

En 1589, il était déjà accroché dans la Tribune des Offices. Plus tard, le Grand Prince Ferdinand l'a fait venir au palais Pitti et l'a gardé dans sa chambre. Les armées de Napoléon l'ont emporté à Paris, et il est revenu après sa chute. Il est devenu l'un des tableaux de Raphaël les plus copiés.

[quietly] La légende a raison sur un point. Qui qu'elle soit, elle ne ressemble pas à une reine des cieux. Elle ressemble à une mère qui serre son enfant.

Cherchez ensuite le portrait d'une jeune femme aux larges manches rouges, une main posée sur le ventre. C'est La Gravida, de Raphaël."""),
"053": ("L'Amphithéâtre",
"Au bord de l'amphithéâtre, de préférence du côté du palais, le palais derrière vous et l'obélisque devant vous. Les gradins de pierre sont fermés pour restauration ; regardez-le depuis les allées qui en font le tour.",
"""[lightly] Commençons par une idée étonnante. Le palais derrière vous est sorti de ce trou.

Ce creux dans la colline était une carrière, et sa pierre a servi à bâtir les murs du palais Pitti. Quand Éléonore de Tolède a commencé ces jardins vers 1550, son architecte, Tribolo, a eu une meilleure idée que de le combler. Il en a fait un théâtre de verdure, taillé dans la colline elle-même. Près d'un siècle plus tard, Giulio Parigi l'a transformé en l'amphithéâtre de pierre que vous voyez aujourd'hui, achevé en 1634.

[warmly] Et puis les Médicis y ont donné des fêtes. Imaginez les gradins remplis de spectateurs, la famille grand-ducale qui préside en majesté et, dans l'arène en contrebas, le genre de spectacle que Florence savait faire mieux que personne. De la musique, des danses, des costumes, des décors peints et des machines de théâtre roulant sur l'herbe. Pour les Médicis, un tel spectacle était une déclaration. Il montrait à chaque ambassadeur de passage à quel point ce petit État était riche, et raffiné.

[quietly] Les fêtes n'ont pas duré éternellement. La dernière grande représentation a eu lieu en 1739, pour accueillir un nouveau souverain, François-Étienne de Lorraine, après l'extinction de la lignée des Médicis. Peu après, les gradins ont été recouverts de végétation, et la musique s'est tue.

[pause] Passons maintenant au centre. L'obélisque est, de très loin, la chose la plus ancienne de ce jardin. Il a été taillé en Égypte pour le pharaon Ramsès Deux, il y a plus de trois mille ans. L'empereur Domitien l'a fait venir à Rome pour un temple d'Isis. Un cardinal Médicis l'a acheté pour sa villa romaine, et en 1790, il est enfin arrivé ici. La grande vasque de granit rouge, à ses pieds, provient de la même villa, et l'a rejoint cinquante ans plus tard.

[warmly] Ainsi, d'un seul regard, vous avez un obélisque égyptien, une villa des Médicis, une carrière de la Renaissance et un théâtre baroque. Le sentier qui monte la colline au-delà de l'obélisque mène à la fontaine de Neptune."""),
},
"de": {
"015": ("Raffael — Madonna della Seggiola",
"Im Saturnsaal, vor dem runden Bild der Jungfrau, die ihr Kind umarmt, mit dem kleinen Johannes am rechten Rand.",
"""[curious] Über dieses Bild erzählt man sich eine schöne Geschichte. Raffael geht durch Rom und sieht in einem Hauseingang eine Bäuerin, die auf einem niedrigen Schemel sitzt, ihr Kind im Arm. Und er malt genau das, was er gesehen hat. [pause] Eine reizende Legende, und mit ziemlicher Sicherheit erfunden. Der Stuhl verrät sie.

Vom Stuhl sieht man nur ein Stück, einen Pfosten mit runden Knäufen. Und das ist kein Schemel einer Bäuerin. Es ist ein Zeremonienstuhl, wie er hohen Würdenträgern am päpstlichen Hof vorbehalten war, und die Knäufe spielen vielleicht auf die Kugeln im Wappen der Medici an. Viele vermuten, dass das Bild für den Medici-Papst Leo den Zehnten entstand, dessen Bildnis hier im selben Saal hängt. Raffael malte es um 1512, in seinen römischen Jahren.

Sie ist also wohl keine Frau aus einem Hauseingang. [warmly] Aber sehen Sie, wie Raffael sie trotzdem so wirken lässt. Maria hebt ein Knie, um ihren Sohn zu halten, und drückt ihn an ihre Brust. Ihre Wange ruht an seiner Schläfe, und doch blickt sie zu Ihnen heraus. Rechts faltet der kleine Johannes die Hände zum Gebet und schaut zu den beiden hin. Die Arme greifen ineinander, und die drei Körper folgen dem runden Rand mit vollkommener Leichtigkeit.

Nun die Farben. Ein weißer Turban, mit Goldfäden durchwirkt, und ein Tuch in Grün und Rot. Ein roter Ärmel neben dem gelben Hemd des Kindes, und das tiefe Ultramarin ihres Kleides. Und in den Blicken ein wenig Wehmut, als wüsste sie schon, was diesem Kind bevorsteht.

Schon 1589 hing es in der Tribuna der Uffizien. Später brachte Großprinz Ferdinando es in den Palazzo Pitti und behielt es in seinem Schlafzimmer. Napoleons Armeen schafften es nach Paris, und nach seinem Sturz kehrte es zurück. Es wurde zu einem der meistkopierten Bilder Raffaels.

[quietly] In einem Punkt hat die Legende recht. Wer sie auch war, sie sieht nicht aus wie eine Himmelskönigin. Sie sieht aus wie eine Mutter, die ihr Kind festhält.

Suchen Sie als Nächstes das Bildnis einer jungen Frau mit weiten roten Ärmeln, eine Hand auf dem Bauch. Das ist Raffaels La Gravida."""),
"053": ("Das Amphitheater",
"Am Rand des Amphitheaters, am besten an der Palastseite, den Palast im Rücken und den Obelisken vor Ihnen. Die steinernen Ränge sind wegen Restaurierung abgesperrt; betrachten Sie es von den Wegen am Rand.",
"""[lightly] Zum Anfang ein merkwürdiger Gedanke. Der Palast hinter Ihnen ist aus diesem Loch gekommen.

Diese Mulde im Hang war ein Steinbruch, und sein Stein steckt in den Mauern des Palazzo Pitti. Als Eleonora von Toledo um 1550 mit diesen Gärten begann, hatte ihr Architekt Tribolo eine bessere Idee, als ihn aufzufüllen. Er machte daraus ein grünes Theater, direkt aus dem Hügel geschnitten. Fast ein Jahrhundert später baute Giulio Parigi es zu dem steinernen Amphitheater um, das Sie heute sehen, und vollendete es 1634.

[warmly] Und dann feierten die Medici hier ihre Feste. Stellen Sie sich die Ränge voller Zuschauer vor, die großherzogliche Familie in vollem Staat, und unten in der Arena die Art von Spektakel, die Florenz besser beherrschte als jede andere Stadt. Musik, Tanz, Kostüme, bemalte Bühnenmaschinen, die über das Gras rollten. Für die Medici war so eine Aufführung eine Botschaft. Sie zeigte jedem Gesandten, wie reich und wie kultiviert dieser kleine Staat war.

[quietly] Die Feste dauerten nicht ewig. Die letzte große Aufführung fand 1739 statt, zur Begrüßung eines neuen Herrschers, Franz Stephan von Lothringen, nachdem das Haus Medici ausgestorben war. Bald darauf wurden die Ränge bepflanzt, und die Musik verstummte.

[pause] Nun zum Mittelpunkt. Der Obelisk in der Mitte ist mit großem Abstand das Älteste in diesem Garten. Er wurde in Ägypten für den Pharao Ramses den Zweiten gehauen, vor mehr als dreitausend Jahren. Kaiser Domitian brachte ihn für einen Isis-Tempel nach Rom. Ein Medici-Kardinal kaufte ihn für seine Villa in Rom, und 1790 kam er schließlich hierher. Das große Becken aus rotem Granit zu seinen Füßen stammt aus derselben Villa und kam fünfzig Jahre später dazu.

[warmly] In einem einzigen Blick haben Sie also einen ägyptischen Obelisken, eine Medici-Villa, einen Steinbruch der Renaissance und ein barockes Theater. Der Weg, der hinter dem Obelisken den Hügel hinaufführt, bringt Sie zum Neptunbrunnen."""),
},
}


# Spanish v2 (5 Oct, user): adapted for LISTENING, not translated line by line: ~300 words, one idea per sentence,
# extra pauses, neutral vocabulary for Spain and Latin America, formal usted. Same facts, same speed.
ES_ADAPTED = {
"015": """[curious] Sobre este cuadro se cuenta una historia preciosa. Rafael camina por Roma. En una puerta ve a una campesina, sentada en un asiento bajo, con su hijo en brazos. Y la pinta tal como la vio. [pause] Es una leyenda encantadora. Y casi seguro, inventada. [pause] La silla la delata.

Fíjese en la silla. Apenas se ve: un poste con pomos redondos. No es el asiento de una campesina. Es una silla de ceremonia, reservada a los altos cargos de la corte del papa. Y esos pomos quizá recuerden las bolas del escudo de los Médici. [pause] Muchos creen que el cuadro se hizo para el papa Médici, León Décimo. Su retrato está en esta misma sala. Rafael lo pintó hacia 1512, en sus años en Roma.

[warmly] Pero mire cómo Rafael logra que parezca real. María levanta una rodilla y aprieta a su hijo contra el pecho. Su mejilla toca la sien del niño. Y, sin embargo, sus ojos se vuelven hacia usted. [pause] A la derecha, el pequeño san Juan junta las manos y los contempla. Los brazos se entrelazan. Y los tres cuerpos siguen el borde del círculo con total naturalidad.

Ahora, el color. Un turbante blanco con hilos de oro. Un pañuelo verde y rojo. Una manga roja junto a la túnica amarilla del Niño. Y el azul intenso del vestido. [pause] En las miradas hay un poco de melancolía, como si ella ya supiera lo que le espera a este niño.

En 1589 ya estaba en la Tribuna de los Uffizi. Después, el Gran Príncipe Fernando lo trajo al Pitti, a su dormitorio. Los ejércitos de Napoleón se lo llevaron a París, y volvió tras su caída. Hoy es uno de los cuadros más copiados de Rafael.

[quietly] La leyenda acierta en una cosa. [pause] Fuera quien fuera, no parece una reina del cielo. Parece una madre que abraza a su hijo.

Ahora busque el retrato de una joven con anchas mangas rojas y una mano sobre el vientre. Es La Gravida, de Rafael.""",
"053": """[lightly] Empecemos con una idea curiosa. [pause] El palacio que tiene a su espalda salió de este hueco.

Esta hondonada era una cantera. Su piedra levantó los muros del Palacio Pitti. Hacia 1550, Leonor de Toledo empezó estos jardines. Su arquitecto, Tribolo, no quiso rellenar el hueco. Lo convirtió en un teatro verde, excavado en la colina. [pause] Casi un siglo después, Giulio Parigi lo transformó en el anfiteatro de piedra que ve ahora. Lo terminó en 1634.

[warmly] Y aquí los Médici hacían sus fiestas. Imagine las gradas llenas de gente, la familia del gran duque en su sitio de honor, y abajo, el tipo de espectáculo que Florencia hacía como nadie. Música, danza, vestuario, decorados pintados que se movían sobre la hierba. [pause] Para los Médici, una fiesta así era un mensaje. Le decía a cada embajador lo rico, y lo culto, que era este pequeño Estado.

[quietly] Las fiestas no duraron para siempre. La última gran función fue en 1739, para recibir a un nuevo soberano, Francisco Esteban de Lorena. Los Médici ya se habían extinguido. Poco después, las gradas se cubrieron de plantas. [pause] Y la música se apagó.

[pause] Ahora, el centro. El obelisco es, de lejos, lo más antiguo de este jardín. Se talló en Egipto para el faraón Ramsés Segundo, hace más de tres mil años. El emperador Domiciano lo llevó a Roma, para un templo de Isis. Un cardenal Médici lo compró para su villa en Roma. Y en 1790 llegó por fin aquí. [pause] La gran pila de granito rojo vino de la misma villa, cincuenta años después.

[warmly] En una sola mirada tiene usted un obelisco egipcio, una villa de los Médici, una cantera del Renacimiento y un teatro barroco. El sendero que sube por la colina, detrás del obelisco, lleva a la Fuente de Neptuno.""",
}
for n, body in ES_ADAPTED.items():
    title, where, _ = T["es"][n]; T["es"][n] = (title, where, body)

def tags(body): return [t for t in re.findall(r"\[([^\]]+)\]", body) if "pause" not in t]   # delivery tags must match; extra pauses allowed
def pauses(body): return len(re.findall(r"\[(?:long )?pause\]", body))
for lang, tracks in T.items():
    os.makedirs(os.path.join(HERE, lang, "tracks"), exist_ok=True)
    for n, (title, where, body) in tracks.items():
        en = open(os.path.join(EN, f"{n}.perf.txt"), encoding="utf-8").read()
        head, _, en_body = en.partition("\n---\n")
        assert tags(body) == tags(en_body), (lang, n, "delivery tags must match the English")
        assert pauses(body) >= pauses(en_body), (lang, n, "no fewer pauses than the English")
        assert body.count("\n\n") == en_body.strip().count("\n\n"), (lang, n, "paragraphs must match")
        head = re.sub(r"^@title: .*$", "@title: " + title, head, flags=re.M)
        head = re.sub(r"^@where: .*$", "@where: " + where, head, flags=re.M)
        head = re.sub(r"^@id: (\d+)", rf"@id: \1 · {lang.upper()} voice sample", head, flags=re.M)
        head += f"\n@lang: {lang}\n@translation: from the fact-checked English V5.1 {n} (5 Oct 2026); facts unchanged; formal address" + ("; v2 adapted for listening (short sentences, extra pauses, neutral Spanish)" if lang == "es" else "")
        open(os.path.join(HERE, lang, "tracks", f"{n}.perf.txt"), "w", encoding="utf-8").write(head + "\n---\n" + body + "\n")
        print(lang, n, len(body.split()), "words")

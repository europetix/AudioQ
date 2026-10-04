MUSÉE DE L'ORANGERIE — GUÍA DE AUDIO V4 EN ESPAÑOL
====================================================

Qué contiene este paquete
-------------------------
  Orangerie_V4_Full_Tour.pdf
    El PDF acompañante en inglés — portada, índice, ficha "Stop & Look"
    para cada pista, y el guion palabra por palabra. Útil como referencia
    visual incluso si escucha en español; la disposición de las salas
    y los datos de cada obra son los mismos.

  GENERATE_AUDIO_ES.command
    Haga doble clic en este archivo para generar las 30 pistas MP3
    en el Escritorio de su Mac. La primera ejecución instalará edge-tts
    (motor de TTS gratuito de Microsoft). Es seguro re-ejecutar — los
    archivos ya generados se omiten.

  scripts/
    Los 30 archivos de guion con nombres ASCII seguros que guían la
    generación de audio. Cada archivo es una pista de narración palabra
    por palabra.

  plan.json
    Manifiesto de las 30 pistas con títulos, registro, duración y
    recuento de palabras. No es necesario para usar el paquete; sirve
    como referencia.


Cómo usarlo
-----------
  1. Abra esta carpeta en Finder.
  2. Haga doble clic en GENERATE_AUDIO_ES.command
     (Si macOS avisa de un desarrollador no identificado:
      botón derecho → Abrir → Abrir. Solo tendrá que hacerlo una vez.)
  3. Espere mientras se instala edge-tts (solo la primera vez — unos
     30 segundos) y se generan 30 archivos MP3. Tiempo total: entre
     10 y 20 minutos, según su conexión.
  4. Los MP3 aparecerán en ~/Desktop/Orangerie_Audio_ES/
  5. El script le ofrecerá abrir esa carpeta automáticamente.


Configuración de voz
--------------------
  Voz:        es-ES-AlvaroNeural (TTS Microsoft Azure, castellano)
  Velocidad:  -8% (ligeramente ralentizada para mayor calidez y claridad)
  Total:      aproximadamente 1 hora 45 minutos de audio en 30 pistas.


Requisitos
----------
  - macOS 10.15 o más reciente
  - Python 3.9+ (preinstalado en macOS 12+)
  - Conexión a internet (edge-tts consulta la API de Microsoft)


Solución de problemas
---------------------
  "command not found: edge-tts"
    El lanzador de este paquete evita ese error llamando
    `python -m edge_tts` directamente. Si aun así lo ve, ejecute:
        python3 -m pip install --user --upgrade edge-tts
    en Terminal, y vuelva a ejecutar el lanzador.

  "permission denied"
    Abra Terminal, cd a esta carpeta, y ejecute:
        chmod +x GENERATE_AUDIO_ES.command
    Luego vuelva a hacer doble clic en el lanzador.

  Una pista falla
    El lanzador omite los MP3 ya generados. Solo vuélvalo a ejecutar
    y continuará desde donde se quedó.


Sobre esta guía
---------------
  Treinta pistas. Aproximadamente una hora y cuarenta y cinco minutos.
  Diseñada para acompañarle a lo largo del Musée de l'Orangerie:

    Parte I    — Llegada y el edificio (3 pistas)
    Parte II   — Los Nenúfares, primera vuelta (8 pistas)
    Parte III  — Monet, el hombre detrás del regalo (1 pista)
    Parte IV   — La colección Walter-Guillaume (13 pistas)
    Parte V    — Regreso a los Nenúfares (3 pistas)
    Parte VI   — Cierre (2 pistas)

  Recórralas en orden, tómese su tiempo, y no se salte la segunda
  visita a los Nenúfares.


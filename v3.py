import pygame
import sys
import os
import random
import json
import math

# --- SISTEMA LINGUE ---
lingua_selezionata = "it" # "it", "en", o "es"

LINGUE = {
    "it": {
        # Menu e UI
        "start": "INIZIA", "exit": "ESCI", "settings": "IMPOSTAZIONI", "back": "INDIETRO",
        "resume": "RIPRENDI", "restart": "RICOMINCIA", "menu": "MENU INIZIALE",
        "lang_label": "Seleziona Lingua:", "vibe": "Vibrazione Schermo: ",
        "rules_title": "BENVENUTO: REGOLE DEL GIOCO",
        "save_select": "SELEZIONA UN SALVATAGGIO",
        "pause_title": "GIOCO IN PAUSA",
        "slot": "Slot", "slot_empty": "Slot Vuoto",
        "certificates": "ATTESTATI", "back_game": "TORNA AL GIOCO",
        "quit": "ESCI", "volume": "Volume:", "music": "Musica:",
        "on": "ACCESA", "off": "SPENTA", "yes": "SI", "no": "NO",
        "pause": "PAUSA", "click_continue": "Clicca per continuare",
        "click_menu": "Clicca per tornare al menu",
        "delete_confirm": "Sei sicuro di voler eliminare il salvataggio?",
        "your_certificates": "TUOI ATTESTATI",
        "mission_complete": "MISSIONE COMPLETATA",
        "certificates_obtained": "ATTESTATI OTTENUTI:",
        "main_menu": "MENU PRINCIPALE", "exit_game": "ESCI DAL GIOCO",
        "back_menu": "TORNA AL MENU", "time": "TEMPO:",
        "time_up": "Tempo scaduto! Non hai risposto abbastanza in fretta.",
        "completed": "[COMP]",
        
        # Titolo e intro
        "game_title": "KISS ME LIKE YOU LOVE ME: SHADOWS OF EQUALITY",
        "game_subtitle": "Un'esperienza interattiva che unisce il libro kiss me like you love me con punti 5 e 10 dell'Agenda 2030",
        "intro": "Niente è mai come appare, e la verità è spesso un gioco di ombre.\nIn questa stanza sei circondato da segreti che attendono di essere svelati.\nNon è solo tecnologia: è potere, è libertà, è il diritto di non essere invisibili.\nEsplora ogni angolo, sfida i tuoi pregiudizi e non aver paura della complessità.\nDimostra che la parità non è un miraggio, ma una conquista coraggiosa.\nIl gioco è appena iniziato. Dimostra quanto vali.",
        
        # Regole
        "rule1": "1. LO SGUARDO: Gli oggetti che nascondono un segreto reagiranno\nal tuo passaggio con un leggero bagliore. Impara a osservare.",
        "rule2": "2. IL MOMENTO: Non tutto è subito accessibile. Alcuni segreti\nsi sbloccheranno solo quando sarai pronto a vederli.",
        "rule3": "3. LA SCELTA: Ogni parola ha un peso. Rispondi correttamente per avanzare.",
        "rule4": "4. IL TEMPO: Hai 10 secondi per rispondere. Se il tempo scade, il gioco finisce.",
        "rule5": "5. IL TRAGUARDO: Colleziona gli Attestati 5 e 10 per sbloccare il finale.",
        "rule6": "6. MEMORIA: Il gioco salva automaticamente quando ricevi un attestato.",
        "rule_click": "Il velo sta per alzarsi. Clicca per entrare nell'ombra.",
        
        # Messaggi oggetti
        "pc_msg": "Un PC non è solo hardware, è il ponte che abbatte i confini:\ncollegare ogni individuo alla rete significa dare a tutti la stessa velocità di opportunità.",
        "watch_msg": "Il tempo non aspetta nessuno,\n ma la vera sfida è fare in modo che tutti abbiano lo stesso orario di partenza.\nRidurre le disuguaglianze significa sincronizzare le opportunità.",
        "phone_msg": "Uno smartphone ha mille sensori, ma nessuno vede la violenza che non lascia lividi.\n Il Punto 5 non è un'app che si installa: è il coraggio di capire che il controllo non è amore, e che un genere non è un telecomando per la vita di un altro. \n Guarda bene lo schermo: chi sta muovendo chi.",
        "system_update": "SISTEMA AGGIORNATO:\nIl cellulare sulla scrivania è ora sbloccato.\nInteragisci con esso per continuare l'analisi.",
        "bonus_unlock": "BONUS SBLOCCATO! \nHai combattuto contro le disuguaglianze e abbattuto i pregiudizi.\nMa ora che l'equilibrio è ristabilito, sei pronto a perderti nel caos?\nLa storia di Kiss Me Like You Love Me ti aspetta.\nEntra nel mondo di Selene e Neil, dove l'amore brucia e le ombre non perdonano.\nAttenzione: la perfezione dell'Agenda 2030 finisce qui. Benvenuti nell'abisso.",
        
        # Domande PC
        "pc_question": "Credi che la tecnologia possa davvero ridurre le disuguaglianze?",
        "pc_ans1": "Sì, se accessibile a tutti.",
        "pc_ans2": "No, crea solo più distacco.",
        "pc_wrong": "Se usata correttamente,\nla tecnologia è in grado di ridurre di molto le disuguaglianze.",
        
        # Domande Orologio
        "watch_question": "È giusto che tutti abbiano le stesse opportunità di partenza?",
        "watch_ans1": "Assolutamente sì.",
        "watch_ans2": "No, ognuno deve fare da sé.",
        "watch_wrong": "Ridurre le disuguaglianze significa proprio questo:\nFare in modo che tutti abbiano le stesse opportunità.",
        
        # Domande Cellulare
        "phone_q1": "Perché garantire a ogni donna il possesso di uno smartphone è un passo fondamentale verso l'uguaglianza?",
        "phone_q1_a1": "Perché le permette di partecipare attivamente alla vita economica e politica, facendo sentire la propria voce.",
        "phone_q1_a2": "Perché è un modo per tenerla occupata e distoglierla da problemi sociali più complessi.",
        "phone_q1_wrong": "Hai confuso un diritto con un passatempo.\nLa tecnologia è un'arma per l'indipendenza.",
        
        "phone_q2": "In che modo l'uso consapevole della tecnologia può aiutare a contrastare la denigrazione della donna?",
        "phone_q2_a1": "Limitando l'uso dei social per evitare di esporsi a critiche o giudizi estetici.",
        "phone_q2_a2": "Creando reti di solidarietà e spazi sicuri dove denunciare abusi e rivendicare i propri diritti.",
        "phone_q2_wrong": "Il silenzio non ferma l'odio.\nSenza reti di solidarietà, le donne restano isolate.",
        
        "phone_q3": "Cosa significa, nel Punto 5 dell'Agenda 2030, includere le donne nella rivoluzione digitale?",
        "phone_q3_a1": "Fornire loro dispositivi economici e semplificati rispetto a quelli degli uomini.",
        "phone_q3_a2": "Abbattere i pregiudizi che negano alle donne le stesse competenze e opportunità tecnologiche degli uomini",
        "phone_q3_wrong": "L'uguaglianza non è semplificazione, è accesso alla complessità.",
        
        # Certificati
        "cert_p10_title": "ATTESTATO OBIETTIVO 10",
        "cert_p10_body": "Hai smesso di guardare e hai iniziato a vedere.\nLa disuguaglianza prospera nell'indifferenza; tu hai scelto di riconoscerla.\nQuesto è il primo passo per distruggerla.",
        "cert_p10_name": "Atto d'Amore I: Il Diritto di Essere Uguali",
        
        "cert_p5_title": "ATTESTATO OBIETTIVO 5",
        "cert_p5_body": "Nessuna donna dovrebbe chiedere il permesso per esistere.\nHai difeso il diritto all'autodeterminazione.",
        "cert_p5_name": "Atto d'Amore II: La Forza della Parità",
        
        "cert_final_title": "ATTESTATO FINALE: LA COMPRENSIONE",
        "cert_final_body": "Hai attraversato l'oscurità di Neil e la forza di Selene.\nHai capito che non esiste parità senza la conoscenza del trauma.\nOra sei pronto a riscrivere le regole.",
        "cert_final_name": "Atto d'Amore III: Il Cuore oltre l'Abisso",
        
        # Racconto finale
        "story0": "La storia che racconterò ora è il riflesso nero dei diritti che hai difeso.\n È la cronaca di un amore tossico, affamato e senza leggi.\n Benvenuti nel mondo di Kiss Me Like You Love Me: dove l'amore non ti salva, ti consuma.",
        "story1": "Selene Anderson si trasferisce a New York per tentare di riallacciare i rapporti con il padre,\n ma ad accoglierla trova un mondo che non le appartiene. \n Nella sua nuova casa vivono i fratelli Miller: i figli della moglie del padre. \n Tra loro c'è Neil, il più enigmatico e tormentato, un ragazzo che porta i segni di un passato che nessuno dovrebbe conoscere.",
        "story2": "Neil non è un ragazzo normale: \n soffre di un disturbo della personalità e di un grave disturbo da stress post-traumatico derivante da un passato oscuro e violento che lo ha segnato profondamente.\n Fin dal primo istante, punta Selene. Non vuole amarla, vuole testarla. \n Inizia un gioco psicologico fatto di provocazioni e silenzi, dove ogni sguardo è una sfida e ogni contatto fisico è un confine che Neil non è pronto a superare.",
        "story3": "Selene scava nell'oscurità di Neil e scopre l'orrore.\n Neil è stato segnato da abusi atroci che hanno trasformato il suo concetto di affetto in qualcosa di distorto. \n Neil è convinto di essere un mostro incapace di provare sentimenti puri.\n La sua mente è un labirinto di traumi, e Selene sta per diventarne prigioniera volontaria.",
        "story4": "Quello tra Selene e Neil non è un amore da favola, è un'ossessione che consuma.\n Neil la spinge verso il baratro, alternando momenti di passione violenta a rifiuti gelidi. \n Selene si ritrova a lottare tra la sua dignità e una dipendenza viscerale da un ragazzo che sembra voler solo affogare.\n Qui la parità svanisce: resta solo il desiderio.",
        "story5": "Mentre il gioco perverso di Player stringe la sua morsa su di loro, Selene deve fare una scelta: \n non si tratta più solo di attrazione, ma di sopravvivenza psichica.\n Entrare nel mondo di Neil significa accettare le sue ombre e le sue ferite. \n La storia di Selene Anderson è la prova che, a volte, l'unico modo per amare qualcuno è imparare a respirare sott'acqua insieme a lui.",
        
        # Schermata finale
        "final_conclusion": "Hai dimostrato che la consapevolezza è il primo passo per il cambiamento.\nAttraverso la tua esplorazione hai raccolto gli strumenti per costruire un futuro\nbasato sull'uguaglianza e la parità di genere.",
        
        # Credits
        "credits": [
            "KISS ME LIKE YOU LOVE ME: SHADOWS OF EQUALITY",
            "",
            "Sviluppato da: Patrono Alessia",
            "Realizzato in stretta collaborazione con i Prof:",
            "Gabriella Testa e Silvia Mariggio',",
            "che hanno ispirato il progetto e guidato ogni passo della sua creazione.",
            "",
            "Ispirato al romanzo di Kira Shell",
            "",
            "OBIETTIVI AGENDA 2030:",
            "Punto 5: Parità di Genere",
            "Punto 10: Ridurre le Disuguaglianze",
            "",
            "Progetto realizzato unendo il libro Kiss Me Like You Love Me,",
            "con i punti 5 e 10 dell'Agenda 2030",
            "",
            "GRAZIE PER AVER GIOCATO",
            "",
            "Fine dell'esperienza"
        ]
    },
    
    "en": {
        # Menu e UI
        "start": "START", "exit": "EXIT", "settings": "SETTINGS", "back": "BACK",
        "resume": "RESUME", "restart": "RESTART", "menu": "MAIN MENU",
        "lang_label": "Select Language:", "vibe": "Screen Vibration: ",
        "rules_title": "WELCOME: GAME RULES",
        "save_select": "SELECT A SAVE SLOT",
        "pause_title": "GAME PAUSED",
        "slot": "Slot", "slot_empty": "Empty Slot",
        "certificates": "CERTIFICATES", "back_game": "BACK TO GAME",
        "quit": "QUIT", "volume": "Volume:", "music": "Music:",
        "on": "ON", "off": "OFF", "yes": "YES", "no": "NO",
        "pause": "PAUSE", "click_continue": "Click to continue",
        "click_menu": "Click to return to menu",
        "delete_confirm": "Are you sure you want to delete this save?",
        "your_certificates": "YOUR CERTIFICATES",
        "mission_complete": "MISSION COMPLETED",
        "certificates_obtained": "CERTIFICATES OBTAINED:",
        "main_menu": "MAIN MENU", "exit_game": "EXIT GAME",
        "back_menu": "BACK TO MENU", "time": "TIME:",
        "time_up": "Time's up! You didn't answer fast enough.",
        "completed": "[DONE]",
        
        # Titolo e intro
        "game_title": "KISS ME LIKE YOU LOVE ME: SHADOWS OF EQUALITY",
        "game_subtitle": "An interactive experience combining the book Kiss Me Like You Love Me with SDG Goals 5 and 10",
        "intro": "Nothing is as it seems, and truth is often a game of shadows.\nIn this room you are surrounded by secrets waiting to be unveiled.\nIt's not just technology: it's power, it's freedom, it's the right not to be invisible.\nExplore every corner, challenge your prejudices and don't be afraid of complexity.\nProve that equality is not a mirage, but a courageous achievement.\nThe game has just begun. Show your worth.",
        
        # Regole
        "rule1": "1. THE GAZE: Objects hiding secrets will react\nto your passage with a faint glow. Learn to observe.",
        "rule2": "2. THE MOMENT: Not everything is immediately accessible. Some secrets\nwill unlock only when you're ready to see them.",
        "rule3": "3. THE CHOICE: Every word carries weight. Answer correctly to advance.",
        "rule4": "4. THE TIME: You have 10 seconds to answer. If time runs out, the game ends.",
        "rule5": "5. THE GOAL: Collect Certificates 5 and 10 to unlock the finale.",
        "rule6": "6. MEMORY: The game saves automatically when you receive a certificate.",
        "rule_click": "The veil is about to lift. Click to enter the shadow.",
        
        # Messaggi oggetti
        "pc_msg": "A PC is not just hardware, it's the bridge that breaks down barriers:\nconnecting every individual to the network means giving everyone the same speed of opportunity.",
        "watch_msg": "Time waits for no one,\nbut the real challenge is ensuring everyone has the same starting time.\nReducing inequalities means synchronizing opportunities.",
        "phone_msg": "A smartphone has a thousand sensors, but no one sees the violence that leaves no bruises.\nGoal 5 is not an app you install: it's the courage to understand that control is not love, and that one gender is not a remote control for another's life.\nLook closely at the screen: who's controlling whom.",
        "system_update": "SYSTEM UPDATED:\nThe phone on the desk is now unlocked.\nInteract with it to continue the analysis.",
        "bonus_unlock": "BONUS UNLOCKED!\nYou fought against inequalities and broke down prejudices.\nBut now that balance is restored, are you ready to lose yourself in chaos?\nThe story of Kiss Me Like You Love Me awaits you.\nEnter the world of Selene and Neil, where love burns and shadows don't forgive.\nWarning: the perfection of the 2030 Agenda ends here. Welcome to the abyss.",
        
        # Domande PC
        "pc_question": "Do you believe technology can truly reduce inequalities?",
        "pc_ans1": "Yes, if accessible to everyone.",
        "pc_ans2": "No, it only creates more distance.",
        "pc_wrong": "When used correctly,\ntechnology can greatly reduce inequalities.",
        
        # Domande Orologio
        "watch_question": "Is it fair for everyone to have the same starting opportunities?",
        "watch_ans1": "Absolutely yes.",
        "watch_ans2": "No, everyone must fend for themselves.",
        "watch_wrong": "Reducing inequalities means exactly this:\nEnsuring everyone has the same opportunities.",
        
        # Domande Cellulare
        "phone_q1": "Why is ensuring every woman owns a smartphone a fundamental step toward equality?",
        "phone_q1_a1": "Because it allows her to actively participate in economic and political life, making her voice heard.",
        "phone_q1_a2": "Because it's a way to keep her busy and distract her from more complex social issues.",
        "phone_q1_wrong": "You confused a right with a pastime.\nTechnology is a weapon for independence.",
        
        "phone_q2": "How can conscious use of technology help counter the denigration of women?",
        "phone_q2_a1": "By limiting social media use to avoid exposure to criticism or aesthetic judgments.",
        "phone_q2_a2": "By creating solidarity networks and safe spaces to report abuse and claim rights.",
        "phone_q2_wrong": "Silence doesn't stop hatred.\nWithout solidarity networks, women remain isolated.",
        
        "phone_q3": "What does it mean, in Goal 5 of the 2030 Agenda, to include women in the digital revolution?",
        "phone_q3_a1": "Providing them with cheaper and simplified devices compared to men's.",
        "phone_q3_a2": "Breaking down prejudices that deny women the same technological skills and opportunities as men",
        "phone_q3_wrong": "Equality is not simplification, it's access to complexity.",
        
        # Certificati
        "cert_p10_title": "CERTIFICATE GOAL 10",
        "cert_p10_body": "You stopped looking and started seeing.\nInequality thrives in indifference; you chose to recognize it.\nThis is the first step to destroy it.",
        "cert_p10_name": "Act of Love I: The Right to Be Equal",
        
        "cert_p5_title": "CERTIFICATE GOAL 5",
        "cert_p5_body": "No woman should ask permission to exist.\nYou defended the right to self-determination.",
        "cert_p5_name": "Act of Love II: The Strength of Equality",
        
        "cert_final_title": "FINAL CERTIFICATE: UNDERSTANDING",
        "cert_final_body": "You crossed through Neil's darkness and Selene's strength.\nYou understood that there is no equality without knowledge of trauma.\nNow you're ready to rewrite the rules.",
        "cert_final_name": "Act of Love III: The Heart Beyond the Abyss",
        
        # Racconto finale
        "story0": "The story I'm about to tell is the dark reflection of the rights you defended.\nIt's the chronicle of a toxic love, hungry and lawless.\nWelcome to the world of Kiss Me Like You Love Me: where love doesn't save you, it consumes you.",
        "story1": "Selene Anderson moves to New York to reconnect with her father,\nbut finds a world that doesn't belong to her.\nIn her new home live the Miller brothers: her father's wife's sons.\nAmong them is Neil, the most enigmatic and tormented, a boy bearing the marks of a past no one should know.",
        "story2": "Neil is not a normal boy:\nhe suffers from a personality disorder and severe PTSD from a dark and violent past that deeply marked him.\nFrom the first moment, he targets Selene. He doesn't want to love her, he wants to test her.\nA psychological game begins, made of provocations and silences, where every glance is a challenge and every physical contact is a boundary Neil isn't ready to cross.",
        "story3": "Selene digs into Neil's darkness and discovers horror.\nNeil has been marked by atrocious abuse that distorted his concept of affection.\nNeil is convinced he's a monster incapable of pure feelings.\nHis mind is a labyrinth of trauma, and Selene is about to become its voluntary prisoner.",
        "story4": "What's between Selene and Neil isn't a fairy tale love, it's a consuming obsession.\nNeil pushes her toward the abyss, alternating moments of violent passion with cold rejections.\nSelene finds herself fighting between her dignity and a visceral dependence on a boy who seems to only want to drown.\nHere equality vanishes: only desire remains.",
        "story5": "As Player's perverse game tightens its grip on them, Selene must make a choice:\nit's no longer just about attraction, but psychic survival.\nEntering Neil's world means accepting his shadows and wounds.\nSelene Anderson's story is proof that sometimes, the only way to love someone is to learn to breathe underwater with them.",
        
        # Schermata finale
        "final_conclusion": "You proved that awareness is the first step to change.\nThrough your exploration you gathered the tools to build a future\nbased on equality and gender parity.",
        
        # Credits
        "credits": [
            "KISS ME LIKE YOU LOVE ME: SHADOWS OF EQUALITY",
            "",
            "Developed by: Patrono Alessia",
            "Created in close collaboration with Professors:",
            "Gabriella Testa and Silvia Mariggio',",
            "who inspired the project and guided every step of its creation.",
            "",
            "Inspired by the novel by Kira Shell",
            "",
            "2030 AGENDA GOALS:",
            "Goal 5: Gender Equality",
            "Goal 10: Reduced Inequalities",
            "",
            "Project created combining the book Kiss Me Like You Love Me",
            "with Goals 5 and 10 of the 2030 Agenda",
            "",
            "THANK YOU FOR PLAYING",
            "",
            "End of experience"
        ]
    },
    
    "es": {
        # Menu e UI
        "start": "INICIAR", "exit": "SALIR", "settings": "AJUSTES", "back": "VOLVER",
        "resume": "REANUDAR", "restart": "REINICIAR", "menu": "MENÚ PRINCIPAL",
        "lang_label": "Seleccionar Idioma:", "vibe": "Vibración de Pantalla: ",
        "rules_title": "BIENVENIDO: REGLAS DEL JUEGO",
        "save_select": "SELECCIONAR RANURA DE GUARDADO",
        "pause_title": "JUEGO EN PAUSA",
        "slot": "Ranura", "slot_empty": "Ranura Vacía",
        "certificates": "CERTIFICADOS", "back_game": "VOLVER AL JUEGO",
        "quit": "SALIR", "volume": "Volumen:", "music": "Música:",
        "on": "ACTIVADA", "off": "DESACTIVADA", "yes": "SÍ", "no": "NO",
        "pause": "PAUSA", "click_continue": "Haz clic para continuar",
        "click_menu": "Haz clic para volver al menú",
        "delete_confirm": "¿Estás seguro de que quieres eliminar esta partida?",
        "your_certificates": "TUS CERTIFICADOS",
        "mission_complete": "MISIÓN COMPLETADA",
        "certificates_obtained": "CERTIFICADOS OBTENIDOS:",
        "main_menu": "MENÚ PRINCIPAL", "exit_game": "SALIR DEL JUEGO",
        "back_menu": "VOLVER AL MENÚ", "time": "TIEMPO:",
        "time_up": "¡Se acabó el tiempo! No respondiste lo suficientemente rápido.",
        "completed": "[COMP]",
        
        # Titolo e intro
        "game_title": "KISS ME LIKE YOU LOVE ME: SHADOWS OF EQUALITY",
        "game_subtitle": "Una experiencia interactiva que une el libro Kiss Me Like You Love Me con los ODS 5 y 10",
        "intro": "Nada es como parece, y la verdad es a menudo un juego de sombras.\nEn esta habitación estás rodeado de secretos esperando ser revelados.\nNo es solo tecnología: es poder, es libertad, es el derecho a no ser invisible.\nExplora cada rincón, desafía tus prejuicios y no temas la complejidad.\nDemuestra que la igualdad no es un espejismo, sino una conquista valiente.\nEl juego acaba de comenzar. Demuestra tu valía.",
        
        # Regole
        "rule1": "1. LA MIRADA: Los objetos que esconden secretos reaccionarán\na tu paso con un ligero resplandor. Aprende a observar.",
        "rule2": "2. EL MOMENTO: No todo es accesible inmediatamente. Algunos secretos\nse desbloquearán solo cuando estés listo para verlos.",
        "rule3": "3. LA ELECCIÓN: Cada palabra tiene peso. Responde correctamente para avanzar.",
        "rule4": "4. EL TIEMPO: Tienes 10 segundos para responder. Si se acaba el tiempo, el juego termina.",
        "rule5": "5. EL OBJETIVO: Recolecta los Certificados 5 y 10 para desbloquear el final.",
        "rule6": "6. MEMORIA: El juego se guarda automáticamente cuando recibes un certificado.",
        "rule_click": "El velo está a punto de levantarse. Haz clic para entrar en la sombra.",
        
        # Messaggi oggetti
        "pc_msg": "Una PC no es solo hardware, es el puente que derriba fronteras:\nconectar a cada individuo a la red significa dar a todos la misma velocidad de oportunidades.",
        "watch_msg": "El tiempo no espera a nadie,\npero el verdadero desafío es asegurar que todos tengan la misma hora de inicio.\nReducir las desigualdades significa sincronizar las oportunidades.",
        "phone_msg": "Un smartphone tiene mil sensores, pero nadie ve la violencia que no deja moretones.\nEl Objetivo 5 no es una app que instalas: es el coraje de entender que el control no es amor, y que un género no es un control remoto para la vida del otro.\nMira bien la pantalla: ¿quién está controlando a quién?",
        "system_update": "SISTEMA ACTUALIZADO:\nEl teléfono en el escritorio está ahora desbloqueado.\nInteractúa con él para continuar el análisis.",
        "bonus_unlock": "¡BONUS DESBLOQUEADO!\nLuchaste contra las desigualdades y derribaste prejuicios.\n¿Pero ahora que el equilibrio está restaurado, estás listo para perderte en el caos?\nLa historia de Kiss Me Like You Love Me te espera.\nEntra en el mundo de Selene y Neil, donde el amor quema y las sombras no perdonan.\nAdvertencia: la perfección de la Agenda 2030 termina aquí. Bienvenido al abismo.",
        
        # Domande PC
        "pc_question": "¿Crees que la tecnología puede reducir realmente las desigualdades?",
        "pc_ans1": "Sí, si es accesible para todos.",
        "pc_ans2": "No, solo crea más distancia.",
        "pc_wrong": "Cuando se usa correctamente,\nla tecnología puede reducir mucho las desigualdades.",
        
        # Domande Orologio
        "watch_question": "¿Es justo que todos tengan las mismas oportunidades de partida?",
        "watch_ans1": "Absolutamente sí.",
        "watch_ans2": "No, cada uno debe valerse por sí mismo.",
        "watch_wrong": "Reducir las desigualdades significa exactamente esto:\nAsegurar que todos tengan las mismas oportunidades.",
        
        # Domande Cellulare
        "phone_q1": "¿Por qué garantizar que cada mujer tenga un smartphone es un paso fundamental hacia la igualdad?",
        "phone_q1_a1": "Porque le permite participar activamente en la vida económica y política, haciendo oír su voz.",
        "phone_q1_a2": "Porque es una forma de mantenerla ocupada y distraerla de problemas sociales más complejos.",
        "phone_q1_wrong": "Confundiste un derecho con un pasatiempo.\nLa tecnología es un arma para la independencia.",
        
        "phone_q2": "¿De qué manera el uso consciente de la tecnología puede ayudar a contrarrestar la denigración de la mujer?",
        "phone_q2_a1": "Limitando el uso de redes sociales para evitar exponerse a críticas o juicios estéticos.",
        "phone_q2_a2": "Creando redes de solidaridad y espacios seguros para denunciar abusos y reclamar derechos.",
        "phone_q2_wrong": "El silencio no detiene el odio.\nSin redes de solidaridad, las mujeres quedan aisladas.",
        
        "phone_q3": "¿Qué significa, en el Objetivo 5 de la Agenda 2030, incluir a las mujeres en la revolución digital?",
        "phone_q3_a1": "Proporcionarles dispositivos más baratos y simplificados en comparación con los de los hombres.",
        "phone_q3_a2": "Derribar los prejuicios que niegan a las mujeres las mismas habilidades y oportunidades tecnológicas que los hombres",
        "phone_q3_wrong": "La igualdad no es simplificación, es acceso a la complejidad.",
        
        # Certificati
        "cert_p10_title": "CERTIFICADO OBJETIVO 10",
        "cert_p10_body": "Dejaste de mirar y empezaste a ver.\nLa desigualdad prospera en la indiferencia; tú elegiste reconocerla.\nEste es el primer paso para destruirla.",
        "cert_p10_name": "Acto de Amor I: El Derecho a Ser Iguales",
        
        "cert_p5_title": "CERTIFICADO OBJETIVO 5",
        "cert_p5_body": "Ninguna mujer debería pedir permiso para existir.\nDefendiste el derecho a la autodeterminación.",
        "cert_p5_name": "Acto de Amor II: La Fuerza de la Igualdad",
        
        "cert_final_title": "CERTIFICADO FINAL: LA COMPRENSIÓN",
        "cert_final_body": "Atravesaste la oscuridad de Neil y la fuerza de Selene.\nEntendiste que no hay igualdad sin conocimiento del trauma.\nAhora estás listo para reescribir las reglas.",
        "cert_final_name": "Acto de Amor III: El Corazón Más Allá del Abismo",
        
        # Racconto finale
        "story0": "La historia que voy a contar es el reflejo oscuro de los derechos que defendiste.\nEs la crónica de un amor tóxico, hambriento y sin leyes.\nBienvenido al mundo de Kiss Me Like You Love Me: donde el amor no te salva, te consume.",
        "story1": "Selene Anderson se muda a Nueva York para intentar reconectar con su padre,\npero encuentra un mundo que no le pertenece.\nEn su nuevo hogar viven los hermanos Miller: los hijos de la esposa de su padre.\nEntre ellos está Neil, el más enigmático y atormentado, un chico que lleva las marcas de un pasado que nadie debería conocer.",
        "story2": "Neil no es un chico normal:\nsufre de un trastorno de personalidad y TEPT grave derivado de un pasado oscuro y violento que lo marcó profundamente.\nDesde el primer momento, apunta a Selene. No quiere amarla, quiere probarla.\nComienza un juego psicológico hecho de provocaciones y silencios, donde cada mirada es un desafío y cada contacto físico es un límite que Neil no está listo para cruzar.",
        "story3": "Selene cava en la oscuridad de Neil y descubre el horror.\nNeil ha sido marcado por abusos atroces que transformaron su concepto de afecto en algo distorsionado.\nNeil está convencido de ser un monstruo incapaz de sentimientos puros.\nSu mente es un laberinto de traumas, y Selene está a punto de convertirse en su prisionera voluntaria.",
        "story4": "Lo que hay entre Selene y Neil no es un amor de cuento de hadas, es una obsesión que consume.\nNeil la empuja hacia el abismo, alternando momentos de pasión violenta con rechazos fríos.\nSelene se encuentra luchando entre su dignidad y una dependencia visceral de un chico que parece solo querer ahogarse.\nAquí la igualdad se desvanece: solo queda el deseo.",
        "story5": "Mientras el juego perverso de Player aprieta su control sobre ellos, Selene debe tomar una decisión:\nya no se trata solo de atracción, sino de supervivencia psíquica.\nEntrar en el mundo de Neil significa aceptar sus sombras y heridas.\nLa historia de Selene Anderson es la prueba de que, a veces, la única forma de amar a alguien es aprender a respirar bajo el agua junto a él.",
        
        # Schermata finale
        "final_conclusion": "Demostraste que la conciencia es el primer paso hacia el cambio.\nA través de tu exploración recopilaste las herramientas para construir un futuro\nbasado en la igualdad y la paridad de género.",
        
        # Credits
        "credits": [
            "KISS ME LIKE YOU LOVE ME: SHADOWS OF EQUALITY",
            "",
            "Desarrollado por: Patrono Alessia",
            "Realizado en estrecha colaboración con los Profesores:",
            "Gabriella Testa y Silvia Mariggio',",
            "quienes inspiraron el proyecto y guiaron cada paso de su creación.",
            "",
            "Inspirado en la novela de Kira Shell",
            "",
            "OBJETIVOS AGENDA 2030:",
            "Objetivo 5: Igualdad de Género",
            "Objetivo 10: Reducción de las Desigualdades",
            "",
            "Proyecto creado combinando el libro Kiss Me Like You Love Me",
            "con los Objetivos 5 y 10 de la Agenda 2030",
            "",
            "GRACIAS POR JUGAR",
            "",
            "Fin de la experiencia"
        ]
    }
}

# --- 1. INIZIALIZZAZIONE ---
pygame.init()
pygame.mixer.init() 
cartella_progetto = os.path.dirname(__file__)
percorso_immagine = os.path.join(cartella_progetto, "immagine_sfondo.png")

# Gestione 3 Slot di salvataggio
percorsi_save = [os.path.join(cartella_progetto, f"save_slot_{i}.json") for i in range(1, 4)]
slot_selezionato = 0
confirma_elimina = -1 

percorso_menu = os.path.join(cartella_progetto, "musica_menu.mp3")
percorso_home = os.path.join(cartella_progetto, "musica_home.mp3")

volume_audio = 0.4
musica_attiva = True
vibrazione_attiva = True
offset_x, offset_y = 0, 0 

L_VIRTUAL, A_VIRTUAL = 1600, 900
info = pygame.display.Info()
monitor_w, monitor_h = info.current_w, info.current_h
win_w = min(L_VIRTUAL, int(monitor_w * 0.9))
win_h = int(win_w * (A_VIRTUAL / L_VIRTUAL))

screen = pygame.display.set_mode((win_w, win_h), pygame.RESIZABLE)
canvas = pygame.Surface((L_VIRTUAL, A_VIRTUAL))
pygame.display.set_caption("Progetto: Kiss Me Like You Love Me: Shadows of Equality")

# --- CLASSE PARTICELLE ---
class Particella:
    def __init__(self):
        self.reset()

    def reset(self):
        self.x = random.randint(0, L_VIRTUAL)
        self.y = random.randint(0, A_VIRTUAL)
        self.vx = random.uniform(-0.5, 0.5)
        self.vy = random.uniform(-0.5, -0.1)
        self.size = random.randint(2, 5)
        self.alpha = random.randint(50, 180)
        self.fade_speed = random.uniform(0.2, 0.8)

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.alpha -= self.fade_speed
        if self.alpha <= 0 or self.y < -10:
            self.reset()

    def draw(self, surf):
        p_surf = pygame.Surface((self.size*2, self.size*2), pygame.SRCALPHA)
        pygame.draw.circle(p_surf, (255, 255, 220, int(self.alpha)), (self.size, self.size), self.size)
        surf.blit(p_surf, (self.x, self.y))

particelle_polvere = [Particella() for _ in range(50)]

# --- RISORSE ---
try:
    sfondo_originale = pygame.image.load(percorso_immagine).convert()
    sfondo = pygame.transform.scale(sfondo_originale, (L_VIRTUAL, A_VIRTUAL))
except pygame.error:
    sfondo = pygame.Surface((L_VIRTUAL, A_VIRTUAL))
    sfondo.fill((200, 200, 200))

# --- LOGICA SALVATAGGI ---
def salva_dati():
    lang = LINGUE[lingua_selezionata]
    finito = lang["cert_final_name"] in attestati_raccolti
    dati = {
        "attestati": attestati_raccolti, "vittoria": vittoria,
        "pc": pc_clicked, "watch": watch_clicked, "phone": phone_clicked,
        "p10": mostrato_certificato_p10, "avviso_cell": avviso_cellulare_mostrato, 
        "bonus": mostrato_avviso_bonus, "finito": finito, "lang": lingua_selezionata
    }
    with open(percorsi_save[slot_selezionato], "w") as f:
        json.dump(dati, f)

def carica_dati(indice):
    global attestati_raccolti, vittoria, pc_clicked, watch_clicked, phone_clicked, mostrato_certificato_p10, avviso_cellulare_mostrato, mostrato_avviso_bonus, slot_selezionato, lingua_selezionata
    if os.path.exists(percorsi_save[indice]):
        try:
            with open(percorsi_save[indice], "r") as f:
                d = json.load(f)
                attestati_raccolti = d.get("attestati", [])
                vittoria = d.get("vittoria", False)
                pc_clicked = d.get("pc", False)
                watch_clicked = d.get("watch", False)
                phone_clicked = d.get("phone", False)
                mostrato_certificato_p10 = d.get("p10", False)
                avviso_cellulare_mostrato = d.get("avviso_cell", False)
                mostrato_avviso_bonus = d.get("bonus", False)
                lingua_selezionata = d.get("lang", "it")
                slot_selezionato = indice
                return True
        except: return False
    return False

def gestisci_musica(percorso):
    if not musica_attiva: return
    try:
        pygame.mixer.music.stop()
        pygame.mixer.music.load(percorso)
        pygame.mixer.music.set_volume(volume_audio)
        pygame.mixer.music.play(-1, fade_ms=2000)
    except pygame.error:
        print(f"Nota: File {os.path.basename(percorso)} non trovato.")

def attiva_vibrazione():
    global offset_x, offset_y
    if vibrazione_attiva:
        offset_x, offset_y = random.randint(-10, 10), random.randint(-10, 10)

# COLORI E FONT
WHITE, BLACK = (255, 255, 255), (0, 0, 0)
GRAY, GOLD = (220, 220, 220), (255, 215, 0)
GREEN, RED = (34, 139, 34), (200, 0, 0)
DARK_BAR = (10, 10, 10, 245)
COBALT_BLUE = (0, 71, 171)

font = pygame.font.SysFont("Arial", 22)
font_vittoria = pygame.font.SysFont("Arial", 28, bold=True)
font_button = pygame.font.SysFont("Arial", 18, bold=True)
font_small = pygame.font.SysFont("Arial", 14, bold=True) 
font_cert = pygame.font.SysFont("Times New Roman", 35, bold=True, italic=True)
font_titolo = pygame.font.SysFont("Arial", 60, bold=True)

# --- STATI ---
MENU, STUDY, THOUGHT, DIALOGUE, END, PAUSE, CERTIFICATE, PORTFOLIO, FINAL_SCREEN, SETTINGS, CREDITS, SLOTS, RULES = range(13)
state = MENU
previous_state = MENU 
message_text, dialogue_step = "", 0
pc_clicked = watch_clicked = phone_clicked = books_clicked = vittoria = False
attestati_raccolti = []
mostrato_certificato_p10 = False
avviso_cellulare_mostrato = False
mostrato_avviso_bonus = False 
titolo_cert, corpo_cert = "", ""
char_index = 0
last_update = 0
TEMPO_RISPOSTA = 20000 
timer_inizio = 0
y_credits = A_VIRTUAL

indice_racconto = 0

ALTEZZA_FASCIA = 180
Y_FASCIA = A_VIRTUAL - ALTEZZA_FASCIA 
Y_PULSANTI = Y_FASCIA - 100 

pc_rect = pygame.Rect(860, 360, 220, 200)
watch_rect = pygame.Rect(1192, 435, 95, 95)
phone_rect = pygame.Rect(735, 550, 100, 45)
books_rect = pygame.Rect(435, 500, 125, 100) 
btn_pause_toggle = pygame.Rect(1450, 20, 130, 50) 
btn_zaino = pygame.Rect(20, 20, 250, 50) 
btn_start_game = pygame.Rect(L_VIRTUAL // 2 - 150, 620, 300, 60)
btn_exit_game = pygame.Rect(L_VIRTUAL // 2 - 150, 710, 300, 60)

# Pulsanti lingue nel menu iniziale
btn_lang_menu_it = pygame.Rect(L_VIRTUAL // 2 - 180, 800, 110, 45)
btn_lang_menu_en = pygame.Rect(L_VIRTUAL // 2 - 55, 800, 110, 45)
btn_lang_menu_es = pygame.Rect(L_VIRTUAL // 2 + 70, 800, 110, 45)

slots_rects = [pygame.Rect(L_VIRTUAL // 2 - 250, 350 + (i*110), 500, 80) for i in range(3)]
elimina_rects = [pygame.Rect(L_VIRTUAL // 2 - 240, 360 + (i*110), 60, 60) for i in range(3)]
btn_si_elimina = [pygame.Rect(L_VIRTUAL // 2 + 100, 365 + (i*110), 65, 50) for i in range(3)]
btn_no_elimina = [pygame.Rect(L_VIRTUAL // 2 + 175, 365 + (i*110), 65, 50) for i in range(3)]

btn_back_slots = pygame.Rect(L_VIRTUAL // 2 - 150, 750, 300, 60)
btn_close_rules = pygame.Rect(L_VIRTUAL // 2 - 150, 750, 300, 60)

btn_resume = pygame.Rect(L_VIRTUAL // 2 - 150, 220, 300, 60)
btn_restart = pygame.Rect(L_VIRTUAL // 2 - 150, 300, 300, 60)
btn_settings = pygame.Rect(L_VIRTUAL // 2 - 150, 380, 300, 60)
btn_back_menu = pygame.Rect(L_VIRTUAL // 2 - 150, 460, 300, 60)
btn_quit = pygame.Rect(L_VIRTUAL // 2 - 150, 540, 300, 60)
btn_toggle_music = pygame.Rect(L_VIRTUAL // 2 - 150, 380, 300, 55)
btn_toggle_vibe = pygame.Rect(L_VIRTUAL // 2 - 150, 460, 300, 55)
btn_lang_it = pygame.Rect(L_VIRTUAL // 2 - 230, 580, 140, 50)
btn_lang_en = pygame.Rect(L_VIRTUAL // 2 - 70, 580, 140, 50)
btn_lang_es = pygame.Rect(L_VIRTUAL // 2 + 90, 580, 140, 50)
btn_back_from_settings = pygame.Rect(L_VIRTUAL // 2 - 150, 720, 300, 60)
btn_final_menu = pygame.Rect(L_VIRTUAL // 2 - 320, 750, 300, 60)
btn_final_exit = pygame.Rect(L_VIRTUAL // 2 + 20, 750, 300, 60)

btn_w, btn_h = 420, 80
gap = 40
start_x = (L_VIRTUAL - (btn_w * 2 + gap)) // 2
btn_left = pygame.Rect(start_x, Y_PULSANTI, btn_w, btn_h)
btn_right = pygame.Rect(start_x + btn_w + gap, Y_PULSANTI, btn_w, btn_h)
btn_large_left = pygame.Rect(start_x, Y_PULSANTI - 40, btn_w, 120)
btn_large_right = pygame.Rect(start_x + btn_w + gap, Y_PULSANTI - 40, btn_w, 120)

def reset_game():
    global state, pc_clicked, watch_clicked, phone_clicked, books_clicked, vittoria, mostrato_certificato_p10, attestati_raccolti, message_text, avviso_cellulare_mostrato, mostrato_avviso_bonus, indice_racconto, y_credits, confirma_elimina, char_index
    state = MENU
    message_text = ""
    char_index = 0
    pc_clicked = watch_clicked = phone_clicked = books_clicked = vittoria = False
    mostrato_certificato_p10 = avviso_cellulare_mostrato = mostrato_avviso_bonus = False
    indice_racconto = 0
    attestati_raccolti = []
    y_credits = A_VIRTUAL
    confirma_elimina = -1
    gestisci_musica(percorso_menu)

def draw_text_centered(surf, text, y_pos, color=BLACK, bold=False, custom_font=None):
    used_font = custom_font if custom_font else (font_vittoria if bold else font)
    lines = text.split('\n')
    for i, line in enumerate(lines):
        t_s = used_font.render(line.strip(), True, color)
        t_r = t_s.get_rect(center=(L_VIRTUAL // 2, y_pos + (i * 35)))
        surf.blit(t_s, t_r)

def draw_button(canvas, rect, text, mouse_pos, color_override=None):
    is_hover = rect.collidepoint(mouse_pos)
    if color_override:
        base_color = (*color_override, 220) if is_hover else (*color_override, 180)
    else:
        base_color = (50, 50, 50, 220) if is_hover else (30, 30, 30, 180)
    
    btn_surf = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)
    pygame.draw.rect(btn_surf, base_color, (0, 0, rect.width, rect.height), border_radius=12)
    canvas.blit(btn_surf, rect.topleft)
    
    words = text.split(' ')
    lines, curr = [], ""
    for w in words:
        if font_button.size(curr + w)[0] < rect.width - 20: curr += w + " "
        else: lines.append(curr); curr = w + " "
    lines.append(curr)
    for i, l in enumerate(lines):
        t_s = font_button.render(l.strip(), True, WHITE)
        t_r = t_s.get_rect(center=(rect.centerx, rect.centery - (len(lines)-1)*10 + i * 20))
        canvas.blit(t_s, t_r)

def draw_interactive_object(surf, rect, mouse_pos):
    if rect.collidepoint(mouse_pos):
        margin = 120 
        glow_surf = pygame.Surface((rect.width + margin*2, rect.height + margin*2), pygame.SRCALPHA)
        for i in range(50, 0, -1):
            alpha = int(70 * (1 - i/50)**3)
            expand = i * (margin / 50)
            pygame.draw.ellipse(glow_surf, (255, 255, 200, alpha), pygame.Rect(margin-expand, margin-expand, rect.width+expand*2, rect.height+expand*2))
        surf.blit(glow_surf, (rect.x - margin, rect.y - margin))

def draw_checkmark(surf, rect):
    punti = [(rect.right - 20, rect.top + 10), (rect.right - 12, rect.top + 20), (rect.right - 4, rect.top + 4)]
    pygame.draw.lines(surf, GREEN, False, punti, 4)

def effetto_transizione(canvas_surf, screen_surf, clock, tipo="OUT"):
    fade_surf = pygame.Surface((L_VIRTUAL, A_VIRTUAL))
    fade_surf.fill(BLACK)
    range_alpha = range(0, 256, 8) if tipo == "OUT" else range(255, -1, -8)
    for alpha in range_alpha:
        fade_surf.set_alpha(alpha)
        real_w, real_h = screen_surf.get_size()
        screen_surf.blit(pygame.transform.smoothscale(canvas_surf, (real_w, real_h)), (0, 0))
        overlay_scaled = pygame.transform.smoothscale(fade_surf, (real_w, real_h))
        screen_surf.blit(overlay_scaled, (0, 0))
        pygame.display.flip()
        clock.tick(60)

def main():
    global state, previous_state, message_text, pc_clicked, watch_clicked, phone_clicked, books_clicked, dialogue_step, vittoria, attestati_raccolti, titolo_cert, corpo_cert, mostrato_certificato_p10, avviso_cellulare_mostrato, mostrato_avviso_bonus, volume_audio, musica_attiva, vibrazione_attiva, offset_x, offset_y, indice_racconto, y_credits, timer_inizio, slot_selezionato, confirma_elimina, char_index, last_update, lingua_selezionata
    running, clock = True, pygame.time.Clock()
    last_obj, txt_main = "", ""
    trascinando_volume = False
    gestisci_musica(percorso_menu)

    while running:
        real_w, real_h = screen.get_size()
        m_x, m_y = pygame.mouse.get_pos()
        m_pos = (m_x * L_VIRTUAL / real_w, m_y * A_VIRTUAL / real_h)
        
        # Recupera le traduzioni per la lingua corrente
        lang = LINGUE[lingua_selezionata]
        
        offset_x *= 0.8
        offset_y *= 0.8
        
        canvas.blit(sfondo, (offset_x, offset_y))
        for p in particelle_polvere:
            p.update()
            p.draw(canvas)

        if state == DIALOGUE:
            tempo_trascorso = pygame.time.get_ticks() - timer_inizio
            if tempo_trascorso > TEMPO_RISPOSTA:
                message_text, vittoria, state = lang["time_up"], False, END
                pygame.mixer.music.stop()

        clickable = False
        if state == MENU: clickable = btn_start_game.collidepoint(m_pos) or btn_exit_game.collidepoint(m_pos) or btn_lang_menu_it.collidepoint(m_pos) or btn_lang_menu_en.collidepoint(m_pos) or btn_lang_menu_es.collidepoint(m_pos)
        elif state == SLOTS: clickable = any(r.collidepoint(m_pos) for r in slots_rects) or any(r.collidepoint(m_pos) for r in elimina_rects) or any(r.collidepoint(m_pos) for r in btn_si_elimina) or any(r.collidepoint(m_pos) for r in btn_no_elimina) or btn_back_slots.collidepoint(m_pos)
        elif state == RULES: clickable = True 
        elif state == STUDY: clickable = pc_rect.collidepoint(m_pos) or watch_rect.collidepoint(m_pos) or btn_pause_toggle.collidepoint(m_pos) or (vittoria and books_rect.collidepoint(m_pos)) or (attestati_raccolti and btn_zaino.collidepoint(m_pos)) or (pc_clicked and watch_clicked and phone_rect.collidepoint(m_pos))
        elif state == PAUSE: clickable = any(b.collidepoint(m_pos) for b in [btn_resume, btn_restart, btn_settings, btn_back_menu, btn_quit])
        elif state == SETTINGS: 
            bar_rect = pygame.Rect((L_VIRTUAL - 400) // 2, 315, 400, 20)
            clickable = any(b.collidepoint(m_pos) for b in [btn_toggle_music, btn_toggle_vibe, btn_back_from_settings, btn_lang_it, btn_lang_en, btn_lang_es]) or bar_rect.collidepoint(m_pos)
        elif state == DIALOGUE: clickable = btn_left.collidepoint(m_pos) or btn_right.collidepoint(m_pos) or btn_large_left.collidepoint(m_pos) or btn_large_right.collidepoint(m_pos) or btn_pause_toggle.collidepoint(m_pos)
        elif state == FINAL_SCREEN: clickable = btn_final_menu.collidepoint(m_pos) or btn_final_exit.collidepoint(m_pos)
        elif state in [THOUGHT, CERTIFICATE, PORTFOLIO, END, CREDITS]: clickable = True
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND if clickable else pygame.SYSTEM_CURSOR_ARROW)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: running = False
            tasto_premuto = pygame.mouse.get_pressed()
            if event.type == pygame.MOUSEBUTTONUP:
                trascinando_volume = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                tasto_premuto = pygame.mouse.get_pressed()
            if tasto_premuto[0] and state == SETTINGS:
                bar_rect = pygame.Rect((L_VIRTUAL - 400) // 2, 315, 400, 20)
                if bar_rect.collidepoint(m_pos):
                    volume_audio = (m_pos[0] - bar_rect.x) / bar_rect.width
                    volume_audio = max(0.0, min(1.0, volume_audio))
                    if musica_attiva:
                        pygame.mixer.music.set_volume(volume_audio)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if state == MENU:
                    if btn_start_game.collidepoint(m_pos): state = SLOTS
                    elif btn_exit_game.collidepoint(m_pos): running = False
                    elif btn_lang_menu_it.collidepoint(m_pos): lingua_selezionata = "it"
                    elif btn_lang_menu_en.collidepoint(m_pos): lingua_selezionata = "en"
                    elif btn_lang_menu_es.collidepoint(m_pos): lingua_selezionata = "es"
                
                elif state == SLOTS:
                    gestito = False
                    if btn_back_slots.collidepoint(m_pos): state = MENU; gestito = True
                    if not gestito and confirma_elimina != -1:
                        if btn_si_elimina[confirma_elimina].collidepoint(m_pos):
                            if os.path.exists(percorsi_save[confirma_elimina]): os.remove(percorsi_save[confirma_elimina])
                            confirma_elimina = -1; gestito = True
                        elif btn_no_elimina[confirma_elimina].collidepoint(m_pos): confirma_elimina = -1; gestito = True
                    if not gestito:
                        for i, r_x in enumerate(elimina_rects):
                            if r_x.collidepoint(m_pos) and os.path.exists(percorsi_save[i]): confirma_elimina = i; gestito = True; break
                    if not gestito:
                        for i, r in enumerate(slots_rects):
                            if r.collidepoint(m_pos):
                                if not carica_dati(i): reset_game(); slot_selezionato = i
                                if musica_attiva: pygame.mixer.music.fadeout(1500)
                                effetto_transizione(canvas, screen, clock, "OUT") 
                                state = RULES 
                                gestito = True
                
                elif state == RULES:
                    state = STUDY; gestisci_musica(percorso_home)
                    canvas.blit(sfondo, (0, 0))
                    effetto_transizione(canvas, screen, clock, "IN")

                elif state == STUDY:
                    if btn_pause_toggle.collidepoint(m_pos): 
                        previous_state = state; state = PAUSE; pygame.mixer.music.set_volume(0.0)
                    elif btn_zaino.collidepoint(m_pos) and attestati_raccolti: state = PORTFOLIO; pygame.mixer.music.pause()
                    elif pc_rect.collidepoint(m_pos): 
                        attiva_vibrazione(); char_index = 0
                        message_text = lang["pc_msg"]
                        pc_clicked, last_obj, state = True, "PC", THOUGHT
                    elif watch_rect.collidepoint(m_pos): 
                        attiva_vibrazione(); char_index = 0
                        message_text = lang["watch_msg"]
                        watch_clicked, last_obj, state = True, "WATCH", THOUGHT
                    elif books_rect.collidepoint(m_pos) and vittoria: 
                        attiva_vibrazione(); indice_racconto = 0; char_index = 0
                        message_text = lang["story0"]
                        books_clicked, last_obj, state = True, "BOOKS", THOUGHT
                        pygame.time.delay(200) 
                    elif phone_rect.collidepoint(m_pos) and pc_clicked and watch_clicked: 
                        attiva_vibrazione(); char_index = 0
                        message_text = lang["phone_msg"]
                        phone_clicked, last_obj, state = True, "PHONE", THOUGHT
                
                elif state == PAUSE:
                    if btn_resume.collidepoint(m_pos): 
                        state = previous_state
                        if musica_attiva: pygame.mixer.music.set_volume(volume_audio)
                    elif btn_restart.collidepoint(m_pos): reset_game(); state = STUDY; gestisci_musica(percorso_home)
                    elif btn_settings.collidepoint(m_pos):
                        previous_state = STUDY if previous_state == PAUSE else previous_state
                        state = SETTINGS
                    elif btn_back_menu.collidepoint(m_pos): reset_game()
                    elif btn_quit.collidepoint(m_pos): running = False
                
                elif state == SETTINGS:
                    bar_rect = pygame.Rect((L_VIRTUAL - 400) // 2, 315, 400, 20)
                    if bar_rect.collidepoint(m_pos):
                        trascinando_volume = True
                        volume_audio = (m_pos[0] - bar_rect.x) / bar_rect.width
                        volume_audio = max(0.0, min(1.0, volume_audio))
                        if musica_attiva: pygame.mixer.music.set_volume(volume_audio)
                    elif btn_toggle_music.collidepoint(m_pos): 
                        musica_attiva = not musica_attiva
                        if musica_attiva:
                            pygame.mixer.music.play(-1); pygame.mixer.music.set_volume(volume_audio)
                        else: pygame.mixer.music.stop()
                    elif btn_toggle_vibe.collidepoint(m_pos): 
                        vibrazione_attiva = not vibrazione_attiva
                    elif btn_back_from_settings.collidepoint(m_pos):
                        state = previous_state
                    elif btn_lang_it.collidepoint(m_pos):
                        lingua_selezionata = "it"
                        salva_dati()
                    elif btn_lang_en.collidepoint(m_pos):
                        lingua_selezionata = "en"
                        salva_dati()
                    elif btn_lang_es.collidepoint(m_pos):
                        lingua_selezionata = "es"
                        salva_dati()

                elif state == THOUGHT:
                        if last_obj == "BOOKS":
                            indice_racconto += 1
                            if indice_racconto <= 5: 
                                char_index = 0
                                message_text = lang[f"story{indice_racconto}"]
                            else: 
                                titolo_cert = lang["cert_final_title"]
                                corpo_cert = lang["cert_final_body"]
                                nome_att = lang["cert_final_name"]
                                if nome_att not in attestati_raccolti: attestati_raccolti.append(nome_att)
                                state = CERTIFICATE; last_obj = "FINAL_DONE" 
                        elif lang["system_update"] in message_text or lang["bonus_unlock"] in message_text: 
                            state = STUDY
                        elif last_obj == "PHONE": 
                            state, dialogue_step = DIALOGUE, 1; timer_inizio = pygame.time.get_ticks()
                        else: 
                            state, dialogue_step = DIALOGUE, ("PC_Q" if last_obj == "PC" else "WATCH_Q")
                            timer_inizio = pygame.time.get_ticks()
                
                elif state == CERTIFICATE:
                    salva_dati()
                    if last_obj == "FINAL_DONE": state = CREDITS
                    elif vittoria and not mostrato_avviso_bonus: 
                        attiva_vibrazione(); char_index = 0
                        message_text = lang["bonus_unlock"]
                        mostrato_avviso_bonus = True; state = THOUGHT
                    elif mostrato_certificato_p10 and not avviso_cellulare_mostrato: 
                        char_index = 0
                        message_text = lang["system_update"]
                        avviso_cellulare_mostrato = True; state = THOUGHT
                    else: state = STUDY

                elif state == FINAL_SCREEN:
                    if btn_final_menu.collidepoint(m_pos): reset_game()
                    elif btn_final_exit.collidepoint(m_pos): running = False 
                elif state == PORTFOLIO: state = STUDY; pygame.mixer.music.unpause()
                elif state == END: reset_game()
                elif state == CREDITS: state = FINAL_SCREEN 
                elif state == DIALOGUE:
                    if btn_pause_toggle.collidepoint(m_pos): previous_state = state; state = PAUSE; pygame.mixer.music.set_volume(0.0)
                    if dialogue_step == "PC_Q":
                        if btn_left.collidepoint(m_pos):
                            if watch_clicked and not mostrato_certificato_p10: 
                                mostrato_certificato_p10 = True
                                titolo_cert = lang["cert_p10_title"]
                                corpo_cert = lang["cert_p10_body"]
                                nome_att = lang["cert_p10_name"]
                                if nome_att not in attestati_raccolti: attestati_raccolti.append(nome_att)
                                state = CERTIFICATE
                            else: state = STUDY
                        elif btn_right.collidepoint(m_pos): 
                            char_index = 0
                            message_text, vittoria, state = lang["pc_wrong"], False, END
                            pygame.mixer.music.stop()
                    elif dialogue_step == "WATCH_Q":
                        if btn_left.collidepoint(m_pos):
                            if pc_clicked and not mostrato_certificato_p10: 
                                mostrato_certificato_p10 = True
                                titolo_cert = lang["cert_p10_title"]
                                corpo_cert = lang["cert_p10_body"]
                                nome_att = lang["cert_p10_name"]
                                if nome_att not in attestati_raccolti: attestati_raccolti.append(nome_att)
                                state = CERTIFICATE
                            else: state = STUDY
                        elif btn_right.collidepoint(m_pos): 
                            char_index = 0
                            message_text, vittoria, state = lang["watch_wrong"], False, END
                            pygame.mixer.music.stop()
                    elif dialogue_step == 1:
                        if btn_large_left.collidepoint(m_pos): dialogue_step = 2; timer_inizio = pygame.time.get_ticks()
                        elif btn_large_right.collidepoint(m_pos): 
                            char_index = 0
                            message_text, vittoria, state = lang["phone_q1_wrong"], False, END
                            pygame.mixer.music.stop()
                    elif dialogue_step == 2:
                        if btn_large_right.collidepoint(m_pos): dialogue_step = 3; timer_inizio = pygame.time.get_ticks()
                        elif btn_large_left.collidepoint(m_pos): 
                            char_index = 0
                            message_text, vittoria, state = lang["phone_q2_wrong"], False, END
                            pygame.mixer.music.stop()
                    elif dialogue_step == 3:
                        if btn_large_right.collidepoint(m_pos): 
                            vittoria = True
                            titolo_cert = lang["cert_p5_title"]
                            corpo_cert = lang["cert_p5_body"]
                            nome_att = lang["cert_p5_name"]
                            if nome_att not in attestati_raccolti: attestati_raccolti.append(nome_att)
                            state = CERTIFICATE
                        elif btn_large_left.collidepoint(m_pos): 
                            char_index = 0
                            message_text, vittoria, state = lang["phone_q3_wrong"], False, END
                            pygame.mixer.music.stop()

        # --- LOGICA TRASCINAMENTO (Fuori dal ciclo eventi) ---
        if trascinando_volume and state == SETTINGS:
            bar_rect = pygame.Rect((L_VIRTUAL - 400) // 2, 315, 400, 20)
            volume_audio = (m_pos[0] - bar_rect.x) / bar_rect.width
            volume_audio = max(0.0, min(1.0, volume_audio))
            if musica_attiva:
                pygame.mixer.music.set_volume(volume_audio)
        
        # --- RENDERING ---
        if state == MENU:
            overlay = pygame.Surface((L_VIRTUAL, A_VIRTUAL), pygame.SRCALPHA)
            overlay.fill((0,0,0,195))
            canvas.blit(overlay, (0,0))
            draw_text_centered(canvas, lang["game_title"], 150, GOLD, True, font_titolo)
            draw_text_centered(canvas, lang["game_subtitle"], 240, WHITE, False, font_vittoria)
            draw_text_centered(canvas, lang["intro"], 380, GRAY, False, font)
            draw_button(canvas, btn_start_game, lang["start"], m_pos)
            draw_button(canvas, btn_exit_game, lang["exit"], m_pos)
            
            # Pulsanti lingue nel menu
            draw_button(canvas, btn_lang_menu_it, "IT", m_pos, GREEN if lingua_selezionata=="it" else None)
            draw_button(canvas, btn_lang_menu_en, "EN", m_pos, GREEN if lingua_selezionata=="en" else None)
            draw_button(canvas, btn_lang_menu_es, "ES", m_pos, GREEN if lingua_selezionata=="es" else None)

        elif state == SLOTS:
            overlay = pygame.Surface((L_VIRTUAL, A_VIRTUAL), pygame.SRCALPHA)
            overlay.fill((0,0,0,230))
            canvas.blit(overlay, (0,0))
            draw_text_centered(canvas, lang["save_select"], 200, GOLD, True, font_titolo)
            for i, r in enumerate(slots_rects):
                ha_file = os.path.exists(percorsi_save[i])
                testo = lang["slot_empty"]
                if ha_file:
                    with open(percorsi_save[i], "r") as f:
                        d = json.load(f)
                        testo = f"{lang['slot']} {i+1} - {lang['certificates']}: {len(d.get('attestati', []))}"
                        if d.get("finito"): testo = f"{lang['completed']} " + testo
                draw_button(canvas, r, testo, m_pos)
                if confirma_elimina == i:
                    pygame.draw.rect(canvas, (40, 40, 40), (r.x + 80, r.y + 10, r.width - 90, r.height - 20), border_radius=10)
                    testo_avviso = font_small.render(lang["delete_confirm"], True, RED)
                    canvas.blit(testo_avviso, (r.x + 95, r.y + 32))
                    draw_button(canvas, btn_si_elimina[i], lang["yes"], m_pos, color_override=(0, 150, 0))
                    draw_button(canvas, btn_no_elimina[i], lang["no"], m_pos, color_override=(150, 0, 0))
                elif ha_file:
                    x_rect = elimina_rects[i]
                    pygame.draw.rect(canvas, (150, 0, 0), x_rect, border_radius=8)
                    txt_x = font_button.render("X", True, WHITE)
                    canvas.blit(txt_x, txt_x.get_rect(center=x_rect.center))
            draw_button(canvas, btn_back_slots, lang["back_menu"], m_pos)

        elif state == RULES:
            canvas.fill(BLACK) 
            pygame.draw.rect(canvas, GOLD, (250, 150, 1100, 600), 3, border_radius=15)
            draw_text_centered(canvas, lang["rules_title"], 200, GOLD, True)
            y_start = 260
            for i in range(1, 7):
                draw_text_centered(canvas, lang[f"rule{i}"], y_start + ((i-1)*65), WHITE, False)
            draw_text_centered(canvas, lang["rule_click"], y_start + 390, WHITE, False)

        elif state == STUDY:
            draw_interactive_object(canvas, pc_rect, m_pos)
            draw_interactive_object(canvas, watch_rect, m_pos)
            if vittoria: draw_interactive_object(canvas, books_rect, m_pos)
            if pc_clicked and watch_clicked: draw_interactive_object(canvas, phone_rect, m_pos)
            if pc_clicked: draw_checkmark(canvas, pc_rect)
            if watch_clicked: draw_checkmark(canvas, watch_rect)
            if vittoria: draw_checkmark(canvas, phone_rect) 
            if books_clicked: draw_checkmark(canvas, books_rect)
            draw_button(canvas, btn_pause_toggle, lang["pause"], m_pos)
            if attestati_raccolti: 
                draw_button(canvas, btn_zaino, f"📜 {lang['certificates']} ({len(attestati_raccolti)})", m_pos)

        elif state == DIALOGUE:
            pygame.draw.rect(canvas, DARK_BAR, (0, Y_FASCIA, L_VIRTUAL, ALTEZZA_FASCIA))
            rimanente = max(0, (TEMPO_RISPOSTA - (pygame.time.get_ticks() - timer_inizio)) // 1000)
            txt_timer = font_vittoria.render(f"{lang['time']} {rimanente}s", True, RED if rimanente < 4 else WHITE)
            canvas.blit(txt_timer, (30, 30))
            draw_button(canvas, btn_pause_toggle, lang["pause"], m_pos)
            
            if dialogue_step == "PC_Q":
                txt_main = lang["pc_question"]
                draw_button(canvas, btn_left, lang["pc_ans1"], m_pos)
                draw_button(canvas, btn_right, lang["pc_ans2"], m_pos)
            elif dialogue_step == "WATCH_Q":
                txt_main = lang["watch_question"]
                draw_button(canvas, btn_left, lang["watch_ans1"], m_pos)
                draw_button(canvas, btn_right, lang["watch_ans2"], m_pos)
            elif dialogue_step == 1:
                txt_main = lang["phone_q1"]
                draw_button(canvas, btn_large_left, lang["phone_q1_a1"], m_pos)
                draw_button(canvas, btn_large_right, lang["phone_q1_a2"], m_pos)
            elif dialogue_step == 2:
                txt_main = lang["phone_q2"]
                draw_button(canvas, btn_large_left, lang["phone_q2_a1"], m_pos)
                draw_button(canvas, btn_large_right, lang["phone_q2_a2"], m_pos)
            elif dialogue_step == 3:
                txt_main = lang["phone_q3"]
                draw_button(canvas, btn_large_left, lang["phone_q3_a1"], m_pos)
                draw_button(canvas, btn_large_right, lang["phone_q3_a2"], m_pos)
            
            for i, line in enumerate(txt_main.split('\n')): 
                canvas.blit(font.render(line, True, WHITE), (30, Y_FASCIA + 50 + (i * 35)))

        elif state == THOUGHT:
            overlay = pygame.Surface((L_VIRTUAL, A_VIRTUAL), pygame.SRCALPHA)
            overlay.fill((0,0,0,180))
            canvas.blit(overlay, (0,0))
            draw_text_centered(canvas, message_text, 400, WHITE)
            if last_obj == "BOOKS" and random.random() < 0.2:
                for _ in range(3):
                    gx = random.randint(-15, 15)
                    gy = random.randint(0, A_VIRTUAL - 50)
                    gw = L_VIRTUAL
                    gh = random.randint(5, 35)
                    try:
                        glitch_strip = canvas.subsurface((0, gy, gw, gh)).copy()
                        canvas.blit(glitch_strip, (gx, gy))
                        if random.random() < 0.3: 
                            pygame.draw.rect(canvas, (random.randint(50,255), 0, 0, 80), (0, gy, gw, gh), special_flags=pygame.BLEND_ADD)
                    except: pass

        elif state == CERTIFICATE:
            overlay = pygame.Surface((L_VIRTUAL, A_VIRTUAL), pygame.SRCALPHA)
            overlay.fill((0,0,0,240))
            canvas.blit(overlay, (0,0))
            pygame.draw.rect(canvas, GOLD, (300, 200, 1000, 450), 4, border_radius=15)
            draw_text_centered(canvas, titolo_cert, 250, GOLD, True, font_cert)
            draw_text_centered(canvas, corpo_cert, 400, WHITE)
        
        elif state == PAUSE:
            overlay = pygame.Surface((L_VIRTUAL, A_VIRTUAL), pygame.SRCALPHA)
            overlay.fill((0,0,0,200))
            canvas.blit(overlay, (0,0))
            draw_text_centered(canvas, lang["pause_title"], 120, WHITE, True)
            draw_button(canvas, btn_resume, lang["resume"], m_pos)
            draw_button(canvas, btn_restart, lang["restart"], m_pos)
            draw_button(canvas, btn_settings, lang["settings"], m_pos)
            draw_button(canvas, btn_back_menu, lang["menu"], m_pos)
            draw_button(canvas, btn_quit, lang["quit"], m_pos)
        
        elif state == SETTINGS:
            overlay = pygame.Surface((L_VIRTUAL, A_VIRTUAL), pygame.SRCALPHA)
            overlay.fill((0,0,0,230))
            canvas.blit(overlay, (0,0))
            draw_text_centered(canvas, lang["settings"], 120, GOLD, True, font_titolo)
            draw_text_centered(canvas, f"{lang['volume']} {int(volume_audio * 100)}%", 250, WHITE)
            bar_width, bar_height = 400, 20
            bar_x, bar_y = (L_VIRTUAL - bar_width) // 2, 315
            pygame.draw.rect(canvas, (60, 60, 60), (bar_x, bar_y, bar_width, bar_height), border_radius=10)
            pygame.draw.rect(canvas, COBALT_BLUE, (bar_x, bar_y, int(bar_width * volume_audio), bar_height), border_radius=10)
            pygame.draw.rect(canvas, WHITE, (bar_x, bar_y, bar_width, bar_height), 2, border_radius=10)
            pos_pallino = bar_x + int(bar_width * volume_audio)
            pygame.draw.circle(canvas, WHITE, (pos_pallino, bar_y + 10), 10)
            draw_button(canvas, btn_toggle_music, f"{lang['music']} {lang['on'] if musica_attiva else lang['off']}", m_pos)
            draw_button(canvas, btn_toggle_vibe, f"{lang['vibe']} {lang['yes'] if vibrazione_attiva else lang['no']}", m_pos)
            
            # Pulsanti lingue
            draw_text_centered(canvas, lang["lang_label"], 540, WHITE)
            draw_button(canvas, btn_lang_it, "ITALIANO", m_pos, GREEN if lingua_selezionata=="it" else None)
            draw_button(canvas, btn_lang_en, "ENGLISH", m_pos, GREEN if lingua_selezionata=="en" else None)
            draw_button(canvas, btn_lang_es, "ESPAÑOL", m_pos, GREEN if lingua_selezionata=="es" else None)
            
            draw_button(canvas, btn_back_from_settings, lang["back_game"], m_pos)

        elif state == FINAL_SCREEN:
            overlay = pygame.Surface((L_VIRTUAL, A_VIRTUAL), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 245))
            canvas.blit(overlay, (0, 0))
            draw_text_centered(canvas, lang["mission_complete"], 100, GOLD, True, font_titolo)
            draw_text_centered(canvas, lang["final_conclusion"], 220, WHITE)
            draw_text_centered(canvas, lang["certificates_obtained"], 380, GOLD, True)
            lista_finale = list(dict.fromkeys(attestati_raccolti))
            for i, a in enumerate(lista_finale):
                t_s = font.render(f"✓ {a}", True, GREEN)
                t_r = t_s.get_rect(center=(L_VIRTUAL // 2, 440 + (i * 45)))
                canvas.blit(t_s, t_r)
            draw_button(canvas, btn_final_menu, lang["main_menu"], m_pos)
            draw_button(canvas, btn_final_exit, lang["exit_game"], m_pos)
        
        elif state == PORTFOLIO:
            overlay = pygame.Surface((L_VIRTUAL, A_VIRTUAL), pygame.SRCALPHA)
            overlay.fill((0,0,0,230))
            canvas.blit(overlay, (0,0))
            draw_text_centered(canvas, lang["your_certificates"], 150, GOLD, True)
            lista_port = list(dict.fromkeys(attestati_raccolti))
            for i, a in enumerate(lista_port): 
                draw_text_centered(canvas, f"📜 {a}", 300 + (i*80), WHITE)
        
        elif state == END:
            overlay = pygame.Surface((L_VIRTUAL, A_VIRTUAL), pygame.SRCALPHA)
            overlay.fill((0,0,0,200))
            canvas.blit(overlay, (0,0))
            draw_text_centered(canvas, message_text, 400, RED, True)
            draw_text_centered(canvas, lang["click_menu"], 650, WHITE)
        
        elif state == CREDITS:
            overlay = pygame.Surface((L_VIRTUAL, A_VIRTUAL), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 255))
            canvas.blit(overlay, (0, 0))
            testo_credits = lang["credits"]
            for i, linea in enumerate(testo_credits):
                t_s = font_vittoria.render(linea, True, GOLD if i == 0 else WHITE)
                t_r = t_s.get_rect(center=(L_VIRTUAL // 2, y_credits + (i * 60)))
                canvas.blit(t_s, t_r)
            y_credits -= 2 
            if y_credits < -(len(testo_credits) * 60): state = FINAL_SCREEN 

        screen.blit(pygame.transform.smoothscale(canvas, (real_w, real_h)), (0, 0))
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
    sys.exit()

if __name__ == "__main__": 
    main()
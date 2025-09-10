# historia_corrigida.py
from openal import oalOpen, oalQuit

def pause():
    # Pausa para imitar los cin.get() del codigo original
    try:
        input()
    except EOFError:
        pass

class SoundManager:
    def __init__(self):
        self.sounds = {}

    def load_sound(self, name, filepath):
        try:
            sound = oalOpen(filepath)
            if sound:
                self.sounds[name] = sound
            else:
                print(f"Error al cargar: {filepath}")
        except Exception as e:
            print(f"Error cargando {filepath}: {e}")

    def play(self, name):
        if name in self.sounds:
            self.sounds[name].play()
        else:
            print(f"Sonido '{name}' no encontrado")




class Character:
    def __init__(self, name: str,  sound=None):
        self.name = name
        self.sound = sound

    def speak(self, message: str):
        print(f"{message}")
        pause()


class Girl(Character):
    def __init__(self, name: str,sound):
        super().__init__(name,sound)
        self.clues = []
        self.inventory = []  # se mantiene pero no es requerida por la logica

    def talk_to_mom(self):
        message = (
            "Hija, si nunca regreso... debes descubrir la verdad y desenterrar todos los secretos."
        )
        self.clues.append("Advertencia de mama")
        self.sound.play("eco")
        #print("[Sonido misterioso que hace eco]")
        pause()
        self.speak(message)

    def talk_to_dad(self):
        message = (
            "Mi chica guerrera, todo estara bien, volveremos en una semana. "
            "Recuerda, si tienes problemas, piensa en tus padres 9735 veces... Te quiero."
        )
        self.clues.append("Codigo del padre: 9735")
        self.sound.play("thunder")
        #print("[Truenos en la distancia]")
        pause()
        self.speak(message)


class Orphanage:
    def __init__(self, name: str,sound=None):
        self.name = name
        self.sound = sound

    def entrance(self):
        print(f"Llegas al orfanato {self.name}. Es sombrio pero algo familiar...")
        self.sound.play("door")
        #print("[Las puertas se cierran con un chirrido aterrador]")
        pause()


class Madam(Character):
    def react(self, choice: str):
        if choice == "1":
            self.speak("No te abandonaron? JAJAJA!")
        elif choice == "2":
            self.speak("A tu habitacion, ahora. Debes acomodarte.")
            print("[Sonido espeluznante]")
            pause()


class Game:
    def __init__(self):

         # --- Inicializar sonidos ---
        self.sound = SoundManager()
        self.sound.load_sound("eco", "eco.wav")
        self.sound.load_sound("thunder", "thunder.wav")
        self.sound.load_sound("door", "door.wav")
        self.sound.load_sound("terrifier", "night.wav")
        self.sound.load_sound("vals", "vals.wav")
        self.sound.load_sound("wind", "wind.wav")
        self.sound.load_sound("morning","morning.wav")
        self.sound.load_sound("nature","nature.wav")
        self.sound.load_sound("nature_left","nature_left.wav")
        self.sound.load_sound("nature_right","nature_right.wav")
        self.sound.load_sound("fall","fall.wav")
        self.sound.load_sound("cut","cut.wav")
        self.sound.load_sound("burn","burn.wav")
        self.sound.load_sound("get","get.wav")
        self.sound.load_sound("wrong","wrong.wav")
        self.sound.load_sound("bloq", "bloq.wav")
        self.sound.load_sound("walk","walk.wav")
        self.sound.load_sound("init","intit.wav")
        self.sound.load_sound("to_realize","realize.wav")
        self.sound.load_sound("birds","birds.wav")
        self.sound.load_sound("kill_girl","kill_girl.wav")
        self.sound.load_sound("kill_madam","kill_madam.wav")
        self.sound.load_sound("stairs","stairs.wav")
        self.sound.load_sound("box","box.wav")
        self.sound.load_sound("atic","atic.wav")
        self.sound.load_sound("atic_right","atic_right.wav")
        self.sound.load_sound("atic_left","atic_left.wav")
        self.sound.load_sound("light","light.wav")
        self.sound.load_sound("sad","sad.wav")
        self.sound.load_sound("think","think.wav")
        self.sound.load_sound("scream","scream.wav")
        self.sound.load_sound("cold","cold.wav")
        self.sound.load_sound("run","run.wav")
        self.sound.load_sound("win","win.wav")
        self.sound.load_sound("lose","lose.wav")
        self.sound.load_sound("voice","voice.wav")
        self.sound.load_sound("discover","discover.wav")


        self.girl = Girl("Chica", self.sound)
        self.madam = Madam("Madam Rolinda")
        self.orphanage = Orphanage("Sinterac", self.sound)
        self.visited_places = set()  # se agregan SOLO cuando el lugar queda completo

    def start(self):
        self.sound.play("init")
        print("--- HISTORIA INTERACTIVA: EL ORFANATO SINTERAC ---")
        pause()
        print(
            "Tenias una familia muy unida, se divertian casi todo el tiempo, y les gustaba escuchar musica y leer libros de terror\n"
            "pero en un momento tus padres te dijeron que se debian ir a un viaje de trabajo,\n"
            "aunque no mencionaron el donde....."
        )
        pause()
        print("Antes de dejarte, tus padres hablan...")
        pause()

        # Padres
        self.girl.talk_to_mom()
        self.girl.talk_to_dad()

        print("Tus padres nunca regresaron...")
        self.sound.play("wind")
        self.sound.play("thunder")
        
        #print("[Sonido de terror, relampagos]")
        pause()
        print("Tiempo despues de la desaparicion de tus padres, eres llevada a un Orfanato\n")
        pause()
        print("\nEL ORFANATO SINTERAC")
        print("        |>>>     |>>>     |>>>        ")
        print("        |        |        |           ")
        print("     ___|___  ___|___  ___|___        ")
        print("    |       ||       ||       |       ")
        print("    |       ||       ||       |       ")
        print("    |   []  ||   []  ||  []   |       ")
        print("    |       ||       ||       |       ")
        print("    |_______||_______||_______|       ")
        print("        |               |             ")
        print("        |      ___      |             ")
        print("        |     |   |     |             ")
        print("        |     |   |     |             ")
        print("        |_____|___|_____|             ")
        # Entrada
        self.orphanage.entrance()

        print('\nAparece Madam Rolinda y te dice desde la escalera.\nOtra bestia abandonada...\n\n')

        print("   /////////////\\\\  ")
        print("  (((((((((((((( \\\\ ")
        print("  ))) ~~      ~~  ((( ")
        print("  ((( (*)     (*) ))) ")
        print("  )))     <       ((( ")
        print("  (((   _______   ))) ")
        print("  ))\\ _________ //(( ")
        print("\nOpciones:\n1) No me abandonaron\n2) Tirar las cosas con enojo")
        choice = input("Elige (1 o 2): ").strip().lower()
        if choice not in {"1", "2"}:
            print("Opcion no valida, la opcion por defecto es 1")
            choice = "1"
        self.madam.react(choice)

        print("\nLa chica llega a su habitacion... pero algo no esta bien...")
        self.sound.play("terrifier")
        print("[Un gigante le cubre la cara con un trapo blanco]")
        #print("[Musica: pam pam pa pa pam pam pa pa... tiruriru]")
        pause()

        print("\n------ A la manana siguiente ------\n")
        self.sound.play("morning")
        pause()
        self.exploration()

    def garden(self):
        """
        Completa cuando recorres los dos lados.
        """
        walk = set()
        self.sound.play("walk")
        print("\nComienzas a caminar")
        self.sound.play("nature")
        print("Mientras caminas logras ver diferentes pajaros y arboles, pareciera que ya no estuvieras en ese espantoso lugar")
        while len(walk) != 2:
            selection = input(
                "De repente te encuentras en un sendero\nTe gustaria explorar el lado derecho o izquierdo: "
            ).strip().lower()

            if selection in {"derecho", "izquierdo"} and selection not in walk:
                walk.add(selection)
                if selection == "derecho":
                    self.sound.play("nature_right")
                    print("Ingresas por el lado derecho")
                    print("Mientras caminabas por ese sendero te encuentras con una fuente antigua y mohosa")
                    pause()
                    self.sound.play("discover")
                    print("Aunque el agua estaba muy turbia lograste ver algo...\nUNA BOTELLA?!")
                    pause()
                    print("Al sacarla ves un aparato tecnologico dentro de ella\nLuce intacto...")
                    pause()
                    print("\nEl aparato te permite ver cosas que antes no podias, ahora observas palabras en los arboles, frases en el agua y logras detectar senderos secretos\nTe emocionas ")
                    pause()
                    explore = input("\nContinuar con contexto del aparato? o seguir explorando?\nSeleccion: ").strip().lower()
                    if explore == "continuar":
                        self.sound.play("to_realize")
                        print("Te das cuenta que la tecnologia que tienes en tus manos, era usada para misiones secretas de espias\ny poder darse mensajes sin que alguien se diera cuenta")
                        print("Decides mantener en secreto ese aparato hasta que deba ser util")
                        self.sound.play("get")
                        print("\nAparato Guardado en el Inventario\n")
                        
                        self.girl.clues.append("aparato")
                        pause()
                        print("Sales del sendero derecho")
                        pause()
                    elif explore == "seguir explorando":
                        self.sound.play("get")
                        print("\nAparato Guardado en el Inventario\n")
                        
                        self.girl.clues.append("aparato")
                        pause()
                        print("Sales del sendero derecho")
                        pause()
                    else:
                        self.sound.play("get")
                        print("\nAparato Guardado en el Inventario\n")
                        
                        self.girl.clues.append("aparato")
                        pause()
                        print("Sales del sendero derecho")
                        pause()

                elif selection == "izquierdo":
                    self.sound.play("nature_left")
                    print("Ingresas por el lado izquierdo")
                    print("Mientras caminabas por ese sendero te encuentras con gran rosal, pero no es un rosal cualquiera,\nsus rosas son de color negro")
                    pause()
                    print("Al prestar atencion, logras ver que hay 3 flores con 3 llaves distintas")
                    pause()
                    print(
                        "\nLlave A: Brilla como el oro, pero pesa como el plomo.\n"
                        "Llave B: Es opaca y fria, pero fue forjada en fuego.\n"
                        "Llave C: Parece fragil, pero ha abierto mas puertas de las que puedes contar.\n"
                    )
                    print("La llave correcta no es la mas brillante, ni la mas reciente. La verdad esta en la experiencia, no en la apariencia.")
                    pause()
                    select = ""
                    while select != "c":
                        print(f"sel = {select}")
                        select = input("Que llave eliges, A, B o C?: ").strip().lower()
                        if select == "a":
                            print("Al tocar la llave, una espina gigante te atraviesa el dedo y la llave dorada y pesada cae sobre tu pie descalzo")
                            self.sound.play("cut")
                            self.sound.play("fall")
                            pause()
                            self.sound.play("voice")
                            print("Una voz terrorifica te dice: Vuelve a intentar")
                            pause()
                        elif select == "b":
                            self.sound.play("burn")
                            print("Al tocar la llave, te quemas la mano, como si hubieras tocado la lava de un volcan")
                            pause()
                            self.sound.play("voice")
                            print("Una voz terrorifica te dice: Vuelve a intentar")
                            
                            pause()
                        elif select == "c":
                            self.sound.play("birds")
                            print("Al tocar la llave, una manada de pajaros protectores se dispersa y se alejan del lugar")
                            pause()
                            print("Te dices a tus adentros: Definitivamente es la llave correcta")
                            self.sound.play("get")
                            self.girl.clues.append("llave")
                            pause()
                        else:
                            print("Opcion no valida")
                            self.sound.play("wrong")
                            pause()
            elif selection in walk:
                print("Ya buscaste en esta zona, trata con la otra")
                self.sound.play("wrong")
                pause()
            else:
                print("La seleccion es incorrecta, intenta de nuevo")
                self.sound.play("wrong")
                pause()

        print("Terminaste de explorar el jardin\nBuen trabajo\n")
        self.sound.play("get")
        return True  

    def attic(self):
        """
        Completa SOLO cuando se abren la caja fuerte (codigo 9735) y la puerta con el collar.
        """
        walkA = []
        self.sound.play("stairs")
        print("\nSubes las escaleras chirriantes hacia el atico...")
        pause()
        self.sound.play("cold")
        print("[El aire cada vez se hace mas frio]")
        pause()
        print("Al subir, ves un desastre total, desde hace anios nadie ha entrado aqui, o eso parece\n")
        self.sound.play("to_realize")
        print("ESPERA... ves algo raro en el suelo\nte das cuenta de que aunque todo esta polvoriento, hay 3 zonas que estan sin polvo, como si alguien hubiese estado ahi\n")
        pause()
        print("Decides investigar esas zonas")
        while len(walkA) != 3:
            print("Que zona quieres investigar? Izquierda, Centro o Derecha: ")
            choice = input().strip().lower()
            if choice in walkA:
                self.sound.play("bloq")
                print("Ya investigaste esa zona, intenta con otra")
                pause()
            elif choice == "izquierda":
                self.sound.play("atic_left")
                print("Caminas por la zona izquierda")
                print("De entre todas la cosas que estan de ese lado, como libros, ropa vieja y cajas, ves una terrorifica porcelana que te observa fijamente")
                pause()
                print("Al  acercarte, ves que la porcelana tiene un collar con una insignia que parece ser la del orfanato Sinterac")
                pause()
                print("Decides guardar el collar en tu inventario? (si/no)")
                select = input().strip().lower()
                if select == "si":
                    print("Guardaste el collar en tu inventario")
                    self.sound.play("get")
                    if "collar" not in self.girl.clues:
                        self.girl.clues.append("collar")
                    walkA.append("izquierda")
                else:
                    print("No guardaste el collar en tu inventario")
                    self.sound.play("wrong")
                pause()
            elif choice == "centro":
                self.sound.play("atic")
                walkA.append("centro")
                print("Caminas por la zona del centro")
                print("De entre todas la cosas que estan de ese lado, ves un libro que llama tu atencion")
                pause()
                print("Al  acercarte, ves que el libro tiene una portada con un dibujo de un arbol y una casa")
                pause()
                print("\nAl abrirlo, ves que es un libro tipo diario, no logras entender las primeras paginas ya que estan desgastadas, pero\n mientras continuas leyendo, te percadas de una nota que esta intacta")
                pause()
                print("NO CONFIES EN MADAM ROLINDA, ELLA NO ES QUIEN DICE SER")
                pause()
                print("Bajo ese mensaje hay una firma, parece ser de ? tuya ?")
                print("tambien ves que bajo eso hay un dibujo muy detallado de una puerta en donde la llave es un amuleto\n")
                print("Decides guardar el libro en tu inventario? (si/no)")
                select = input().strip().lower()
                if select == "si":
                    print("Guardaste el libro en tu inventario")
                    self.sound.play("get")
                    if "libro" not in self.girl.clues:
                        self.girl.clues.append("libro")
                else:
                    print("No guardaste el libro en tu inventario")
                    self.sound.play("wrong")
                pause()
            elif choice == "derecha":
                self.sound.play("atic_right")
                print("Caminas por la zona derecha")
                print("De entre todas la cosas que estan de ese lado, ves una caja fuerte antigua")
                pause()
                print("Al  acercarte, ves que la caja tiene un grabado con un dibujo de un arbol y una casa, igual que el libro del centro")
                pause()
                self.sound.play("bloq")
                print("Intentas abrir la caja fuerte, pero esta cerrada con un codigo numerico de 4 digitos")
                pause()
                select = ""
                while select != "9735":
                    print("Recuerdas que tu padre te dijo algo sobre un numero secreto:\nDigita el codigo: ")
                    select = input().strip().lower()
                    if select == "9735":
                        print("Ingresaste el codigo 9735")
                        self.sound.play("box")
                        print("La caja se abre con un chirrido...")
                        pause()
                        print("Dentro encuentras una fotografia")
                        pause()
                        print("La fotografia es del atico, pero algo no cuadra, ya que en la foto hay una puerta antigua que ahora no puedes ver")
                        print("Buscas la puerta en el atico, pero no la encuentras\nHasta que ves una pared que parece diferente\ny en ella hay un hueco con la forma de un amuleto")
                        print("ESA SI ES LA PUERTA DEL DIBUJO")
                        print("Decides guardar la fotografia en tu inventario? (si/no)")
                        myChoice = input().strip().lower()
                        if myChoice == "si":
                            print("Guardaste la fotografia en tu inventario")
                            self.sound.play("get")
                            if "fotografia" not in self.girl.clues:
                                self.girl.clues.append("fotografia")
                        else:
                            print("No guardaste la fotografia en tu inventario")
                            self.sound.play("wrong")
                        print("Quieres abrir la puerta? (si/no)")
                        myChoice = input().strip().lower()
                        if myChoice == "si" and "collar" in self.girl.clues:
                            walkA.append("derecha")
                            print("Usas el collar para abrir la puerta\nLa puerta se abre con un chirrido...")
                            pause()
                            print("Al entrar, ves no solo un cuarto...\n")
                            pause()
                            self.sound.play("to_realize")
                            print("ES UNA PRISION !")
                            print("Ves a varias personas encerradas, algunas son apenas unos chicos, pero otras ya son adultos\nLas personas no estan bien...\nEstan heridas como si hubiesen sido torturadas\n")
                            pause()
                            print("Temblando decides salir de ese lugar\n")
                        elif myChoice == "si" and "collar" not in self.girl.clues:
                            print("Por el momento no tienes el amuleto, buscalo en la zona izquierda")
                            self.sound.play("bloq")
                            pause()
                        else:
                            print("Decides no abrir la puerta por ahora")
                            self.sound.play("bloq")
                            pause()
                    else:
                        print("El codigo es incorrecto, vuelve a intentar")
                        self.sound.play("wrong")
                        pause()
            else:
                print("No ubicas esa zona. Usa: izquierda, centro o derecha.")
                self.sound.play("wrong")
                pause()

        # atico completo
        return True

    def basement(self):
        """
        Completa SOLO si abres el cofre con la llave (clue 'llave').
        Permite bajar sin llave y regresar luego.
        """
        print("\nBajas al Oscuro Sotano\n")
        print("Para iluminarlo tienes dos opciones:\n1) Prender Vela\n2) Prender Linterna")
        sel = input("Selecciona tu fuente de luz: ").strip().lower()

        if sel == "1":
            self.sound.play("light")
            print("\nEnciendes la blanca vela\n")
        elif sel == "2":
            self.sound.play("light")
            print("\nEncendiste la linterna\n")

        print("Al bajar te encuentras que ademas de calentador, tambien hay varias cajas en este lugar\npero te llama la atencion una en especifico\n\n------ VAS A MIRAR ------\n\n")
        print("La caja en realidad es un cofre que necesita llave")
        print("Abrir el Cofre? (si/no)")
        select2 = input().strip().lower()
        if select2 == "si":
            if "llave" in self.girl.clues:
                self.sound.play("box")
                print("\n[El cofre se abre con un chirrido...]")
                self.sound.play("think")
                print("Encuentras muchos papeles viejos y amarillentos...")
                print("\nDos de ellos llaman tu atencion:")
                pause()
                print("\n1. Un papel doblado cuidadosamente que dice:")
                print("'El numero secreto que nunca debes olvidar: 9735'")
                print("[Este debe ser el numero que papa menciono...]")
                if "Numero secreto confirmado" not in self.girl.clues:
                    self.girl.clues.append("Numero secreto confirmado")
                pause()
                print("\n2. Una fotografia...")
                self.sound.play("sad")
                print("[Tus manos tiemblan al verla]")
                print("En la imagen estan tus padres... sonriendo junto a Madam Rolinda")
                print("La fecha en el reverso es de hace 15 años")
                if "Foto misteriosa con Madam Rolinda" not in self.girl.clues:
                    self.girl.clues.append("Foto misteriosa con Madam Rolinda")
                pause()
                return True  # sotano completo
            else:
                print("\n[El cofre no se abre...]")
                self.sound.play("bloq")
                print("Necesitas encontrar una llave dorada")
                print("Tal vez deberias explorar el jardin primero...")
                pause()
                return False
        else:
            print("Decides no abrir el cofre por ahora.")
            self.sound.play("bloq")
            pause()
            return False

    def exploration(self):
        # Termina naturalmente cuando las 4 zonas queden completas (sin break/continue)
        while len(self.visited_places) < 4:
            self.sound.play("think")
            print("Cuando despiertas decides explorar el lugar...")
            print("Que va a explorar:\n1) Patio\n2) Salon principal\n3) Sotano\n4) Atico\n5) Revisar pistas")
            place = input("Selecciona el lugar: ").strip().lower()

            if place == "1":
                if "patio" not in self.visited_places:
                    patio_done = self.garden()
                    if patio_done:
                        self.visited_places.add("patio")
                else:
                    print("Ese lugar ya fue explorado.")
                    self.sound.play("wrong")
                    pause()

            elif place == "2":
                if "salon" not in self.visited_places:
                    self.sound.play("vals")
                    print("Exploras el salon principal.")
                    print("Ves un retrato de una familia, y en el marco esta tallada la fecha de la desaparicion de tus padres.")
                    input()
                    print("Sientes un nudo en la garganta")
                    input()
                    print("desearias que nunca hubieran ido a ese viaje")
                    self.girl.clues.append("Retrato con fecha misteriosa")
                    self.visited_places.add("salon")
                    pause()
                else:
                    print("Ese lugar ya fue explorado.")
                    self.sound.play("wrong")
                    pause()

            elif place == "3":
                # Permite multiples entradas hasta completarlo
                sotano_done = self.basement()
                if sotano_done:
                    self.visited_places.add("sotano")

            elif place == "4":
                # Permite multiples entradas hasta completarlo
                if "atico" not in self.visited_places:
                    atico_done = self.attic()
                    if atico_done:
                        self.visited_places.add("atico")
                else:
                    print("Ese lugar ya fue explorado.")
                    self.sound.play("wrong")
                    pause()

            elif place == "5":
                self.sound.play("think")
                print("Tus pistas actuales:")
                for clue in self.girl.clues:
                    print(f"- {clue}")
                pause()
            else:
                print("Ese lugar ya fue explorado o no existe.")
                self.sound.play("wrong")
                pause()

        self.ending()

    def ending(self):
        print("--- EL DESCUBRIMIENTO ---")
        pause()
        self.sound.play("think")
        print("Con las pistas que encontraste, empiezas a unir las piezas...")
        for clue in self.girl.clues:
            print(f"- {clue}")
            pause()
        self.sound.play("box")
        print("El numero 9735 abre la caja del sotano. Dentro encuentras un diario polvoriento.")
        print("Tus manos tiemblan mientras lo lees...")
        pause()
        self.sound.play("true")
        print("El diario revela la verdad: Madam Rolinda trabajo como ninera de tus padres...\n")
        print("Ella los traiciono, entregandolos a sus enemigos y asegurando su muerte.")
        print("Ahora lo sabes... el orfanato es una trampa, y Rolinda es la asesina.")
        self.sound.play("scream")
        print("[Truenos y un grito lejano resuenan por los pasillos]\n")
        pause()

        print("Que haras ahora?")
        print("1) Enfrentar a Madam Rolinda  2) Intentar huir del orfanato")
        decision = input("Elige (1 o 2): ").strip().lower()

        if decision == "1":
            self.sound.play("box")
            print("Con la llave oxidada del atico, abres un viejo cofre y encuentras un cuchillo.")
            print("Esperas a Rolinda en la oscuridad... y cuando aparece, atacas con furia.")
            self.sound.play("kill_madam")
            print("[Gritos llenan el orfanato]")
            pause()
            self.sound.play("win")
            print("La nina ha vencido. Rolinda yace muerta. El secreto de sus padres ha sido vengado.")
            print("--- FINAL: LA NINA SE CONVIERTE EN SU PROPIA GUERRERA ---")
        else:
            self.sound.play("run")
            print("Corres hacia la salida, pero las puertas se cierran con violencia.")
            print("Rolinda aparece detras de ti, riendo de forma escalofriante.")
            print("No hay escape...")
            pause()
            self.sound.play("kill_girl")
            print("[Un grito final resuena en el orfanato]")
            self.sound.play("lose")
            print("--- FINAL: MADAM ROLINDA ACABO CON LA NINA ---")



Game().start()

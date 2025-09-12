from soundManager import SoundManager, pause
from characters import Girl, Madam, Orphanage
from places import garden, attic, basement


class Game:
    def __init__(self):
        # --- Inicializar sonidos ---
        self.sound = SoundManager()
        self.sound.load_sound("eco", "sounds/eco.wav")
        self.sound.load_sound("thunder", "sounds/thunder.wav")
        self.sound.load_sound("door", "sounds/door.wav")
        self.sound.load_sound("door2", "sounds/door2.wav")
        self.sound.load_sound("terrifier", "sounds/night.wav")
        self.sound.load_sound("vals", "sounds/vals.wav")
        self.sound.load_sound("wind", "sounds/wind.wav")
        self.sound.load_sound("morning","sounds/morning.wav")
        self.sound.load_sound("nature","sounds/nature.wav")
        self.sound.load_sound("nature_left","sounds/nature_left.wav")
        self.sound.load_sound("nature_right","sounds/nature_right.wav")
        self.sound.load_sound("fall","sounds/fall.wav")
        self.sound.load_sound("cut","sounds/cut.wav")
        self.sound.load_sound("burn","sounds/burn.wav")
        self.sound.load_sound("get","sounds/get.wav")
        self.sound.load_sound("wrong","sounds/wrong.wav")
        self.sound.load_sound("bloq", "sounds/bloq.wav")
        self.sound.load_sound("walk","sounds/walk.wav")
        self.sound.load_sound("init","sounds/init.wav")
        self.sound.load_sound("to_realize","sounds/realize.wav")
        self.sound.load_sound("birds","sounds/birds.wav")
        self.sound.load_sound("kill_girl","sounds/kill_girl.wav")
        self.sound.load_sound("kill_madam","sounds/kill_madam.wav")
        self.sound.load_sound("stairs","sounds/stairs.wav")
        self.sound.load_sound("box","sounds/box.wav")
        self.sound.load_sound("atic","sounds/atic.wav")
        self.sound.load_sound("atic_right","sounds/atic_right.wav")
        self.sound.load_sound("atic_left","sounds/atic_left.wav")
        self.sound.load_sound("light","sounds/light.wav")
        self.sound.load_sound("sad","sounds/sad.wav")
        self.sound.load_sound("think","sounds/think.wav")
        self.sound.load_sound("scream","sounds/scream.wav")
        self.sound.load_sound("cold","sounds/cold.wav")
        self.sound.load_sound("run","sounds/run.wav")
        self.sound.load_sound("win","sounds/win.wav")
        self.sound.load_sound("lose","sounds/lose.wav")
        self.sound.load_sound("voice","sounds/voice.wav")
        self.sound.load_sound("discover","sounds/discover.wav")
        self.sound.load_sound("true","sounds/true.wav")

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

        print("\n------ A la mañana siguiente ------\n")
        self.sound.play("morning")
        pause()
        self.exploration()




    def exploration(self):
        while len(self.visited_places) < 4:
            self.sound.play("think")
            print("Cuando despiertas decides explorar el lugar...")
            print("Que va a explorar:\n1) Patio\n2) Salon principal\n3) Sotano\n4) Atico\n5) Revisar pistas")
            place = input("Selecciona el lugar: ").strip().lower()

            if place == "1":
                if "patio" not in self.visited_places:
                    patio_done = garden(self)
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
                    self.sound.play("vals")
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
                sotano_done = basement(self)
                if sotano_done:
                    self.visited_places.add("sotano")

            elif place == "4":
                if "atico" not in self.visited_places:
                    atico_done = attic(self)
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
        pause()
        self.sound.play("scream")
        print("[Un grito lejano resuena por los pasillos]\n")
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
            pause()
            
            print("La nina ha vencido. Rolinda yace muerta. El secreto de sus padres ha sido vengado.")
            
            print("--- FINAL: LA NINA SE CONVIERTE EN SU PROPIA GUERRERA ---")
            
        else:
            self.sound.play("run")
            self.sound.play("kill_girl")
            
            print("Corres hacia la salida, pero las puertas se cierran con violencia.")
            print("Rolinda aparece detras de ti, riendo de forma escalofriante.")
            print("No hay escape...")
            pause()
            self.sound.play("lose")
            pause()
            
            print("[Un grito final resuena en el orfanato]")
            
            print("--- FINAL: MADAM ROLINDA ACABO CON LA NINA ---")



from soundManager import pause

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
                print("\nEl aparato te permite ver cosas que antes no podias, ahora observas palabras en los arboles, frases en el agua y logras detectar senderos secretos ")
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
                print("Mientras caminabas por ese sendero te encuentras con un gran rosal, pero no es un rosal cualquiera,\nsus rosas son de color negro")
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
    print("Al subir, ves un desastre total, desde hace años nadie ha entrado aqui, o eso parece\n")
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
            print("Bajo ese mensaje hay una firma, parece ser ¿tuya ?")
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
                        self.sound.play("door2")
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

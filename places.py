import json

class Place:
    def __init__(self, game):
        self.game = game 
        with open("places.json", "r", encoding="utf-8") as f:
            self.places_narr = json.load(f)

    def showJ(self, key: str):
        seq = self.places_narr.get(key, [])
        for text in seq:
            sname = text.get("sound")
            if sname:
                self.game.sound.play(sname)

            if "lines" in text:
                print("\n".join(text["lines"]))
                input()
                continue

            if "say" in text:
                print(text["say"])
                if text.get("pause", True):
                    input()



class Garden(Place):
    def run(self):
        s = self.game.sound
        girl = self.game.girl
        self.showJ("gardenStart")

        walk = set()
        while len(walk) != 2:
            selection = input(
                "De repente te encuentras en un sendero\nTe gustaria explorar el lado derecho o izquierdo: "
            ).strip().lower()

            if selection in {"derecho", "izquierdo"} and selection not in walk:
                walk.add(selection)

                if selection == "derecho":
                    self.showJ("gardenRightIntro")
                    explore = input("\nContinuar con contexto del aparato? o seguir explorando?\nSeleccion: ").strip().lower()
                    if explore == "continuar":
                        self.showJ("gardenRightContinuar")
                        girl.clues.append("aparato")
                        self.showJ("gardenRightEnd")
                    elif explore == "seguir explorando":
                        self.showJ("gardenRightSave")
                        girl.clues.append("aparato")
                        self.showJ("gardenRightEnd")
                    else:
                        self.showJ("gardenRightSave")
                        girl.clues.append("aparato")
                        self.showJ("gardenRightEnd")

                elif selection == "izquierdo":
                    self.showJ("gardenLeftIntro")
                    select = ""
                    while select != "c":
                        select = input("Que llave eliges, A, B o C?: ").strip().lower()
                        if select == "a":
                            print("Al tocar la llave, esta se convierte en una daga y te atraviesa el dedo")
                            s.play("cut")
                            s.play("fall")
                            input()
                            s.play("voice")
                            print("El señor del holograma te dice: Vuelve a intentar")
                            input()
                        elif select == "b":
                            s.play("burn")
                            print("Al tocar la llave, te quemas la mano, como si hubieras tocado la lava de un volcan")
                            input()
                            s.play("voice")
                            print("El señor del holograma te dice: Vuelve a intentar")
                            input()
                        elif select == "c":
                            s.play("birds")
                            print("Al tocar la llave, una manada de pajaros protectores se dispersa y se alejan del lugar")
                            input()
                            print("Te dices a tus adentros: Definitivamente es la llave correcta")
                            s.play("get")
                            print("Agregas la llave a tu mochila")
                            girl.clues.append("llave")
                            input()
                        else:
                            print("Opcion no valida")
                            s.play("wrong")
                            input()

            elif selection in walk:
                print("Al tomar el objeto especial de la zona, una barrera se genera ante ella y ya no te permite entrar")
                print("Ya buscaste en esta zona, trata con la otra")
                s.play("wrong")
                input()
            else:
                print("La seleccion es incorrecta, intenta de nuevo")
                s.play("wrong")
                input()
        self.showJ("gardenEnd")
        return True

class Attic(Place):
    def run(self):
        s = self.game.sound
        girl = self.game.girl

        self.showJ("atticIntro")

        walkA = []
        while len(walkA) != 3:
            print("Que zona quieres investigar? Izquierda, Centro o Derecha: ")
            choice = input().strip().lower()

            if choice in walkA:
                s.play("bloq")
                print("Una barrera se genera ante ti y no te permite volver a la zona")
                print("Ya investigaste esa zona, intenta con otra")
                input()
                continue

            if choice == "izquierda":
                self.showJ("atticLeft")
                print("Decides guardar el collar en tu mochila? (si/no)")
                select = input().strip().lower()
                if select == "si":
                    print("Guardaste el collar en tu mochila")
                    s.play("get")
                    if "collar" not in girl.clues:
                        girl.clues.append("collar")
                    walkA.append("izquierda")
                else:
                    print("No guardaste el collar en tu mochila")
                input()

            elif choice == "centro":
                walkA.append("centro")
                self.showJ("atticCenterIntro")
                print("Decides guardar el libro en tu mochila? (si/no)")
                select = input().strip().lower()
                if select == "si":
                    print("Guardaste el libro en tu mochila")
                    s.play("get")
                    if "libro" not in girl.clues:
                        girl.clues.append("libro")
                else:
                    print("No guardaste el libro en tu mochila")
                input()

            elif choice == "derecha":
                self.showJ("atticRightIntro")

                select = ""
                while select != "9735":
                    print("Recuerdas que tu padre te dijo algo sobre un numero secreto:\nDigita el codigo: ")
                    select = input().strip().lower()
                    if select == "9735":
                        print("Ingresaste el codigo 9735")
                        s.play("box")
                        self.showJ("atticRight")

                        print("Decides guardar la fotografia en tu mochila? (si/no)")
                        myChoice = input().strip().lower()
                        if myChoice == "si":
                            print("Guardaste la fotografia en tu mochila")
                            s.play("get")
                            if "fotografia" not in girl.clues:
                                girl.clues.append("fotografia")
                        else:
                            print("No guardaste la fotografia en tu mochila")

                        print("Quieres abrir la puerta? (si/no)")
                        myChoice = input().strip().lower()
                        if myChoice == "si" and "collar" in girl.clues:

                            walkA.append("derecha")
                            self.showJ("atticSecretDoor")
                        elif myChoice == "si" and "collar" not in girl.clues:
                            print("[Por el momento no tienes el amuleto, buscalo en la zona izquierda]")
                            s.play("bloq")
                            input()
                        else:
                            print("Decides no abrir la puerta por ahora")
                            s.play("bloq")
                            input()
                    else:
                        print("La puerta te dice: ")
                        print("El codigo es incorrecto, vuelve a intentar")
                        s.play("wrong")
                        input()
            else:
                print("No ubicas esa zona. Usa: izquierda, centro o derecha.")
                input()

        return True


class Basement(Place):
    def run(self):
        s = self.game.sound
        girl = self.game.girl

        self.showJ("basementIntro")

        sel = input("Selecciona tu fuente de luz: ").strip().lower()
        if sel == "1":
            s.play("light")
            print("\nEnciendes la blanca vela\n[suena encendedor]")
        elif sel == "2":
            s.play("light")
            print("\nEncendiste la linterna\n[suena switch de linterna]")

        s.play("warm")
        print("Al bajar te encuentras que ademas de calentador, tambien hay varias cajas en este lugar\npero te llama la atencion una en especifico\n\n------ VAS A MIRAR ------\n\n")
        print("La caja en realidad es un cofre que necesita llave")
        print("Abrir el Cofre? (si/no)")
        select2 = input().strip().lower()

        if select2 == "si":
            s.play("warm2")
            if "llave" in girl.clues:
                self.showJ("basementOpen")
                if "Numero secreto confirmado" not in girl.clues:
                    girl.clues.append("Numero secreto confirmado")
                if "Foto misteriosa con Madam Rolinda" not in girl.clues:
                    girl.clues.append("Foto misteriosa con Madam Rolinda")
                return True
            else:
                print("\n[El cofre no se abre...]")
                s.play("bloq")
                print("[Necesitas encontrar una llave dorada]")
                print("[Tal vez deberias explorar el jardin primero...]")
                input()
                return False
        else:
            print("Decides no abrir el cofre por ahora.")
            input()
            return False

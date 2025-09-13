from soundManager import pause

class Character:
    def __init__(self, name: str, sound=None):
        self.name = name
        self.sound = sound

    def speak(self, message: str):
        print(f"{message}")
        input()


class Girl(Character):
    def __init__(self, name: str, sound):
        super().__init__(name, sound)
        self.clues = []
        self.inventory = []

    # Ahora el texto viene desde JSON (se pasa como argumento)
    def talk_to_mom(self, message: str):
        self.clues.append("Caja secreta")
        self.clues.append("Advertencia de mama")
        if self.sound:
            self.sound.play("eco")
        input()
        self.speak(message)

    # Ahora el texto viene desde JSON (se pasa como argumento)
    def talk_to_dad(self, message: str):
        self.clues.append("Codigo del padre: 9735")
        if self.sound:
            self.sound.play("thunder")
        input()
        self.speak(message)


class Orphanage:
    def __init__(self, name: str, sound=None):
        self.name = name
        self.sound = sound

    def entrance(self):
        print(f"Llegas al orfanato {self.name}. Es sombrio pero algo familiar...\nLa puerta de este se abre ante ti")
        if self.sound:
            self.sound.play("door")
        input()


class Madam(Character):
    # Respuesta se puede proveer desde JSON (dict opcional)
    def react(self, choice: str, lines: dict | None = None):
        if lines is not None:
            msg = lines.get(choice, lines.get("default", ""))
            if msg:
                self.speak(msg)
            # En tu versión original, para la opción 2 además imprime esta línea:
            if choice == "2":
                print("[Sonido espeluznante]")
                input()
            return

        # Fallback (por si alguien llama sin JSON)
        if choice == "1":
            self.speak("No te abandonaron? ")
        elif choice == "2":
            self.speak("A tu habitacion, ahora. Debes acomodarte.")
            print("[Sonido espeluznante]")
            input()

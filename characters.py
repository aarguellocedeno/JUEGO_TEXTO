from soundManager import pause

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
        self.inventory = []  

    def talk_to_mom(self):
        message = (
            "Hija, si nunca regreso... debes descubrir la verdad y desenterrar todos los secretos."
        )
        self.clues.append("Advertencia de mama")
        self.sound.play("eco")
        pause()
        self.speak(message)

    def talk_to_dad(self):
        message = (
            "Mi chica guerrera, todo estara bien, volveremos en una semana. "
            "Recuerda, si tienes problemas, piensa en tus padres 9735 veces... Te quiero."
        )
        self.clues.append("Codigo del padre: 9735")
        self.sound.play("thunder")
        pause()
        self.speak(message)


class Orphanage:
    def __init__(self, name: str,sound=None):
        self.name = name
        self.sound = sound

    def entrance(self):
        print(f"Llegas al orfanato {self.name}. Es sombrio pero algo familiar...")
        self.sound.play("door")
        pause()


class Madam(Character):
    def react(self, choice: str):
        if choice == "1":
            self.speak("No te abandonaron? JAJAJA!")
        elif choice == "2":
            self.speak("A tu habitacion, ahora. Debes acomodarte.")
            print("[Sonido espeluznante]")
            pause()
            
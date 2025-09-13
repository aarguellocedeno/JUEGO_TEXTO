from plaenum import PlaceID
import json
from soundManager import SoundManager
from characters import Girl, Madam, Orphanage
from places import Garden, Attic, Basement


class Game:
    def __init__(self):
        self.sound = SoundManager()
        self.load_sounds_from_json("sounds.json")

        with open("history.json", "r", encoding="utf-8") as f:
            self.narr = json.load(f)

        with open("people.json", "r", encoding="utf-8") as f:
            self.dialogs = json.load(f)

        self.girl = Girl("Chica", self.sound)
        self.madam = Madam("Madam Rolinda")
        self.orphanage = Orphanage("Sinterac", self.sound)

        self.visited_places: set[PlaceID] = set()

    # 🔥 FIX: ahora maneja bien "file" y "pos"
    def load_sounds_from_json(self, filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            sounds = json.load(f)
        for name, data in sounds.items():
            path = data["file"]
            pos = tuple(data.get("pos", (0, 0, 0)))
            self.sound.load_sound(name, path, pos)

    def _play_seq(self, key):
        seq = self.narr.get(key, [])
        for ev in seq:
            if "sound" in ev:
                self.sound.play(ev["sound"])
            if "say" in ev:
                print(ev["say"])
                input()

    def paint(self, key):
        seq = self.narr.get(key, [])
        for ev in seq:
            if "sound" in ev:
                self.sound.play(ev["sound"])
            if "say" in ev:
                print(ev["say"])

    def start(self):
        self._play_seq("intro")

        print(self.dialogs["parents"]["mom"])
        self.girl.clues.append("Caja secreta")
        self.girl.clues.append("Advertencia de mama")
        self.sound.play("eco")
        self.sound.rotate_around_player("eco", radius=15, speed=2)
        input()

        print(self.dialogs["parents"]["dad"])
        self.girl.clues.append("Codigo del padre: 9735")
        self.sound.play("thunder")
        self.sound.rotate_around_player("thunder", radius=15, speed=2)
        input()

        self._play_seq("despues_de_papas")
        self.paint("orphanage_art")
        self.orphanage.entrance()

        self.paint("madam_intro")
        choice = input("Elige (1 o 2): ").strip().lower()
        if choice not in {"1", "2"}:
            print("Opcion no valida, la opcion por defecto es 1")
            choice = "1"
        mad = self.dialogs.get("madam", {})
        msg = mad.get(choice, mad.get("default", ""))
        if msg:
            print(msg)
            input()
        if choice == "2":
            print("[Sonido espeluznante]")
            input()

        self._play_seq("noche")
        self._play_seq("manana")

        self.exploration()

    def exploration(self):
        print("Cuando despiertas decides explorar el lugar...")
        while len(self.visited_places) < 4:
            self.sound.play("think")
            self.sound.stop("sad")
            self.sound.stop("warm")
            print("[ Entraste a una zona de seleccion ]")
            print("[Un lugar central en el que podras seleccionar que lugar explorar]")
            print("Que vas a explorar:\n1) Patio\n2) Salon principal\n3) Sotano\n4) Atico\n5) Revisar pistas")
            sel = input("Selecciona el lugar: ").strip().lower()

            mapping = {
                "1": PlaceID.PATIO,
                "2": PlaceID.SALON,
                "3": PlaceID.SOTANO,
                "4": PlaceID.ATICO,
                "5": "pistas",
            }
            key = mapping.get(sel, None)
            if key is None:
                print("Opcion no valida.")
                self.sound.play("wrong")
                input()
            if key == "pistas":
                self.sound.stop("think")
                self.sound.play("unpack")
                print("Tus pistas actuales:")
                for clue in self.girl.clues:
                    print(f"- {clue}")
                input()

            place_id: PlaceID = key

            if place_id in self.visited_places:
                if place_id == PlaceID.PATIO:
                    print("Una barrera se antepone a ti, y suena un sonido de negacion\nAl ya tener el objeto de la zona en tus manos no te permitira volver a entrar")
                    print("Ese lugar ya fue explorado.")
                elif place_id == PlaceID.SALON:
                    print("Al ya haber pasado por aqui una alarma se activo, y genero una barrera para que no puedas volver a pasar")
                    print("Ese lugar ya fue explorado.\n")
                elif place_id == PlaceID.ATICO:
                    print("Cuando entraste aqui, un secuaz de madam Rolinda te vio y decidio activar la barrera para que no volvieras a entrar")
                    print("Este lugar ya fue explorado")
                else:
                    print("Ese lugar ya fue explorado.")
                self.sound.play("wrong")
                input()

            done = False
            if place_id == PlaceID.PATIO:
                self.sound.stop("think")
                done = Garden(self).run()
            elif place_id == PlaceID.SALON:
                self.sound.stop("think")
                self.sound.play("vals")
                self.sound.rotate_around_player("vals", radius=15, speed=2)
                print("Exploras el salon principal.")
                print("Ves un retrato de una familia, y en el marco esta tallada la fecha de la desaparicion de tus padres.")
                self.sound.play("vals")
                input()
                print("Sientes un nudo en la garganta")
                print("desearias que nunca hubieran ido a ese viaje")
                self.girl.clues.append("Retrato con fecha misteriosa")
                input()
                done = True
            elif place_id == PlaceID.SOTANO:
                self.sound.stop("think")
                done = Basement(self).run()
            elif place_id == PlaceID.ATICO:
                self.sound.stop("think")
                done = Attic(self).run()

            if done:
                self.visited_places.add(place_id)

        self.ending()

    def ending(self):
        self._play_seq("ending_intro")
        for clue in self.girl.clues:
            print(f"- {clue}")
            input()
        self._play_seq("ending_verdad")
        for ask in self.narr.get("ending_pregunta", []):
            if "say" in ask:
                print(ask["say"])
        decision = input("Elige (1 o 2): ").strip().lower()

        if decision == "1":
            self._play_seq("ending_fight")
        else:
            self._play_seq("ending_escape")

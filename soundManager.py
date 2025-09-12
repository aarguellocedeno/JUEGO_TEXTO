from openal import oalOpen

def pause():
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

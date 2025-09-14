from openal import oalOpen
import threading
import time
import math
import json

def pause():
    try:
        input()
    except EOFError:
        pass

class SoundManager:
    def __init__(self):
        self.sounds = {}
        self.running_rotations = {} 

    def load_sound(self, name, filepath, position=(0, 0, 0)):
        try:
            sound = oalOpen(filepath)
            if sound:
                sound.set_position(position)
                self.sounds[name] = sound
               
            else:
                print(f"[ERROR] {filepath}")
        except Exception as e:
            print(f"loading Error {filepath}: {e}")

    def load_sounds_from_json(self, filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            sounds = json.load(f)
        for name, data in sounds.items():
            path = data["file"]
            pos = tuple(data.get("pos", (0, 0, 0)))
            self.load_sound(name, path, pos)

    def set_position(self, name, position):
        if name in self.sounds:
            self.sounds[name].set_position(position)
        else:
            print(f"Sound '{name}' not found")

    def play(self, name, loop=False):
        if name in self.sounds:
            self.sounds[name].play()
            if loop:
                self.sounds[name].set_looping(True)
        else:
            print(f"Sound '{name}' not found")

    def stop(self, name):
        if name in self.sounds:
            self.sounds[name].stop()
            if name in self.running_rotations:
                self.running_rotations[name] = False
        else:
            print(f"Sound '{name}' not found")

    def rotate_around_player(self, name, radius=10, speed=1):
        if name not in self.sounds:
            print(f"Sound '{name}' not found")
            return

        self.running_rotations[name] = True

        def _rotate():
            angle = 0
            while self.running_rotations[name]:
                x = radius * math.cos(math.radians(angle))
                y = radius * math.sin(math.radians(angle))
                self.set_position(name, (x, y, 0))
                time.sleep(0.05)
                angle = (angle + speed) % 360

        t = threading.Thread(target=_rotate, daemon=True)
        t.start()

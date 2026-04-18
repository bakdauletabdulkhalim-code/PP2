import pygame
import os

class Player:
    def __init__(self):
        BASE_DIR = os.path.dirname(__file__)

        self.tracks = [
            os.path.join(BASE_DIR, "music", "Еркебұлан Құмаров - Жылтыр көйлек.mp3"),
            os.path.join(BASE_DIR, "music", "Ұланғасыр Қами - Балқия.mp3")
        ]

        self.index = 0

    def play(self):
        pygame.mixer.music.load(self.tracks[self.index])
        pygame.mixer.music.play()

    def stop(self):
        pygame.mixer.music.stop()

    def next(self):
        self.index = (self.index + 1) % len(self.tracks)
        self.play()

    def prev(self):
        self.index = (self.index - 1) % len(self.tracks)
        self.play()
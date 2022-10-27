import pygame
import os
from sound import Sound
from theme import Theme

class Config:

    def __init__(self):

        self.themes = []
        self._add_themes()
        self.idx = 0
        self.theme = self.themes[self.idx]
        self.move_sound = Sound(
            os.path.join('assets/sounds/move.wav')
        )
        self.capture_sound = Sound(
            os.path.join('assets/sounds/capture.wav')
        )

    def change_theme(self):
        self.idx += 1

    def _add_themes(self):
        pass
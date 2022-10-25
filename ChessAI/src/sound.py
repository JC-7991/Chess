import pygame

class Sound:
    
    def __init__(self, path):
        self.path = path
        self.sound = pygame.mixer.Sound()

    def play(self):
        pass
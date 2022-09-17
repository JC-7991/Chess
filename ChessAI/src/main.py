import pygame
import sys

from const import *

# Main file
class Main:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Chess')

    def mainloop(self):
        pass

main = Main()
main.mainloop()
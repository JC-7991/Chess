import pygame
import sys

from const import *

# Main file
class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
    def mainloop(self):
        print("World!")

main = Main()
main.mainloop()
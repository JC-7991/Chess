import pygame
from const import *

class Game:

    def __init__(self):
        pass

    def show_bg(self, surface):

        for row in range(ROWS):
            for col in range(COLS):
                if(row + col) % 2 == 0:
                    # light green
                    color = (234, 235, 200)
                else:
                    # dark green
                    color = (119, 154, 88)
                rect = (col * SQSIZE, row * SQSIZE, SQSIZE, SQSIZE)
                pygame.draw.rect(surface, color, rect)
    
    def show_pieces(surface):
        pass
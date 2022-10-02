import pygame
from const import *

class Dragger:

    def __init__(self):

        self.piece = None
        self.mouseX = 0
        self.mouseY = 0
        
        self.initial_row = 0
        self.initial_col = 0

    def update_mouse(self, pos):
        self.mouseX, self.mouseY = pos

    def save_initial(self, pos):
        self.initial_row = pos[1] // SQSIZE
        self.initial_col = pos[0] // SQSIZE

    def drag_piece(self, piece):
        pass



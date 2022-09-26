from const import *
from square import Square
from piece import *

class Board:

    def __init__(self):

        self.squares = [[0, 0, 0, 0, 0, 0, 0, 0] for col in range(COLS)]
        self._create()

    def _create(self):

        for row in range(ROWS):
            for col in range(COLS):
                self.squares[row][col] = Square(row, col)

    def _add_pieces(self, color):

        row_pawn, row_other = (6, 7) if color == 'white' else (1, 0)
        for col in range(COLS):
            self.squares[row_other][col] = Square(row_pawn, col, Pawn(color)) 
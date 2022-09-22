class Piece:

    def __init__(self, name, color, value, texture = None, texture_rect = None):
        pass

class Pawn(Piece):

    def _init_(self, color):  
        self.dir = -1 if color == 'white' else 1
        super().__init('pawn', color, 1.0)

class Knight(Piece):

    def _init_(self, color):  
        super().__init('knight', color, 3.0)
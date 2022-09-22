class Piece:

    def __init__(self, name, color, value, texture = None, texture_rect = None):
        pass

class Pawn(Piece):

    def _init_(self, color):  
        self.dir = -1 if color == "white" else 1
        super().__init()
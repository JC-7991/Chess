class Piece:

    def __init__(self, name, color, value, texture, teture_rect = None):
        pass

class Pawn(Piece):

    def _init_(self, color):
        
        self.dir = -1 if color == "white" else 1
class Square:

    def __init__(self, row, col, piece = None):
        self.row = row
        self.col = col
        self.piece = piece

    def has_piece(self):
        return self.piece != None

    def has_rival_piece(self, color):
        pass

    def isempty_or_rival(self, color):
        pass

    @staticmethod
    def in_range(*args):

        for arg in args:
            if arg < 0 or arg > 7:
                return False
        return True
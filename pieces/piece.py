from pieces.pawn import Pawn
from pieces.knight import Knight
from pieces.bishop import Bishop
from pieces.rook import Rook
from pieces.queen import Queen
from pieces.king import King


class Piece:

    def __init__(self, colour, piece_type, file, rank):
        self.colour = colour
        self.file = file
        self.rank = rank
        self.type = piece_type
        if self.type == 'pawn':
            self.typemgr = Pawn(colour=colour, file=file, rank=rank)
        elif self.type == 'knight':
            self.typemgr = Knight(colour=colour, file=file, rank=rank)
        elif self.type == 'bishop':
            self.typemgr = Bishop(colour=colour, file=file, rank=rank)
        elif self.type == 'rook':
            self.typemgr = Rook(colour=colour, file=file, rank=rank)
        elif self.type == 'queen':
            self.typemgr = Queen(colour=colour, file=file, rank=rank)
        elif self.type == 'king':
            self.typemgr = King(colour=colour, file=file, rank=rank)

from Pieces.king import King
from Pieces.queen import Queen
from Pieces.rook import Rook
from Pieces.bishop import Bishop
from Pieces.knight import Knight
from Pieces.pawn  import Pawn
from vector import vec

class Game:

    def __init__(self):

        self.Board = [Pawn(0, vec(1,7)), Pawn(0, vec(2,7)), Pawn(0, vec(3,7)), Pawn(0, vec(4,7)),
                      Pawn(0, vec(5,7)), Pawn(0, vec(6,7)), Pawn(0, vec(7,7)), Pawn(0, vec(8,7)),
                      Rook(0, vec(1,8)), Rook(0,vec(8,8)), Knight(0, vec(2,8)), Knight(0, vec(7,8)),
                      Bishop(0, vec(3,8)), Bishop(1, vec(6,8)), Queen(0, vec(4,8)), King(0, vec(5,8)),
                      Pawn(1, vec(1,7)), Pawn(1, vec(2,7)), Pawn(1, vec(3,7)), Pawn(1, vec(4,7)),
                      Pawn(1, vec(5,7)), Pawn(1, vec(6,7)), Pawn(1, vec(7,7)), Pawn(1, vec(8,7)),
                      Rook(1, vec(1,8)), Rook(1,vec(8,8)), Knight(1, vec(2,8)), Knight(1, vec(7,8)),
                      Bishop(1, vec(3,8)), Bishop(1, vec(6,8)), Queen(1, vec(4,8)), King(1, vec(5,8))]


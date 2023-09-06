
from vector import vec
import re

class MoveError(Exception):
    pass

class Move:

    """
    class representing movement in chess

    Attributes:
        move (str): movement in chess


    """
    pawn_expr = re.compile('[a-h][1-8]')
    piece_expr = re.compile('[K,N,R,B,Q][a-h][1-8]')
    piece_takes_expr = re.compile('[K,N,R,B,Q]x[a-h][1-8]')
    pawn_takes_expr = re.compile('[a-h]x[a-h][1-8]')
    short_castle_expr = re.compile('(0-0)|(O-O)')
    long_castle_expr = re.compile('(0-0-0)|(O-O-O)')
    promote_expr = re.compile('[a-h][1-8]=[K,N,Q,B,R]')



    def __init__(self, move:str):
        """
        initializes an object with parameters
        """
        if len(move) >5:
            raise MoveError("invalid move")
        
        if self.pawn_expr.match(move) is not None:
            self.move = move
        elif self.piece_expr.match(move) is not None:
            self.move = move
        elif self.piece_takes_expr.match(move) is not None:
            self.move = move
        elif self.pawn_takes_expr.match(move) is not None:
            self.move = move
        elif self.short_castle_expr.match(move) is not None:
            self.move = move
        elif self.long_castle_expr.match(move) is not None:
            self.move = move
        elif self.promote_expr.match(move) is not None:
            self.move = move
        
        else:
            raise MoveError("invalid move")

    
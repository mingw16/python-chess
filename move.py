
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
    move_pattern = ['[a-h][1-8]','[K,N,R,B,Q][a-h][1-8]','[K,N,R,B,Q]x[a-h][1-8]','[a-h]x[a-h][1-8]','(0-0)|(O-O)','(0-0-0)|(O-O-O)','[a-h][1-8]=[K,N,Q,B,R]']


    def __init__(self, move:str):
        """
        initializes an object with parameters
        """
        correct = False
        for pattern in self.move_pattern:
            expr = re.compile(pattern)
            if expr.match(move) is not None:
                correct = True
                self.move = move
                break
        if not correct or len(move) >5 or len(move) < 2:
            raise MoveError("invalid move")

    

from typing import Final
# from piece import Move, Piece
from .piece import Piece

class Queen(Piece):

    MOVES = [(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),
             (0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),
             (-1,0),(-2,0),(-3,0),(-4,0),(-5,0),(-6,0),(-7,0),
             (0,-1),(0,-2),(0,-3),(0,-4),(0,-5),(0,-6),(0,-7),
             (1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),
             (-1,1),(-2,2),(-3,3),(-4,4),(-5,5),(-6,6),(-7,7),
             (1,-1),(2,-2),(3,-3),(4,-4),(5,-5),(6,-6),(7,-7),
             (-1,-1),(-2,-2),(-3,-3),(-4,-4),(-5,-5),(-6,-6),(-7,-7)
             ]
    
    def canMove(self, move, board):
        pass
        


    def getPossibleMoves(self, board):
        possible_moves = []
        for move in self.MOVES:
            if self.canMove(move, board):
                possible_moves.append(move)

        return possible_moves
        

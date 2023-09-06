from Pieces.king import King
from Pieces.queen import Queen
from Pieces.bishop import Bishop
from Pieces.pawn import Pawn
from Pieces.rook import Rook
from Pieces.knight import Knight

from vector import vec
from move import Move, MoveError
import re

class Game:

    def __init__(self):

        self.Board = [Pawn(0, vec(1,7)), Pawn(0, vec(2,7)), Pawn(0, vec(3,7)), Pawn(0, vec(4,7)),
                      Pawn(0, vec(5,7)), Pawn(0, vec(6,7)), Pawn(0, vec(7,7)), Pawn(0, vec(8,7)),
                      Rook(0, vec(1,8)), Rook(0,vec(8,8)), Knight(0, vec(2,8)), Knight(0, vec(7,8)),
                      Bishop(0, vec(3,8)), Bishop(1, vec(6,8)), Queen(0, vec(4,8)), King(0, vec(5,8)),
                      Pawn(1, vec(1,2)), Pawn(1, vec(2,2)), Pawn(1, vec(3,2)), Pawn(1, vec(4,2)),
                      Pawn(1, vec(5,2)), Pawn(1, vec(6,2)), Pawn(1, vec(7,2)), Pawn(1, vec(8,2)),
                      Rook(1, vec(1,1)), Rook(1,vec(8,1)), Knight(1, vec(2,1)), Knight(1, vec(7,1)),
                      Bishop(1, vec(3,1)), Bishop(1, vec(6,1)), Queen(1, vec(4,1)), King(1, vec(5,1))]
        

    def loop(self):

        print("GRA W SZACHY ")
        print("GRASZ KOLOREM BIAŁYM \n PODAJ RUCH:")
        while True:
            user_input = input()
            print(user_input)
            try:
                move = Move(user_input)
            except MoveError:
                print("podaj ruch jeszcze raz")
                continue
            if user_input == "!q":
                break
                


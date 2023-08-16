
from collections import namedtuple
from .. import vec


class Piece:

    def __init__(self, color:int, pos:vec):
        self.color = color
        self.pos = pos
from enum import Enum


class Colour(Enum):
    BLACK = 1
    WHITE = 2


class Piece:
    def __init__(self, colour):
        self.colour = colour

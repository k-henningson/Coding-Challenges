import unittest
from chess import *


class TestChess(unittest.TestCase):
    def test_a_piece_can_be_black(self):
        black_piece = Piece(Colour.BLACK)
        self.assertEqual(black_piece.colour, Colour.BLACK)

    def test_a_piece_can_be_white(self):
        white_piece = Piece(Colour.WHITE)
        self.assertEqual(white_piece.colour, Colour.WHITE)


if __name__ == '__main__':
    unittest.main()

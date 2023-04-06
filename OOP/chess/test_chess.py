import unittest
from chess import Board


class TestChess(unittest.TestCase):
    def test_display_board_empty_prints_8x8_matrix(self):
        board = Board()
        self.assertEqual(board.display_board(), "_ _ _ _ _ _ _ _ \n" * 8)


if __name__ == '__main__':
    unittest.main()

import unittest
from chess import Board


class TestChess(unittest.TestCase):
    def test_create_board_prints_8x8_matrix_find_starting_point(self):
        board = Board()
        self.assertEqual(board._board[0][0], None)

    def test_create_board_prints_8x8_matrix_find_ending_point(self):
        board = Board()
        self.assertEqual(board._board[7][7], None)

    def test_create_board_prints_8x8_matrix_find_invalid_point(self):
        board = Board()
        with self.assertRaises(IndexError) as context:
            board._board[8][8]
        expected_error_msg = "list index out of range"
        self.assertEqual(str(context.exception), expected_error_msg)


if __name__ == '__main__':
    unittest.main()

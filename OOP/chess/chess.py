class Board:
    def __init__(self):
        # will print a list as [None, None, None... etc 8 times] and each list will print 8 times
        self._board = [[None] * 8 for _ in range(8)]

    def display_board(self):
        board_string = ""
        # nested for loop to iterate rows and pieces
        for row in self._board:
            for piece in row:
                if piece is None:
                    # generates intial board as no pieces created yet
                    board_string += "_ "
                else:
                    # will replace _ with piece type when pieces created
                    board_string += piece.type + " "
            # new line after each row prints
            board_string += "\n"
        return print(board_string)


board = Board()
board.display_board()

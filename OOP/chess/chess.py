class Board:
    def __init__(self):
        # will print a list as [None, None, None... etc 8 times] and each list will print 8 times
        self._board = [[None] * 8 for _ in range(8)]

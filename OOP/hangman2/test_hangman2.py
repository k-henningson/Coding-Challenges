import unittest
from hangman2 import Hangman


class TestHangman(unittest.TestCase):
    def test_guess_incorrect(self):
        hangman = Hangman("test")
        # 1. Guessing a letter in the word shows us the word with that letter revealed
        self.assertEqual(hangman.guess("E"), '_E__')
        # 2. Guessing the same letter twice does nothing
        self.assertEqual(hangman.guess("E"), '_E__')
        # 3. Guessing a wrong letter decrements our remaining lives
        self.assertEqual(hangman.guess('a'), '_E__')
        self.assertEqual(hangman.lives, 5)
        # 4. Guessing wrong 6 times causes the game to end
        self.assertEqual(hangman.guess("q"), '_E__')
        self.assertEqual(hangman.guess("p"), '_E__')
        self.assertEqual(hangman.guess("y"), '_E__')
        self.assertEqual(hangman.guess("z"), '_E__')
        self.assertEqual(hangman.guess(
            "m"), 'Game over, the secret word was TEST.')

    def test_correct(self):
        hangman = Hangman('python')
        # 5. Guessing the correct word causes the game to end in a win
        self.assertEqual(hangman.guess("p"), 'P_____')
        self.assertEqual(hangman.guess("y"), 'PY____')
        self.assertEqual(hangman.guess("t"), 'PYT___')
        self.assertEqual(hangman.guess("h"), 'PYTH__')
        self.assertEqual(hangman.guess("o"), 'PYTHO_')
        self.assertEqual(hangman.guess(
            "n"), 'Congratulations, you win! The secret word was PYTHON.')

    def test_solution_is_always_uppercase(self):
        for letter in ("h", "H"):
            hangman = Hangman("hello")
            self.assertEqual("H____", hangman.guess(letter))

if __name__ == '__main__':
    unittest.main()

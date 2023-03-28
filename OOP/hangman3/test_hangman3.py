import unittest
from hangman3 import Hangman


class TestHangman(unittest.TestCase):
    def test_guess_word_prints_correct_underscore_length(self):
        hangman = Hangman('hockey', 'l')
        self.assertEqual(hangman.guess('a'), '______')

    def test_guess_incorrect_letter(self):
        hangman = Hangman('test', 'l')
        self.assertEqual(hangman.guess("a"), '____')

    def test_guess_correct_letter(self):
        hangman = Hangman('apple', 'l')
        self.assertEqual(hangman.guess("a"), 'A____')

    def test_guess_correct_letter_twice_prints_same_output(self):
        hangman = Hangman('peach', 'l')
        self.assertEqual(hangman.guess('a'), '__A__')
        self.assertEqual(hangman.guess('a'), '__A__')

    def test_guess_incorrect_letter_decrements_lives(self):
        hangman = Hangman('strawberry', 'p')
        self.assertEqual(hangman.guess('q'), '__________')
        self.assertEqual(hangman.lives, 5)

    def test_guess_incorrect_word(self):
        hangman = Hangman('roulette', 'j')
        self.assertEqual(hangman.guess('q'), '________')
        self.assertEqual(hangman.guess("w"), '________')
        self.assertEqual(hangman.guess("y"), '________')
        self.assertEqual(hangman.guess("i"), '________')
        self.assertEqual(hangman.guess("p"), '________')
        self.assertEqual(hangman.guess(
            "s"), 'Game over, the secret word was ROULETTE.')

    def test_guess_correct_word(self):
        hangman = Hangman('python', 'u')
        self.assertEqual(hangman.guess("p"), 'P_____')
        self.assertEqual(hangman.guess("y"), 'PY____')
        self.assertEqual(hangman.guess("t"), 'PYT___')
        self.assertEqual(hangman.guess("h"), 'PYTH__')
        self.assertEqual(hangman.guess("o"), 'PYTHO_')
        self.assertEqual(hangman.guess(
            "n"), 'Congratulations, you win! The secret word was PYTHON.')

    def test_solution_is_always_uppercase(self):
        for letter in ("h", "H"):
            hangman = Hangman("hello", 'y')
            self.assertEqual("H____", hangman.guess(letter))

    def test_roulette_letter_kills_game(self):
        hangman = Hangman('putin', 'p')
        self.assertEqual(hangman.guess(
            'p'), 'Game over, the secret word was PUTIN.')


if __name__ == '__main__':
    unittest.main()

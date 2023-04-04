import unittest
from hangman4 import Hangman
from hangman4 import Roulette


class TestHangman(unittest.TestCase):
    def test_guess_word_prints_correct_underscore_length(self):
        hangman = Hangman('hockey')
        self.assertEqual(hangman.guess('a'), '______')

    def test_guess_incorrect_letter(self):
        hangman = Hangman('test')
        self.assertEqual(hangman.guess("a"), '____')

    def test_guess_correct_letter(self):
        hangman = Hangman('apple')
        self.assertEqual(hangman.guess("a"), 'A____')

    def test_guess_correct_letter_twice_prints_same_output(self):
        hangman = Hangman('peach')
        self.assertEqual(hangman.guess('a'), '__A__')
        self.assertEqual(hangman.guess('a'), '__A__')

    def test_guess_incorrect_letter_decrements_lives(self):
        hangman = Hangman('strawberry')
        self.assertEqual(hangman.guess('q'), '__________')
        self.assertEqual(hangman.lives, 5)

    def test_guess_incorrect_word(self):
        hangman = Hangman('roulette')
        self.assertEqual(hangman.guess('q'), '________')
        self.assertEqual(hangman.guess("w"), '________')
        self.assertEqual(hangman.guess("y"), '________')
        self.assertEqual(hangman.guess("i"), '________')
        self.assertEqual(hangman.guess("p"), '________')
        self.assertEqual(hangman.guess(
            "s"), 'Game over, the secret word was ROULETTE.')

    def test_guess_correct_word(self):
        hangman = Hangman('python')
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


class TestRoulette(unittest.TestCase):
    def test_guess_word_prints_correct_underscore_length(self):
        roulette = Roulette('hockey', 'l')
        self.assertEqual(roulette.guess('a'), '______')

    def test_guess_incorrect_letter(self):
        roulette = Roulette('test', 'l')
        self.assertEqual(roulette.guess("a"), '____')

    def test_guess_correct_letter(self):
        roulette = Roulette('apple', 'p')
        self.assertEqual(roulette.guess("a"), 'A____')

    def test_roulette_letter_kills_game(self):
        roulette = Roulette('putin', 'p')
        self.assertEqual(roulette.guess(
            "p"), 'Game over, the secret word was PUTIN.')


if __name__ == '__main__':
    unittest.main()

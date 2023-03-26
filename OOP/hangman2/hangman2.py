import random
import string


class Hangman:
    def __init__(self, secret_word):
        self._lives = 6
        self._secret_word = secret_word.upper()
        self._alphabet = set(string.ascii_uppercase)
        self._letters_guessed = set()

    @property
    def lives(self):
        """Number of lives remaining"""
        return self._lives

    def guess(self, letter):
        """Guesses a letter. Returns the currently solved secret word."""
        uppercase_letter = letter.upper()
        if uppercase_letter in self._alphabet:
            if not uppercase_letter in self._secret_word and not uppercase_letter in self._letters_guessed:
                self._decrement_lives()
                if (self._lives == 0):
                    return self._end_game()

            #  can always add to a set won't cause duplicate
            self._letters_guessed.add(uppercase_letter)
            if self._secret_word == self._update_secret_word():
                return self._win_game()

        return self._update_secret_word()

    def _update_secret_word(self):
        revealed_word = ''
        for char in self._secret_word:
            if (char in self._letters_guessed):
                revealed_word += char
            else:
                revealed_word += '_'
                
        return revealed_word

    def _decrement_lives(self):
        if (self._lives >= 1):
            self._lives = self._lives - 1

    def _end_game(self):
        return (f'Game over, the secret word was {self._secret_word}.')

    def _win_game(self):
        return (f'Congratulations, you win! The secret word was {self._secret_word}.')

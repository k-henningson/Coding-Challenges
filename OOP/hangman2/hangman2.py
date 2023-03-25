import random
import string


class Hangman:
    def __init__(self, secret_word):
        self.lives = 6
        self.secret_word = secret_word.upper()
        self.alphabet = set(string.ascii_uppercase)
        self.letters_guessed = set()

    def update_secret_word(self):
        revealed_word = ''
        for char in self.secret_word:
            if (char in self.letters_guessed):
                revealed_word += char
            else:
                revealed_word += '_'
        return revealed_word

    def decrement_lives(self):
        if (self.lives >= 1):
            self.lives = self.lives - 1

    def guess(self, letter):
        letter = letter.upper()
        if letter in self.alphabet:
            if not letter in self.secret_word and not letter in self.letters_guessed:
                self.decrement_lives()
                if (self.lives == 0):
                    return self.end_game()
            #  can always add to a set won't cause duplicate
            self.letters_guessed.add(letter)
            if self.secret_word == self.update_secret_word():
                return self.win_game()
        return self.update_secret_word()

    def end_game(self):
        return (f'Game over, the secret word was {self.secret_word}.')

    def win_game(self):
        return (f'Congratulations, you win! The secret word was {self.secret_word}.')


game1 = Hangman('hockey')
print(game1.guess('h'))
print(game1.guess('o'))
print(game1.guess('c'))
print(game1.guess('k'))
print(game1.guess('e'))
print(game1.guess('y'))

game2 = Hangman('hockey')
print(game2.guess('a'))
print(game2.guess('b'))
print(game2.guess('d'))
print(game2.guess('f'))
print(game2.guess('g'))
print(game2.guess('i'))

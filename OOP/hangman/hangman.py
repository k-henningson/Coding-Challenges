from words import word_list
import random
import string


def get_word(word_list):
    word = random.choice(word_list)
    return word.upper()


def hangman():
    word = get_word(word_list)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    incorrect_letters = set()
    lives = 6

    # user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        print("\nYou have", lives, "lives left and have used the following letters: ",
              " ".join(incorrect_letters))

        # status of current word (i.e. W - R D)
        current_word = [
            letter if letter in incorrect_letters else '-' for letter in word]
        print("Current word: ", ' '.join(current_word))

        letter_guessed = input('Guess a letter: ').upper()
        if letter_guessed in alphabet - incorrect_letters:
            incorrect_letters.add(letter_guessed)
            if letter_guessed in word_letters:
                word_letters.remove(letter_guessed)

            else:
                lives = lives - 1
                print("\nLetter guessed is not in the word, try again.")

        elif letter_guessed in incorrect_letters:
            print("\nYou have already guessed that character. Please try again.")

        else:
            print("\nInvalid character, please try again.")

    # end of game
    if lives == 0:
        print("You lost, sorry. The word was", word)
    else:
        print("You guessed the correct word!", word, "Way to go!")


hangman()

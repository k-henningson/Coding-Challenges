from hangman import get_word


def test_hangman():
    assert get_word(["entrance"]) == "ENTRANCE", "Should be ENTRANCE"
    # comment out hangman() call in hangman.py to run test


if __name__ == "__main__":
    test_hangman()
    print("Everything passed")

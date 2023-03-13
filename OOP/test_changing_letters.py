from changing_letters import swap


def test_changing_letters():
    assert swap("HelloWorld!") == "HEllOWOrld!", "Should be HEllOWOrld"
    assert swap("Hello Peter!") == "HEllO PEtEr!", "Should be HEllO PEtEr"


if __name__ == "__main__":
    test_changing_letters()
    print("Everything passed")

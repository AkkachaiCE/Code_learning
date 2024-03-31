from bank import value

def main():

    test_bank()

def test_bank():
    assert value("hello") == 0
    assert value(" hello ") == 0
    assert value("Hi") == 20
    assert value("How you doing?") == 20
    assert value("Good Morning") == 100
    assert value("What's up?") == 100

if __name__ == "__main__":
    main()

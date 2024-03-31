from jar import Jar
import pytest

def test_init():
    try:
        jar = Jar(-2)
        with pytest.raises(ValueError):
            assert init(jar)
    except ValueError:
        ...


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    try:
        jar = Jar()
        jar.deposit(-2)
        with pytest.raises(ValueError):
            assert init(jar)

        jar.deposit(-2.5)
        with pytest.raises(ValueError):
            assert init(jar)

        jar.deposit(13)
        with pytest.raises(ValueError):
            assert init(jar)
    except ValueError:
        ...

def test_withdraw():
    try:
        jar = Jar()
        jar.withdraw(-2)
        with pytest.raises(ValueError):
            assert withdraw(jar)

        jar.withdraw(-2.6)
        with pytest.raises(ValueError):
            assert withdraw(jar)
    except ValueError:
        ...

from fuel import convert, gauge
import pytest

def main():
    test_fuel()

def test_fuel():
    try:
        assert gauge(convert("3/4")) == "75%"
        assert gauge(convert("1/3")) == "33%"
        assert gauge(convert("2/3")) == "67%"
        assert gauge(convert("0/100")) == "E"
        assert gauge(convert("1/100")) == "E"
        assert gauge(convert("100/100")) == "F"
        assert gauge(convert("99/100")) == "F"
        assert gauge(convert("100/0")) == ZeroDivisionError

    except (ValueError, ZeroDivisionError):
        pass

    with pytest.raises(ValueError):
        convert("5/4")
        convert("6/4")


if __name__ == "__main__":
    main()

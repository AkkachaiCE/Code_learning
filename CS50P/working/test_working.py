from working import convert
import pytest

def main():
    test_convert()

def test_convert():

    try:
        assert convert("9 AM to 5 PM") == "09:00 to 17:00"
        assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
        assert convert("8 PM to 8 AM") == "20:00 to 08:00"
        assert convert("8:00 PM to 8:00 AM") == "20:00 to 08:00"

    except ValueError:
        print("A ValueError was raised, as expected.")

    with pytest.raises(ValueError):
        convert("8:60 AM to 4:60 PM")
    with pytest.raises(ValueError):
        convert("9AM to 5PM")
    with pytest.raises(ValueError):
        convert("09:00 to 17:00")
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")
    with pytest.raises(ValueError):
        convert("9:00 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("10:7 AM - 5:1 PM")
    with pytest.raises(ValueError):
        convert("9:00 AM 5:00 PM")
    with pytest.raises(ValueError):
        convert("9:72 to 6:30")




if __name__ == "__main__":
    main()

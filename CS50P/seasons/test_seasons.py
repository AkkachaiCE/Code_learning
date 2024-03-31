from seasons import is_valid_date

def main():
    test_is_valid_date()

def test_is_valid_date():
    assert is_valid_date("1999-01-01") == True
    assert is_valid_date("2020-06-01") == True
    assert is_valid_date("February 6th, 1998") == False

if __name__ == "__main__":
    main()

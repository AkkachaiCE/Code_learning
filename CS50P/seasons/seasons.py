from datetime import date, datetime, timedelta
import sys
import inflect

def main():
    #print(date.today())
    user_input = input("Date of Birth: ")
    if is_valid_date(user_input):
        user_time = datetime.strptime(user_input, '%Y-%m-%d')
        today = datetime.strptime(str(date.today()), '%Y-%m-%d')
        difference = today - user_time
        minutes = int(difference.total_seconds() / 60)

        p = inflect.engine()
        words = p.number_to_words(minutes).replace(" and", "").capitalize()
        print(words + " minutes")
    else:
        sys.exit("Invalid Date")

def is_valid_date(s):
    try:
        datetime.strptime(s, '%Y-%m-%d')
        return True
    except ValueError:
        return False




if __name__ == "__main__":
    main()

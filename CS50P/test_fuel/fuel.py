def main():
    while True:
        try:
            user_input = input("Fraction: ")
            result = gauge(convert(user_input))
            if result:
                print(result)
                break
        except (ValueError, ZeroDivisionError):
            continue

def convert(fraction):
    fraction = fraction.split("/")

    if int(fraction[0]) > int(fraction[1]):
        raise ValueError
    elif int(fraction[1]) == 0:
        raise ZeroDivisionError
    else:
        fuel_left = round((int(fraction[0]) / int(fraction[1])) * 100)
        return fuel_left


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return str(percentage)+"%"

if __name__ == "__main__":
    main()

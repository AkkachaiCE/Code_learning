while True:
    try:
        user_input = input("Fraction: ")
        fractions = user_input.split("/")
        fuel_left = round((int(fractions[0]) / int(fractions[1])) * 100)
        #print("fuel_left", fuel_left)

        if int(fractions[0]) == 0 or fuel_left < 2:
            print("E")
            break
        elif int(fractions[0])/int(fractions[1]) > 1:
            ...
        elif fuel_left >= 99:
            print("F")
            break
        else:
            print(int(fuel_left),"%", sep="")
            break


    except ZeroDivisionError:
        ...
    except ValueError:
        ...






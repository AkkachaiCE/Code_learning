def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if 6 < len(s) or len(s) < 2:
        #print(len(s))
        return False
    elif s[0:2].isalpha() == False:
        #print("Check alpha", _)
        return False

    count = 0
    for _ in s:
        if _.isdigit():
            count += 1
    if count >= 1:
        found_zero = False
        found_num = False
        found_text = False
        for _ in s:
            if _ == "0":
                found_zero = True
            elif _.isdigit():
                found_num = True
            if found_zero and found_num == False:
                return False

    found_num = False
    found_char = False
    for _ in s:
        if _.isdigit():
            found_num = True
        elif _.isalpha():
            found_char = True
            if found_num and found_char:
                return False


    for _ in s:
        if not _.isalpha() and not _.isdigit():
            #print("Check alpha or digit", _)
            return False
    return True


if __name__ == "__main__":
    main()

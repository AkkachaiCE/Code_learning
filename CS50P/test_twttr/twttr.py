def main():
    user_input = input("Input: ")
    print("Output: ", end="")
    short = shorten(user_input)
    print(short, end="")
    print("")

def shorten(word):
    new_word = []
    for _ in word:
        if _.lower() == "a" or _.lower() == "e" or _.lower() == "i" or _.lower() == "o" or _.lower() == "u":
            continue
        else:
            new_word += _
    new_word = "".join(new_word)
    return new_word

if __name__ == "__main__":
    main()

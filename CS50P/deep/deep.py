def main():
    user_input = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    user_input = user_input.lower().strip()
    if user_input == "forty-two" or user_input == "forty two" or user_input == "42":
        print("Yes")
    else:
        print("No")

main()

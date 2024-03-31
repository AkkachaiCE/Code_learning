def main():
    user_input = input("Greeting: ")
    user_input = user_input.lower().strip()
    #print(user_input)

    if "hello" in user_input:
        print("$0")
    elif "h" in user_input[0]:
        print("$20")
    else:
        print("$100")


main()

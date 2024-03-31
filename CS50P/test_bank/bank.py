def main():
    user_input = input("Greeting: ")
    #user_input = user_input.lower().strip()
    amount = value(user_input)
    print(f"${amount}")

def value(greeting):
    greeting = greeting.lower().strip()
    if "hello" in greeting:
        return int(0)
    elif "h" in greeting[0]:
        return int(20)
    else:
        return int(100)

if __name__ == "__main__":
    main()

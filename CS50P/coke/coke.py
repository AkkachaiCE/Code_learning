Amount_Due = 50
print("Amount Due:", Amount_Due)

while Amount_Due > 0:
    while True:
        user_input = input("Insert Coin: ")
        if user_input == "25" or user_input == "10" or user_input == "5":
            break
        else:
            print("Amount Due:", Amount_Due)
    Amount_Due = Amount_Due - int(user_input)
    if Amount_Due <= 0:
        break
    else:
        print("Amount Due:", Amount_Due)
print("Change Owed:", abs(Amount_Due))


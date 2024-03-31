user_input = input("Input: ")
print("Output: ", end="")
for _ in user_input:
    if _.lower() == "a" or _.lower() == "e" or _.lower() == "i" or _.lower() == "o" or _.lower() == "u":
        print("", end="")
    else:
        print(_, end="")
print("")

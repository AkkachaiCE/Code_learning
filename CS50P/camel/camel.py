user_input = input("camelCase: ")
print("snake_case: ", end=""y)
for _ in user_input:
    if _.isupper():
        print("_" + _.lower(), end="")
    else:
        print(_, end="")
print("")

user_input = input("Expression: ")
x, y, z = user_input.split(" ")

if y == "+":
    print(float(x) + float(z))
elif y == "-":
    print(float(x) - float(z))
elif y == "*":
    print(float(x) * float(z))
else:
    print("{:.1f}".format(float(x) / float(z)))


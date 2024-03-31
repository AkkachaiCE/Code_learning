Menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

Total = 0.00
order = []
while True:
    try:
        item = input("Item: ").title()
        order.append(item)
        if item in Menu:
            #print("Total:", Menu[item])
            Total = Total + Menu[item]
            print("Total: ${:.2f}".format(Total), sep="")
        #elif item == "":
            #break
    except EOFError:
        break

    except KeyError:
        ...
print("")

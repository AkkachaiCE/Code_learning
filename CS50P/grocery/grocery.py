item_list = {}
while True:
    try:
        item = input()
        if item not in item_list:
            item_list[item] = 1
        else:
            item_list[item] = item_list[item] + 1

    except EOFError:
        break
    except KeyError:
        ...
for key, value in sorted(item_list.items()):
    print(value, key.upper())

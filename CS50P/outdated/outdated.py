Month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    try:
        date = input("Date: ").title().strip()
        if "/" in date:
            date = date.split("/")
            if int(date[0]) > 12 or int(date[1]) > 31:
                ...
            else:
                break
        elif "," in date:
            date = date.replace(",", "").split(" ")
            if int(date[1]) > 31:
                ...
            else:
                date[0] = Month.index(date[0]) + 1
                #print(index)
                break
    except ValueError:
        ...
print(f"{date[2]}-{int(date[0]):02}-{int(date[1]):02}")

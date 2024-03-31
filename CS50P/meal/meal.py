def main():
    user_input = input("What time is it? ")
    #hours, minutes = user_input.split(":")
    time_con = convert(user_input)

    if 7 <= time_con <= 8:
        print("breakfast time")
    elif 12 <= time_con <= 13:
        print("lunch time")
    elif 18 <= time_con <= 19:
        print("dinner time")

def convert(user_input):
    hours, minutes = user_input.split(":")
    time = float(hours) + (float(minutes)/60)
    #print(time)
    return time


if __name__ == "__main__":
    main()

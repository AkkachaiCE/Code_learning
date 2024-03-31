import random

while True:
    try:
        user_level = input("Level: ")
        if int(user_level) > 0:
            break
        else:
            ...
    except ValueError:
        ...

random_number = random.randint(1, int(user_level))
#user_guess = 0
while True:
    try:
        user_guess = input("Guess: ")
        if int(user_guess) > random_number:
            print("Too Large!")
        elif int(user_guess) < random_number:
            print("Too small!")
        elif int(user_guess) == random_number:
            print("Just right!")
            break
        else:
            ...
    except ValueError:
        ...


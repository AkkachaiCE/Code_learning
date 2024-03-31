import random

def main():
    user_score = 0

    level_input = get_level()
    for _ in range(10):
        gen_num = generate_integer(level_input)
        #print(f"{gen_num[0]} + {gen_num[1]} = ", end="")
        flag = True
        #check answer
        for _ in range(3):
            try:
                print(f"{gen_num[0]} + {gen_num[1]} = ", end="")
                answer = input()
                if int(answer) == gen_num[0] + gen_num[1]:
                    user_score = user_score + 1
                    flag = False
                    break
                else:
                    print("EEE")
            except ValueError:
                print("EEE")
        if flag:
            print(f"{gen_num[0]} + {gen_num[1]} = {gen_num[0] + gen_num[1]}")

    print("Score:", user_score)

def get_level():
    while True:
        try:
            user_level = input("Level: ")
            if 0 < int(user_level) <= 3:
                break
            else:
                ...
        except ValueError:
            ...
    return int(user_level)

def generate_integer(level):
    #print(level)
    if level == 1:
        lower_bound = 0
    else:
        lower_bound = 10**(level-1)

    upper_bound = 10**level-1
    #print(lower_bound, upper_bound)
    random_x = random.randint(lower_bound, upper_bound)
    random_y = random.randint(lower_bound, upper_bound)
    #print(f"{random_x} + {random_y} = ", end="")
    return random_x, random_y


if __name__=="__main__":
    main()

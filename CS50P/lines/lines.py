import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) == 2:
    if (sys.argv[1]).endswith(".py"):
        try:
            with open(sys.argv[1], 'r') as file:
                lines = 0
                for line in file:
                    line = line.strip()
                    if line == "":
                        pass
                    elif line.startswith("#"):
                        pass
                    else:
                        lines += 1
                print(lines)
        except FileNotFoundError:
            print("The file does not exist.")
    else:
        sys.exit("Not a Python file")
else:
    sys.exit("Too many command-line arguments")

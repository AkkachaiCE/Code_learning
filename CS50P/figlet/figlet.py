import sys
from pyfiglet import Figlet
figlet = Figlet()

#print(sys.argv[1])
if len(sys.argv) == 1:
    print(figlet.renderText(input("Input: ")))
elif len(sys.argv) == 3:
    #user_input = input("Input: ")
    if sys.argv[1] != "-f" and sys.argv[1] != "--font":
        print("Invalid usage")
        sys.exit(1)
    else:
        if sys.argv[2] in figlet.getFonts():
            figlet.setFont(font=sys.argv[2])
            print(figlet.renderText(input("Input: ")))
        else:
            print("Invalid usage")
            sys.exit(2)
else:
    print("Invalid usage")
    sys.exit(3)


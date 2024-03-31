def main():
    user_input = input("File name: ")
    user_input = user_input.lower().strip()
    #print(user_input)

    if ".gif" in user_input:
        print("image/gif")
    elif ".jpg" in user_input or ".jpeg" in user_input:
        print("image/jpeg")
    elif ".png" in user_input:
        print("image/png")
    elif ".pdf" in user_input:
        print("application/pdf")
    elif ".txt" in user_input:
        print("text/plain")
    elif ".zip" in user_input:
        print("application/zip")
    else:
        print("application/octet-stream")


main()

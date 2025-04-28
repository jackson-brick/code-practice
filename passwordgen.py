import random
import os
os.system('clear')
z=os.get_terminal_size()[0]




while True:
    os.system('clear')
    print("Are you using a website or an app?".center(z))
    webApp = input()
    if webApp.strip().lower() == "website":
        webApp = "website"
        break
    elif webApp.strip().lower() == "app":
        webApp = "app"
        break

while True:
    name = ""
    firstDot = 0
    os.system('clear')
    if webApp == "website":
        print("Enter the full url of the website you need the password for".center(z))
        website = input()
        if website.count(".") == 1:
            for i in website:
                if firstDot == 0 and i != ".":
                    name += i
                elif i == ".":
                    firstDot += 1
        elif website.count(".") == 2:
            for i in website:
                if firstDot == 1 and i != ".":
                    name += i
                elif i == ".":
                    firstDot += 1
        else:
            print("That is not a url. Press ENTER to try again.".center(z))
            input()
    else:
        print("Enter the name of the app you need the password for".center(z))
        app = input()
        if app.strip().isalpha():
            name = app.lower().strip()
        while True:
            os.system('clear')
            print(f"Is {name} correct?".center(z))
            yesOrNo = input()
            if yesOrNo.strip().lower() == "yes":
                break
            elif yesOrNo.strip().lower() == "no":
                break
    if yesOrNo.strip().lower() == "yes":
        break



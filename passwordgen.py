import random
import os
os.system('clear')
z=os.get_terminal_size()[0]


while True:
    print("Are you using a website or an app?".center(z))
    webApp = input()
    webApp=webApp.strip().lower()
    websiteScore = 0
    appScore = 0
    for i in range(len(webApp)):
        try:
            if webApp[i] == "website"[i]:
                websiteScore += 1
        except:
            pass
        try:
            if webApp[i] == "app"[i]:
                appScore += 1
        except:
            pass
    print(websiteScore)
    if not websiteScore >=3 and appScore >=2:
        print("true")
        if websiteScore - appScore > 0:
            webApp = "website"
            break
        elif websiteScore-appScore < 0:
            webApp = "app"
            break
print(webApp)
print("Enter the full url of the website you need the password for")
website = input()


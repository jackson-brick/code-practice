import random
import os
os.system('clear')
z=os.get_terminal_size()[0]

websiteToken = 107.25
appToken = 109.5

print("Are you using a website or an app?".center(z))
webApp = input()
word=webApp.strip().lower()
finalCount = 0
weightCount = 0
for i in range(len(word)):
    finalCount +=  ((i+1)*ord(word[i]))
    weightCount += (i+1)
webApp = finalCount/weightCount
if (websiteToken-webApp) > (appToken-webApp):
    webApp = "app"
else:
    webApp = "website"
print(webApp)
print("Enter the full url of the website you need the password for")
website = input()


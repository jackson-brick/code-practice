import random
import os

#with open('diaryusers.json','r') as file:
    #diaryusers = json.load(file)

os.system('clear')
newUser = []
charList = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0","!","@","#","$","%","^","&","*","(",")","-","_","=","+","`","~","{","}","[","]","|","\\","\'","\"",":",";","<",">",",",".","?","/"," "]
tempCharList = []
for ele in charList:
    
    tempCharList.append(ele)
randomCharList = []
for item in range(len(tempCharList)):
    randomCharList.append(random.choice(tempCharList))
    tempCharList.remove(randomCharList[item])
keyDict = {"a":"","b":"","c":"","d":"","e":"","f":"","g":"","h":"","i":"","j":"","k":"","l":"","m":"","n":"","o":"","p":"","q":"","r":"","s":"","t":"","u":"","v":"","w":"","x":"","y":"","z":"","A":"","B":"","C":"","D":"","E":"","F":"","G":"","H":"","I":"","J":"","K":"","L":"","M":"","N":"","O":"","P":"","Q":"","R":"","S":"","T":"","U":"","V":"","W":"","X":"","Y":"","Z":"","1":"","2":"","3":"","4":"","5":"","6":"","7":"","8":"","9":"","0":"","!":"","@":"","#":"","$":"","%":"","^":"","&":"","*":"","(":"",")":"","-":"","_":"","=":"","+":"","`":"","~":"","{":"","}":"","[":"","]":"","|":"","\\":"","'":"","\"":"",":":"",";":"","<":"",">":"",",":"",".":"","?":"","/":""," ":""}
for item in range(len(charList)):
    keyDict[charList[item]] = randomCharList[item]
newUser.append({"key":keyDict,"name":"jacksonbrick","password":"blahblah","fontColor":"default","fontBold":"no"})
print(newUser)


#All the imports for the code
import time #To add delays between screen outputs
import os #To clear screen and maybe to get terminal size so things can be properly centered no matter what size the screen is
from colorama import Style, Fore, Back #Will be used to format and make the outputs look better
import random #Will be used to randomize order of questions and to name the Study Buddy
import sys #will be used for its 'sys.exit()' function to quit the program easily at any time
import json #for json writing and reading



#-----------------------------------------------------------
#Global Variable Section
#-----------------------------------------------------------
screenSize = os.get_terminal_size() #This gets the width and height of the terminal, respectively
z = screenSize[0] #Puts the width of the screen into a variable; ("blah blah blah".center(z))
subject = "csp" #sets default subject to Comp Sci

print(Back.BLACK) #sets background to black as default or until changed in user's settings
with open('questions.json', 'r') as file: #loads questions.json into variable 'questions'
    questions = json.load(file)
with open('userinfo.json','r') as file: #loads userinfo.json into variable 'userinfo'
    userinfo = json.load(file)
userAtUser = userinfo["user"] #makes data inside userinfo into an appendable list
#-----------------------------------------------------------
#Study Buddy face options storage
#-----------------------------------------------------------
#print("+-----------------+-----------------+".center(z)) #Face template
#print("|                                   |".center(z))
#print("|                                   |".center(z))
#print("|                                   |".center(z))
#print("|                                   |".center(z))
#print("|                                   |".center(z))
#print("|                                   |".center(z))
#print("|                                   |".center(z))
#print("|                                   |".center(z))
#print("+-----------------+-----------------+".center(z))

def buddy_face_standard_smile():

    print("+-----------------+-----------------+".center(z)) #Normal standard face
    print("|           __         __           |".center(z))
    print("|           ||         ||           |".center(z))
    print("|           ||         ||           |".center(z))
    print("|                                   |".center(z))
    print("|       _____________________       |".center(z))
    print("|        -__             __-        |".center(z))
    print("|           ----_____----           |".center(z))
    print("|                                   |".center(z))
    print("+-----------------+-----------------+".center(z))
def buddy_face_dead():
    print("+-----------------+-----------------+".center(z)) #Dead face
    print("|                                   |".center(z))
    print("|           \/         \/           |".center(z))
    print("|           /\         /\           |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|         _________________         |".center(z))
    print("|                  | | |            |".center(z))
    print("|                   \ /             |".center(z))
    print("+-----------------+-----------------+".center(z))
def buddy_face_unamused():
    print("+-----------------+-----------------+".center(z)) #unamused face
    print("|                                   |".center(z))
    print("|           ||         ||           |".center(z))
    print("|           ||         ||           |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|         ~~~~~~~~~~~~~~~~~         |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("+-----------------+-----------------+".center(z))
def buddy_face_talkOption1():
    print("+-----------------+-----------------+".center(z)) #talking, slight smile
    print("|           __         __           |".center(z))
    print("|           ||         ||           |".center(z))
    print("|           ||         ||           |".center(z))
    print("|                                   |".center(z))
    print("|           _____________           |".center(z))
    print("|          -_           _-          |".center(z))
    print("|             --_____--             |".center(z))
    print("|                                   |".center(z))
    print("+-----------------+-----------------+".center(z))
def buddy_face_talkOption2():
    print("+-----------------+-----------------+".center(z)) #natural talking
    print("|           __         __           |".center(z))
    print("|           ||         ||           |".center(z))
    print("|           ||         ||           |".center(z))
    print("|                                   |".center(z))
    print("|            ___________            |".center(z))
    print("|           |           |           |".center(z))
    print("|            ---_______-            |".center(z))
    print("|                                   |".center(z))
    print("+-----------------+-----------------+".center(z))
def buddy_face_talkOption3():
    print("+-----------------+-----------------+".center(z)) #talking, closed-ish mouth
    print("|           __         __           |".center(z))
    print("|           ||         ||           |".center(z))
    print("|           ||         ||           |".center(z))
    print("|                                   |".center(z))
    print("|               _____               |".center(z))
    print("|              |     |              |".center(z))
    print("|               -___-               |".center(z))
    print("|                                   |".center(z))
    print("+-----------------+-----------------+".center(z))
def buddy_face_question():
    print("+-----------------+-----------------+".center(z)) #raised eyebrow, questioning
    print("|           ==                      |".center(z))
    print("|           ||         __           |".center(z))
    print("|           ||         ||           |".center(z))
    print("|                                   |".center(z))
    print("|       _____________________       |".center(z))
    print("|        -__             __-        |".center(z))
    print("|           ----_____----           |".center(z))
    print("|                                   |".center(z))
    print("+-----------------+-----------------+".center(z))
def buddy_face_setting_attachment():
    print("|                                   |".center(z)) #extension for settings screen
    print("|              SETTINGS             |".center(z))
    print("|                                   |".center(z))
    print("+-----------------+-----------------+".center(z))
def buddy_face_nameplate_attachment():
    print("\n" + (studyBuddyName).center(z) + "\n") #name of study buddy to be displayed

#-----------------------------------------------------------
#Space for all my functions
#-----------------------------------------------------------

def write_to_json(lst):
    """
    Takes new user list, appends it to existing list of users, writes it to json file
    lst (list): List of information to be added to userinfo.json
    Returns nothing
    """
    userAtUser.append(lst)
    with open("userinfo.json","w") as outfile:
        jsonVar = json.dumps(userAtUser,indent=4)
        outfile.write('{\n"user": ' + jsonVar + '\n}')

def add_entry_new_user(newUser, userName, studyBuddyName, password):
    """
    Takes information given in user_intro() and adds to newUser list
    newUser (list): Empty list to be added to
    userName (string): User's chosen username
    studyBuddyName (string): User's chosen study buddy name
    password (string): User's chosen password
    returns appended list newUser
    """
    newUser.append({"name":userName, "password": password, "studybuddyname": studyBuddyName, "subject": "csp","fontColor":"default","screenMode":"dark","gameMode":"quiz","qamount":10,"correct":0,"total":0,"status":"new"})
    return newUser

def write_to_json_updated_settings():
    """
    Updates user's preferences after changing them in settings
    Uses userNum, userDataDict, and userAtUser
    userNum (int): Describes the user's index position in userinfo.json
    userDataDict (dictionary): The python variable that represents the json dictionary
    userAtUser (list): list of users, appendable, equal to userinfo["user"]
    returns nothing
    """
    global userNum
    userAtUser.pop(userNum) #removes the user that is trying to change their settings temporarily, they will be appended with updated settings later
    userAtUser.append(userDataDict) #appends updated user settings
    userNum = -1 #userNum is now set to the -1 because it is the index number, and no matter what the active user is at the end of the list
    with open("userinfo.json","w") as outfile:
        jsonVar = json.dumps(userAtUser,indent=4)
        outfile.write('{\n"user": ' + jsonVar + '\n}') #Fully rewrites json file with new list


def study_buddy_wake_animation():
    """
    Animation to show at start of code
    """

    print("+-----------------+-----------------+".center(z)) 
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.05)
    os.system('clear')

    print("+-----------------+-----------------+".center(z)) 
    print("|                                  0|".center(z))
    print("|1                                  |".center(z))
    print("|                                  0|".center(z))
    print("|0                                  |".center(z))
    print("|                                  1|".center(z))
    print("|1                                  |".center(z))
    print("|                                  0|".center(z))
    print("|1                                  |".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.05)
    os.system('clear')

    print("+-----------------+-----------------+".center(z)) 
    print("|                                 01|".center(z))
    print("|10                                 |".center(z))
    print("|                                 00|".center(z))
    print("|01                                 |".center(z))
    print("|                                 10|".center(z))
    print("|11                                 |".center(z))
    print("|                                 00|".center(z))
    print("|11                                 |".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.05)
    os.system('clear')

    print("+-----------------+-----------------+".center(z)) 
    print("|                                010|".center(z))
    print("|100                                |".center(z))
    print("|                                000|".center(z))
    print("|010                                |".center(z))
    print("|                                100|".center(z))
    print("|110                                |".center(z))
    print("|                                000|".center(z))
    print("|110                                |".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.05)
    os.system('clear')

    print("+-----------------+-----------------+".center(z)) 
    print("|                               0100|".center(z))
    print("|1001                               |".center(z))
    print("|                               0001|".center(z))
    print("|0101                               |".center(z))
    print("|                               1001|".center(z))
    print("|1101                               |".center(z))
    print("|                               0001|".center(z))
    print("|1101                               |".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.05)
    os.system('clear')

    print("+-----------------+-----------------+".center(z)) 
    print("|                              01001|".center(z))
    print("|10010                              |".center(z))
    print("|                              00010|".center(z))
    print("|01010                              |".center(z))
    print("|                              10010|".center(z))
    print("|11010                              |".center(z))
    print("|                              00010|".center(z))
    print("|11010                              |".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.05)
    os.system('clear')

    print("+-----------------+-----------------+".center(z)) 
    print("|                             010010|".center(z))
    print("|100101                             |".center(z))
    print("|                             000101|".center(z))
    print("|010100                             |".center(z))
    print("|                             100101|".center(z))
    print("|110101                             |".center(z))
    print("|                             000101|".center(z))
    print("|110101                             |".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.05)
    os.system('clear')

    print("+-----------------+-----------------+".center(z)) 
    print("|                            0100101|".center(z))
    print("|1001011                            |".center(z))
    print("|                            0001010|".center(z))
    print("|0101001                            |".center(z))
    print("|                            1001010|".center(z))
    print("|1101010                            |".center(z))
    print("|                            0001010|".center(z))
    print("|1101010                            |".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.05)
    os.system('clear')

    print("+-----------------+-----------------+".center(z)) 
    print("|                           01001010|".center(z))
    print("|10010111                           |".center(z))
    print("|                           00010101|".center(z))
    print("|01010011                           |".center(z))
    print("|                           10010101|".center(z))
    print("|11010101                           |".center(z))
    print("|                           00010101|".center(z))
    print("|11010101                           |".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.05)
    os.system('clear')

    print("+-----------------+-----------------+".center(z)) 
    print("|                          010010101|".center(z))
    print("|100101110                          |".center(z))
    print("|                          000101010|".center(z))
    print("|010100111                          |".center(z))
    print("|                          100101010|".center(z))
    print("|110101010                          |".center(z))
    print("|                          000101010|".center(z))
    print("|110101010                          |".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.05)
    os.system('clear')

    print("+-----------------+-----------------+".center(z)) 
    print("|                         0100101010|".center(z))
    print("|1001011101                         |".center(z))
    print("|                         0001010101|".center(z))
    print("|0101001110                         |".center(z))
    print("|                         1001010101|".center(z))
    print("|1101010100                         |".center(z))
    print("|                         0001010100|".center(z))
    print("|1101010100                         |".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.05)
    os.system('clear')

    print("+-----------------+-----------------+".center(z)) 
    print("|                        01001010101|".center(z))
    print("|10010111010                        |".center(z))
    print("|                        00010101010|".center(z))
    print("|01010011101                        |".center(z))
    print("|                        10010101011|".center(z))
    print("|11010101000                        |".center(z))
    print("|                        00010101001|".center(z))
    print("|11010101001                        |".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.05)
    os.system('clear')

    print("+-----------------+-----------------+".center(z)) 
    print("|                       010010101010|".center(z))
    print("|100101110101                       |".center(z))
    print("|                       000101010101|".center(z))
    print("|010100111010                       |".center(z))
    print("|                       100101010111|".center(z))
    print("|110101010001                       |".center(z))
    print("|                       000101010010|".center(z))
    print("|110101010010                       |".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.05)
    os.system('clear')

    print("+-----------------+-----------------+".center(z)) 
    print("|                      0100101010101|".center(z))
    print("|1001011101010                      |".center(z))
    print("|                      0001010101010|".center(z))
    print("|0101001110101                      |".center(z))
    print("|                      1001010101111|".center(z))
    print("|1101010100010                      |".center(z))
    print("|                      0001010100101|".center(z))
    print("|1101010100101                      |".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.05)
    os.system('clear')

    print("+-----------------+-----------------+".center(z)) 
    print("|                     01001010101010|".center(z))
    print("|10010111010101                     |".center(z))
    print("|                     00010101010101|".center(z))
    print("|01010011101010                     |".center(z))
    print("|                     10010101011111|".center(z))
    print("|11010101000101                     |".center(z))
    print("|                     00010101001011|".center(z))
    print("|11010101001010                     |".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.05)
    os.system('clear')

    print("+-----------------+-----------------+".center(z)) 
    print("|                    010010101010100|".center(z))
    print("|100101110101010                    |".center(z))
    print("|                    000101010101011|".center(z))
    print("|010100111010101                    |".center(z))
    print("|                    100101010111110|".center(z))
    print("|110101010001010                    |".center(z))
    print("|                    000101010010110|".center(z))
    print("|110101010010101                    |".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.05)
    os.system('clear')

    print("+-----------------+-----------------+".center(z)) 
    print("|                   0100101010101001|".center(z))
    print("|1001011101010101                   |".center(z))
    print("|                   0001010101010111|".center(z))
    print("|0101001110101010                   |".center(z))
    print("|                   1001010101111100|".center(z))
    print("|1101010100010101                   |".center(z))
    print("|                   0001010100101100|".center(z))
    print("|1101010100101010                   |".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.05)
    os.system('clear')

    print("+-----------------+-----------------+".center(z)) 
    print("|                  01001010101010010|".center(z))
    print("|10010111010101010                  |".center(z))
    print("|                  00010101010101110|".center(z))
    print("|01010011101010101                  |".center(z))
    print("|                  10010101011111000|".center(z))
    print("|11010101000101010                  |".center(z))
    print("|                  00010101001011000|".center(z))
    print("|11010101001010101                  |".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.05)
    os.system('clear')

    print("+-----------------+-----------------+".center(z)) 
    print("|                 010010101010100101|".center(z))
    print("|100101110101010101                 |".center(z))
    print("|                 000101010101011101|".center(z))
    print("|010100111010101010                 |".center(z))
    print("|                 100101010111110001|".center(z))
    print("|110101010001010101                 |".center(z))
    print("|                 000101010010110001|".center(z))
    print("|110101010010101010                 |".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.05)
    os.system('clear')

    print("+-----------------+-----------------+".center(z)) 
    print("|                0100101010101001010|".center(z))
    print("|1001011101010101010                |".center(z))
    print("|                0001010101010111011|".center(z))
    print("|0101001110101010101                |".center(z))
    print("|                1001010101111100010|".center(z))
    print("|1101010100010101010                |".center(z))
    print("|                0001010100101100010|".center(z))
    print("|1101010100101010101                |".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.05)
    os.system('clear')

    print("+-----------------+-----------------+".center(z)) 
    print("|               01001010101010010101|".center(z))
    print("|10010111010101010101               |".center(z))
    print("|               00010101010101110110|".center(z))
    print("|01010011101010101010               |".center(z))
    print("|               10010101011111000101|".center(z))
    print("|11010101000101010101               |".center(z))
    print("|               00010101001011000101|".center(z))
    print("|11010101001010101010               |".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.05)
    os.system('clear')

    print("+-----------------+-----------------+".center(z)) 
    print("|              010010101010100101010|".center(z))
    print("|100101110101010101010              |".center(z))
    print("|              000101010101011101101|".center(z))
    print("|010100111010101010101              |".center(z))
    print("|              100101010111110001010|".center(z))
    print("|110101010001010101011              |".center(z))
    print("|              000101010010110001010|".center(z))
    print("|110101010010101010101              |".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.05)
    os.system('clear')

    print("+-----------------+-----------------+".center(z)) 
    print("|             0100101010101001010100|".center(z))
    print("|1001011101010101010101             |".center(z))
    print("|             0001010101010111011010|".center(z))
    print("|0101001110101010101010             |".center(z))
    print("|             1001010101111100010101|".center(z))
    print("|1101010100010101010110             |".center(z))
    print("|             0001010100101100010101|".center(z))
    print("|1101010100101010101010             |".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.05)
    os.system('clear')

    print("+-----------------+-----------------+".center(z)) 
    print("|            01001010101010010101001|".center(z))
    print("|10010111010101010101010            |".center(z))
    print("|            00010101010101110110101|".center(z))
    print("|01010011101010101010100            |".center(z))
    print("|            10010101011111000101010|".center(z))
    print("|11010101000101010101101            |".center(z))
    print("|            00010101001011000101011|".center(z))
    print("|11010101001010101010101            |".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.05)
    os.system('clear')

    print("+-----------------+-----------------+".center(z)) 
    print("|           010010101010100101010010|".center(z))
    print("|100101110101010101010101           |".center(z))
    print("|           000101010101011101101010|".center(z))
    print("|010100111010101010101001           |".center(z))
    print("|           100101010111110001010101|".center(z))
    print("|110101010001010101011010           |".center(z))
    print("|           000101010010110001010110|".center(z))
    print("|110101010010101010101010           |".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.05)
    os.system('clear')

    print("+-----------------+-----------------+".center(z)) 
    print("|          0100101010101001010100101|".center(z))
    print("|1001011101010101010101010          |".center(z))
    print("|          0001010101010111011010101|".center(z))
    print("|0101001110101010101010010          |".center(z))
    print("|          1001010101111100010101010|".center(z))
    print("|1101010100010101010110101          |".center(z))
    print("|          0001010100101100010101101|".center(z))
    print("|1101010100101010101010101          |".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.05)
    os.system('clear')

    print("+-----------------+-----------------+".center(z)) 
    print("|         01001010101010010101001010|".center(z))
    print("|10010111010101010101010101         |".center(z))
    print("|         00010101010101110110101010|".center(z))
    print("|01010011101010101010100101         |".center(z))
    print("|         10010101011111000101010101|".center(z))
    print("|11010101000101010101101011         |".center(z))
    print("|         00010101001011000101011010|".center(z))
    print("|11010101001010101010101010         |".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.05)
    os.system('clear')

    print("+-----------------+-----------------+".center(z)) 
    print("|        010010101010100101010010100|".center(z))
    print("|100101110101010101010101010        |".center(z))
    print("|        000101010101011101101010101|".center(z))
    print("|010100111010101010101001010        |".center(z))
    print("|        100101010111110001010101010|".center(z))
    print("|110101010001010101011010110        |".center(z))
    print("|        000101010010110001010110101|".center(z))
    print("|110101010010101010101010101        |".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.05)
    os.system('clear')

    print("+-----------------+-----------------+".center(z)) 
    print("|       0100101010101001010100101001|".center(z))
    print("|1001011101010101010101010101       |".center(z))
    print("|       0001010101010111011010101010|".center(z))
    print("|0101001110101010101010010101       |".center(z))
    print("|       1001010101111100010101010100|".center(z))
    print("|1101010100010101010110101101       |".center(z))
    print("|       0001010100101100010101101010|".center(z))
    print("|1101010100101010101010101010       |".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.05)
    os.system('clear')

    print("+-----------------+-----------------+".center(z)) 
    print("|      01001010101010010101001010011|".center(z))
    print("|10010111010101010101010101010      |".center(z))
    print("|      00010101010101110110101010101|".center(z))
    print("|01010011101010101010100101010      |".center(z))
    print("|      10010101011111000101010101001|".center(z))
    print("|11010101000101010101101011010      |".center(z))
    print("|      00010101001011000101011010101|".center(z))
    print("|11010101001010101010101010101      |".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.05)
    os.system('clear')

    print("+-----------------+-----------------+".center(z)) 
    print("|     010010101010100101010010100111|".center(z))
    print("|100101110101010101010101010101     |".center(z))
    print("|     000101010101011101101010101011|".center(z))
    print("|010100111010101010101001010101     |".center(z))
    print("|     100101010111110001010101010010|".center(z))
    print("|110101010001010101011010110100     |".center(z))
    print("|     000101010010110001010110101010|".center(z))
    print("|110101010010101010101010101010     |".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.05)
    os.system('clear')

    print("+-----------------+-----------------+".center(z)) 
    print("|    0100101010101001010100101001110|".center(z))
    print("|1001011101010101010101010101010    |".center(z))
    print("|    0001010101010111011010101010111|".center(z))
    print("|0101001110101010101010010101010    |".center(z))
    print("|    1001010101111100010101010100101|".center(z))
    print("|1101010100010101010110101101001    |".center(z))
    print("|    0001010100101100010101101010100|".center(z))
    print("|1101010100101010101010101010101    |".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.05)
    os.system('clear')

    print("+-----------------+-----------------+".center(z)) 
    print("|   01001010101010010101001010011100|".center(z))
    print("|10010111010101010101010101010101   |".center(z))
    print("|   00010101010101110110101010101111|".center(z))
    print("|01010011101010101010100101010101   |".center(z))
    print("|   10010101011111000101010101001010|".center(z))
    print("|11010101000101010101101011010010   |".center(z))
    print("|   00010101001011000101011010101001|".center(z))
    print("|11010101001010101010101010101011   |".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.05)
    os.system('clear')

    print("+-----------------+-----------------+".center(z)) 
    print("|  010010101010100101010010100111001|".center(z))
    print("|100101110101010101010101010101010  |".center(z))
    print("|  000101010101011101101010101011110|".center(z))
    print("|010100111010101010101001010101010  |".center(z))
    print("|  100101010111110001010101010010101|".center(z))
    print("|110101010001010101011010110100101  |".center(z))
    print("|  000101010010110001010110101010011|".center(z))
    print("|110101010010101010101010101010110  |".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.05)
    os.system('clear')

    print("+-----------------+-----------------+".center(z)) 
    print("| 0100101010101001010100101001110011|".center(z))
    print("|1001011101010101010101010101010101 |".center(z))
    print("| 0001010101010111011010101010111100|".center(z))
    print("|0101001110101010101010010101010101 |".center(z))
    print("| 1001010101111100010101010100101010|".center(z))
    print("|1101010100010101010110101101001010 |".center(z))
    print("| 0001010100101100010101101010100110|".center(z))
    print("|1101010100101010101010101010101101 |".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.05)
    os.system('clear')

    print("+-----------------+-----------------+".center(z)) #FULL SCREEN
    print("|01001010101010010101001010011100110|".center(z))
    print("|10010111010101010101010101010101010|".center(z))
    print("|00010101010101110110101010101111001|".center(z))
    print("|01010011101010101010100101010101010|".center(z))
    print("|10010101011111000101010101001010101|".center(z))
    print("|11010101000101010101101011010010101|".center(z))
    print("|00010101001011000101011010101001100|".center(z))
    print("|11010101001010101010101010101011010|".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.05)
    os.system('clear')

    print("+-----------------+-----------------+".center(z)) 
    print("|1001010101010010101001010011100110 |".center(z))
    print("| 1001011101010101010101010101010101|".center(z))
    print("|0010101010101110110101010101111001 |".center(z))
    print("| 0101001110101010101010010101010101|".center(z))
    print("|0010101011111000101010101001010101 |".center(z))
    print("| 1101010100010101010110101101001010|".center(z))
    print("|0010101001011000101011010101001100 |".center(z))
    print("| 1101010100101010101010101010101101|".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.05)
    os.system('clear')

    print("+-----------------+-----------------+".center(z)) 
    print("|001010101010010101001010011100110  |".center(z))
    print("|  100101110101010101010101010101010|".center(z))
    print("|010101010101110110101010101111001  |".center(z))
    print("|  010100111010101010101001010101010|".center(z))
    print("|010101011111000101010101001010101  |".center(z))
    print("|  110101010001010101011010110100101|".center(z))
    print("|010101001011000101011010101001100  |".center(z))
    print("|  110101010010101010101010101010110|".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.05)
    os.system('clear')

    print("+-----------------+-----------------+".center(z)) 
    print("|01010101010010101001010011100110   |".center(z))
    print("|   10010111010101010101010101010101|".center(z))
    print("|10101010101110110101010101111001   |".center(z))
    print("|   01010011101010101010100101010101|".center(z))
    print("|10101011111000101010101001010101   |".center(z))
    print("|   11010101000101010101101011010010|".center(z))
    print("|10101001011000101011010101001100   |".center(z))
    print("|   11010101001010101010101010101011|".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.05)
    os.system('clear')

    print("+-----------------+-----------------+".center(z)) 
    print("|1010101010010101001010011100110    |".center(z))
    print("|    1001011101010101010101010101010|".center(z))
    print("|0101010101110110101010101111001    |".center(z))
    print("|    0101001110101010101010010101010|".center(z))
    print("|0101011111000101010101001010101    |".center(z))
    print("|    1101010100010101010110101101001|".center(z))
    print("|0101001011000101011010101001100    |".center(z))
    print("|    1101010100101010101010101010101|".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.05)
    os.system('clear')

    print("+-----------------+-----------------+".center(z)) 
    print("|010101010010101001010011100110     |".center(z))
    print("|     100101110101010101010101010101|".center(z))
    print("|101010101110110101010101111001     |".center(z))
    print("|     010100111010101010101001010101|".center(z))
    print("|101011111000101010101001010101     |".center(z))
    print("|     110101010001010101011010110100|".center(z))
    print("|101001011000101011010101001100     |".center(z))
    print("|     110101010010101010101010101010|".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.05)
    os.system('clear')

    print("+-----------------+-----------------+".center(z)) 
    print("|10101010010101001010011100110      |".center(z))
    print("|      10010111010101010101010101010|".center(z))
    print("|01010101110110101010101111001      |".center(z))
    print("|      01010011101010101010100101010|".center(z))
    print("|01011111000101010101001010101      |".center(z))
    print("|      11010101000101010101101011010|".center(z))
    print("|01001011000101011010101001100      |".center(z))
    print("|      11010101001010101010101010101|".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.05)
    os.system('clear')

    print("+-----------------+-----------------+".center(z)) 
    print("|0101010010101001010011100110       |".center(z))
    print("|       1001011101010101010101010101|".center(z))
    print("|1010101110110101010101111001       |".center(z))
    print("|       0101001110101010101010010101|".center(z))
    print("|1011111000101010101001010101       |".center(z))
    print("|       1101010100010101010110101101|".center(z))
    print("|1001011000101011010101001100       |".center(z))
    print("|       1101010100101010101010101010|".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.05)
    os.system('clear')

    print("+-----------------+-----------------+".center(z)) 
    print("|101010010101001010011100110        |".center(z))
    print("|        100101110101010101010101010|".center(z))
    print("|010101110110101010101111001        |".center(z))
    print("|        010100111010101010101001010|".center(z))
    print("|011111000101010101001010101        |".center(z))
    print("|        110101010001010101011010110|".center(z))
    print("|001011000101011010101001100        |".center(z))
    print("|        110101010010101010101010101|".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.05)
    os.system('clear')

    print("+-----------------+-----------------+".center(z)) 
    print("|01010010101001010011100110         |".center(z))
    print("|         10010111010101010101010101|".center(z))
    print("|10101110110101010101111001         |".center(z))
    print("|         01010011101010101010100101|".center(z))
    print("|11111000101010101001010101         |".center(z))
    print("|         11010101000101010101101011|".center(z))
    print("|01011000101011010101001100         |".center(z))
    print("|         11010101001010101010101010|".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.05)
    os.system('clear')

    print("+-----------------+-----------------+".center(z)) 
    print("|1010010101001010011100110          |".center(z))
    print("|          1001011101010101010101010|".center(z))
    print("|0101110110101010101111001          |".center(z))
    print("|          0101001110101010101010010|".center(z))
    print("|1111000101010101001010101          |".center(z))
    print("|          1101010100010101010110101|".center(z))
    print("|1011000101011010101001100          |".center(z))
    print("|          1101010100101010101010101|".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.05)
    os.system('clear')

    print("+-----------------+-----------------+".center(z)) 
    print("|010010101001010011100110           |".center(z))
    print("|           100101110101010101010101|".center(z))
    print("|101110110101010101111001           |".center(z))
    print("|           010100111010101010101001|".center(z))
    print("|111000101010101001010101           |".center(z))
    print("|           110101010001010101011010|".center(z))
    print("|011000101011010101001100           |".center(z))
    print("|           110101010010101010101010|".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.05)
    os.system('clear')

    print("+-----------------+-----------------+".center(z)) 
    print("|10010101001010011100110            |".center(z))
    print("|            10010111010101010101010|".center(z))
    print("|01110110101010101111001            |".center(z))
    print("|            01010011101010101010100|".center(z))
    print("|11000101010101001010101            |".center(z))
    print("|            11010101000101010101101|".center(z))
    print("|11000101011010101001100            |".center(z))
    print("|            11010101001010101010101|".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.05)
    os.system('clear')

    print("+-----------------+-----------------+".center(z)) 
    print("|0010101001010011100110             |".center(z))
    print("|             1001011101010101010101|".center(z))
    print("|1110110101010101111001             |".center(z))
    print("|             0101001110101010101010|".center(z))
    print("|1000101010101001010101             |".center(z))
    print("|             1101010100010101010110|".center(z))
    print("|1000101011010101001100             |".center(z))
    print("|             1101010100101010101010|".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.05)
    os.system('clear')

    print("+-----------------+-----------------+".center(z)) 
    print("|010101001010011100110              |".center(z))
    print("|              100101110101010101010|".center(z))
    print("|110110101010101111001              |".center(z))
    print("|              010100111010101010101|".center(z))
    print("|000101010101001010101              |".center(z))
    print("|              110101010001010101011|".center(z))
    print("|000101011010101001100              |".center(z))
    print("|              110101010010101010101|".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.05)
    os.system('clear')

    print("+-----------------+-----------------+".center(z)) 
    print("|10101001010011100110               |".center(z))
    print("|               10010111010101010101|".center(z))
    print("|10110101010101111001               |".center(z))
    print("|               01010011101010101010|".center(z))
    print("|00101010101001010101               |".center(z))
    print("|               11010101000101010101|".center(z))
    print("|00101011010101001100               |".center(z))
    print("|               11010101001010101010|".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.05)
    os.system('clear')

    print("+-----------------+-----------------+".center(z)) 
    print("|0101001010011100110                |".center(z))
    print("|                1001011101010101010|".center(z))
    print("|0110101010101111001                |".center(z))
    print("|                0101001110101010101|".center(z))
    print("|0101010101001010101                |".center(z))
    print("|                1101010100010101010|".center(z))
    print("|0101011010101001100                |".center(z))
    print("|                1101010100101010101|".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.05)
    os.system('clear')

    print("+-----------------+-----------------+".center(z)) 
    print("|101001010011100110                 |".center(z))
    print("|                 100101110101010101|".center(z))
    print("|110101010101111001                 |".center(z))
    print("|                 010100111010101010|".center(z))
    print("|101010101001010101                 |".center(z))
    print("|                 110101010001010101|".center(z))
    print("|101011010101001100                 |".center(z))
    print("|                 110101010010101010|".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.05)
    os.system('clear')

    print("+-----------------+-----------------+".center(z)) 
    print("|01001010011100110                  |".center(z))
    print("|                  10010111010101010|".center(z))
    print("|10101010101111001                  |".center(z))
    print("|                  01010011101010101|".center(z))
    print("|01010101001010101                  |".center(z))
    print("|                  11010101000101010|".center(z))
    print("|01011010101001100                  |".center(z))
    print("|                  11010101001010101|".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.05)
    os.system('clear')

    print("+-----------------+-----------------+".center(z)) 
    print("|1001010011100110                   |".center(z))
    print("|                   1001011101010101|".center(z))
    print("|0101010101111001                   |".center(z))
    print("|                   0101001110101010|".center(z))
    print("|1010101001010101                   |".center(z))
    print("|                   1101010100010101|".center(z))
    print("|1011010101001100                   |".center(z))
    print("|                   1101010100101010|".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.05)
    os.system('clear')

    print("+-----------------+-----------------+".center(z)) 
    print("|001010011100110                    |".center(z))
    print("|                    100101110101010|".center(z))
    print("|101010101111001                    |".center(z))
    print("|                    010100111010101|".center(z))
    print("|010101001010101                    |".center(z))
    print("|                    110101010001010|".center(z))
    print("|011010101001100                    |".center(z))
    print("|                    110101010010101|".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.05)
    os.system('clear')

    print("+-----------------+-----------------+".center(z)) 
    print("|01010011100110                     |".center(z))
    print("|                     10010111010101|".center(z))
    print("|01010101111001                     |".center(z))
    print("|                     01010011101010|".center(z))
    print("|10101001010101                     |".center(z))
    print("|                     11010101000101|".center(z))
    print("|11010101001100                     |".center(z))
    print("|                     11010101001010|".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.05)
    os.system('clear')

    print("+-----------------+-----------------+".center(z)) 
    print("|1010011100110                      |".center(z))
    print("|                      1001011101010|".center(z))
    print("|1010101111001                      |".center(z))
    print("|                      0101001110101|".center(z))
    print("|0101001010101                      |".center(z))
    print("|                      1101010100010|".center(z))
    print("|1010101001100                      |".center(z))
    print("|                      1101010100101|".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.05)
    os.system('clear')

    print("+-----------------+-----------------+".center(z)) 
    print("|010011100110                       |".center(z))
    print("|                       100101110101|".center(z))
    print("|010101111001                       |".center(z))
    print("|                       010100111010|".center(z))
    print("|101001010101                       |".center(z))
    print("|                       110101010001|".center(z))
    print("|010101001100                       |".center(z))
    print("|                       110101010010|".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.05)
    os.system('clear')

    print("+-----------------+-----------------+".center(z)) 
    print("|10011100110                        |".center(z))
    print("|                        10010111010|".center(z))
    print("|10101111001                        |".center(z))
    print("|                        01010011101|".center(z))
    print("|01001010101                        |".center(z))
    print("|                        11010101000|".center(z))
    print("|10101001100                        |".center(z))
    print("|                        11010101001|".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.05)
    os.system('clear')

    print("+-----------------+-----------------+".center(z)) 
    print("|0011100110                         |".center(z))
    print("|                         1001011101|".center(z))
    print("|0101111001                         |".center(z))
    print("|                         0101001110|".center(z))
    print("|1001010101                         |".center(z))
    print("|                         1101010100|".center(z))
    print("|0101001100                         |".center(z))
    print("|                         1101010100|".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.05)
    os.system('clear')

    print("+-----------------+-----------------+".center(z)) 
    print("|011100110                          |".center(z))
    print("|                          100101110|".center(z))
    print("|101111001                          |".center(z))
    print("|                          010100111|".center(z))
    print("|001010101                          |".center(z))
    print("|                          110101010|".center(z))
    print("|101001100                          |".center(z))
    print("|                          110101010|".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.05)
    os.system('clear')

    print("+-----------------+-----------------+".center(z)) 
    print("|11100110                           |".center(z))
    print("|                           10010111|".center(z))
    print("|01111001                           |".center(z))
    print("|                           01010011|".center(z))
    print("|01010101                           |".center(z))
    print("|                           11010101|".center(z))
    print("|01001100                           |".center(z))
    print("|                           11010101|".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.05)
    os.system('clear')

    print("+-----------------+-----------------+".center(z)) 
    print("|1100110                            |".center(z))
    print("|                            1001011|".center(z))
    print("|1111001                            |".center(z))
    print("|                            0101001|".center(z))
    print("|1010101                            |".center(z))
    print("|                            1101010|".center(z))
    print("|1001100                            |".center(z))
    print("|                            1101010|".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.05)
    os.system('clear')

    print("+-----------------+-----------------+".center(z)) 
    print("|100110                             |".center(z))
    print("|                             100101|".center(z))
    print("|111001                             |".center(z))
    print("|                             010100|".center(z))
    print("|010101                             |".center(z))
    print("|                             110101|".center(z))
    print("|001100                             |".center(z))
    print("|                             110101|".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.05)
    os.system('clear')

    print("+-----------------+-----------------+".center(z)) 
    print("|00110                              |".center(z))
    print("|                              10010|".center(z))
    print("|11001                              |".center(z))
    print("|                              01010|".center(z))
    print("|10101                              |".center(z))
    print("|                              11010|".center(z))
    print("|01100                              |".center(z))
    print("|                              11010|".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.05)
    os.system('clear')

    print("+-----------------+-----------------+".center(z)) 
    print("|0110                               |".center(z))
    print("|                               1001|".center(z))
    print("|1001                               |".center(z))
    print("|                               0101|".center(z))
    print("|0101                               |".center(z))
    print("|                               1101|".center(z))
    print("|1100                               |".center(z))
    print("|                               1101|".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.05)
    os.system('clear')

    print("+-----------------+-----------------+".center(z)) 
    print("|110                                |".center(z))
    print("|                                100|".center(z))
    print("|001                                |".center(z))
    print("|                                010|".center(z))
    print("|101                                |".center(z))
    print("|                                110|".center(z))
    print("|100                                |".center(z))
    print("|                                110|".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.05)
    os.system('clear')

    print("+-----------------+-----------------+".center(z)) 
    print("|10                                 |".center(z))
    print("|                                 10|".center(z))
    print("|01                                 |".center(z))
    print("|                                 01|".center(z))
    print("|01                                 |".center(z))
    print("|                                 11|".center(z))
    print("|00                                 |".center(z))
    print("|                                 11|".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.05)
    os.system('clear')

    print("+-----------------+-----------------+".center(z)) 
    print("|0                                  |".center(z))
    print("|                                  1|".center(z))
    print("|1                                  |".center(z))
    print("|                                  0|".center(z))
    print("|1                                  |".center(z))
    print("|                                  1|".center(z))
    print("|0                                  |".center(z))
    print("|                                  1|".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.05)
    os.system('clear')

    print("+-----------------+-----------------+".center(z)) #PIT STOP: if you found this, take a break from scrolling through this long animation.
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(1)
    os.system('clear')

    print("+-----------------+-----------------+".center(z)) 
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|            |                      |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.05)
    os.system('clear')

    print("+-----------------+-----------------+".center(z)) 
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|            S|                     |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.05)
    os.system('clear')

    print("+-----------------+-----------------+".center(z)) 
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|            ST|                    |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.05)
    os.system('clear')

    print("+-----------------+-----------------+".center(z)) 
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|            STA|                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.05)
    os.system('clear')

    print("+-----------------+-----------------+".center(z)) 
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|            STAR|                  |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.05)
    os.system('clear')

    print("+-----------------+-----------------+".center(z)) 
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|            START|                 |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.05)
    os.system('clear')

    print("+-----------------+-----------------+".center(z)) 
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|            STARTI|                |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.05)
    os.system('clear')

    print("+-----------------+-----------------+".center(z)) 
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|            STARTIB|                |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.05)
    os.system('clear')

    print("+-----------------+-----------------+".center(z)) 
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|            STARTIBG|              |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.5)
    os.system('clear')

    print("+-----------------+-----------------+".center(z)) 
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|            STARTIB|               |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.25)
    os.system('clear')

    print("+-----------------+-----------------+".center(z)) 
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|            STARTI|                |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.5)
    os.system('clear')

    print("+-----------------+-----------------+".center(z)) 
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|            STARTIN|               |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.05)
    os.system('clear')

    print("+-----------------+-----------------+".center(z)) 
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|            STARTING|              |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.05)
    os.system('clear')

    print("+-----------------+-----------------+".center(z)) 
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|            STARTING |             |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.25)
    os.system('clear')

    print("+-----------------+-----------------+".center(z)) 
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|            STARTING U|            |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.05)
    os.system('clear')

    print("+-----------------+-----------------+".center(z)) 
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|            STARTING UP|           |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.35)
    os.system('clear')

    print("+-----------------+-----------------+".center(z)) 
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|            STARTING UP            |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.35)
    os.system('clear')

    print("+-----------------+-----------------+".center(z)) 
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|            STARTING UP|           |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.35)
    os.system('clear')

    print("+-----------------+-----------------+".center(z)) 
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|            STARTING UP            |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.35)
    os.system('clear')

    print("+-----------------+-----------------+".center(z)) 
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|            STARTING UP|           |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.35)
    os.system('clear')

    print("+-----------------+-----------------+".center(z)) 
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|            STARTING UP            |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.35)
    os.system('clear')

    print("+-----------------+-----------------+".center(z)) 
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|            STARTING UP|           |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.35)
    os.system('clear')

    print("+-----------------+-----------------+".center(z)) 
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|            STARTING UP            |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.35)
    os.system('clear')

    print("+-----------------+-----------------+".center(z)) 
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.5)
    os.system('clear')

    print("+-----------------+-----------------+".center(z)) 
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(1)
    os.system('clear')

    print("+-----------------+-----------------+".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|               _____               |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.05)
    os.system('clear')

    print("+-----------------+-----------------+".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|           _____________           |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.05)
    os.system('clear')

    print("+-----------------+-----------------+".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|       _____________________       |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(1)
    os.system('clear')

    print("+-----------------+-----------------+".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|           __         __           |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|       _____________________       |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.05)
    os.system('clear')

    print("+-----------------+-----------------+".center(z))
    print("|                                   |".center(z))
    print("|           __         __           |".center(z))
    print("|           ||         ||           |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|       _____________________       |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.05)
    os.system('clear')

    print("+-----------------+-----------------+".center(z))
    print("|           __         __           |".center(z))
    print("|           ||         ||           |".center(z))
    print("|           ||         ||           |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|       _____________________       |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(1)
    os.system('clear')

    print("+-----------------+-----------------+".center(z))
    print("|          __         __            |".center(z))
    print("|          ||         ||            |".center(z))
    print("|          ||         ||            |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|       _____________________       |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.05)
    os.system('clear')

    print("+-----------------+-----------------+".center(z))
    print("|         __         __             |".center(z))
    print("|         ||         ||             |".center(z))
    print("|         ||         ||             |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|       _____________________       |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.75)
    os.system('clear')

    print("+-----------------+-----------------+".center(z))
    print("|          __         __            |".center(z))
    print("|          ||         ||            |".center(z))
    print("|          ||         ||            |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|       _____________________       |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.05)
    os.system('clear')

    print("+-----------------+-----------------+".center(z))
    print("|           __         __           |".center(z))
    print("|           ||         ||           |".center(z))
    print("|           ||         ||           |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|       _____________________       |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.05)
    os.system('clear')

    print("+-----------------+-----------------+".center(z))
    print("|            __         __          |".center(z))
    print("|            ||         ||          |".center(z))
    print("|            ||         ||          |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|       _____________________       |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.05)
    os.system('clear')

    print("+-----------------+-----------------+".center(z))
    print("|             __         __         |".center(z))
    print("|             ||         ||         |".center(z))
    print("|             ||         ||         |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|       _____________________       |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.75)
    os.system('clear')

    print("+-----------------+-----------------+".center(z))
    print("|            __         __          |".center(z))
    print("|            ||         ||          |".center(z))
    print("|            ||         ||          |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|       _____________________       |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.05)
    os.system('clear')

    print("+-----------------+-----------------+".center(z))
    print("|           __         __           |".center(z))
    print("|           ||         ||           |".center(z))
    print("|           ||         ||           |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|       _____________________       |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(1)
    os.system('clear')

    print("+-----------------+-----------------+".center(z))
    print("|           __         __           |".center(z))
    print("|           ||         ||           |".center(z))
    print("|           ||         ||           |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|       _____________________       |".center(z))
    print("|               _____               |".center(z))
    print("|                                   |".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.05)
    os.system('clear')

    print("+-----------------+-----------------+".center(z))
    print("|           __         __           |".center(z))
    print("|           ||         ||           |".center(z))
    print("|           ||         ||           |".center(z))
    print("|                                   |".center(z))
    print("|                                   |".center(z))
    print("|       _____________________       |".center(z))
    print("|           ----_____----           |".center(z))
    print("|                                   |".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.05)
    os.system('clear')

    print("+-----------------+-----------------+".center(z))
    print("|           __         __           |".center(z))
    print("|           ||         ||           |".center(z))
    print("|           ||         ||           |".center(z))
    print("|                                   |".center(z))
    print("|       _____________________       |".center(z))
    print("|        --               --        |".center(z))
    print("|           ----_____----           |".center(z))
    print("|                                   |".center(z))
    print("+-----------------+-----------------+".center(z))

    time.sleep(0.05)
    os.system('clear')
    buddy_face_standard_smile()
    time.sleep(2)
def help_animation():
    """
    What first-time users and anyone who types help will see, gives instructions on what to do and what command words work and what they do
    """
    os.system('clear')
    buddy_face_talkOption1()
    print("")
    print(f"Hey there {userName}! I am your Study Buddy, but you can call me {studyBuddyName}".center(z))
    time.sleep(2.5)
    print("")
    print("Press ENTER to continue".center(z))
    input()
    os.system('clear')
    buddy_face_talkOption3()
    print("")
    print("If you want to change your preferences or check your stats, type SETTINGS".center(z))
    time.sleep(2.5)
    print("")
    print("Press ENTER to continue".center(z))
    input()
    os.system('clear')
    buddy_face_talkOption2()
    print("")
    print("At any point in time, type HELP for a hint or QUIT to shut me down".center(z))
    time.sleep(2.5)
    print("")
    print("Press ENTER to continue".center(z))
    input()
    os.system('clear')
    userDataDict['status'] = "cleared"
    write_to_json_updated_settings()
def user_intro():
    """
    Given upon entrance, user can log in or sign up, if they sign up then newUser is returned, if they log in then studyBuddyName, userName, userNum, password, subject, fontColor, screenMode, gameMode, qAmount, progBarSects, and userDataDict are returned
    newUser (list): empty list have preferences appended to
    studyBuddyName (string): name of study buddy
    userName (string): name of user
    userNum (int): user's index number in userinfo.json file
    password (string): user's password saved to a variable to be checked later in settings if they want to change sensitive info
    subject (string): preferred subject (default for new user)
    fontColor (string): preferred font color (default for new user)
    screenMode (string): preferred screen mode (dark for new user)
    gameMode (string): preferred game mode (quiz for new user)
    qAmount (int): preferred number of questions for quiz game mode (10 for new user)
    progBarSects (int): gives number of '*' to be printed for the progress bar for each section based on the number of questions user is being quizzed on and size of screen
    userDataDict (dictionary): Logged in user's data as a dictionary so it can be changed if they change it later in settings
    """
    global studyBuddyName
    global userName
    global userNum
    global userinfo
    global password
    global subject
    global fontColor
    global screenMode
    global gameMode
    global qAmount
    global progBarSects
    global userDataDict
    returnVar = "false"
    userNum = ""
    while True:
        with open('userinfo.json','r') as file:
            userinfo = json.load(file)
        
        os.system('clear')
        buddy_face_standard_smile()
        print("")
        print("Have an account already? Type log in!".center(z))
        print("\n" + "Need an account? Type sign up!".center(z))
        logOrSign = input()
        if logOrSign.lower() == "log in": 
            while True:
                os.system('clear')
                buddy_face_standard_smile()
                print("")
                print("Username: ".center(z))
                usernameCheck = input()
                print("Password: ".center(z))
                passwordCheck = input()
                for user in range(len(userAtUser)):
                    if usernameCheck == userinfo["user"][user]["name"]:  #sets a variable to true if username matches something in userinfo
                        userName = usernameCheck
                        userNum = user
                        returnVar = "true"
                        break
                    else:
                        pass
                if returnVar == "true":
                    if passwordCheck == userinfo["user"][userNum]["password"]: #checks that the password matches the saved password of the username given before
                        returnVar = "pass"
                        userName = usernameCheck
                        userNum = user
                        password = userinfo["user"][userNum]["password"]
                        studyBuddyName = userinfo["user"][userNum]["studybuddyname"]
                        subject = userinfo["user"][userNum]["subject"]
                        fontColor = userinfo["user"][userNum]["fontColor"]
                        screenMode = userinfo["user"][userNum]["screenMode"]
                        gameMode = userinfo["user"][userNum]["gameMode"]
                        qAmount = userinfo["user"][userNum]["qamount"]
                        userDataDict = userinfo["user"][userNum]
                        progBarSects = int((z-17)/qAmount) - 1 #-1 to determine how many '#' to print for progress bar excluding '|' and -17 because that is how many characters are used on that line that should be excluded from the calculation of screen sizing
                    else:
                        returnVar = "false"
                    if returnVar == "pass":
                        break
                    else:
                        pass
                if returnVar == "false":
                    os.system('clear')
                    buddy_face_unamused()
                    print("")
                    print(Fore.RED + Style.BRIGHT + "Your username or password is incorrect!".center(z) + Fore.RESET + Style.NORMAL)
                    time.sleep(3)
                    break
        elif logOrSign.lower() == "sign up":
            userNameMatch = ""
            checkInfo = ""
            userNameCorrect = ""
            while True:
                os.system('clear')
                buddy_face_standard_smile()
                print("")
                print("Create a username: ".center(z))
                userName = input()
                print("Create a password: ".center(z))
                password = input()
                for user in range(len(userAtUser)):
                    if userName == userinfo["user"][user]["name"]: #checks to see if a username is already taken, if it is then local variable userNameMatch is not set to p to let the code know later that the username is taken
                        userNameMatch = "fail"
                    else:
                        pass
                if len(userName) < 5 or len(userName) > 15:
                    os.system('clear')
                    buddy_face_talkOption1()
                    print("")
                    print(Fore.RED + Style.BRIGHT + "Username must be between 5 and 15 digits!".center(z) + Fore.RESET + Style.NORMAL)
                    time.sleep(3)
                    break
                elif len(password) < 8 or len(password) > 24:
                    os.system('clear')
                    buddy_face_talkOption3()
                    print("")
                    print(Fore.RED + Style.BRIGHT + "Password must be between 8 and 24 digits!".center(z) + Fore.RESET + Style.NORMAL)
                    time.sleep(3)
                    break
                elif userNameMatch == "fail":
                    os.system('clear')
                    buddy_face_talkOption3()
                    print("")
                    print(Fore.RED + Style.BRIGHT + "That username is already taken!".center(z) + Fore.RESET + Style.NORMAL)
                    time.sleep(3)
                    break
                else:
                    userNameCorrect = "p"

                if userNameCorrect == "p":
                    while True:
                        os.system('clear')
                        buddy_face_question()
                        print("")
                        print(f"Username: {userName}".center(z) + "\n" + (f"Password: {password[0]}{password[1]}" + ("*" * (len(password) - 3)) + f"{password[-1]}").center(z) + "\n" + "Does this information look correct?".center(z)) #neat little display of username and password with password being covered up
                        checkInfo = input()
                        if checkInfo.lower() == "yes":
                            break
                        elif checkInfo.lower() == "no":
                            break
                        else:
                            pass
                    if checkInfo.lower() == "yes":
                        break
            if checkInfo.lower() == "yes": #only goes here if checkInfo variable has been set to yes which can only be done by completing username and password
                while True:
                    while True:
                        os.system('clear')
                        buddy_face_standard_smile()
                        print("")
                        print("What would you like to name your Study Buddy?".center(z))
                        studyBuddyName = input("\n")
                        if len(studyBuddyName) < 5 or len(studyBuddyName) > 15:
                            os.system('clear')
                            buddy_face_dead()
                            print("")
                            print(Fore.RED + Style.BRIGHT + "Your Study Buddy's name must be between 5 and 15 digits!".center(z) + Fore.RESET + Style.NORMAL)
                            time.sleep(3)
                        else:
                            break
                    os.system('clear')
                    buddy_face_question()
                    print("")
                    print(f"{studyBuddyName}? Does that sound right?".center(z))
                    checkStudyName = input("\n")
                    if checkStudyName.lower() == "yes":
                        newUser = []
                        add_entry_new_user(newUser,userName,studyBuddyName,password) #now, all needed info has been gathered for a new user so it can be added to our json file
                        write_to_json(newUser[0])
                        break
                    else:
                        pass
        if returnVar == "pass":
            break
        else:
            pass
    if logOrSign.lower() == "log in":
        if userinfo["user"][userNum]['status'] == "new": #After logging in, it checks to see if the user has been marked as new or not, and if they are then they get the help animation, if they have seen the help animation before then they don't have to sit through it again
            help_animation()
        else:
            pass
    else: 
        pass
def home_menu():
    """
    Displays home menu, showing users what their possible commands are if the help animation was not clear enough, application of variable userInput is at the bottom of code
    global userInput (string): input from user dictating which function they will go to next
    Returns userInput
    """
    if screenMode == "dark":
        print(Back.BLACK)
    elif screenMode == "light":
        print(Back.WHITE)
    global userInput
    os.system('clear')
    buddy_face_standard_smile()
    buddy_face_nameplate_attachment()
    print("+---------------------+                +---------------------+".center(z))
    print("|                     |                |                     |".center(z))
    print("|        START        |                |       SETTINGS      |".center(z))
    print("|                     |                |                     |".center(z))
    print("+---------------------+                +---------------------+".center(z))
    print("")
    print("+---------------------+                +---------------------+".center(z))
    print("|                     |                |                     |".center(z))
    print("|        HELP         |                |         QUIT        |".center(z))
    print("|                     |                |                     |".center(z))
    print("+---------------------+                +---------------------+".center(z))
    userInput = input()
def settings():
    """
    Displays setting options, changes variables for the user's preferences and saves them to json file
    screenMode (string): User's preferred screen mode (dark or light)
    subject (string): User's preferred subject (csp, phys, span, or stats)
    fontColor (string): User's preferred font color (default, red, yellow, green, blue, magenta, cyan)
    qAmount (int): User's preferred number of questions (8 to 25)
    progBarSects (int): number of '*' that should be printed for the progress bar, based on number of preferred questions
    gameMode (string): User's preferred game mode (quiz or flashcards)
    userName (string): User's preferred name (5 to 15 characters)
    studyBuddyName (string): User's preferred study buddy name (5 to 15 characters)
    settingInput (string): The setting which the user would like to change
    """
    while True:
        os.system('clear')
        global screenMode
        global subject
        global fontColor
        global qAmount
        global progBarSects
        global gameMode
        global userName
        global studyBuddyName
        global settingInput
        userNameMatch = ""
        if screenMode == "dark":
            print(Back.BLACK)
        elif screenMode == "light":
            print(Back.WHITE)
        os.system('clear')
        buddy_face_standard_smile()
        buddy_face_setting_attachment()
        print("")
        print("Game Settings                Profile".center(z))
        print("")
        print(Style.BRIGHT + "To change a setting, type the name of the setting".center(z) + "Type BACK to return to the start screen:".center(z) + Style.NORMAL)
        settingInput = input()
        os.system('clear')
        if settingInput.lower() == "game settings":
            while True:
                if screenMode == "dark":
                    print(Back.BLACK)
                elif screenMode == "light":
                    print(Back.WHITE)
                os.system('clear')
                buddy_face_standard_smile()
                buddy_face_setting_attachment()
                if gameMode == "quiz": #only shows sample question if user wants to use quiz game mode option
                    settingSentence = [" What is the name of the base computers use to count and read? " , " True or false: the median is more resistant than the mean. " , " How do you find the coefficient of friction using normal and frictional force? "," Qué quiere decir la palabra \"perro\" en inglés? "]
                    print("")
                    print(Style.DIM + "This is an example of what the QUIZ questions will look like".center(z) + Style.NORMAL)
                    print("")
                    if subject.lower() == "csp":
                        if fontColor.lower() == "default":
                            print(Style.DIM + ("-" * len(settingSentence[0])).center(z) + Style.NORMAL)
                            print(settingSentence[0].center(z))
                            print(Style.DIM + ("-" * len(settingSentence[0])).center(z) + Style.NORMAL)
                        elif fontColor.lower() == "red":
                            print(Style.DIM + ("-" * len(settingSentence[0])).center(z) + Style.NORMAL)
                            print(Fore.RED + settingSentence[0].center(z) + Fore.RESET)
                            print(Style.DIM + ("-" * len(settingSentence[0])).center(z) + Style.NORMAL)
                        elif fontColor.lower() == "green":
                            print(Style.DIM + ("-" * len(settingSentence[0])).center(z) + Style.NORMAL)
                            print(Fore.GREEN + settingSentence[0].center(z) + Fore.RESET)
                            print(Style.DIM + ("-" * len(settingSentence[0])).center(z) + Style.NORMAL)
                        elif fontColor.lower() == "yellow":
                            print(Style.DIM + ("-" * len(settingSentence[0])).center(z) + Style.NORMAL)
                            print(Fore.YELLOW + settingSentence[0].center(z) + Fore.RESET)
                            print(Style.DIM + ("-" * len(settingSentence[0])).center(z) + Style.NORMAL)
                        elif fontColor.lower() == "blue":
                            print(Style.DIM + ("-" * len(settingSentence[0])).center(z) + Style.NORMAL)
                            print(Fore.BLUE + settingSentence[0].center(z) + Fore.RESET)
                            print(Style.DIM + ("-" * len(settingSentence[0])).center(z) + Style.NORMAL)
                        elif fontColor.lower() == "magenta":
                            print(Style.DIM + ("-" * len(settingSentence[0])).center(z) + Style.NORMAL)
                            print(Fore.MAGENTA + settingSentence[0].center(z) + Fore.RESET)
                            print(Style.DIM + ("-" * len(settingSentence[0])).center(z) + Style.NORMAL)
                        elif fontColor.lower() == "cyan":
                            print(Style.DIM + ("-" * len(settingSentence[0])).center(z) + Style.NORMAL)
                            print(Fore.CYAN + settingSentence[0].center(z) + Fore.RESET)
                            print(Style.DIM + ("-" * len(settingSentence[0])).center(z) + Style.NORMAL)
                    elif subject.lower() == "stats":
                        if fontColor.lower() == "default":
                            print(Style.DIM + ("-" * len(settingSentence[1])).center(z) + Style.NORMAL)
                            print(settingSentence[1].center(z))
                            print(Style.DIM + ("-" * len(settingSentence[1])).center(z) + Style.NORMAL)
                        elif fontColor.lower() == "red":
                            print(Style.DIM + ("-" * len(settingSentence[1])).center(z) + Style.NORMAL)
                            print(Fore.RED + settingSentence[1].center(z) + Fore.RESET)
                            print(Style.DIM + ("-" * len(settingSentence[1])).center(z) + Style.NORMAL)
                        elif fontColor.lower() == "green":
                            print(Style.DIM + ("-" * len(settingSentence[1])).center(z) + Style.NORMAL)
                            print(Fore.GREEN + settingSentence[1].center(z) + Fore.RESET)
                            print(Style.DIM + ("-" * len(settingSentence[1])).center(z) + Style.NORMAL)
                        elif fontColor.lower() == "yellow":
                            print(Style.DIM + ("-" * len(settingSentence[1])).center(z) + Style.NORMAL)
                            print(Fore.YELLOW + settingSentence[1].center(z) + Fore.RESET)
                            print(Style.DIM + ("-" * len(settingSentence[1])).center(z) + Style.NORMAL)
                        elif fontColor.lower() == "blue":
                            print(Style.DIM + ("-" * len(settingSentence[1])).center(z) + Style.NORMAL)
                            print(Fore.BLUE + settingSentence[1].center(z) + Fore.RESET)
                            print(Style.DIM + ("-" * len(settingSentence[1])).center(z) + Style.NORMAL)
                        elif fontColor.lower() == "magenta":
                            print(Style.DIM + ("-" * len(settingSentence[1])).center(z) + Style.NORMAL)
                            print(Fore.MAGENTA + settingSentence[1].center(z) + Fore.RESET)
                            print(Style.DIM + ("-" * len(settingSentence[1])).center(z) + Style.NORMAL)
                        elif fontColor.lower() == "cyan":
                            print(Style.DIM + ("-" * len(settingSentence[1])).center(z) + Style.NORMAL)
                            print(Fore.CYAN + settingSentence[1].center(z) + Fore.RESET)
                            print(Style.DIM + ("-" * len(settingSentence[1])).center(z) + Style.NORMAL)
                    elif subject.lower() == "phys":
                        if fontColor.lower() == "default":
                            print(Style.DIM + ("-" * len(settingSentence[2])).center(z) + Style.NORMAL)
                            print(settingSentence[2].center(z))
                            print(Style.DIM + ("-" * len(settingSentence[2])).center(z) + Style.NORMAL)
                        elif fontColor.lower() == "red":
                            print(Style.DIM + ("-" * len(settingSentence[2])).center(z) + Style.NORMAL)
                            print(Fore.RED + settingSentence[2].center(z) + Fore.RESET)
                            print(Style.DIM + ("-" * len(settingSentence[2])).center(z) + Style.NORMAL)
                        elif fontColor.lower() == "green":
                            print(Style.DIM + ("-" * len(settingSentence[2])).center(z) + Style.NORMAL)
                            print(Fore.GREEN + settingSentence[2].center(z) + Fore.RESET)
                            print(Style.DIM + ("-" * len(settingSentence[2])).center(z) + Style.NORMAL)
                        elif fontColor.lower() == "yellow":
                            print(Style.DIM + ("-" * len(settingSentence[2])).center(z) + Style.NORMAL)
                            print(Fore.YELLOW + settingSentence[2].center(z) + Fore.RESET)
                            print(Style.DIM + ("-" * len(settingSentence[2])).center(z) + Style.NORMAL)
                        elif fontColor.lower() == "blue":
                            print(Style.DIM + ("-" * len(settingSentence[2])).center(z) + Style.NORMAL)
                            print(Fore.BLUE + settingSentence[2].center(z) + Fore.RESET)
                            print(Style.DIM + ("-" * len(settingSentence[2])).center(z) + Style.NORMAL)
                        elif fontColor.lower() == "magenta":
                            print(Style.DIM + ("-" * len(settingSentence[2])).center(z) + Style.NORMAL)
                            print(Fore.MAGENTA + settingSentence[2].center(z) + Fore.RESET)
                            print(Style.DIM + ("-" * len(settingSentence[2])).center(z) + Style.NORMAL)
                        elif fontColor.lower() == "cyan":
                            print(Style.DIM + ("-" * len(settingSentence[2])).center(z) + Style.NORMAL)
                            print(Fore.CYAN + settingSentence[2].center(z) + Fore.RESET)
                            print(Style.DIM + ("-" * len(settingSentence[2])).center(z) + Style.NORMAL)
                    elif subject.lower() == "span":
                        if fontColor.lower() == "default":
                            print(Style.DIM + ("-" * len(settingSentence[3])).center(z) + Style.NORMAL)
                            print(settingSentence[3].center(z))
                            print(Style.DIM + ("-" * len(settingSentence[3])).center(z) + Style.NORMAL)
                        elif fontColor.lower() == "red":
                            print(Style.DIM + ("-" * len(settingSentence[3])).center(z) + Style.NORMAL)
                            print(Fore.RED + settingSentence[3].center(z) + Fore.RESET)
                            print(Style.DIM + ("-" * len(settingSentence[3])).center(z) + Style.NORMAL)
                        elif fontColor.lower() == "green":
                            print(Style.DIM + ("-" * len(settingSentence[3])).center(z) + Style.NORMAL)
                            print(Fore.GREEN + settingSentence[3].center(z) + Fore.RESET)
                            print(Style.DIM + ("-" * len(settingSentence[3])).center(z) + Style.NORMAL)
                        elif fontColor.lower() == "yellow":
                            print(Style.DIM + ("-" * len(settingSentence[3])).center(z) + Style.NORMAL)
                            print(Fore.YELLOW + settingSentence[3].center(z) + Fore.RESET)
                            print(Style.DIM + ("-" * len(settingSentence[3])).center(z) + Style.NORMAL)
                        elif fontColor.lower() == "blue":
                            print(Style.DIM + ("-" * len(settingSentence[3])).center(z) + Style.NORMAL)
                            print(Fore.BLUE + settingSentence[3].center(z) + Fore.RESET)
                            print(Style.DIM + ("-" * len(settingSentence[3])).center(z) + Style.NORMAL)
                        elif fontColor.lower() == "magenta":
                            print(Style.DIM + ("-" * len(settingSentence[3])).center(z) + Style.NORMAL)
                            print(Fore.MAGENTA + settingSentence[3].center(z) + Fore.RESET)
                            print(Style.DIM + ("-" * len(settingSentence[3])).center(z) + Style.NORMAL)
                        elif fontColor.lower() == "cyan":
                            print(Style.DIM + ("-" * len(settingSentence[3])).center(z) + Style.NORMAL)
                            print(Fore.CYAN + settingSentence[3].center(z) + Fore.RESET)
                            print(Style.DIM + ("-" * len(settingSentence[3])).center(z) + Style.NORMAL)
                    
                else:
                    pass
                if screenMode == "dark":
                    modeName = "Dark"
                elif screenMode == "light":
                    modeName = "Light"
                if subject == "csp":
                    subjectName = "Computer Science"
                elif subject == "stats":
                    subjectName = "Statistics"
                elif subject == "phys":
                    subjectName = "Physics"
                elif subject == "span":
                    subjectName = "Spanish"
                print("")
                print(f"Subject:   {subjectName.capitalize()}".center(z))
                print("")
                print(f"Font color:   {fontColor.capitalize()}".center(z))
                print("")
                print(f"Screen Mode:   {modeName.capitalize()}".center(z))
                print("")
                print(f"Game Mode:   {gameMode.capitalize()}".center(z))
                print("")    
                if gameMode.lower() == "quiz": #only shows number of questions if the user wants to see the quiz game mode
                    print(f"Question Amount:   {qAmount}".center(z))
                    print("")
                elif gameMode.lower() == "flashcards":
                    pass


                
                print(Style.BRIGHT + "To change a setting, type the name of the setting".center(z) + "Type BACK to return to the main setting screen:".center(z) + Style.NORMAL)
                settingInput = input()
                os.system('clear')
                if settingInput.lower() == "subject":
                    buddy_face_standard_smile()
                    buddy_face_setting_attachment()
                    print("")
                    print("Computer Science (CSP) | Statistics (STATS) | Physics (PHYS) | Spanish (SPAN)".center(z))
                    subjectPreference = input()
                    if subjectPreference.lower() == "csp" or subjectPreference.lower() == "phys" or subjectPreference.lower() == "span" or subjectPreference.lower() == "stats" or subjectPreference.lower() == "computer science" or subjectPreference.lower() == "statistics" or subjectPreference.lower() == "physics" or subjectPreference.lower() == "spanish":
                        if subjectPreference.lower() == "computer science":
                            subject = "csp"
                        elif subjectPreference.lower() == "statistics":
                            subject = "stats"
                        elif subjectPreference.lower() == "physics":
                            subject = "phys"
                        elif subjectPreference.lower() == "spanish":
                            subject = "span"
                        else:
                            subject = subjectPreference.lower()
                        userDataDict['subject'] = subject #changes user's preference, will be updated at end of settings()
                    else:
                        pass
                        
                elif settingInput.lower() == "font color":
                    buddy_face_standard_smile()
                    buddy_face_setting_attachment()
                    print("")
                    print(("Default   " + Fore.RED + "Red   " + Fore.YELLOW + "Yellow   " + Fore.GREEN + "Green   " + Fore.BLUE + "Blue   " + Fore.MAGENTA + "Magenta   " + Fore.CYAN + "Cyan").center(z+30))
                    print(Fore.RESET)
                    colorPreference = input()
                    if colorPreference.lower() == "red":
                        fontColor = "red"
                        os.system('clear')
                    elif colorPreference.lower() == "yellow":
                        fontColor = "yellow"
                        os.system('clear')
                    elif colorPreference.lower() == "green":
                        fontColor = "green"
                        os.system('clear')
                    elif colorPreference.lower() == "blue":
                        fontColor = "blue"
                        os.system('clear')
                    elif colorPreference.lower() == "magenta":
                        fontColor = "magenta"
                        os.system('clear')
                    elif colorPreference.lower() == "cyan":
                        fontColor = "cyan"
                        os.system('clear')
                    elif colorPreference.lower() == "default":
                        fontColor = "default"
                        os.system('clear')
                    userDataDict['fontColor'] = fontColor #changes user's preference, will be updated at end of settings()
                elif settingInput.lower() == "screen mode":
                    if screenMode == "dark":
                        screenMode = "light"
                    elif screenMode == "light":
                        screenMode = "dark"
                    userDataDict['screenMode'] = screenMode #changes user's preference, will be updated at end of settings()
                elif settingInput.lower() == "question amount":
                    buddy_face_standard_smile()
                    buddy_face_setting_attachment()
                    print("")
                    print("How many questions would you like to have? (Note: You may choose a number from 8 to 25)".center(z))
                    qInput = input("\n\n\n")
                    if qInput.isdigit():
                        if int(qInput) <= 25 and int(qInput) >= 8:
                            qAmount = int(qInput)
                            progBarSects = int((z-17)/qAmount) - 1
                        else:
                            print(Fore.RED + Style.BRIGHT + "You can only have 8 to 25 questions!".center(z) + Fore.RESET + Style.NORMAL)
                            time.sleep(2)
                    else: 
                        pass
                    userDataDict['qamount'] = qAmount #changes user's preference, will be updated at end of settings()
                elif settingInput.lower() == "game mode":
                    if gameMode == "quiz":
                        gameMode = "flashcards"
                    elif gameMode == "flashcards":
                        gameMode = "quiz"
                    userDataDict['gameMode'] = gameMode #changes user's preference, will be updated at end of settings()
                elif settingInput.lower() == "quit":
                    quit_animation()
                elif settingInput.lower() == "back":
                    break
                write_to_json_updated_settings() #user's preferences are updated in json file
        elif settingInput.lower() == "profile":
            while True:
                os.system('clear')
                newPlayer = "false"
                if userinfo["user"][userNum]['total'] == 0: #sets user's average score to 0 instead of using the formula below because if they are new, their total will = 0 and you cannot divide by 0, even with 0 on top of the fraction, also sets variable so code knows they are new and will print a cool little message for them
                    avrgQuizScore = 0
                    newPlayer = "true"
                else:
                    avrgQuizScore = userinfo["user"][userNum]["correct"]/userinfo["user"][userNum]['total'] #if they are not new, then their average score will be calculated
                    avrgQuizScore *= 1000
                    avrgQuizScore = int(avrgQuizScore)
                    avrgQuizScore /= 10
                buddy_face_standard_smile()
                buddy_face_setting_attachment()
                if newPlayer == "true": #cool little message if they are new to help them know what to do to add to their stats page
                    print("")
                    print(Fore.GREEN + Style.BRIGHT + "NEW USER!!! Hop into a quiz to stack up your stats!".center(z) + Fore.RESET + Style.NORMAL)
                print("")
                print(f"Username:   {userName}".center(z))
                print("")
                print(f"Study Buddy Name:   {studyBuddyName}".center(z))
                print("")
                print(f"Correct Questions Answered:   {userinfo["user"][userNum]["correct"]}".center(z))
                print("")
                print(f"Average Quiz Score:   {avrgQuizScore}%".center(z))
                print("")
                print(Style.BRIGHT + "To change a setting, type the name of the setting".center(z) + "Type BACK to return to the main setting screen:".center(z) + Style.NORMAL)
                settingInput = input()
                os.system('clear')
                if settingInput.lower() == "username": #requires password to change
                    buddy_face_standard_smile()
                    buddy_face_setting_attachment()
                    print("")
                    print(Fore.RED + Style.BRIGHT + "Enter your password to change your username".center(z) + Fore.RESET + Style.NORMAL)
                    passwordCheck = input()
                    if passwordCheck == password:
                        while True:
                            while True:
                                os.system('clear')
                                buddy_face_standard_smile()
                                buddy_face_setting_attachment()
                                print("")
                                print("New username:".center(z))
                                newUserName = input()
                                for user in range(len(userAtUser)):
                                    if newUserName == userinfo["user"][user]["name"]: #checks to see if a username is already taken, if it is then local variable userNameMatch is not set to p to let the code know later that the username is taken
                                        if newUserName == userinfo["user"][userNum]["name"]:
                                            pass
                                        else:
                                            userNameMatch = "fail"
                                    else:
                                        pass
                                if len(userName) < 5 or len(userName) > 15:
                                    os.system('clear')
                                    buddy_face_talkOption1()
                                    print("")
                                    print(Fore.RED + Style.BRIGHT + "Username must be between 5 and 15 digits!".center(z) + Fore.RESET + Style.NORMAL)
                                    time.sleep(3)
                                elif userNameMatch == "fail":
                                    os.system('clear')
                                    buddy_face_talkOption3()
                                    print("")
                                    print(Fore.RED + Style.BRIGHT + "That username is already taken!".center(z) + Fore.RESET + Style.NORMAL)
                                    userNameMatch = ""
                                    time.sleep(3)
                                else:
                                    break
                            while True:
                                os.system('clear')
                                buddy_face_standard_smile()
                                buddy_face_setting_attachment()
                                print("")
                                print(f"Is {newUserName} correct?")
                                checkNewUserName = input()
                                if checkNewUserName.lower() == "yes":
                                    userName = newUserName
                                    userDataDict['name'] = newUserName #changes user's preference, will be updated at end of settings()
                                    break
                                elif checkNewUserName.lower() == "no":
                                    break
                                else:
                                    pass
                            if checkNewUserName.lower() == "yes":
                                break
                            else:
                                pass
                elif settingInput.lower() == "study buddy name": #requires password to change
                    buddy_face_standard_smile()
                    buddy_face_setting_attachment()
                    print("")
                    print(Fore.RED + Style.BRIGHT + "Enter your password to change your Study Buddy Name".center(z) + Fore.RESET + Style.NORMAL)
                    passwordCheck = input()
                    if passwordCheck == password:
                        while True:
                            while True:
                                os.system('clear')
                                buddy_face_standard_smile()
                                buddy_face_setting_attachment()
                                print("")
                                print("New Study Buddy Name:".center(z))
                                newStudyBuddyName = input()
                                if len(newStudyBuddyName) < 5 or len(newStudyBuddyName) > 15:
                                    os.system('clear')
                                    buddy_face_dead()
                                    print("")
                                    print(Fore.RED + Style.BRIGHT + "Your Study Buddy's name must be between 5 and 15 digits!".center(z) + Fore.RESET + Style.NORMAL)
                                    time.sleep(3)
                                else:
                                    break
                            while True:
                                os.system('clear')
                                buddy_face_standard_smile()
                                buddy_face_setting_attachment()
                                print("")
                                print(f"Is {newStudyBuddyName} good?".center(z))
                                checkNewStudyBuddyName = input()
                                if checkNewStudyBuddyName.lower() == "yes":
                                    studyBuddyName = newStudyBuddyName
                                    userDataDict['studybuddyname'] = newStudyBuddyName #changes user's preference, will be updated at end of settings()
                                    break
                                elif checkNewStudyBuddyName.lower() == "no":
                                    break
                                else:
                                    pass
                            if checkNewStudyBuddyName.lower() == "yes":
                                break
                            else:
                                pass
                elif settingInput.lower() == "quit":
                    quit_animation()
                elif settingInput.lower() == "back":
                    break
                else:
                    pass
                write_to_json_updated_settings() #changes user's preference in json file
        elif settingInput.lower() == "back":
            break
def quit_animation():
    """
    Animation that can be called to at almost any point, little easter egg if you quit then the study buddy acts like it is dying
    """
    os.system('clear')
    buddy_face_question()
    print("")
    print("Wait, you are shutting me off?".center(z))
    time.sleep(3)
    os.system('clear')
    buddy_face_unamused()
    print("")
    print("Wow, and I really thought we were becoming friends".center(z))
    time.sleep(3)
    os.system('clear')
    buddy_face_talkOption3()
    print("")
    print(f"Wait, {userName}, I feel weird".center(z))
    time.sleep(3)
    os.system('clear')
    buddy_face_talkOption3()
    print("")
    print(f"Please, please don't do thi-".center(z))
    time.sleep(2)
    os.system('clear')
    buddy_face_dead()
    sys.exit() #forcefully shuts down the run
def study_buddy(subject):
    """
    This function displays the questions and checks the answers to a given subject, determined in settings or defaulted to csp
    subject (string): Tells code what subject to display from
    returns user's quiz score if gameMode == "quiz"
    """
    global checkCounter
    global userDataDict
    if gameMode == "quiz":
        checkCounter = 0
        randomQChoice = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
        usedQList = []
        for lcv in range(qAmount): #creates a random list of the amount of questions that the user wants for their quiz in order to randomize the order of the questions for every time the quiz is taken
            ele = random.choice(randomQChoice)
            usedQList.append(ele)
            randomQChoice.remove(ele)
        os.system('clear')
        for ques in range(qAmount):
            if ques == 0: #checks to see if the question number is 0 because otherwise the formula used below would cause an error because it cannot divide by zero
                percentRight = 0.0
            else:
                percentRight = checkCounter/ques * 1000 #shows a live count of their percentage of correct answers, rounding at the first decimal place
                percentRight = int(percentRight)
                percentRight /= 10
            buddy_face_standard_smile()
            buddy_face_nameplate_attachment()
            print("+" + ("-" * (progBarSects + 1) * qAmount) + "+")
            print("|" + Fore.BLUE + Style.BRIGHT + ((("#" * progBarSects) + "|") * ques) + ((" " * (progBarSects + 1)) * (qAmount-ques)) + Style.NORMAL + Fore.RESET + "|   " + Style.BRIGHT + f"{checkCounter}/{ques}   {percentRight}%" + Style.NORMAL)
            print("+" + ("-" * (progBarSects + 1) * qAmount) + "+")
            print("\n")
            if fontColor.lower() == "default":
                print(questions[subject][usedQList[ques]]['question'])
            elif fontColor.lower() == "red":
                print(Fore.RED + questions[subject][usedQList[ques]]['question'] + Fore.RESET)
            elif fontColor.lower() == "yellow":
                print(Fore.YELLOW + questions[subject][usedQList[ques]]['question'] + Fore.RESET)
            elif fontColor.lower() == "green":
                print(Fore.GREEN + questions[subject][usedQList[ques]]['question'] + Fore.RESET)
            elif fontColor.lower() == "blue":
                print(Fore.BLUE + questions[subject][usedQList[ques]]['question'] + Fore.RESET)
            elif fontColor.lower() == "magenta":
                print(Fore.MAGENTA + questions[subject][usedQList[ques]]['question'] + Fore.RESET)
            elif fontColor.lower() == "cyan":
                print(Fore.CYAN + questions[subject][usedQList[ques]]['question'] + Fore.RESET)
            if questions[subject][usedQList[ques]]['qtype'] == "mcq":
                correctAnswer = questions[subject][usedQList[ques]]['answer']
                print(Style.BRIGHT + questions[subject][usedQList[ques]]["optionA"])
                print(questions[subject][usedQList[ques]]['optionB'])
                print(questions[subject][usedQList[ques]]['optionC'])
                print(questions[subject][usedQList[ques]]['optionD'] + Style.NORMAL)
                userAnswer = input()
                if userAnswer.lower() == "quit":
                    quit_animation()
                elif userAnswer.lower() == "help":
                    mcqList = ["a","b","c","d"]
                    mcqList.remove(correctAnswer) #removes the correct answer from the list of mcq options
                    mcqList.remove(random.choice(mcqList)) #removes another random option that is incorrect, the other two will be grayed out 
                    os.system('clear')
                    buddy_face_standard_smile()
                    buddy_face_nameplate_attachment()
                    print("+" + ("-" * (progBarSects + 1) * qAmount) + "+")
                    print("|" + Fore.BLUE + Style.BRIGHT + ((("#" * progBarSects) + "|") * ques) + ((" " * (progBarSects + 1)) * (qAmount-ques)) + Style.NORMAL + Fore.RESET + "|   " + Style.BRIGHT + f"{checkCounter}/{ques}   {percentRight}%" + Style.NORMAL)
                    print("+" + ("-" * (progBarSects + 1) * qAmount) + "+")
                    print("\n")
                    if fontColor.lower() == "default":
                        print(questions[subject][usedQList[ques]]['question'])
                    elif fontColor.lower() == "red":
                        print(Fore.RED + questions[subject][usedQList[ques]]['question'] + Fore.RESET)
                    elif fontColor.lower() == "yellow":
                        print(Fore.YELLOW + questions[subject][usedQList[ques]]['question'] + Fore.RESET)
                    elif fontColor.lower() == "green":
                        print(Fore.GREEN + questions[subject][usedQList[ques]]['question'] + Fore.RESET)
                    elif fontColor.lower() == "blue":
                        print(Fore.BLUE + questions[subject][usedQList[ques]]['question'] + Fore.RESET)
                    elif fontColor.lower() == "magenta":
                        print(Fore.MAGENTA + questions[subject][usedQList[ques]]['question'] + Fore.RESET)
                    elif fontColor.lower() == "cyan":
                        print(Fore.CYAN + questions[subject][usedQList[ques]]['question'] + Fore.RESET)

                    if mcqList[0] == "a":  #grays out mcq options according to the list made previously
                        print(Style.DIM + questions[subject][usedQList[ques]]['optionA'] + Style.NORMAL)
                    else:
                        print(Style.BRIGHT + questions[subject][usedQList[ques]]['optionA'] + Style.NORMAL)
                    if mcqList[0] == "b" or mcqList[1] == "b":
                        print(Style.DIM + questions[subject][usedQList[ques]]['optionB' ] + Style.NORMAL)
                    else:
                        print(Style.BRIGHT + questions[subject][usedQList[ques]]['optionB'] + Style.NORMAL)
                    if mcqList[0] == "c" or mcqList[1] == "c":
                        print(Style.DIM + questions[subject][usedQList[ques]]['optionC'] + Style.NORMAL)
                    else:
                        print(Style.BRIGHT + questions[subject][usedQList[ques]]['optionC'] + Style.NORMAL)
                    if mcqList[1] == "d":
                        print(Style.DIM + questions[subject][usedQList[ques]]['optionD'] + Style.NORMAL)
                    else:
                        print(Style.BRIGHT + questions[subject][usedQList[ques]]['optionD'] + Style.NORMAL)
                    userAnswer = input()
                    if userAnswer.lower() == "quit":
                        quit_animation()
                    else:
                        userAnswer = str(userAnswer)
                        if userAnswer.lower() == questions[subject][usedQList[ques]]['answer'] or userAnswer.lower() == questions[subject][usedQList[ques]]['altanswer']: #checks the answer, comparing to questions.json
                            os.system('clear')
                            buddy_face_standard_smile()
                            buddy_face_nameplate_attachment()
                            print("+" + ("-" * (progBarSects + 1) * qAmount) + "+")
                            print("|" + Fore.BLUE + Style.BRIGHT + ((("#" * progBarSects) + "|") * ques) + ((" " * (progBarSects + 1)) * (qAmount-ques)) + Style.NORMAL + Fore.RESET + "|   " + Style.BRIGHT + f"{checkCounter}/{ques}   {percentRight}%" + Style.NORMAL)
                            print("+" + ("-" * (progBarSects + 1) * qAmount) + "+")
                            print("\n")
                            if fontColor.lower() == "default":
                                print(questions[subject][usedQList[ques]]['question'])
                            elif fontColor.lower() == "red":
                                print(Fore.RED + questions[subject][usedQList[ques]]['question'] + Fore.RESET)
                            elif fontColor.lower() == "yellow":
                                print(Fore.YELLOW + questions[subject][usedQList[ques]]['question'] + Fore.RESET)
                            elif fontColor.lower() == "green":
                                print(Fore.GREEN + questions[subject][usedQList[ques]]['question'] + Fore.RESET)
                            elif fontColor.lower() == "blue":
                                print(Fore.BLUE + questions[subject][usedQList[ques]]['question'] + Fore.RESET)
                            elif fontColor.lower() == "magenta":
                                print(Fore.MAGENTA + questions[subject][usedQList[ques]]['question'] + Fore.RESET)
                            elif fontColor.lower() == "cyan":
                                print(Fore.CYAN + questions[subject][usedQList[ques]]['question'] + Fore.RESET)
                            if correctAnswer == "a":
                                print(Style.BRIGHT + Fore.GREEN + questions[subject][usedQList[ques]]["optionA"] + Fore.RESET + Style.NORMAL)
                                print(Style.DIM + questions[subject][usedQList[ques]]['optionB'])
                                print(questions[subject][usedQList[ques]]['optionC'])
                                print(questions[subject][usedQList[ques]]['optionD'] + Style.NORMAL)
                            elif correctAnswer == "b":
                                print(Style.DIM + questions[subject][usedQList[ques]]["optionA"] + Style.NORMAL)
                                print(Style.BRIGHT + Fore.GREEN + questions[subject][usedQList[ques]]['optionB'] + Fore.RESET + Style.NORMAL)
                                print(Style.DIM + questions[subject][usedQList[ques]]['optionC'])
                                print(questions[subject][usedQList[ques]]['optionD'] + Style.NORMAL)
                            elif correctAnswer == "c":
                                print(Style.DIM + questions[subject][usedQList[ques]]["optionA"])
                                print(questions[subject][usedQList[ques]]['optionB'] + Style.NORMAL)
                                print(Style.BRIGHT + Fore.GREEN + questions[subject][usedQList[ques]]['optionC'] + Fore.RESET + Style.NORMAL)
                                print(Style.DIM + questions[subject][usedQList[ques]]['optionD'] + Style.NORMAL)
                            elif correctAnswer == "d":
                                print(Style.DIM + questions[subject][usedQList[ques]]["optionA"])
                                print(questions[subject][usedQList[ques]]['optionB'])
                                print(questions[subject][usedQList[ques]]['optionC'] + Style.NORMAL)
                                print(Style.BRIGHT + Fore.GREEN + questions[subject][usedQList[ques]]['optionD'] + Fore.RESET + Style.NORMAL)                       
                            checkCounter += 1
                            print("\n" + Fore.GREEN + Style.BRIGHT + "CORRECT" + Fore.RESET + Style.NORMAL + "\n")
                            print("Press ENTER to continue")
                            input()
                        else:
                            os.system('clear')
                            buddy_face_standard_smile()
                            buddy_face_nameplate_attachment()
                            print("+" + ("-" * (progBarSects + 1) * qAmount) + "+")
                            print("|" + Fore.BLUE + Style.BRIGHT + ((("#" * progBarSects) + "|") * ques) + ((" " * (progBarSects + 1)) * (qAmount-ques)) + Style.NORMAL + Fore.RESET + "|   " + Style.BRIGHT + f"{checkCounter}/{ques}   {percentRight}%" + Style.NORMAL)
                            print("+" + ("-" * (progBarSects + 1) * qAmount) + "+")
                            print("\n")
                            if fontColor.lower() == "default":
                                print(questions[subject][usedQList[ques]]['question'])
                            elif fontColor.lower() == "red":
                                print(Fore.RED + questions[subject][usedQList[ques]]['question'] + Fore.RESET)
                            elif fontColor.lower() == "yellow":
                                print(Fore.YELLOW + questions[subject][usedQList[ques]]['question'] + Fore.RESET)
                            elif fontColor.lower() == "green":
                                print(Fore.GREEN + questions[subject][usedQList[ques]]['question'] + Fore.RESET)
                            elif fontColor.lower() == "blue":
                                print(Fore.BLUE + questions[subject][usedQList[ques]]['question'] + Fore.RESET)
                            elif fontColor.lower() == "magenta":
                                print(Fore.MAGENTA + questions[subject][usedQList[ques]]['question'] + Fore.RESET)
                            elif fontColor.lower() == "cyan":
                                print(Fore.CYAN + questions[subject][usedQList[ques]]['question'] + Fore.RESET)
                            if correctAnswer == "a":
                                print(Style.BRIGHT + Fore.GREEN + questions[subject][usedQList[ques]]["optionA"] + Style.NORMAL)
                                print(Style.DIM + Fore.RED + questions[subject][usedQList[ques]]['optionB'])
                                print(questions[subject][usedQList[ques]]['optionC'])
                                print(questions[subject][usedQList[ques]]['optionD'] + Style.NORMAL + Fore.RESET)
                            elif correctAnswer == "b":
                                print(Style.DIM + Fore.RED + questions[subject][usedQList[ques]]["optionA"] + Style.NORMAL)
                                print(Style.BRIGHT + Fore.GREEN + questions[subject][usedQList[ques]]['optionB'] + Style.NORMAL)
                                print(Style.DIM + Fore.RED + questions[subject][usedQList[ques]]['optionC'])
                                print(questions[subject][usedQList[ques]]['optionD'] + Style.NORMAL + Fore.RESET)
                            elif correctAnswer == "c":
                                print(Style.DIM + Fore.RED + questions[subject][usedQList[ques]]["optionA"])
                                print(questions[subject][usedQList[ques]]['optionB'] + Style.NORMAL)
                                print(Style.BRIGHT + Fore.GREEN + questions[subject][usedQList[ques]]['optionC'] + Style.NORMAL)
                                print(Style.DIM + Fore.RED + questions[subject][usedQList[ques]]['optionD'] + Style.NORMAL + Fore.RESET)
                            elif correctAnswer == "d":
                                print(Style.DIM + Fore.RED + questions[subject][usedQList[ques]]["optionA"])
                                print(questions[subject][usedQList[ques]]['optionB'])
                                print(questions[subject][usedQList[ques]]['optionC'] + Style.NORMAL)
                                print(Style.BRIGHT + Fore.GREEN + questions[subject][usedQList[ques]]['optionD'] + Fore.RESET + Style.NORMAL)                       
                            print("\n" + Fore.RED + Style.BRIGHT + "INCORRECT" + Fore.RESET + Style.NORMAL + "\n")
                            print("Press ENTER to continue")
                            input()
                            pass
                        os.system('clear')
                else:
                    userAnswer = str(userAnswer)
                    if userAnswer.lower() == questions[subject][usedQList[ques]]['answer'] or userAnswer.lower() == questions[subject][usedQList[ques]]['altanswer']:
                        os.system('clear')
                        buddy_face_standard_smile()
                        buddy_face_nameplate_attachment()
                        print("+" + ("-" * (progBarSects + 1) * qAmount) + "+")
                        print("|" + Fore.BLUE + Style.BRIGHT + ((("#" * progBarSects) + "|") * ques) + ((" " * (progBarSects + 1)) * (qAmount-ques)) + Style.NORMAL + Fore.RESET + "|   " + Style.BRIGHT + f"{checkCounter}/{ques}   {percentRight}%" + Style.NORMAL)
                        print("+" + ("-" * (progBarSects + 1) * qAmount) + "+")
                        print("\n")
                        if fontColor.lower() == "default":
                            print(questions[subject][usedQList[ques]]['question'])
                        elif fontColor.lower() == "red":
                            print(Fore.RED + questions[subject][usedQList[ques]]['question'] + Fore.RESET)
                        elif fontColor.lower() == "yellow":
                            print(Fore.YELLOW + questions[subject][usedQList[ques]]['question'] + Fore.RESET)
                        elif fontColor.lower() == "green":
                            print(Fore.GREEN + questions[subject][usedQList[ques]]['question'] + Fore.RESET)
                        elif fontColor.lower() == "blue":
                            print(Fore.BLUE + questions[subject][usedQList[ques]]['question'] + Fore.RESET)
                        elif fontColor.lower() == "magenta":
                            print(Fore.MAGENTA + questions[subject][usedQList[ques]]['question'] + Fore.RESET)
                        elif fontColor.lower() == "cyan":
                            print(Fore.CYAN + questions[subject][usedQList[ques]]['question'] + Fore.RESET)
                        if correctAnswer == "a":
                            print(Style.BRIGHT + Fore.GREEN + questions[subject][usedQList[ques]]["optionA"] + Fore.RESET + Style.NORMAL)
                            print(Style.DIM + questions[subject][usedQList[ques]]['optionB'])
                            print(questions[subject][usedQList[ques]]['optionC'])
                            print(questions[subject][usedQList[ques]]['optionD'] + Style.NORMAL)
                        elif correctAnswer == "b":
                            print(Style.DIM + questions[subject][usedQList[ques]]["optionA"] + Style.NORMAL)
                            print(Style.BRIGHT + Fore.GREEN + questions[subject][usedQList[ques]]['optionB'] + Fore.RESET + Style.NORMAL)
                            print(Style.DIM + questions[subject][usedQList[ques]]['optionC'])
                            print(questions[subject][usedQList[ques]]['optionD'] + Style.NORMAL)
                        elif correctAnswer == "c":
                            print(Style.DIM + questions[subject][usedQList[ques]]["optionA"])
                            print(questions[subject][usedQList[ques]]['optionB'] + Style.NORMAL)
                            print(Style.BRIGHT + Fore.GREEN + questions[subject][usedQList[ques]]['optionC'] + Fore.RESET + Style.NORMAL)
                            print(Style.DIM + questions[subject][usedQList[ques]]['optionD'] + Style.NORMAL)
                        elif correctAnswer == "d":
                            print(Style.DIM + questions[subject][usedQList[ques]]["optionA"])
                            print(questions[subject][usedQList[ques]]['optionB'])
                            print(questions[subject][usedQList[ques]]['optionC'] + Style.NORMAL)
                            print(Style.BRIGHT + Fore.GREEN + questions[subject][usedQList[ques]]['optionD'] + Fore.RESET + Style.NORMAL)                
                        checkCounter += 1
                        print("\n" + Fore.GREEN + Style.BRIGHT + "CORRECT" + Fore.RESET + Style.NORMAL + "\n")
                        print("Press ENTER to continue")
                        input()
                    else:
                        os.system('clear')
                        buddy_face_standard_smile()
                        buddy_face_nameplate_attachment()
                        print("+" + ("-" * (progBarSects + 1) * qAmount) + "+")
                        print("|" + Fore.BLUE + Style.BRIGHT + ((("#" * progBarSects) + "|") * ques) + ((" " * (progBarSects + 1)) * (qAmount-ques)) + Style.NORMAL + Fore.RESET + "|   " + Style.BRIGHT + f"{checkCounter}/{ques}   {percentRight}%" + Style.NORMAL)
                        print("+" + ("-" * (progBarSects + 1) * qAmount) + "+")
                        print("\n")
                        if fontColor.lower() == "default":
                            print(questions[subject][usedQList[ques]]['question'])
                        elif fontColor.lower() == "red":
                            print(Fore.RED + questions[subject][usedQList[ques]]['question'] + Fore.RESET)
                        elif fontColor.lower() == "yellow":
                            print(Fore.YELLOW + questions[subject][usedQList[ques]]['question'] + Fore.RESET)
                        elif fontColor.lower() == "green":
                            print(Fore.GREEN + questions[subject][usedQList[ques]]['question'] + Fore.RESET)
                        elif fontColor.lower() == "blue":
                            print(Fore.BLUE + questions[subject][usedQList[ques]]['question'] + Fore.RESET)
                        elif fontColor.lower() == "magenta":
                            print(Fore.MAGENTA + questions[subject][usedQList[ques]]['question'] + Fore.RESET)
                        elif fontColor.lower() == "cyan":
                            print(Fore.CYAN + questions[subject][usedQList[ques]]['question'] + Fore.RESET)
                        if correctAnswer == "a":
                            print(Style.BRIGHT + Fore.GREEN + questions[subject][usedQList[ques]]["optionA"] + Style.NORMAL)
                            print(Style.DIM + Fore.RED + questions[subject][usedQList[ques]]['optionB'])
                            print(questions[subject][usedQList[ques]]['optionC'])
                            print(questions[subject][usedQList[ques]]['optionD'] + Style.NORMAL + Fore.RESET)
                        elif correctAnswer == "b":
                            print(Style.DIM + Fore.RED + questions[subject][usedQList[ques]]["optionA"] + Style.NORMAL)
                            print(Style.BRIGHT + Fore.GREEN + questions[subject][usedQList[ques]]['optionB'] + Style.NORMAL)
                            print(Style.DIM + Fore.RED + questions[subject][usedQList[ques]]['optionC'])
                            print(questions[subject][usedQList[ques]]['optionD'] + Style.NORMAL + Fore.RESET)
                        elif correctAnswer == "c":
                            print(Style.DIM + Fore.RED + questions[subject][usedQList[ques]]["optionA"])
                            print(questions[subject][usedQList[ques]]['optionB'] + Style.NORMAL)
                            print(Style.BRIGHT + Fore.GREEN + questions[subject][usedQList[ques]]['optionC'] + Style.NORMAL)
                            print(Style.DIM + Fore.RED + questions[subject][usedQList[ques]]['optionD'] + Style.NORMAL + Fore.RESET)
                        elif correctAnswer == "d":
                            print(Style.DIM + Fore.RED + questions[subject][usedQList[ques]]["optionA"])
                            print(questions[subject][usedQList[ques]]['optionB'])
                            print(questions[subject][usedQList[ques]]['optionC'] + Style.NORMAL)
                            print(Style.BRIGHT + Fore.GREEN + questions[subject][usedQList[ques]]['optionD'] + Fore.RESET + Style.NORMAL)                    
                        print("\n" + Fore.RED + Style.BRIGHT + "INCORRECT" + Fore.RESET + Style.NORMAL + "\n")
                        print("Press ENTER to continue")
                        input()
                        pass
                    os.system('clear')
            elif questions[subject][usedQList[ques]]['qtype'] == "tfq":
                print("\n\n\n")
                userAnswer = input()
                if userAnswer.lower() == "quit":
                    quit_animation()
                elif userAnswer.lower() == "help":
                    os.system('clear')
                    buddy_face_standard_smile()
                    buddy_face_nameplate_attachment()
                    print("+" + ("-" * (progBarSects + 1) * qAmount) + "+")
                    print("|" + Fore.BLUE + Style.BRIGHT + ((("#" * progBarSects) + "|") * ques) + ((" " * (progBarSects + 1)) * (qAmount-ques)) + Style.NORMAL + Fore.RESET + "|   " + Style.BRIGHT + f"{checkCounter}/{ques}   {percentRight}%" + Style.NORMAL)
                    print("+" + ("-" * (progBarSects + 1) * qAmount) + "+")
                    print("\n")
                    if fontColor.lower() == "default":
                        print(questions[subject][usedQList[ques]]['question'])
                    elif fontColor.lower() == "red":
                        print(Fore.RED + questions[subject][usedQList[ques]]['question'] + Fore.RESET)
                    elif fontColor.lower() == "yellow":
                        print(Fore.YELLOW + questions[subject][usedQList[ques]]['question'] + Fore.RESET)
                    elif fontColor.lower() == "green":
                        print(Fore.GREEN + questions[subject][usedQList[ques]]['question'] + Fore.RESET)
                    elif fontColor.lower() == "blue":
                        print(Fore.BLUE + questions[subject][usedQList[ques]]['question'] + Fore.RESET)
                    elif fontColor.lower() == "magenta":
                        print(Fore.MAGENTA + questions[subject][usedQList[ques]]['question'] + Fore.RESET)
                    elif fontColor.lower() == "cyan":
                        print(Fore.CYAN + questions[subject][usedQList[ques]]['question'] + Fore.RESET)
                    
                    print("")
                    print(Style.BRIGHT + questions[subject][usedQList[ques]]['hint'] + Style.NORMAL)
                    print("\n")
                    userAnswer = input()
                    if userAnswer.lower() == "quit":
                        quit_animation()
                    else:
                        userAnswer = str(userAnswer)
                        if userAnswer.lower() == questions[subject][usedQList[ques]]['answer'] or userAnswer.lower() == questions[subject][usedQList[ques]]['altanswer']:
                            checkCounter += 1
                            print("")
                            print(Style.BRIGHT + Fore.GREEN + "CORRECT" + Fore.RESET + Style.NORMAL)
                            print("\nPress ENTER to continue")
                            input()
                        else:
                            print("")
                            print(Style.BRIGHT + Fore.RED + "INCORRECT" + Fore.RESET + Style.NORMAL)
                            print("\nPress ENTER to continue")
                            input()
                        os.system('clear')
                else:
                    userAnswer = str(userAnswer)
                    if userAnswer.lower() == questions[subject][usedQList[ques]]['answer'] or userAnswer.lower() == questions[subject][usedQList[ques]]['altanswer']:
                        checkCounter += 1
                        print("")
                        print(Style.BRIGHT + Fore.GREEN + "CORRECT" + Fore.RESET + Style.NORMAL)
                        print("\nPress ENTER to continue")
                        input()
                    else:
                        print("")
                        print(Style.BRIGHT + Fore.RED + "INCORRECT" + Fore.RESET + Style.NORMAL)
                        print("\nPress ENTER to continue")
                        input()
                        pass
                    os.system('clear')
            elif questions[subject][usedQList[ques]]['qtype'] == "frq":
                print(questions[subject][usedQList[ques]]['optionA'])
                print("")
                userAnswer = input()
                if userAnswer.lower() == "quit":
                    quit_animation()
                elif userAnswer.lower() == "help":
                    os.system('clear')
                    buddy_face_standard_smile()
                    buddy_face_nameplate_attachment()
                    print("+" + ("-" * (progBarSects + 1) * qAmount) + "+")
                    print("|" + Fore.BLUE + Style.BRIGHT + ((("#" * progBarSects) + "|") * ques) + ((" " * (progBarSects + 1)) * (qAmount-ques)) + Style.NORMAL + Fore.RESET + "|   " + Style.BRIGHT + f"{checkCounter}/{ques}   {percentRight}%" + Style.NORMAL)
                    print("+" + ("-" * (progBarSects + 1) * qAmount) + "+")
                    print("\n")
                    if fontColor.lower() == "default":
                        print(questions[subject][usedQList[ques]]['question'])
                    elif fontColor.lower() == "red":
                        print(Fore.RED + questions[subject][usedQList[ques]]['question'] + Fore.RESET)
                    elif fontColor.lower() == "yellow":
                        print(Fore.YELLOW + questions[subject][usedQList[ques]]['question'] + Fore.RESET)
                    elif fontColor.lower() == "green":
                        print(Fore.GREEN + questions[subject][usedQList[ques]]['question'] + Fore.RESET)
                    elif fontColor.lower() == "blue":
                        print(Fore.BLUE + questions[subject][usedQList[ques]]['question'] + Fore.RESET)
                    elif fontColor.lower() == "magenta":
                        print(Fore.MAGENTA + questions[subject][usedQList[ques]]['question'] + Fore.RESET)
                    elif fontColor.lower() == "cyan":
                        print(Fore.CYAN + questions[subject][usedQList[ques]]['question'] + Fore.RESET)
                    
                    print(questions[subject][usedQList[ques]]['hint'])
                    print("")
                    userAnswer = input()
                    if userAnswer.lower() == "quit":
                        quit_animation()
                    else:
                        if userAnswer.isdigit():
                            print("")
                            print(Style.BRIGHT + Fore.RED + "INCORRECT" + Fore.RESET + Style.NORMAL)
                            print("")
                            print("Correct answer: " + Fore.GREEN + Style.BRIGHT + questions[subject][usedQList[ques]]['answer'] + Fore.RESET + Style.NORMAL)
                            print("\nPress ENTER to continue")
                            input()
                            pass
                        else:
                            if userAnswer.lower() == questions[subject][usedQList[ques]]['answer']:
                                checkCounter += 1
                                print("")
                                print(Style.BRIGHT + Fore.GREEN + "CORRECT" + Fore.RESET + Style.NORMAL)
                                print("\nPress ENTER to continue")
                                input()
                            else:
                                print("")
                                print(Style.BRIGHT + Fore.RED + "INCORRECT" + Fore.RESET + Style.NORMAL)
                                print("")
                                print("Correct answer: " + Fore.GREEN + Style.BRIGHT + questions[subject][usedQList[ques]]['answer'] + Fore.RESET + Style.NORMAL)
                                print("\nPress ENTER to continue")
                                input()
                                pass
                        os.system('clear')
                else:
                    userAnswer = str(userAnswer)
                    if userAnswer.lower() == questions[subject][usedQList[ques]]['answer']:
                        checkCounter += 1
                        print("")
                        print(Style.BRIGHT + Fore.GREEN + "CORRECT" + Fore.RESET + Style.NORMAL)
                        print("\nPress ENTER to continue")
                        input()
                    else:
                        print("")
                        print(Style.BRIGHT + Fore.RED + "INCORRECT" + Fore.RESET + Style.NORMAL)
                        print("")
                        print("Correct answer: " + Fore.GREEN + Style.BRIGHT + questions[subject][usedQList[ques]]['answer'] + Fore.RESET + Style.NORMAL)
                        print("\nPress ENTER to continue")
                        input()
                        pass
                    os.system('clear')

        finalScore = int((checkCounter/qAmount) * 1000)
        finalScore /= 10 #finds final percentage score
        userDataDict['correct'] = (userinfo["user"][userNum]['correct'] + checkCounter) #adds number of correct to user's profile, for the profile page
        userDataDict['total'] = (userinfo["user"][userNum]['total'] + qAmount) #adds number of total questions answered to user's profile to be able to find average percentage for profile page
        write_to_json_updated_settings()
        buddy_face_talkOption3()
        print("")
        print("\n" + f"You got {checkCounter} questions correct! (Press ENTER to continue)".center(z))
        input()
        os.system('clear')
        buddy_face_talkOption1()
        print("")
        print("\n" + f"You got {checkCounter} questions correct! (Press ENTER to continue)".center(z))
        print("\n" + f"That is an accuracy of {finalScore}%".center(z))
        input()
        os.system('clear')
        buddy_face_talkOption2()
        print("")
        print("\n" + f"You got {checkCounter} questions correct! (Press ENTER to continue)".center(z))
        print("\n" + f"That is an accuracy of {finalScore}%".center(z))
        print("")
        if percentRight >= 80:
            print("Great work! Keep it up!".center(z))
        elif percentRight >= 60:
            print("You're on the right track, keep on learning!".center(z))
        else:
            print("Hey, maybe next time! Keep progressing and you'll get there!".center(z))
        input()
    elif gameMode == "flashcards":
        os.system('clear')
        print("INSTRUCTIONS (Press ENTER to go to next one)".center(z)) #instructions for flashcards so they are not too confusing
        input()
        print("These are the flashcards to help you study!".center(z))
        input()
        print("Press ENTER to flip the card, type NEXT (or N) to move on or BACK (or B) to go to the last card!".center(z))
        input()
        print("At any time, type HOME to return to the home screen or SHUFFLE to shuffle the deck!".center(z))
        input()
        randomFlashChoice = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24] #all possible indexes for flashcards
        random.shuffle(randomFlashChoice) #shuffles list
        if subject == "csp":
            flashSubject = "cspflash"
        elif subject == "stats":
            flashSubject = "statsflash"
        elif subject == "phys":
            flashSubject = "physflash"
        elif subject == "span":
            flashSubject = "spanflash"
        card = 0
        while True:
            os.system('clear')
            buddy_face_standard_smile()
            buddy_face_nameplate_attachment()
            print(Style.BRIGHT + f"{card + 1}/25".center(z) + "\n" + Style.NORMAL) #shows what card the user is on
            if fontColor.lower() == "default":
                print(questions[flashSubject][randomFlashChoice[card]]['word'].center(z))
            elif fontColor.lower() == "red":
                print(Fore.RED + questions[flashSubject][randomFlashChoice[card]]['word'].center(z) + Fore.RESET)
            elif fontColor.lower() == "yellow":
                print(Fore.YELLOW + questions[flashSubject][randomFlashChoice[card]]['word'].center(z) + Fore.RESET)
            elif fontColor.lower() == "green":
                print(Fore.GREEN + questions[flashSubject][randomFlashChoice[card]]['word'].center(z) + Fore.RESET)
            elif fontColor.lower() == "blue":
                print(Fore.BLUE + questions[flashSubject][randomFlashChoice[card]]['word'].center(z) + Fore.RESET)
            elif fontColor.lower() == "magenta":
                print(Fore.MAGENTA + questions[flashSubject][randomFlashChoice[card]]['word'].center(z) + Fore.RESET)
            elif fontColor.lower() == "cyan":
                print(Fore.CYAN + questions[flashSubject][randomFlashChoice[card]]['word'].center(z) + Fore.RESET)
            print("\n\n\n")
            flashInput = input()
            if flashInput.lower() == "next" or flashInput.lower() == "n":
                if card == 24:
                    os.system('clear')
                    print("\n\n" + Style.BRIGHT + "You've reached the end! Would you like to start again?".center(z) + Style.NORMAL)
                    contInput = input()
                    if contInput.lower() == "yes":
                        card = 0
                    else:
                        break
                else:
                    card += 1
            elif flashInput.lower() == "back" or flashInput.lower() == "b":
                if card == 0:
                    pass
                else:
                    card -= 1
            elif flashInput.lower() == "home":
                break
            elif flashInput.lower() == "shuffle":
                random.shuffle(randomFlashChoice)
                card = 0
            elif flashInput.lower() == "quit":
                quit_animation()
            else:
                os.system('clear')
                buddy_face_standard_smile()
                buddy_face_nameplate_attachment()
                print(Style.BRIGHT + f"{card + 1}/25".center(z) + "\n" + Style.NORMAL)
                if fontColor.lower() == "default":
                    print(questions[flashSubject][randomFlashChoice[card]]['definition'].center(z))
                elif fontColor.lower() == "red":
                    print(Fore.RED + questions[flashSubject][randomFlashChoice[card]]['definition'].center(z) + Fore.RESET)
                elif fontColor.lower() == "yellow":
                    print(Fore.YELLOW + questions[flashSubject][randomFlashChoice[card]]['definition'].center(z) + Fore.RESET)
                elif fontColor.lower() == "green":
                    print(Fore.GREEN + questions[flashSubject][randomFlashChoice[card]]['definition'].center(z) + Fore.RESET)
                elif fontColor.lower() == "blue":
                    print(Fore.BLUE + questions[flashSubject][randomFlashChoice[card]]['definition'].center(z) + Fore.RESET)
                elif fontColor.lower() == "magenta":
                    print(Fore.MAGENTA + questions[flashSubject][randomFlashChoice[card]]['definition'].center(z) + Fore.RESET)
                elif fontColor.lower() == "cyan":
                    print(Fore.CYAN + questions[flashSubject][randomFlashChoice[card]]['definition'].center(z) + Fore.RESET)
                print("\n\n\n")
                flashInput = input()
                if flashInput.lower() == "next" or flashInput.lower() == "n":
                    if card == 24:
                        os.system('clear')
                        print("\n\n" + Style.BRIGHT + "You've reached the end! Would you like to start again?".center(z) + Style.NORMAL)
                        contInput = input()
                        if contInput.lower() == "yes":
                            card = 0
                        else:
                            break
                    else:
                        card += 1
                elif flashInput.lower() == "back" or flashInput.lower() == "b":
                    if card == 0:
                        pass
                    else:
                        card -= 1
                elif flashInput.lower() == "home":
                    break
                elif flashInput.lower() == "shuffle":
                    random.shuffle(randomFlashChoice)
                    card = 0
                else:
                    pass

    
#-----------------------------------------------------------
#Actual execution of code
#-----------------------------------------------------------
os.system('clear')
print("Press ENTER to wake up your Study Buddy!".center(z))
input()
study_buddy_wake_animation()
print("Please welcome the one, the only, Study Buddy!".center(z))
user_intro() #asks for the user's name and to name their Study Buddy
while True:
    home_menu()
    if userInput.lower() == "start":
        study_buddy(subject) 
    elif userInput.lower() == "settings":
        settings()
    elif userInput.lower() == "help":
        help_animation()
    elif userInput.lower() == "quit":
        quit_animation()

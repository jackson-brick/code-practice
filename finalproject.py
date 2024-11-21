#All the imports for the code
import time #To add delays between screen outputs
import os #To clear screen and maybe to get terminal size so things can be properly centered no matter what size the screen is
import math #May be used to get scores or to round
from colorama import Style, Fore, Back #Will be used to format and make the outputs look better
import random #Will be used to randomize order of questions and to name the Study Buddy
import sys #will be used for its 'sys.exit()' function to quit the program easily at any time

#-----------------------------------------------------------
#Global Variable Section
#-----------------------------------------------------------
screenSize = os.get_terminal_size() #This gets the width and height of the terminal, respectively
z = screenSize[0] #Puts the width of the screen into a variable; ("blah blah blah".center(z))
subject = "csp" #sets default subject to Comp Sci
fontColor = "default"
screenMode = "dark"
print(Back.BLACK)
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

#-----------------------------------------------------------


def study_buddy_wake_animation():
      #01001010101010010101001010011100110 1
      #10010111010101010101010101010101010 2
      #00010101010101110110101010101111001 3
      #01010011101010101010100101010101010 4
      #10010101011111000101010101001010101 5
      #11010101000101010101101011010010101 6
      #00010101001011000101011010101001100 7
      #11010101001010101010101010101011010 8

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

    print("+-----------------+-----------------+".center(z)) #EMPTY SCREEN
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
    print("If you want to change your preferences, type SETTINGS".center(z))
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


def user_intro():
    global studyBuddyName
    global userName
    global studyBuddyNameList
    randStudyBuddy = [["Merry","Comical","Whimsical","Absurd","Feral","Crazy","Happy","Lazy","Energetic","Smart","Gleeful","Grumpy","Nervous","Peaceful","Playful","Proud","Silly","Sleepy","Creative"],["Dog","Cat","Cow","Hen","Sheep","Rabbit","Duck","Horse","Pig","Turkey","Chicken","Donkey","Goat","Deer","Fish","Bee","Goat","Goose","Rat"]]
    while True:
        os.system('clear')
        buddy_face_standard_smile()
        print("")
        print("Which option would you like to use to name your Study Buddy?".center(z))
        print("\n")
        print("a. Random Name\tb. Custom Name".center(z))
        studyBuddyNameChoice = input("\n") #Asks user if they want to choose their Study Buddy's name or get a random one
        if studyBuddyNameChoice.lower() == "a" or studyBuddyNameChoice.lower() == "b":
            break

        else:
            pass
    while True:
        os.system('clear')
        if studyBuddyNameChoice.lower() == "a":
            studyBuddyNameList = [] #Creates Study Buddy's name using random choices from list
            studyBuddyNameList.append(random.choice(randStudyBuddy[0]))
            studyBuddyNameList.append(random.choice(randStudyBuddy[1]))
            studyBuddyName = " ".join(studyBuddyNameList)
        else:
            buddy_face_standard_smile()
            print("")
            print("What would you like to call your Study Buddy?".center(z))
            studyBuddyName = input("\n")
            studyBuddyName = studyBuddyName.capitalize()
        os.system('clear')
        buddy_face_question()
        print("")
        print(f"{studyBuddyName}? Does that sound right?".center(z))
        checkStudyName = input("\n")
        if checkStudyName.lower() == "yes":
            break
        else:
            pass
    while True:
        os.system('clear')
        buddy_face_standard_smile()
        print("")
        print("What would you like to be called?".center(z))
        userName = input("\n")
        os.system('clear')
        buddy_face_question()
        print("")
        print(f"{userName.capitalize()}? Am I saying that right?".center(z))
        checkName = input("\n")
        if checkName.lower() == "yes":
            userName = userName.capitalize()
            os.system('clear')
            break
        else:
            pass
    help_animation()



def home_menu():
    global userInput
    os.system('clear')
    buddy_face_standard_smile()
    print("")
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
    if screenMode == "dark":
        print(Back.BLACK)
    elif screenMode == "light":
        print(Back.WHITE)
    os.system('clear')
    global subject
    buddy_face_standard_smile()
    print("|                                   |".center(z))
    print("|              SETTINGS             |".center(z))
    print("|                                   |".center(z))
    print("+-----------------+-----------------+".center(z))
    print("")
    #order will be csp, stats, physics, spanish
    global fontColor
    settingSentence = ["What is the name of the base computers use to count and read?" , "True or false: the median is more resistant than the mean" , "How do you find the coefficient of friction using normal and frictional force?","Qué quiere decir la palabra \"perro\" en inglés?"]
    if subject.lower() == "csp":
        if fontColor.lower() == "default":
            print(Style.BRIGHT + settingSentence[0].center(z) + Style.RESET_ALL)
            if screenMode == "dark":
                print(Back.BLACK)
            elif screenMode == "light":
                print(Back.WHITE)
        elif fontColor.lower() == "red":
            print(Style.BRIGHT + Fore.RED + settingSentence[0].center(z) + Style.RESET_ALL)
            if screenMode == "dark":
                print(Back.BLACK)
            elif screenMode == "light":
                print(Back.WHITE)
        elif fontColor.lower() == "green":
            print(Style.BRIGHT + Fore.GREEN + settingSentence[0].center(z) + Style.RESET_ALL)
            if screenMode == "dark":
                print(Back.BLACK)
            elif screenMode == "light":
                print(Back.WHITE)
        elif fontColor.lower() == "yellow":
            print(Style.BRIGHT + Fore.YELLOW + settingSentence[0].center(z) + Style.RESET_ALL)
            if screenMode == "dark":
                print(Back.BLACK)
            elif screenMode == "light":
                print(Back.WHITE)
        elif fontColor.lower() == "blue":
            print(Style.BRIGHT + Fore.BLUE + settingSentence[0].center(z) + Style.RESET_ALL)
            if screenMode == "dark":
                print(Back.BLACK)
            elif screenMode == "light":
                print(Back.WHITE)
        elif fontColor.lower() == "magenta":
            print(Style.BRIGHT + Fore.MAGENTA + settingSentence[0].center(z) + Style.RESET_ALL)
            if screenMode == "dark":
                print(Back.BLACK)
            elif screenMode == "light":
                print(Back.WHITE)
        elif fontColor.lower() == "cyan":
            print(Style.BRIGHT + Fore.CYAN + settingSentence[0].center(z) + Style.RESET_ALL)
            if screenMode == "dark":
                print(Back.BLACK)
            elif screenMode == "light":
                print(Back.WHITE)
    elif subject.lower() == "stats":
        if fontColor.lower() == "default":
            print(Style.BRIGHT + settingSentence[1].center(z) + Style.RESET_ALL)
            if screenMode == "dark":
                print(Back.BLACK)
            elif screenMode == "light":
                print(Back.WHITE)
        elif fontColor.lower() == "red":
            print(Style.BRIGHT + Fore.RED + settingSentence[1].center(z) + Style.RESET_ALL)
            if screenMode == "dark":
                print(Back.BLACK)
            elif screenMode == "light":
                print(Back.WHITE)
        elif fontColor.lower() == "green":
            print(Style.BRIGHT + Fore.GREEN + settingSentence[1].center(z) + Style.RESET_ALL)
            if screenMode == "dark":
                print(Back.BLACK)
            elif screenMode == "light":
                print(Back.WHITE)
        elif fontColor.lower() == "yellow":
            print(Style.BRIGHT + Fore.YELLOW + settingSentence[1].center(z) + Style.RESET_ALL)
            if screenMode == "dark":
                print(Back.BLACK)
            elif screenMode == "light":
                print(Back.WHITE)
        elif fontColor.lower() == "blue":
            print(Style.BRIGHT + Fore.BLUE + settingSentence[1].center(z) + Style.RESET_ALL)
            if screenMode == "dark":
                print(Back.BLACK)
            elif screenMode == "light":
                print(Back.WHITE)
        elif fontColor.lower() == "magenta":
            print(Style.BRIGHT + Fore.MAGENTA + settingSentence[1].center(z) + Style.RESET_ALL)
            if screenMode == "dark":
                print(Back.BLACK)
            elif screenMode == "light":
                print(Back.WHITE)
        elif fontColor.lower() == "cyan":
            print(Style.BRIGHT + Fore.CYAN + settingSentence[1].center(z) + Style.RESET_ALL)
            if screenMode == "dark":
                print(Back.BLACK)
            elif screenMode == "light":
                print(Back.WHITE)
    elif subject.lower() == "phys":
        if fontColor.lower() == "default":
            print(Style.BRIGHT + settingSentence[2].center(z) + Style.RESET_ALL)
            if screenMode == "dark":
                print(Back.BLACK)
            elif screenMode == "light":
                print(Back.WHITE)
        elif fontColor.lower() == "red":
            print(Style.BRIGHT + Fore.RED + settingSentence[2].center(z) + Style.RESET_ALL)
            if screenMode == "dark":
                print(Back.BLACK)
            elif screenMode == "light":
                print(Back.WHITE)
        elif fontColor.lower() == "green":
            print(Style.BRIGHT + Fore.GREEN + settingSentence[2].center(z) + Style.RESET_ALL)
            if screenMode == "dark":
                print(Back.BLACK)
            elif screenMode == "light":
                print(Back.WHITE)
        elif fontColor.lower() == "yellow":
            print(Style.BRIGHT + Fore.YELLOW + settingSentence[2].center(z) + Style.RESET_ALL)
            if screenMode == "dark":
                print(Back.BLACK)
            elif screenMode == "light":
                print(Back.WHITE)
        elif fontColor.lower() == "blue":
            print(Style.BRIGHT + Fore.BLUE + settingSentence[2].center(z) + Style.RESET_ALL)
            if screenMode == "dark":
                print(Back.BLACK)
            elif screenMode == "light":
                print(Back.WHITE)
        elif fontColor.lower() == "magenta":
            print(Style.BRIGHT + Fore.MAGENTA + settingSentence[2].center(z) + Style.RESET_ALL)
            if screenMode == "dark":
                print(Back.BLACK)
            elif screenMode == "light":
                print(Back.WHITE)
        elif fontColor.lower() == "cyan":
            print(Style.BRIGHT + Fore.CYAN + settingSentence[2].center(z) + Style.RESET_ALL)
            if screenMode == "dark":
                print(Back.BLACK)
            elif screenMode == "light":
                print(Back.WHITE)
    elif subject.lower() == "span":
        if fontColor.lower() == "default":
            print(Style.BRIGHT + settingSentence[3].center(z) + Style.RESET_ALL)
            if screenMode == "dark":
                print(Back.BLACK)
            elif screenMode == "light":
                print(Back.WHITE)
        elif fontColor.lower() == "red":
            print(Style.BRIGHT + Fore.RED + settingSentence[3].center(z) + Style.RESET_ALL)
            if screenMode == "dark":
                print(Back.BLACK)
            elif screenMode == "light":
                print(Back.WHITE)
        elif fontColor.lower() == "green":
            print(Style.BRIGHT + Fore.GREEN + settingSentence[3].center(z) + Style.RESET_ALL)
            if screenMode == "dark":
                print(Back.BLACK)
            elif screenMode == "light":
                print(Back.WHITE)
        elif fontColor.lower() == "yellow":
            print(Style.BRIGHT + Fore.YELLOW + settingSentence[3].center(z) + Style.RESET_ALL)
            if screenMode == "dark":
                print(Back.BLACK)
            elif screenMode == "light":
                print(Back.WHITE)
        elif fontColor.lower() == "blue":
            print(Style.BRIGHT + Fore.BLUE + settingSentence[3].center(z) + Style.RESET_ALL)
            if screenMode == "dark":
                print(Back.BLACK)
            elif screenMode == "light":
                print(Back.WHITE)
        elif fontColor.lower() == "magenta":
            print(Style.BRIGHT + Fore.MAGENTA + settingSentence[3].center(z) + Style.RESET_ALL)
            if screenMode == "dark":
                print(Back.BLACK)
            elif screenMode == "light":
                print(Back.WHITE)
        elif fontColor.lower() == "cyan":
            print(Style.BRIGHT + Fore.CYAN + settingSentence[3].center(z) + Style.RESET_ALL)
            if screenMode == "dark":
                print(Back.BLACK)
            elif screenMode == "light":
                print(Back.WHITE)
    print("")
    
    global settingInput
    if subject == "csp":
        subjectName = "Computer Science"
    elif subject == "stats":
        subjectName = "Statistics"
    elif subject == "phys":
        subjectName = "Physics"
    elif subject == "span":
        subjectName = "Spanish"
    print(f"Subject:   {subjectName}".center(z))
    print("")
    print(f"Font color:   {fontColor}".center(z))
    print("")
    print

    settingInput = input(Style.BRIGHT + "To change a setting, type the name of the setting".center(z) + "Type BACK to return to the start screen:".center(z) + "\n" + Style.RESET_ALL)
    if screenMode == "dark":
        print(Back.BLACK)
    elif screenMode == "light":
        print(Back.WHITE)
    os.system('clear')
    if settingInput.lower() == "subject":
        print("Computer Science (CSP) | Statistics (STATS) | Physics (PHYS) | Spanish (SPAN)".center(z))
        subjectPreference = input()
        if subjectPreference.lower() == "csp" or subjectPreference.lower() == "phys" or subjectPreference.lower() == "span" or subjectPreference.lower() == "stats":
            subject = subjectPreference.lower()
        else:
            pass
            
    elif settingInput.lower() == "font color":
        print(("Default   " + Fore.RED + "Red   " + Fore.YELLOW + "Yellow   " + Fore.GREEN + "Green   " + Fore.BLUE + "Blue   " + Fore.MAGENTA + "Magenta   " + Fore.CYAN + "Cyan").center(z))
        colorPreference = input()
        if colorPreference.lower() == "red":
            fontColor = "Red"
            os.system('clear')
        elif colorPreference.lower() == "yellow":
            fontColor = "Yellow"
            os.system('clear')
        elif colorPreference.lower() == "green":
            fontColor = "Green"
            os.system('clear')
        elif colorPreference.lower() == "blue":
            fontColor = "Blue"
            os.system('clear')
        elif colorPreference.lower() == "magenta":
            fontColor = "Magenta"
            os.system('clear')
        elif colorPreference.lower() == "cyan":
            fontColor = "Cyan"
            os.system('clear')
        elif colorPreference.lower() == "default":
            fontColor = "Default"
            os.system('clear')
    else:
        pass


def study_buddy(subject):
    print("studyBuddy DO LATER")
    
#def check_answer():
    
print("Press ENTER to wake up your Study Buddy!".center(z))
input()
#study_buddy_wake_animation()
print("Please welcome the one, the only, Study Buddy!".center(z))
user_intro() #asks for the user's name and to name their Study Buddy
while True:
    home_menu()
    if userInput.lower() == "start":
        study_buddy(subject) #MAKE SURE TO DO LATER
    elif userInput.lower() == "settings":
        while True:
            settings()
            if settingInput == "back":
                break
    elif userInput.lower() == "help":
        help_animation()
    elif userInput.lower() == "quit":
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
        sys.exit()

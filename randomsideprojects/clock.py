import time
import os
z = os.get_terminal_size()
z = z[0]
start = False

#time gives us the time from 
#Format: Sun Dec 29 22:17:31 2024
x = time.time() - 28800
irl = time.ctime(x)
strmin = irl[14] + irl[15]
intmin = int(strmin)
lockedminute = intmin

while True:
    os.system('clear')
    x = time.time() - 28800
    irl = time.ctime(x)
    
    dayname = irl[0] + irl[1] + irl[2]
    month = irl[4] + irl[5] + irl[6]
    if irl[8] == " ":
        daynum = "0" + irl[9]
    else:
        daynum = irl[8] + irl[9]
    strhour = irl[11] + irl[12]
    inthour = int(strhour)
    strmin = irl[14] + irl[15]
    intmin = int(strmin)
    if inthour > 12:
        inthour-=12
        strhour = str(inthour)
        period = "pm"
    elif inthour == 0:
        inthour+=12
        strhour = str(inthour)
        period = "am"
    elif inthour == 12:
        period = "pm"
    strsec = irl[17] + irl[18]
    intsec = int(strsec)
    year = irl[-4] + irl[-3] + irl[-2] + irl[-1]
    if start == True:
        print("+------------------------------------------+".center(z))
        print("+                                          +".center(z))
        print(f"+             Date : {dayname} {month} {daynum}            +".center(z))
        print("+                                          +".center(z))
        print("+------------------------------------------+".center(z))
        
        print("+------------------------------------------+".center(z))
        print("+                                          +".center(z))
        print(f"+                  {strhour}:{strmin} {period}                 +".center(z))
        print("+                                          +".center(z))
        print("+------------------------------------------+".center(z))
        time.sleep(60)
    else:
        print("+------------------------------------------+".center(z))
        print("+                                          +".center(z))
        print(f"+             Date : {dayname} {month} {daynum}            +".center(z))
        print("+                                          +".center(z))
        print("+------------------------------------------+".center(z))
        
        print("+------------------------------------------+".center(z))
        print("+                                          +".center(z))
        print(f"+                  {strhour}:{strmin} {period}                 +".center(z))
        print("+                                          +".center(z))
        print("+------------------------------------------+".center(z))
        time.sleep(60-intsec)
        if intmin != lockedminute:
            start = True


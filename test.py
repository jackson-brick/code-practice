import os
import time
z = os.get_terminal_size()
z=z[0]

print("I will do prompts 9, 10, 11, and 12".center(z))
print("")
print("Press ENTER to continue".center(z))
input()

listOfBooks = [{"title":"The Great Gatsby","author":"F. Scott Fitzgerald","year":1925},{"title":"Adventures of Huckleberry Finn","author":"Mark Twain","year":1885},{"title":"Percy Jackson and the Lightning Thief","author":"Rick Riordan","year":2005},{"title":"Percy Jackson and the Sea of Monsters","author":"Rick Riordan","year":2006}]

def findBookByAuthor(books,author):
    matchVar = False
    for book in range(len(books)):
        if author.lower().strip() == books[book]["author"].lower():
            if matchVar == False:
                matchVar = True
                while True:
                    os.system('clear')
                    print("Type EXIT to go back to the author page".center(z))
                    print(books[book]["author"].center(z))
                    print("")
                    for entry in books:
                        if books[book]["author"] == entry["author"]:
                            print((entry["title"] + " : " + str(entry["year"])).center(z))
                    print("")
                    bookInput = input()
                    if bookInput.lower().strip() == "exit":
                        break


while True:
    os.system('clear')
    print("Prompt 9".center(z))
    authorList = []
    for book in listOfBooks:
        matchVar = False
        for author in authorList:
            if author == book["author"]:
                matchVar = True
        if matchVar == False:
            authorList.append(book["author"])
    for author in authorList:
        print(author.center(z))
    print("")
    print("Type the name of an author to see their works!".center(z))
    print("Type DONE to move to the next prompt".center(z))
    print("")
    authorInput = input()
    if authorInput.lower().strip() == "done":
        break
    else:
        os.system('clear')
        findBookByAuthor(listOfBooks,authorInput)


evenOrOdd = {"even":[],"odd":[]}
keyList = ("even","odd")
while True:
    os.system('clear')
    print("Prompt 10".center(z))
    print(f"{keyList[0]} : {evenOrOdd[keyList[0]]}".center(z))
    print(f"{keyList[1]} : {evenOrOdd[keyList[1]]}".center(z))
    print("")
    print("Type a number and it will be sorted into the dictionary".center(z))
    print("Type DONE to move to the next prompt".center(z))
    evenOdd = input()
    evenOddDigit = True
    for char in evenOdd:
        if char.isdigit() or char == ".":
            pass
        else:
            evenOddDigit = False
    if evenOddDigit == True:
        if int(evenOdd[-1]) % 2 == 1:
            evenOrOdd["odd"].append(evenOdd)
        else:
            evenOrOdd["even"].append(evenOdd)
            
    else:
        if evenOdd.lower().strip() == "done":
            break

os.system('clear')
print("Prompt 11".center(z))

studentClass = {"Jackson Brick":{"math":100,"english":99,"csp":100},"Benjamin Gonzalez":{"math":94,"english":89,"csp":100},"Evany Stately":{"math":95,"english":98,"csp":91},"Sho Kitagawa":{"math":95,"english":98,"csp":91}}

def findHighestAverage(studentClass):
    studentKeys = list(studentClass.keys())
    keyCounter = 0
    highestStudent = [0]
    for student in studentClass:
        totalGrade = 0
        for grade in studentClass[student]:
            totalGrade += studentClass[student][grade]
        totalGrade /= 3
        if totalGrade > highestStudent[0]:
            highestStudent = [int(totalGrade),studentKeys[keyCounter]]
        keyCounter+=1
    return highestStudent

print("")
print("Students:".center(z))
for student in studentClass:
    print(student.center(z))
    for grade in studentClass[student]:
        print(f"{grade.upper()} - {studentClass[student][grade]}".center(z))
    print("")
print("")
print(f"{findHighestAverage(studentClass)[1]} has the highest average grade of {findHighestAverage(studentClass)[0]}".center(z))
print("")
print("Press ENTER to continue to the next prompt".center(z))
input()
os.system('clear')
print("Prompt 12".center(z))

queue = ["Jackson","Benji","Samuel"]

def enqueue(queue,item):
    queue.append(item.capitalize())
def dequeue(queue,name):
    queue.remove(name.capitalize())
    os.system('clear')
    print("You left the line!".center(z))
    quit()
def peek(queue):
    centeredSentence = ""
    for person in range(len(queue)):
        if person == len(queue)-2:
            centeredSentence += f"and {queue[person]} are in front of you!"
        elif person == len(queue)-1:
            pass
        else:
            centeredSentence += f"{queue[person]}, "
    print(centeredSentence)
    time.sleep(2)
        
print("There is a line of people in front of you! To step in line, you must give your name!".center(z))
name = input()
enqueue(queue,name)
while True:
    print("")
    print("You can now peek around the person in front of you to see who is left in the queue (Type PEEK) or you can leave the line (Type EXIT)".center(z))
    queueInput = input()
    if queueInput.lower().strip() == "exit":
        dequeue(queue,name)
    elif queueInput.lower().strip() == "peek":
        peek(queue)



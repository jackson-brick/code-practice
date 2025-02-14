import csv
import os
z=os.get_terminal_size()
z=z[0]

bibleList = []
with open('bibleentries.csv','r') as file:
    bible = csv.DictReader(file)
    for line in bible:
        bibleList.append(line)
bookList = []
for line in bibleList:
    if line["Book Name"] not in bookList:
        bookList.append(line["Book Name"])

def write():
    for line in bibleList:
        os.system('clear')
        if line["Notes"] == "":
            print(f"{line["Book Name"]} {line["Chapter"]}:{line["Verse"]}".center(z))
            print("")
            print(line["Text"].center(z))
            print("")
            notes = input()
            if notes.lower().strip() == "done":
                break
            else:
                line["Notes"] = notes
            


write()





with open('bibleentries.csv','w',newline='') as file:
    field_names = ["Verse ID","Book Name","Book Number","Chapter","Verse","Text","Notes"]
    writer = csv.DictWriter(file,fieldnames=field_names)
    writer.writeheader()
    for line in bibleList:
        writer.writerow(line)







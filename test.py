import csv

words = []
with open('hangman.csv','r') as file:
    word = csv.reader(file)
    header = next(word)


with open('hangman.csv','w',newline="") as file:
    field_names = ["word"]
    writer = csv.DictWriter(file, fieldnames= field_names)
    writer.writeheader()
    for line in header:
        writer.writerow(line)
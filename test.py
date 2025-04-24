import csv

words = []
with open('hangman.csv','r') as file:
    word = csv.DictReader(file)
    for line in word:
        print(line)
        input()
        words.append(line)
print(words)
print(words[0])
print(words[-1])
import random

mcqList = ["a","b","c","d"]
correctAnswer = "c"
mcqList.remove(correctAnswer)
mcqList.remove(random.choice(mcqList))

print(mcqList)

print(int(7.9))
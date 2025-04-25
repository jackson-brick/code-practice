word = input("Word to be tokenized: ")
word=word.strip().lower()
finalCount = 0
weightCount = 0
for i in range(len(word)):
    finalCount +=  ((i+1)*ord(word[i]))
    weightCount += (i+1)

print(finalCount/weightCount)




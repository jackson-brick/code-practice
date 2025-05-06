word = input("Password to be encrypted: ")

wordVal = 0
for i in word:
    wordVal += ord(i)
print(wordVal)




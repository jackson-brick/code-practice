import os

screenSize = os.get_terminal_size()
z = int(screenSize[0])

paragraph = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair."
mylist = []

usedParagraph = paragraph.split()
#for word in range(len(usedParagraph)):
    #usedParagraph[word] = usedParagraph[word] + " "


print(*usedParagraph)

wordAcrossScreen = 0
emptySpaceCounter = 0
#for word in usedParagraph:
    #wordAcrossScreen += int(len(word))
    #if wordAcrossScreen > z:
        #wordAcrossScreen -= int(len(word))
        #for i in range(z-wordAcrossScreen):
            #print(" ", end = "")
        #wordAcrossScreen = 0
    #else:
        #print(word, end = "")
    








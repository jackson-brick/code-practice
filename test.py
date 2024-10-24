import os

screenSize = os.get_terminal_size()
z = int(screenSize[0])

#paragraph = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair."
#paragraph = "Two roads diverged in a wood, and I took the one less traveled by, and that has made all the difference."
paragraph = "…and Gibraltar as a girl where I was a Flower of the mountain yes when I put the rose in my hair like the Andalusian girls used or shall I wear a red yes and how he kissed me under the Moorish wall and I thought well as well him as another and then I asked him with my eyes to ask again yes and then he asked me would I yes to say yes my mountain flower and first I put my arms around him yes and drew him down to me so he could feel my breasts all perfume yes and his heart was going like mad and yes I said yes I will Yes."
mylist = []

usedParagraph = paragraph.split()
for word in range(len(usedParagraph)):
    usedParagraph[word] = usedParagraph[word] + " "



wordAcrossScreen = 0
emptySpaceCounter = 0
for word in usedParagraph:
    wordAcrossScreen += int(len(word))
    if wordAcrossScreen > z:
        print("\n" + word, end = "")
        wordAcrossScreen = 0 + len(word)
    else:
        print(word, end = "")
    








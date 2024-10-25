import os
import time
import random
import math

screenSize = os.get_terminal_size()
z = int(screenSize[0])



def loading_sequence(seconds_to_load):
    loadingList = ["fun paragraphs" , "challenging words" , "all the code" , "security measures" , "eye-tracking software" , "the CIA's confidential files" , "your address" , "my shopping list" , "all the answers to the algebra test"]
    usedLoadingList = []
    for lcv in range(seconds_to_load):
        usedLoadingList.append(random.choice(loadingList))
        loadingList.remove(f"{usedLoadingList[lcv]}")
    os.system('clear')
    time.sleep(0.5)
    while seconds_to_load > 0:
        print(f"Loading {usedLoadingList[(seconds_to_load - 1)]}".center(z))
        time.sleep(0.5)
        os.system('clear')
        print(f"Loading {usedLoadingList[(seconds_to_load - 1)]}  .".center(z))
        time.sleep(0.5)
        os.system('clear')
        print(f"Loading {usedLoadingList[(seconds_to_load - 1)]}  .  .".center(z))
        time.sleep(0.5)
        os.system('clear')
        print(f"Loading {usedLoadingList[(seconds_to_load - 1)]}  .  .  .".center(z))
        time.sleep(1)
        os.system('clear')
        seconds_to_load -= 1
    while len(usedLoadingList) > 0:
        loadingList.append(usedLoadingList[-1])
        usedLoadingList.pop(-1)



print("Press ENTER to launch Type Racer\n\n".center(z))
input()
os.system('clear')

loading_sequence(4)

print("+-+-+-+-+-+-+-+-+--+-+-+-+-+-+-+-+-+".center(z))
print("+                                  +".center(z))
print("+            Type Racer            +".center(z))
print("+                                  +".center(z))
print("+              Welcome             +".center(z))
print("+                                  +".center(z))
print("+-+-+-+-+-+-+-+-+--+-+-+-+-+-+-+-+-+".center(z))

print("")
print("You will receive a prompt to type. It must be typed properly. Press ENTER to begin.\n\n".center(z))
input()



def print_paragraph():
    global checkParagraph
    global usedParagraph
    paragraph = ["It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair." , "…and Gibraltar as a girl where I was a Flower of the mountain yes when I put the rose in my hair like the Andalusian girls used or shall I wear a red yes and how he kissed me under the Moorish wall and I thought well as well him as another and then I asked him with my eyes to ask again yes and then he asked me would I yes to say yes my mountain flower and first I put my arms around him yes and drew him down to me so he could feel my breasts all perfume yes and his heart was going like mad and yes I said yes I will Yes." , "The only people for me are the mad ones, the ones who are mad to live, mad to talk, mad to be saved, desirous of everything at the same time, the ones who never yawn or say a commonplace thing, but burn, burn, burn like fabulous yellow roman candles exploding like spiders across the stars." , ". . . this is how to make a good medicine for a cold; this is how to make a good medicine to throw away a child before it even becomes a child; this is how to catch a fish; this is how to throw back a fish you don't like, and that way something bad won't fall on you; this is how to bully a man; this is how a man bullies you; this is how to love a man; and if this doesn't work there are other ways, and if they don't work don't feel too bad about giving up; this is how to spit up in the air if you feel like it, and this is how to move quick so that it doesn't fall on you; this is how to make ends meet; always squeeze bread to make sure it's fresh; but what if the baker won't let me feel the bread?; you mean to say that after all you are really going to be the kind of woman who the baker won't let near the bread?" , "I must not fear. Fear is the mind-killer. Fear is the little-death that brings total obliteration. I will face my fear. I will permit it to pass over me and through me. And when it has gone past I will turn the inner eye to see its path. Where the fear has gone there will be nothing. Only I will remain." , "I am an invisible man. No, I am not a spook like those who haunted Edgar Allan Poe; nor am I one of your Hollywood-movie ectoplasms. I am a man of substance, of flesh and bone, fiber and liquids—and I might even be said to possess a mind. I am invisible, understand, simply because people refuse to see me." , "He who has felt the deepest grief is best able to experience supreme happiness. Live, then, and be happy, beloved children of my heart, and never forget, that until the day God will deign to reveal the future to man, all human wisdom is contained in these two words: \"Wait and Hope.\""]
    usedParagraph = random.choice(paragraph)
    checkParagraph = usedParagraph  
    usedParagraph = usedParagraph.split()
    for word in range(len(usedParagraph)):
        usedParagraph[word] = usedParagraph[word] + " "

    wordAcrossScreen = 0
    for word in usedParagraph:
        wordAcrossScreen += int(len(word))
        if wordAcrossScreen > z:
            print("\n" + word, end = "")
            wordAcrossScreen = 0 + len(word)
        else:
            print(word, end = "")

while True:
    print_paragraph()
    timeStart = time.time()
    response = input()
    if response == checkParagraph:
        break
    else:
        print("You've made a mistake! Try again. Press ENTER to start.")
        input()
        
timeEnd = time.time()
timeDeltaTime = timeEnd - timeStart
wpm = (len(usedParagraph) * 60) / timeDeltaTime
print(f"You correctly typed the paragraph with {round(wpm , 1)} words per minute")



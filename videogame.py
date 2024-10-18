#This will be a videogame about a player and their cat who level up to fight bosses and eventually take over their kingdom
import time
#import sys
import random

healthStat = 0
jumpStat = 0
strengthStat = 0
speedStat = 0
power1Name = " "
power1Dam = 0
power2Name = " "
power2Dam = 0
power3Name = " "
power3Dam = 0
power4Name = " "
power4Dam = 0


def intro():
    print("\n*You wake up in the ground. You do not remember how you got there, or why there is a cat next to you. You only remember your name. All of a sudden, a man in a horse-drawn carriage appears coming down the road.*")
    
    name = input("\nJohn: Welcome- erm... Well, I suppose I don't know your name yet traveller. What should I call you?\n\n")
    
    nameConfirm = input(f"\n{name.capitalize()}? Am I saying that right?\n\n")
    while True:
        if nameConfirm.upper() == "YES":
            break
        elif nameConfirm.upper() == "NO":
            name = input("\nI'm sorry, for the mistake, what should I call you then?\n\n")
            nameConfirm = input(f"\n{name.capitalize()}? Am I saying that right?\n\n")
        else:
            nameConfirm = input("I'm sorry, was that a yes or a no?\n")

    print(f"\nWell then {name}, let me show you around!")
    time.sleep(2)
    print("\nI see your cat has already chosen you. That is a lucky thing you know.")
    time.sleep(4)
    print("\nIn this kingdom, cats can choose you as their owner, but this is something that can take a lifetime to occur.")
    time.sleep(4)
    print("\nYou are lucky yours chose you so early in your life.")
    time.sleep(4)
    print("\nI reckon you don't know how you got here. That is very common in this place, though we do not know why.")
    time.sleep(4)
    print("\nIn the village, we try not to challenge the existing order because the consequences here are deadly.")
    time.sleep(4)
    print("\nThough there are some scary beings out there in this forest, they only come out at night.")
    time.sleep(4)
    print("\nThe real worry us villagers have is the king. He is vile and ruthless, and does not like newcomers.")
    time.sleep(5)
    print("\n should really get used to the powers of your cat. Wait, did I mention your cat has powers?")
    time.sleep(5)
    print("\nHave you even chosen the powers yet? No? Well, hold your hand above the cat's head, yes like that, and choose its abilities.")
    time.sleep(5)
    charChoice = input("\nChoose what abilities your cat has. Press ENTER to cycle through them. Enter the name of the cat you want underneath its description.")
    charChoice = "empty"
    while charChoice =="empty":
        print("\nHulkat\nAbility: Strength\nWeaknesses: Poison Attacks, Speed Attacks")
        charChoice = input()
        charChoice = charChoice.lower()
        if charChoice == "hulkat":
            charChoice = charChoice.capitalize()
            healthStat = 180
            jumpStat = 50
            strengthStat = 300
            speedStat = 50
            power1Name = "Hulkat Smash"
            power1Dam = 150
            power2Name = "Right hook, Upper cat"
            power2Dam = 120
            power3Name = "Muscle shield"
            power3Dam = 0
            power4Name = "Sonic clap"
            power4Dam = 30
            break
        else:
            charChoice = "empty"
        print("\nSpeedster\nAbility: Speed\nWeaknesses: Ice Attacks, Fire Attacks")
        charChoice =  input()
        charChoice = charChoice.lower()
        if charChoice == "speedster":
            charChoice = charChoice.capitalize()
            break
        else:
            charChoice = "empty"
        print("\nHelikitty\nAbility: Flight\nWeaknesses: Water Attacks, Earth Attacks")
        charChoice = input()
        charChoice = charChoice.lower()
        if charChoice == "helikitty":
            charChoice = charChoice.capitalize()
            break
        else:
            charChoice = "empty"
        print("\nBrick\nAbility: Impenetrable Skin\nWeaknesses: Strength Attacks, Flight Attacks")
        charChoice = input()
        charChoice = charChoice.lower()
        if charChoice == "brick":
            charChoice = charChoice.capitalize()
            break
        else:
            charChoice = "empty"
    print(f"\nYou have chosen {charChoice}!")

    time.sleep(2)
    dial = input("\nNow that you have chosen your cat, maybe you can help our village deal with some of the monsters that have been terrorizing us. Come with me!")
def first_fight():
    print("John: Welcome to the villa- AHHHHHHH! ")





intro()
loading_sequence(3)
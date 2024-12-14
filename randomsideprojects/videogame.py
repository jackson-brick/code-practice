#This will be a videogame about a player and their cat who level up to fight bosses and eventually take over their kingdom
import time
#import sys
import random
import os

screen_size = os.get_terminal_size()

healthPoints = 200
power1Name = " "
power1Dam = 150
power2Name = " "
power2Dam = 120
power3Name = " "
power3Dam = 0
power4Name = " "
power4Dam = 30
print("*Press ENTER to continue\n\n")
input()

def intro():
    print("\n*You wake up in the ground. You do not remember how you got there, or why there is a cat next to you. You only remember your name. All of a sudden, a man in a horse-drawn carriage appears coming down the road.*")
    input()
    os.system('clear')
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
    os.system('clear')
    print(f"\nWell then {name}, let me show you around!")
    input()
    os.system('clear')
    print("\nI see your cat has already chosen you. That is a lucky thing you know.")
    input()
    os.system('clear')
    print("\nIn this kingdom, cats can choose you as their owner, but this is something that can take a lifetime to occur.")
    input()
    os.system('clear')
    print("\nYou are lucky yours chose you so early in your life.")
    input()
    os.system('clear')
    print("\nI reckon you don't know how you got here. That is very common in this place, though we do not know why.")
    input()
    os.system('clear')
    print("\nIn the village, we try not to challenge the existing order because the consequences here are deadly.")
    input()
    os.system('clear')
    print("\nThough there are some scary beings out there in this forest, they only come out at night.")
    input()
    os.system('clear')
    print("\nThe real worry us villagers have is the king. He is vile and ruthless, and does not like newcomers.")
    input()
    os.system('clear')
    print("\n You should really get used to the powers of your cat. Wait, did I mention your cat has powers?")
    input()
    os.system('clear')
    print("\nHave you even chosen the powers yet? No? Well, hold your hand above the cat's head, yes like that, and choose its abilities.")
    input()
    os.system('clear')
    global charChoice
    charChoice = input("\nChoose what abilities your cat has. Press ENTER to cycle through them. Enter the name of the cat you want underneath its description.")
    charChoice = "empty"
    while charChoice =="empty":
        os.system('clear')
        print("\nKittypool\nDescription: Made of water, the ocean is his domain. Most cats don't like baths; they fear the wrath of KittyPool\nWeaknesses: Bombocat, oil")
        charChoice = input()
        charChoice = charChoice.lower()
        if charChoice == "kittypool":
            charChoice = charChoice.capitalize()
            global power1Name
            global power2Name
            global power3Name
            global power4Name
            power1Name = "Torrent"
            power2Name = "Tsunami"
            power3Name = "Wave Dash"
            power4Name = "Barrier Reef"
            break
        else:
            charChoice = "empty"
        os.system('clear')
        print("\nBombocat\nAbility: This fiery hot-head can get heated pretty easily. You better not be around when the flames engulf him\nWeaknesses: Skytty, rain")
        charChoice =  input()
        charChoice = charChoice.lower()
        if charChoice.lower == "bombocat":
            charChoice = charChoice.capitalize()
            power1Name = "Nuke"
            power2Name = "Grenade"
            power3Name = "Mushroom Cloud"
            power4Name = "Fire Wall"
            break
        else:
            charChoice = "empty"
        os.system('clear')
        print("\nPicatchu\nAbility: With lightning at his fingertips, Picatchu can smite his opponents with the fury of a god\nWeaknesses: Kittypool, bad conductors")
        charChoice = input()
        if charChoice.lower() == "picatchu":
            charChoice = charChoice.capitalize()
            power1Name = "Thunderstrike"
            power2Name = "Zeus's Smite"
            power3Name = "Energy Shield"
            power4Name = "Thunder Clap"
            break
        else:
            charChoice = "empty"
        os.system('clear')
        print("\nSkytty\nAbility: The skies are at Cloud Cat's whim, from the unforgiving winds of a tornado to the force of gravity that we encounter every day\nWeaknesses: Picatchu, light pollution")
        charChoice = input()
        if charChoice.lower() == "brick":
            charChoice = charChoice.capitalize()
            power1Name = "Downpour"
            power2Name = "Hail Storm"
            power3Name = "Eye of the Storm"
            power4Name = "Wind Wall"
            break
        else:
            charChoice = "empty"
    os.system('clear')
    print(f"\nYou have chosen {charChoice}!")

    time.sleep(2.5)
    os.system('clear')
    input("\nNow that you have chosen your cat, maybe you can help our village deal with some of the monsters that have been terrorizing us. Come with me!")

def loading_sequence(seconds_to_load):
    os.system('clear')
    time.sleep(0.5)
    while seconds_to_load > 0:
        print("Loading")
        time.sleep(1)
        os.system('clear')
        print("Loading  .")
        time.sleep(1)
        os.system('clear')
        print("Loading  .  .")
        time.sleep(1)
        os.system('clear')
        print("Loading  .  .  .")
        time.sleep(1)
        os.system('clear')
        seconds_to_load -= 1



def fight_sequence():
    while True:
        used_power = input(f"Which power will {charChoice.capitalize()} use?")
        print(f"1. {power1Name}\n2. {power2Name}\n3. {power3Name}\n4. {power4Name}")
        #while enemyHealth > 0:






intro()
loading_sequence(2)

print("John: Welcome to the villa- AHHHHHHH! ")
time.sleep(1)
print("John: A Mutt is attacking me! Quick, have your cat fight off the Mutt!")
enemyHealth = 200
time.sleep(2)
print("John: Remember that your first two powers are the strongest, but have the longest cool time.")
time.sleep(2)
print("John: Your last two powers are defensive and must be deployed before your opponent attacks. It can only be held up for one attack.")
#This will be a videogame about a player and their cat who level up to fight bosses and eventually take over their kingdom

print("\n*You wake up in the ground. You do not remember how you got there, or why there is a cat next to you. You only remember your name. All of a sudden, a man in a horse-drawn carriage appears coming down the road.*")

name = input("\nJohn: Welcome- erm... Well, I suppose I don't know your name yet traveller. What should I call you?\n")
nameConfirm = input(f"{name}? Am I saying that right?\n")
nameConfirm = nameConfirm.upper()
while nameConfirm != "YES" and nameConfirm != "NO":
    nameConfirm = input("I'm sorry, was that a yes or a no?\n")
if nameConfirm == "NO":
    name = input("I'm sorry, for the mistake, what should I call you then?\n")
else:
    name = name

print(f"Well then {name}, let me show you around!")
print("\nI see your cat has already chosen you. That is a lucky thing you know. In this kingdom, cats can choose you as their owner, but this is something that can take a lifetime to occur. You are lucky yours chose you so early in your life. I reckon you don't know how you got here. That is very common in this place, though we do not know why. In the village, we try not to challenge the existing order because the consequences here are deadly. Though there are some scary beings out there in this forest, they only come out at night. The real worry us villagers have is the king. He is vile and ruthless, and does not like newcomers. You should really get used to the powers of your cat. Wait, did I mention your cat has powers? Have you even chosen the powers yet? No? Well, hold your hand above the cat's head, yes like that, and choose its abilities.")

charChoice = input("\nChoose what abilities your cat has. Press ENTER to cycle through them. Enter the name of the cat you want underneath its description.")
charChoice = "empty"
while charChoice =="empty":
    print("Hulkat\nAbility: Strength\nWeaknesses: Poison Attacks, Speed Attacks")
    charChoice = input()
    charChoice = charChoice.upper()
    if charChoice == "HULKAT":
        break
    else:
        charChoice = "empty"
    print("Speedster\nAbility: Speed\nWeaknesses: Ice Attacks, Fire Attacks")
    charChoice =  input()
    charChoice = charChoice.upper()
    if charChoice == "SPEEDSTER":
        break
    else:
        charChoice = "empty"
    print("")


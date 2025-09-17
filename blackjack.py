import random
import time
import os
z = os.get_terminal_size()[0]
os.system('clear')
def get_name_of_card(suit,number):
    if number == 1:
        return f"Ace of {suit}"
    elif number == 11:
        return f"Jack of {suit}"
    elif number == 12:
        return f"Queen of {suit}"
    elif number == 13:
        return f"King of {suit}"
    else:
        return f"{number} of {suit}"

def get_card_value(card):
    if card[:3].lower() == "ace":
        return -1
    elif card[:4] == "Jack" or card[:4] == "King" or card[:5] == "Queen":
        return 10
    elif card[1] == " ":
        return int(card[0])
    else:
        return int(card[:2])
    
def deal_card():
    x=random.choice(deckList)
    deckList.remove(x)
    return x

def is_vowel(card):
    if card[0].lower() == "a":
        return "n "
    else:
        return " "

def card_display(hand,phase):
    numCards = len(hand)
    print("-------  " * numCards)
    if phase == "open":
        for i in range(numCards):
            print(f"|   {str(get_value_display(hand[i],"top"))}|  ", end="")
        print("\n"+"|     |  " * numCards)
        for i in range(numCards):
            print(f"|{str(get_value_display(hand[i],"bottom"))}   |  ", end="")
    elif phase=="hidden":
        for i in range(numCards):
            if i == 0:
                print("|/////|  ",end="")
            else:
                print(f"|   {str(get_value_display(hand[i],"top"))}|  ", end="")
        print("\n"+"|/////|  " + "|     |  " * (numCards-1))
        for i in range(numCards):
            if i == 0:
                print("|/////|  ",end="")
            else:
                print(f"|{str(get_value_display(hand[i],"bottom"))}   |  ", end="")

    print("\n"+"-------  " * numCards)

def get_value_display(card,side):
    if side == "top":
        if card[:3].lower() == "ace":
            return " A"
        elif card[:4] == "Jack":
            return " J"
        elif card[:4] == "King":
            return " K"
        elif card[:5] == "Queen":
            return " Q"
        elif card[1] == " ":
            return f" {card[0]}"
        else:
            return int(card[:2])
    if side == "bottom":
        if card[:3].lower() == "ace":
            return "A "
        elif card[:4] == "Jack":
            return "J "
        elif card[:4] == "King":
            return "K "
        elif card[:5] == "Queen":
            return "Q "
        elif card[1] == " ":
            return f"{card[0]} "
        else:
            return int(card[:2])
print("Welcome to blackjack".center(z))
while True:
    print("How many decks do you wanna use?".center(z))
    numDecks = input()
    print("")
    try:
        numDecks = int(numDecks)
        break
    except (NameError,ValueError):
        print("Invalid number. Please enter an integer.".center(z))
        print("Press ENTER to try again".center(z))
        input()
        os.system('clear')
os.system('clear')
suits = ["Hearts","Spades","Clubs","Diamonds"]
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13]

deckList = []
for i in range(numDecks):
    for suit in suits:
        for num in numbers:
            deckList.append(get_name_of_card(suit,num))

playerCards = []
dealerCards = []
playerCards.append(deal_card())
dealerCards.append(deal_card())
playerCards.append(deal_card())
dealerCards.append(deal_card())
print("You are dealt a" + is_vowel(playerCards[0]) + playerCards[0])
print("")
time.sleep(1.7)
print("The dealer deals himself a card face down")
print("")
time.sleep(1.7)
print("You are dealt a" + is_vowel(playerCards[1]) + playerCards[1])
print("")
time.sleep(1.7)
print("The dealer deals himself a" + is_vowel(dealerCards[1]) + dealerCards[1])
print("")

os.system('clear')
print("Your cards:\n")
card_display(playerCards,"open")
print("\nDealer's Cards:")
card_display(dealerCards,"hidden")

print("")
print("What would you like to do?".center(z))
print("HIT   |   STAND   |   DOUBLE")

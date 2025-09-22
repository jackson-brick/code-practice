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

def get_card_value(card,score):
    if card[:3].lower() == "ace":
        if score+11 <= 21:
            return 11
        else:
            return 1
    elif card[:4] == "Jack" or card[:4] == "King" or card[:5] == "Queen":
        return 10
    elif card[1] == " ":
        return int(card[0])
    else:
        return int(card[:2])

def two_aces(card1,card2):
    if card1[:3].lower() == "ace":
        if card2[:3].lower() == "ace":
            return True
    return False

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
    topEdge = "-------  " * numCards
    topLine = ""
    midLine = ""
    bottomLine = ""
    bottomEdge = "-------  " * numCards
    print(topEdge.center(z))
    if phase == "open":
        for i in range(numCards):
            topLine += f"|   {str(get_value_display(hand[i],"top"))}|  "
        print(topLine.center(z))
        midLine = "|     |  " * numCards
        print(midLine.center(z))
        for i in range(numCards):
            bottomLine += f"|{str(get_value_display(hand[i],"bottom"))}   |  "
        print(bottomLine.center(z))
    elif phase=="hidden":
        for i in range(numCards):
            if i == 0:
                topLine += "|/////|  "
            else:
                topLine += f"|   {str(get_value_display(hand[i],"top"))}|  "
        print(topLine.center(z))
        midLine = "|/////|  " + "|     |  " * (numCards-1)
        print(midLine.center(z))
        for i in range(numCards):
            if i == 0:
                bottomLine += "|/////|  "
            else:
                bottomLine += f"|{str(get_value_display(hand[i],"bottom"))}   |  "
        print(bottomLine.center(z))

    print(bottomEdge.center(z))

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

def calculate_score(hand):
    aceCount=0
    score = 0
    for i in hand:
        if i[:3].lower() == "ace":
            aceCount +=1
        else:
            score += get_card_value(i)

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
playerScore = 0
dealerCards = []
dealerScore = 0
random.shuffle(deckList)
playerCards.append(deal_card())
dealerCards.append(deal_card())
playerCards.append(deal_card())
dealerCards.append(deal_card())
playerScore += get_card_value(playerCards[0],playerScore)
playerScore += get_card_value(playerCards[1],playerScore)
dealerScore += get_card_value(dealerCards[0],playerScore)
dealerScore += get_card_value(dealerCards[1],playerScore)
print(f"You are dealt a{is_vowel(playerCards[0])}{playerCards[0]}".center(z))
print("")
time.sleep(1.7)
print("The dealer deals himself a card face down".center(z))
print("")
time.sleep(1.7)
print(f"You are dealt a{is_vowel(playerCards[1])}{playerCards[1]}".center(z))
print("")
time.sleep(1.7)
print(f"The dealer deals himself a{is_vowel(dealerCards[1])}{dealerCards[1]}".center(z))
print("")
time.sleep(1.7)
print("Press ENTER to start the game".center(z))
input()

result = ""
while result == "":
    os.system('clear')
    print(f"Your cards:        Your score: {playerScore}".center(z))
    print("")
    card_display(playerCards,"open")
    print("")
    print(f"Dealer's Cards:".center(z))
    card_display(dealerCards,"hidden")

    print("")
    print("What would you like to do?".center(z))
    if get_card_value(playerCards[0],0) == get_card_value(playerCards[1],0) or two_aces(playerCards[0],playerCards[1]):
        print("HIT   |   STAND   |   DOUBLE   |   SURRENDER   |   SPLIT".center(z))
    else:
        print("HIT   |   STAND   |   DOUBLE   |   SURRENDER".center(z))
    action = input().lower()
    if action == "hit":
        playerCards.append(deal_card())
        playerScore += get_card_value(playerCards[-1],playerScore)
    elif action == "stand":
        print("stand")
    elif action == "double":
        print("double down")
    elif action == "split" and get_card_value(playerCards[0],0) == get_card_value(playerCards[1],0) or action == "split" and two_aces(playerCards[0],playerCards[1]):
        print("split")

    if playerScore > 21:
        for i in playerCards:
            if i[:3].lower() == "ace":
                print("FINSIH LATER")
        result = "dealerWin"
    if dealerScore > 21:
        result = "playerWin"

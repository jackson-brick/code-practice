import random
import os
import time
from colorama import Fore,Style
z = os.get_terminal_size()[0]
os.system('clear')
animations = True
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
        return 10

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
    print(topEdge.strip().center(z))
    if phase == "open":
        for i in range(numCards):
            topLine += f"|   {str(get_value_display(hand[i],"top"))}|  "
        print(topLine.strip().center(z))
        midLine = "|     |  " * numCards
        print(midLine.strip().center(z))
        for i in range(numCards):
            bottomLine += f"|{str(get_value_display(hand[i],"bottom"))}   |  "
        print(bottomLine.strip().center(z))
    elif phase=="hidden":
        for i in range(numCards):
            if i == 1:
                topLine += "|/////|  "
            else:
                topLine += f"|   {str(get_value_display(hand[i],"top"))}|  "
        print(topLine.strip().center(z))
        midLine = "|     |  " + "|/////|  " * (numCards-1)
        print(midLine.strip().center(z))
        for i in range(numCards):
            if i == 1:
                bottomLine += "|/////|  "
            else:
                bottomLine += f"|{str(get_value_display(hand[i],"bottom"))}   |  "
        print(bottomLine.strip().center(z))

    print(bottomEdge.strip().center(z))

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
        if get_card_value(i) == -1:
            aceCount+=1
        else:
            score += get_card_value(i)
    if aceCount >0:
        score += aceCount
        if score + 10<=21:
            score += 10

    return score

def check_card_animation(dealerHand):
    os.system('clear')
    print("_"*z)
    card_display(dealerHand,"hidden")
    print("The dealer is checking his hidden card for a blackjack".center(z))
    time.sleep(0.3)
    os.system('clear')
    print("_"*int(((z/2)+1)) + "-------" + "_"*int(((z/2)-8)))
    print("-------  |/////|".center(z))
    print(f"|   {str(get_value_display(dealerCards[0],"top"))}|  |/////|".center(z))
    print("|     |  |/////|".center(z))
    print(f"|{str(get_value_display(dealerCards[0],"bottom"))}   |  -------".center(z))
    print("-------         ".center(z))
    print("The dealer is checking his hidden card for a blackjack".center(z))
    time.sleep(0.3)
    os.system('clear')
    print("_"*int(((z/2)+1)) + "|/////|" + "_"*int(((z/2)-8)))
    print("-------  |/////|".center(z))
    print(f"|   {str(get_value_display(dealerCards[0],"top"))}|  |/////|".center(z))
    print("|     |  -------".center(z))
    print(f"|{str(get_value_display(dealerCards[0],"bottom"))}   |         ".center(z))
    print("-------         ".center(z))
    print("The dealer is checking his hidden card for a blackjack".center(z))
    time.sleep(0.3)
    os.system('clear')
    print("_"*int(((z/2)+1)) + "|/////|" + "_"*int(((z/2)-8)))
    print("-------  |/////|".center(z))
    print(f"|   {str(get_value_display(dealerCards[0],"top"))}|  -------".center(z))
    print("|     |         ".center(z))
    print(f"|{str(get_value_display(dealerCards[0],"bottom"))}   |         ".center(z))
    print("-------         ".center(z))
    print("The dealer is checking his hidden card for a blackjack".center(z))
    time.sleep(0.3)
    os.system('clear')
    print("_"*int(((z/2)+1)) + "|/////|" + "_"*int(((z/2)-8)))
    print("-------  -------".center(z))
    print(f"|   {str(get_value_display(dealerCards[0],"top"))}|         ".center(z))
    print("|     |         ".center(z))
    print(f"|{str(get_value_display(dealerCards[0],"bottom"))}   |         ".center(z))
    print("-------         ".center(z))
    print("The dealer is checking his hidden card for a blackjack".center(z))
    time.sleep(0.3)
    os.system('clear')
    print("_"*int(((z/2)+1)) + "-------" + "_"*int(((z/2)-8)))
    print("-------         ".center(z))
    print(f"|   {str(get_value_display(dealerCards[0],"top"))}|         ".center(z))
    print("|     |         ".center(z))
    print(f"|{str(get_value_display(dealerCards[0],"bottom"))}   |         ".center(z))
    print("-------         ".center(z))
    print("The dealer is checking his hidden card for a blackjack".center(z))
    time.sleep(0.3)
    os.system('clear')
    print("_"*z)
    print("-------         ".center(z))
    print(f"|   {str(get_value_display(dealerCards[0],"top"))}|         ".center(z))
    print("|     |         ".center(z))
    print(f"|{str(get_value_display(dealerCards[0],"bottom"))}   |         ".center(z))
    print("-------         ".center(z))
    print("The dealer is checking his hidden card for a blackjack".center(z))
    time.sleep(2)
    os.system('clear')
    print("_"*z)
    print("-------         ".center(z))
    print(f"|   {str(get_value_display(dealerCards[0],"top"))}|         ".center(z))
    print("|     |         ".center(z))
    print(f"|{str(get_value_display(dealerCards[0],"bottom"))}   |         ".center(z))
    print("-------         ".center(z))
    print("The dealer is checking his hidden card for a blackjack".center(z))
    time.sleep(0.3)
    os.system('clear')
    print("_"*int(((z/2)+1)) + "-------" + "_"*int(((z/2)-8)))
    print("-------         ".center(z))
    print(f"|   {str(get_value_display(dealerCards[0],"top"))}|         ".center(z))
    print("|     |         ".center(z))
    print(f"|{str(get_value_display(dealerCards[0],"bottom"))}   |         ".center(z))
    print("-------         ".center(z))
    print("The dealer is checking his hidden card for a blackjack".center(z))
    time.sleep(0.3)
    os.system('clear')
    print("_"*int(((z/2)+1)) + "|/////|" + "_"*int(((z/2)-8)))
    print("-------  -------".center(z))
    print(f"|   {str(get_value_display(dealerCards[0],"top"))}|         ".center(z))
    print("|     |         ".center(z))
    print(f"|{str(get_value_display(dealerCards[0],"bottom"))}   |         ".center(z))
    print("-------         ".center(z))
    print("The dealer is checking his hidden card for a blackjack".center(z))
    time.sleep(0.3)
    os.system('clear')
    print("_"*int(((z/2)+1)) + "|/////|" + "_"*int(((z/2)-8)))
    print("-------  |/////|".center(z))
    print(f"|   {str(get_value_display(dealerCards[0],"top"))}|  -------".center(z))
    print("|     |         ".center(z))
    print(f"|{str(get_value_display(dealerCards[0],"bottom"))}   |         ".center(z))
    print("-------         ".center(z))
    print("The dealer is checking his hidden card for a blackjack".center(z))
    time.sleep(0.3)
    os.system('clear')
    print("_"*int(((z/2)+1)) + "|/////|" + "_"*int(((z/2)-8)))
    print("-------  |/////|".center(z))
    print(f"|   {str(get_value_display(dealerCards[0],"top"))}|  |/////|".center(z))
    print("|     |  -------".center(z))
    print(f"|{str(get_value_display(dealerCards[0],"bottom"))}   |         ".center(z))
    print("-------         ".center(z))
    print("The dealer is checking his hidden card for a blackjack".center(z))
    time.sleep(0.3)
    os.system('clear')
    print("_"*int(((z/2)+1)) + "-------" + "_"*int(((z/2)-8)))
    print("-------  |/////|".center(z))
    print(f"|   {str(get_value_display(dealerCards[0],"top"))}|  |/////|".center(z))
    print("|     |  |/////|".center(z))
    print(f"|{str(get_value_display(dealerCards[0],"bottom"))}   |  -------".center(z))
    print("-------         ".center(z))
    print("The dealer is checking his hidden card for a blackjack".center(z))
    time.sleep(0.3)
    os.system('clear')
    print("_"*z)
    card_display(dealerHand,"hidden")
    print("The dealer is checking his hidden card for a blackjack".center(z))

def hidden_flip_animation():
    print("_"*z)
    card_display(dealerCards,"hidden")
    print(f"Dealer's Cards".center(z))
    time.sleep(0.3)
    os.system('clear')
    print("_"*z)
    print("-------   ----- ".center(z))
    print(f"|   {str(get_value_display(dealerCards[0],"top"))}|   |///| ".center(z))
    print("|     |   |///| ".center(z))
    print(f"|{str(get_value_display(dealerCards[0],"bottom"))}   |   |///| ".center(z))
    print("-------   ----- ".center(z))
    time.sleep(0.3)
    os.system('clear')
    print("_"*z)
    print("-------    ---  ".center(z))
    print(f"|   {str(get_value_display(dealerCards[0],"top"))}|    |/|  ".center(z))
    print("|     |    |/|  ".center(z))
    print(f"|{str(get_value_display(dealerCards[0],"bottom"))}   |    |/|  ".center(z))
    print("-------    ---  ".center(z))
    time.sleep(0.3)
    os.system('clear')
    print("_"*z)
    print("-------     -   ".center(z))
    print(f"|   {str(get_value_display(dealerCards[0],"top"))}|     |   ".center(z))
    print("|     |     |   ".center(z))
    print(f"|{str(get_value_display(dealerCards[0],"bottom"))}   |     |   ".center(z))
    print("-------     -   ".center(z))
    time.sleep(0.3)
    os.system('clear')
    print("_"*z)
    print("-------    ---  ".center(z))
    print(f"|   {str(get_value_display(dealerCards[0],"top"))}|    |{(str(get_value_display(dealerCards[1],"bottom")))[0]}|  ".center(z))
    print("|     |    | |  ".center(z))
    print(f"|{str(get_value_display(dealerCards[0],"bottom"))}   |    |{(str(get_value_display(dealerCards[1],"bottom")))[0]}|  ".center(z))
    print("-------    ---  ".center(z))
    time.sleep(0.3)
    os.system('clear')
    print("_"*z)
    print("-------   ----- ".center(z))
    print(f"|   {str(get_value_display(dealerCards[0],"top"))}|   | {str(get_value_display(dealerCards[1],"top"))}| ".center(z))
    print("|     |   |   | ".center(z))
    print(f"|{str(get_value_display(dealerCards[0],"bottom"))}   |   |{str(get_value_display(dealerCards[1],"bottom"))} | ".center(z))
    print("-------   ----- ".center(z))
    time.sleep(0.3)
    os.system('clear')
    print("_"*z)
    print("-------  -------".center(z))
    print(f"|   {str(get_value_display(dealerCards[0],"top"))}|  |   {str(get_value_display(dealerCards[1],"top"))}|".center(z))
    print("|     |  |     |".center(z))
    print(f"|{str(get_value_display(dealerCards[0],"bottom"))}   |  |{str(get_value_display(dealerCards[1],"bottom"))}   |".center(z))
    print("-------  -------".center(z))
    time.sleep(0.3)
    os.system('clear')
    print("_"*z)
    card_display(dealerCards,"open")
    time.sleep(0.3)
    os.system('clear')

    
    

print("Welcome to blackjack".center(z))
while True:
    print("How many decks do you wanna use? (1-10)".center(z))
    numDecks = input()
    print("")
    try:
        numDecks = int(numDecks)
        if numDecks >10 or numDecks <1:
            print("Choose a valid number of decks (1-10)".center(z))
            print("Press ENTER to try again".center(z))
            input()
            os.system('clear')
        else:
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
balance = 1000.0
while balance >0:
    while True:
        os.system('clear')
        print("How much will you bet on this hand?".center(z))
        print(f"Your balance: ${balance}".center(z))
        bet = input()
        try:
            bet = float(bet)
            if bet > 0 and bet <= balance:
                bet = round(bet,2)
                break
            else:
                print("Make a bet within your balance range. Press ENTER to try again.".center(z))
                input()
        except:
            print("Please enter a valid number for a bet. Press ENTER to try again.".center(z))
            input()


    playerCards = []

    dealerCards = []
    random.shuffle(deckList)
    playerCards.append(deal_card())
    dealerCards.append(deal_card())
    playerCards.append(deal_card())
    dealerCards.append(deal_card())
    os.system('clear')
    print(f"You are dealt a{is_vowel(playerCards[0])}{playerCards[0]}".center(z))
    print("")
    print(f"The dealer deals himself a{is_vowel(dealerCards[0])}{dealerCards[0]}".center(z))
    print("")
    print(f"You are dealt a{is_vowel(playerCards[1])}{playerCards[1]}".center(z))
    print("")
    print("The dealer deals himself a card face down".center(z))
    print("")
    print("Press ENTER to start the game".center(z))
    input()

    result = ""
    gameStart = True
    playerTurn = True
    playerDoubled = 0
    while result == "":
        playerScore = calculate_score(playerCards)
        dealerScore = calculate_score(dealerCards)
        if playerScore > 21:
            #Player score will only increase if player hits
            result = "playerBust"
            
        if dealerScore > 21:
            #Dealer score only increases if the player stands
            result = "dealerBust"
            
        if playerScore > 21 and playerDoubled == 1:
            result = "playerDoubleBust"
        if playerScore == 21 and gameStart:
            os.system('clear')
            print("You got a BLACKJACK".center(z))
            print("Let's see what the dealer has... Press ENTER to continue".center(z))
            input()
            hidden_flip_animation()
            if playerScore == dealerScore:
                result = "push"
            else:
                result = "playerNaturalBlackjackWin"
            playerTurn = False
        elif playerScore==21:
            os.system('clear')
            hidden_flip_animation()
            playerTurn = False
        if not gameStart and not playerTurn and dealerScore >=17:
            if playerScore > dealerScore:
                result = "playerWin"
            elif playerScore < dealerScore:
                result = "dealerWin"
            else:
                result = "push"
            
        if gameStart and result == "":
            gameStart = False
            if get_card_value(dealerCards[0]) == 10 or get_card_value(dealerCards[0]) == -1:    
                
                os.system('clear')
                if animations:
                    check_card_animation(dealerCards)
                else:
                    print("The dealer is checking his hidden card for a blackjack".center(z))
                    time.sleep(0.5)
                
                if dealerScore == 21:
                    #This ending will flip the dealer's card and show their blackjack
                    result = "dealerGameStartBlackjack"
                    playerTurn = False
                else:
                    print("The dealer does not have a blackjack".center(z))
                    print("Press ENTER to continue".center(z))
                    input()
        os.system('clear')
        print("_"*z)
        if playerTurn and playerDoubled == 0:
            card_display(dealerCards,"hidden")
            print(f"Dealer's Cards".center(z))
        elif not playerTurn and playerDoubled == 0:
            card_display(dealerCards,"open")
            print(f"Dealer's Cards     |    Dealer's score: {dealerScore}".center(z))
            if result == "dealerGameStartBlackjack":
                break
        elif not playerTurn and playerDoubled == 1:
            card_display(dealerCards,"hidden")
            print(f"Dealer's Cards".center(z))
        elif not playerTurn and playerDoubled == 2:
            card_display(dealerCards,"open")
            print(f"Dealer's Cards     |    Dealer's score: {dealerScore}".center(z))

        print("\n")
        print(f"Your balance: ${balance}    |    Your current bet: ${bet}     |    Your score: {playerScore}".center(z))
        card_display(playerCards,"open")
        print(f"Your cards".center(z))
        print("")
        if result == "dealerBust":
            break
        if playerDoubled == 0:
            if playerTurn:
                print("What would you like to do?".center(z))
                if get_card_value(playerCards[0]) == get_card_value(playerCards[1]) and result == "":
                    print("HIT   |   STAND   |   DOUBLE   |   SURRENDER   |   SPLIT".center(z))
                else:
                    print("HIT   |   STAND   |   DOUBLE   |   SURRENDER".center(z))
            if result == "" and playerTurn:
                action = input().lower()
            else:
                action = ""
            if playerTurn:
                if action == "hit":
                    playerCards.append(deal_card())
                elif action == "stand":
                    os.system('clear')
                    hidden_flip_animation()
                    playerTurn = False
                elif action == "double":
                    if bet*2 <= balance:
                        bet *= 2
                        print("")
                        print(f"You doubled your bet to ${bet}".center(z))
                        time.sleep(2)
                        print(f"The dealer will deal you one more card".center(z))
                        print("Press ENTER to continue".center(z))
                        input()
                        playerCards.append(deal_card())
                        playerTurn = False
                        playerDoubled += 1
                elif action == "split" and get_card_value(playerCards[0]) == get_card_value(playerCards[1]):
                    print("split")
            elif result == "":
                print("")
                print(Fore.RED + Style.BRIGHT + "Dealer is drawing...".center(z))
                print(Style.RESET_ALL)
                print("Press ENTER to continue".center(z))
                input()
                dealerCards.append(deal_card())
        elif playerDoubled == 1:
            if result == "playerDoubleBust":
                result = "playerBust"
                break
            playerDoubled += 1
            print("Press ENTER to continue".center(z))
            input()
            os.system('clear')
            hidden_flip_animation()
        else:
            if result == "":
                print("")
                print(Fore.RED + Style.BRIGHT + "Dealer is drawing...".center(z))
                print(Style.RESET_ALL)
                print("Press ENTER to continue".center(z))
                input()
                dealerCards.append(deal_card())

    if result == "playerBust":
        #dealer wins
        print("")
        print(Fore.RED + Style.BRIGHT + "DEALER WINS".center(z))
        balance -= bet
        print(Style.RESET_ALL)
        print("Press ENTER to play again".center(z))
        input()
    elif result == "dealerBust":
        #player wins
        print("")
        print(Fore.GREEN + Style.BRIGHT + "YOU WIN".center(z))
        balance += bet
        print(Style.RESET_ALL)
        print("Press ENTER to play again".center(z))
        input()
    elif result == "dealerGameStartBlackjack":
        if (get_card_value(playerCards[0])+get_card_value(playerCards[1])) != 21:
            #dealer wins
            print("")
            print(Fore.RED + Style.BRIGHT + "DEALER WINS".center(z))
            balance -= bet
            print(Style.RESET_ALL)
            print("Press ENTER to play again".center(z))
            input()
        else:
            #tie
            print("")
            print(Fore.YELLOW + Style.BRIGHT + "IT'S A TIE".center(z))
            print(Style.RESET_ALL)
            print("Press ENTER to play again".center(z))
            input()
    elif result == "dealerWin":
        print("")
        print(Fore.RED + Style.BRIGHT + "DEALER WINS".center(z))
        balance -= bet
        print(Style.RESET_ALL)
        print("Press ENTER to play again".center(z))
        input()
    elif result == "playerWin":
        print("")
        print(Fore.GREEN + Style.BRIGHT + "YOU WIN".center(z))
        balance += bet
        print(Style.RESET_ALL)
        print("Press ENTER to play again".center(z))
        input()
    elif result == "push":
        print("")
        print(Fore.YELLOW + Style.BRIGHT + "IT'S A TIE".center(z))
        print(Style.RESET_ALL)
        print("Press ENTER to play again".center(z))
        input()
    elif result == "playerNaturalBlackjackWin":
        print("")
        print(Fore.GREEN + Style.BRIGHT + "You win with a natural blackjack! You get 1.5x your bet!".center(z))
        balance += (1.5*bet)
        print(Style.RESET_ALL)
        print("Press ENTER to play again".center(z))
        input()
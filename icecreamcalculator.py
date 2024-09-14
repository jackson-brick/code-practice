
#Write a code for an ice cream shop taking someone's order and giving them their price at the end


print("+-+-+-+-+-+-+-+-+--+-+-+-+-+-+-+-+-+")
print("+                                  +")
print("+        The Ice Cream Shop        +")
print("+                                  +")
print("+              Welcome             +")
print("+                                  +")
print("+-+-+-+-+-+-+-+-+--+-+-+-+-+-+-+-+-+")

print("\n")

container = input("What kind of ice cream container would you like: cup or cone? ")
while container != "cup" and container != "cone":
    print("Invalid respone! Please try again: ")
    container = input("What kind of ice cream container would you like: cup or cone? ")
if container == "cup":
    container = 2
elif container == "cone":
    container = 3.5
scoops = input("How many scoops would you like (You may have up to four) (*You must write out number as a word*)? ")
while scoops != "one" and scoops != "two" and scoops != "three" and scoops != "four":
    print("Invalid response! Please try again: ")
    scoops = input("How many scoops would you like (You may have up to four) (*You must write out number as a word*)? ")
if scoops == "one":
    scoops = 1
elif scoops == "two":
    scoops = 1.5
elif scoops == "three":
    scoops = 2
elif scoops == "four":
    scoops = 2.5
flake = input("Would you like to add coconut flakes? ")
while flake != "yes" and flake != "no":
    print("Invalid response! Please try again: ")
    flake = input("Would you like to add coconut flakes? ")
if flake == "yes":
    flake = 1.5
elif flake == "no":
    flake = 0
sprinkle = input("Would you like chocolate sprinkles? ")
while sprinkle != "yes" and sprinkle != "no":
    print("Invalid response! Please try again: ")
    sprinkle = input("Would you like chocolate sprinkles? ")
if sprinkle == "yes":
    sprinkle = 1
elif sprinkle == "no":
    sprinkle = 0
fruit = input("Would you like any fruit toppings? ")
while fruit != "yes" and fruit != "no":
    print("Invalid response! Please try again: ")
    fruit = input("Would you like any fruit toppings? ")
if fruit == "yes":
    topping = input("Would you like strawberries (50c) or bananas ($1)? ")
    while topping != "strawberries" and topping != "bananas":
        print("Invalid response! Please try again: ")
        topping = input("Would you like strawberries or bananas? ")
    if topping == "strawberries":
        topping = 0.5
    elif topping == "bananas":
        topping = 1
elif fruit == "no":
    topping = 0


total = float(container) + float(scoops) + float(flake) + float(sprinkle) + float(topping)

print(f"Your total is ${total}!")

    






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
scoops = input("How many scoops would you like (You may have up to four)? ")
while scoops != "1" and scoops != "2" and scoops != "3" and scoops != "4":
    print("Invalid response! Please try again: ")
    scoops = input("How many scoops would you like (You may have up to four)? ")
if scoops == "1":
    scoops = 1
elif scoops == "2":
    scoops = 1.5
elif scoops == "3":
    scoops = 2
elif scoops == "4":
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
    topping = input("Would you like strawberries (50c), bananas ($1), or both ($1.50)? ")
    while topping != "strawberries" and topping != "bananas":
        print("Invalid response! Please try again: ")
        topping = input("Would you like strawberries or bananas? ")
    if topping == "strawberries":
        topping = 0.5
    elif topping == "bananas":
        topping = 1
    elif topping == "both":
        topping = 1.5
elif fruit == "no":
    topping = 0


total = float(container) + float(scoops) + float(flake) + float(sprinkle) + float(topping)
intTotal = int(total)
cents = int((total - intTotal) * 100)
if cents != 0:
    print(f"Your total is ${intTotal}.{cents}!")
else:
    print(f"Your total is ${intTotal}.00!")

    





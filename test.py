import os
import time
z = os.get_terminal_size()
z=z[0]

print("I will be doing all the prompts!".center(z))
input()
os.system('clear')
print("Prompt 1: Person Class".center(z))
class Person:
    __firstName = None
    __lastName = None
    def __init__(self,firstName,lastName):
        self.__firstName = firstName
        self.__lastName = lastName
    def getFirstName(self):
        return self.__firstName
    def setFirstName(self,name):
        self.__firstName = name
    def getLastName(self):
        return self.__lastName
    def setLastName(self,name):
        self.__lastName = name
        
person1 = Person("Jackson","Brick")
person2 = Person("Benji","Gonzalez")
print(f"Person 1's name is {person1.getFirstName()} {person1.getLastName()}".center(z))
print(f"Person 2's name is {person2.getFirstName()} {person2.getLastName()}".center(z))
input()
os.system('clear')
print("Change person 1's first name:".center(z))
a = input()
person1.setFirstName(a)
print(f"Person 1's name is now {person1.getFirstName()} {person1.getLastName()}".center(z))
print("Change person 1's last name:".center(z))
a = input()
person1.setLastName(a)
print(f"Person 1's name is now {person1.getFirstName()} {person1.getLastName()}".center(z))
print("Change person 2's first name:".center(z))
a = input()
person2.setFirstName(a)
print(f"Person 2's name is now {person2.getFirstName()} {person2.getLastName()}".center(z))
print("Change person 2's last name:".center(z))
a = input()
person2.setLastName(a)
print(f"Person 2's name is now {person2.getFirstName()} {person2.getLastName()}".center(z))
print("Press ENTER to continue".center(z))
input()
os.system('clear')
print("Prompt 2: Product Class".center(z))

class Product:
    __name = None
    __price = None
    def __init__(self,name,price):
        self.__name = name
        self.__price = price
    def getName(self):
        return self.__name
    def setName(self,name):
        self.__name = name
    def getPrice(self):
        return self.__price
    def setPrice(self,price):
        if price.isdigit():
            self.__price = price
        else:
            os.system('clear')
            print("You must enter a number.".center(z))
product1 = Product("Milk",100)
product2 = Product("Chocolate bar",50)
print(f"{product1.getName()} costs ${product1.getPrice()}".center(z))
print(f"{product2.getName()} costs ${product2.getPrice()}".center(z))
print("Change the name of product 1:".center(z))
a = input()
product1.setName(a)
print(f"{product1.getName()} costs ${product1.getPrice()}".center(z))
while True:
    print("Change the price of product 1:".center(z))
    a = input()
    product1.setPrice(a)
print(f"{product1.getName()} costs ${product1.getPrice()}".center(z))
print("Change the name of product 2:".center(z))
a = input()
product2.setName(a)
print(f"{product2.getName()} costs ${product2.getPrice()}".center(z))
print("Change the price of product 2:".center(z))
a = input()
product2.setPrice(a)
print(f"{product2.getName()} costs ${product2.getPrice()}".center(z))

print("Press ENTER to continue".center(z))
input()
os.system('clear')
print("Prompt 3: City Class".center(z))
class City:
    __name = None
    __population = None
    def __init__(self,name,population):
        self.__name = name
        self.__population = population
    def getName(self):
        return self.__name
    def setName(self,name):
        self.__name = name
    def getPop(self):
        return self.__population
    def setPop(self,population):
        if population.isdigit():
            self.__population = population
            if population == "1":
                print("You are the last one in your city!")
                
city1 = City("Jackson Junction","200000")
print(f"{city1.getName()} : {city1.getPop()}".center(z))
print("Name your city:".center(z))
name = input()
while True:
    print("How many people are in your city?".center(z))
    pop = input()
    if pop.isdigit():
        break
    else:
        print("Enter a digit.".center(z))
city2 = City(name,pop)
print(f"{city2.getName()} has {city2.getPop()} citizens.".center(z))
print("Your city is undergoing changes! You must rename it! What will you name it? ".center(z))
name = input()
city2.setName(name)
while True:
    print("Your city is undergoing changes! How many people are left in your city? ".center(z))
    pop = input()
    if pop.isdigit():
        city2.setPop(pop)
        break
print(f"{city2.getName()} has {city2.getPop()} citizens.")

print("Press ENTER to continue".center(z))
input()
os.system('clear')
print("Prompt 4: Phone Class".center(z))
class Phone:
    __brand = None
    __model = None
    def __init__(self,brand,model):
        self.__brand = brand
        self.__model = model
    def getBrand(self):
        return self.__brand
    def getModel(self):
        return self.__model
    def setBrand(self,brand):
        self.__brand = brand
    def setModel(self,model):
        self.__model = model
phone = Phone("Apple","iPhone 15 Pro Max")
print(f"I have an {phone.getBrand()} {phone.getModel()}.".center(z))
print("What brand phone do you have?".center(z))
brand = input()
print(f"What model is this {brand} phone of yours? ".center(z))
model = input()
phone.setBrand(brand)
phone.setModel(model)
print(f"You have a {phone.getBrand()} {phone.getModel()}.".center(z))
print("Press ENTER to continue".center(z))
input()
os.system('clear')
print("Prompt 5: Pet Class".center(z))
class Pet:
    __name = None
    __species = None
    def __init__(self,name,species):
        self.__name = name
        self.__species = species
    def getName(self):
        return self.__name
    def getSpecies(self):
        return self.__species
    def setName(self,name):
        self.__name = name
    def setSpecies(self,species):
        self.__species = species
pet1 = Pet("Apple","dog")
pet2 = Pet("Butter","cat")
print(f"{pet1.getName()} is a {pet1.getSpecies()}!".center(z))
print(f"{pet2.getName()} is a {pet2.getSpecies()}!".center(z))
print("Wait-- there was an error in the second entry! Could you tell me, what species should the second pet be? ".center(z))
species = input()
pet2.setSpecies(species)
print(f"Great! Now what should we name this {species}? ".center(z))
name = input()
pet2.setName(name)
print(f"{pet1.getName()} is a {pet1.getSpecies()}!".center(z))
print(f"{pet2.getName()} is a {pet2.getSpecies()}!".center(z))

print("Press ENTER to continue".center(z))
input()
os.system('clear')
print("Prompt 6: GymMember Class".center(z))
class GymMember:
    __name = None
    __membershipType = None
    __checkIns = 0
    def __init__(self,name,membershipType,checkIns):
        self.__name = name
        self.__membershipType = membershipType
        self.__checkIns = int(checkIns)
    def display(self):
        print(f"{self.__name} : {self.__membershipType}".center(z))
        print(f"Check-Ins : {self.__checkIns}".center(z))
    def checkIn(self):
        self.__checkIns += 1
    def upOrDowngrade(self):
        if self.__membershipType == "Basic":
            self.__membershipType = "Premium"
        else:
            while True:
                os.system('clear')
                print("Are you sure you would like to downgrade? ".center(z))
                sure = input()
                if sure.lower().strip() == "yes":
                    self.__membershipType = "Basic"
                    break
                elif sure.lower().strip() == "no":
                    break
print("What is your first and last name? ".center(z))
name = input()
gymMember = GymMember(name,"Basic",0)
while True:
    os.system('clear')
    gymMember.display()
    print("To change your membership, type MEMBERSHIP".center(z))
    print("To check-in, type CHECK".center(z))
    print("When done working out, type DONE".center(z))
    gym = input()
    if gym.lower().strip() == "done":
        break
    elif gym.lower().strip() == "membership":
        gymMember.upOrDowngrade()
    elif gym.lower().strip() == "check":
        gymMember.checkIn()

os.system('clear')
print("Prompt 7: Event Class".center(z))
class Event:
    __eventName = None
    __date = None
    __attendees = []
    def __init__(self,eventName,date,attendees = []):
        self.__eventName = eventName
        self.__date = date
        self.__attendees = attendees
    def __str__(self):
        return f"The {self.__eventName} will happen on {self.__date} and has {len(self.__attendees)} attendees".center(z)
    def getAttendees(self):
        for attendee in self.__attendees:
            print(attendee.center(z))
    def addAttendee(self,attendee):
        self.__attendees.append(attendee.capitalize())
    def removeAttendee(self,attendee):
        attendee = attendee.lower().strip()
        for person in self.__attendees:
            if attendee == person.lower().strip():
                self.__attendees.remove(attendee.capitalize())
        
event = Event("Tyler the Creator Concert","May 8, 2025",["Jackson","Denise","Evany","Benji"])
while True:
    os.system('clear')
    print("ADD or REMOVE attendees".center(z))
    print("Type DONE to move to the next prompt".center(z))
    print("")
    print(event)
    print("")
    event.getAttendees()
    print("")
    eventInput = input()
    if eventInput.lower().strip() == "done":
        break
    elif eventInput.lower().strip() == "add":
        print("What is the name of the person you would like to add? ".center(z))
        attendee = input()
        event.addAttendee(attendee)
    elif eventInput.lower().strip() == "remove":
        print("What is the name of the person you would like to remove? ".center(z))
        attendee = input()
        event.removeAttendee(attendee)

os.system('clear')
print("Prompt 8: ShoppingCart Class".center(z))
class ShoppingCart:
    __owner = None
    __items = []
    def __init__(self,owner,items):
        self.__owner = owner
        self.__items = items
    def displayCart(self):
        print(f"{self.__owner}'s cart:".center(z))
        print("")
        if len(self.__items) > 0:
            for item in self.__items:
                print(item.center(z))
        else:
            print("You have no items in your cart!".center(z))
    def addItem(self,item):
        self.__items.append(item)
    def removeItem(self,item):
        for lcv in self.__items:
            if item == lcv:
                self.__items.remove(item)
        
print("What is your name?".center(z))
name = input()
shopcart = ShoppingCart(name,[])
while True:
    os.system('clear')
    print("Type ADD to add an item. Type REMOVE to take one away!".center(z))
    print("Type DONE to move on.".center(z))
    print("")
    shopcart.displayCart()
    shop = input()
    if shop.lower().strip() == "done":
        break
    elif shop.lower().strip() == "add":
        print("What would you like to add? ".center(z))
        add = input()
        shopcart.addItem(add)
    elif shop.lower().strip() == "remove":
        print("What would you like to remove?".center(z))
        remove = input()
        shopcart.removeItem(remove)

os.system('clear')
print("Prompt 9: RestaurantOrder Class".center(z))
class RestaurantOrder:
    __customerName = None
    __orderItems = {}
    __totalPrice = 0
    def __init__(self,customerName,orderItems = {"Water":[0,1]},totalPrice = 0):
        self.__customerName = customerName
        self.__orderItems = orderItems
        orderListValues = list(self.__orderItems.values())
        for lcv in range(len(self.__orderItems)):
            self.__totalPrice += (orderListValues[lcv][0]*orderListValues[lcv][1])
    def addItem(self,key,price,quantity):
        orderListValues = list(self.__orderItems.values())
        wasTheItemInTheList = False
        orderList = list(self.__orderItems.keys())
        for lcv in orderList:
            if key == lcv:
                self.__orderItems[key][1] += int(quantity)
                self.__totalPrice += (int(orderListValues[orderList.index(key)][0])*int(orderListValues[orderList.index(key)][1]))
                wasTheItemInTheList = True
        if wasTheItemInTheList == False:
            self.__orderItems[key] = [int(price),int(quantity)]
            orderList = list(self.__orderItems.keys())
            orderListValues = list(self.__orderItems.values())
            self.__totalPrice += (int(orderListValues[orderList.index(key)][0])*int(orderListValues[orderList.index(key)][1]))
    def removeItem(self,key):
        orderList = list(self.__orderItems.keys())
        orderListValues = list(self.__orderItems.values())
        key = key.capitalize()
        for lcv in orderList:
            if key == lcv:
                self.__totalPrice -= (int(orderListValues[orderList.index(key)][0])*int(orderListValues[orderList.index(key)][1]))
                del self.__orderItems[key]
    def orderSummary(self):
        orderListValues = list(self.__orderItems.values())
        orderList = list(self.__orderItems.keys())
        print(self.__customerName.center(z))
        print("")
        for lcv in range(len(self.__orderItems)):
            print(f"{orderList[lcv]}   (x{orderListValues[lcv][1]})".center(z))
        print("")
        print(f"Total:\t\t\t${self.__totalPrice}".center(z))
print("What is your name? ".center(z))
name = input()
order = RestaurantOrder(name,{"Water":[0,1]},0)
while True:
    os.system('clear')
    print("Welcome to Jackson's Jumbo Jambalaya!".center(z))
    print("Type an item's name to order it or REMOVE to take something off the bill!".center(z))
    print("Type DONE to move to the next prompt!".center(z))
    print("")
    print("MENU:".center(z))
    print("Water : FREE".center(z))
    print("Lemonade : $3".center(z))
    print("Salad : $8".center(z))
    print("Chicken : $11".center(z))
    print("Fish : $16".center(z))
    print("Steak : $22".center(z))
    print("")
    order.orderSummary()
    menu = input()
    if menu.lower().strip() == "done":
        break
    elif menu.lower().strip() == "water" or menu.lower().strip() == "lemonade" or menu.lower().strip() == "salad" or menu.lower().strip() == "chicken" or menu.lower().strip() == "fish" or menu.lower().strip() == "steak":
        print(f"How many {menu}s would you like? ".center(z))
        quant = input()
        if menu.lower().strip() == "water":
            order.addItem("Water",0,quant)
        elif menu.lower().strip() == "lemonade":
            order.addItem("Lemonade",3,quant)
        elif menu.lower().strip() == "salad":
            order.addItem("Salad",8,quant)
        elif menu.lower().strip() == "chicken":
            order.addItem("Chicken",11,quant)
        elif menu.lower().strip() == "fish":
            order.addItem("Fish",16,quant)
        elif menu.lower().strip() == "steak":
            order.addItem("Steak",22,quant)
    elif menu.lower().strip() == "remove":
        print("Which item would you like to remove (This will remove ALL of chosen item) ".center(z))
        remove = input()
        order.removeItem(remove)
        
os.system('clear')
print("Prompt 10: Inventory Class with Validation".center(z))
class Inventory:
    __name = None
    __quantity = 0
    def __init__(self,name,quantity):
        self.__name = name
        self.__quantity = quantity
    def validateLogic(self,validateInput):
        if validateInput.isdigit():
            if float(validateInput) == int(validateInput):
                return True
            else:
                return False
        else:
            return False
    def increase(self,increaseValue):
        self.__quantity += int(increaseValue)
    def decrease(self,decreaseValue):
        if self.__quantity - int(decreaseValue) >= 0:
            self.__quantity -= int(decreaseValue)
    def getItemName(self):
        return self.__name
    def getQuantity(self):
        return self.__quantity

item = Inventory("Cheese",10)
while True:
    os.system('clear')
    print(f"Type INCREASE to increase the amount of {item.getItemName()}".center(z))
    print(f"Type DECREASE to decrease the amount of {item.getItemName()}".center(z))
    print("Type DONE to move to the next module".center(z))
    print("REMEMBER: you may only increment with integers, don't try any funny business!".center(z))
    print("")
    print(f"{item.getItemName()} : You have {item.getQuantity()}".center(z))
    itemInput = input()
    if itemInput.lower().strip() == "done":
        break
    elif itemInput.lower().strip() == "increase":
        print("How many are you adding? ".center(z))
        itemInput = input()
        if item.validateLogic(itemInput) == True:
            item.increase(itemInput)
        else:
            os.system('clear')
            print("Read the rules again.".center(z))
    elif itemInput.lower().strip() == "decrease":
        print("How many are you taking off? ".center(z))
        itemInput = input()
        if item.validateLogic(itemInput) == True:
            item.decrease(itemInput)
        else:
            os.system('clear')
            print("Read the rules again.".center(z))

os.system('clear')
print("Prompt 11: PasswordManager Class".center(z))
class PasswordManager:
    __username = None
    __password = None
    def __init__(self,username,password = ""):
        self.__username = username
        self.__password = password
    def setPassword(self,password):
        if len(password) > 7:
            for lcv in password:
                if lcv.isdigit():
                    for char in password:
                        if char == "!" or char == "?" or char == "@" or char == "#" or char =="$" or char == "%" or char == "^" or char == "&" or char == "*" or char == "(" or char == ")" or char == "-" or char == "_" or char == "+" or char == "=" or char == ":" or char == ";" or char == "{" or char == "}" or char == "[" or char == "]" or char == "|" or char == "\\" or char == "<" or char == ">" or char == "," or char == "." or char == "/":
                            self.__password = password
                            return True
            os.system('clear')
            print("You must include at least one number and special character in your password".center(z))
            time.sleep(2)
            return False
        else:
            os.system('clear')
            print("You must have at least 8 character in your password".center(z))
            time.sleep(2)
            return False
    def verifyPassword(self,username,password):
        if username == self.__username:
            if password == self.__password:
                print(f"Welcome back {self.__username}!".center(z))
                return True
            else:
                print("Username or password was incorrect.".center(z))
                return False
        else:
            print("Username or password was incorrect".center(z))
            return False
print("What would you like your username to be? ".center(z))
name = input()
user = PasswordManager(name)
while True:
    os.system('clear')
    print("What would you like your password to be? ".center(z))
    password = input()
    if user.setPassword(password) == True:
        break
while True:
    print("Now you can log in!".center(z))
    print("")
    print("Username: ".center(z))
    name = input()
    print("")
    print("Password: ".center(z))
    password = input()
    if user.verifyPassword(name,password) == True:
        break

os.system('clear')
print("Prompt 12: Car Class with Fuel Efficiency".center(z))
class Car:
    __make = None
    __model = None
    __fuelLevel = 0
    __milesDriven = 0
    __mileAccumulator = 0
    __averageMPG = 0
    def __init__(self,make,model,fuelLevel,milesDriven,mileAccumulator,averageMPG):
        self.__make = make
        self.__model = model
        self.__fuelLevel = fuelLevel
        self.__milesDriven = milesDriven
        self.__mileAccumulator = mileAccumulator
        self.__averageMPG = averageMPG
    def __str__(self):
        return f"You were gifted a car! It is a {self.__make} {self.__model} and has an average mpg of {self.__averageMPG}!".center(z)
    def drive(self,miles):
        os.system('clear')
        if miles.isdigit():
            if int(miles) > 0:
                if self.__fuelLevel - ((float(miles)+self.__mileAccumulator) / self.__averageMPG) >= 0:
                    self.__fuelLevel -= int((float(miles)+self.__mileAccumulator) / self.__averageMPG)
                    self.__milesDriven += int(miles)
                    self.__mileAccumulator += int(miles)
                    print(f"You drove {miles} miles!".center(z))
                    if self.__fuelLevel == 0:
                        print("You've ran out of gas! Time to refill!".center(z))
                        time.sleep(2)
                    else:
                        print(f"You have {self.__fuelLevel} gallons of gas remaining".center(z))
                        time.sleep(2)
                else:
                    print("You don't have enough gas for that distance!".center(z))
                    time.sleep(2)
        else:
            os.system('clear')
            print("Enter a valid distance.".center(z))
            time.sleep(2)
    def refill(self,refillAmt):
        os.system('clear')
        if refillAmt.isdigit():
            self.__mileAccumulator = 0
            if self.__fuelLevel + float(refillAmt) <= 36:
                self.__fuelLevel += int(refillAmt)
            else:
                self.__fuelLevel = 36
                print("That is too much. Your tank is now full".center(z))
        else:
            print("Enter a valid fuel amount.".center(z))
    def getMiles(self):
        return self.__milesDriven
    def getFuelLevel(self):
        return self.__fuelLevel
        
car = Car("Ford","F150",36,10,0,23)
print(car)

while True:
    os.system('clear')
    print("You can DRIVE or REFILL your car!".center(z))
    print("Type DONE to exit the modules!".center(z))
    print(f"Miles Driven: {car.getMiles()}".center(z))
    print(f"Fuel Level: {car.getFuelLevel()}/36".center(z))
    carInput = input()
    if carInput.lower().strip() == "done":
        break
    elif carInput.lower().strip() == "drive":
        print("How many miles will you drive? ".center(z))
        drive = input()
        car.drive(drive)
    elif carInput.lower().strip() == "refill":
        print("How many gallons will you put in your car? ".center(z))
        refill = input()
        car.refill(refill)
    



from colorama import Fore, Style, Back

#dayname = "Mon"
#month = "Jan"
#daynum = " 7"
#strhour = "11"
#strmin = "37"
#period = "AM"
#print("----------------------------------------------------------------------------------------------------------")
#print("           " + Fore.BLACK + Style.DIM + "+=====================================================+" + Style.NORMAL)
#print("           |" + Back.LIGHTBLACK_EX + Style.BRIGHT + "      " + Fore.BLACK + "|" + Back.RESET + "      " + Fore.GREEN + "##       #####" + Fore.RESET + "                          |")
#print("           |     |      ###_____#########                        |            +----------------------+")
#print("           |     | ____/ __|_____|########                       |            |                      |")
#print(f"           |      /  ___/  |     |  ####                         |            |      {dayname} {month} {daynum}      |")
#print("           |        /      |     |                               |            |                      |")
#print("           |       /       |     |                               |            +----------------------+")
#print("           |\ /\ /\|/\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ |")
#print("           | |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  ||            +----------------------+")
#print(f"           |#####################################################|            |       {strhour}:{strmin} {period}       |")
#print("           |#####################################################|            +----------------------+")
#print("           +=====================================================+")

import os
import time

z = os.get_terminal_size()
z = z[0]

print("I will be doing all the prompts for the practice and enjoyment of coding :)".center(z))
print("Press ENTER to continue".center(z))
input()
os.system('clear')

class Dog:
    name = None
    breed = None
    def __init__(self,name,breed=None):
        self.name = name
        self.breed = breed
    def __str__(self):
        return f"Hello {self.name}! You are a beautiful {self.breed}!".center(z)

dog1 = Dog("Bruce","Weimaraner")
dog2 = Dog("Charles","Golden Retriever")

print("Prompt 1: Dog Class".center(z))
print("")
print(dog1)
print(dog2) #NOTE: I am unsure if the prompt is asking for me to use the __str__ function for the printing of the classes, so from now on I will do both to show my understanding for both "methods" of printing
print("Without function:".center(z))
print(f"Hello {dog1.name}!".center(z))
print(f"Hello {dog2.name}!".center(z))
print("")
print("Press ENTER to move to the next prompt".center(z))
input()
os.system('clear')

class Song:
    title = None
    artist = None
    def __init__(self,title,artist):
        self.title = title
        self.artist = artist
    def __str__(self):
        return f"{self.title}, by {self.artist}".center(z)

song1 = Song("Happy Birthday","Patty Hill")
song2 = Song("House of Gold","Twenty One Pilots")
song3 = Song("Blank Space","Taylor Swift")

print("Prompt 2: Song Class".center(z))
print("")
print(song1)
print(song2)
print(song3)
print("Without function:".center(z))
print(f"{song1.artist} made {song1.title}.".center(z))
print(f"{song2.artist} made {song2.title}.".center(z))
print(f"{song3.artist} made {song3.title}.".center(z))
print("")
print("Press ENTER to move to the next prompt".center(z))
input()
os.system('clear')

class Player:
    firstName = None
    lastName = None
    sport = None
    salary = None
    def __init__(self,firstName,lastName,sport,salary):
        self.firstName = firstName
        self.lastName = lastName
        self.sport = sport
        self.salary = salary
    def __str__(self):
        return f"{self.firstName} {self.lastName} does {self.sport} and makes {self.salary} per year".center(z)

player1 = Player("Lionel","Messi","soccer","$12 million")
player2 = Player("LeBron","James","basketball","$48.7 million")

print("Prompt 3: Player Class".center(z))
print("")
print(player1)
print(player2)
print("Without function:".center(z))
print(f"{player1.firstName} {player1.lastName} does {player1.sport} and makes {player1.salary} per year".center(z))
print(f"{player2.firstName} {player2.lastName} does {player2.sport} and makes {player2.salary} per year".center(z))
print("")
print("Press ENTER to move to the next prompt".center(z))
input()
os.system('clear')

class Fruit:
    name = None
    color = None
    def __init__(self,name,color):
        self.name = name
        self.color = color
    def __str__(self):
        return f"{self.name}: {self.color}".center(z)

fruit1 = Fruit("Orange","orange")
fruit2 = Fruit("Strawberry", "red")
fruit3 = Fruit("Watermelon", "red")

print("Prompt 4: Fruit Class".center(z))
print("")
print(fruit1)
print(fruit2)
print(fruit3)
print("Without function:".center(z))
print(f"{fruit1.name}: {fruit1.color}".center(z))
print(f"{fruit2.name}: {fruit2.color}".center(z))
print(f"{fruit3.name}: {fruit3.color}".center(z))
print("")
print("Press ENTER to move to the next prompt".center(z))
input()
os.system('clear')

class Trail:
    name = None
    distance = None
    activities = None
    def __init__(self,name,distance,activities):
        self.name = name
        self.distance = distance
        self.activities = activities
    def __str__(self):
        return f"The {self.name} Trail is {self.distance} long and is suitable for {self.activities}".center(z)
trail1 = Trail("Harbor Lane","19 miles","running, biking, walking, boating")
trail2 = Trail("Devil's Tongue","145 kilometers","running, walking, biking")

print("Prompt 5: Trail Class".center(z))
print("")
print(trail1)
print(trail2)
print("Without function:".center(z))
print(f"The {trail1.name} Trail is {trail1.distance} long and is suitable for {trail1.activities}".center(z))
print(f"The {trail2.name} Trail is {trail2.distance} long and is suitable for {trail2.activities}".center(z))
print("")
print("Press ENTER to move to the next prompt".center(z))
input()
os.system('clear')

class Student:
    name = None
    grade = None
    studentID = None
    def __init__(self,name,grade,studentID):
        self.name = name
        self.grade = grade
        self.studentID = studentID
    def __str__(self):
        return f"Student ID: {self.studentID}, Name: {self.name}, Grade: {self.grade}".center(z)

student1 = Student("Jackson","A","212551")
student2 = Student("Benji","F","101010")
student3 = Student("Robert","B","311177")
print("Prompt 6: Student Class".center(z))
print("")
print(student1)
print(student2)
print(student3)
print("Without funciton:".center(z))
print(f"Student ID: {student1.studentID}, Name: {student1.name}, Grade: {student1.grade}".center(z))
print(f"Student ID: {student2.studentID}, Name: {student2.name}, Grade: {student2.grade}".center(z))
print(f"Student ID: {student3.studentID}, Name: {student3.name}, Grade: {student3.grade}".center(z))
print("")
print("Press ENTER to move to the next prompt".center(z))
input()
os.system('clear')

class Movie:
    title = None
    genre = None
    rating = None
    def __init__(self,title,genre,rating):
        self.title = title
        self.genre = genre
        self.rating = rating
    def __str__(self):
        return f"The movie {self.title} is a(n) {self.genre} movie and is rated {self.rating}".center(z)

movie1 = Movie("Deadpool","Action/Superhero","R")
movie2 = Movie("The Little Prince","Family/Adventure","PG")

print("Prompt 7: Movie Class".center(z))
print("")
print(movie1)
print(movie2)
print("Without function:".center(z))
print(f"The movie {movie1.title} is an {movie1.genre} movie and is rated {movie1.rating}".center(z))
print(f"The movie {movie2.title} is a {movie2.genre} movie and is rated {movie2.rating}".center(z))
print("")
print("Press ENTER to move to the next prompt".center(z))
input()
os.system('clear')

class Animal:
    name = None
    species = None
    def __init__(self,name,species):
        self.name = name
        self.species = species
    def __str__(self):
        return f"{self.name} : {self.species}".center(z)
class Zoo:
    location: None
    animals = None
    def __init__(self,location,*animals):
        animalList = []
        self.location = location
        for animal in animals:
            animalList.append(animal)
        self.animals = ', '.join(animalList)

    def __str__(self):
        return f"The zoo at {self.location} has a {self.animals}".center(z)
        
animal1 = Animal("Monkey","Mammal")
animal2 = Animal("Hawk","Bird")
animal3 = Animal("Shark","Fish")
animal4 = Animal("Black Mamba","Reptile")

zoo1 = Zoo("123 Adventure Way", animal1.name,animal2.name,animal3.name,animal4.name)

print("Prompt 8: Animal and Zoo Class".center(z))
print("")
print(zoo1)
print("Without function:".center(z))
print(f"The zoo at {zoo1.location} has a {zoo1.animals}".center(z))
print("")
print("Press ENTER to move to the next prompt".center(z))
input()
os.system('clear')

class Laptop:
    brand = None
    model = None
    price = None
    storageSize = None
    def __init__(self,brand,model,price,storageSize):
        self.brand = brand
        self.model = model
        self.price = price
        self.storageSize = storageSize
    def __str__(self):
        return f"The {self.brand} {self.model} has {self.storageSize} of storage and is only {self.price}!".center(z)

laptop1 = Laptop("Microsoft","Surface Laptop","$800","256 GB")
laptop2 = Laptop("Lenovo","IdeaPad Duet 5 OLED Chromebook","$610","64 GB")

print("Prompt 9: Laptop Class".center(z))
print("")
print(laptop1)
print(laptop2)
print("Without function:".center(z))
print(f"The {laptop1.brand} {laptop1.model} has {laptop1.storageSize} of storage and is only {laptop1.price}!".center(z))
print(f"The {laptop2.brand} {laptop2.model} has {laptop2.storageSize} of storage and is only {laptop2.price}!".center(z))
print("")
print("Press ENTER to move to the next prompt".center(z))
input()
os.system('clear')
globalItems = []
class ShoppingCart:
    owner = None
    items = []
    def __init__(self,items):
        self.items = items
    def printItem(self):
        if len(self.items) > 0:
            for item in range(len(self.items)):
                print((item + ". " + self.items[item]).center(z))
        else:
            print("There are no items to display".center(z))
    def addItem(items):
        globalItems.append(items)
    def removeItem(items):
        globalItems.remove(items)
while True:
    print("Prompt 10: ShoppingCart Class with Methods".center(z))
    print("You can ADD or REMOVE. Type DONE to move to the next prompt")
    print("")
    ShoppingCart.printItem
    print("")
    listInput = input()
    if listInput.lower().strip() == "add":
        print("What would you like to add?".center(z))
        addInput = input()
        ShoppingCart.addItem(addInput)
    elif listInput.lower().strip() == "remove":
        print("What would you like to remove?".center(z))
        removeInput = input()
        ShoppingCart.removeItem(removeInput)
    elif listInput.lower().strip() == "done":
        break
    os.system('clear')

os.system('clear')

print("Prompt 11:".center(z))
print("")
print(song1.center(z))
print(song2.center(z))
print(song3.center(z))
print("")
print("Press ENTER to move to the next prompt".center(z))
input()
os.system('clear')

print("Prompt 12:".center(z))
print("")
print(song1.center(z))
print(song2.center(z))
print(song3.center(z))
print("")
print("Press ENTER to move to the next prompt".center(z))
input()
os.system('clear')


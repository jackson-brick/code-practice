import time


input("Type something: ")
for i in range(4):
    print("Time is ticking...")
    print(4-i)
    time.sleep(1)
test = input("Type the word fart: ")
if test == "fart":
    print("You passed!")
else:
    print("Test failed.")

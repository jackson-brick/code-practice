import time


print("this should be a loading sequence")


def loading_sequence():
    load = ["Loading", ".", ".", "."]
    for loading_sequence_word in load:
        print(loading_sequence_word, end = " ")
        time.sleep(1)




loading_sequence()
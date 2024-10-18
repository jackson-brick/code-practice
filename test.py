import time


print("this should be a loading sequence")


def loading_sequence(seconds_to_load):
    time.sleep(0.5)
    print("Loading")
    for stl in range(seconds_to_load):
        print("   .")
        time.sleep(1)




loading_sequence(5)
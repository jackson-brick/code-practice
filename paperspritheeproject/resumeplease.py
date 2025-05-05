import csv
import time
import random
import os
from colorama import Fore, Style, Back
z = os.get_terminal_size()
z = z[0]
os.system('clear')

#A mysterious organization hired you to interview people and decide whether or not to let them through

users = []
with open('rpusers.csv','r') as file:
    reader = csv.DictReader(file)
    for line in reader:
        users.append(line)

intro_phrases = []

def login(username, password):
    for user in users:
        if user['username'] == username:
            if user['password'] == password:
                return True
    return False

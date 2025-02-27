from colorama import Fore, Style
import os
import random
import time
z=os.get_terminal_size()
z=z[0]

tempList = [" "," "," "," "," "," "," "]
keyboard_characters = ['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', '\\','a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', "'", 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '{', '}', '|', ':', '"', '<', '>', '?', '~', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '{', '}', '|','A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ':', '"', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']
security_check_messages = [
    "Initializing security protocols...",
    "Performing security integrity check...",
    "Scanning for malware...",
    "Checking firewall status...",
    "Verifying system encryption...",
    "Authenticating user credentials...",
    "Verifying security patches...",
    "Checking for unauthorized access...",
    "Validating antivirus software...",
    "Running network security scan...",
    "Checking for updates to security definitions...",
    "System security configuration loaded...",
    "Checking for system vulnerabilities...",
    "Verifying multi-factor authentication settings...",
    "Ensuring secure boot configuration...",
    "Examining data protection settings...",
    "Checking for known security threats...",
    "Performing device authentication...",
    "Network security protocols established...",
    "Initiating threat detection...",
    "Scanning external drives for potential threats...",
    "Monitoring system for unauthorized changes..."
]



def unencryption():
    print(Style.DIM)
    for lcv in security_check_messages:
        for line in range(10):
            x=""
            os.system('clear')
            lineLen = random.randint(3,50)
            for i in range(lineLen):
                x += random.choice(keyboard_characters)
            tempList.insert(0,x)
            tempList.pop(-1)

            print(Fore.GREEN + Style.BRIGHT+lcv+Style.RESET_ALL)
            time.sleep(0.01)
            print("")
            for item in tempList:
                print(Fore.GREEN + Style.DIM + item + Style.RESET_ALL)
                time.sleep(0.01)
            
    if code != "This is the way the world ends; Not with a bang but a whimper.":
        os.system('clear')
        print(Fore.RED + Style.BRIGHT+lcv+Style.RESET_ALL)
        print("")
        for item in tempList:
            print(Fore.RED + Style.DIM + item + Style.RESET_ALL)
        
    print(Style.RESET_ALL)
        

while True:
    os.system('clear')
    print(Style.RESET_ALL)
    print(Style.DIM)
    print(("Computer Information: " + Style.NORMAL + Style.BRIGHT + Fore.RED +"LOCKED").center(z))
    print(Style.RESET_ALL)
    print(Fore.GREEN)
    print("\n\n\n")
    code = input()
    os.system('clear')
    unencryption()
    if code == "Bypassing the security protocols...":
        print("")
        print(Style.BRIGHT + Fore.GREEN)
        print("Code success. Press ENTER to continue.")
        input()
        os.system('clear')
        break
    else:
        print(Style.BRIGHT + Fore.RED)
        print("ERROR 45D-13: CODE FAILED. Press ENTER to reboot.")
        print(Fore.GREEN)
        input()
        os.system('clear')


print(Style.RESET_ALL)
print(Style.DIM)
print(("Computer Information: " + Style.NORMAL + Style.BRIGHT + Fore.GREEN +"UNLOCKED").center(z))
input()
print(Style.RESET_ALL)
os.system('clear')
print("\t\tI\n\nWe are the hollow men\nWe are the stuffed men\nLeaning together\nHeadpiece filled with straw. Alas!\nOur dried voices, when\nWe whisper together\nAre quiet and meaningless\nAs wind in dry grass\nOr rats' feet over broken glass\nIn our dry cellar\n\nShape without form, shade without colour,\nParalysed force, gesture without motion;\n\nThose who have crossed\nWith direct eyes, to death's other Kingdom\nRemember us-if at all-not as lost\nViolent souls, but only\nAs the hollow men\nThe stuffed men.\n\n\n\t\tII\n\nEyes I dare not meet in dreams\nIn death's dream kingdom\nThese do not appear:\nThere, the eyes are\nSunlight on a broken column\nThere, is a tree swinging\nAnd voices are\nIn the wind's singing\nMore distant and more solemn\nThan a fading star.\n\nLet me be no nearer\nIn death's dream kingdom\nLet me also wear\nSuch deliberate disguises\nRat's coat, crowskin, crossed staves\nIn a field\nBehaving as the wind behaves\nNo nearer-\n\nNot that final meeting\nIn the twilight kingdom\n\n\n\t\tIII\n\nThis is the dead land\nThis is cactus land\nHere the stone images\nAre raised, here they receive\nThe supplication of a dead man's hand\nUnder the twinkle of a fading star.\n\nIs it like this\nIn death's other kingdom\nWaking alone\nAt the hour when we are\nTrembling with tenderness\nLips that would kiss\nForm prayers to broken stone.\n\n\n\t\tIV\n\nThe eyes are not here\nThere are no eyes here\nIn this valley of dying stars\nIn this hollow valley\nThis broken jaw of our lost kingdoms\n\nIn this last of meeting places\nWe grope together\nAnd avoid speech\nGathered on this beach of the tumid river\n\nSightless, unless\nThe eyes reappear\nAs the perpetual star\nMultifoliate rose\nOf death's twilight kingdom\nThe hope only\nOf empty men.\n\n\n\t\tV\n\nHere we go round the prickly pear\nPrickly pear prickly pear\nHere we go round the prickly pear\nAt five o'clock in the morning.\n\nBetween the idea\nAnd the reality\nBetween the motion\nAnd the act\nFalls the Shadow\n\t\t\t\t\tFor Thine is the Kingdom\n\nBetween the conception\nAnd the creation\nBetween the emotion\nAnd the response\nFalls the Shadow\n\t\t\t\t\tLife is very long\n\nBetween the desire\nAnd the spasm\nBetween the potency\nAnd the existence\nBetween the essence\nAnd the descent\nFalls the Shadow\n\t\t\t\t\tFor Thine is the Kingdom\n\nFor Thine is\nLife is\nFor Thine is the\n\nThis is the way the world ends\nThis is the way the world ends\nThis is the way the world ends\nNot with a bang but a whimper.")


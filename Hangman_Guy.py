#Aravind Alwar
#April 29,2023
#Hangman_Guy.py

def Hangman_Guy(chances):
    if chances==10:
        print("  _________      \n")
        print("  |        |     \n")
        print("  |        |     \n")
        print("           o     \n")
        print("___________|_____\n")
    elif chances == 9:
        print("  _________      \n")
        print("  |        |     \n")
        print("  |        0     \n")
        print("           o     \n")
        print("___________|_____")
    elif chances ==8:
        print("  _________      \n")
        print("  |        |     \n")
        print("  |        0     \n")
        print("           o     \n")
        print("__________/|_____")
    elif chances == 7:
        print("  _________      \n")
        print("  |        |     \n")
        print("  |        0     \n")
        print("           o     \n")
        print("__________/|\____")
    elif chances ==6:
        print("  _________      \n")
        print("  |        |     \n")
        print("  |        0     \n")
        print("           |     \n")
        print("__________/|\____")
    elif chances == 5:
        print("  _________      \n")
        print("  |        |     \n")
        print("  |        0     \n")
        print("           |\    \n")
        print("__________/|\____")
    elif chances == 4:
        print("  _________      \n")
        print("  |        |     \n")
        print("  |        0     \n")
        print("          /|\    \n")
        print("__________/|\____")
    elif chances == 3:
        print("  _________      \n")
        print("  |        |     \n")
        print("  |        0o    \n")
        print("          /|\    \n")
        print("__________/|\____")
    elif chances == 2:
        print("  _________      \n")
        print("  |        |     \n")
        print("  |       o0o    \n")
        print("          /|\    \n")
        print("__________/|\____")
    elif chances == 1:
        print("  _________      \n")
        print("  |        >     \n")
        print("  |       o0o    \n")
        print("          /|\    \n")
        print("__________/|\____")
    elif chances == 0:
        print("  _________      \n")
        print("  |        <>    \n")
        print("  |       o0o    \n")
        print("          /|\    \n")
        print("__________/|\____")
        print("You lost your turns!")

#Aravind Alwar
#January 31, 2023
#Hangman.py-App
import Game_Design
ON=True
def Menu():
    print("=======HangMan=======")
    print("Welcome to the Hangman app,a place for you to sharpen your brain with detective work!")
    print("To begin this game,Press 1.")
    print("To view credits and Design,press 2.")
    print("If you want to exit,press 3.")
def Decision(Choice):
    if Choice==1:
        Game_Design.Play()
    elif Choice==2:
        Game_Design.Credits()
    elif Choice==3:
        print("Thank you for your interest in the Hangman App!! We hope to see you in the future.")
        pass

if __name__=='__main__':
    Menu()
    while ON:
        Choice=int(input("Enter your choice(1,2,or 3):"))
        Decision(Choice)
        if Choice==3:
            ON=False

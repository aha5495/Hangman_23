#February 1,2023
from Hangman_Guy import Hangman_Guy    #Needed for effective implementation of the game.
import random
def Play():
    Total=['Computer','Engineer','Surfing','Entertainment','Macbook','HBO','Integration','Setup','Optimize','Technology']
    for word in list(Total):
        print(word)
        i=tuple(word)
        print(i)
    Chosen=random.choice(Total)
    chances=10
    amt_left=int(len(Chosen))
    Letters_guessed=' ' #We need a record of what word was used exactly.
    Incorrect=[]
    Correct=[]
    print()
    guessed=False
    name=input("What is your name:")
    print("Today's contestant,",name," will be guessing the order of the assigned random word!")
#Task 2:We need to output the exact word correctly when a user guesses the letters.
    while (chances > 0) and (guessed==False) and (amt_left>=0): #I initially had my own idea of doing it down there.Why is a while loop needed here?
        for l in Chosen: # Needed to loop through each letter in the Word;Thus,a for loop is important.
            if l in Letters_guessed: #Assume the user guessed a letter correctly...
                print(l,end=' ') #Print the letter how many ever times it is in Chosen variable.
                Correct.append(l) #Add it to the set of correct letters
            else:
                print('_',end=' ') #We aim for our hidden mysteries to be '_'.
                Incorrect.append(l) #Incorrect Add
#Task 1:Have the user guess the letter for a certain # of turns
#Curiousity:Why no while loop here?- Because we are applying that to the process of the letters printing out rather than guessing.
        guess=input("\nLetter:")
        Letters_guessed+=guess #We need to know what letter was exactly guessed at that time.This updates.
        if guess in Chosen:
            print(f"Correct!! The letter {guess} is in the word.Keep it up!")
            amt_left -= Chosen.count(guess)
        else:
            Letters_guessed+=guess
            chances-=1
            print(f"The letter {guess} is not in the word.{chances} more chances left!")
            Hangman_Guy(chances) #Print is redundant,as the function already prints.
# Task 4:Guessed Variable switches to true
        if amt_left == 0:
            guessed = True
#Task 3:The endings of a game.
    if chances==0 or amt_left!=0 or guessed==False:
        print(f'Sorry {name}, you did not guess the word.The word\'s {Chosen}.Better luck next time!')
        Hangman_Guy(chances)
    else:
        print(f"Congratulations {name},you managed to solve the word with {chances} chances remaining.")
        Hangman_Guy(chances)
        print(Chosen)
def Credits():
    print("Creator credit goes to:Aravind Alwar and CMPSCI 132 colleague\n")
    print("Design:Aravind Alwar\n")
    print("Implementation Credit:https://www.pythonforbeginners.com/code-snippets-source-code/game-hangman")
    print("This has been my First hands-on coding App I've aimed to build. I first thought,as a new Year")
    print("resolution, that I needed to get some hands-on experience with Coding to advance in my career.I wanted to start with something")
    print("familiar, so I decided to try out Hangman. Overall,I cannot express how grateful I am of all who have")
    print("been willing to sacrifice their time to help me out achieve my goal. That's a takeaway from the project")
    print("that I've learned. Teamwork,especially when stuck alone,can really make the difference in quality. Special")
    print("thanks to all for being interested in the game. It took me 2 months to build,but we tackled the wind. Stay tuned")
    print("for my upcoming projects anytime!!")


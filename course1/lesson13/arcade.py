from rps9 import playGame
from numberGuess import numberGuess
import sys
def chooseGame (player):
    welcomeBack = False
    while True:
        if welcomeBack == True:
             print(f"\n{player}, welcome back to the arcade meun")
        playerChoice=  input(f"\n{player}, please enter 1 for Rock Paper Scissors, 2 for Number Guess, \n\n\n or x to quit the arcade game \n")
        if playerChoice not in ["1", "2", "x"]:
            print(f"\n{player}, you must enter either 1, 2, or x")
            chooseGame(player)
        welcomeBack = True
        if playerChoice == "1":
            rps = playGame(player)
            rps()
        elif playerChoice == "2":
            number = numberGuess(player)
            number()
        else :
            print(f"\n{player}, good bye")
            sys.exit()


if __name__ == "__main__":
 import argparse

 person = argparse.ArgumentParser(
     description= "This is for providing a personalized game experience"
 )
 person.add_argument(
     "-n", "--name" , metavar= "name", required= True, help= "Provide a name to get a personalized game experience"
 )

 args = person.parse_args()
 
 chooseGame(args.name)


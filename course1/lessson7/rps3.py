import random
from enum import Enum
import sys

def playGame():
    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3
    playerName =  input("\n what's that your name again?\n")
    print(f"\n Welcome {playerName} to rock, paper, scissors")
    def playRound():
        playerChoice = input(playerName + " " + "Enter your choice: \n 1 for rock \n 2 for paper \n 3 for scissors \n")
        pythonChice = random.choice("123")

        if playerChoice not in ["1", "2", "3"]:
            print("\n You must enter either 1, 2, or 3")
            playRound()
        convertedPlayerChoice = int(playerChoice)
        convertedPythonChoice = int(pythonChice)

    

        print("you chose", " " ,str(RPS(convertedPlayerChoice)).replace("RPS.", ""))
        print("python chose", " " ,str(RPS(convertedPythonChoice)).replace("RPS.", ""))

        if convertedPlayerChoice == convertedPythonChoice:
            print("it's a tie")
        elif convertedPlayerChoice == RPS.ROCK.value and convertedPythonChoice == RPS.PAPER.value:
            print("python wins")
        elif convertedPlayerChoice == RPS.PAPER.value and convertedPythonChoice == RPS.SCISSORS.value:
            print("python wins")
        elif convertedPlayerChoice == RPS.SCISSORS.value and convertedPythonChoice == RPS.ROCK.value:
            print("python wins")
        else: 
            print("you win")
    
        while True:
            playagain = input("\n do you want to play again? y/q \n")
            if playagain.lower() not in ["y", "q"]:
                print("invalid input")
                continue
            else :
                break

        if playagain.lower() == "y" : 
            playRound()
        else :
            print("good bye")
            sys.exit()


    playRound()

             

playGame()
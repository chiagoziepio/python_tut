import random
from enum import Enum
import sys

gameCount = 1

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

        def decideWinner(convertedPlayerChoice, convertedPythonChoice):

            if convertedPlayerChoice == convertedPythonChoice:
                return "it's a tie"
            elif convertedPlayerChoice == RPS.ROCK.value and convertedPythonChoice == RPS.PAPER.value:
                return "python wins"
            elif convertedPlayerChoice == RPS.PAPER.value and convertedPythonChoice == RPS.SCISSORS.value:
                return "python wins"
            elif convertedPlayerChoice == RPS.SCISSORS.value and convertedPythonChoice == RPS.ROCK.value:
                return "python wins"
            else: 
                return "you win"

        gameResult = decideWinner(convertedPlayerChoice, convertedPythonChoice)
        print(gameResult)

        

        global gameCount
        print("game " + str(gameCount) + " is over")
        gameCount += 1

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
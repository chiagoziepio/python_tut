from enum import Enum
import random
import sys

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

playagain = True

playerName = input("\n what is your name?: \n")
convertedPlayerName = str(playerName).lower()
print(convertedPlayerName + " " + "welcome to RPS game")
while playagain : 
    playerChoice = input("\n Enter your choice: \n 1 for rock \n 2 for paper \n 3 for scissors \n")
    convertedPlayerChoice = int(playerChoice)
    if convertedPlayerChoice < 1 or convertedPlayerChoice > 3:
        print("invalid choice")
        continue

   

    computerChoice = random.choice("123")
    convertedComputerChoice = int(computerChoice)

    print("\n computer choice is" + str(RPS(convertedComputerChoice)).replace("RPS.", ""))
    print(convertedPlayerName + "you chose " + str(RPS(convertedPlayerChoice)).replace("RPS.", ""))
    if convertedPlayerChoice == convertedComputerChoice:
        print("it's a tie")
    elif convertedPlayerChoice == RPS.ROCK.value and convertedComputerChoice == RPS.PAPER.value:
        print("you win")
    elif convertedPlayerChoice == RPS.PAPER.value and convertedComputerChoice == RPS.SCISSORS.value:
        print("you win")
    elif convertedPlayerChoice == RPS.SCISSORS.value and convertedComputerChoice == RPS.ROCK.value:
        print("you win")
    else:
        print("you lose")
    playagain = input("\n do you want to play again? y/n \n")
    if playagain.lower() == "y":
        continue
    else:
        playagain = False
        sys.exit("\n good bye")
        break

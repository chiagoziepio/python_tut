import random
from enum import Enum
import sys



def playGame():
    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    gameCount = 0
    playerWins = 0
    pythonWins = 0

    playerName =  input("\n what's that your name again?\n")
    print(f"\n Welcome {playerName} to rock, paper, scissors")
    def playRound():
        nonlocal gameCount
        nonlocal playerWins
        nonlocal pythonWins
        playerChoice = input(f"{playerName} Enter your choice: \n 1 for rock \n 2 for paper \n 3 for scissors \n")
        pythonChice = random.choice("123")

        if playerChoice not in ["1", "2", "3"]:
            print("\n You must enter either 1, 2, or 3")
            playRound()
        convertedPlayerChoice = int(playerChoice)
        convertedPythonChoice = int(pythonChice)

    

        print(f"you chose {RPS(convertedPlayerChoice).name}")
        print(f"python chose {RPS(convertedPythonChoice).name}")

        def decideWinner(convertedPlayerChoice : int, convertedPythonChoice : int):

            nonlocal playerWins
            nonlocal pythonWins


            if convertedPlayerChoice == convertedPythonChoice:
                return "it's a tie"
            elif convertedPlayerChoice == RPS.ROCK.value and convertedPythonChoice == RPS.PAPER.value:
                pythonWins += 1
                return "python wins"
            elif convertedPlayerChoice == RPS.PAPER.value and convertedPythonChoice == RPS.SCISSORS.value:
                pythonWins += 1
                return "python wins"
            elif convertedPlayerChoice == RPS.SCISSORS.value and convertedPythonChoice == RPS.ROCK.value:
                pythonWins += 1
                return "python wins"
            else: 
                playerWins += 1
                return "you win"

        gameResult = decideWinner(convertedPlayerChoice, convertedPythonChoice)
        print(gameResult)
        gameCount += 1
        print(f"\ngame {gameCount} is over")
        print(f"\n you have {playerWins} wins")
     
        print(f"\npython has {pythonWins} wins")
  

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


    return playRound

             

play_rock_paper_scissor = playGame
if __name__ == "__main__":
 play = play_rock_paper_scissor()
 play()
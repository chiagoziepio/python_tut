import random
from enum import Enum
import sys



def playGame(playerName = "unknown Player"):
    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    gameCount = 0
    playerWins = 0
    pythonWins = 0

  
    print(f"\n{playerName}, welcome to rock, paper, scissors")
    def playRound():
        nonlocal gameCount
        nonlocal playerWins
        nonlocal pythonWins
        nonlocal playerName

        playerChoice = input(f"\n{playerName}, please enter your choice: \n 1 for rock \n 2 for paper \n 3 for scissors \n")
        pythonChice = random.choice("123")

        if playerChoice not in ["1", "2", "3"]:
            print(f"\n{playerName}, you must enter either 1, 2, or 3")
            playRound()
        convertedPlayerChoice = int(playerChoice)
        convertedPythonChoice = int(pythonChice)

    

        print(f"{playerChoice}, you chose {RPS(convertedPlayerChoice).name}")
        print(f"python chose {RPS(convertedPythonChoice).name}")

        def decideWinner(convertedPlayerChoice : int, convertedPythonChoice : int):

            nonlocal playerWins
            nonlocal pythonWins
            nonlocal playerName


            if convertedPlayerChoice == convertedPythonChoice:
                return f"{playerName} it's a tie"
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
                return f"{playerName} you won"

        gameResult = decideWinner(convertedPlayerChoice, convertedPythonChoice)
        print(gameResult)
        gameCount += 1
        print(f"\ngame {gameCount} is over")
        print(f"\n{playerName} you have {playerWins} wins")
     
        print(f"\npython has {pythonWins} wins")
  

        while True:
            playagain = input(f"\n {playerName}, do you want to play again? y/q \n")
            if playagain.lower() not in ["y", "q"]:
                print("invalid input")
             
                continue
            else :
                break

        if playagain.lower() == "y" : 
       
            playRound()
        else :
            print(f"good bye, {playerName}")
            if __name__ == "__main__":
                sys.exit()
            else:    
                return


    return playRound

             


if __name__ == "__main__":
 import argparse

 person = argparse.ArgumentParser(
     description= "This is for providing a personalized game experience"
 )
 person.add_argument(
     "-n", "--name" , metavar= "name", required= True, help= "Provide a name to get a personalized game experience"
 )

 args = person.parse_args()
 
 play_rock_paper_scissor = playGame(args.name)
 play_rock_paper_scissor()
 
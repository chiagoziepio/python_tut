import random
import sys
def numberGuess(name = "unknown Player"):
    tries = 0
    def playGuess():
        nonlocal tries
        nonlocal name
        playerGuess = input(f"\n{name},  i am thinking of a number between 1 and 10, take a guess: \n")
        if playerGuess not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
            print(f"\n{name}, you must enter a number between 1 and 10")
            playGuess()
        convertedPlayerGuess = int(playerGuess)
        
      
        pythonGuess = random.randint(1, 10)
        print(f"\n{name}, your guess is {convertedPlayerGuess}")
        print(f"python guessed {pythonGuess}")
        tries += 1
        def checkGuess(playerGuess : int, pythonGuess : int):
            nonlocal tries
            nonlocal name
            if playerGuess == pythonGuess:
                return f"\n{name}, you win"
            else:
                return f"\n{name}, you lose"
        guessResult = checkGuess(convertedPlayerGuess, pythonGuess)
        print(guessResult)
        print(f"\n{name} you have {tries} tries done")
        while True:
            playagain = input(f"\n {name}, do you want to play again? y/q \n")
            if playagain.lower() not in ["y", "q"]:
                print("invalid input")
                
                continue
            else :
                break

        if playagain.lower() == "y" : 
            
            playGuess()
        else :
            print(f"good bye, {name}")
            if __name__ == "__main__":
                sys.exit()
            else:    
                return
            
         

    return playGuess

if __name__ == "__main__":
 import argparse

 person = argparse.ArgumentParser(
     description= "This is for providing a personalized game experience"
 )
 person.add_argument(
     "-n", "--name" , metavar= "name", required= True, help= "Provide a name to get a personalized game experience"
 )

 args = person.parse_args()
 name = args.name
 play = numberGuess(name)
 play()
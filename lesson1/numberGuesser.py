
import random
import sys



def guessGame(name : str):
    gameCount = 0
    wins = 0
    def gamePlayer (name : str):
        userChoice = input(f"{name}, guess the number i have in mind, from 1 to 100\n")

        if not userChoice.isdigit() or int(userChoice) < 1 or int(userChoice) > 100 :
            
            print("what you entered it not a number or doesnt fall in the range, please try again")
            return gamePlayer(name)

        computerChoice = random.randint(1, 100)
        convertedUserChoice = int(userChoice)

        
        def askToPlayAgain():
            playAgainResponse = input("\n Do you want to play again, Enter: \n y for Yes\n n for No\n")
            return playAgainResponse


        def decideWinner(computerChoice, convertedUserChoice):
          
            nonlocal wins
           
            if computerChoice == convertedUserChoice :
                wins += 1
                return   f"💐 hurray {name}, you guessed right. You guessed {convertedUserChoice} and i had {computerChoice} in mind"
            else :
                return  f"you guessed wrong You guessed {convertedUserChoice} and i had {computerChoice} in mind"
        
        guessResult = decideWinner(computerChoice, convertedUserChoice)
        nonlocal gameCount
        gameCount += 1
        print(guessResult)
        print(f"Games played: {gameCount}")
        print(f"Wins: {wins}")
        print(" ")
        playAgainResponse = askToPlayAgain()

        if playAgainResponse.lower() == "y":
           return gamePlayer(name)
        else : 
            print("Thanks for playing 🥳🍾")
            if __name__ == "__main__":
                sys.exit()
            else:
                return
    return gamePlayer




if __name__ == "__main__":
    import argparse
    guessParser = argparse.ArgumentParser(
    description= "Guessing game"

  )

    guessParser.add_argument(
    "-n" , "--name" , metavar= "name",
    required= True , help= "enter a name to address you by"
   )


    args = guessParser.parse_args()
    game = guessGame(args.name)
    game(args.name)




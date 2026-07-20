from numberGuesser import guessGame
from rps import  rock_paper_scissors
import sys



def chooseGame(name= "this man"):
    welcomeBack = False
    
    while True :
        if welcomeBack == True :
            print(f"Welcome back {name}")
        userOpt = input("welcome to the arcade meun. Please select\n 1 for RPS game \n 2 for number guessing game\n or x to exit the\n")
        if userOpt not in ["1", "2", "x"]:
            chooseGame()
        welcomeBack = True
        if userOpt == "1":
            rock_paper_scissors()
        elif userOpt == "2":
          game = guessGame(name)
          game(name)
        else  :
            sys.exit()
      
if __name__ == "__main__":
    import argparse
    arcadeParser = argparse.ArgumentParser(
    description= "arcade menu"

    )

    arcadeParser.add_argument(
    "-n" , "--name" , metavar= "name",
    required= True , help= "enter a name to address you by"
    )


    args = arcadeParser.parse_args()
    chooseGame(args.name)
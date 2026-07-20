from enum import Enum
import sys
import random


def rps_game():
    game_count = 0
    player_win_count = 0
    computer_win_count = 0
    tie_count = 0

    def playRPS():
        class RPS (Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

    

        playerChoice = input("\nEnter your choice, \n 1 for Rock,\n 2 for paper,\n 3 for scissors:\n")


        if not playerChoice.isdigit():
            print("Invalid choice, please try again, enter 1, 2 or 3")
            return playRPS()
        convetedPlayerChoice = int(playerChoice)


        if convetedPlayerChoice < 1 or convetedPlayerChoice >  3 :
            print("Invalid choice, please try again, enter 1, 2 or 3")
            return playRPS()

        computerChoice = int(random.choice("123"))


        print("\nYou chose" + " " + str(RPS(convetedPlayerChoice)).replace("RPS.", ""))
        print("Computer chose" + " " + str(RPS(computerChoice)).replace("RPS.", "") )
        print(" ")

        def gameDecisioning( computerChoice, convetedPlayerChoice) :
            nonlocal player_win_count
            nonlocal computer_win_count
            nonlocal tie_count
            if convetedPlayerChoice == computerChoice:
                tie_count += 1
                return "It's a tie"
                
            elif convetedPlayerChoice == 1 and computerChoice == 2:
                computer_win_count += 1
                return "You lose"
            elif convetedPlayerChoice == 1 and computerChoice == 3:
                player_win_count += 1
                return "You win"
            elif convetedPlayerChoice == 2 and computerChoice == 1:
                player_win_count += 1
                return "You win"
            elif convetedPlayerChoice == 2 and computerChoice == 3:
                computer_win_count += 1
                return "You lose"
            elif convetedPlayerChoice == 3 and computerChoice == 1:
                computer_win_count += 1
                return "You lose"
            elif convetedPlayerChoice == 3 and computerChoice == 2:
                player_win_count += 1
                return "You win"
            else:

                return "Invalid choice, please try again, enter 1, 2 or 3"
                
        nonlocal game_count
        game_count += 1
        print(f"Games played: {game_count}")
        result =   gameDecisioning(computerChoice, convetedPlayerChoice)
        print(" ")
        print(result)
        print(" ")
        print(f"Player wins: {player_win_count}")
        print(f"Computer wins: {computer_win_count}")
        print(f"Ties: {tie_count}")
        def askToPlayAgain():
            playAgainResponse = input("\n Do you want to play again, Enter: \n y for Yes\n n for No\n")
            return playAgainResponse
        playAgainResponse = askToPlayAgain()

        if playAgainResponse.lower() == "y":
            return playRPS()
        else:
           if __name__ == "__main__":
                sys.exit("Thanks for playing")
           else :
                return
               

       

    return playRPS


rock_paper_scissors = rps_game()

if __name__ == "__main__":
    rock_paper_scissors()


   
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

print("Welcome to Rock Paper Scissors")
playerName = input("Enter your name: ")
print("Hello " + playerName)

playerChoice = input("Enter 1 for rock \n 2 for paper \n 3 for scissors \n")
player = int(playerChoice)
computerChoice = random.choice("123")
computer = int(computerChoice)

if player < 1 or player >  3:
    print("Invalid choice")
    exit()

print("Computer chose " + str(RPS(computer)).replace("RPS.", " "))
print("You chose " + str(RPS(player)).replace("RPS.", " "))
if player == 1 and computer == 3 : 
    print(" 🍾  You win")
elif player == 2 and computer == 1 : 
    print(" 🍾  You win")
elif player == 3  and computer == 2 :
    print(" 🍾  You win")
elif player == computer    :
    print("🫢  It's a tie")
else:
    print(" 🖥️  computer wins")
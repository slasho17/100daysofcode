import random

playersChoice = -1
options = {0: "Rock", 1: "Paper", 2: "Scissors"}
while playersChoice not in options:
    playersChoice = int(input("Press 0 for rock, 1 for paper and 2 for scissors"))
    
botChoice = random.randint(0,2)

if playersChoice == botChoice:
    print("Draw")
elif playersChoice == 1 and botChoice == 0:
    print("Bot chose rock, you win. Congratulations")
elif playersChoice == 2 and botChoice == 0:
    print("Bot chose rock, you lose. Loser")
elif playersChoice == 0 and botChoice == 1:
    print("Bot chose paper, you lose. Loser")
elif playersChoice == 0 and botChoice == 2:
    print("Bot chose scissors, you win. Congratulations")
elif playersChoice == 1 and botChoice == 2:
    print("Bot chose scissors, you lose. Loser")
elif playersChoice == 2 and botChoice == 1:
    print("Bot chose paper, you win. Congratulations")

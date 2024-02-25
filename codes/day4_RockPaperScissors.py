import random

players_choice = -1
options = {0: "Rock", 1: "Paper", 2: "Scissors"}
while players_choice not in options:
    players_choice = int(input("Press 0 for rock, 1 for paper and 2 for scissors"))
    
bot_choice = random.randint(0,2)

if players_choice == bot_choice:
    print("Draw")
elif players_choice == 1 and bot_choice == 0:
    print("Bot chose rock, you win. Congratulations")
elif players_choice == 2 and bot_choice == 0:
    print("Bot chose rock, you lose. Loser")
elif players_choice == 0 and bot_choice == 1:
    print("Bot chose paper, you lose. Loser")
elif players_choice == 0 and bot_choice == 2:
    print("Bot chose scissors, you win. Congratulations")
elif players_choice == 1 and bot_choice == 2:
    print("Bot chose scissors, you lose. Loser")
elif players_choice == 2 and bot_choice == 1:
    print("Bot chose paper, you win. Congratulations")

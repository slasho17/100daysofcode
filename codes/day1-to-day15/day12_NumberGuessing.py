import random
difficulty = input("Welcome to number guessing, what difficulty would you like to play? Type 'easy' or 'hard':\n")

while(difficulty not in ['easy', 'hard']):
    difficulty = input("Welcome to number guessing, what difficulty would you like to play? Type 'easy' or 'hard':\n")
    
if difficulty == 'easy':
    attempts = 10
else:
    attempts = 5

occult_number = random.randint(0, 100)
while attempts > 0:
    print(f"You have {attempts} attempts remaining")
    guess = int(input("Guess a number from 0 to 100: "))
    if guess == occult_number:
        print("Congrats, you guessed right :)")
        exit()
    elif guess > occult_number:
        print("Too high")
    elif guess < occult_number:
        print("Too low")
    attempts = attempts -1

print(f"Too bad, you ran out of guess. The number was {occult_number}")
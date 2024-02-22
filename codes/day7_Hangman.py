# you'll need to run "pip install random-word" for this to work
# you'll need to run "pip install replit" for this to work

from random_word import RandomWords
from replit import clear
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

r = RandomWords()
word = r.get_random_word()
displayWord = ["_"] * len(word)
lives = 6
lettersGuessed = []
print(word)
while True:
    clear()
    print(stages[lives])
    print(displayWord)
    guess = input("Choose a letter\n").lower()
    if guess in lettersGuessed:
        print("You already tried this one, try again")
        continue
    lettersGuessed.append(guess)
    guessedRight = False
    
    for i, letter in enumerate(word):
        if guess == letter:
            displayWord[i] = guess
            guessedRight = True
            
            if "_" not in displayWord:
                print("You win, congrats")
                exit()

    if guessedRight is False:
        lives = lives -1

    if lives == 0:
        print(stages[lives])
        print("Suxs to b u loser")
        print("the word was: ", word)
        exit()
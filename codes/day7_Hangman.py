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
display_word = ["_"] * len(word)
lives = 6
letters_guessed = []
print(word)
while True:
    clear()
    print(stages[lives])
    print(display_word)
    guess = input("Choose a letter\n").lower()
    if guess in letters_guessed:
        print("You already tried this one, try again")
        continue
    letters_guessed.append(guess)
    guessed_right = False
    
    for i, letter in enumerate(word):
        if guess == letter:
            display_word[i] = guess
            guessed_right = True
            
            if "_" not in display_word:
                print("You win, congrats")
                exit()

    if guessed_right is False:
        lives = lives -1

    if lives == 0:
        print(stages[lives])
        print("Suxs to b u loser")
        print("the word was: ", word)
        exit()
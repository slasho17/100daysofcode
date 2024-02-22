import day14_extra
from replit import clear
import random

data = day14_extra.data
score = 0
continuePlaying = True
while continuePlaying:
    clear()
    print (day14_extra.logo)
    print (f"Your current score is {score}")
    A = random.choice(data)
    B = random.choice(data)
    print (f"Compare A: {A['name']}, {A['description']} from {A['country']}")
    print (day14_extra.vs)
    print (f"Compare B: {B['name']}, {B['description']} from {B['country']}")
    choice = input("Choose between A of B: ").upper()
    if (choice == "A" and A['follower_count'] > B['follower_count']) or (choice == "B" and A['follower_count'] < B['follower_count']):
        score = score +1
    else:
        print("You lose, sucks to be youuu")
        exit()
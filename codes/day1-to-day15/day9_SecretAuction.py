from replit import clear
print("Welcome to the auction, we are selling Maia's favorite blanket")

name = input("What is your name?")
bid = int(input("What is your bid?"))
continue_playing = input("Are there other players? y/n")

all_bids = {bid:name}
while continue_playing == 'y':
    clear()
    name = input("What is your name?")
    bid = int(input("What is your bid?"))
    all_bids[bid] = name
    continue_playing = input("Are there other players? y/n")

print (all_bids.keys())
print (max(all_bids.keys()))
print (f"The winner is {all_bids[max(all_bids.keys())]}")
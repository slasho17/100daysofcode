from replit import clear
print("Welcome to the auction, we are selling Maia's favorite blanket")

name = input("What is your name?")
bid = int(input("What is your bid?"))
continuePlaying = input("Are there other players? y/n")

allBids = {bid:name}
while continuePlaying == 'y':
    clear()
    name = input("What is your name?")
    bid = int(input("What is your bid?"))
    allBids[bid] = name
    continuePlaying = input("Are there other players? y/n")

print (allBids.keys())
print (max(allBids.keys()))
print (f"The winner is {allBids[max(allBids.keys())]}")
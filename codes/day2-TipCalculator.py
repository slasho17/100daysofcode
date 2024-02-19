print("Welcome to the tip calculator.")
totalBill = int(input("What was the total bill?"))

tipsList = [10, 12, 15]
tipPercentage = 0
while (int(tipPercentage) not in tipsList):
    print("Tips can be of 10%, 12% or 15%")
    tipPercentage = int(input("What percentage do you wish to tip?"))

totalPeople = int(input("How many people will split the bill"))

tip = (tipPercentage / totalBill) * 100
individualBill = (totalBill + tip) / totalPeople

print (f"Each person shall pay R${individualBill} bucks")
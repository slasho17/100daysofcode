print("Welcome to the tip calculator.")
total_bill = int(input("What was the total bill?"))

tips_list = [10, 12, 15]
tip_percentage = 0
while (int(tip_percentage) not in tips_list):
    print("Tips can be of 10%, 12% or 15%")
    tip_percentage = int(input("What percentage do you wish to tip?"))

total_people = int(input("How many people will split the bill"))

tip = (tip_percentage / total_bill) * 100
individual_bill = (total_bill + tip) / total_people

print (f"Each person shall pay R${individual_bill} bucks")
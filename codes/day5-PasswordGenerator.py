import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to my password generator!")
numberOfLetters = int(input("How many letters do you want in your password?"))
numberOfSymbols = int(input("How many symbols do you want in your password?"))
numberOfNumbers = int(input("How many numbers do you want in your password?"))

myPassword = []
while numberOfLetters or numberOfNumbers or numberOfSymbols:
    charType = random.randint(0, 2)
    if  charType == 0:
        if numberOfLetters == 0:
            continue
        myPassword.append(letters[random.randint(0, len(letters) -1)])
        numberOfLetters = numberOfLetters -1
    elif  charType == 1:
        if numberOfSymbols == 0:
            continue
        myPassword.append(symbols[random.randint(0, len(symbols) -1)])
        numberOfSymbols = numberOfSymbols -1
    elif  charType == 2:
        if numberOfNumbers == 0:
            continue
        myPassword.append(numbers[random.randint(0, len(numbers) -1)])
        numberOfNumbers = numberOfNumbers -1
      
stringPassword = ''.join(myPassword)  
print("Your password is " + stringPassword)
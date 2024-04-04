import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to my password generator!")
number_of_letters = int(input("How many letters do you want in your password?"))
number_of_symbols = int(input("How many symbols do you want in your password?"))
number_of_numbers = int(input("How many numbers do you want in your password?"))

my_password = []
while number_of_letters or number_of_numbers or number_of_symbols:
    char_type = random.randint(0, 2)
    if  char_type == 0:
        if number_of_letters == 0:
            continue
        my_password.append(letters[random.randint(0, len(letters) -1)])
        number_of_letters = number_of_letters -1
    elif  char_type == 1:
        if number_of_symbols == 0:
            continue
        my_password.append(symbols[random.randint(0, len(symbols) -1)])
        number_of_symbols = number_of_symbols -1
    elif  char_type == 2:
        if number_of_numbers == 0:
            continue
        my_password.append(numbers[random.randint(0, len(numbers) -1)])
        number_of_numbers = number_of_numbers -1
      
string_password = ''.join(my_password)  
print("Your password is " + string_password)
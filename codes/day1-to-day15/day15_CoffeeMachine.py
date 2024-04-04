MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

def print_report():
    for resource, ammount in resources.items():
        print(f"{resource}: {ammount}")

def check_valid_option(coffee_option):
    if coffee_option == 'espresso' or coffee_option == 'latte' or coffee_option == 'cappuccino':
        return True
    else:
        return False
    
def get_payment():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    return (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)

def finish_transaction(paid, coffee_option):
    cost =  MENU[coffee_option]["cost"]
    change = paid - cost
    if change >= 0:
        print(f"Here is R${change} in change")
        resources["money"] = resources["money"] + cost
        return True
    else:
        print(f"You dont have enough money, {coffee_option} costs R${cost} and you only paid R${paid}")
        return False

def check_resources(coffee_option):
    ret = True
    for resource, ammount in resources.items():
        for ingredient, ingredient_ammount in MENU[coffee_option]["ingredients"].items():
            if resource == ingredient and ammount < ingredient_ammount:
                print(f"Sorry, we don't have {ingredient}, please fill the machine or choose another option.")
                ret = False
    return ret

def make_coffe(coffee_option):
    for resource, ammount in resources.items():
        for ingredient, ingredient_ammount in MENU[coffee_option]["ingredients"].items():
            if resource == ingredient:
                resources[ingredient] = resources[ingredient] - ingredient_ammount
    print(f"Here is your {coffee_option}, enjoy!")

                
def __main__():
    while True:
        coffee_option = input("What would you like?: (espresso, cappuccino, latte) (report or exit):\n")
        if coffee_option == "report":
            print_report()
            continue
        elif coffee_option == "exit":
            exit()
        elif check_valid_option(coffee_option):
            if check_resources(coffee_option):
                payment = get_payment()
                if finish_transaction(payment, coffee_option):
                    make_coffe(coffee_option)
        else:
            print("Invalid option.")
        
__main__()    
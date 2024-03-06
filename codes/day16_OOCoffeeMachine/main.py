from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
    
def __main__():
    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()
    print([drink.name for drink in menu.menu])
    while True:
        coffee_option = input("What would you like?: (espresso, cappuccino, latte) (report or exit):\n")
        if coffee_option == "report":
            coffee_maker.report()
            money_machine.report()
            continue
        elif coffee_option == "exit":
            exit()
        elif coffee_option in [drink.name for drink in menu.menu]:
            drink = menu.find_drink(coffee_option)
            if coffee_maker.is_resource_sufficient(drink):
                if money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)
        else:
            print("Invalid option.")
        
__main__()    
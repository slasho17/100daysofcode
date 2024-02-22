from replit import clear

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    clear()
    num1 = int(input("What is the first number?\n"))
    shouldContinue = True
    while shouldContinue:
        operationSymbol = input(f"Choose an operation: | {' | '.join(operations.keys())} |\n")
        num2 = int(input("What is the next number?\n"))
        answer = operations[operationSymbol](num1, num2)
        print(f"{num1} {operationSymbol} {num2} = {answer}")
        shouldContinue = input("Type y to continue calculating, or n to stop") == "y"
        num1 = answer
        if(shouldContinue == False):
            calculator()
            
calculator()
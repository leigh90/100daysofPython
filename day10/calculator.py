from art import logo

# add
def add(n1,n2):
    return n1 + n2
# subtract
def subtract(n1,n2):
    return n1 - n2

# multiply
def multiply(n1,n2):
    return n1 * n2

# divide
def divide(n1,n2):
    return n1 // n2

operations = {
    "+":add,
     "-":subtract, 
     "*":multiply, 
     "//":divide
}

def calculator():
    print(logo)
    num1 = float(input("Whats the first number? "))
    for symbol in operations:
        print(symbol)
    should_continue = True
 
    while should_continue:
        operation_symbol = input("Choose an operation from the line above ")
        num2 = float(input("Whats the second number? "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(F"Type 'y' to continue calculating with {answer} or 'n' to start a new calculation: ") == 'y':
            num1 = answer
        else:
            should_continue=False
            calculator() #recursion since its calling itself to start again

calculator()
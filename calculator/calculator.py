
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    should_continue = True
    n1 = float(input("What is the first number? "))

    while should_continue:
        for operation in operations:
            print(operation)
        operation_decider = input("Pick an operation")
        n2 = float(input("What is the second number ?"))
        res = operations[operation_decider](n1, n2)
        print(f"{n1} {operation_decider} {n2} = {res}")

        choice = input(f"Type 'y' to continue calculating with {res}, or type anything else to start a new calculation: ")
        if choice == "y":
            n1 = res
        else:
            should_continue = False
            print("\n" * 20)
            calculator()
calculator()

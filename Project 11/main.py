import art

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
    "/": divide
}


def calculator():
    print(art.logo)
    should_run = True
    number_1 = float(input("Enter first number: "))

    while should_run:

        print("+\n", "-\n", "*\n", "/")

        operation_symbol = input("Pick an operation: ")

        if operation_symbol not in operation_symbol:
            print("Invalid operation")
        else:
            number_2 = float(input("Enter the next number: "))

            result_1 = operations[operation_symbol](number_1, number_2)
            print(f"{number_1} {operation_symbol} {number_2} = {result_1}")
            choice = input(f"Type 'y' to continue calculating with {result_1}, or type 'n' to start a new calculation: ").lower()
            if choice == "y":
                number_1 = result_1
            elif choice == "n":
                should_run = False
                print("\n" * 20)
                calculator()
            else:
                print("Please enter either 'y' or 'n'")

calculator()
from art import logo

print(logo)


def add(n1, n2):
    return n1 + n2


def substract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide,
}


def calculator():
    num1 = float(input("What's the first number ? \n"))
    for operation in operations:
        print(operation)

    calculation_finished = True
    while calculation_finished:
        operation_symbol = input("Pick an operation")
        num2 = float(input("What's the next number ? \n"))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if (
            input(
                f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation"
            )
            == "y"
        ):
            num1 = answer
        else:
            calculation_finished = False
            calculator()


calculator()

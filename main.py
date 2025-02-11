import art
print(art.logo)

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operators = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    should= True
    num1 = float(input("What is the first number?: "))

    while should:
        for symbol in operators:
            print(symbol)
        symbol = input("Pick an operation: ")
        num2 = float(input("What is the next number?: "))
        answer = operators[symbol](num1, num2)
        print(f"{num1} {symbol} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

        if choice == "y":
            num1 = answer
        else:
            should = False
            print("\n" * 20)
            calculator()


calculator()







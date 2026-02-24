import os

HISTORY_FILE = "history.txt"


class Calculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b


def save_history(record):
    with open(HISTORY_FILE, "a") as file:
        file.write(record + "\n")


def show_history():

    if not os.path.exists(HISTORY_FILE):
        print("\nNo history found.\n")
        return

    with open(HISTORY_FILE, "r") as file:
        content = file.read()

        if content.strip() == "":
            print("\nHistory is empty.\n")
        else:
            print("\n=== History ===")
            print(content)


def clear_history():

    with open(HISTORY_FILE, "w") as file:
        file.write("")

    print("\nHistory cleared.\n")


def parse_input(user_input):

    parts = user_input.split()

    if len(parts) != 3:
        raise ValueError("Format must be: number operator number")

    num1 = float(parts[0])
    operator = parts[1]
    num2 = float(parts[2])

    return num1, operator, num2


def perform_calculation(calc, num1, operator, num2):

    operations = {
        "+": calc.add,
        "-": calc.subtract,
        "*": calc.multiply,
        "/": calc.divide
    }

    if operator not in operations:
        raise ValueError("Invalid operator")

    result = operations[operator](num1, num2)

    return result


def main():

    calculator = Calculator()

    print("=== Advanced Command Line Calculator ===")
    print("Examples: 5 + 3")
    print("Commands:")
    print("history  -> Show history")
    print("clear    -> Clear history")
    print("exit     -> Quit\n")

    while True:

        user_input = input("Enter command: ").strip()

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        elif user_input.lower() == "history":
            show_history()

        elif user_input.lower() == "clear":
            clear_history()

        else:

            try:
                n1, op, n2 = parse_input(user_input)

                result = perform_calculation(calculator, n1, op, n2)

                record = f"{n1} {op} {n2} = {result}"

                print("Result:", result)

                save_history(record)

            except Exception as e:
                print("Error:", e)


if __name__ == "__main__":
    main()
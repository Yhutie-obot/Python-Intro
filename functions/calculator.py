def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y


completed_calculation = False  # Flag to track if a calculation was completed

while True:
    if not completed_calculation:
        print("Options:")
        print("\t\tEnter 1 for addition")
        print("\t\tEnter 2 for subtraction")
        print("\t\tEnter 3 for multiplication")
        print("\t\tEnter 4 for division")
        print("\t\tEnter 'exit' to end the program")

    user_input = input(": ")

    if user_input == "exit":
        break
    elif user_input in ("1", "2", "3", "4"):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if user_input == "1":
                print("Result: ", add(num1, num2))
            elif user_input == "2":
                print("Result: ", subtract(num1, num2))
            elif user_input == "3":
                print("Result: ", multiply(num1, num2))
            elif user_input == "4":
                if num2 == 0:
                    print("Result: Cannot divide by zero")
                else:
                    print("Result: ", divide(num1, num2))

            completed_calculation = True  # Set the flag to indicate successful calculation
        except ValueError:
            print("Invalid input. Please enter numeric values.")
    else:
        print("Invalid input. Please choose a valid option.")

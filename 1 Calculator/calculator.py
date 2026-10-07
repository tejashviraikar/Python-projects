# ----------------------------------------
# Python Calculator Application
# ----------------------------------------

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error! Division by zero is not allowed."
    return a / b


def modulus(a, b):
    if b == 0:
        return "Error! Division by zero is not allowed."
    return a % b


def power(a, b):
    return a ** b


def display_menu():
    print("\n========== PYTHON CALCULATOR ==========")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")
    print("6. Power (^)")
    print("7. Exit")
    print("=======================================\n")


while True:

    display_menu()

    try:
        choice = int(input("Enter your choice (1-7): "))

        if choice == 7:
            print("\nThank you for using the Calculator!")
            break

        if choice not in range(1, 7):
            print("Invalid choice! Please select between 1 and 7.")
            continue

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == 1:
            print("Result =", add(num1, num2))

        elif choice == 2:
            print("Result =", subtract(num1, num2))

        elif choice == 3:
            print("Result =", multiply(num1, num2))

        elif choice == 4:
            print("Result =", divide(num1, num2))

        elif choice == 5:
            print("Result =", modulus(num1, num2))

        elif choice == 6:
            print("Result =", power(num1, num2))

    except ValueError:
        print("Invalid Input! Please enter numeric values.")

    except Exception as e:
        print("Something went wrong:", e)
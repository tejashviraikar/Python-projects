import csv
import os

FILE_NAME = "expenses.csv"


# ----------------------------
# Create CSV File
# ----------------------------
def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Description", "Amount"])


# ----------------------------
# Add Expense
# ----------------------------
def add_expense():
    date = input("Enter Date (YYYY-MM-DD): ")
    category = input("Enter Category: ")
    description = input("Enter Description: ")

    try:
        amount = float(input("Enter Amount: "))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

        with open(FILE_NAME, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([date, category, description, amount])

        print("Expense added successfully!")

    except ValueError:
        print("Invalid amount.")


# ----------------------------
# View Expenses
# ----------------------------
def view_expenses():
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        print("\n========== EXPENSES ==========")

        for row in reader:
            print("{:<12} {:<15} {:<20} {}".format(*row))

        print("===============================")


# ----------------------------
# Total Expenses
# ----------------------------
def total_expenses():

    total = 0

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            total += float(row["Amount"])

    print(f"\nTotal Expense: ₹{total:.2f}")


# ----------------------------
# Category Wise Total
# ----------------------------
def category_total():

    totals = {}

    with open(FILE_NAME, "r") as file:

        reader = csv.DictReader(file)

        for row in reader:

            category = row["Category"]
            amount = float(row["Amount"])

            totals[category] = totals.get(category, 0) + amount

    print("\n====== CATEGORY TOTALS ======")

    for category, amount in totals.items():
        print(f"{category:<15} ₹{amount:.2f}")

    print("=============================")


# ----------------------------
# Menu
# ----------------------------
def menu():

    print("\n========== EXPENSE TRACKER ==========")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Category-wise Total")
    print("5. Exit")
    print("=====================================")


# ----------------------------
# Main Program
# ----------------------------
def main():

    initialize_file()

    while True:

        menu()

        try:

            choice = int(input("Enter your choice: "))

            if choice == 1:
                add_expense()

            elif choice == 2:
                view_expenses()

            elif choice == 3:
                total_expenses()

            elif choice == 4:
                category_total()

            elif choice == 5:
                print("Thank you for using Expense Tracker!")
                break

            else:
                print("Invalid choice.")

        except ValueError:
            print("Please enter a valid number.")


if __name__ == "__main__":
    main()
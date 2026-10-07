import random


# ----------------------------
# Roll Dice Function
# ----------------------------
def roll_dice(number_of_dice):
    rolls = []

    for _ in range(number_of_dice):
        rolls.append(random.randint(1, 6))

    return rolls


# ----------------------------
# Display Menu
# ----------------------------
def display_menu():
    print("\n" + "=" * 40)
    print("        DICE ROLLER SIMULATOR")
    print("=" * 40)


# ----------------------------
# Main Program
# ----------------------------
def main():
    display_menu()

    while True:

        try:
            number = int(input("\nHow many dice do you want to roll? "))

            if number <= 0:
                print("Please enter a number greater than 0.")
                continue

            result = roll_dice(number)

            print("\n🎲 Rolling Dice...\n")

            for i, value in enumerate(result, start=1):
                print(f"Dice {i}: {value}")

            print(f"\nTotal = {sum(result)}")

            choice = input("\nRoll again? (y/n): ").lower()

            if choice != "y":
                print("\n👋 Thanks for playing!")
                break

        except ValueError:
            print("Invalid input! Please enter a valid number.")


if __name__ == "__main__":
    main()
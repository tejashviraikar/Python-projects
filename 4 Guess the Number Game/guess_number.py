import random


# ----------------------------
# Play Game
# ----------------------------
def play_game():
    secret_number = random.randint(1, 100)
    attempts = 0

    print("\n🎯 I have selected a number between 1 and 100.")
    print("Can you guess it?")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue

            if guess < secret_number:
                print("📉 Too Low! Try again.")

            elif guess > secret_number:
                print("📈 Too High! Try again.")

            else:
                print("\n🎉 Congratulations!")
                print(f"You guessed the correct number: {secret_number}")
                print(f"Total Attempts: {attempts}")
                break

        except ValueError:
            print("Invalid input! Please enter a valid number.")


# ----------------------------
# Main Program
# ----------------------------
def main():
    print("=" * 40)
    print("      GUESS THE NUMBER GAME")
    print("=" * 40)

    while True:
        play_game()

        play_again = input("\nDo you want to play again? (y/n): ").lower()

        if play_again != "y":
            print("\n👋 Thanks for playing!")
            break


if __name__ == "__main__":
    main()
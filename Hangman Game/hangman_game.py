# Build a hangman game where players guess a word by suggesting letters. The game continues until the player correctly guesses the word or runs out of attempts.

import random  # Import the random module to select a random word

# List of words for the Hangman game
word_list = ['python', 'hangman', 'programming', 'developer', 'algorithm']

def choose_word(word_list):
    """Randomly select a word from the word list."""
    return random.choice(word_list)

def display_current_state(word, guessed_letters):
    """Display the current state of the guessed word with correct letters revealed."""
    current_state = ''.join([letter if letter in guessed_letters else '_' for letter in word])
    return current_state

def hangman():
    """Main function to play the Hangman game."""
    # Choose a random word for the player to guess
    word_to_guess = choose_word(word_list)
    guessed_letters = set()  # Set to store guessed letters
    attempts_left = 6  # Number of attempts allowed

    print("Welcome to Hangman!")
    print("Try to guess the word!")

    # Game loop
    while attempts_left > 0:
        # Display the current state of the word
        current_state = display_current_state(word_to_guess, guessed_letters)
        print(f"Current state: {current_state}")
        
        # Check if the player has guessed the entire word
        if '_' not in current_state:
            print("Congratulations! You've guessed the word!")
            break

        # Get the player's guess
        guess = input("Guess a letter: ").lower()

        # Validate the player's guess
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        # Check if the letter was already guessed
        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue

        # Add the guessed letter to the set of guessed letters
        guessed_letters.add(guess)

        # Check if the guessed letter is in the word
        if guess in word_to_guess:
            print("Correct!")
        else:
            print("Incorrect!")
            attempts_left -= 1
            print(f"Attempts left: {attempts_left}")

    # If the player runs out of attempts
    if attempts_left == 0:
        print(f"Sorry, you've run out of attempts. The word was '{word_to_guess}'.")

# Start the Hangman game
hangman()

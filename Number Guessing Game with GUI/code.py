import tkinter as tk
import random

# Function to start the game
def start_game():
    global number_to_guess
    min_val = int(min_entry.get())
    max_val = int(max_entry.get())
    number_to_guess = random.randint(min_val, max_val)  # Generate random number to guess
    feedback_label.config(text="Game started! Guess a number.")  # Feedback message
    guess_button.config(state="normal")  # Enable the guess button

# Function to check the guessed number
def check_guess():
    guess = int(guess_entry.get())
    if guess < number_to_guess:
        feedback_label.config(text="Too low! Try again.")
    elif guess > number_to_guess:
        feedback_label.config(text="Too high! Try again.")
    else:
        feedback_label.config(text="Correct! You guessed the number!")

# Set up the main window
root = tk.Tk()
root.title("Number Guessing Game")

# GUI elements
min_label = tk.Label(root, text="Enter Minimum Number:")
min_label.pack()
min_entry = tk.Entry(root)
min_entry.pack()

max_label = tk.Label(root, text="Enter Maximum Number:")
max_label.pack()
max_entry = tk.Entry(root)
max_entry.pack()

start_button = tk.Button(root, text="Start Game", command=start_game)
start_button.pack()

feedback_label = tk.Label(root, text="Set the range and start the game.")
feedback_label.pack()

guess_label = tk.Label(root, text="Enter your guess:")
guess_label.pack()
guess_entry = tk.Entry(root)
guess_entry.pack()

guess_button = tk.Button(root, text="Submit Guess", command=check_guess, state="disabled")
guess_button.pack()

# Run the application
root.mainloop()

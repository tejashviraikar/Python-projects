import random  # Import the random module to allow the computer to make a random choice

def play_game():
    """Function to play a single round of Rock, Paper, Scissors"""
    print("Welcome to Rock, Paper, Scissors!")

    # Define the possible moves
    moves = {1: "Rock", 2: "Paper", 3: "Scissors"}

    # Get the player's move
    player_move = int(input("Select your move (1 for Rock, 2 for Paper, 3 for Scissors): "))

    # Validate player input
    if player_move not in moves:
        print("Invalid input. Please enter 1, 2, or 3.")
        return

    # Randomly select the computer's move
    computer_move = random.randint(1, 3)

    # Display the moves
    print(f"Computer chose {moves[computer_move]}. You chose {moves[player_move]}.")

    # Determine the game outcome using conditional statements
    if player_move == computer_move:
        print("It's a tie!")
    elif (player_move == 1 and computer_move == 3) or \
         (player_move == 2 and computer_move == 1) or \
         (player_move == 3 and computer_move == 2):
        print("You win!")
    else:
        print("You lose!")

# Start the game
play_game()

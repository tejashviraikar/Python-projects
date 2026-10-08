# Initialize the Tic-Tac-Toe board as a 3x3 matrix with empty strings
board = [[' ' for _ in range(3)] for _ in range(3)]

def print_board():
    """Print the current state of the Tic-Tac-Toe board."""
    print("\nCurrent state:")
    for row in range(3):
        print("|".join(board[row]))
        if row < 2:
            print("-----")

def check_winner(player):
    """Check if the given player has won the game."""
    # Check rows and columns
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def check_draw():
    """Check if the game is a draw (i.e., all cells are filled with no winner)."""
    return all(board[row][col] != ' ' for row in range(3) for col in range(3))

def make_move(player):
    """Prompt the current player to make a move and update the board."""
    while True:
        try:
            move = input(f"Player {player}, enter your move (row and column): ")
            row, col = map(int, move.split(","))
            if board[row - 1][col - 1] == ' ':
                board[row - 1][col - 1] = player
                break
            else:
                print("This cell is already occupied. Please try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter row and column as two numbers separated by a comma (e.g., 1, 2).")

def play_game():
    """Main function to handle the flow of the Tic-Tac-Toe game."""
    current_player = 'X'
    print("Welcome to Tic-Tac-Toe!")

    while True:
        print_board()
        make_move(current_player)

        # Check if the current player has won
        if check_winner(current_player):
            print_board()
            print(f"Player {current_player} wins!")
            break

        # Check if the game is a draw
        if check_draw():
            print_board()
            print("It's a draw!")
            break

        # Switch players
        current_player = 'O' if current_player == 'X' else 'X'

# Start the Tic-Tac-Toe game
play_game()

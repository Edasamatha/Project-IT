# Project 17: Tic-Tac-Toe Game
# Two-player console version of Tic-Tac-Toe

# Step 1: Function to display the board
def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))      # Print each row with separators
        print("-" * 9)
    print("\n")

# Step 2: Function to check if a player has won
def check_winner(board, player):
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:  # row
            return True
        if board[0][i] == board[1][i] == board[2][i] == player:  # column
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:  # top-left to bottom-right
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:  # top-right to bottom-left
        return True

    return False

# Step 3: Function to check for a draw
def is_draw(board):
    for row in board:
        if " " in row:
            return False
    return True

# Step 4: Get player input
def get_move(player):
    while True:
        try:
            row = int(input(f"Player {player} - Enter row (0-2): "))
            col = int(input(f"Player {player} - Enter column (0-2): "))
            if row in range(3) and col in range(3):
                return row, col
            else:
                print("Please enter numbers between 0 and 2.")
        except ValueError:
            print("Invalid input. Please enter numeric values.")

# Step 5: Main game loop
def main():
    board = [[" " for _ in range(3)] for _ in range(3)]  # 3x3 grid
    current_player = "X"

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        row, col = get_move(current_player)

        # Check if the cell is already filled
        if board[row][col] != " ":
            print("That spot is already taken. Try again.")
            continue

        # Place the player's symbol
        board[row][col] = current_player
        print_board(board)

        # Check for winner
        if check_winner(board, current_player):
            print(f"🎉 Player {current_player} wins!")
            break

        # Check for draw
        if is_draw(board):
            print("It's a draw! 🤝")
            break

        # Switch turns
        current_player = "O" if current_player == "X" else "X"

# Run the game
if __name__ == "__main__":
    main()

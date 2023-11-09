import random

# Define the Tic-Tac-Toe board
board = [" " for _ in range(9)]

# Function to print the Tic-Tac-Toe board
def print_board(board):
    for i in range(0, 9, 3):
        print(f"{board[i]} | {board[i+1]} | {board[i+2]}")
        if i < 6:
            print("---------")

# Function to check if a player has won
def check_winner(board, player):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]

    for combo in winning_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

# Function to check if the board is full
def is_board_full(board):
    return " " not in board

# Function to make a move for the AI player using Minimax
def minimax(board, depth, maximizing_player):
    if check_winner(board, "X"):
        return -1
    if check_winner(board, "O"):
        return 1
    if is_board_full(board):
        return 0

    if maximizing_player:
        max_eval = float("-inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                eval = minimax(board, depth + 1, False)
                board[i] = " "
                max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                eval = minimax(board, depth + 1, True)
                board[i] = " "
                min_eval = min(min_eval, eval)
        return min_eval

# Function to find the best move for the AI player
def find_best_move(board):
    best_move = -1
    best_eval = float("-inf")
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            eval = minimax(board, 0, False)
            board[i] = " "
            if eval > best_eval:
                best_eval = eval
                best_move = i
    return best_move

# Main game loop
while True:
    print_board(board)

    # Human player's turn
    while True:
        try:
            move = int(input("Enter your move (0-8): "))
            if 0 <= move <= 8 and board[move] == " ":
                board[move] = "X"
                break
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Enter a number between 0 and 8.")

    # Check if the human player has won
    if check_winner(board, "X"):
        print_board(board)
        print("You win!")
        break

    # Check if the board is full (a tie)
    if is_board_full(board):
        print_board(board)
        print("It's a tie!")
        break

    # AI player's turn
    ai_move = find_best_move(board)
    board[ai_move] = "O"

    # Check if the AI player has won
    if check_winner(board, "O"):
        print_board(board)
        print("AI wins!")
        break
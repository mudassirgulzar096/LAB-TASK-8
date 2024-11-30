import math

# Function to check if a player has won
def check_winner(board, player):
    for i in range(3):
        # Check rows and columns
        if all([board[i][j] == player for j in range(3)]) or all([board[j][i] == player for j in range(3)]):
            return True
    # Check diagonals
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

# Function to check if the board is full
def is_board_full(board):
    return all(board[i][j] != '_' for i in range(3) for j in range(3))

# Minimax algorithm
def min_max(board, depth, is_maximizing):
    if check_winner(board, 'A'):  # AI wins
        return 10 - depth
    if check_winner(board, 'B'):  # Opponent wins
        return depth - 10
    if is_board_full(board):  # Draw
        return 0

    if is_maximizing:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = 'A'  # AI's move
                    best = max(best, min_max(board, depth + 1, False))
                    board[i][j] = '_'
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = 'B'  # Opponent's move
                    best = min(best, min_max(board, depth + 1, True))
                    board[i][j] = '_'
        return best

# Function to find the best move for AI
def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                board[i][j] = 'A'  # AI's move
                move_val = min_max(board, 0, False)
                board[i][j] = '_'
                if move_val > best_val:
                    best_val = move_val
                    best_move = (i, j)
    return best_move

# Test the function with a board using 'A', 'B', and '_'
board = [
    ['A', 'B', 'A'],
    ['', 'B', ''],
    ['A', '', '']
]

best_move = find_best_move(board)
print(f"Best move for AI: Row {best_move[0]}, Column {best_move[1]}")
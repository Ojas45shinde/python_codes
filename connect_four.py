

import numpy as np

ROW_COUNT = 6
COLUMN_COUNT = 7
EMPTY = 0
PLAYER_1 = 1
PLAYER_2 = 2

def create_board():
    return np.zeros((ROW_COUNT, COLUMN_COUNT), int)

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def is_valid_location(board, col):
    return board[ROW_COUNT-1][col] == EMPTY

def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == EMPTY:
            return r

def print_board(board):
    print(np.flip(board, 0))

def winning_move(board, piece):
    # Check horizontal locations
    for col in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][col] == piece and board[r][col+1] == piece and board[r][col+2] == piece and board[r][col+3] == piece:
                return True

    # Check vertical locations
    for col in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-3):
            if board[r][col] == piece and board[r+1][col] == piece and board[r+2][col] == piece and board[r+3][col] == piece:
                return True

    # Check positively sloped diagonals
    for col in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT-3):
            if board[r][col] == piece and board[r+1][col+1] == piece and board[r+2][col+2] == piece and board[r+3][col+3] == piece:
                return True

    # Check negatively sloped diagonals
    for col in range(COLUMN_COUNT-3):
        for r in range(3, ROW_COUNT):
            if board[r][col] == piece and board[r-1][col+1] == piece and board[r-2][col+2] == piece and board[r-3][col+3] == piece:
                return True

def play_game():
    board = create_board()
    game_over = False
    turn = 0

    print_board(board)

    while not game_over:
        if turn == 0:
            col = int(input("Player 1's turn (0-6): "))
            piece = PLAYER_1
        else:
            col = int(input("Player 2's turn (0-6): "))
            piece = PLAYER_2

        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, piece)

            if winning_move(board, piece):
                print_board(board)
                print(f"Player {piece} wins!")
                game_over = True

            print_board(board)

            turn += 1
            turn = turn % 2
        else:
            print("Column full! Choose another column.")

if __name__ == "__main__":
    play_game()

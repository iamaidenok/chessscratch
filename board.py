#Board code
import numpy as np
player=1
turn=0
row=0
column=0
winner=0
def determine_turn():
    global turn
    global player
    turn+=1
    if turn%2 != 0:
        player = 2
    else:
        player = 1

def prompt_user():
    global row
    global column
    global pick_piece
    global new_square
    global new_row
    global new_column
    pick_piece = input("Pick a piece to move by inputting the square it's on\n")
    pick_piece = list(pick_piece)
    if pick_piece[0] == 'a':
        column = 0
    elif pick_piece[0] == 'b':
        column = 1
    elif pick_piece[0] == 'c':
        column = 2
    elif pick_piece[0] == 'd':
        column = 3
    elif pick_piece[0] == 'e':
        column = 4
    elif pick_piece[0] == 'f':
        column = 5
    elif pick_piece[0] == 'g':
        column = 6
    elif pick_piece[0] == 'h':
        column = 7   
    if pick_piece[1] == '1':
        row = 7
    elif pick_piece[1] == '2':
        row = 6
    elif pick_piece[1] == '3':
        row = 5
    elif pick_piece[1] == '4':
        row = 4
    elif pick_piece[1] == '5':
        row = 3
    elif pick_piece[1] == '6':
        row = 2
    elif pick_piece[1] == '7':
        row = 1
    elif pick_piece[1] == '8':
        row = 0
    new_square = input("Pick a square to move the piece\n")
    new_square = list(new_square)
    if new_square[0] == 'a':
        new_column = 0
    elif new_square[0] == 'b':
        new_column = 1
    elif new_square[0] == 'c':
        new_column = 2
    elif new_square[0] == 'd':
        new_column = 3
    elif new_square[0] == 'e':
        new_column = 4
    elif new_square[0] == 'f':
        new_column = 5
    elif new_square[0] == 'g':
        new_column = 6
    elif new_square[0] == 'h':
        new_column = 7   
    if new_square[1] == '1':
        new_row = 7
    elif new_square[1] == '2':
        new_row = 6
    elif new_square[1] == '3':
        new_row = 5
    elif new_square[1] == '4':
        new_row = 4
    elif new_square[1] == '5':
        new_row = 3
    elif new_square[1] == '6':
        new_row = 2
    elif new_square[1] == '7':
        new_row = 1
    elif new_square[1] == '8':
        new_row = 0
#if board[row][column] == '00':
def moving_pieces():
    global chosen_piece
    chosen_piece = board[row][column]
    board[row][column] = '00'
    board[new_row][new_column] = chosen_piece
    print(board)

board = np.array([['BR', 'BN', 'BB', 'BQ', 'BK', 'BB', 'BN', 'BR'], ['BP', 'BP', 'BP', 'BP','BP', 'BP', 'BP', 'BP'], ['00','00','00','00','00','00','00','00'], ['00','00','00','00','00','00','00','00'], ['00','00','00','00','00','00','00','00'], ['00','00','00','00','00','00','00','00'], ['WP', 'WP', 'WP', 'WP','WP', 'WP', 'WP', 'WP'], ['WR', 'WN', 'WB', 'WQ', 'WK', 'WB', 'WN', 'WR']], dtype = object)
print(board)
while True:
    prompt_user()
    moving_pieces()
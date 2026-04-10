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
    for i in range(8):
        indicator = ord(pick_piece[0])-97
        if indicator == i:
            column = i
            break   
    for i in range(8):
        row_options = [7,6,5,4,3,2,1,0]
        indicator = ord(pick_piece[1])-49
        if indicator == i:
            row = row_options[i]
            break
    new_square = input("Pick a square to move the piece\n")
    new_square = list(new_square)
    for i in range(8):
        indicator = ord(new_square[0])-97
        if indicator == i:
            new_column = i
            break
    for i in range(8):
        row_options = [7,6,5,4,3,2,1,0]
        indicator = ord(new_square[1])-49
        if indicator == i:
            new_row = row_options[i]
            break
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
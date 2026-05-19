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
        player = 'W'
    else:
        player = 'B'

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

def moving_pieces():
    global chosen_piece
    chosen_piece = board[row][column]
    chosenpiece = list(chosen_piece)
    if chosenpiece[0] != player:
        while True: #code that makes user pick their own piece
            print("Pick one of YOUR pieces")
            prompt_user()
            chosen_piece = board[row][column]
            chosenpiece = list(chosen_piece)
            if chosenpiece[0] == player:
                break
    if chosenpiece[1] == 'P':
        pawn()
    #elif chosenpiece[1] == 'R':
        #function for rooks
    #elif chosenpiece[1] == 'N':
        #function for knights
    #elif chosenpiece[1] == 'B':
        #function for bishops
    #elif chosenpiece[1] == 'Q':
        #function for queens(just mash bishop and rook)
    #elif chosenpiece[1] == 'K':
        #function for king(include not being able to move into check and checkmate)
    #board[row][column] = '00'
    #board[new_row-1][new_column] = chosen_piece
    #print(board)
def pawn():
    while True:
        if player == 'W':
            if new_row == row-1 and new_column == column:
                break
            elif row == 6 and new_row == row-2 and new_column == column:
                break
            else:
                print("Pick a legal move")
                prompt_user()
        if player == 'B':
            if new_row == row+1 and new_column == column:
                break            
            elif row == 1 and new_row == row+2 and new_column == column: 
                break
            else:              
                print("Pick a legal move")
                prompt_user()
    board[row][column] = '00'
    board[new_row][new_column] = chosen_piece
    print(board)

board = np.array([['BR', 'BN', 'BB', 'BQ', 'BK', 'BB', 'BN', 'BR'], ['BP', 'BP', 'BP', 'BP','BP', 'BP', 'BP', 'BP'], ['00','00','00','00','00','00','00','00'], ['00','00','00','00','00','00','00','00'], ['00','00','00','00','00','00','00','00'], ['00','00','00','00','00','00','00','00'], ['WP', 'WP', 'WP', 'WP','WP', 'WP', 'WP', 'WP'], ['WR', 'WN', 'WB', 'WQ', 'WK', 'WB', 'WN', 'WR']], dtype = object)
print(board)
while True:
    determine_turn()
    prompt_user()
    moving_pieces()

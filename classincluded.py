import numpy as np

class Board:
    def __init__(self):
        self.grid = np.array([
            ['BR','BN','BB','BQ','BK','BB','BN','BR'], 
            ['BP','BP','BP','BP','BP','BP','BP','BP'], 
            ['00','00','00','00','00','00','00','00'], 
            ['00','00','00','00','00','00','00','00'], 
            ['00','00','00','00','00','00','00','00'], 
            ['00','00','00','00','00','00','00','00'], 
            ['WP','WP','WP','WP','WP','WP','WP','WP'], 
            ['WR','WN','WB','WQ','WK','WB','WN','WR']
            ], dtype = object)
    def move_piece(self, start_row, start_column, end_row, end_column):
        r1, c1 = self.translating_grid(start_row, start_column)
        r2, c2 = self.translating_grid(end_row, end_column)
        piece = self.grid[r1][c1]
        self.grid[r1][c1] = '00'
        self.grid[r2][c2] = piece
        self.print_board()

    def get_piece(self, row, column):
        r, c = self.translating_grid(row, column)
        return self.grid[r][c]

    def print_board(self):
        print(self.grid)

    def translating_grid(self,column, row):
        column = ord(column)-97
        row_options = [7,6,5,4,3,2,1,0]
        rows = [1,2,3,4,5,6,7,8]
        index = rows.index(row)
        row = row_options[index]
        return row, column

#later add way to just add a square like a7 or smth instead of row column
board = Board()
print(board.translating_grid('a',7))


print(board.get_piece('b',7))
board.move_piece('a', 7, 'a', 6)
class Pawn: #en passant might lowk fuck my crack
    def __init__(self, color):
        self.color = color
    def move_collector(self, board, row, column):
        legal_moves = []
        if self.color == 'W':
            if board[row-1][column] == '00':
                legal_moves.append((row-1,column))
            if row == 6 and board[row-1][column] == '00' and board[row-2][column] == '00':
                legal_moves.append((row-2,column))
        else:
            if board[row+1][column] == '00':
                legal_moves.append((row+1,column))
            if row == 1 and board[row+1][column] == '00' and board[row+2][column] == '00':
                legal_moves.append((row+2,column))
        return legal_moves
'''pawn = Pawn('W')
moves = pawn.move_collector(board.grid,1,0)
print(moves)'''
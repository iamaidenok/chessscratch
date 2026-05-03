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
    def move_piece(self, start, end):
        r1, c1 = self.translating_grid(start)
        r2, c2 = self.translating_grid(end)
        piece = self.grid[r1][c1]
        self.grid[r1][c1] = '00'
        self.grid[r2][c2] = piece
        self.print_board()

    def get_piece(self, square):
        r, c = self.translating_grid(square)
        return self.grid[r][c]

    def print_board(self):
        print(self.grid)

    '''def translating_grid(self,column, row):
        column = ord(column)-97
        row_options = [7,6,5,4,3,2,1,0]
        rows = [1,2,3,4,5,6,7,8]
        index = rows.index(row)
        row = row_options[index]
        return row, column'''

    def translating_grid(self,square):
        square = list(square)
        column = ord(square[0])-97
        row_options = [7,6,5,4,3,2,1,0]
        rows = [1,2,3,4,5,6,7,8]
        index = rows.index(int(square[1]))
        row = row_options[index]
        return row, column
    
    def opp_translating_grid(self, row, column):
        rows = chr(column + 97)
        column = 8 - row
        return rows + str(column)
    #lowk might need function to change square back into row column format
board = Board()
'''print(board.translating_grid('a7'))


print(board.get_piece('b7'))
board.move_piece('a7', 'a6')'''
class Pawn: #en passant might lowk fuck my crack
    def __init__(self, color):
        self.color = color
    def move_collector(self, board, square):
        row, column = board.translating_grid(square)
        legal_moves = []
        if self.color == 'W':
            if board.grid[row-1][column] == '00':
                legal_moves.append((row-1,column))
            if row == 6 and board.grid[row-1][column] == '00' and board.grid[row-2][column] == '00':
                legal_moves.append((row-2,column))
        else:
            if board.grid[row+1][column] == '00':
                legal_moves.append((row+1,column))
            if row == 1 and board.grid[row+1][column] == '00' and board.grid[row+2][column] == '00':
                legal_moves.append((row+2,column))
        legal_moves_translated = []
        for i in legal_moves:
            row = i[0]
            column = i[1]
            square = board.opp_translating_grid(row,column)
            legal_moves_translated.append(square)
        return legal_moves_translated
pawn = Pawn('B')
moves = pawn.move_collector(board,'a7')
print(moves)
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
        piece = self.grid[start_row][start_column]
        self.grid[start_row][start_column] = '00'
        self.grid[end_row][end_column] = piece
        print(self.grid)

    def get_piece(self, row, column):
        return self.grid[row][column]  

#later add way to just add a square like a7 or smth instead of row column
board = Board()
print(board.get_piece(1,0))
board.move_piece(1, 0, 2, 0)
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
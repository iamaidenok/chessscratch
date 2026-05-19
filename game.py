from board import Board
from pawn import Pawn

class Game: 
    #should have turns, ask player for moves, check if move is legal, special rules, 
    def __init__(self):
        self.board = Board()
        self.turn = 'W'

    def determine_turn(self):
        if self.turn == 'W':
            self.turn = 'B'
        else: 
            self.turn = 'W'
    
    def ask_player_for_moves(self):
        self.board.print_board()
        start = input("Pick a piece: \n")
        piece = self.board.get_piece(start)
        
        if piece[0] != self.turn:
            print("pick ur own piece fn")
            return
        
        #pawn
        if piece[1] == "P":
            pawn = Pawn(self.turn)
            legal_moves = pawn.move_collector(self.board,start)
            print("Your legal moves are: ", legal_moves)
            end = input("Where you moving it? \n")
            if end in legal_moves:
                self.board.move_piece(start,end)
                self.determine_turn()
            else:
                print('pick a legal move fn')
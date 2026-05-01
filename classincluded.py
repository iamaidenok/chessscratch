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
        
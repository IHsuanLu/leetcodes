# try putting queens at each of the postion in every "row"
# keep track of which "cols", "pos_diag", and "neg_diag" we placed queens in using "set()"
# patterns of neg_diag and pos_diag
#   neg_diag => (row - col = $constant)
#   pos_diag => (row + col = $constant)
from ast import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        pos_diag = set() # row + col = $constant
        neg_diag = set() # row - col = $constant
        
        res = []
        board = [["."] * n for i in range(n)]
        
        def backtrack(cur_row):
            if cur_row >= n:
                copy = ["".join(r) for r in board]
                # [['.', '.', '.', '.'], ['.', '.', '.', '.'], ['.', '.', '.', '.'], ['.', '.', '.', '.']] => ['....', '....', '....', '....']
                res.append(copy)
                return
            
            # try every position (col) in the current row
            for col in range(n):
                if (col in cols or (cur_row + col) in pos_diag or (cur_row - col) in neg_diag):
                    continue # skip the position
                
                # allow to place, update all of the sets
                cols.add(col)
                pos_diag.add(cur_row + col)
                neg_diag.add(cur_row - col)
                
                # update the board
                board[cur_row][col] = "Q"
                
                backtrack(cur_row + 1)
                
                # clean up
                cols.remove(col)
                pos_diag.remove(cur_row + col)
                neg_diag.remove(cur_row - col)
                
                # update the board
                board[cur_row][col] = "."
                
        backtrack(0)
        return res
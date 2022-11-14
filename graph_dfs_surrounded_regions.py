# reverse thinking
# capture surronded region = capture everything except unsurrounded region

from ast import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        num_row, num_col = len(board), len(board[0])
            
        def dfs(row, col):
            # out of bound
            if row < 0 or col < 0 or row >= num_row or col >= num_col:
                return
            
            if board[row][col] != "O":
                return False
            
            board[row][col] = "T"
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        # capture unsurrounded region (O -> T), run dfs
        for r in range(num_row):
            for c in range(num_col):
                if board[r][c] == "O" and (r in [0, num_row - 1] or c in [0, num_col - 1]):
                    dfs(r,c)

        # capture surround region (O -> X)
        # uncapture unsurrounded region (T -> O)
        for r in range(num_row):
            for c in range(num_col):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"

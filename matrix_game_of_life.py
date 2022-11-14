from ast import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row_num, col_num = len(board), len(board[0])
        
        copy = [row[:] for row in board]
        def get_live_neighbors(r, c):
            delta_rows = [-1, -1, 0, 1, 1, 1, 0, -1]
            delta_cols = [0, 1, 1, 1, 0, -1, -1, -1]
            res = 0
            for i in range(len(delta_rows)):
                new_row = r + delta_rows[i]
                new_col = c + delta_cols[i]
                if new_row < 0 or new_col < 0 or new_row >= row_num or new_col >= col_num:
                    continue
                if copy[new_row][new_col] == 1:
                    res += 1
            return res
        
        for r in range(row_num):
            for c in range(col_num):
                live_neighbors_count = get_live_neighbors(r, c)
                if board[r][c] == 1 and (live_neighbors_count < 2 or live_neighbors_count > 3):
                    board[r][c] = 0
                elif board[r][c] == 0 and live_neighbors_count == 3:
                    board[r][c] = 1
                                         
                        
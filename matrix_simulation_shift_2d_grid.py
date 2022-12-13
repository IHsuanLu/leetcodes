from ast import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        row_num, col_num = len(grid), len(grid[0])
        k = k % (row_num * col_num)

        del_row = k // col_num
        del_col = k % col_num

        res = [[0 for _ in range(col_num)] for _ in range(row_num)]
        for r in range(row_num):
            for c in range(col_num):
                new_row = (r + del_row + 1) % row_num if (c + del_col) >= col_num else (r + del_row) % row_num
                new_col = (c + del_col) % col_num
                res[new_row][new_col] = grid[r][c]

        return res
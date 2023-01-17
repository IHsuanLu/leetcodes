from ast import List


class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        prefix_mat = [row[:] for row in grid]
        row_num, col_num = 2, len(grid[0])

        for r in range(row_num):
            for c in range(1, col_num):
                prefix_mat[r][c] += prefix_mat[r][c - 1]
        
        res = float("inf")
        for c in range(col_num):
            group1 = prefix_mat[0][col_num - 1] - prefix_mat[0][c]
            group2 = prefix_mat[1][c - 1] if c - 1 >= 0 else 0 
            second_robot = max(group1, group2)
            res = min(res, second_robot) # use min cause the first robot wants to minimize what the second robot could get

        return res


# Not working
class Solution:
    def get_prefix_mat(self, grid):
        prefix_mat = [row[:] for row in grid]
        row_num, col_num = 2, len(grid[0])
        for r in range(1, row_num):
            prefix_mat[r][0] += prefix_mat[r - 1][0]

        for c in range(1, col_num):
            prefix_mat[0][c] += prefix_mat[0][c - 1]

        for r in range(1, row_num):
            for c in range(1, col_num):
                prefix_mat[r][c] += prefix_mat[r - 1][c] + prefix_mat[r][c - 1]
        
        return prefix_mat

    def gridGame(self, grid: List[List[int]]) -> int:
        # get the prefix sum
        # starting from (1, n-1) and tracing back to 
        prefix_map = self.get_prefix_mat(grid)

        curr_row, curr_col = 1, len(grid[0]) - 1
        while curr_row > 0 or curr_col > 0:
            grid[curr_row][curr_col] = 0
            if curr_row - 1 >= 0 and curr_col - 1 >= 0:
                if prefix_map[curr_row - 1][curr_col] > prefix_map[curr_row][curr_col - 1]:
                    curr_row -= 1
                else:
                    curr_col -= 1
            elif curr_row - 1 >= 0:
                curr_row -= 1
            else:
                curr_col -= 1

        grid[0][0] = 0
        prefix_map = self.get_prefix_mat(grid)

        res = 0
        curr_row, curr_col = 1, len(grid[0]) - 1
        while curr_row > 0 or curr_col > 0:
            res += grid[curr_row][curr_col]
            if curr_row - 1 >= 0 and curr_col - 1 >= 0:
                if prefix_map[curr_row - 1][curr_col] > prefix_map[curr_row][curr_col - 1]:
                    curr_row -= 1
                else:
                    curr_col -= 1
            elif curr_row - 1 >= 0:
                curr_row -= 1
            else:
                curr_col -= 1

        return res

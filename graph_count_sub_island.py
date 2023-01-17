from ast import List


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        """
        traverse grid2 -> see if every cell of the island is included in grid1
        """
        row_num, col_num = len(grid1), len(grid1[0])

        def dfs(r, c):
            if r < 0 or r >= row_num or c < 0 or c >= col_num:
                return True

            if grid2[r][c] == 0:
                return True
            if grid1[r][c] == 0:
                return False

            # visited based case should come at the very last
            if (r, c) in visited:
                return True
            visited.add((r, c))

            res1 = dfs(r + 1, c)
            res2 = dfs(r - 1, c)
            res3 = dfs(r, c + 1)
            res4 = dfs(r, c - 1)

            return res1 and res2 and res3 and res4
        
        visited = set()
        total = 0
        for r in range(row_num):
            for c in range(col_num):
                if grid2[r][c] == 1 and (r, c) not in visited:
                    if dfs(r, c):
                        total += 1

        return total
            


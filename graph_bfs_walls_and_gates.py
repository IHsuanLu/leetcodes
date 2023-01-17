from ast import List
from collections import deque


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        """
        [[2147483647,-1,0,2147483647],
         [2147483647,2147483647,2147483647,-1],
         [2147483647,-1,2147483647,-1],
         [0,-1,2147483647,2147483647]]

        for every gate, we run a bfs to fill the level into the room
            -> if the cell is `INF`, we fill in the current level
            -> if the cell is `-1`, return
            -> if the cell is a number other than `INF`, we keep the smaller number
        """
        INF = 2147483647
        row_num, col_num = len(rooms), len(rooms[0])
        queue = deque([])
        for r in range(row_num):
            for c in range(col_num):
                if rooms[r][c] == 0:
                    queue.append((r, c, 0))

        def get_neighbors(row, col):
            neighbors = []
            delta_rows = [-1, 0, 1, 0]
            delta_cols = [0, 1, 0, -1]
            for i in range(4):
                new_row = row + delta_rows[i]
                new_col = col + delta_cols[i]
                if new_row < 0 or new_row >= row_num or new_col < 0 or new_col >= col_num:
                    continue
                neighbors.append((new_row, new_col))
            return neighbors
        
        # BFS
        visited = set()
        while queue:
            for _ in range(len(queue)):
                r, c, level = queue.popleft()
                if (r, c) in visited:
                    continue
                visited.add((r, c))

                if rooms[r][c] == -1: 
                    continue

                if rooms[r][c] == INF:
                    rooms[r][c] = level

                for neighbor in get_neighbors(r, c):
                    n_r, n_c = neighbor
                    queue.append((n_r, n_c, level + 1))

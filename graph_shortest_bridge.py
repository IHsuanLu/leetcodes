class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        N = len(grid)
        
        queue = deque([])
        curr_color = 2
        def paint(r, c, color):
            if r < 0 or r >= N or c < 0 or c >= N:
                return
            if grid[r][c] != 1:
                return

            grid[r][c] = color

            # prepare for the BFS later
            if curr_color == 2:
                queue.append((r, c))

            paint(r + 1, c, color)
            paint(r - 1, c, color)
            paint(r, c + 1, color)
            paint(r, c - 1, color)
        
        for r in range(N):
            for c in range(N):
                if grid[r][c] != 0:
                    paint(r, c, curr_color)

                    # assign different color to the other island
                    curr_color += 1

        def get_neighbors(r, c, color):
            neighbors = []
            delta_rows = [-1, 0, 1, 0]
            delta_cols = [0, 1, 0, -1]
            for i in range(4):
                new_row = r + delta_rows[i]
                new_col = c + delta_cols[i]
                if new_row < 0 or new_row >= N or new_col < 0 or new_col >= N:
                    continue

                # skip if the color is the same
                if grid[new_row][new_col] == color:
                    continue
                neighbors.append((new_row, new_col))
            return neighbors
        
        # BFS get the shortest distance between two island
        level = -1
        visited = set()
        while queue:
            for _ in range(len(queue)):
                nxt_r, nxt_c = queue.popleft()
                if (nxt_r, nxt_c) in visited:
                    continue
                visited.add((nxt_r, nxt_c))

                # direct return when the very first target is found 
                if grid[nxt_r][nxt_c] != 0 and grid[nxt_r][nxt_c] != 2:
                    return level

                for n_r, n_c in get_neighbors(nxt_r, nxt_c, 2):
                    queue.append((n_r, n_c))
            
            level += 1

        return -1
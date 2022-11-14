from collections import deque

def get_knight_shortest_path(x: int, y: int) -> int:
    def get_neighbors(coord):
        r,c = coord
        delta_row = [-2, -2, -1, 1, 2, 2, 1, -1]
        delta_col = [-1, 1, 2, 2, 1, -1, -2, -2]
        res = []
        for i in range(len(delta_row)):
            row = r + delta_row[i]
            col = c + delta_col[i]
            res.append((row, col))
        return res
    
    
    def bfs(start):
        visited = set()
        steps = 0
        queue = deque([start])
        while len(queue) > 0:
            n = len(queue)
            for _ in range(n):
                node = queue.popleft()
                if node[0] == y and node[1] == x:
                    return steps
                for neighbor in get_neighbors(node):
                    r, c = neighbor
                    if neighbor in visited:
                        continue
                    queue.append(neighbor)
                    visited.add(neighbor)
            steps += 1
                    
    
    
    return bfs((0,0))
from typing import List
from collections import deque

def flood_fill(r: int, c: int, replacement: int, image: List[List[int]]) -> List[List[int]]:
    num_rows, num_cols = len(image), len(image[0])
    def get_neighbors(coord, color):
        row, col = coord
        delta_row = [-1, 0, 1, 0]
        delta_col = [0, 1, 0, -1]
        res = []
        for i in range(len(delta_row)):
            neighbor_row = row + delta_row[i]
            neighbor_col = col + delta_col[i]
            if 0 <= neighbor_row < num_rows and 0 <= neighbor_col < num_cols:
                # valid
                if image[neighbor_row][neighbor_col] == color: #only grab those with the same color
                    res.append((neighbor_row, neighbor_col))
        return res
    
    
    def bfs(root):
        queue = deque([root])
        visited = [[False for col in range(num_cols)] for row in range(num_rows)]
        
        r, c = root
        color = image[r][c] # get the root color
        image[r][c] = replacement # replace the root color
        visited[r][c] = True
        
        while len(queue) > 0:
            n = len(queue)
            for _ in range(n):
                target = queue.popleft()
                for neighbor in get_neighbors(target, color):
                    r, c = neighbor
                    if visited[r][c]:
                        continue
                    image[r][c] = replacement
                    queue.append(neighbor)
                    visited[r][c] = True
        
    bfs((r,c))
    return image
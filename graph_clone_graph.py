# we dont wanna create node every single time; instead, we can manage a map storing the new created nodes since neighbors might be shared
# https://leetcode.com/problems/clone-graph/discuss/42314/Python-solutions-(BFS-DFS-iteratively-DFS-recursively).

from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

# BFS
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':      
        if not node:
            return None     

        visited = set()
        queue = deque([node])
        memo = {}
        
        while len(queue) > 0:
            for _ in range(len(queue)):
                nxt = queue.popleft()
                if nxt in visited:
                    continue
                visited.add(nxt)

                if nxt not in memo:
                    memo[nxt] = Node(nxt.val)

                for neighbor in nxt.neighbors:
                    if neighbor not in memo:
                        memo[neighbor] = Node(neighbor.val)

                    # append neighbors
                    memo[nxt].neighbors.append(memo[neighbor])

                    # append neighbor to queue for next round
                    queue.append(neighbor)                 
    
        return memo[node]
                        
                        
# DFS
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None     

        visited = set()
        memo = {}

        def dfs(head):
            if head is None:
                return
            
            if head in visited:
                return
            visited.add(head)

            if head not in memo:
                memo[head] = Node(head.val)

            for neighbor in head.neighbors:
                if neighbor not in memo:
                    memo[neighbor] = Node(neighbor.val)
                
                memo[head].neighbors.append(memo[neighbor])

                dfs(neighbor)
        
        dfs(node)
        return memo[node]
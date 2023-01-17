from ast import List
import collections

"""
# Hint 
Treat the graph as undirected. Start a dfs from the root, if you come across an edge in the forward direction, you need to reverse the edge.
"""
# DFS -> (Treat the graph as undirected)
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adjacents = collections.defaultdict(list)
        undirected_adjacents = collections.defaultdict(list)
        for p, c in connections:
            adjacents[p].append(c)
            undirected_adjacents[p].append(c)
            undirected_adjacents[c].append(p)

        visited = set()
        total = [0]
        def dfs(node):
            if not undirected_adjacents[node]:
                return
            
            for child in undirected_adjacents[node]:
                if child not in visited and child != 0:
                    visited.add(child)
                    if node not in adjacents[child]:
                        total[0] += 1
                
                    dfs(child)

        dfs(0)
        return total[0]

# not working -> too many unexpected edge cases
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adjacents = collections.defaultdict(list)
        for p, c in connections:
            adjacents[p].append(c)
        
        visited = set()
        def dfs(node, acc):
            if not adjacents[node]:
                return acc
            
            total = 0
            for child in adjacents[node]:
                if child not in visited and child != 0:
                    visited.add(child)
                    total = dfs(child, acc + 1)
            
            return total

        res = 0
        for i in range(n):
            res += dfs(i, 0)

        return res
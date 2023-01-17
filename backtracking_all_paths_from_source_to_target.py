from ast import List
import collections

"""

- there could be at most `2^(N-1) - 1` possible paths in the graph.
- it takes O(N) time to build a path.
    -> time complexity should be O(2^(N) * N)
    -> space complexity should be O(N) -> recusive stack (exclude the return value O(2^(N) * N))

"""

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        adjacents = collections.defaultdict(list)
        for i in range(len(graph)):
            for j in range(len(graph[i])):
                adjacents[i].append(graph[i][j])

        res = []
        def dfs(node, path):
            if node == len(graph) - 1:
                res.append(path[:])
                return
            
            for neighbor in adjacents[node]:
                path.append(neighbor)
                dfs(neighbor, path)
                path.pop()
            
        dfs(0, [0])
        return res

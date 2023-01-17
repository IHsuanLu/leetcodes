from ast import List
import collections


class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        adjacents = collections.defaultdict(list)
        for u, v in relations:
            adjacents[u].append(v)
        
        """
        topological sort
            -> get the max depth of the node list
        """
        cycle = set()
        memo = {}
        def dfs(node):
            if not adjacents[node]:
                return 0
            if node in cycle:
                return -1
            if node in memo:
                return memo[node]

            cycle.add(node)
            
            max_sems = 1
            for neighbor in adjacents[node]:
                depth = dfs(neighbor)
                if depth == -1:
                    return -1
                max_sems = max(max_sems, depth + 1)
            
            cycle.remove(node)
            memo[node] = max_sems
            return max_sems

        res = 1
        for i in range(1, n + 1):
            depth = dfs(i)
            if depth == -1:
                return -1
            res = max(res, depth)

        return res + 1
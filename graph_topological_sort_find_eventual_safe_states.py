from ast import List
import collections


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        adjacents = collections.defaultdict(list)
        for i in range(len(graph)):
            adjacents[i].extend(graph[i])
        
        memo = {}
        def dfs(node, cycle):
            if node in memo:
                return memo[node]
            if not adjacents[node]:
                return True
            if node in cycle:
                return False
            cycle.add(node)

            for neighbor in adjacents[node]:
                if not dfs(neighbor, cycle):
                    # return `False` directly if cycle is detected
                    return False
            
            # remove the node from the set detecting cycle
            # otherwise, case like `[[],[0,2,3,4],[3],[4],[]]` will be wrong
            # since graph[2], graph[3] will be visited multiple times and it's not a cycle
            cycle.remove(node)

            memo[node] = True
            return True
        
        res = []
        for i in range(len(graph)):
            if dfs(i, set()):
                res.append(i)

        return res
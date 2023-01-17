# FAV
from ast import List
import collections

# DFS -> works
class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adjacents = collections.defaultdict(list)
        # undirected graph
        for u, v in edges:
            adjacents[u].append(v)
            adjacents[v].append(u)

        def dfs(node, visited):
            node_has_apple = False
            if hasApple[node]:
                node_has_apple = True
            
            acc = 0
            for child in adjacents[node]:
                # prevent cycle in undirected graph
                if child in visited:
                    continue
                visited.add(child)
                    
                child_has_apple, child_acc = dfs(child, visited)
                if child_has_apple:
                    acc += child_acc + 1
                    # if a child has apple ==> it parent has apple
                    node_has_apple = True
            
            return node_has_apple, acc
            
        return dfs(0, set({0}))[1] * 2

# DFS -> not working
class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adjacents = collections.defaultdict(list)
        for u, v in edges:
            adjacents[u].append(v)
        
        """
        we only need to know the furthest node that has apples
        """

        def dfs(node):
            if not adjacents[node]:
                print("!!", node)
                return 1 if hasApple[node] else 0
            
            sum_val = 0
            child_has_apple = False
            for child in adjacents[node]:
                child_sum_val = dfs(child)
                if child_sum_val:
                    child_has_apple = True
                
                sum_val += child_sum_val

            if child_has_apple:
                sum_val += 1
            
            return sum_val
            
        res = dfs(0)
        return res * 2
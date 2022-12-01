from ast import List
import collections


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        adjacents = collections.defaultdict(list)
        val_map = {}
        
        for i, (p, c) in enumerate(equations):
            adjacents[p].append(c)
            adjacents[c].append(p)
            val_map[(p, c)] = values[i]
            val_map[(c, p)] = 1 / values[i] 
        
        res = []
        def dfs(node, target, acc, visited):
            if node == target:
                return acc
            
            if node in visited:
                return -1
            visited.add(node)
            
            for neighbor in adjacents[node]:
                score = dfs(neighbor, target, acc * val_map[(node, neighbor)], visited)
                if score != -1:
                    return score
                else:
                    # get score as -1 does not mean there is no find in such a dfs call
                    # a -> b (2.0); b -> c (6.0) -> return 6.0
                    #             ; b -> a (-1, visited)
                    
                    # if we return -1 directly here, meaning any one of the neighbor gets
                    # -1 -> we'll keep returning -1 to the parents
                    print("????", node, neighbor)
            
            # only reach here if there is not early-returned score
            print("!!!!", node, neighbor)
            return -1
        
        for tp, tc in queries:
            if tp not in adjacents or tc not in adjacents:
                res.append(-1)
            else:
                result = dfs(tp, tc, 1, set())
                res.append(result)
        
        return res


# n = # of nodes
# e = # of edges = size of equations = size of values
# q = size of queries
# time: O(q * e)
# space: O(n + e)

# total complexity is O(q * e), with O(e) additional space for the graph.

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adjacents = collections.defaultdict(list)
        val_map = {}
        
        for i, (p, c) in enumerate(equations):
            adjacents[p].append(c)
            adjacents[c].append(p)
            val_map[(p, c)] = values[i]
            val_map[(c, p)] = 1 / values[i] 
        
        res = []
        def dfs(node, target, acc, visited):
            if node == target:
                res.append(acc)
                return True
            
            if node in visited:
                return False
            visited.add(node)
            
            for neighbor in adjacents[node]:
                if dfs(neighbor, target, acc * val_map[(node, neighbor)], visited):
                    return True
            
            return False
        
        for tp, tc in queries:
            if tp not in adjacents or tc not in adjacents:
                res.append(-1)
            else:
                solution_found = dfs(tp, tc, 1, set())
                if not solution_found:
                    res.append(-1)
        
        return res
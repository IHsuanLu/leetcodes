from ast import List
import collections

# two arrays
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if len(trust) < n - 1: # not all nodes are connected
            return -1
        
        outwards_count = [0] * (n + 1)
        inwards_count = [0] * (n + 1)

        for u, v in trust:
            outwards_count[u] += 1
            inwards_count[v] += 1
        
        for i in range(1, n + 1):
            if outwards_count[i] == 0 and inwards_count[i] == n - 1:
                return i
        
        return -1


# hash map as an adjacency list
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        adjacents = collections.defaultdict(list)
        for u, v in trust:
            adjacents[u].append(v)
        
        if not trust:
            return n if n == 1 else -1

        for i in range(1, n + 1):
            if i not in adjacents:
                is_town_judge = True
                for j in range(1, n + 1):
                    if i != j and i not in adjacents[j]:
                        is_town_judge = False
                        break

                if is_town_judge:
                    return i

        return -1
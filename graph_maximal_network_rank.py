from ast import List
import collections


class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        if not roads:
            return 0

        adjacents = collections.defaultdict(list)
        
        for u, v in roads:
            adjacents[u].append(v)
            adjacents[v].append(u)
        
        # choose the max coeverage
        candidates = sorted([(len(v), k) for k, v in adjacents.items()], reverse=True) 
        max_rank = -1
        
        for i in range(len(candidates)):
            for j in range(i + 1, len(candidates)):
                c1, node1 = candidates[i]
                c2, node2 = candidates[j]
                
                rank = c1 + c2
                if node1 in adjacents[node2] and node2 in adjacents[node1]:
                    rank -= 1
                
                max_rank = max(max_rank, rank)

        return max_rank
    
from ast import List
import collections

# DFS dives to the deepest valid place and starts the result accumulation
# do not need to handle cycle, it's just another path (e.g. A -> B; A -> B -> C -> A -> B)

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjacents = collections.defaultdict(list)
        price_map = {}
        for start, end, price in flights:
            adjacents[start].append(end)
            price_map[(start, end)] = price
        
        def dfs(node, stop_remained, memo):
            # terminate if node = dist, return 0
            # since the distance of itself is 0, and start accumulating price with price_map
            if node == dst:
                return 0
            
            if stop_remained < 0:
                return float('inf')
            
            if (node, stop_remained) in memo:
                return memo[(node, stop_remained)]

            min_res = float('inf')
            for neighbor in adjacents[node]:
                res = dfs(neighbor, stop_remained - 1, memo) + price_map[(node, neighbor)]
                min_res = min(min_res, res)
            
            memo[(node, stop_remained)] = min_res
            return min_res
        
        memo = {}
        res = dfs(src, k, memo)
        return res if res != float('inf') else -1


# reach and handle (X)
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjacents = collections.defaultdict(list)
        price_map = {}
        for start, end, price in flights:
            adjacents[start].append(end)
            price_map[(start, end)] = price
        
        min_val = [float('inf')]
        def dfs(node, stop_remained, acc):
            if stop_remained < 0:
                return float('inf')
            
            if node == dst:
                # update the min cost
                min_val[0] = min(min_val[0], acc)
                return
            
            for nxt in adjacents[node]:
                dfs(nxt, stop_remained - 1, acc + price_map[(node, nxt)])
        
        dfs(src, k + 1, 0)
        return min_val[0] if min_val[0] != float('inf') else -1
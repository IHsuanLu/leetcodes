from ast import List
import collections
import heapq

# Dijkstra's Algorithm - a single soource shortest path algorithm
# It uses uses a “greedy approach”. Each step selects the “minimum weight” from the currently reached vertices to find the “shortest path” to other vertices.
# Limitation: it doesn't work when there are negative weight

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Directed Acyclic Graph + Find the minimum path -> Dijstra's Algorithm
        # Use min heap to decide which one to go next 
        adjacents = collections.defaultdict(list)
        for _from, _to, time in times:
            adjacents[_from].append((time, _to))

        min_heap = []
        heapq.heapify(min_heap)
        for item in adjacents[k]:
            heapq.heappush(min_heap, item)

        visited = { k }
        while min_heap:
            nxt_time_consumed, nxt_node = heapq.heappop(min_heap)
            if nxt_node in visited:
                continue
            visited.add(nxt_node)

            if len(visited) == n:
                return nxt_time_consumed

            for child_time_consumed, child in adjacents[nxt_node]:
                # store the acc time here, so we don't need to handle the min_sum separately
                heapq.heappush(min_heap, (nxt_time_consumed + child_time_consumed, child))

        # if not every node is visted -> there is unconnected nodes
        return -1

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjacents = collections.defaultdict(list)
        time_map = {}
        
        for _from, _to, time in times:
            adjacents[_from].append(_to)
            time_map[(_from, _to)] = time
        
        res = 0

        min_heap = [(0, k)]
        heapq.heapify(min_heap)
        
        visited = set()
        
        while len(min_heap) > 0:
            path_count, node = heapq.heappop(min_heap)
            if node in visited:
                continue
            visited.add(node)

            res = max(res, path_count)
            
            for child in adjacents[node]:
                heapq.heappush(min_heap, (time_map[(node, child)] + path_count, child))
        
        # if not every node is visted -> there is unconnected nodes
        return res if len(visited) == n else -1
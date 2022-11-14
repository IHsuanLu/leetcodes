from ast import List
import heapq


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key= lambda s: s[1])
        
        tu_end_times_and_caps = []
        heapq.heapify(tu_end_times_and_caps)
        
        curr_cap = 0
        for i in range(len(trips)):
            heapq.heappush(tu_end_times_and_caps, (trips[i][2], trips[i][0]))
            
            curr_cap += trips[i][0]
            if curr_cap > capacity:
                return False
            
            while i + 1 < len(trips) and tu_end_times_and_caps and tu_end_times_and_caps[0][0] <= trips[i+1][1]:
                _, cap = heapq.heappop(tu_end_times_and_caps)
                curr_cap -= cap
                
                
        return True
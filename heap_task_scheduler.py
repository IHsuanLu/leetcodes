# we don't need to consider the type of the task cause that doesn't matter
# shifting the time directly stands for idleling the scheduler

from ast import List
from collections import Counter, deque
import heapq


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        
        # store count only cause the type of the task doesn't matter
        max_heap = [-count for count in counter.values()] 
        heapq.heapify(max_heap)
        
        queue = deque() # [-count, time_to_add_back_to_heap]
        time = 0 
        while max_heap or queue:
            time += 1 
            if max_heap:
                count = heapq.heappop(max_heap)
                count += 1
                if count != 0:
                    queue.append((count, time + n))
            
            if queue and queue[0][1] == time:
                count, _ = queue.popleft()
                heapq.heappush(max_heap, count)
        
        return time
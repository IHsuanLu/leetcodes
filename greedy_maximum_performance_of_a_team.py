"""
how do we know if the efficiency is maximized?
-> brute force: try the permuation with the length of `k`, and get the minumum
    -> O(2^N)

** We don't necessarily need to take `k` but at most `k` ** 

How can we do it better?
    - since we don't necessarily need to take `k` but at most `k`, 
      we can greedily always choose the emplooyee `k - 1` to `1` with the higher efficiency than `k`
      Further, since there won't be a negative value in `speed` array, selecting `k - 1` to `1` with efficiency higher than `k` will always be a plus to a team
      because only the smallest efficiency will be considered
    
    - with that, we sort the `efficiency` in descending order, and `speed` correspondingly
    ```
    speed = [x for _, x in sorted(zip(efficiency, speed), reverse=True)]
    efficiency.sort(reverse=True)
    ```
"""

# FAV

from ast import List
import heapq


# O(nlogn + nlogk) (sorting + heap operation with the size of k)
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        speed = [x for _, x in sorted(zip(efficiency, speed), reverse=True)]
        efficiency.sort(reverse=True)
        
        min_heap = []
        heapq.heapify(min_heap)

        sum_val = 0
        max_performance = 0
        for i in range(n):
            heapq.heappush(min_heap, speed[i])
            sum_val += speed[i]
            
            while len(min_heap) > k:
                sum_val -= heapq.heappop(min_heap)
            
            max_performance = max(max_performance, sum_val * efficiency[i])

        modulo = 10 ** 9 + 7 
        return max_performance % modulo

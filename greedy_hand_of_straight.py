# Same as 1296.Divide Array in Sets of K Consecutive Numbers

# greedily grab the minimum value as the first element in the set
from ast import List
import heapq

# O(n * n)
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        memo = {}
        for num in hand:
            memo[num] = 1 + memo.get(num, 0)
        
        while len(memo.keys()) > 0:
            minimum = min(memo.keys())
            for i in range(groupSize):
                if (minimum + i) not in memo:
                    return False
                else:
                    memo[minimum + i] -= 1
                
                if memo[minimum + i] < 0:
                    return False
                if memo[minimum + i] == 0:
                    del memo[minimum + i]
        
        return True


# enhancement in finding minimum -> min_heap, by adding every key values into the min_heap

# O(n * logn)
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        memo = {}
        for num in hand:
            memo[num] = 1 + memo.get(num, 0)
        
        min_heap = list(memo.keys())
        heapq.heapify(min_heap)
                        
        while len(min_heap) > 0:
            minimum = min_heap[0]
                        
            for i in range(minimum, minimum + groupSize):
                if i not in memo:
                    return False
                memo[i] -= 1
                
                if memo[i] == 0:
                    # if we ever try to pop the value from the heap which is not the minimum value, then we can return False directly
                    # [1,1,3,6,2,3,4,7,8] -> get [1, 2, 3] -> [1, X, 3]
                    if i != min_heap[0]:
                        return False
                    heapq.heappop(min_heap)
        
        return True
# in increasing order
#   -> if the value is not the largest in the previous window, we don't even need to consider it in the next round
#   -> using deque (monotonic decresing deque, pop every smaller value before adding a new one)
#       -> why not stack?
#           -> we want add/remove element from the last with O(1); and also remove element from the beginning with O(1)
#           -> left-most will always be the maximum
#           -> pop the left element when the length of the queue is larger than the given "k", aka adding to the result
#   -> achieve O(n)
from ast import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        l = r = 0 # window's frame
        queue = deque() # put indices
        
        while r < len(nums): # while the r is still inbound
            while queue and nums[queue[-1]] < nums[r]:
                queue.pop()
            
            queue.append(r) 
            
            # if the left-most val in the queue is out of the window's bound, we remove it from the queue
            if l > queue[0]:
                queue.popleft()
                
            # edge case, if we wanna append result, we need to make sure the windows is in size of k
            if (r + 1) >= k:
                res.append(nums[queue[0]])
                l += 1 # move left pointer only if the size of the window reaches "k"
                
            r += 1
        
        return res
            


# it's not gonna work
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
            
        
        dp = [float('-inf')] * len(nums)
        dp[0] = nums[0]
        
        for i in range(1, len(nums)):
            if k == 2:
                dp[i] = max(nums[i - k + 1], nums[i])
            else:
                dp[i] = max(dp[i - 1], nums[i])
        
        return dp[k-1:]
        # [1,3,-1,-3,5,3,6,7]
        # [1,3,3,3,5,5,6,7]
        # [3,3,5,5,6,7]
        # [3,5,5,6,7]
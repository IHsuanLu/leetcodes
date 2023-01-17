from ast import List

# Time: O(n^2)
# -> each time we run LIS takes O(n) time.  

# Space: O(n)
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        memo = {}
        def dfs(idx):
            if idx in memo:
                return memo[idx]
            
            max_val = 0
            max_freq = 1
            for i in range(idx, len(nums)):
                if i + 1 < len(nums) and nums[i + 1] > nums[idx]:
                    child_max, child_freq = dfs(i + 1)
                    if child_max > max_val:
                        max_val = child_max
                        max_freq = child_freq
                    elif child_max == max_val:
                        max_freq += child_freq

            memo[idx] = (max_val + 1, max_freq)
            return memo[idx]
                    
        max_val, max_freq = 0, 1
        for i in range(len(nums)):
            val, freq = dfs(i)
            if val > max_val:
                max_val = val
                max_freq = freq
            elif max_val == val:
                max_freq += freq

        return max_freq
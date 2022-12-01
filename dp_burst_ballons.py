# Intuition:
# Firstly, let's see if we can identify any subproblems?
#   -> For each element in the array, we can decide to either include it or not to include it
#   -> we will get 2^n subsequence
#   -> yet, we wouldn't want to cache something that is 2^n huge

# Can we do better?
#   -> Instead of subsequence -> let's view it as subarrays

# Examples
#
# [3,1,5,8] 
#   -> if we pop `5`
#   -> we will get [3,1] and [8]
# 
# Yet, that's not gonna work! -> [3,1] and [8] are actually connected
#                             -> if we view them separately, we will miss the maximum outcome
#                             -> pop `1` and get `24`

# how can we fix it?

# We can view it another way around
# What if we pop `5` last?
#   -> i.e., [3,1] and [8] will never be together

# let's say if we want to pop [3,1] prior to [5]
#   -> we will be setting the l, r boundary at `3` and `1`, and there will be implicit boundary for calculation like
#   -> 1, [3, 1], 5
#   -> 5. [8], 1

# Our decision tree will base on (what if I pop the specific last)
# -> [3,1,5,8] -> [1, 3, 1, 5, 8, 1] -> add impliciit walls
#                     l  i     r
#                     
# if we pop a number at index `i` -> we will get `nums[l-1] * nums[i] * nums[r+1] + memo[i+1][r] + memo[l][i-1]`

# Space complexity: O(n^2) // the combination of subarrays
# Time complexity: O(n^3) // iterate thru every element per given subarray -> O(n^2 * n)

from functools import lru_cache


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        memo = [[0] * len(nums)] * len(nums)
        
        @lru_cache(maxsize=None)
        def dfs(l, r):
            if l > r:
                return 0
            
            if l in memo and r in memo[l]:
                return memo[l][r]
            
            # the maximum we can get in (l, r) pair
            memo[l][r] = 0
            
            # assume i is the last element to pop
            for i in range(l, r + 1):
                coins = nums[l - 1] * nums[i] * nums[r + 1] + dfs(i + 1, r) + dfs(l, i - 1)
                memo[l][r] = max(memo[l][r], coins)
            
            return memo[l][r]
            
        return dfs(1, len(nums) - 2)
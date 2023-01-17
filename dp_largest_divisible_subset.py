# FAV

from ast import List
from collections import defaultdict

# O(N^2) -> DFS w/ memoization
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        """
        1. sort the array 
            -> what can we take advantage of via sorting?
                -> if a x is divisible by y, and y is divisible by z (y > x)
                    -> we can know that x is also divisible to z
        2. intuition
        1 -> [1]
        2 -> [1,2]
        3 -> [1,3]
        4 -> [1,2,4]

        3. overlapping subproblem -> dynamic programming

        4. bottom-up or top-down (DFS + memoization)
        """
        nums.sort()
        memo = defaultdict(list)
        def dfs(idx):
            if idx == len(nums):
                return []
                
            # memoization
            if idx in memo:
                return memo[idx]

            max_subset = []
            for i in range(idx):
                if nums[idx] % nums[i] == 0:
                    # keep on the recursive call
                    max_subset = max(max_subset, dfs(i), key=len)
            
            # for the max array (reference data type) -> we should give a deepcopy for the memo hmap
            deep_copy = max_subset[:]
            deep_copy.append(nums[idx])

            memo[idx] = deep_copy
            return memo[idx]
        
        res = []
        for i in range(len(nums)):
            res = max(res, dfs(i), key=len)

        return res


# O(N^2) -> backtracking w/ memoization
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        
        self.res = []
        memo = defaultdict(int)
        def dfs(idx, path):
            # this is not the base case, yet just update when needed
            if len(path) > len(self.res):
                self.res = path[:]
            
            for i in range(idx + 1, len(nums)):
                # for the "largest" kind of problem, we can keep doing if the result will be larger than the previous cached one
                if nums[i] % path[-1] == 0 and len(path) + 1 > memo[nums[i]]:
                    path.append(nums[i])
                    memo[nums[i]] = len(path)
                    dfs(i, path)
                    path.pop()

        dfs(-1, [1])
        return self.res[1:]



# O(2^N) -> backtracking w/o memoization
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        
        self.res = []
        def dfs(idx, path):
            if len(path) > len(self.res):
                self.res = path[:]
            
            for i in range(idx + 1, len(nums)):
                if nums[i] % path[-1] == 0:
                    path.append(nums[i])
                    dfs(i, path)
                    path.pop()

        dfs(-1, [1])
        return self.res[1:]
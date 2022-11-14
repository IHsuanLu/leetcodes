from ast import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def dfs(idx, memo):
            if idx in memo:
                return memo[idx]
            count = 1
            for j in range(idx+1, len(nums)):
                if nums[j] > nums[idx]:
                    count = max(count, 1+dfs(j, memo))

            memo[idx] = count
            return count

        memo = {}
        for i in range(len(nums)):
            dfs(i, memo)
        
        return max(memo.values())

#         DP Solution
#         LIS = [1] * len(nums)
        
#         # Iterate in reverse order
#         for i in range(len(nums) - 1, -1, -1):
#             for j in range(i+1, len(nums)):
#                 if nums[i] < nums[j]:
#                     LIS[i] = max(LIS[i], 1 + LIS[j])
                    
#         return max(LIS)
from ast import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        1. brute force O(2^N)
            -> either include the element or not into our solution

        2. intuition
            -> recursively go through every single element in the array
                -> 10 -> find 101; 101 -> find nothing -> return (output: 2)
                      -> find 18; 18 -> find nothing -> return (output: 2)
                      -> get max output -> 2
                   ...
                   2 -> find 5; 5 -> find 7; 7 -> find 101
                                               -> find 18
                      -> get max output -> 4

        3. repeated work spotted
        4. add the memoization (cache) -> O(N^2)

        5. implement
        """

        memo = {}
        def dfs(idx):
            if idx == len(nums):
                return 0
            if idx in memo:
                return memo[idx]
            
            max_val = 1
            for i in range(idx + 1, len(nums)):
                if nums[i] > nums[idx]:
                    max_val = max(max_val, dfs(i) + 1)

            memo[idx] = max_val
            return max_val

        res = 0
        for i in range(len(nums)):
            res = max(res, dfs(i))
        
        return res


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

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        def dfs(idx):
            if idx in memo:
                return memo[idx]

            res = 1
            for i in range(idx, len(nums)):
                if i + 1 < len(nums) and nums[i + 1] > nums[idx]:
                    res = max(res, dfs(i + 1) + 1)

            memo[idx] = res
            return res

        max_val = 0
        for i in range(0, len(nums)):     
            max_val = max(max_val, dfs(i))

        return max_val

# Bottom-up
# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#        LIS = [1] * len(nums)
#    
#        # Iterate in reverse order
#        for i in range(len(nums) - 1, -1, -1):
#            for j in range(i+1, len(nums)):
#                if nums[i] < nums[j]:
#                    LIS[i] = max(LIS[i], 1 + LIS[j])
#                
#        return max(LIS)
# Intuition:
# O(k^n)
# decision tree - for every elements in the `nums` array, it could be categorized in any of the k groups

# Enhanced solution
# O(k*2^n)
# decision thoughts - for every elements in the `nums` array, it could either be included in our sum or not included -> create a single bucket at a time
#   for example, `nums = [4,3,2,3,5,2,1], k = 4`; target = 5
#      -> we try to sum up to `5` with any values in the array
#      -> decrease `k` by one and update the input array, or use additional space, to remove the used elements

from ast import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k:
            return False
        nums.sort(reverse=True)
        
        target = sum(nums) / k
        used = [False] * len(nums)
        
        memo = {}
        def backtrack(curr, remained_k, subset_sum):
            # since subproblem depends on used indices of array, if same subproblem occurs again just return dp value
            if tuple(used) in memo:
                return memo[tuple(used)]

            if remained_k == 0:
                return True
            # we are done with the current subset
            if subset_sum == target:
                res_partition = backtrack(0, remained_k - 1, 0) # start from the begining again
                memo[tuple(used)] = res_partition
                return res_partition
            
            # subset
            for i in range(curr, len(nums)):
                if used[i] or subset_sum + nums[i] > target:
                    continue
                    
                used[i] = True
                
                if backtrack(i + 1, remained_k, subset_sum + nums[i]):
                    return True
                
                used[i] = False
            
            memo[tuple(used)] = False
            return False
        
        return backtrack(0, k, 0)

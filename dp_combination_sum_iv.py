from ast import List

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        def dfs(remainder, memo):
            if remainder in memo:
                return memo[remainder]

            if remainder == 0:
                return 1
            if remainder < 0:
                return -1
            
            total = 0
            for num in nums:
                rlt = dfs(remainder - num, memo)
                if rlt != -1:
                    total += rlt
            
            memo[remainder] = total
            return total
        
        return dfs(target, {})
                
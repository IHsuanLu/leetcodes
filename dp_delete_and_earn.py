from ast import List

# O(n) -> hash map with count
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:     
        max_num = max(nums)

        hmap = {}
        for n in nums:
            hmap[n] = hmap.get(n, 0) + 1
            
        memo = {}
        def dfs(num):
            if num > max_num:
                return 0
            if num in memo:
                return memo[num]
            
            occurence = hmap[num] if num in hmap else 0
            sum1 = (num * occurence) + dfs(num + 2)
            sum2 = dfs(num + 1)
            memo[num] = max(sum1, sum2)
            return memo[num]
        
        return dfs(1)


# O(nlogn) -> with sorting
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:       
        nums.sort()
        temp = []
        l = 0
        for r in range(len(nums)):
            if nums[r] != nums[l]:
                temp.append(nums[l] * (r - l))
                if nums[r] - nums[l] > 1:
                    temp.append(0)
                l = r
            if r == len(nums) - 1:
                temp.append(nums[l] * (r - l + 1))
        
        memo = {}
        def dfs(idx):
            if idx >= len(temp):
                return 0
            if idx in memo:
                return memo[idx]
            
            sum1 = temp[idx] + dfs(idx + 2)
            sum2 = dfs(idx + 1)
            memo[idx] = max(sum1, sum2)
            return memo[idx]

        return dfs(0)
            

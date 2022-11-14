from ast import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        rlt = []
        for i, n in enumerate(nums):
            # avoid duplicate
            if i > 0 and n == nums[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                sum = n + nums[l] + nums[r]
                if sum > 0:
                    r -= 1
                elif sum < 0:
                    l += 1
                else:
                    rlt.append([n, nums[l], nums[r]]) 
                    # still need to shift pointer
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return rlt
from ast import List


# O(1) space
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n

        # nums = nums[n-k:] + nums[:n-k]
        # The below one can truly change the value of old nums, but the above one just changes its reference to a new nums not the value of old nums.
        nums[:] = nums[n-k:] + nums[:n-k]


# O(n) space
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        res = []
        n = len(nums)
        k = k % n
        
        for i in range(n - 1, -1, -1):
            if k > 0:
                res.insert(0, nums[i])
                k -= 1
            else:
                break
                
        nums[:] = res + nums[:n - len(res)]
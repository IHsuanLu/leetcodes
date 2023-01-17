# FAV
from ast import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        """
        hash number
            -> we traverse the array
            -> for every number nums[i] -> we mark nums[abs(nums[i]) - 1] as negative 
                -> if we found nums[i] has already been negative
                -> we add it to the result
        """
        """
        [4,3,2,7,8,2,3,1]
        """
        res = []
        for i in range(len(nums)):
            if nums[abs(nums[i]) - 1] > 0:
                nums[abs(nums[i]) - 1] *= -1
            else:
                res.append(abs(nums[i]))

        return res

from ast import List

# The smaller elements on the right of a number will jump from its right to its left during the sorting process.

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def divide(tuples):
            if len(tuples) == 1:
                return tuples
            mid = len(tuples) // 2
            left = divide(tuples[:mid])
            right = divide(tuples[mid:])
            return conquer(left, right)

        def conquer(left, right):
            merged_arr = []
            i = j = 0
            while i < len(left) and j < len(right):
                """
                1. why sort the array in descending order?
                    -> if we move the smaller value upfront (sorted ascending order)
                        -> the rest rounds will generate the wrong output cause the smaller value is moved to the front
                2. why `+= len(right) - j`?
                    -> since the array is sorted in descending order each round
                        -> once we found the first smaller value, we can assume the remaining element (index > j) will all be smaller than `left[i][1]`
                """
                if left[i][1] > right[j][1]:
                    merged_arr.append(left[i])
                    res[left[i][0]] += len(right) - j
                    i += 1
                else:
                    merged_arr.append(right[j])
                    j += 1
            merged_arr.extend(left[i:] or right[j:])
            return merged_arr

        res = [0] * len(nums)
        tuples = [(i, n) for i, n in enumerate(nums)]
        divide(tuples)
        return res

# O(n^2) -> time limited exceeded
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        
        for i in range(len(nums) - 1, -1, -1):
            valid_counts = 0
            for j in range(len(nums) - 1, i, -1):
                if nums[j] < nums[i]:
                    valid_counts += 1
            
            res[i] = valid_counts
                
        return res
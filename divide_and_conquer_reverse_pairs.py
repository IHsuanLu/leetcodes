from ast import List


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        # use merge sort technique
        # For each integer in the first part, count the number of integers that satisfy the condition from the second part. 
        
        def divide(arr):
            if len(arr) == 1:
                return arr
            mid = len(arr) // 2
            left = divide(arr[:mid])
            right = divide(arr[mid:])            
            return conquer(left, right)
        
        res = [0]
        def conquer(left, right):
            merged_arr = []
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged_arr.append(left[i])
                    i += 1
                else:
                    merged_arr.append(right[j])
                    j += 1
            
            merged_arr.extend(left[i:] or right[j:])
            
            v = 0
            for u in range(len(left)):
                while v < len(right) and right[v] * 2 < left[u]:
                    v += 1
                
                res[0] += v
            
            return merged_arr
        
        divide(nums)
        return res[0]
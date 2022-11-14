# https://leetcode.com/problems/sum-of-subarray-minimums/discuss/257811/Python-O(n)-slightly-easier-to-grasp-solution-(explained)
# A = [3,1,2,5,4]
# result = [3,2,4,9,12]
# 
# 3
# 1 + 1
# 1 + 1 + 2
# 1 + 1 + 2 + 5
# 1 + 1 + 2 + 4 + 4
#
# pattern:
# if A[i-1] <= A[i] then result[i] = result[i-1] + A[i]
# 
# reason:
# our subarrays ending with i-th value are basically same subarrays for (i-1)-th value with extra element A[i] added to each one of them and plus one extra subarray consisting of singular value A[i].
# Adding same or bigger value to subarrays doesn't change their minimal values.
# Thus we can reuse previous sum and account for that extra singular subarray, thus result[i] = result[i-1] + A[i]

from ast import List


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        modulo = 10**9+7        
        arr = [0] + arr # 加一位prefix 0, making (i-j) at least 1

        res = [0] * len(arr)
        stack = []
        
        for i in range(len(arr)):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop() 
            
            if stack: 
                j = stack[-1]
                res[i] = res[j] + (i-j)*arr[i]

            stack.append(i)
            
        return sum(res) % modulo
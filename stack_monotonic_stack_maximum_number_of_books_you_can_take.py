# FAV

from ast import List

# Monotonic stack + DP, ref: https://leetcode.com/problems/maximum-number-of-books-you-can-take/solutions/2367084/python3-increasing-stack-only-record-sudden-changes/
class Solution:
    def maximumBooks(self, books: List[int]) -> int:
        res = 0
        """
        increasing stack stores [x, y], where
        x -> indices when number of books are smaller than the triangle slope
        y -> the best result starting from index `x` to the left
        """
        stack = [] # [x, y]
        for i in range(len(books)):
            while stack and books[stack[-1][0]] + (i - stack[-1][0]) >= books[i]:
                stack.pop()
            
            last_idx, last_res = -1, 0
            if stack:
                last_idx, last_res = stack[-1]
            
            # calculate the maximum of books we can take at index `i`
            # accumulated res + current round

            height = min(i - last_idx, books[i])
            l1, l2 = books[i] - height + 1, books[i] # upper and lower line of the trapezoid
            current_res = last_res + ((l1 + l2) * height // 2)

            stack.append([i, current_res])
            res = max(res, current_res)

        return res

# TLE, pass 70/84
class Solution:
    def maximumBooks(self, books: List[int]) -> int:
        """
        create a monotonic decreasing stack
            -> started from the end of the given array

        if there is no element in the stack
            -> push
        
        if there is one or more elements in the stack
            -> if the next number is smaller than the number, stack[-1]
                -> push the element in it
            -> if the next number is larger than or equal to the number, stack[-1]
                -> get the sum of the stack
                    -> + `stack[-1] - 1`
                    -> goes on adding the potential books that we could take (while loop)
                -> clean the stack
        """
        stack = []
        curr_sum = 0
        res = 0
        for i in range(len(books) - 1, -1, -1):
            if not stack:
                stack.append(books[i])
                curr_sum += books[i]
                continue
            
            if books[i] < stack[-1]:
                stack.append(books[i])
                curr_sum += books[i]
            else:
                top_num = stack[-1]
                j = i
                while j >= 0 and top_num - 1 >= 0:
                    valid_num = min(books[j], top_num - 1)
                    curr_sum += valid_num
                    top_num = valid_num
                    j -= 1

                res = max(res, curr_sum)
                curr_sum = books[i]
                stack = [books[i]]

        return max(res, curr_sum)


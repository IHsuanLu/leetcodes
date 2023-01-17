# FAV
# two-pass, greedy approach
class Solution:
    def minimumDeletions(self, s: str) -> int:
        left_b_count = 0
        right_a_count = 0
        for i in range(len(s)):
            if s[i] == 'a':
                right_a_count += 1
        
        res = len(s)
        for i in range(len(s)):
            res = min(res, right_a_count + left_b_count)
            if s[i] == 'a':
                right_a_count -= 1
            elif s[i] == 'b':
                left_b_count += 1
        
        return min(res, right_a_count + left_b_count)

# one-pass, stack
class Solution:
    def minimumDeletions(self, s: str) -> int:
        count = 0
        stack = []        
        for c in s:
            if c == 'b':
                stack.append(c)
            elif stack:
                stack.pop()
                count += 1
        return count
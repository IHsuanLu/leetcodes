# Top-down DFS + Memoization
"""
How did we reduce the time complexity from O(2^N) to O(N^2)?

- finding the Space complexity of memoized top-down recursive solutions is always a great way arrive at the time complexity. Why? Because they are the same. Yet somehow space comlexity of such algorithms is easier to wrap our heads around.
- the dimensions of your memoization matrix is basically the time complexity
- You have l, r pointers. l pointer iterates over the entire length of the input from start to end. So does the r pointer but in the opposite direction. They do that independently of each other and despite of memoization as can be seen in the visual. Hence the input is scanned twice. hence the O(N^2) time complexity

"""

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        memo = {}
        def dfs(l, r):
            # singleton -> count 1
            if l == r:
                return 1
            
            # all chars scanned - out of bounds
            if l > r:
                return 0

            if (l, r) in memo:
                return memo[(l, r)]

            if s[l] == s[r]:
                # count 2 and recurse on double-sided shrinking subseq
                memo[(l, r)] = 2 + dfs(l + 1, r - 1)
                return memo[(l, r)]
            
            left_count = dfs(l, r - 1)
            right_count = dfs(l + 1, r)
            memo[(l, r)] = max(left_count, right_count)

            return memo[(l, r)]
        
        return dfs(0, len(s) - 1)


# backtracking -> TLE
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        max_val = [0]
        memo = {}

        def backtrack(idx, path):
            if idx in memo:
                return memo[idx]

            if path == path[::-1]:
                max_val[0] = max(max_val[0], len(path))

            for i in range(idx, len(s)):
                path.append(s[i])
                memo[idx] = path

                backtrack(i + 1, path)

                path.pop()
                del memo[idx]
            
        backtrack(0, [])
        return max_val[0]
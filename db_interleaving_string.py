# we need to setup two pointers i1 and i2 to keep track the positions we're at in `s1` and `s2`
# the position of the `s3` can be calculated by i1 + i2

# if s3[i1+i2] matches only either s1[i1] or s2[i1]
#   then that one should be the decsion
# elif s3[i1+i2] matches both s1[i1] and s2[i1]
#   then we're going to do backtrack and try every posibillity to determine which substring to choose

# time complexity w/o memoization O(2^(n+m)), n + m is the length of s3
# time complexity w/ memoization O(n*m)

# what is the overrlapping subproblem?
#   we can store, from the pointer set (i1, i2), whether or not can we form the given string s3 
# we can using dp(caching) or dfs(memoization) to reduce the time complexity down to O(n*m)

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != (len(s1) + len(s2)):
            return False
        
        def dfs(idx1, idx2, memo):
            if idx1 == len(s1) and idx2 == len(s2):
                return True
            
            if (idx1, idx2) in memo:
                return memo[(idx1, idx2)]
            
            if idx1 < len(s1) and s1[idx1] == s3[idx1+idx2]:
                res = dfs(idx1 + 1, idx2, memo)
                if res: 
                    return True
            
            if idx2 < len(s2) and s2[idx2] == s3[idx1+idx2]:
                res = dfs(idx1, idx2 + 1, memo)
                if res: 
                    return True
            
            memo[(idx1, idx2)] = False
            return False
        
        return dfs(0,0,{})
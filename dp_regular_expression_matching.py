# draw decision trees (O(2^n) when encounter "*" -> dp memoization -> O(N^2)) for the followings for the clearer vision
# aa, a*

# s = a a b, c * a * b = p
#     i      j
#
# -> not gonna use the "*" after "c", according to the decision tree 
#   -> (i, j+2)
#
# s = a a b, c * a * b = p
#     i          j
#
# we find "s[i] == p[j]", we can shift "i"
#   -> (i+1, j)
#
# s = a a b, c * a * b = p
#       i        j
# 
#   -> (i+1, j)
# s = a a b, c * a * b = p
#         i      j
#
#
#   -> (i, j+2)
# s = a a b, c * a * b = p
#         i          j
# 
# compare the two characters
#
#   -> (i+1, j+1)
# s = a a b  , c * a * b   = p
#           i            j
#
# return True
#
#
# if i and j are both out of bounds -> then the two strings match
# what if i is inbound and j is out of bound?
#   -> return False (s = aa; p = a)
#
# what if j is inbound and i is out of bound?
#   -> (s = a  ; p = a * b *)
#             i          j 
#   -> Not necessarily should return False

# solution with memoization
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # top-down memoization dp solution
        memo = {}
        
        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i >= len(s) and j >= len(p):
                return True
            elif j >= len(p):
                # only j is out of bound
                return False

            
            # Note that i is still can be out of bound
            match = i < len(s) and (s[i] == p[j] or p[j] == ".")
            if (j + 1) < len(p) and p[j + 1] == "*":
                res_skipping_star = dfs(i, j+2) # don't use the "*"

                # we can only use the "*" if there is a match
                res_using_star = False
                if match:
                    res_using_star = dfs(i+1, j) # use the "*"
                
                print("write", (i,j), res_skipping_star or res_using_star)
                memo[(i, j)] = res_skipping_star or res_using_star
                # if either way returns True, then we can return True
                return res_skipping_star or res_using_star
            
            # for no star cases, we are simply comparing two chars
            if match:
                res_comparing_chars = dfs(i+1, j+1)
                memo[(i, j)] = res_comparing_chars
                return res_comparing_chars
            
            # if no star and not match, return False directly
            return False
        
        return dfs(0, 0)

# line 72 print 
# write (3, 4) False
# write (2, 4) False
# write (1, 4) False
# write (0, 4) False
# write (0, 2) False
# write (1, 2) False
# write (2, 2) False
# write (7, 4) True
# write (6, 4) True
# write (5, 4) True
# write (4, 4) True
# write (4, 2) True
# write (3, 2) True
# write (3, 0) True
# write (2, 0) True
# write (1, 0) True
# write (0, 0) True
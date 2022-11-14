# parenthesis
#   - a left has to have a corresponding right; 
#   - right cannot go first (len(left) >= len(right) at any given point); 
#   - in a FIFO natural order 

# brute force apporoach
# how to deal with wildcard?
#   -> use desicion tree and list out every possibility
#   -> run recursively for every possibility once meeting *
#   -> keep track of number of '('


# Dynamic Programming: O(n^2)
class Solution:
    def checkValidString(self, s: str) -> bool:
        dp = {(len(s), 0): True}  # key=(i, leftCount) -> isValid

        def dfs(i, left_count):
            if i == len(s) or left_count < 0:
                return left_count == 0
            if (i, left_count) in dp:
                return dp[(i, left_count)] 

            if s[i] == "(":
                dp[(i, left_count)] = dfs(i + 1, left_count + 1)
            elif s[i] == ")":
                dp[(i, left_count)] = dfs(i + 1, left_count - 1)
            else:
                dp[(i, left_count)] = (
                    dfs(i + 1, left_count + 1) or dfs(i + 1, left_count - 1) or dfs(i + 1, left_count)
                )
            return dp[(i, left_count)]

        return dfs(0, 0)


# Greedy: O(n)
# use multiple variables to store multiple possibilities (left_max, left_min) 
#   -> represent the range of the possibilities
#   -> if the range contains "0" return "True"
#
# note that we will reset left_min to "0" if it happens to be negative, yet the left_max should stay the same cause we wanna handle the case like `))((` 
#   -> (left_min = 0; left_max = -2) -> return False 
class Solution:
    def checkValidString(self, s: str) -> bool:
        left_min, left_max = 0, 0 # remained left paramethesis
        
        for c in s:
            if c == "(":
                left_min += 1
                left_max += 1
            elif c == ")":
                left_min -= 1
                left_max -= 1
            else:
                # wildcard, if empty string, we don't update the count
                left_min -= 1 # )
                left_max += 1 # (
            
            if left_max < 0:
                return False
            
            # but left_max is not negative, chances are the string is still valid
            if left_min < 0: # s like "( * ) (" will fail if there is this line of adjustment
                left_min = 0           
        
        return left_min == 0

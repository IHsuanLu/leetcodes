# draw decision tree
# "25525511135" -> how to make a decision?
# -> placing three dots in the string, so where to put the first dot?

# first dot (only continue to the next decision if the first partitioned integer is valid)
#   2.5525511135
#   25.525511135
#   255.25511135
from ast import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        
        if len(s) > 12:
            return res
        
        def backtrack(idx, dots, path):
            # base cases
            if dots == 4 and idx == len(s):
                res.append(path[:-1]) # remove the last dot
                return
            if dots > 4:
                return
            
            for i in range(idx, min(idx + 3, len(s))): # prevent out of bound
                if int(s[idx:i+1]) <= 255 and (len(s[idx:i+1]) == 1 or s[idx:i+1][0] != "0"):
                    backtrack(i + 1, dots + 1, path + s[idx:i+1] + ".")
                    # don't neet to pop cause, unlike passing array, we are not reusing the same reference again and again

        backtrack(0, 0, "")
        return res


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        
        if len(s) > 12:
            return res
        
        def backtrack(idx, dots, path):
            # base cases
            if dots == 4 and idx == len(s):
                res.append(".".join(path[:])) # remove the last dot
                return
            if dots > 4:
                return
            
            for i in range(idx, min(idx + 3, len(s))): # prevent out of bound
                if int(s[idx:i+1]) <= 255 and (len(s[idx:i+1]) == 1 or s[idx:i+1][0] != "0"):
                    path.append(s[idx:i+1])
                    backtrack(i + 1, dots + 1, path)
                    path.pop()
        
        backtrack(0, 0, [])
        return res
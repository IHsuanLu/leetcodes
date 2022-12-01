from ast import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:    
        res = l = r = 0
        while r < len(neededTime):
            while r < len(neededTime) and colors[r] == colors[l]:
                r += 1
                continue
            
            if r - l > 1:
                # there is adjacent
                max_val = max(neededTime[l:r])
                res += sum(neededTime[l:r]) - max_val
                l = r
            else:
                # there is no adjacent
                l += 1
            # move r
            r += 1

        return res


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:    
        res = 0
        r = l = 0
        
        while r < len(neededTime):
            curr_total = 0
            curr_max = 0
            # shift r if the chars are the same
            while r < len(neededTime) and colors[l] == colors[r]:
                curr_total += neededTime[r]
                curr_max = max(curr_max, neededTime[r])
                r += 1
            
            res += curr_total - curr_max
            l = r
        
        return res
                
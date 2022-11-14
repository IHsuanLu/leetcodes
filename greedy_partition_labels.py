from ast import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # a: (0, 8)
        # b: (1, 5)
        # c: (4, 7)
        # d: (9, 14)
        # e: (10, 15)
        # h: (16, 19)
        # i: (17, 22)
        # j: (18, 23)
        # k: (20, -1)
        # l: (21, -1)
        # when a tail meets a head
        memo = {}
        res = []
        for i in range(len(s)):
            if s[i] in memo:
                memo[s[i]] = (memo[s[i]][0], i)
            else:
                memo[s[i]] = (i, i)
        
        curr_max_end = -1
        tuples = list(memo.values())
        for i in range(len(tuples)):
            curr_max_end = max(curr_max_end, tuples[i][1])
            if i + 1 < len(tuples) and curr_max_end + 1 == tuples[i + 1][0]:
                res.append(tuples[i + 1][0] if not res else tuples[i + 1][0] - sum(res))

        res.append(len(s) - sum(res))
        return res


# Neetcode solution
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        memo = {} # char -> last_index in s
        
        for i, c in enumerate(s):
            memo[c] = i
        
        res = []
        # end is the pointer for the end of the partition
        # update the "end", if some other characters have the last_index > end
        size = end = 0 
        for i, c in enumerate(s):
            size += 1
            if memo[c] > end:
                end = memo[c]
            
            if i == end: # means the substring before has every appeared characters
                res.append(size)
                size = 0
        
        return res
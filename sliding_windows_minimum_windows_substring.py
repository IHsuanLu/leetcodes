# hold two maps one for s, the other for t.
# keep the "have" and "need" count, and increment the "have" count if the key iterated matches "need_map"
# only check if have_count == need_count, if yes then the map is equal

# slide window
# remove the left-most character, update the have count
# keep forwarding until the have_count meets the need_count
# start popping and removing the redundant count if applicable
# pop one more character and fail the match of the have_count and the need_count
# resume forwarding until the have_count meets the need_count

# if we compare map while running the loop, we can do it on leaner time


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""        
        
        s_memo, t_memo = {}, {}
        for c in t:
            t_memo[c] = 1 + t_memo.get(c, 0)
            
        have, need = 0, len(t_memo)
        res, res_length = [-1, -1], float('inf')
        
        l = 0
        for r in range(len(s)):
            c = s[r]
            
            # update map once iterated to the charactor
            s_memo[c] = 1 + s_memo.get(c, 0)
            
            # does s_memo satisfy the needs of t_memo
            if c in t_memo and s_memo[c] == t_memo[c]:
                have += 1 # update have count

            # does have count meets need count
            while have == need:
                # update the result
                if (r - l + 1) < res_length: # if the window's size smaller than res 
                    res = [l, r]
                    res_length = (r - l + 1)
                
                # shrink the window, pop from the left of the window
                s_memo[s[l]] -= 1
                if s[l] in t_memo and s_memo[s[l]] < t_memo[s[l]]:
                    have -= 1
                
                l += 1
        
        l, r = res
        return s[l:r+1] if res_length != float('inf') else ""
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:        
        counter = {}
        for c in s:
            counter[c] = counter.get(c, 0) + 1
        
        longest = 0
        
        # Repeat the same process for max_unique_chars_allowed = 2, 3, 4, ... and how many unique chars do we have in the initial problem? 26 (lowercase). We can reduce 26 to count of unique chars in the strings later.
        for max_unique_chars_count in range(1, len(counter.keys()) + 1):
            hmap = {}
            curr_unique_chars_count = 0
            
            l = 0
            for r, c in enumerate(s):
                if c in hmap:
                    hmap[c] += 1
                else:
                    hmap[c] = 1
                    curr_unique_chars_count += 1
                
                while curr_unique_chars_count > max_unique_chars_count:
                    hmap[s[l]] -= 1
                    
                    if hmap[s[l]] == 0:
                        del hmap[s[l]]
                        curr_unique_chars_count -= 1
                        
                    l += 1

                if all(i >= k for i in hmap.values()):
                    longest = max(longest, r - l + 1)
            

        return longest

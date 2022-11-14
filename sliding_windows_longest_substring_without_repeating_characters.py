class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        memo = set()
        longest = i = j = 0

        # if the index is not updated, the same loop will run multiple times
        while i <= len(s) - 1:
            if not s[i] in memo:
                memo.add(s[i])
                i += 1
            else:
                # keep removing until the char[i] no longer in the set 
                memo.remove(s[j]) 
                j += 1
            longest = max(longest, i - j)

        return longest
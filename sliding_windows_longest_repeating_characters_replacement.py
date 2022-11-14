# we want to replace the characters that are less frequent in the window
# the length of the window - count of the most frequent character = number of the characters in the window that need replacement
# sliding windows -> started at the beginning and expand as much as possible, as long as the condition is valid; if not, shift the left pointer

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        memo = {}
        longest = j = 0
        for i in range(len(s)):
            memo[s[i]] = 1 + memo.get(s[i], 0)
            
            while (i - j + 1) - max(memo.values()) > k:
                memo[s[j]] -= 1
                j += 1
            
            longest = max(longest, (i - j + 1))
                
        return longest


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        memo = {}
        longest = i = j = 0
        for char in s:
            if char not in memo:
                memo[char] = 1
            else:
                memo[char] += 1
            
            if (i - j + 1) - max(memo.values()) > k:
                memo[s[j]] -= 1
                j += 1
            
            longest = max(longest, (i - j + 1))
            i+=1
                
        return longest
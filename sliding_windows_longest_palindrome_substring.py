# O(N * N^2) => O(N^2)
# loop through every possibilities(N^2) and check if palindrome(N) => loop through every character(N) and expand to left and right(N)
# how about the even palindrome? 
#   -> tackle them as the edge case parallelly with the odd case

# the optimized way of doing it is, starting from the middile and expanding outward
#   -> what is the longest palindrome with every character as the center of the palindrome
#   -> check if the new expanded characters are the same

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        res_length = 0
        
        for i in range(len(s)):
            r = l = i
            # odd length
            while r < len(s) and l >= 0 and s[r] == s[l]:
                # it's palindrome
                if (r - l + 1) > res_length:
                    res = s[l:r + 1]
                    res_length = r - l + 1
                
                r += 1
                l -= 1
        
            # even length
            l, r = i, i+1
            while r < len(s) and l >= 0 and s[r] == s[l]:
                # it's palindrome
                if (r - l + 1) > res_length:
                    res = s[l:r + 1]
                    res_length = r - l + 1
                
                r += 1
                l -= 1
                
        return res
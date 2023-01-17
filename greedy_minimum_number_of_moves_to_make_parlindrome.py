# FAV

"""
Why greedy works?

- we cannot do unnecessary moves (https://leetcode.com/problems/minimum-number-of-moves-to-make-palindrome/solutions/1847011/c-2-pointers-with-detail-proof-and-explanation/)

- in the example `abcdabcd`
    - if you keep right end 'd' still, you know that all the other letters are to its left. 
      So when you find and swap the nearest 'd' to left end, 
      you are sure that every single swap you make isn't unnecessary, 
      because 'd' should be in front of all of them.

- special case `abcdabczd`
    - Notice here, you should avoid trying to swap the 'z' to the center before the whole process ends. 
      That is because at this time you can't guarantee all the swap you do is necessary.
"""

# iterative
class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        res = 0
        s = list(s)
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                curr = r
                while l < curr and s[curr] != s[l]:
                    curr -= 1

                # if there is no pair with the character (it should be in the middle)
                if curr == l:
                    res += 1
                    s[l], s[l + 1] = s[l + 1], s[l]
                else:
                    while curr < r:
                        res += 1
                        s[curr], s[curr + 1] = s[curr + 1], s[curr]
                        curr += 1

                    l += 1
                    r -= 1
            else:
                l += 1
                r -= 1

        return res

# recursive
class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        """
        letelt
        lettel
        """
        res = [0]
        s = list(s)
        def find_and_swap(l, r):
            if l >= r:
                return 

            curr = r
            while l < curr and s[curr] != s[l]:
                curr -= 1

            # if there is no pair with the character (it should be in the middle)
            if curr == l:
                res[0] += 1
                s[l], s[l + 1] = s[l + 1], s[l]
            else:
                while curr < r:
                    res[0] += 1
                    s[curr], s[curr + 1] = s[curr + 1], s[curr]
                    curr += 1
                
                l += 1
                r -= 1

            find_and_swap(l, r)

        find_and_swap(0, len(s) - 1)
        return res[0]
        

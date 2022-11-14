from ast import List


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        hmap = {}
        res = 0
        for w in words:
            hmap[w] = hmap.get(w, 0) + 1
        
        central = False
        for k, v in hmap.items():
            if k[0] == k[1]:
                if v % 2 == 0:
                    res += (v * 2)
                else:
                    # 都先加偶數組
                    res += ((v - 1) * 2)
                    central = True
            # consider a pair of non-palindrome words,
            # such that one is the reverse of another
            # word[1] + word[0] is the reversed word             
            elif k[0] < k[1]: # use < so that we don't count duplicates
                res += (2 * min(v, hmap.get(k[::-1], 0))) * 2

        # 最後再補central組給第一個奇數pair 
        if central:
            res += 2
        
        return res
# brute force; backtrack to get all bit substrings of lenght k -> check if all in the given string s
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        counter = {"0": k, "1": k}
        
        res = list([])
        def backtrack(path, memo):
            if len(path) == k:
                res.append("".join(path[:]))
                return
            
            for n in memo:
                path.append(n)
                memo[n] -= 1
                
                backtrack(path, memo)
                
                path.pop()
                memo[n] += 1
                
        backtrack([], counter)
                
        for r in range(0, len(s) - k + 1):
            if s[r:r+k] in res:
                res.remove(s[r:r+k])
        
        return len(res) == 0


# hash set + bit manipulation -> we don't actually need to generate the substrings
# we just need to know if the count of the substrings of s equals to 1 << k (2^k)
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool: 
        hset = set()
        for r in range(0, len(s) - k + 1):
            hset.add(s[r:r+k])
                    
        return len(hset) == 1 << k
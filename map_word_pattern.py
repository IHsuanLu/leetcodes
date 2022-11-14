class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        arr = s.split(" ")
        if len(pattern) != len(arr):
            return False
        
        hmap = {}
        reserved = set()
        for i in range(len(arr)):
            if pattern[i] in hmap:
                if hmap[pattern[i]] != arr[i]:
                    return False
            else:
                if arr[i] in reserved:
                    return False
                hmap[pattern[i]] = arr[i]
                reserved.add(arr[i])
                
        return True
from ast import List

# space: O(n)
class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            chars[:] = chars[0]
            return 1

        def _append_res(char, count):
            if count > 1: 
                res.extend([char, *str(count)])
            else:
                res.append(char)

        l = 0
        res = []
        for r in range(1, len(chars)):
            if chars[r] != chars[r - 1]:
                count = (r - 1) - l + 1
                _append_res(chars[l], count)
                l = r
            
            if r == (len(chars) - 1):
                count = r - l + 1
                _append_res(chars[l], count)

        chars[:] = res
        return len(chars)


# space: O(1)
class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            chars[:] = chars[0]
            return 1

        def _append_res(idx, char, count):
            arr = [char]
            if count > 1:
                arr.extend([*str(count)])
            for ele in arr:
                chars[idx] = ele
                idx += 1
                            
            return idx

        l = 0
        curr = 0
        for r in range(1, len(chars)):
            if chars[r] != chars[r - 1]:
                count = (r - 1) - l + 1
                curr = _append_res(curr, chars[l], count)
                l = r
            
            if r == (len(chars) - 1):
                count = r - l + 1
                curr = _append_res(curr, chars[l], count)
        
        chars[:] = chars[:curr]
        return len(chars)
from ast import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letter_map = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        
        res = []
        def dfs(curr_digit_idx, path):
            if curr_digit_idx >= len(digits):
                res.append(path)
                return
            
            letters = letter_map[digits[curr_digit_idx]]
            for letter in letters:
                # 26-28 => dfs(curr_digit_idx + 1, path + letter)
                path += letter
                dfs(curr_digit_idx + 1, path)
                path = path[:-1]
        
        if digits:
            dfs(0, "")
        
        return res
#FAV

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        modulo = 10**9+7
        adjacents = {
            'a': ['e'],
            'e': ['a', 'i'],
            'i': ['a', 'e', 'o', 'u'],
            'o': ['i', 'u'],
            'u': ['a']
        }

        memo = {}
        def dfs(node, remaining_n):
            if remaining_n == 0:
                return 1
            
            if (node, remaining_n) in memo:
                return memo[(node, remaining_n)]

            sum_val = 0
            for neighbor in adjacents[node]:
                sum_val += dfs(neighbor, remaining_n - 1)

            memo[(node, remaining_n)] = sum_val
            return sum_val


        res = 0
        for key in adjacents:
            res += dfs(key, n - 1)

        return res % modulo


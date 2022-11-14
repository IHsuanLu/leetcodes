class Solution:
    def numDecodings(self, s: str) -> int:
        PREFIXES = [str(i) for i in range(1, 27)]
        def dfs(current_idx, memo):
            if len(s) == current_idx:
                return 1
            if current_idx in memo:
                return memo[current_idx]

            ways = 0
            remaining = s[current_idx:]

            for prefix in PREFIXES:
                if remaining.startswith(prefix):
                    ways += dfs(current_idx + len(prefix), memo)

            memo[current_idx] = ways
            return ways
        
        return dfs(0, {})


class Solution:
    def numDecodings(self, s: str) -> int:
        def dfs(current_idx, memo):
            if len(s) == current_idx:
                return 1 
            if current_idx in memo:
                return memo[current_idx]
            if s[current_idx] == "0":
                return 0
            
            res = dfs(current_idx + 1, memo)
            if current_idx + 1 < len(s) and (s[current_idx] == "1" or (s[current_idx] == "2" and s[current_idx + 1] in "0123456")):
                res += dfs(current_idx + 2, memo)

            memo[current_idx] = res
            return res
        
        return dfs(0, {})
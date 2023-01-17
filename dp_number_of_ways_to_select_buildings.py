# FAV

# prefix_sum
class Solution:
    def numberOfWays(self, s: str) -> int:
        """
        - treat index as the middle of the solution
            - for 1 -> we want it to form "010"
            - for 0 -> we want it to form "101"
        -> add up all the products while iterating thru the prefix array
        """
        prefixes = [[0, 0] for _ in range(len(s))] 
        for i in range(len(s)):
            zero_count = prefixes[i][0] + 1 if s[i] == "0" else 0
            one_count = prefixes[i][1] + 1 if s[i] == "1" else 0

            if i > 0:
                zero_count += prefixes[i - 1][0]
                one_count += prefixes[i - 1][1]
            
            prefixes[i] = [zero_count, one_count]         

        res = 0
        for i in range(len(s)):
            if s[i] == "0":
                res += prefixes[i][1] * (prefixes[-1][1] - prefixes[i][1])
            elif s[i] == "1":
                res += prefixes[i][0] * (prefixes[-1][0] - prefixes[i][0])

        return res


# brute force -> TLE
class Solution:
    def numberOfWays(self, s: str) -> int:
        res = [0]
        def dfs(idx, path):
            if len(path) == 3:
                res[0] += 1
            
            for i in range(idx + 1, len(s)):
                if not path or (path and path[-1] != s[i]):
                    dfs(i, path + s[i])
        
        dfs(-1, "")
        return res[0]
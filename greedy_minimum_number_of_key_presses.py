# Without extra space 
class Solution:
    def minimumKeypresses(self, s: str) -> int:
        counter = {}
        for c in s:
            counter[c] = counter.get(c, 0) + 1

        res = 0
        for i, value in enumerate(sorted(counter.values(), reverse=True)):
            press = (i // 9) + 1
            res += press * value
            
        return res


# With extra space
class Solution:
    def minimumKeypresses(self, s: str) -> int:
        counter = {}
        for c in s:
            counter[c] = counter.get(c, 0) + 1

        costs = [0] * 26
        level = [1, 9] # level, space
        res = 0
        for key in sorted(counter, key=counter.get, reverse=True):
            code = ord(key) - ord('a')
            if costs[code] != 0:
                res += costs[code] * counter[key]
            else:
                costs[code] = level[0]
                res += costs[code] * counter[key]
                level[1] -= 1
                if level[1] == 0:
                    level = [level[0] + 1, 9]

        return res
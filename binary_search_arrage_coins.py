# exclude equal case
class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n == 1:
            return 1

        def get_sum(val):
            return ((1 + val) * val) // 2

        l, r = 1, n
        res = -1
        while l < r:
            mid = (l + r) // 2
            sum_val = get_sum(mid)

            if sum_val > n:
                r = mid
            else:
                res = max(res, mid)
                l = mid + 1

        return res

# include equal case
class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n == 1:
            return 1

        def get_sum(val):
            return ((1 + val) * val) // 2

        l, r = 1, n
        while l <= r:
            mid = (l + r) // 2
            sum_val = get_sum(mid)

            if sum_val > n:
                r = mid - 1
            elif sum_val < n:
                l = mid + 1
            else:
                return mid

        return r
from ast import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        res = [0] + [1] * len(ratings) + [0]
        ratings = [float('inf')] + ratings + [float('inf')]

        for i in range(1, len(ratings) - 1):
            if ratings[i] > ratings[i - 1]:
                res[i] = res[i - 1] + 1

        for i in range(len(ratings) - 2, 0, -1):
            if ratings[i] > ratings[i + 1] and res[i] <= res[i + 1]:
                res[i] = res[i + 1] + 1
        
        return sum(res)
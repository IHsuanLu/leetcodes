from ast import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]

        dp = [None] * numRows
        dp[0], dp[1] = [1], [1, 1]
        
        for i in range(2, numRows):
            temp = []
            for j in range(1, i):
                temp.append(dp[i - 1][j - 1] + dp[i - 1][j])

            dp[i] = [1] + temp + [1]
        
        return dp
# check how many diagonals do we get?
#   => MxN matrix, number of diagonals = M + N - 1

# 1 2 3
# 4 5 6
# 7 8 9

# 5 diagonals
# how do we know which element fits in which array?
# sum of (x, y) should be no. of diagonal - 1

# [1]
# [2,4]
# [3,5,7]
# [6,8]
# [9]

# note that the top-down traverse has the default sequence
# we just need to reverse the even row
from ast import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        row_num, col_num = len(mat), len(mat[0])
        diagonals = [[] * n for n in range(row_num + col_num - 1)]
        res = []
                
        for r in range(row_num):
            for c in range(col_num):
                diagonals[r + c].append(mat[r][c])
                
        for i in range(len(diagonals)):
            d = diagonals[i][::-1] if i % 2 == 0 else diagonals[i]
            for n in d:
                res.append(n)
                
        return res


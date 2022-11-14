# O(m * n * 4 ^ $WORD_LENGTH)
# setup the base case
# remainings are every other valid round
from ast import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        num_rows, num_cols = len(board), len(board[0])
        visited = set() # make sure we don't reuse the same cell, (row, col) tuple
        
        def dfs(row, col, curr_char_idx):
            if curr_char_idx == len(word):
                return True
            
            # out of bound
            if row < 0 or col < 0 or row >= num_rows or col >= num_cols:
                return False
            
            # incorrect answer
            if word[curr_char_idx] != board[row][col]:
                return False
            
            # already visited
            if (row, col) in visited:
                return False
            
            # record visited path
            visited.add((row, col))
                    
            # check adjacent cells
            res = (
                dfs(row + 1, col, curr_char_idx + 1) or
                dfs(row - 1, col, curr_char_idx + 1) or
                dfs(row, col + 1, curr_char_idx + 1) or
                dfs(row, col - 1, curr_char_idx + 1)
            )
            
            # clean up visited path for the next recusive call
            visited.remove((row, col))

            return res
        
        
        for i in range(num_rows):
            for j in range(num_cols):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
        
        return False
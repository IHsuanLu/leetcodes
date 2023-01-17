# FAV

from ast import List

# brute force w/ memoization, O(cols * n + rows)
class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        idx, res = 0, 0
        memo = {} # {word_idx: [complete_word_count, next_start_word_idx]}
        
        for _ in range(rows):
            start_word_idx = idx
            if start_word_idx in memo:
                _count, _idx = memo[start_word_idx]
                idx = _idx
                res += _count
            else:
                complete_word_count = 0

                #  ----------- brute force approach -----------
                col = 0
                if len(sentence[idx]) > cols:
                    return 0
                while col + len(sentence[idx]) <= cols:
                    col += len(sentence[idx])
                    if col < cols:
                        col += 1

                    idx = (idx + 1) % len(sentence)
                    if idx == 0: 
                        complete_word_count += 1
                #  ----------- brute force approach -----------

                memo[start_word_idx] = [complete_word_count, idx]
                res += complete_word_count

        return res


# brute force, O(rows * cols) -> TLE
class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        idx, res = 0, 0

        for _ in range(rows):
            col = 0
            if len(sentence[idx]) > cols:
                return 0
            while col + len(sentence[idx]) <= cols:
                col += len(sentence[idx])
                if col < cols:
                    col += 1

                idx = (idx + 1) % len(sentence)
                if idx == 0: 
                    res += 1

        return res

# brute force -> maximum recursion depth exceeded
class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        res = [0]
        def dfs(idx, remained_row, remained_col):
            next_idx = idx + 1 if idx + 1 < len(sentence) else 0
            if remained_col - len(sentence[idx]) >= 0:                
                remained_col -= len(sentence[idx])
                if remained_col > 0:
                    remained_col -= 1

                if idx >= len(sentence) - 1:
                    res[0] += 1
            
                dfs(next_idx, remained_row, remained_col)
            elif remained_row > 0:
                dfs(idx, remained_row - 1, cols)

        dfs(0, rows - 1, cols)
        return res[0]

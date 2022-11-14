# base case 1
#   if both `word1` and `word2` are empty; return 0
# base case 2
#   if either `word1` or `word2` is empty; return the length of the non-empty one

"""
if not word1 and not word2:
    return 0
if not word1:
    return len(word2)
if not word2:
    return len(word1)
"""

# if the word1[idx1] == word[idx2]
#   we will get the new subproblem of checking word1[idx1 + 1] == word[idx2 + 1]
#   operation_count = 0
# else
#   try `insert` -> (idx1, idx2 + 1)
#       `delete` -> (idx1 + 1, idx2) 
#       `replace` -> (idx1 + 1, idx2 + 1)
#   operation_count = 1

# **we don't know which one will lead us to the minimum operation** -> so we need to try 'em all
# 
# insert -> insert word2[idx2] into word1 at index word[idx1 - 1]
#        -> we don't need to move around `idx1`, and we can assume word2[idx2] has a match and move `idx2` to the next position

# delete -> ignore the character word1[idx1]

# replace -> replace the character word1[idx1] with word2[idx2]
#         -> both of them move on to the next round


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:        
        def dfs(i, j, memo):
            if i == len(word1) or j == len(word2):
                # if either one has not reached the end, we need to add the length to the operations
                return (len(word1) - i) + (len(word2) - j)
            
            if (i, j) in memo:
                return memo[(i, j)]
            
            count = 0
            if word1[i] == word2[j]:
                count += dfs(i + 1, j + 1, memo)
            else:
                insert_count = dfs(i, j + 1, memo) # Insert
                delete_count = dfs(i + 1, j, memo) # Delete
                replace_count = dfs(i + 1, j + 1, memo) # Replace
                count += min(insert_count, delete_count, replace_count) + 1
            
            memo[(i, j)] = count
            return count
        
        return dfs(0, 0, {})
# mark down the occurance of the currSum; if the `currSum - targetSum`` happen to be in the memo, meaning that
# from the node, where its currSum equals to the current round's `currSum  - target`, to current round's node,
# the sum should be target sum

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        memo = {0:1}
        res = [0]

        def dfs(root, prevSum, targetSum):
            if not root:
                return 0

            currSum = prevSum + root.val
            
            if currSum - targetSum in memo:
                res[0] += memo[currSum - targetSum]

            if currSum in memo:
                memo[currSum] += 1
            else:
                memo[currSum] = 1
            
                
            dfs(root.left, currSum, targetSum)
            dfs(root.right, currSum, targetSum)

            # backtracking
            memo[currSum] -= 1

                    
        dfs(root, 0, targetSum)
        
        return res[0]
            

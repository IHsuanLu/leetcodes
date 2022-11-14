# the key is that we cannot split the twice
# once we splited it, we can no longer count the parents
# so we need to calculate two values per node
#   1. the max we can get if we split
#   2. the max we can get if we don't split
# for the (1.), we check with the current max and see if we need to update the max val
# for the (2.), we return to the parent since parents will be interested in only this val

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = root.val
        
        # return max path sum without split
        def dfs(head):
            if not head:
                return 0
            
            left_max = dfs(head.left)
            right_max = dfs(head.right)
            
            left_max = max(left_max, 0)
            right_max = max(right_max, 0)
            
            # compute max sum with split
            self.res = max(self.res, head.val + left_max + right_max)
            
            # we don't wanna wrap max 0 to head.val
            return head.val + max(left_max, right_max)
        
        dfs(root)
        return self.res
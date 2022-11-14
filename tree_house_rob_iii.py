from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:        
        def dfs(node):
            if not node:
                return (0, 0) # robPrev, robNext
            
            left_compo = dfs(node.left)
            right_compo = dfs(node.right)
            
            rob = node.val + left_compo[1] + right_compo[1]
            not_rob = max(left_compo) + max(right_compo)
            
            return (rob, not_rob)
        
        return max(dfs(root))
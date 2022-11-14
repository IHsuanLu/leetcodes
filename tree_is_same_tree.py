from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(l, r):
            if l is None and r is None:
                return True
            
            if l is None or r is None:
                return False
            
            if l.val != r.val:
                return False

            return dfs(l.left, r.left) and dfs(l.right, r.right)
        
        return dfs(p, q)
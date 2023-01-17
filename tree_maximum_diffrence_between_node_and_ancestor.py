from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        curr_max_diff = [-1]
        def dfs(node, curr_max, curr_min):
            if not node:
                return
            
            curr_max_diff[0] = max(curr_max_diff[0], abs(curr_max - node.val), abs(curr_min - node.val))
            curr_max = max(node.val, curr_max)
            curr_min = min(node.val, curr_min)

            dfs(node.left, curr_max, curr_min)
            dfs(node.right, curr_max, curr_min)
        
        dfs(root, root.val, root.val)
        return curr_max_diff[0]
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0

            return max(dfs(node.left), dfs(node.right)) + 1

        degree = dfs(root)
        res = [0]
        def _dfs(node, level):
            if not node:
                return
            if level == degree:
                res[0] += node.val

            _dfs(node.left, level + 1)
            _dfs(node.right, level + 1)
        
        _dfs(root, 1)
        return res[0]

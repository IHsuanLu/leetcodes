class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = [0]
        def dfs(node, max_val):
            if node is None:
                return
            
            if node.val >= max_val:
                res[0] += 1
            
            dfs(node.left, max(max_val, node.val))
            dfs(node.right, max(max_val, node.val))           
            
        dfs(root, float('-inf'))
        
        return res[0]
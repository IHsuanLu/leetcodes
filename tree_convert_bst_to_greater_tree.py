from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# w/o global variable
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node, acc):
            if not node:
                return acc
            
            right_acc = dfs(node.right, acc)
            node.val += left_acc
            left_acc = dfs(node.left, node.val)  
            
            return right_acc
            
        dfs(root, 0)
        return root


# w/ global variable
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        acc = [0]
        def dfs(node):
            if not node:
                return 0
            
            
            dfs(node.right)
            acc[0] += node.val
            node.val = acc[0]
            dfs(node.left)    
            
        
        dfs(root)
        return root
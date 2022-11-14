# key: the in-order traversal of BST is a sorted array, and that's the intuition of solving the problem
# we can easily spot the midplaced nodes `first` and `second`, as **first is larger than the element next to it** while **second is smaller than the element ahead of it**.


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.first = self.second = None
        self.prev = TreeNode(float('-inf'))
        
        def dfs(node):
            if not node:
                return 
            
            dfs(node.left)
            
            if not self.first and self.prev.val >= node.val:
                self.first = self.prev
            if self.first and self.prev.val >= node.val:
                self.second = node
                
            # move the prev pointer before the next round
            self.prev = node
            dfs(node.right)            
            
        dfs(root)        
        self.first.val, self.second.val = self.second.val, self.first.val
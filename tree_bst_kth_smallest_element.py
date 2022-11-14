# BST -> DFS will be traversing in ascending order

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root, k):
        self.k_remained = k
        self.res = 0
        def dfs(head):
            if head is None:
                return
            
            dfs(head.left)
            self.k_remained -= 1
            if self.k_remained == 0:
                self.res = head.val
                return
            
            dfs(head.right)
        
        dfs(root)
        return self.res

    
# iterative solution    
# stack = []
# while root or stack:
#     while root:
#         stack.append(root)
#         root = root.left
#     root = stack.pop()
#     k -= 1
#     if k == 0:
#         return root.val
#     root = root.right
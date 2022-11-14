from ast import List
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def dfs(left, right):
            if left > right:
                return None
            
            root_idx = (left + right) // 2
            
            head = TreeNode(nums[root_idx])
            head.left = dfs(left, root_idx - 1)
            head.right = dfs(root_idx + 1, right)
            
            return head
        
        return dfs(0, len(nums) - 1)
# the key is that we cannot split the twice
# once we splited it, we can no longer count the parents
# so we need to calculate two values per node
#   1. the max we can get if we split
#   2. the max we can get if we don't split
# for the (1.), we check with the current max and see if we need to update the max val
# for the (2.), we return to the parent since parents will be interested in only this val

from ast import List
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        def dfs(node, remained, curr):
            if not node:
                return
            
            curr.append(node.val)
            
            if remained == node.val and not node.left and not node.right:
                res.append(curr[:])
            else:
                dfs(node.left, remained - node.val, curr)
                dfs(node.right, remained - node.val, curr)
                
            curr.pop()
            
        dfs(root, targetSum, [])
        
        return res


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        
        def dfs(node, remained, curr):
            if not node:
                return
            
            curr.append(node.val)
            remained -= node.val

            if remained == 0 and not node.left and not node.right:
                # possible answers
                res.append(curr[:])
            else:
                dfs(node.left, remained, curr)
                dfs(node.right, remained, curr)  

            curr.pop()
            
        
        dfs(root, targetSum, [])
        return res
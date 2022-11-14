# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = deque([root])
        
        res = 1
        while len(queue) > 0:
            for _ in range(len(queue)):
                next = queue.popleft()
                
                children = [next.left, next.right]
                if not children[0] and not children[1]:
                    return res
                
                for child in children:
                    if child:
                        queue.append(child)
                
            res += 1
                    
        return -1
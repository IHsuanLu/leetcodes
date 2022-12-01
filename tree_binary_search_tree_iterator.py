from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.arr = []
        self.curr = -1
        
        while True:
            while root:
                self.stack.append(root)
                root = root.left
            
            if not self.stack:
                break
            
            nxt = self.stack.pop()
            self.arr.append(nxt.val)
            
            root = nxt.right
        

    def next(self) -> int:
        self.curr += 1
        return self.arr[self.curr]

    def hasNext(self) -> bool:
        temp = self.curr + 1
        return temp < len(self.arr)



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        
        while root:
            self.stack.append(root)
            root = root.left


    def next(self) -> int:
        if not self.stack:
            return -1
        
        nxt = self.stack.pop()
        
        if nxt.right:
            root = nxt.right
            while root:
                self.stack.append(root)
                root = root.left
            
        return nxt.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0

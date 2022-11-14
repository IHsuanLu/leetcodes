from typing import Optional


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# iterative version
class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':         
        if not root:
            return None
        
        tail = dummy = Node(-1)
        leftmost = True
        
        def dfs(node):
            nonlocal tail #access tail rom outside the scope
            nonlocal dummy
            nonlocal leftmost
            
            if not node:
                return

            dfs(node.left)
            
            if leftmost:
                dummy = node
                leftmost = False
            
            tail.right = node
            node.left = tail
            tail = node
            
            dfs(node.right)
        
        dfs(root)
        
        dummy.left = tail
        tail.right = dummy

        return tail.right


# recursive version
class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':         
        if not root:
            return None
        
        curr = root
        tail = dummy = Node(-1)
        
        stack = []
        leftmost = True
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
        
            nxt = stack.pop()
            
            if leftmost:
                dummy = nxt
                leftmost = False
                
            tail.right = nxt
            nxt.left = tail
            tail = nxt
            
            nxt = nxt.right
            curr = nxt
            
        dummy.left = tail
        tail.right = dummy
        
        return dummy
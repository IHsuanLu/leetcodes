# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        path = set()
        while p:
            path.add(p)
            p = p.parent 
        while q not in path:
            q = q.parent 
        return q


class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        left_path = []
        def left_to_root(node, path):
            if not node:
                return None
            
            path.append(node.val)
            left_to_root(node.parent, path) 
            
            return node
        
        left_to_root(p, left_path)

        def right_to_root(node):
            if not node:
                return None
            
            if node.val in left_path:
                return node
            
            res = right_to_root(node.parent) 
            
            return res if res else node
                
        return right_to_root(q)
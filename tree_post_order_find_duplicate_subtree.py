from ast import List
from typing import Optional

# Since the question request us to return list of node, so we cannot make up a subset, using backtracking and popping first node in-orderly, then find the duplicate
# instead, we should use post order traversal and store the string into a hash map

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        hmap = {}
        res = []
        def dfs(node, path):
            if node is None:
                return '#'
            
            left = dfs(node.left, path)
            right = dfs(node.right, path)
            
            node_val = str(node.val)
            path += ','.join([left, right, node_val])
            
            hmap[path] = hmap.get(path, 0) + 1
            if hmap[path] == 2:
                res.append(node)
                    
            return path
        
        dfs(root, '')      

        return res

## Wrong solution
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        subsets = []
        def dfs(node, path):
            if node is None:
                subsets.append(path[:])
                return 
            
            
            path.append(node.val)
            
            dfs(node.left, path)
            path.pop(0)
            
            dfs(node.right, path)
            
        ## find the duplicate subset using tuple
            
        dfs(root, [])
        print(subsets)



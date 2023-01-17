# FAV
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# LCA (enhanced) -> accepted, we do not want to append the path on calling the recursive function
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def find_lca(node):
            if not node:
                return None

            if node.val in [startValue, destValue]:
                return node

            left = find_lca(node.left)
            right = find_lca(node.right)

            return node if left and right else left or right

        def dfs(node, path, target):
            if not node:
                return ""
            
            if node.val == target:
                return "".join(path)

            path.append("L")
            left_res = dfs(node.left, path, target)
            path.pop()
            if left_res:
                return left_res
            
            path.append("R")
            right_res = dfs(node.right, path, target)
            path.pop()
            return right_res

        root = find_lca(root)
        start_path = dfs(root, [], startValue)
        dest_path = dfs(root, [], destValue)
        return len(start_path) * "U" + dest_path

# LCA (enhanced) -> TLE, pass 287/332
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def find_lca(node):
            if not node:
                return None

            if node.val in [startValue, destValue]:
                return node

            left = find_lca(node.left)
            right = find_lca(node.right)

            return node if left and right else left or right

        def dfs(node, path, target):
            if not node:
                return ""
            
            if node.val == target:
                return path

            left_res = dfs(node.left, path + "L", target)
            if left_res:
                return left_res

            return dfs(node.right, path + "R", target)

        root = find_lca(root)
        start_path = dfs(root, "", startValue)
        dest_path = dfs(root, "", destValue)
        return len(start_path) * "U" + dest_path


# LCA -> TLE, pass 287/332
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        """
        1. find the lca of two start and dest nodes
        2. implement dfs and start recording the path as we find the start value

        - problems
            - we might find the dest first
            - we can still start recording it, but we need to reverse the output at the end
        """
        def find_lca(node):
            if not node:
                return None

            if node.val in [startValue, destValue]:
                return node

            left = find_lca(node.left)
            right = find_lca(node.right)

            return node if left and right else left or right

        root = find_lca(root)
        first_found = [None]
        def dfs(node, path, depth):
            if not node:
                return ""
            
            if node != root and node.val == startValue:
                if not first_found[0]:
                    first_found[0] = startValue
                return "U" * depth
            if node != root and node.val == destValue:
                if not first_found[0]:
                    first_found[0] = destValue
                return path
            
            left_res = dfs(node.left, path + "L", depth + 1)
            right_res = dfs(node.right, path + "R", depth + 1)

            return left_res + right_res if first_found[0] == startValue else right_res + left_res

        res = dfs(root, "", 0)
        return res
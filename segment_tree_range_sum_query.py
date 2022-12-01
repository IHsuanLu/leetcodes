from ast import List


class SegmentTreeNode:
    def __init__(self, start, end, val=0, left=None, right=None):
        self.start, self.end = start, end
        self.sum = val
        self.left = left
        self.right = right

class NumArray:
    def _build_tree(self, start, end, nums):
        if start == end:
            return SegmentTreeNode(start, end, nums[start])
        mid = (start + end) // 2
        left = self._build_tree(start, mid, nums)
        right = self._build_tree(mid + 1, end, nums)
        return SegmentTreeNode(start, end, left.sum + right.sum, left, right)

    def __init__(self, nums: List[int]):
        self.root = self._build_tree(0, len(nums) - 1, nums)

    
    def _update_tree(self, node, idx, val):
        if not node:
            return 0

        # we find the exact target
        if node.start == node.end == idx:
            node.sum = val
            return node.sum

        mid = (node.start + node.end) // 2
        if idx <= mid:
            left_sum = self._update_tree(node.left, idx, val)
            node.sum = left_sum + node.right.sum
        else:
            right_sum = self._update_tree(node.right, idx, val)
            node.sum = node.left.sum + right_sum
        
        return node.sum
            
    def update(self, index: int, val: int) -> None:
        self._update_tree(self.root, index, val)
        
        
    def _find_sum_range(self, node, left, right):
        if node.start == left and node.end == right:
            return node.sum
        
        mid = (node.start + node.end) // 2
        if mid >= right:
            return self._find_sum_range(node.left, left, right)
        elif mid < left:
            return self._find_sum_range(node.right, left, right)
        else:
            return self._find_sum_range(node.left, left, mid) + self._find_sum_range(node.right, mid + 1, right)
        
    def sumRange(self, left: int, right: int) -> int:
        return self._find_sum_range(self.root, left, right)

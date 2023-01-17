from ast import List


class SegmentTreeNode:
    def __init__(self, min, max, left=None, right=None):
        self.min, self.max = min, max
        self.count = 0 # it marks how many sub ranges under this node
        self.left = left
        self.right = right

# Conceptual Reference: 
    #   - https://leetcode.com/problems/count-of-range-sum/solutions/1674377/java-segment-tree-with-explanation/
    #   - https://leetcode.com/problems/count-of-range-sum/solutions/77987/java-segmenttree-solution-36ms/

# This is a binary tree, each node contains a range formed by "min" and "max".
# the "min" of a parent node is determined by the minimum lower boundary of all its children
# the "max" is determined by the maximum upper boundary of all its children.
# And remember, the boundary value must be a sum of a certain range(i, j). And values between min and max may not corresponding to a valid sum
class SegmentTree:
    def _build_tree(self, low, high, nums):
        if low == high:
            return SegmentTreeNode(nums[low], nums[high])

        mid = (low + high) // 2
        left = self._build_tree(low, mid, nums)
        right = self._build_tree(mid + 1, high, nums)
        return SegmentTreeNode(nums[low], nums[high], left, right)

    def _update_node_count(self, node, val):
        if not node:
            return
        if node.max >= val >= node.min:
            node.count += 1
            self._update_node_count(node.left, val)
            self._update_node_count(node.right, val)

    def __init__(self, nums):
        self.root = self._build_tree(0, len(nums) - 1, nums)

class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        def get_count(node, min, max):
            if not node:
                return 0
            if node.max < min or node.min > max:
                return 0
            if node.min >= min and node.max <= max:
                return node.count

            return get_count(node.left, min, max) + get_count(node.right, min, max)

        prefix_sums = nums[:]
        for i in range(1, len(prefix_sums)):
            prefix_sums[i] += prefix_sums[i - 1]

        # need sorted on unique values
        sorted_prefix_sums_set = sorted(set(prefix_sums))

        segment_tree = SegmentTree(sorted_prefix_sums_set)
        root = segment_tree.root

        res = 0
        for i in range(len(nums) - 1, -1, -1):
            # record the prefix sum from 0 to i - 1
            segment_tree._update_node_count(root, prefix_sums[i])

            """
            lower <= range_sum(i, j) <= upper
            -> lower <= prefix_sum(j) - prefix_sum(i) <= upper
            -> lower + prefix_sum(i) <= prefix_sum(j) <= upper + prefix_sum(i)

            # for a given prefix sum at index i, we need to find all the index j that is larger than i that is within a certain range.
            """
            ref_prefix_sum = prefix_sums[i - 1] if i - 1 >= 0 else 0

            res += get_count(root, lower + ref_prefix_sum, upper + ref_prefix_sum)

        return res

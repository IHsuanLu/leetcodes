from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:    
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = slow = head

        while fast and fast.next:
            slow = slow.next                # Step of 1
            fast = fast.next.next           # Setp of 2

            if slow is fast:                # Checking whether two pointers meet
                return True

        return False
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = start = head
        
        found = False
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                # Floyd Cycle Algorithm
                # distance of starting point to the begining of cycle
                # equals to
                # distance of the point when fast & slow pointers meet
                while slow != start:
                    slow = slow.next
                    start = start.next
                found = True
                break

        return start if found else None
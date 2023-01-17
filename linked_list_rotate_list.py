from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # edge cases
        if not head:
            return None

        # get the length of the list
        length = 0
        curr = head
        while curr:
            curr = curr.next
            length += 1
        
        # k mod length for removing repetitive works
        k %= length

        # if k == 0, do nothing
        if k == 0:
            return head

        # rotate
        temp = length - k
        prev, curr = None, head
        while temp:
            prev = curr
            curr = curr.next
            temp -= 1
        
        tail = curr
        while tail and tail.next:
            tail = tail.next
        
        tail.next = head
        prev.next = None

        return curr
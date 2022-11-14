# create dummy node to cater the edge cases
#   head could change if the reversed part contains the head

# set the pointers
#   1. the node before start
#   2. starter node
#   3. dummy node

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, curr = dummy, head
        
        for _ in range(left - 1):
            prev = prev.next
            curr = curr.next
            
        # we don't know the ending point, bu we can know how many times to do the reverse
        tempPrev = None
        for _ in range(right - left + 1):
            tempNext = curr.next
            curr.next = tempPrev
            tempPrev = curr
            curr = tempNext
            
        # print(tempPrev.val, tempNext.val, prev.val, curr.val)
        prev.next.next = curr
        prev.next = tempPrev
        
        # we might be reassigning the head, so it should be dummy.next and not `head`
        return dummy.next 
            
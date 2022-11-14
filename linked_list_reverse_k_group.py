from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy # we need to save one node right before every kth group for connection

        while True:
            kth = self.getKth(groupPrev, k) # last node of the group
            if not kth:
                break

            groupNext = kth.next

            # reverse group
            prev, curr = groupNext, groupPrev.next # set the head of the next group as "prev" instead of None
            while curr != groupNext:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            # update the pointers for the next round
            temp = groupPrev.next # store the first node of the group to temp
            groupPrev.next = kth # connect to the 
            groupPrev = temp
        
        return dummy.next


    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr

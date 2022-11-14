# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# O(max(m, n))
# O(n)
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        memo = set()
        res = None
        while headA or headB:
            if headA is not None:
                if headA not in memo:
                    memo.add(headA)
                    headA = headA.next
                else:
                    res = headA
                    break
            
            if headB is not None:
                if headB not in memo:
                    memo.add(headB)
                    headB = headB.next
                else:
                    res = headB
                    break
        
        return res


# O(m + n)
# O(1)

# two pointers, https://leetcode.com/problems/intersection-of-two-linked-lists/discuss/2116127/Python-oror-Easy-2-approaches-oror-O(1)-space#1424740

# Notice that if list A and list B have the same length, this solution will terminate in no more than 1 traversal; 
# if both lists have different lengths, this solution will terminate in no more than 2 traversals 
# -- in the second traversal, swapping a and b synchronizes a and b before the end of the second traversal. 
# By synchronizing a and b I mean both have the same remaining steps in the second traversal so that it's guaranteed for them to reach the first intersection node,
#  or reach null at the same time

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        one = headA
        two = headB

        while one != two:
            one = headB if one is None else one.next
            two = headA if two is None else two.next
        return one



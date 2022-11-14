from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        def merge(fn, sn):
            dummy = curr = ListNode()
            while fn and sn:
                if fn.val > sn.val:
                    curr.next = sn
                    sn = sn.next
                else: 
                    curr.next = fn
                    fn = fn.next
                curr = curr.next
                    
            curr.next = fn or sn
#             while fn:
#                 curr.next = fn
#                 fn = fn.next
#                 curr = curr.next
                
#             while sn:
#                 curr.next = sn
#                 sn = sn.next
#                 curr = curr.next
                            
            return dummy.next
                
        
        def dfs(node):
            if not node or not node.next:
                # we want to return node if node has not `next`
                return node
        
            slow = node
            fast = node.next

            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
                
            nxt = slow.next
            slow.next = None
    
            fn = dfs(node)
            sn = dfs(nxt) 
                            
            return merge(fn, sn)
        
        return dfs(head)

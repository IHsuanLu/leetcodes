# Doubly Linked List
class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next, self.prev = None, None

class BrowserHistory:
    def __init__(self, homepage: str):
        self.head = ListNode(homepage)
        self.curr = self.head

    # O(1)
    def visit(self, url: str) -> None:
        newNode = ListNode(url)
        self.curr.next = newNode
        newNode.prev = self.curr
        
        self.curr = newNode

    # O(steps)
    def back(self, steps: int) -> str:
        while steps:
            if self.curr.prev:
                self.curr = self.curr.prev
            steps -= 1
        
        return self.curr.val

    # O(steps)
    def forward(self, steps: int) -> str:
        while steps:
            if self.curr.next:
                self.curr = self.curr.next
            steps -= 1
        
        return self.curr.val


# Array
class BrowserHistory:
    def __init__(self, homepage: str):
        self.arr = [homepage]
        self.curr = 0

    # O(n)
    def visit(self, url: str) -> None:
        self.arr[:] = self.arr[:self.curr + 1]
        self.arr.append(url)
        self.curr = len(self.arr) - 1
        
    # O(1)
    def back(self, steps: int) -> str:
        self.curr = max(self.curr - steps, 0)
        return self.arr[self.curr]
    
    # O(1)
    def forward(self, steps: int) -> str:
        self.curr = min(self.curr + steps, len(self.arr) - 1)
        return self.arr[self.curr]

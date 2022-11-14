# hashMap with a doubly linked list
# O(1) -> must use hash map
# LRU, MRU -> use doubly linked list to keep track

class Node:
    def __init__(self, key=0, val=0):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # map key to the corresponding node with the same key

        # dummy node to tell which is the "least recently used" and "most recently used"
        # Left -> LRU ; Right -> MRU
        self.left, self.right = Node()

        # connect by default
        self.left.next = self.right
        self.right.prev = self.left

    
    # remove from the list
    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev


    # insert at the right
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev


    def get(self, key: int) -> int:
        if key in self.cache:
            # make the node with given key MRU
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        
        if len(self.cache) > self.capacity:
            # remove from the list
            lru = self.left.next
            self.remove(lru)

            # delete the LRU from the cache
            del self.cache[lru.key] 
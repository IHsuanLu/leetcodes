# Hashmap provides Insert and Delete in average constant time, although has problems with GetRandom; 
## There is no indexes in hashmap, and hence to get true random value, one has first to convert hashmap keys in a list, that would take linear time.

# Array List has indexes and could provide Insert and GetRandom in average constant time, though has problems with Delete.
import random


class RandomizedSet:
    def __init__(self):
        self.hmap = {} # key: val; index; idx in the arr
        self.arr = [] 

    def insert(self, val: int) -> bool:
        if val in self.hmap:
            return False
        
        self.arr.append(val)
        self.hmap[val] = len(self.arr) - 1
        return True
        
    def remove(self, val: int) -> bool:
        if val not in self.hmap:
            return False
        
        idx = self.hmap[val]
        last_ele = self.arr[-1]
        
        self.arr[idx], self.arr[-1] = self.arr[-1], self.arr[idx]
        self.arr.pop()

        self.hmap[last_ele] = idx

        del self.hmap[val]
                
        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)
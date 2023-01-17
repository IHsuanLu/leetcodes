# FAV
import collections

# optimal version 
"""
the `max_freq` is ensured to be decremented by `1` if there is only one value has the current `max_freq` 
since at least the prev maximum value will have its frequency equal to `max_freq - 1`; 
otherwise, the `max_freq` stays the same

-> the key is -> we want to know the corresponding values with the specific `count`

example: [5,4,5,3,4,2,5]

counter
{
    5: 3,
    4: 2,
    3: 1,
    2: 1
}

count_maps
{
    1: [5,4,3,2],
    2: [5,4]
    3: [5]
}

Let's say if we want to add another `3`
-> we check the counter and know the count of `3` is currently 1
-> we add `3` to `group 2`, indicating there at count `2` we have [5,4,3] (order preserved)
"""

class FreqStack:
    def __init__(self):
        self.counter = {}
        self.max_freq = 0

         # count: values appears in the certain count
        self.counter_map = collections.defaultdict(list)
        
    def push(self, val: int) -> None:
        self.counter[val] = self.counter.get(val, 0) + 1
        self.max_freq = max(self.max_freq, self.counter[val])

        self.counter_map[self.counter[val]].append(val)

    def pop(self) -> int:
        res = self.counter_map[self.max_freq].pop()
        self.counter[res] -= 1
        if not self.counter_map[self.max_freq]:
            self.max_freq -= 1
        
        return res


# slight enhancement -> get rid of the sorting part

"""
1. the count of the most frequent element -> counter (hash map)
2. the max_freq so far (we can get this while forming the counter)
"""
class FreqStack:
    def __init__(self):
        self.hmap = {}
        self.max_freq = 0
        self.stack = []
        self.temp_stack = [] # for storing temporary element
        
    def push(self, val: int) -> None:
        self.hmap[val] = self.hmap.get(val, 0) + 1
        self.max_freq = max(self.max_freq, self.hmap[val])
        self.stack.append(val)

    def pop(self) -> int:
        while self.stack and self.hmap[self.stack[-1]] < self.max_freq:
            self.temp_stack.append(self.stack.pop())

        res = self.stack.pop()
        
        while self.temp_stack:
            self.stack.append(self.temp_stack.pop())

        self.hmap[res] -= 1
        self.max_freq = max(self.hmap.values())
        return res
        

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()

# intuition -> Beats 5%
class FreqStack:
    def __init__(self):
        self.hmap = {}
        self.stack = []
        self.temp_stack = [] # for storing temporary element
        
    def push(self, val: int) -> None:
        self.hmap[val] = self.hmap.get(val, 0) + 1
        self.stack.append(val)

    def pop(self) -> int:
        keys = sorted(self.hmap, key=self.hmap.get, reverse=True)
        max_freq = self.hmap[keys[0]]

        while self.stack and self.hmap[self.stack[-1]] < max_freq:
            self.temp_stack.append(self.stack.pop())

        res = self.stack.pop()
        
        while self.temp_stack:
            self.stack.append(self.temp_stack.pop())

        self.hmap[res] -= 1
        return res

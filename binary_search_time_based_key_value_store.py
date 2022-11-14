import collections


class TimeMap:

    def __init__(self):
        self.hmap = collections.defaultdict(list) # key: [[timestamp, value]]
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hmap:
            self.hmap[key] = []
        
        self.hmap[key].append([timestamp, value])
    
    # to use binary search, we need our input to be sorted
    # `All the timestamps timestamp of set are strictly increasing.`
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hmap:
            return ""
        
        res = ""
        values = self.hmap.get(key, [])

        l, r = 0, len(values) - 1
        while l <= r:
            mid = (l + r) // 2
            # smaller than `timestamp`
            # record the res and move right til the right most
            if values[mid][0] <= timestamp:
                res = values[mid][1]
                l = mid + 1
            else:
                r = mid - 1

        
        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
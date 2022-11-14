import collections
import heapq

# time complexity O(nlogn). 
# As there might be n pairs of tuple stores in the heap, and each push would take O(logn) time(tree height).

class Solution:
    def reorganizeString(self, s: str) -> str:
        map = {}
        res = ""
        
        for c in s: #(n)
            map[c] = map.get(c, 0) + 1
        
        heap = [(-v, k) for k, v in map.items()]
        heapq.heapify(heap) #(n)
        
        while len(heap) > 1:
            count1, char1 = heapq.heappop(heap)
            count2, char2 = heapq.heappop(heap)
            
            res += char1
            res += char2
            
            count1 += 1
            count2 += 1
            
            if count1 != 0:
                heapq.heappush(heap, (count1, char1))
            
            if count2 != 0:
                heapq.heappush(heap, (count2, char2))
        
        
        if heap:
            count, char = heapq.heappop(heap)
            if abs(count) > 1:
                return ""
            else:
                res += char
        
        return res


class Solution:
    def reorganizeString(self, s: str) -> str:
        if len(s) == 1:
            return s
        count = collections.Counter(s)
        digit0 = max(count.keys(), key = lambda x: count[x])

        an = [digit0 for _ in range(count[digit0])]
        i = 0
        for digit in count:
            if digit != digit0:
                for _ in range(count[digit]):
                    an[i%len(an)] += digit
                    i += 1
        
        return ''.join(an) if i >= len(an) - 1 else ''
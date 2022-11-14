import heapq


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
    
        invalid_index = []
        heapq.heapify(invalid_index)

        for i in range(len(s)):
            if s[i] == "(":
                stack.append((s[i], i))
            elif s[i] == ")":
                if stack:
                    stack.pop()
                else:
                    heapq.heappush(invalid_index, i * -1)
            
        while stack:
            _, idx = stack.pop()
            heapq.heappush(invalid_index, idx * -1)
                        
        while invalid_index:
            nxt = heapq.heappop(invalid_index)
            nxt *= -1
            s = s[:nxt] + s[nxt+1:]
                        
        return s

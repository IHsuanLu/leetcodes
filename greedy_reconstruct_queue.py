from ast import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
        # [[4,4],[5,2],[5,0],[6,1],[7,1],[7,0]]
        people.sort(key=lambda s: (s[0], -s[1]))
        res = [None for _ in range(len(people))]
        
        for height, prev_count in people:
            valid_spots = 0
            curr = 0
            while valid_spots != prev_count or res[curr] is not None:
                if res[curr] is None or res[curr][0] >= height:
                    valid_spots += 1
                curr += 1
    
            res[curr] = [height, prev_count]
    
        return res


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key = lambda x: [x[0], -x[1]])
        
        res = [None] * len(people)
        for h, prev_count in people:
            empty_count = 0
            for i, item in enumerate(res):
                if item is None:
                    empty_count += 1
                    
                    if empty_count == prev_count + 1:
                        res[i] = [h, prev_count]
                        # break
            
        return res
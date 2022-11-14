class Solution:
    def minSwaps(self, s: str) -> int:
        counter = {'0': 0, '1': 0}
        for n in s:
            counter[n] = counter.get(n, 0) + 1
        
        if abs(counter['1'] - counter['0']) > 1:
            return -1
        
        valid_res = []
        if counter['1'] == counter['0']:
            valid_res.extend(['01'*counter['0'], '10'*counter['0']])
        else:
            starter = '10' if counter['1'] > counter['0'] else '01'
            valid_res.append(starter*min(counter['1'],counter['0']) + starter[0])
        
        
        min_val = len(s)
        for res in valid_res:
            mis_matches = 0
            for i in range(len(res)):
                if s[i] != res[i]:
                    mis_matches += 1
            
            min_val = min(min_val, mis_matches // 2)
            
        return min_val

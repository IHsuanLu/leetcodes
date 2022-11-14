class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1
        
        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)
        
        # sliding windows
        j = 0
        for i in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            index = ord(s2[i]) - ord('a')
            s2Count[index] += 1
            
            # if it happen to match the s1Count array
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]: # were equals but no longer
                matches -= 1
                
            # left pointer
            index = ord(s2[j]) - ord('a')
            s2Count[index] -= 1
            
            # if it happen to match the s1Count array
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]: # were equals but no longer
                matches -= 1
            
            j += 1
        
        return matches == 26
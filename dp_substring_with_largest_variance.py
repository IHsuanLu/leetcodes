
# Kadene Algorithm, https://leetcode.com/problems/substring-with-largest-variance/solutions/2412313/python-kadene-algo-with-explanation/
class Solution:
    def largestVariance(self, s: str) -> int:
		# Create a dictionary with the count of all chars of s
        chars = {}
        for c in s:
            chars[c] = chars.get(c, 0) + 1

        # Calculate the possible permulations
        permutations = itertools.permutations(chars, 2)
        
		# Calculate the max subarray count with kadene algo
        count = 0
        for a, b in permutations:
            count = max(self.kadene(a, b, s, chars), count)
        return count

    def kadene(self, a, b, s, chars):
        count = 0
        max_local = 0

		# Keep track if c has become a or b
        is_a = False
        is_b = False

		# Keep track of characters for a and b
        val_a = chars[a]
        val_b = chars[b]
        for c in s:

			# No need to continue if c is not a or b
            if c != a and c != b:
                continue

			# Reset the max_local if there are no chars left or max_total
		    # is negative
            if max_local < 0 and val_a != 0 and val_b != 0:
                max_local = 0
                is_a = False
                is_b = False

			# Add 1 to the local max if c is the expected char
            if c == a:
                max_local += 1
                val_a -= 1
                is_a = True
						
			# Remove 1 from the local max if c is the expected char
            if c == b:
                max_local -= 1
                val_b -=1
                is_b = True
            
			# Only calculate the count if a and b apperared
            if is_a and is_b:
                count = max(count, max_local)

        return count


# brute force (recursion) -> TLE, pass 91/138
from collections import Counter


class Solution:
    def largestVariance(self, s: str) -> int:
        """
        - we need to know the count of each character
        - how many distict characters are there in the given string
        """
        
        hset = set(s)
        if len(hset) == 1:
            return 0

        """
        use recursion to enumerate all the substrings
        """
        memo = set()
        def dfs(idx):
            if idx >= len(s):
                return 0

            max_variance = 0
            for i in range(idx, len(s)):
                substring = s[idx: i + 1]
                if substring in memo:
                    continue
                memo.add(substring)

                counter = Counter(substring)
                variance = max(max_variance, counter.values()) - min(counter.values())
                max_variance = max(max_variance, variance, dfs(i + 1))

            return max_variance

        
        return dfs(0)



# brute force -> TLE. pass 97/138
class Solution:
    def largestVariance(self, s: str) -> int:
        """
        - we need to know the count of each character
        - how many distict characters are there in the given string
        """
        
        hset = set(s)
        if len(hset) == 1:
            return 0

        """
        use recursion to enumerate all the substrings
        """
        res = 0
        memo = set()
        counter = {}
        for i in range(len(s)):
            for j in range(i, len(s)):
                substring = s[i: j + 1]
                if substring in memo:
                    continue
                memo.add(substring)
                
                for c in substring:
                    counter[c] = counter.get(c, 0) + 1
                
                min_occurence = min(counter.values())
                max_occurence = max(counter.values())
                res = max(res, max_occurence - min_occurence)

                counter.clear()

        return res
            

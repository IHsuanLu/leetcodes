from ast import List


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        """
        serveral cases:
            - place at the leftmost, rightmost index
            - place at the middle of two ones
        """
        ones = []
        for i in range(len(seats)):
            if seats[i] == 1:
                ones.append(i)

        max_val = 0
        
        # edge cases
        max_val = max(ones[0], len(seats) - ones[-1] - 1)

        # middle cases
        for i in range(1, len(ones)):
            max_val = max(max_val, (ones[i] - ones[i - 1]) // 2)

        return max_val
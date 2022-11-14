class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = list([i for i in range(1, n+1)])
        lastIndex = 0

        while len(arr) > 1:
            lastIndex = (lastIndex + k - 1) % len(arr)
            del arr[lastIndex]
            
            # relocate the index after removing element from arr
            lastIndex = lastIndex % len(arr)

        return arr[0]

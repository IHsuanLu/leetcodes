class Solution:
    def maximumSwap(self, num: int) -> int:
        # iterate the num from right to left
        # record the max number in an arry
        # and the same time check if there is a number smaller than the max number up front the array, if yes, we can do the swap
        
        num_arr = [int(n) for n in str(num)]
        max_left_idx = len(num_arr) - 1
        
        x, y = -1, -1
        
        for i in range(len(num_arr) - 2, -1, -1):
            if num_arr[i] > num_arr[max_left_idx]:
                max_left_idx = i
            elif num_arr[i] < num_arr[max_left_idx]:
                x = i
                y = max_left_idx
        
        if x != -1 and y != -1:
            num_arr[x], num_arr[y] = num_arr[y], num_arr[x]
            
        return int("".join([str(n) for n in num_arr]))
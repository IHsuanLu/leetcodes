class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y+x
        
class Solution:
    def largestNumber(self, nums):
        nums_str_arr = sorted(map(str, nums), key=LargerNumKey)
        largest_num = ''.join(nums_str_arr)
        return '0' if largest_num[0] == '0' else largest_num
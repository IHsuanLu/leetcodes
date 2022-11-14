import random

nums = [1,2,3]

def quick_select_n_smallest(n):            
    start, end = 0, len(nums) - 1
    while True:
        pivot = nums[random.randint(start,end)]
        l, r = start, end # moving pointers
        p = start # pivot pointer
        
        while p <= r:
            if nums[p] > pivot: # swap to the back
                nums[p], nums[r] = nums[r], nums[p]
                r -= 1
            elif nums[p] < pivot: # swap to the front
                nums[p], nums[l] = nums[l], nums[p]
                l += 1
                p += 1
            else: # skip
                p += 1
        
        # r, l intersection is an index, where to the left are all values smaller than the random pivot, while to the right are all larger values.
        n_idx = n - 1
        if l <= n_idx <= r:
            return pivot
        elif n_idx < l:
            end = r - 1
        else:
            start = l + 1


res = quick_select_n_smallest(len(nums) // 2)    
half = (len(nums)+1) // 2
nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]
print(res, nums)
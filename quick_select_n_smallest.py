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



# ----------
k = len(nums) // 2 # kth smallest
def quick_select(start, end):
    pivot = nums[start]
    l, r = start, end
    p = start
    
    while p <= r:
        if nums[p] < pivot:
            nums[p], nums[l] = nums[l], nums[p]
            p += 1
            l += 1
        elif nums[p] > pivot:
            nums[p], nums[r] = nums[r], nums[p]
            r -= 1
        else:
            p += 1
    
    if (p - 1) > k:
        return quick_select(start, r - 1)
    elif (p - 1) < k:
        return quick_select(l + 1, end)
    else:
        return pivot


def quickSort(nums):
    def helper(start, end):
        if start >= end: 
            return 

        l, r = start, end
        p = (r - l) // 2 + l
        pivot = nums[p]

        while l <= r:
            while l <= r and nums[l] < pivot: 
                l += 1
            while l <= r and nums[r] > pivot: 
                r -= 1
            if l <= r :
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        
        # different from quick select, quick sort does the sorting on both sides
        helper(start, r)
        helper(l, end)

    helper(0, len(nums)-1)
    return nums


def quick_sort_recur(start, end):
    if start >= end:
        return

    pivot, p = nums[start], start
    l, r = start, end            
    while p <= r:
        if nums[p] < pivot:
            nums[p], nums[l] = nums[l], nums[p]
            p += 1
            l += 1
        elif nums[p] > pivot:
            nums[p], nums[r] = nums[r], nums[p]
            r -= 1
        else:
            p += 1
    
    quick_sort_recur(start, r - 1)
    quick_sort_recur(l + 1, end)
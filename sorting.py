def bubble_sort(arr):
  for i in range(len(arr)):
    for j in range(len(arr) - i - 1):
      if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]

 
def selection_sort(arr):
  for i in range(len(arr)):
    curr_min_idx = i
    for j in range(i + 1, len(arr)):
      if arr[j] < arr[curr_min_idx]:
        curr_min_idx = j

    arr[i], arr[curr_min_idx] = arr[curr_min_idx], arr[i]
    
    
def insertion_sort(arr):
  for i in range(1, len(arr)):
    key = arr[i]
    j = i-1
    while j >=0 and key < arr[j] :
        arr[j+1] = arr[j]
        j -= 1
    arr[j+1] = key


def merge_sort(nums):
    if not nums:
        return []
    
    def divide(arr):
        if len(arr) == 1:
            return arr
        mid = len(arr) // 2
        left = divide(arr[:mid])
        right = divide(arr[mid:])
        return conquer(left, right)
    
    def conquer(left, right):
        temp_res = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                temp_res.append(left[i])
                i += 1
            else:
                temp_res.append(right[j])
                j += 1
        temp_res.extend(left[i:] or right[j:])
        return temp_res
                                    
    return divide(nums)
    


def quick_sort(nums):
  def helper(start, end):
      if start >= end:
          return

      l, r = start, end
      pivot, p = nums[start], start
      
      while l <= r:
          # find the candidate that is larger than pivot
          while l <= r and nums[l] < pivot:
              l += 1
          
          # find the candidate that is smaller than pivot
          while l <= r and nums[r] > pivot:
              r -= 1
          
          if l <= r:
              nums[l], nums[r] = nums[r], nums[l]
              l += 1
              r -= 1
      
      helper(start, r)
      helper(l, end)
  
  helper(0, len(nums) - 1)

  return nums
    
    
test = [2,1,3,5,4]
print(quick_sort(test))


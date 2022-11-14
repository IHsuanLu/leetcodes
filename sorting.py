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
    
    
test = [2,1,3,5,4]
insertion_sort(test)
print(test)


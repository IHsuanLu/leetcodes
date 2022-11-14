from ast import List


class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        row_num, col_num = len(mat), len(mat[0])
        
        def binary_search(l, r, arr, target):
            if target < arr[l] or target > arr[r]:
                return False

            while l <= r:    
                mid = (l + r) // 2
                if arr[mid] > target:
                    r = mid -1
                elif arr[mid] < target:
                    l = mid + 1
                else:
                    return True
            
            return False
    
        for candidate in mat[0]:
            res = [True] + [False] * (row_num - 1)
            for row in range(1, row_num):
                l, r = 0, col_num - 1
                if not binary_search(l, r, mat[row], candidate):
                    break
                res[row] = True

            if all(r for r in res):
                return candidate
        
        return -1
                

class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        row_num, col_num = len(mat), len(mat[0])
        
        hmap = {}
        min_val = float('inf')
        for r in range(row_num):
            for c in range(col_num):
                hmap[mat[r][c]] = hmap.get(mat[r][c], 0) + 1
                if mat[r][c] in hmap and hmap[mat[r][c]] == row_num:
                    min_val = min(min_val, mat[r][c])
        
        return min_val if min_val != float('inf') else -1
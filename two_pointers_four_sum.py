from ast import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
                
        def k_sum(k, start, remained_target, path):
            if k > 2:
                # backtrack to find the combinations of length k - 2

                # starting from `start` to create unique `subset`
                for i in range(start, len(nums) - 2):
                     # we don't want duplicate, yet still wanna keep the first composition, so we add `i != start`
                    if i != start and nums[i] == nums[i - 1]:
                        continue
    
                    path.append(nums[i])
                    k_sum(k - 1, i + 1, remained_target - nums[i], path)
                    path.pop()
            else:     
                # for quad, we will have every combination with length (k - 2) of the elements before len(nums) - 2
                # [1,0,-1,0,-2,2], [-2,-1,0,0,1,2]
                # [[-2, -1], [-2. 0], [-1, 0], [0, 0]]

                # create two pointers finding the remaining two elements
                l, r = start, len(nums) - 1
                while l < r:
                    two_sum = nums[l] + nums[r]
                    if two_sum > remained_target:
                        r -= 1
                    elif two_sum < remained_target:
                        l += 1
                    else:
                        res.append(path[:] + [nums[l], nums[r]])

                        l += 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1

        
        k_sum(4, 0, target, [])
        return res
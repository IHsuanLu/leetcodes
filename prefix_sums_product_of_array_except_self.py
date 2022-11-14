from ast import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
#         [2,3,4,5]
#.        i = 0; 1 * rtl_prefix_products[1]
#.        i = 1; ltr_prefix_products[0] * rtl_prefix_products[2] 
#         i = 3; ltr_prefix_products[2] * 1
        
#         [2,6,24,120]    
#         [120,60,20,5] 
        products = [1] * len(nums)
        
        for i in range(1, len(nums)):
            products[i] = products[i - 1] * nums[i - 1]
            
        
        rightProduct = 1
        for i in range(len(nums) - 1, -1, -1):
            products[i] *= rightProduct
            rightProduct *= nums[i]
            
        # [60,40,30,24]
        return products



class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
#         [2,3,4,5]
#.        i = 0; 1 * rtl_prefix_products[1]
#.        i = 1; ltr_prefix_products[0] * rtl_prefix_products[2] 
#         i = 3; ltr_prefix_products[2] * 1
        
#         [2,6,24,120]    
#         [120,60,20,5] 
        ltr_prefix_products = [1] * len(nums)
        rtl_prefix_products = [1] * len(nums)
        
        curr_product = 1
        for i, n in enumerate(nums):
            curr_product *= n
            ltr_prefix_products[i] = curr_product
        
        curr_product = 1
        for i in range(len(nums) - 1, -1, -1):
            curr_product *= nums[i]
            rtl_prefix_products[i] = curr_product
            
        res = [1] * len(nums)
        for i in range(len(nums)):
            left_product = 1
            right_product = 1
            if i - 1 >= 0:
                left_product = ltr_prefix_products[i - 1]
            
            if i < len(nums) - 1:
                right_product = rtl_prefix_products[i + 1]
                
            res[i] = left_product * right_product

        # [60,40,30,24]
        return res
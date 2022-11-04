"""
Time = O(n)
Space = O(1)
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Create to accumulate multiplication arrays
        res = [1] * len(nums)
        # right = [1] * len(nums)
        
        # O(n)
        for i in range(1, len(res)):
            res[i] = nums[i-1] * res[i-1]
            
        # O(n)
        product = 1
        for i in range(len(res)-1, -1, -1):
            res[i] *= product
            product *= nums[i]
            
        return res
        
        
        
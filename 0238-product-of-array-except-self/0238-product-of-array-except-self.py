"""
Time = O(n)
Space = O(1)
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        
        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1]
        
        product = nums[i]
        for i in range(len(nums)-2, -1, -1):
            res[i] *= product
            product *= nums[i]
            
        return res
        
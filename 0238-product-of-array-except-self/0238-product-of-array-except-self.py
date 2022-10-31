"""
input: arr = [1, 2, 3, 5]
return: arr = [30, 15, 10, 6]
[1, 1, 1*2, 1*2*3]
[5*3*2, 5*3, 5, 1]
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        right = [1] * len(nums)
        res = []
        
        for i in range(1, len(nums)):
            left[i] = left[i-1] * nums[i-1]
        
        for i in range(len(nums)-2, -1, -1):
            right[i] = right[i+1] * nums[i+1]
        
        for i in range(len(nums)):
            res.append(left[i] * right[i])
            
        return res
        
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        First create two accumulate multiplication arrays
        [1, nums[0], nums[0]*nums[1], nums[0]*nums[1]*nums[2]]
        [nums[3]*nums[2]*nums[1], nums[3]*nums[2], nums[3], 1]]
        
        Multiple them according to their indices
        """
        # Create to accumulate multiplication arrays
        left = [1] * len(nums)
        right = [1] * len(nums)
        
        # Left
        for i in range(1, len(left)):
            left[i] = nums[i-1] * left[i-1]
        # Right
        for i in range(len(right)-2, -1, -1):
            right[i] = nums[i+1] * right[i+1]
            
        # Multiple two arrays according to their indices
        for i in range(len(left)):
            left[i] *= right[i]
            
        return left
        
        
        
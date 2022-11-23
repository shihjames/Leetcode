"""
Time = O(n)
Space = O(1)
"""
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        cur = 0
        
        for i in range(len(nums)):
            if float(cur) == (total - nums[i]) / 2:
                return i
            cur += nums[i]
        
        return -1
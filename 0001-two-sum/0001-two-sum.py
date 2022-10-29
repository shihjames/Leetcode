"""
Time = O(n)
Space = O(n)
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remain = {}
        
        for i in range(len(nums)):
            if nums[i] not in remain:
                remain[target-nums[i]] = i
            else:
                return [remain[nums[i]], i]
        
        return [-1, -1]
"""
Time = O(n)
Space = O(n)
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remaining = {}
        
        for i in range(len(nums)):
            if nums[i] in remaining:
                return [i, remaining[nums[i]]]
            remaining[target-nums[i]] = i
            
        return [-1, -1]
        
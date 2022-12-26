class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_index = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] + i >= last_index:
                last_index = i
        
        return last_index == 0
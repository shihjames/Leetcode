"""

"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0
        
        for i in range(len(nums)):
            cur_length = 0
            if nums[i] - 1 not in nums_set:
                cur = nums[i]
                while cur in nums_set:
                    cur_length += 1
                    cur += 1
            longest = max(longest, cur_length)
        
        return longest
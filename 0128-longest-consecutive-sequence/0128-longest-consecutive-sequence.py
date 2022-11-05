"""
Time = O(n)
Space = O(n)
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0
        
        # Traverse throught the array
        # O(n)
        for i in range(len(nums)):
            if nums[i] - 1 in num_set:
                continue
            # Found the first number in a certain sequence
            cur_length = 1
            cur_num = nums[i]
            while (cur_num + 1) in num_set:
                cur_length += 1
                cur_num += 1
            
            # Update the longest
            longest = max(longest, cur_length)
        
        return longest
        
"""
Time = O(n)
Space = O(n)
"""
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        ele_count = {}
        for num in nums:
            if num in ele_count:
                return True
            ele_count[num] = 1
        return False
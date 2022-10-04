"""
Time = O(m+n)
Space = O(min(m, n))
"""
from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        intersection = []
        counter = Counter(nums1)
        for num in nums2:
            if counter[num] > 0:
                intersection.append(num)
                counter[num] -= 1
        
        return intersection
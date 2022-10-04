"""
Time = O(n+m)
Space = O(n)
"""
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # return set(nums1).intersection(set(nums2))
        intersection = []
        set1 = set(nums1)
        for num in nums2:
            if num in set1:
                intersection.append(num)
                set1.remove(num)
        
        return intersection 
            
        
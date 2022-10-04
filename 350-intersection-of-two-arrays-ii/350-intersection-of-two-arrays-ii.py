from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = []
        counter = Counter(nums1)
        for num in nums2:
            if counter[num] > 0:
                intersection.append(num)
                counter[num] -= 1
        
        return intersection
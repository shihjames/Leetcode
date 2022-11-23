"""
Time = O(n)
Space = O(n)
"""
from collections import defaultdict
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # O(n)
        indices = defaultdict(int)
        for index, num in enumerate(nums1):
            indices[num] = index
        
        res = [-1] * len(nums1)
        
        stack = []
        # O(n)
        for i in range(len(nums2)):
            cur = nums2[i]
            while stack and cur > stack[-1]:
                num = stack.pop()
                if num in indices:
                    res[indices[num]] = cur
            stack.append(cur)
        
        return res
                    
                
        
        
            
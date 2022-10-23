class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        indices = defaultdict(int)
        res = [-1] * len(nums1)
        for index, num in enumerate(nums1):
            indices[num] = index
        
        stack = []
        for i in range(len(nums2)):
            cur = nums2[i]
            while stack and cur > stack[-1]:
                num = stack.pop()
                if num in indices:
                    res[indices[num]] = cur
            stack.append(cur)

        return res
            
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        short, long = nums1, nums2
        if len(short) > len(long):
            short, long = long, short
            
        total = len(short) + len(long)
        half = total // 2
        left, right = 0, len(short)-1
        
        while True:
            shortMid = left + (right - left) // 2
            longMid = half - shortMid - 2
            
            shortL = short[shortMid] if shortMid >= 0 else float("-inf")
            shortR = short[shortMid + 1] if shortMid < len(short) - 1 else float("inf")
            longL = long[longMid] if longMid >= 0 else float("-inf")
            longR = long[longMid + 1] if longMid < len(long) - 1 else float("inf")
            
            if shortL <= longR and longL <= shortR:
                if total % 2 == 0:
                    return (max(shortL, longL) + min(shortR, longR)) / 2
                return min(shortR, longR)
            elif shortL > longR:
                right = shortMid - 1
            else:
                left = shortMid + 1
        return 0
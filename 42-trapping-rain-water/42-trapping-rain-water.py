"""
Time = O(n)
Space = O(n)
"""
class Solution:
    def trap(self, height: List[int]) -> int:
        left = [height[0]] * len(height)
        right = [height[-1]] * len(height)
        area = 0
        
        for i in range(1, len(height)):
            left[i] = max(height[i], left[i-1])
            
        for i in range(len(height)-2, -1, -1):
            right[i] = max(height[i], right[i+1])
            
        for i in range(len(height)):
            area += min(left[i], right[i]) - height[i]
        
        return area
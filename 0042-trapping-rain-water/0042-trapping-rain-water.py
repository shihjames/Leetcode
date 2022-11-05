"""
Time = O(3n) = O(n)
Space = O(2n) = O(n)
"""
class Solution:
    def trap(self, height: List[int]) -> int:
        # Represent each position's left or right wall's height
        left = [0] * len(height)
        right = [0] * len(height)
        left[0] = height[0]
        right[-1] = height[-1]
        # O(n)
        for i in range(1, len(left)):
            left[i] = max(left[i-1], height[i])
        # O(n)
        for i in range(len(right)-2, -1, -1):
            right[i] = max(right[i+1], height[i])
        # O(n)
        # Calculate total area
        total = 0
        for i in range(len(height)):
            total += min(left[i], right[i]) - height[i]
            
        return total
            
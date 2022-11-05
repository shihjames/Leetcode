"""
Time = O(n)
Space = O(1)
"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Create two pointers
        left = 0
        right = len(height) - 1
        cur_max_area = 0
        
        # Traverse through the array
        while left < right:
            # Calculate the current area
            w = right - left
            h = min(height[left], height[right])
            cur_max_area = max(cur_max_area, w * h)
            # move one of the pointer which points to the shorter wall
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return cur_max_area
"""
Time = O(n)
Space = O(1)
"""
class Solution:
    def jump(self, nums: List[int]) -> int:
        l = r = 0
        jump = 0
        # Greedy: find the furthest step in each iteration
        while r < len(nums) - 1:
            furthest = 0
            # Try all possibilities and find the furthest
            for i in range(l, r + 1):
                if nums[i] + i > furthest:
                    furthest = nums[i] + i
            # Update new interval
            l = r + 1
            r = furthest
            # Update number of jumps
            jump += 1
        
        return jump
        
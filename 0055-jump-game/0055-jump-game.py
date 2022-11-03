"""
Time = O(n)
Space = O(1)
"""
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Set goal to the last index
        goal = len(nums)-1
        # Traverse backward
        for i in range(len(nums)-1, -1, -1):
            # If current index can reach the goal
            if nums[i] + i >= goal:
                # Update new goal position
                goal = i
        
        # Check goal position is at the first index
        return goal == 0
        
#         def jumpHelper(index):
#             # Able to jump to the destination
#             if index >= len(nums)-1:
#                 return True
#             # Simply use the previous result
#             if index in memo:
#                 return memo[index]
#             # Try all jumps
#             res = False
#             for i in range(nums[index], 0, -1):
#                 if jumpHelper(index + i):
#                     res = True
#                     break
#             memo[index] = res
#             return res
            
#         if len(nums) == 0:
#             return False
#         if len(nums) == 1:
#             return True
#         memo = {}
#         return jumpHelper(0)
        
        
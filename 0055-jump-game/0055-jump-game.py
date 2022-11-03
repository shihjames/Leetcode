"""
Time = O()
"""
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums)-1
        for i in range(len(nums)-1, -1, -1):
            if nums[i] + i >= goal:
                goal = i
                
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
        
        
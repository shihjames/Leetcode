"""
Time = O(n*n!)
Space = O(n!)
"""
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(cur):
            if len(cur) == len(nums):
                res.append(cur.copy())
                return
            
            for i in range(len(nums)):
                if nums[i] not in cur:
                    cur.append(nums[i])
                    backtrack(cur)
                    cur.pop()
                    
        res = []
        backtrack([])
        return res
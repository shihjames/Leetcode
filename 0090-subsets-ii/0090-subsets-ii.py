class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(index, cur_comb):
            if index == len(nums):
                res.append(cur_comb[:])
                return
            
            cur_comb.append(nums[index])
            backtrack(index + 1, cur_comb)
            cur_comb.pop()
            
            while index + 1 < len(nums) and nums[index] == nums[index+1]:
                index += 1
            
            backtrack(index + 1, cur_comb)
                
        
        nums.sort()
        res = []
        backtrack(0, [])
        return res
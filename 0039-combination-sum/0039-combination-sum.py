class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(cur_comb, cur_sum, index):
            if index >= len(candidates) or cur_sum > target:
                return
            
            if cur_sum == target:
                res.append(cur_comb[:])
                return
            
            for i in range(index, len(candidates)):
                backtrack(cur_comb + [candidates[i]], cur_sum + candidates[i], i)
                
            
        res = []
        backtrack([], 0, 0)
        return res
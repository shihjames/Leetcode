"""
Time = O(n**(t/m))
Space = O(t/m)
"""
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(cur, index, total):
            if total == target:
                res.append(cur[:])
                return
            elif index >= len(candidates) or total > target:
                return
            # choose
            cur.append(candidates[index])
            # Explore
            backtrack(cur, index, total+candidates[index])
            # Un-choose
            cur.pop()
            # Exclude
            backtrack(cur, index+1, total)
            
                
        res = []
        backtrack([], 0, 0)
        return res
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(cur, index, total):
            if total == target:
                res.append(cur[:])
                return
            elif total > target:
                return
            else:
                for i in range(index, len(candidates)):
                    if total + candidates[i] > target:
                        break
                    cur.append(candidates[i])
                    backtrack(cur, i, total+candidates[i])
                    cur.pop()
                
        res = []
        candidates.sort()
        backtrack([], 0, 0)
        return res
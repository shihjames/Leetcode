class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(first, cur_comb):
            if len(cur_comb) == k:
                res.append(cur_comb.copy())
                return
            
            for i in range(first, n + 1):
                cur_comb.append(i)
                backtrack(i + 1, cur_comb)
                cur_comb.pop()
                
        res = []
        backtrack(1, [])
        return res
            
            
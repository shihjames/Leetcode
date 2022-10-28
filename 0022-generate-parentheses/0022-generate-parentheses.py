class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(cur, left, right):
            if len(cur) == 2*n:
                res.append(cur)
                return
            if left < n:
                cur += "("
                backtrack(cur, left+1, right)
                cur = cur[:-1]
            if right < left:
                cur += ")"
                backtrack(cur, left, right+1)
                cur = cur[:-1] 

        res = []
        backtrack("", 0, 0)
        return res
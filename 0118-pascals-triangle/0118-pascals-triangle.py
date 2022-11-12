class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            rows = [1] * (i + 1)
            if i > 1:
                for i in range(1, len(rows)-1):
                    rows[i] = res[-1][i] + res[-1][i-1]
            res.append(rows)
        
        return res
            
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:        
        def generateHelper(left_cnt, right_cnt, cur_str):
            if len(cur_str) == n * 2:
                res.append(cur_str)
                
            if left_cnt < n:
                generateHelper(left_cnt + 1, right_cnt, cur_str + "(")
                
            if right_cnt < left_cnt:
                generateHelper(left_cnt, right_cnt + 1, cur_str + ")")
               
        res = []
        generateHelper(0, 0, "")
        
        return res
                
        
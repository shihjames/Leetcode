class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        1. add a left parentheses
        2. check number of ")" is no more than "(", add a right parentheses
        
        recursive function(left_count, right_count, string)
        
        if length of string equals to n * 2
            add string to result
        
        if left_count is smaller than n
            recursive function(left_count + 1, right_count, string + "(")
        
        if right_count is smaller than left_count
            recursive function(left_count, right_count + 1, string + ")")
        """
        res = []
        
        def generateHelper(left_cnt, right_cnt, cur_str):
            if len(cur_str) == n * 2:
                res.append(cur_str)
                
            if left_cnt < n:
                generateHelper(left_cnt + 1, right_cnt, cur_str + "(")
                
            if right_cnt < left_cnt:
                generateHelper(left_cnt, right_cnt + 1, cur_str + ")")
                
        generateHelper(0, 0, "")
        
        return res
                
        
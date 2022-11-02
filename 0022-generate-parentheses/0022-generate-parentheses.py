class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        # Recursive function for generating parentheses
        def helper(left, right, cur_str):
            # Length of cur_str equals to n -> Finish generating
            if len(cur_str) == n * 2:
                res.append(cur_str)
            # check numbers of left paren and right paren:
            if left < n:
                helper(left + 1, right, cur_str + "(")
            if right < left:
                helper(left, right + 1, cur_str + ")")
         
        helper(0, 0, "")
        return res
        
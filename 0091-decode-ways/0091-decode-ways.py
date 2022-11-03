"""
Time = O(n)
Space = O(n)
"""
class Solution:
    def numDecodings(self, s: str) -> int:
        def dfs(index):
            if index in dp:
                return dp[index]
            
            if s[index] == "0":
                return 0
            
            
            res = dfs(index + 1)
            
            if (index + 1) < len(s) and (s[index] == "1" or (s[index] == "2" and int(s[index + 1]) <= 6)):
                res += dfs(index + 2)
                                       
            dp[index] = res
            return res
            
        dp = {len(s): 1}
        return dfs(0)
        
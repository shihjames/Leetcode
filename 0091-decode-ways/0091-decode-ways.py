"""
Time = O(n)
Space = O(n)
"""
class Solution:
    def numDecodings(self, s: str) -> int:
        def dfs(index):
            if index in dp:
                return dp[index]
            
            if index == len(s):
                return 1
            
            if s[index] == "0":
                return 0
            
            if index == len(s) - 1 :
                return 1
            
            res = dfs(index + 1)
            
            if int(s[index: index + 2]) <= 26:
                res += dfs(index + 2)
                                       
            dp[index] = res
            return res
            
        dp = {}
        return dfs(0)
        
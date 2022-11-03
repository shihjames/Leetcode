class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[0 for i in range(len(s))] for i in range(len(s))]
        count = 0
        
        # Single letter substrings
        for i in range(len(s)):
            count += 1
            dp[i][i] = True
            
        # Double letter substrings
        for i in range(len(s) - 1):
            dp[i][i+1] = (s[i] == s[i+1])
            if s[i] == s[i+1]:
                count += 1 
                
        # Other substrings
        for l in range(3, len(s) + 1):
            i = 0
            j = i + l - 1
            while j < len(s):
                dp[i][j] = dp[i + 1][j - 1] and s[i] == s[j]
                if dp[i][j]:
                    count += 1
                i += 1
                j += 1
                
        return count
            
                    
        
#         count = 0
        
#         for i in range(len(s)):
#             # Odd case
#             left, right = i, i
#             while left >= 0 and right < len(s) and s[left] == s[right]:
#                 count += 1
#                 left -= 1
#                 right += 1
#             # Even case
#             left, right = i, i + 1
#             while left >= 0 and right < len(s) and s[left] == s[right]:
#                 count += 1
#                 left -= 1
#                 right += 1
            
#         return count
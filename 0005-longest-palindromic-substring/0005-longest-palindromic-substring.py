"""
Time = O(n**2)
Space = O(1)
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        longest_len = 0
        
        for i in range(len(s)):
            # Odd case
            left = i
            right = i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            if right - left - 1 > longest_len:
                res = s[left + 1: right]
                longest_len = len(res)
            
            # Even case
            left = i
            right = i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            if right - left - 1 > longest_len:
                res = s[left + 1: right]
                longest_len = len(res)
            
        return res
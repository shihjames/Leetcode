"""
Time = O(n**2)
Space = O(1)
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        length = 0
        
        for i in range(len(s)):
            # Odd case
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > length:
                    res = s[left: right + 1]
                    length = right - left + 1
                left -= 1
                right += 1
            # Even case
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > length:
                    res = s[left: right + 1]
                    length = right - left + 1
                left -= 1
                right += 1
            
        return res
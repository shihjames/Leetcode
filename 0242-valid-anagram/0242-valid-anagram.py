"""
Time = O(n)
Space = O(1)
"""
from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        chars = [0] * 26
        
        for i in range(len(s)):
            chars[ord(s[i]) - ord("a")] += 1
        
        for i in range(len(t)):
            if chars[ord(t[i]) - ord("a")] == 0:
                return False
            chars[ord(t[i]) - ord("a")] -= 1
        
        return True
"""
Time = O(n)
Space = O(1)
"""
from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        char_count = defaultdict(int)
        
        for char in s:
            char_count[char] += 1 
        
        for char in t:
            char_count[char] -= 1
            if char_count[char] < 0:
                return False
                
        return True
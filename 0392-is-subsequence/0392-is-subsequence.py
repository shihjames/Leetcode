"""
Time = O(n)
Space = O(1)
"""
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        if s == "":
            return True
        
        index = 0
        for i in range(len(t)):
            if s[index] == t[i]:
                index += 1
            if index == len(s):
                return True
            
        return False
"""
Time = O(n)
Space = O(m)
where m = # of unique chars in pattern and words in s
"""
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        patterns = {}
        words = {}
        s = s.split(" ")
        
        if len(s) != len(pattern):
            return False
        
        for i in range(len(pattern)):
            if pattern[i] not in patterns:
                if s[i] not in words:
                    patterns[pattern[i]] = s[i]
                    words[s[i]] = pattern[i]
                else:
                    return False
            else:
                if patterns[pattern[i]] != s[i]:
                    return False
        
        return True
                
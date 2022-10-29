from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counter_s = Counter(s)
        counter_t = Counter(t)
        
        for char, count in counter_s.items():
            if count != counter_t[char]:
                return False
            
        return True
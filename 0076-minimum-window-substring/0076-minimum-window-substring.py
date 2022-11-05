"""
Time = O(n)
Space = O(len(t))
"""
from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        # Count each element in string t
        counter = Counter(t)
        need = len(t)
        shortest = ""
        shortest_len = len(s) + 1
        # Two pointers to create a interval
        l = 0
        for r in range(len(s)):
            # Check if the current element is in the dictionary
            if s[r] in counter:
                counter[s[r]] -= 1
                if counter[s[r]] >= 0:
                    need -= 1
            # Narrow down the interval
            while l <= r and need == 0:
                if r - l + 1 < shortest_len:
                    shortest = s[l: r + 1]
                    shortest_len = len(shortest)
                if s[l] in counter:
                    counter[s[l]] += 1
                    if counter[s[l]] > 0:
                        need += 1
                l += 1
        
        return shortest
                    
            
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Different length
        if len(s) != len(t):
            return False
        # Creat dictionary to count number of chars
        counter = Counter(s)
        for char in t:
            if char not in counter or counter[char] == 0:
                return False
            else:
                counter[char] -= 1
        return True
                
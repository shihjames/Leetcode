"""
Time = O(nk)
space = O(26nk) = O(nk)
"""
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        # O(n)
        for s in strs:
            letters = [0] * 26
            # O(k)
            for char in s:
                letters[ord(char) - ord("a")] += 1
            anagrams[tuple(letters)].append(s)
            
        return anagrams.values()
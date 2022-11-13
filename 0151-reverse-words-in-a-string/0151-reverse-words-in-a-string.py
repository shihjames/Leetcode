"""
Time = O(n)
Space = O(n)
"""
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        return " ".join(words[::-1])
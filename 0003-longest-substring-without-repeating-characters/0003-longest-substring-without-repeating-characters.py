"""
Time = O(n)
Space = O(n)
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        left = 0
        longest = 1
        char_set = set()
        char_set.add(s[left])
        
        for right in range(1, len(s)):
            if s[right] not in char_set:
                char_set.add(s[right])
                longest = max(longest, right - left + 1)
            else:
                while s[left] != s[right]:
                    if s[left] in char_set:
                        char_set.remove(s[left])
                    left += 1
                left += 1
        
        return longest
            
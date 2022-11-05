"""
Time = O(n)
Space = O(1)
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        1. Use two pointers, left (forward) and right (backward)
        2. Check elements which are pointed by the two pointers are the same
        (Skip non-alphabetic and non-numeric elements)
        """
        
        left, right = 0, len(s) - 1
        
        while left < right:
            # Make sure two pointers point to valid elements
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
                
            if s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1
        
        return True
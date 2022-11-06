"""
Time = O(n)
Space = O(n)
"""
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {")": "(", "]": "[", "}": "{"}
        # Traverse to all brackets
        for i in range(len(s)):
            if s[i] in "([{":
                stack.append(s[i])
            else:
                if stack:
                    top = stack[-1]
                    # Check if they are matched
                    if top != brackets[s[i]]:
                        return False
                    else:
                        stack.pop()
                else:
                    return False
        
        return len(stack) == 0
            
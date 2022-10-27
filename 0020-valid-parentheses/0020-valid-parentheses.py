class Solution:
    def isValid(self, s: str) -> bool:
        paren_dict = {")": "(", "]": "[", "}": "{"}
        stack = []
        for i in range(len(s)):
            if s[i] in "([{":
                stack.append(s[i])
            else:
                if not stack or paren_dict[s[i]] != stack[-1]:
                    return False
                else:
                    stack.pop()
        return len(stack) == 0
"""
Time = O(n)
Space = O(n)
"""
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i] not in "+-*/":
                stack.append(int(tokens[i]))
            else:
                token2 = stack.pop()
                token1 = stack.pop()
                if tokens[i] == "+":
                    stack.append(token1 + token2)
                elif tokens[i] == "*":
                    stack.append(token1 * token2)
                elif tokens[i] == "-":
                    stack.append(token1 - token2)
                elif tokens[i] == "/":
                    stack.append(int(token1 / token2))
        return stack[0]
                    
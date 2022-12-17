"""
Time = O(n)
Space = O(n)
"""
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in "+-*/":
                opd2 = int(stack.pop())
                opd1 = int(stack.pop())
                if token == "+":
                    stack.append(opd1 + opd2)
                elif token =="-":
                    stack.append(opd1 - opd2)
                elif token == "*":
                    stack.append(opd1 * opd2)
                else:
                    stack.append(int(opd1 / opd2))
            else:
                stack.append(int(token))
        
        return stack[0]
            
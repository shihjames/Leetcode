"""
Time = O(n)
Space = O(n)
"""
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Create a stack
        stack = []
        # Traverse through the array
        for i in range(len(tokens)):
            # Operands
            if tokens[i] not in "+-*/":
                stack.append(int(tokens[i]))
            # Operator
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                if tokens[i] == "+":
                    stack.append(num1 + num2)
                elif tokens[i] == "-":
                    stack.append(num1 - num2)
                elif tokens[i] == "*":
                    stack.append(num1 * num2)
                elif tokens[i] == "/":
                    stack.append(int(num1 / num2))
        
        return stack[0]
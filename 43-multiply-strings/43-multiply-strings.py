class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1 = num1[::-1]
        num2 = num2[::-1]
        if int(num1) == 0 or int(num2) == 0:
            return "0"
        res = [0] * (len(num1) + len(num2))
        for i in range(len(num1)):
            for j in range(len(num2)):
                cur = int(num1[i]) * int(num2[j]) + res[i+j]
                res[i+j] = cur % 10
                res[i+j+1] += cur // 10
        if res[-1] == 0:
            res.pop()
        return "".join(str(num) for num in reversed(res))
                
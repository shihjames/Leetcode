class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        
        # traverse the list
        for i in range(len(temperatures)):
            cur_temp = temperatures[i]
            # Empty stack or not a warmer day
            if len(stack) == 0 or cur_temp <= stack[-1][0]:
                stack.append((cur_temp, i))
            # Found next warmer day
            else:
                while stack and stack[-1][0] < cur_temp:
                    prev_temp, index = stack.pop()
                    res[index] = i - index
                stack.append((cur_temp, i))
        
        return res
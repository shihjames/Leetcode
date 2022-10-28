class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)
        for index, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                prev_temp, prev_index = stack.pop()
                ans[prev_index] = index - prev_index
            stack.append((temp, index))
        return ans
                
                    
            
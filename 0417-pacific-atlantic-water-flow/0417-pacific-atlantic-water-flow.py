"""
Time = O(row*col)
Space = O(row*col)
"""
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def dfs(row, col, visited, prev_h):
            if (row, col) in visited or row < 0 or col < 0 or row >= rows or col >= cols or heights[row][col] < prev_h:
                return
            visited.add((row, col))
            for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                dfs(row+dr, col+dc, visited, heights[row][col])
        
        rows, cols = len(heights), len(heights[0])
        pacific, atlantic = set(), set()
        result = []
        
        for col in range(cols):
            dfs(0, col, pacific, heights[0][col])
            dfs(rows-1, col, atlantic, heights[rows-1][col])
            
        for row in range(rows):
            dfs(row, 0, pacific, heights[row][0])
            dfs(row, cols-1, atlantic, heights[row][cols-1])
        
        for row in range(rows):
            for col in range(cols):
                if (row, col) in pacific and (row, col) in atlantic:
                    result.append([row, col])
        return result
        
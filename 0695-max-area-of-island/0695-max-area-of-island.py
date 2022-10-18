"""
Time = O(n)
Space = O(n)
"""
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(row, col):
            if row < 0 or col < 0 or row >= rows or col >= cols or grid[row][col] == 0:
                return 0
            grid[row][col] = 0
            cur = 0
            for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                cur += dfs(row+dr, col+dc)
            return cur + 1
            
        
        rows, cols, mx_area = len(grid), len(grid[0]), 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    cur_area = dfs(row, col)
                    mx_area = max(mx_area, cur_area)
        
        return mx_area
                

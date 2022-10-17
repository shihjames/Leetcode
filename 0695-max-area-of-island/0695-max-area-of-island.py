"""
Time = O(n)
Space = O(n)
"""
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(i, j, count):
            if i < 0 or i > len(grid)-1 or j < 0 or j > len(grid[0])-1 or grid[i][j] == 0:
                return count-1
            grid[i][j] = 0
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                count = dfs(i+dx, j+dy, count+1)
            return count
        
        area = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    cur = dfs(row, col, 1)
                    area = max(area, cur)
        return area
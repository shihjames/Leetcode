class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(row, col, count):
            if row < 0 or col < 0 or row >= rows or col >= cols or grid[row][col] == 0:
                return count - 1
            grid[row][col] = 0
            for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                count = dfs(row+dr, col+dc, count+1)
            return count
            
        
        rows, cols, mx_area = len(grid), len(grid[0]), 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    cur_area = dfs(row, col, 1)
                    mx_area = max(mx_area, cur_area)
        
        return mx_area
                

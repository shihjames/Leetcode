class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(i, j, count):
            if i < 0 or i > len(grid)-1 or j < 0 or j > len(grid[0])-1:
                return count-1
            if grid[i][j] == 0:
                return count-1
            grid[i][j] = 0
            for x, y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                count = dfs(i+x, j+y, count+1)
            return count
        
        area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    cur = dfs(i, j, 1)
                    area = max(area, cur)
        return area
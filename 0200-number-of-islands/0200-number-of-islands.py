class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(row, col):
            if row < 0 or col < 0 or row >= rows or col >= cols or grid[row][col] == "0":
                return
            grid[row][col] = "0"
            for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                dfs(row + dr, col + dc)
            
        rows, cols = len(grid), len(grid[0])
        num_island = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    num_island += 1
                    dfs(row, col)
        
        return num_island
            
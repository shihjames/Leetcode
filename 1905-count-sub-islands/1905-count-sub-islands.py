class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def dfs(row, col, isSubIsland):
            if row < 0 or col < 0 or row >= rows or col >= cols or grid2[row][col] == 0:
                return isSubIsland
            grid2[row][col] = 0
            if grid1[row][col] == 0:
                isSubIsland = 0
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                if dfs(row + dr, col + dc, isSubIsland) == 0:
                    isSubIsland = 0
            return isSubIsland
        
        rows, cols = len(grid2), len(grid2[0])
        island_count = 0
        for row in range(rows):
            for col in range(cols):
                if grid2[row][col] == 1:
                    island_count += dfs(row, col, 1)
        return island_count
                    
                
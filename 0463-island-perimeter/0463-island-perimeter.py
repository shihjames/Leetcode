class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        perimeter = 0
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    perimeter += 4
                    if row > 0 and grid[row-1][col]:
                        perimeter -= 2
                    if col > 0 and grid[row][col-1]:
                        perimeter -= 2
        
        return perimeter

"""
Time = O(n)
Space = O(n)
"""
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def dfs(row, col):
            if (not (0 <= row < rows and 0 <= col < cols)) or grid[row][col] == 0:
                return 0
            
            # Prevent traversing to the visited element
            grid[row][col] = 0
            
            # 4 direction
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            
            area = 1
            # DFS for 4 direction
            for dr, dc in directions:
                area += dfs(row + dr, col + dc)
                
            return area
            
        max_area = 0
        rows, cols = len(grid), len(grid[0])
        # Traverse the grid
        for row in range(rows):
            for col in range(cols):
                # If found an island execute dfs
                if grid[row][col] == 1:
                    cur_area = dfs(row, col)
                    max_area = max(max_area, cur_area)
                    
        return max_area
                
        
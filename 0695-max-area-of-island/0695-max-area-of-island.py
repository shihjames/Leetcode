from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        max_area = 0
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    queue = deque([(row, col)])
                    cur_area = 0
                    while queue:
                        r, c = queue.popleft()
                        grid[r][c] = 0
                        cur_area += 1
                        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                            new_row, new_col = r + dr, c + dc
                            if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == 1:
                                grid[new_row][new_col] = 0
                                queue.append((new_row, new_col))
                    max_area = max(max_area, cur_area)
        return max_area
                    
        
#     def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
#         def dfs(row, col):
#             if row < 0 or col < 0 or row >= rows or col >= cols or grid[row][col] == 0:
#                 return 0
#             grid[row][col] = 0
#             area = 0
#             for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
#                 area += dfs(row+dr, col+dc)
#             return area + 1
            
#         rows = len(grid)
#         cols = len(grid[0])
#         max_area = 0
        
#         for row in range(rows):
#             for col in range(cols):
#                 if grid[row][col] == 1:
#                     cur_area = dfs(row, col)
#                     if cur_area > max_area:
#                         max_area = cur_area
#         return max_area
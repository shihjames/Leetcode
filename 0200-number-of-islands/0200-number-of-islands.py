class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        num_island = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    num_island += 1
                    grid[row][col] = "0"
                    queue = deque([(row, col)])
                    while queue:
                        r, c = queue.popleft()
                        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                            new_row, new_col = r + dr, c + dc
                            if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == "1":
                                grid[new_row][new_col] = "0"
                                queue.append((new_row, new_col))

        return num_island
        
#         def dfs(row, col):
#             if row < 0 or col < 0 or row >= rows or col >= cols or grid[row][col] == "0":
#                 return
#             grid[row][col] = "0"
#             for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
#                 dfs(row + dr, col + dc)
            
#         rows, cols = len(grid), len(grid[0])
#         num_island = 0
#         for row in range(rows):
#             for col in range(cols):
#                 if grid[row][col] == "1":
#                     num_island += 1
#                     dfs(row, col)
        
#         return num_island
            
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols, fresh = len(grid), len(grid[0]), 0
        queue = deque()
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    fresh += 1
                elif grid[row][col] == 2:
                    queue.append((row, col))
        
        if fresh == 0:
            return 0
        
        time = -1
        while queue:
            for i in range(len(queue)):
                row, col = queue.popleft()
                for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    new_row, new_col = row + dr, col + dc
                    if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == 1:
                        queue.append((new_row, new_col))
                        grid[new_row][new_col] = 2
                        fresh -= 1
            time += 1
        
        return time if fresh == 0 else -1
                    
        
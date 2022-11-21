"""
Time = O(rows * cols)
Space = O(max(rows, cols))
"""
from collections import deque
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        queue = deque([(entrance[0], entrance[1], 0)])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        rows, cols = len(maze), len(maze[0])
        maze[entrance[0]][entrance[1]] = "+"
        
        while queue:
            row, col, dis = queue.popleft()
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                # Valid move
                if 0 <= new_row < rows and 0 <= new_col < cols and maze[new_row][new_col] == ".":
                    # Return if reach exit
                    if new_row == 0 or new_row == rows - 1 or new_col == 0 or new_col == cols - 1:
                        return dis + 1
                    # Mark as visited
                    maze[new_row][new_col] = "+"
                    # Add position to queue
                    queue.append((new_row, new_col, dis+1))
        return -1
                    
                    
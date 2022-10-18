"""
Time = O(n)
Spce = O(n)
"""

from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    count += 1
                    grid[row][col] = "0"
                    queue = deque([(row, col)])
                    while queue:
                        r, c = queue.popleft()
                        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                            if 0 <= r+dr < len(grid) and 0 <= c+dc < len(grid[0]) and grid[r+dr][c+dc] == "1":
                                grid[r+dr][c+dc] = "0"
                                queue.append((r+dr, c+dc))
        return count
                    
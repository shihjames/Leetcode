"""
Time = O(n)
Space = O(n)
"""

from collections import deque
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        queue = deque()
        rows, cols = len(rooms), len(rooms[0])
        for row in range(rows):
            for col in range(cols):
                if rooms[row][col] == 0:
                    queue.append((row, col, 0))
        
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while queue:
            for i in range(len(queue)):
                row, col, dis = queue.popleft()
                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc
                    if 0 <= new_row < rows and 0 <= new_col < cols and rooms[new_row][new_col] == 2**31-1:
                        queue.append((new_row, new_col, dis+1))
                        rooms[new_row][new_col] = dis + 1
        
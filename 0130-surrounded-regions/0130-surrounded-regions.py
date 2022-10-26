class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols or board[row][col] != "O":
                return
            board[row][col] = "*"
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dr, dc in directions:
                dfs(row + dr, col + dc)
            
        rows, cols = len(board), len(board[0])
        borders = []
        for row in range(rows):
            for col in range(cols):
                if row == 0 or col == 0 or row == rows-1 or col == cols-1:
                    borders.append((row, col))
        
        for row, col in borders:
            dfs(row, col)
        
        for row in range(rows):
            for col in range(cols):
                if board[row][col] != "*":
                    board[row][col] = "X"
                else:
                    board[row][col] = "O"
        
                    
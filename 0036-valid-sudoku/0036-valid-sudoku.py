class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols = len(board), len(board[0])
        
        for row in range(rows):
            row_set = set()
            for col in range(cols):
                if board[row][col] != ".":
                    if board[row][col] in row_set:
                        return False
                    row_set.add(board[row][col])
        
        print("row")
        
        for col in range(cols):
            col_set = set()
            for row in range(rows):
                if board[row][col] != ".":
                    if board[row][col] in col_set:
                        return False
                    col_set.add(board[row][col])
        
        print("col")
                
        for row in range(0, rows, 3):
            for col in range(0, cols, 3):
                box_set = set()
                for dr in range(3):
                    for dc in range(3):
                        if board[row+dr][col+dc] != ".":
                            if board[row+dr][col+dc] in box_set:
                                return False
                            box_set.add(board[row+dr][col+dc])
        
        print("box")
        
        return True
                
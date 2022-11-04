from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        1. Create three kind of sets (row, column, box)
        2. Traverse the board one by one
        3. Check if the current number is already in the sets
        """
        
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)
        
        for row in range(9):
            for col in range(9):
                cur = board[row][col]
                if cur != ".":
                    # Check row set
                    if cur in rows[row]:
                        return False
                    # Check col set
                    if cur in cols[col]:
                        return False
                    # Check box set
                    if cur in boxes[(row // 3, col // 3)]:
                        return False
                    rows[row].add(cur)
                    cols[col].add(cur)
                    boxes[(row // 3, col // 3)].add(cur)
                
        return True
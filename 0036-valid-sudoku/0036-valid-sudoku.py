"""
Time = O(n**2)
Space = O(n**2)
"""
from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
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
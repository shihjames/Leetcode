class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols = len(board), len(board[0])
        row_dic = defaultdict(set)
        col_dic = defaultdict(set)
        box_dic = defaultdict(set)
        
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == ".":
                    continue
                    
                if board[row][col] in row_dic[row] or board[row][col] in col_dic[col] or board[row][col] in box_dic[(row // 3, col // 3)]:
                    return False
                
                row_dic[row].add(board[row][col])
                col_dic[col].add(board[row][col])
                box_dic[(row // 3, col // 3)].add(board[row][col])
                
        return True
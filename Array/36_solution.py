class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check_row(lst):
            s = set()
            for val in lst:
                if val in s:
                    return False
                if val != ".":
                    s.add(val)
            return True
        
        def check_column(board):
            s = set()
            for row in range(9):
                for col in range(9):
                    if board[col][row] in s:
                        return False
                    if board[col][row] != ".":
                        s.add(board[col][row])
                s = set()
            return True
        
        def check_square(board, x, y):
            s = set()
            for row in range(y, y + 3):
                for col in range(x, x + 3):
                    if board[row][col] in s:
                        return False
                    if board[row][col] != ".":
                        s.add(board[row][col])
            return True
        
        # Check row
        for lst in board:
            if not check_row(lst):
                return False
        
        # Check Column
        if not check_column(board):
            return False

        # Check square
        for x in range(0, 7, 3):
            for y in range(0, 7, 3):
                if not check_square(board, x, y):
                    return False
        
        return True

"""
Time Complexity = O(n^3)
Space Complexity = O(n)

Works on Leetcode
"""
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check in each row
        for i in range(len(board)):
            row = set()
            for j in range(len(board[0])):
                if board[i][j] != ".":
                    if int(board[i][j]) in row:
                        return False
                    row.add(int(board[i][j]))
        #check in each column
        for j in range(len(board[0])):
            column = set()
            for i in range(len(board)):
                if board[i][j] != ".":
                    if int(board[i][j]) in column:
                        return False
                    column.add(int(board[i][j]))

        
        #check in block level
        for block in range(0, 9):
            miniSudoku = set()
            for i in range(int(block/3)*3, (int(block/3)*3)+3):
                for j in range((block%3)*3, ((block%3)*3)+3):
                    if board[i][j] != ".":
                        if int(board[i][j]) in miniSudoku:
                            return False
                        miniSudoku.add(int(board[i][j]))
        return True
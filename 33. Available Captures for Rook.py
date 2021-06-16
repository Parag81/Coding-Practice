"""
On an 8 x 8 chessboard, there is exactly one white rook 'R' and some number of white bishops 'B', black pawns 'p', and empty squares '.'.

When the rook moves, it chooses one of four cardinal directions (north, east, south, or west), then moves in that direction until it chooses to stop, reaches the edge of the board, captures a black pawn, or is blocked by a white bishop. A rook is considered attacking a pawn if the rook can capture the pawn on the rook's turn. The number of available captures for the white rook is the number of pawns that the rook is attacking.

Return the number of available captures for the white rook.

 

Example 1:


Input: board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
Output: 3
Explanation: In this example, the rook is attacking all the pawns.
"""

def numRookCaptures(self, board):
        captures = 0
        row = -1
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    row, col = i, j
                    break
            if row == i:
                break
        for i in range(row,-1,-1):
            if board[i][col] == 'p':
                captures += 1
                break
            elif board[i][col] == 'B':
                break
        for i in range(col,-1,-1):
            if board[row][i] == 'p':
                captures += 1
                break
            elif board[row][i] == 'B':
                break
        for i in range(row, 8):
            if board[i][col] == 'p':
                captures += 1
                break
            elif board[i][col] == 'B':
                break
        for i in range(col, 8):
            if board[row][i] == 'p':
                captures += 1
                break
            elif board[row][i] == 'B':
                break
        return captures
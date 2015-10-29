class Solution:
    # @param {character[][]} board
    # @return {boolean}
    def isValidSudoku(self, board):
        def is_valid(i, j):
            val = board[i][j]
            board[i][j] = '.'
            for k in xrange(9):
                if(board[i][k]==val or board[k][j]==val or board[(i/3)*3+k/3][(j/3)*3+k%3]==val):
                    board[i][j] = val
                    return False
            board[i][j] = val
            return True
        
        for i in xrange(9):
            for j in xrange(9):
                if '1'<=board[i][j]<='9' and not is_valid(i, j):
                    return False
        return True

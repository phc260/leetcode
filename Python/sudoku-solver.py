class Solution:
    # @param {character[][]} board
    # @return {void} Do not return anything, modify board in-place instead.
    def solveSudoku(self, board):
        def is_valid(i, j):
            val = board[i][j]
            board[i][j] = '.'
            for k in xrange(9):
                if(board[i][k]==val or board[k][j]==val or board[(i/3)*3+k/3][(j/3)*3+k%3]==val):
                    board[i][j] = val
                    return False
            board[i][j] = val
            return True
        
            
        def DFS(board):
            for i in xrange(9):
                for j in xrange(9):
                    if board[i][j]=='.':
                        for k in '123456789':
                            board[i][j] = k
                            if is_valid(i, j) and DFS(board):
                                return True
                        board[i][j] = '.'
                        return False
            return True
        DFS(board)

class Solution:
    # @param {character[][]} board
    # @return {void} Do not return anything, modify board in-place instead.
    def solve(self, board):
        if len(board)<3 or len(board[0])<3:
            return
        
        r = len(board)
        c = len(board[0])
        stk = []
        
        for i in xrange(r):
            if board[i][0]=='O': stk.append((i, 0))
            if board[i][c-1]=='O': stk.append((i, c-1))
            
        for i in xrange(c):
            if board[0][i]=='O': stk.append((0, i))
            if board[r-1][i]=='O': stk.append((r-1, i))
        
        while stk:
            i, j = stk.pop()
            board[i][j] = '@'
            if i>0 and board[i-1][j]=='O': stk.append((i-1, j))
            if i+1<r and board[i+1][j]=='O': stk.append((i+1, j))
            if j>0 and board[i][j-1]=='O': stk.append((i, j-1))
            if j+1<c and board[i][j+1]=='O': stk.append((i, j+1))
            
        for i in xrange(r):
            for j in xrange(c):
                if board[i][j]=='O': board[i][j] = 'X'
                if board[i][j]=='@': board[i][j] = 'O'

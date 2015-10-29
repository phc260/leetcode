class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        r = len(board)
        c = len(board[0])
        
        def DFS(board, word, i, x, y):
            if i>=len(word):
                return True
            if 0<=x<r and 0<=y<c and board[x][y]==word[i]:
                t = board[x][y]
                board[x][y] = '@'
                if (DFS(board, word, i+1, x-1, y)
                    or DFS(board, word, i+1, x+1, y)
                    or DFS(board, word, i+1, x, y-1)
                    or DFS(board, word, i+1, x, y+1)):
                    return True
                board[x][y] = t
            return False
            
            
        for i in xrange(r):
            for j in xrange(c):
                if DFS(board, word, 0, i, j):
                    return True

        return False
class Solution:
    # @param {integer} n
    # @return {integer}
    def __init__(self):
        self.ans = 0
    def totalNQueens(self, n):
        # place kth queen in column c
        def can_place(k, c):
            for i in xrange(k):
                if board[i]==c or abs(k-i)==abs(board[i]-c):
                    return False
            return True

        def DFS(i):
            if i>=n:
                self.ans += 1
                return
            for j in xrange(n):
                if can_place(i, j):
                    board[i] = j
                    DFS(i+1)

        self.ans = 0
        board = [-1]*n
        DFS(0)
        return self.ans

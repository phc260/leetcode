class Solution:
    # @return a list of lists of string
    def solveNQueens(self, n):
        
        # place kth queen in column c
        def can_place(k, c):
            for i in xrange(k):
                if board[i]==c or abs(k-i)==abs(board[i]-c):
                    return False
            return True
        
        def DFS(i, partial_list=[]):
            if i>=n:
                ans.append(partial_list)
                return
            for j in xrange(n):
                if can_place(i, j):
                    board[i] = j
                    DFS(i+1, partial_list+['.'*j+'Q'+'.'*(n-j-1)])
                    
        board = [-1]*n
        ans = []
        DFS(0)
        return ans

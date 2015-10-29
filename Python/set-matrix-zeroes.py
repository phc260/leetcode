class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        
        row = [0]*m
        col = [0]*n
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    row[i] = col[j] = 1
                    
        for i in range(m):
            for j in range(n):
                if row[i] or col[j]:
                    matrix[i][j] = 0
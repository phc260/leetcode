class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        n = len(matrix)
        layer = n/2
        for i in range(layer):
            for j in range(i, n-i-1):
                t = matrix[i][j]
                # lower-left to upper-left
                matrix[i][j] = matrix[n-1-j][i]
                # lower-right to lower-left
                matrix[n-1-j][i] = matrix[n-1-i][n-1-j]
                # upper-right to lower-right
                matrix[n-1-i][n-1-j]= matrix[j][n-1-i]
                # upper-left to upper-right
                matrix[j][n-1-i] = t
                
        return matrix
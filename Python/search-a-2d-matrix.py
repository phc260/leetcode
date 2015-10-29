class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        m = len(matrix)
        n = len(matrix[0])
		
        for i in range(m):
            if matrix[i][0]==target: return True
            if matrix[i][n-1]==target: return True
            
            if matrix[i][0]>target: return False
        
            if matrix[i][0]<target and matrix[i][n-1]>target:
                for j in range(1,n-1):
                    if matrix[i][j]==target: return True
                return False
            
        return False

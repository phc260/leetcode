class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        r = len(triangle)
        
        for i in xrange(1, r):
            c = len(triangle[i])
            triangle[i][0] += triangle[i-1][0]
            
            for j in range(1, c-1):
                triangle[i][j] += min(triangle[i-1][j-1], triangle[i-1][j])
                
            triangle[i][c-1] += triangle[i-1][c-2]
            
        return min(triangle[r-1])

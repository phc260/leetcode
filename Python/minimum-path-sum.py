class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        r = len(grid)
        c = len(grid[0])
        
        for i in xrange(1, r): grid[i][0] += grid[i-1][0]
        for i in xrange(1, c): grid[0][i] += grid[0][i-1]
        
        for i in xrange(1, r):
            for j in xrange(1, c):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        
        return grid[r-1][c-1]
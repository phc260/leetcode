class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        dp = [[0]*(n+1) for i in xrange(m+1)]
        dp[m-1][n] = 1
        for i in xrange(m-1,-1,-1):
            for j in xrange(n-1,-1,-1):
                dp[i][j] = dp[i+1][j]+dp[i][j+1] if obstacleGrid[i][j]==0 else 0
                
        return dp[0][0]
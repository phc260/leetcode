class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        dp = [1] + [0]*(n-1)
        for i in xrange(m):
            for j in xrange(1, n):
                dp[j] += dp[j-1]
                
        return dp[n-1]
class Solution:
    # @param {string} s
    # @param {string} t
    # @return {integer}
    """
    def numDistinct(self, s, t):
        m = len(s)
        n = len(t)
        dp = [[0]*(n+1) for i in xrange(m+1)]
        for i in xrange(m+1): dp[i][0] = 1
        for i in xrange(m):
            for j in xrange(n):
                dp[i+1][j+1] = dp[i][j+1]
                if s[i]==t[j]: dp[i+1][j+1] += dp[i][j]
        return dp[m][n]
    """
    def numDistinct(self, s, t):
        m = len(s)
        n = len(t)
        dp = [1]+[0]*n
        for i in xrange(m):
            dp_j = dp[0]
            for j in xrange(n):
                dp_j_plus_1 = dp[j+1]
                if s[i]==t[j]: dp[j+1] += dp_j
                dp_j = dp_j_plus_1
        return dp[n]

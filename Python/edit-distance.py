class Solution:
    # @param {string} word1
    # @param {string} word2
    # @return {integer}
    def minDistance(self, wordp1, wordp2):
        
        m = len(wordp1)+1
        n = len(wordp2)+1
        
        dp = [[0]*n for i in xrange(m)]
        
        for i in xrange(1,m): dp[i][0] = i
        for j in xrange(1,n): dp[0][j] = j
        
        for i in xrange(1,m):
            for j in xrange(1,n):
                dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+(0 if wordp1[i-1]==wordp2[j-1] else 1))
                
        return dp[m-1][n-1]

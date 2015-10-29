class Solution:
    # @param {string} s1
    # @param {string} s2
    # @param {string} s3
    # @return {boolean}
    def isInterleave(self, s1, s2, s3):
        n1 = len(s1)
        n2 = len(s2)
        n3 = len(s3)
        if n1+n2!=n3: return False

        dp =[[False]*(n2+1) for i in xrange(n1+1)]
        dp[0][0] = True
        for i in xrange(n1):
            dp[i+1][0] = dp[i][0] and s1[i]==s3[i]
        for i in xrange(n2):
            dp[0][i+1] = dp[0][i] and s2[i]==s3[i]
        
        for i in xrange(n1):
            for j in xrange(n2):
                dp[i+1][j+1] = (dp[i][j+1] and s1[i]==s3[i+j+1]) or (dp[i+1][j] and s2[j]==s3[i+j+1])
        return dp[n1][n2]

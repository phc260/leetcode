class Solution:
    # @param {string} s
    # @param {string} p
    # @return {boolean}
    def isMatch(self, s, p):
        dp = [[False]*(len(p)+1) for j in xrange(len(s)+1)]
        dp[0][0] = True
        for i in xrange(len(p)):
            if i>0 and p[i]=='*':
                dp[0][i+1]=dp[0][i-1]
        for i in xrange(len(s)):
            for j in xrange(len(p)):
                if p[j]=='.': dp[i+1][j+1]=dp[i][j]
                elif p[j]=='*': dp[i+1][j+1]=dp[i+1][j] or dp[i+1][j-1] or (dp[i][j+1] and (s[i]==p[j-1] or p[j-1]=='.'))
                else: dp[i+1][j+1]=dp[i][j] and s[i]==p[j]
        return dp[len(s)][len(p)]

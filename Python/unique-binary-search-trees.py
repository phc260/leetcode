class Solution:
    # @return an integer
    def numTrees(self, n):
        count = [1]*2 + [0]*(n-1)
        for i in xrange(2,n+1):
            for j in xrange(i):
                count[i] += count[j]*count[i-j-1];
                
        return count[n]
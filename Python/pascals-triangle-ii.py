class Solution:
    # @param {integer} rowIndex
    # @return {integer[]}
    def getRow(self, rowIndex):
        ans = [1]*(rowIndex+1)
        for i in xrange(1, rowIndex+1):
            ans[i] = ans[i-1]*(rowIndex+1-i)/i
        return ans

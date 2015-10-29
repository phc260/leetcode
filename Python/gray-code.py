class Solution:
    # @return a list of integers
    def grayCode(self, n):
        ans = [0]
        for i in xrange(n):
            for j in xrange(len(ans)-1, -1, -1):
                ans.append(ans[j] + (1<<i))
        return ans
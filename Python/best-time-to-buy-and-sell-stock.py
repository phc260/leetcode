INT_MAX = 2147483647
class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        
        maxp = 0
        low = INT_MAX
        
        for i in xrange(len(prices)):
            low = min(low, prices[i])
            maxp = max(maxp, prices[i] - low)
            
        return maxp
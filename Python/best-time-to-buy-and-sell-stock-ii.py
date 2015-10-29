class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        
        maxp = 0
        
        for i in xrange(1, len(prices)):
            if prices[i]>prices[i-1]:
                maxp += (prices[i]-prices[i-1])
            
        return maxp
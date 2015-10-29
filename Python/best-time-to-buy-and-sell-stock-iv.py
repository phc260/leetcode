class Solution:
    # @param {integer} k
    # @param {integer[]} prices
    # @return {integer}
    
    # Best Time to Buy and Sell Stock II
    def maxProfit2(self, prices):
        
        maxp = 0
        for i in xrange(1, len(prices)):
            if prices[i]>prices[i-1]:
                maxp += (prices[i]-prices[i-1])
            
        return maxp
    
    def maxProfit(self, k, prices):
        if k>len(prices):
            return self.maxProfit2(prices)
        
        local = [0]*(k+1)
        glob = [0]*(k+1)
        
        for i in xrange(len(prices)-1):
            incr = prices[i+1] - prices[i]
            
            j = k
            while j>0:
                local[j] = max(glob[j-1]+max(incr, 0), local[j]+incr)
                glob[j] = max(glob[j], local[j])
                j -= 1
        
        return glob[k]

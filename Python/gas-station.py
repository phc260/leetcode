class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        
        n = len(gas)
        total = end_sum = 0
        end = -1
        
        for i in xrange(n):
            total += gas[i]-cost[i]
            end_sum += gas[i]-cost[i]
            
            if end_sum<0:
                end_sum = 0
                end = i
                
        return end+1 if total>=0 else -1
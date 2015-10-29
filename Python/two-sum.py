class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        d = {}
        for i in xrange(len(num)):
            d[num[i]] = i
        
        for i in xrange(len(num)):
            val = target-num[i]
            if val in d and i<d[val]:
                    return (i+1, d[val]+1)
                
        return (0, 0)

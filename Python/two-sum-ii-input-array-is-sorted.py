class Solution:
    # @param {integer[]} numbers
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, numbers, target):
        d = {}
        for i in xrange(len(numbers)):
            d[numbers[i]] = i
        
        for i in xrange(len(numbers)):
            val = target-numbers[i]
            if val in d and i!=d[val]:
                return [i+1, d[val]+1]
        return [0, 0]
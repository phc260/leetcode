class Solution:
    # @param num, a list of integer
    # @return an integer
    def findPeakElement(self, num):
        
        max_idx = 0
        max_val = num[max_idx]
        
        for i in xrange(1, len(num)):
            if num[i]>max_val:
                max_val = num[i]
                max_idx = i
                
        return max_idx
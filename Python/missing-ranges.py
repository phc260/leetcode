class Solution:
    # @param A, a list of integers
    # @param lower, an integer
    # @param upper, an integer
    # @return a list of strings
    def findMissingRanges(self, A, lower, upper):
        def get_range(start, end):
            return str(start)+'->'+str(end) if start<end else str(start)
        n = len(A)
        ans = []
        
        prev = lower-1
        
        for i in xrange(n+1):
            curr = A[i] if i!=n else upper+1
            
            if curr-prev>1:
                ans.append(get_range(prev+1, curr-1))
            prev = curr
        
        return ans

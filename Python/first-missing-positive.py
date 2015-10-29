class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        n = len(A)
        i=0
        while i<n:
        	if A[i]!=i+1 and 0<A[i]<=n and A[i]!=A[A[i]-1]:
        		j = A[i]-1
        		A[i], A[j] = A[j], A[i]
        	else:
        	    i += 1
        
        for i in xrange(n):
            if A[i]!=i+1:
                return i+1
        return n+1
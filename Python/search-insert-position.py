class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        n = len(A)
        for i in xrange(n):
            if target<=A[i]:
                return i;
                
        return n
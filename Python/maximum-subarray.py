class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        S = 0
        M = A[0]
        
        for i in A:
            S += i
            if S>M: M = S
            if S<0: S = 0
        return M
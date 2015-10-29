class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        n = len(A)
        jump = [0]*n
        
        for i in range(1, n):
            jump[i] = max(jump[i-1], A[i-1]) -1
            
            if jump[i]<0:
                return False
        
        return jump[n-1]>=0
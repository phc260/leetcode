class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        n = len(A)
        left = [0] * n
        right = [0] * n
        
        water = 0
        
        for i in range(1, n):
            left[i] = max(left[i-1], A[i-1])
            
        for i in range(n-2, -1, -1):
            right[i] = max(right[i+1], A[i+1])
            
        for i in range(n):
            v = min(left[i], right[i]) - A[i]
            if v>0:
                water += v
            
        return water

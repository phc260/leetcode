class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing(void)
    def merge(self, A, m, B, n):
        T = A[:]
        
        i = j = k = 0
        
        while k<m and j<n:
            if T[k] < B[j]:
                A[i] = T[k]
                k += 1
            else:
                A[i] = B[j]
                j += 1
                
            i += 1
        
        while k<m:
            A[i] = T[k]
            i += 1
            k += 1
            
        while j<n:
            A[i] = B[j]
            i += 1
            j += 1
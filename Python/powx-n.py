class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float

        
    def pow(self, x, n):
        
        def power(x, n):
            if n==0: return 1.0
            v = power(x, n/2)
            return v*v if n%2==0 else v*v*x
        ###################################

        return power(x, n) if n>=0 else 1/power(x, -n)

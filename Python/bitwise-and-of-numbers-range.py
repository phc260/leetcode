class Solution:
    # @param m, an integer
    # @param n, an integer
    # @return an integer
    def rangeBitwiseAnd(self, m, n):
        x = m^n
        s = x>>1
        while s:
            x |= s
            s >>= 1
        return m&n&~x
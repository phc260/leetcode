class Solution:
    # @return an integer
    def trailingZeroes(self, n):
        return n/5+self.trailingZeroes(n/5) if n else 0
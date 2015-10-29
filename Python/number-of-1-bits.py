class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        count = 0
        while n:
            n &= (n-1)
            count += 1
        return count

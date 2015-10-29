class Solution:
    # @return an integer
    def reverse(self, x):
        y = str(abs(x))
        y = y[::-1]
        return int(y) if x>=0 else -int(y)
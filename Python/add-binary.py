class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        x = int(a, base=2)
        y = int(b, base=2)
        
        return '{:b}'.format(x+y)
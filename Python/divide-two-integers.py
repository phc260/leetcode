INT_MAX = 2147483647
INT_MIN = -2147483648
class Solution:
    # @param {integer} dividend
    # @param {integer} divisor
    # @return {integer}
    def divide(self, dividend, divisor):
        if divisor==0: return INT_MAX
        if dividend==0: return 0
        if dividend==INT_MIN and divisor==-1: return INT_MAX
        
        ret = 0
        dvd = abs(dividend)
        dvs = abs(divisor)
        
        while dvd>=dvs:
            i = 0
            a = dvs
            while a<=dvd:
                a <<= 1
                i += 1
            
            ret += (1<<(i-1))
            dvd -= (dvs<<(i-1))
            
        
        return -ret if (dividend<0) ^ (divisor<0) else ret 

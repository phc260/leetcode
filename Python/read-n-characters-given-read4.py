# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution:
    # @param buf, Destination buffer (a list of characters)
    # @param n,   Maximum number of characters to read (an integer)
    # @return     The number of characters read (an integer)
    def read(self, buf, n):
        
        total = 0
        bytes = 4
        while bytes==4:
            buf4 = ['']*4
            bytes = read4(buf4)
            bytes = min(bytes, n-total)
            buf[total:bytes] = buf4[:bytes]
            total += bytes
        return total
